"""Test the questionnaire schema with a few sample cases.

Follows the exact pattern from nde-analysis/analyze_experiences.py
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import random
from datetime import datetime, timezone
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence

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
DEFAULT_SECRETS = ROOT / "secrets" / "azure_openai.env"

# Map logical dataset names to actual folder paths
DATASET_PATHS = {
    "rrp": DATA_ROOT / "rrp_cases" / "radical_remission",
    "pmc": DATA_ROOT / "pmc_cases" / "pmc",
    "nderf": DATA_ROOT / "nderf",
    "iands": DATA_ROOT / "iands",
}

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


def load_azure_credentials(config_path: Path) -> Dict[str, str]:
    """Load Azure OpenAI credentials - exact copy from nde-analysis."""
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


def build_user_prompt(
    *,
    title: str,
    dataset: str,
    source_url: Optional[str],
    content: str,
) -> str:
    """Build user prompt - adapted from nde-analysis."""
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


def collect_samples(datasets: Sequence[str], limit: int) -> List[Path]:
    """Collect random sample files from specified datasets."""
    all_files: List[Path] = []
    
    for ds in datasets:
        ds_path = DATASET_PATHS.get(ds)
        if ds_path is None:
            logging.warning(f"Unknown dataset: {ds}")
            continue
        if not ds_path.exists():
            logging.warning(f"Dataset path missing: {ds_path}")
            continue
            
        files = list(ds_path.glob("*.json"))
        logging.info(f"Found {len(files)} files in {ds}")
        all_files.extend(files)
    
    if not all_files:
        return []
    
    random.shuffle(all_files)
    return all_files[:limit]


async def request_analysis(
    client: OpenAI,
    *,
    model: str,
    prompt: str,
    temperature: float,
    max_output_tokens: int,
    retries: int = 3,
) -> tuple[RemissionAnalysisResponse, Optional[Mapping[str, object]], Optional[str]]:
    """Request analysis - exact pattern from nde-analysis."""
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


async def analyze_case(
    client: OpenAI,
    model: str,
    file_path: Path,
    temperature: float,
    max_output_tokens: int,
) -> dict:
    """Analyze a single case file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        return {"error": f"JSON parse error: {exc}", "file": str(file_path)}
    
    title = str(data.get("title") or file_path.stem).strip() or "Untitled Case"
    content = str(data.get("content") or data.get("narrative") or data.get("text") or "").strip()
    source_url = str(data.get("url") or data.get("source_url") or "").strip() or None
    dataset = data.get("source", file_path.parent.name)
    
    if not content:
        return {"error": "No content in file", "file": str(file_path)}
    
    prompt = build_user_prompt(
        title=title,
        dataset=dataset,
        source_url=source_url,
        content=content,
    )
    checksum = sha256(content.encode("utf-8")).hexdigest()
    
    logging.info(f"Analyzing: {file_path.name} ({len(content)} chars)")
    
    try:
        analysis, usage, response_id = await request_analysis(
            client,
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
    except Exception as exc:
        return {"error": f"API error: {exc}", "file": str(file_path)}
    
    payload = {
        "dataset": dataset,
        "source_file": str(file_path.relative_to(ROOT)),
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
    
    return {
        "success": True,
        "file": str(file_path.name),
        "payload": payload,
    }


def print_summary(result: dict):
    """Print a summary of an analysis result."""
    if "error" in result:
        print(f"\n❌ ERROR: {result['file']}")
        print(f"   {result['error']}")
        return
    
    payload = result["payload"]
    analysis = payload["analysis"]
    
    print(f"\n✅ SUCCESS: {result['file']}")
    print(f"   Disease Category: {analysis['disease_category_flag']}")
    print(f"   Cancer: {analysis['is_cancer_case']} | Autoimmune: {analysis['is_autoimmune_case']}")
    
    diag = analysis["diagnosis"]
    print(f"   Diagnosis: {diag.get('disease_name') or diag.get('diagnosis_raw') or 'Unknown'}")
    
    rem = analysis["remission_outcome"]
    print(f"   Remission Type: {rem.get('remission_type', 'unknown')}")
    print(f"   Verified: {analysis['is_verified_remission']}")
    print(f"   Transformation Narrative: {analysis['has_transformation_narrative']}")
    
    if analysis.get("case_summary"):
        print(f"   Summary: {analysis['case_summary'][:100]}...")


async def run_test(args: argparse.Namespace) -> int:
    """Run the test pipeline."""
    samples = collect_samples(args.datasets, args.limit)
    if not samples:
        logging.error("No sample files found")
        return 1
    
    creds = load_azure_credentials(Path(args.secrets_path))
    model = args.model or creds["AZURE_OPENAI_DEPLOYMENT"]
    
    # Create client exactly as nde-analysis does
    client = OpenAI(
        api_key=creds["AZURE_OPENAI_KEY"],
        base_url=creds["AZURE_OPENAI_ENDPOINT"],
    )
    
    logging.info(f"Testing {len(samples)} samples...")
    print(f"\n{'='*60}")
    print(f"TESTING REMISSION ANALYSIS SCHEMA")
    print(f"Model: {model}")
    print(f"Samples: {len(samples)}")
    print(f"{'='*60}")
    
    results = []
    success_count = 0
    
    for sample in samples:
        result = await analyze_case(
            client,
            model,
            sample,
            temperature=args.temperature,
            max_output_tokens=args.max_output_tokens,
        )
        results.append(result)
        print_summary(result)
        if result.get("success"):
            success_count += 1
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {success_count}/{len(samples)} successful")
    print(f"{'='*60}")
    
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nResults saved to: {args.output}")
    
    return 0 if success_count == len(samples) else 1


def main():
    parser = argparse.ArgumentParser(description="Test schema extraction on sample cases")
    parser.add_argument("--datasets", nargs="+", default=["rrp", "pmc"],
                        help="Datasets to sample from")
    parser.add_argument("--limit", type=int, default=3,
                        help="Number of cases to analyze")
    parser.add_argument("--model", default=None,
                        help="Model deployment name (default: from env)")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output JSON file for results")
    parser.add_argument("--temperature", type=float, default=0.7,
                        help="Sampling temperature (default: 0.7)")
    parser.add_argument("--max-output-tokens", type=int, default=10000,
                        help="Max output tokens (default: 10000)")
    parser.add_argument("--secrets-path", type=str, default=str(DEFAULT_SECRETS),
                        help="Path to azure_openai.env")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbose output")
    args = parser.parse_args()
    
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    
    try:
        exit_code = asyncio.run(run_test(args))
    except KeyboardInterrupt:
        logging.error("Interrupted by user")
        exit_code = 1
    except Exception as exc:
        logging.error("Pipeline aborted: %s", exc)
        exit_code = 1
    
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
