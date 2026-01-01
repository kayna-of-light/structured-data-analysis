"""Batch analysis of remission cases using Azure OpenAI.

Follows the exact pattern from nde-analysis/analyze_experiences.py
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
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

from dotenv import dotenv_values
from openai import APIStatusError, OpenAI, OpenAIError, RateLimitError
from pydantic import ValidationError

# Add parent to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.questionnaire import RemissionAnalysisResponse

ROOT = Path(__file__).parent.parent
DATA_ROOT = ROOT / "data"
OUTPUT_ROOT = ROOT / "output"
ANALYSIS_DIR = OUTPUT_ROOT / "analysis"
DEFAULT_SECRETS = ROOT / "secrets" / "azure_openai.env"

# Map logical dataset names to actual folder paths
DATASET_PATHS = {
    "rrp": DATA_ROOT / "rrp_cases" / "radical_remission",
    "pmc": DATA_ROOT / "pmc_cases" / "pmc",
    "nderf": DATA_ROOT / "nderf",
    "iands": DATA_ROOT / "iands",
}

SUPPORTED_DATASETS = tuple(DATASET_PATHS.keys())

SYSTEM_PROMPT = """\
You are an expert researcher analyzing spontaneous remission and radical healing case narratives.
Extract both medical information (diagnosis, treatment, outcome) and psycho-spiritual factors 
(Turner's 9 Radical Remission factors, existential shifts, anomalous experiences).

Ground every answer strictly in the supplied narrative. If the narrative omits a detail, 
use 'not_mentioned' for enums or empty lists/None for optional fields.

Be especially careful to:
1. Identify the disease category (cancer, autoimmune, infectious, etc.)
2. Note all treatments mentioned (conventional and alternative)
3. Extract any Turner factors present (diet change, supplements, emotions, intuition, etc.)
4. Note any spiritual practices or existential shifts described
5. Assess the verification level based on medical detail provided
"""


@dataclass(slots=True)
class CaseJob:
    dataset: str
    source_path: Path
    target_path: Path


def _read_json(path: Path) -> Mapping[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_user_prompt(
    *,
    title: str,
    dataset: str,
    source_url: Optional[str],
    content: str,
) -> str:
    header_lines = [
        f"Dataset: {dataset}",
        f"Title: {title.strip() or 'Untitled Case'}",
    ]
    if source_url:
        header_lines.append(f"Source URL: {source_url}")
    header_lines.append("Narrative:")
    header_lines.append(content.strip())
    header_lines.append("\nProvide the most accurate structured questionnaire responses possible.")
    return "\n\n".join(header_lines)


def collect_jobs(datasets: Sequence[str], *, limit: Optional[int]) -> List[CaseJob]:
    jobs: List[CaseJob] = []
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    for dataset in datasets:
        source_dir = DATASET_PATHS.get(dataset)
        if source_dir is None:
            logging.warning("Unknown dataset: %s", dataset)
            continue
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
    logging.info("Collected %d jobs from %d datasets", len(jobs), len(datasets))
    if limit is not None and limit >= 0:
        jobs = jobs[:limit]
    return jobs


def load_azure_credentials(config_path: Path) -> Dict[str, str]:
    collected: Dict[str, str] = {}
    for key in (
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_KEY",
        "AZURE_OPENAI_DEPLOYMENT",
    ):
        env_value = os.getenv(key)
        if env_value:
            collected[key] = env_value
    if config_path.exists():
        collected.update({k: v for k, v in dotenv_values(config_path).items() if v})
    missing = [
        key
        for key in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_KEY", "AZURE_OPENAI_DEPLOYMENT")
        if not collected.get(key)
    ]
    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"Missing Azure OpenAI credentials for: {joined}")
    return collected


async def request_analysis(
    client: OpenAI,
    *,
    model: str,
    prompt: str,
    temperature: float,
    max_output_tokens: int,
    retries: int = 3,
) -> tuple[RemissionAnalysisResponse, Optional[Mapping[str, object]], Optional[str]]:
    backoff = 2.0
    last_error: Optional[str] = None
    for attempt in range(1, retries + 1):
        try:
            loop = asyncio.get_running_loop()
            call = partial(
                client.responses.parse,
                model=model,
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=temperature,
                max_output_tokens=max_output_tokens,
                text_format=RemissionAnalysisResponse,
            )
            response = await loop.run_in_executor(None, call)
            analysis = response.output_parsed
            usage = None
            if getattr(response, "usage", None):
                usage_obj = response.usage
                if hasattr(usage_obj, "model_dump"):
                    usage = usage_obj.model_dump()
                else:
                    usage = json.loads(json.dumps(usage_obj))
            return analysis, usage, getattr(response, "id", None)
        except (OpenAIError, ValidationError) as exc:
            last_error = str(exc)
            logging.warning(
                "Structured response attempt %s/%s failed: %s", attempt, retries, exc
            )
            rate_limited = isinstance(exc, RateLimitError) or (
                isinstance(exc, APIStatusError) and getattr(exc, "status_code", None) == 429
            )
            if attempt == retries:
                continue
            if rate_limited:
                wait_time = 60.0
                logging.warning(
                    "Rate limit encountered; waiting %.0f seconds before retrying.",
                    wait_time,
                )
            else:
                wait_time = backoff + random.random()
            await asyncio.sleep(wait_time)
            if not rate_limited:
                backoff *= 2
    raise RuntimeError(last_error or "Unknown Azure OpenAI failure")


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
    if not overwrite and job.target_path.exists():
        logging.debug("Skipping %s (already analyzed)", job.target_path.name)
        return "skipped"
    try:
        data = _read_json(job.source_path)
    except json.JSONDecodeError as exc:
        logging.error("Failed to parse %s: %s", job.source_path, exc)
        return "invalid"
    
    title = str(data.get("title") or job.source_path.stem).strip() or "Untitled Case"
    content = str(data.get("content") or data.get("narrative") or data.get("text") or "").strip()
    source_url = str(data.get("url") or data.get("source_url") or "").strip() or None
    
    if not content:
        logging.warning("No content in %s; skipping", job.source_path)
        return "empty"
    
    prompt = build_user_prompt(
        title=title,
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
        except Exception as exc:
            logging.error("Analysis failed for %s: %s", job.source_path, exc)
            return "failed"
    
    payload = {
        "dataset": job.dataset,
        "source_file": str(job.source_path.relative_to(ROOT)),
        "source_url": source_url,
        "title": title,
        "content": content,
        "analysis_model": model,
        "analysis_timestamp": datetime.now(timezone.utc).isoformat(),
        "source_checksum": checksum,
        "questionnaire_schema": "RemissionAnalysisResponse",
        "analysis": analysis.model_dump(mode="json"),
        "response_id": response_id,
        "usage": usage,
    }
    
    job.target_path.parent.mkdir(parents=True, exist_ok=True)
    job.target_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    logging.info("Wrote analysis to %s", job.target_path.name)
    return "written"


async def run_pipeline(args: argparse.Namespace) -> Dict[str, int]:
    datasets = args.datasets or list(SUPPORTED_DATASETS)
    jobs = collect_jobs(datasets, limit=args.limit)
    if not jobs:
        logging.warning("No matching cases were found to analyze.")
        return {}
    
    if args.dry_run:
        client = None
        model_name = args.model or "dry-run"
    else:
        creds = load_azure_credentials(Path(args.secrets_path))
        model_name = args.model or creds["AZURE_OPENAI_DEPLOYMENT"]
        client = OpenAI(
            api_key=creds["AZURE_OPENAI_KEY"],
            base_url=creds["AZURE_OPENAI_ENDPOINT"],
        )
    
    semaphore = asyncio.Semaphore(max(1, args.max_concurrency))
    stats: Dict[str, int] = {}
    
    logging.info("Starting analysis of %d cases with concurrency=%d", len(jobs), args.max_concurrency)
    
    tasks = [
        asyncio.create_task(
            process_job(
                job,
                client=client,
                model=model_name,
                temperature=args.temperature,
                max_output_tokens=args.max_output_tokens,
                semaphore=semaphore,
                overwrite=args.overwrite,
                dry_run=args.dry_run,
            )
        )
        for job in jobs
    ]
    
    completed = 0
    total = len(tasks)
    for task in asyncio.as_completed(tasks):
        status = await task
        stats[status] = stats.get(status, 0) + 1
        completed += 1
        if completed % 10 == 0 or completed == total:
            logging.info("Progress: %d/%d complete", completed, total)
    
    return stats


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Batch Azure OpenAI analysis for remission case datasets.",
    )
    parser.add_argument(
        "--datasets",
        nargs="+",
        default=list(SUPPORTED_DATASETS),
        choices=list(SUPPORTED_DATASETS),
        help=f"Datasets to process (default: all). Available: {', '.join(SUPPORTED_DATASETS)}",
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
        help="Maximum number of concurrent Azure OpenAI calls (default: 4).",
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
        help="Upper bound for structured response tokens (default: 10000).",
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
    parser = create_parser()
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
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
