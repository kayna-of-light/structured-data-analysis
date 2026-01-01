"""Batch Azure OpenAI analysis for spontaneous remission case datasets.

This script iterates over every JSON record in the data directories,
calls Azure OpenAI with the structured questionnaire schema, and saves
the results under output/analysis.

Usage:
    python analyze_cases.py --max-concurrency 4 --log-level INFO
    python analyze_cases.py --datasets radicalremission --limit 25 --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from functools import partial
from typing import Any, Dict, List, Mapping, Optional, Sequence
from urllib.parse import urlsplit, urlunsplit

from dotenv import dotenv_values
from openai import APIStatusError, OpenAI, OpenAIError, RateLimitError
from pydantic import ValidationError

from models import RemissionAnalysisResponse

ROOT = Path(__file__).parent
DATA_ROOT = ROOT / "data"
OUTPUT_ROOT = ROOT / "output"
ANALYSIS_DIR = OUTPUT_ROOT / "analysis"
DEFAULT_SECRETS = ROOT / "secrets" / "azure_openai.env"
DEFAULT_API_VERSION = "2024-05-01-preview"

# Supported dataset directories
SUPPORTED_DATASETS = (
    "radicalremission",
    "ions",
    "lourdes",
    "pubmed",
    "nderf_healing",
    "healthtalk",
)

SYSTEM_PROMPT = (
    "You are an expert researcher who analyzes spontaneous remission and radical healing case narratives "
    "according to the detailed questionnaire schema provided via structured output. "
    "Your goal is to extract both medical 'ground truth' (diagnosis, treatment, outcome) and "
    "psycho-spiritual factors (Turner's 9 factors, existential shifts, anomalous experiences). "
    "Ground every answer strictly in the supplied testimony. If the narrative omits a "
    "detail, mark the corresponding enum as not_mentioned or use empty lists. Only capture "
    "quotes or free-text details that are explicitly present."
)


@dataclass(slots=True)
class CaseJob:
    """Represents a single case to be analyzed."""
    dataset: str
    source_path: Path
    target_path: Path


def _read_json(path: Path) -> Mapping[str, object]:
    """Read JSON file and return contents."""
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_user_prompt(
    *,
    title: str,
    date: Optional[str],
    dataset: str,
    source_url: Optional[str],
    content: str,
) -> str:
    """Build the user prompt for case analysis."""
    header_lines = [
        f"Dataset: {dataset}",
        f"Title: {title.strip() or 'Untitled Case'}",
    ]
    if date:
        header_lines.append(f"Reported date: {date}")
    if source_url:
        header_lines.append(f"Source URL: {source_url}")
    header_lines.append("Case Narrative:")
    header_lines.append(content.strip())
    header_lines.append(
        "\nAnalyze this remission case according to the structured questionnaire. "
        "Extract medical details, identify which of Turner's 9 factors are present, "
        "note any anomalous experiences (NDE/STE), and assess the validation tier."
    )
    return "\n\n".join(header_lines)


def collect_jobs(datasets: Sequence[str], *, limit: Optional[int]) -> List[CaseJob]:
    """Collect all case files to be analyzed."""
    jobs: List[CaseJob] = []
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    
    for dataset in datasets:
        source_dir = DATA_ROOT / dataset
        if not source_dir.exists():
            logging.warning("Skipping dataset %s because %s is missing", dataset, source_dir)
            continue
        for path in sorted(source_dir.glob("*.json")):
            target_name = f"{dataset}-{path.name}"
            jobs.append(
                CaseJob(
                    dataset=dataset,
                    source_path=path,
                    target_path=ANALYSIS_DIR / target_name,
                )
            )
    
    if limit is not None and limit >= 0:
        jobs = jobs[:limit]
    return jobs


def load_azure_credentials(config_path: Path) -> Dict[str, str]:
    """Load Azure OpenAI credentials from env file."""
    if not config_path.exists():
        raise FileNotFoundError(
            f"Azure credentials not found at {config_path}. "
            f"Copy secrets/azure_openai.env.example to secrets/azure_openai.env "
            f"and fill in your values."
        )
    return dict(dotenv_values(config_path))


async def request_analysis(
    client: OpenAI,
    *,
    model: str,
    prompt: str,
    temperature: float,
    max_output_tokens: int,
    retries: int = 3,
) -> tuple[dict, dict, str]:
    """
    Call Azure OpenAI with structured output and return the parsed analysis.
    
    Returns:
        Tuple of (analysis_dict, usage_dict, response_id)
    """
    for attempt in range(1, retries + 1):
        try:
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                partial(
                    client.beta.chat.completions.parse,
                    model=model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    response_format=RemissionAnalysisResponse,
                    temperature=temperature,
                    max_tokens=max_output_tokens,
                ),
            )
            
            message = response.choices[0].message
            if message.refusal:
                raise ValueError(f"Model refused: {message.refusal}")
            if message.parsed is None:
                raise ValueError("No structured output returned")
            
            return (
                message.parsed.model_dump(),
                response.usage.model_dump() if response.usage else {},
                response.id,
            )
            
        except RateLimitError as exc:
            wait_time = 2 ** attempt + random.random()
            logging.warning(
                "Rate limited (attempt %d/%d), waiting %.1fs: %s",
                attempt, retries, wait_time, exc
            )
            await asyncio.sleep(wait_time)
            
        except APIStatusError as exc:
            logging.error("API error: %s", exc)
            raise
            
    raise RuntimeError(f"Failed after {retries} retries")


async def process_job(
    job: CaseJob,
    *,
    client: Optional[OpenAI],
    model: str,
    temperature: float,
    max_output_tokens: int,
    semaphore: asyncio.Semaphore,
    overwrite: bool,
    dry_run: bool,
) -> str:
    """Process a single case job."""
    
    if job.target_path.exists() and not overwrite:
        logging.debug("Skipping %s (already exists)", job.source_path)
        return "skipped"
    
    try:
        raw_data = _read_json(job.source_path)
    except (json.JSONDecodeError, IOError) as exc:
        logging.error("Failed to read %s: %s", job.source_path, exc)
        return "error"
    
    # Extract fields from raw data (adapt based on your scraper output format)
    title = str(raw_data.get("title", ""))
    date = raw_data.get("date") or raw_data.get("reported_date")
    source_url = raw_data.get("source_url") or raw_data.get("url")
    content = raw_data.get("content") or raw_data.get("narrative") or raw_data.get("text", "")
    
    if not content:
        logging.warning("No content in %s; skipping", job.source_path)
        return "empty"
    
    prompt = build_user_prompt(
        title=title,
        date=date,
        dataset=job.dataset,
        source_url=source_url,
        content=content,
    )
    
    checksum = sha256(content.encode("utf-8")).hexdigest()
    
    if dry_run:
        logging.info("Dry-run: would analyze %s", job.source_path)
        return "dry_run"
    
    if client is None:
        raise RuntimeError("Azure OpenAI client is required when not running with --dry-run.")
    
    async with semaphore:
        try:
            analysis, usage, response_id = await request_analysis(
                client,
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            )
            
            output_data = {
                "metadata": {
                    "source_path": str(job.source_path),
                    "dataset": job.dataset,
                    "title": title,
                    "source_url": source_url,
                    "content_checksum": checksum,
                    "analyzed_at": datetime.now(timezone.utc).isoformat(),
                    "azure_response_id": response_id,
                },
                "usage": usage,
                "analysis": analysis,
            }
            
            job.target_path.parent.mkdir(parents=True, exist_ok=True)
            with job.target_path.open("w", encoding="utf-8") as fh:
                json.dump(output_data, fh, indent=2, ensure_ascii=False)
            
            logging.info("Analyzed %s -> %s", job.source_path.name, job.target_path.name)
            return "success"
            
        except Exception as exc:
            logging.error("Failed to analyze %s: %s", job.source_path, exc)
            return "error"


async def run_pipeline(args: argparse.Namespace) -> Dict[str, int]:
    """Run the analysis pipeline."""
    jobs = collect_jobs(args.datasets, limit=args.limit)
    
    if not jobs:
        logging.info("No jobs to process.")
        return {}
    
    logging.info("Collected %d jobs to process.", len(jobs))
    
    client: Optional[OpenAI] = None
    model = args.model
    
    if not args.dry_run:
        creds = load_azure_credentials(Path(args.secrets_path))
        endpoint = creds.get("AZURE_OPENAI_ENDPOINT", "")
        api_key = creds.get("AZURE_OPENAI_API_KEY", "")
        deployment = args.model or creds.get("AZURE_OPENAI_DEPLOYMENT", "")
        api_version = creds.get("AZURE_OPENAI_API_VERSION", DEFAULT_API_VERSION)
        
        if not all([endpoint, api_key, deployment]):
            raise ValueError("Missing Azure OpenAI credentials in env file.")
        
        # Normalize endpoint
        parts = urlsplit(endpoint)
        base_url = urlunsplit((parts.scheme, parts.netloc, "", "", ""))
        
        client = OpenAI(
            api_key=api_key,
            base_url=f"{base_url}/openai/deployments/{deployment}",
            default_query={"api-version": api_version},
        )
        model = deployment
    
    semaphore = asyncio.Semaphore(args.max_concurrency)
    
    tasks = [
        process_job(
            job,
            client=client,
            model=model,
            temperature=args.temperature,
            max_output_tokens=args.max_output_tokens,
            semaphore=semaphore,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
        for job in jobs
    ]
    
    results = await asyncio.gather(*tasks)
    
    stats: Dict[str, int] = {}
    for result in results:
        stats[result] = stats.get(result, 0) + 1
    
    return stats


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description="Batch Azure OpenAI analysis for spontaneous remission case datasets.",
    )
    parser.add_argument(
        "--datasets",
        nargs="+",
        default=list(SUPPORTED_DATASETS),
        choices=list(SUPPORTED_DATASETS),
        help="Datasets to process (default: all).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional cap on how many files to process across all datasets.",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=4,
        help="Maximum number of concurrent Azure OpenAI calls.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature for the model (default: 0.7).",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=10000,
        help="Upper bound for structured response tokens.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Override the Azure OpenAI deployment name (defaults to env file).",
    )
    parser.add_argument(
        "--secrets-path",
        type=str,
        default=str(DEFAULT_SECRETS),
        help="Path to the azure_openai.env file.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-run analysis even if the target JSON already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List which files would be analyzed without calling Azure OpenAI.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging verbosity level.",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="[%(levelname)s] %(message)s"
    )
    
    try:
        stats = asyncio.run(run_pipeline(args))
    except KeyboardInterrupt:
        logging.error("Interrupted by user")
        raise SystemExit(1)
    except Exception as exc:
        logging.error("Pipeline aborted: %s", exc)
        raise SystemExit(1)
    
    if not stats:
        logging.info("No work performed.")
        return
    
    summary = ", ".join(f"{key}={value}" for key, value in sorted(stats.items()))
    logging.info("Analysis complete: %s", summary)


if __name__ == "__main__":
    main()
