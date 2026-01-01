"""
Quick LLM validation script for filtering true physical remission cases.

Processes NDE cases in parallel through Azure OpenAI to classify whether
they contain genuine physical healing/remission of the experiencer.

Usage:
    python scripts/validate_remission_cases.py data/nderf_healing data/validated/nderf --workers 10
    python scripts/validate_remission_cases.py data/iands_healing data/validated/iands --workers 10
"""

from __future__ import annotations

import asyncio
import json
import os
import random
import shutil
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import partial
from typing import Optional, Mapping
import argparse
import logging

from dotenv import dotenv_values
from openai import APIStatusError, OpenAI, OpenAIError, RateLimitError
from pydantic import ValidationError

from models.validation_schema import QuickValidation

ROOT = Path(__file__).parent.parent
DEFAULT_SECRETS = ROOT / "secrets" / "azure_openai.env"
DEFAULT_API_VERSION = "2024-05-01-preview"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


SYSTEM_PROMPT = """You are a medical research assistant classifying near-death experience (NDE) narratives for physical healing content.

Your task: Determine if this narrative describes PHYSICAL healing/remission of a medical condition experienced by the person who had the NDE.

CLASSIFY AS "confirmed_remission" ONLY IF:
- The experiencer (not someone else) had a physical medical condition
- The condition was healed, cured, or went into remission
- The healing is clearly connected to the NDE or occurred around that time
- There is some specificity about what was healed (cancer, paralysis, disease, etc.)

CLASSIFY AS "probable_remission" IF:
- Healing is mentioned but details are vague
- The connection to NDE is unclear but plausible

CLASSIFY AS "spiritual_only" IF:
- Only emotional, psychological, or spiritual healing is described
- Terms like "healed" refer to grief, trauma, relationships, or outlook on life

CLASSIFY AS "third_party" IF:
- The narrative describes healing someone ELSE (the experiencer became a healer)
- The narrative mentions a family member or friend who was healed

CLASSIFY AS "no_healing" IF:
- No healing content is found in the narrative

Be conservative: only mark "confirmed_remission" for clear, specific cases of physical healing of the experiencer."""


@dataclass
class ValidationStats:
    """Track validation statistics."""
    total: int = 0
    confirmed_remission: int = 0
    probable_remission: int = 0
    spiritual_only: int = 0
    third_party: int = 0
    no_healing: int = 0
    insufficient_data: int = 0
    errors: int = 0
    
    def add_result(self, result: str):
        self.total += 1
        if result == "confirmed_remission":
            self.confirmed_remission += 1
        elif result == "probable_remission":
            self.probable_remission += 1
        elif result == "spiritual_only":
            self.spiritual_only += 1
        elif result == "third_party":
            self.third_party += 1
        elif result == "no_healing":
            self.no_healing += 1
        elif result == "insufficient_data":
            self.insufficient_data += 1
    
    def summary(self) -> str:
        return f"""
Validation Results:
  Total processed: {self.total}
  ✅ Confirmed remission: {self.confirmed_remission}
  🔶 Probable remission: {self.probable_remission}
  💭 Spiritual only: {self.spiritual_only}
  👥 Third party healing: {self.third_party}
  ❌ No healing: {self.no_healing}
  ❓ Insufficient data: {self.insufficient_data}
  ⚠️  Errors: {self.errors}
"""


def load_azure_credentials(config_path: Path) -> dict[str, str]:
    """Load Azure OpenAI credentials from environment or config file."""
    collected: dict[str, str] = {}
    for key in (
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_KEY",
        "AZURE_OPENAI_DEPLOYMENT",
        "AZURE_OPENAI_API_VERSION",
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
    
    collected.setdefault("AZURE_OPENAI_API_VERSION", DEFAULT_API_VERSION)
    return collected


def build_user_prompt(title: str, content: str) -> str:
    """Build the user prompt for validation."""
    return f"""Title: {title}

Narrative:
{content}

Analyze this narrative and classify it according to the schema."""


async def request_validation(
    client: OpenAI,
    *,
    model: str,
    prompt: str,
    temperature: float,
    max_output_tokens: int,
    retries: int = 3,
) -> tuple[QuickValidation, Optional[Mapping[str, object]]]:
    """Request validation from Azure OpenAI using structured output."""
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
                text_format=QuickValidation,
            )
            response = await loop.run_in_executor(None, call)
            validation = response.output_parsed
            usage = None
            if getattr(response, "usage", None):
                usage_obj = response.usage
                if hasattr(usage_obj, "model_dump"):
                    usage = usage_obj.model_dump()
                else:
                    usage = json.loads(json.dumps(usage_obj))
            return validation, usage
        except (OpenAIError, ValidationError) as exc:
            last_error = str(exc)
            logging.warning(
                "Validation attempt %s/%s failed: %s", attempt, retries, exc
            )
            rate_limited = isinstance(exc, RateLimitError) or (
                isinstance(exc, APIStatusError) and getattr(exc, "status_code", None) == 429
            )
            if attempt == retries:
                continue
            if rate_limited:
                wait_time = 60.0
                logging.warning(
                    "Azure rate limit encountered; waiting %.0f seconds before retrying.",
                    wait_time,
                )
            else:
                wait_time = backoff + random.random()
            await asyncio.sleep(wait_time)
            if not rate_limited:
                backoff *= 2
    raise RuntimeError(last_error or "Unknown Azure OpenAI failure")


class RemissionValidator:
    """Validates NDE cases for physical remission content using LLM."""
    
    def __init__(
        self,
        client: OpenAI,
        model: str,
        output_dir: Path,
        include_probable: bool = False
    ):
        self.client = client
        self.model = model
        self.output_dir = output_dir
        self.include_probable = include_probable
        self.stats = ValidationStats()
        self.results: list[dict] = []
        
        # Create output directories
        (output_dir / "confirmed").mkdir(parents=True, exist_ok=True)
        if include_probable:
            (output_dir / "probable").mkdir(parents=True, exist_ok=True)
    
    async def validate_case(
        self,
        file_path: Path,
        semaphore: asyncio.Semaphore
    ) -> Optional[dict]:
        """Validate a single NDE case."""
        async with semaphore:
            try:
                # Load the case
                with open(file_path, 'r', encoding='utf-8') as f:
                    case = json.load(f)
                
                content = case.get('content', '')
                title = case.get('title', file_path.stem)
                
                if not content or len(content) < 100:
                    return None
                
                # Truncate very long content
                if len(content) > 15000:
                    content = content[:15000] + "... [truncated]"
                
                prompt = build_user_prompt(title, content)
                
                # Call LLM
                validation, usage = await request_validation(
                    self.client,
                    model=self.model,
                    prompt=prompt,
                    temperature=0.1,
                    max_output_tokens=500,
                )
                
                # Convert to dict
                result = validation.model_dump(mode="json")
                result['file'] = file_path.name
                result['title'] = title
                
                # Update stats
                self.stats.add_result(result['validation_result'])
                
                # Copy to appropriate directory if validated
                if result['validation_result'] == 'confirmed_remission':
                    dest = self.output_dir / "confirmed" / file_path.name
                    shutil.copy2(file_path, dest)
                    print(f"✅ {title[:50]}... -> confirmed ({result['condition_description']})")
                elif result['validation_result'] == 'probable_remission' and self.include_probable:
                    dest = self.output_dir / "probable" / file_path.name
                    shutil.copy2(file_path, dest)
                    print(f"🔶 {title[:50]}... -> probable ({result['condition_description']})")
                elif result['validation_result'] == 'spiritual_only':
                    print(f"💭 {title[:50]}... -> spiritual only")
                elif result['validation_result'] == 'third_party':
                    print(f"👥 {title[:50]}... -> third party")
                else:
                    print(f"❌ {title[:50]}... -> {result['validation_result']}")
                
                return result
                
            except Exception as e:
                self.stats.errors += 1
                print(f"⚠️  Error processing {file_path.name}: {e}")
                return None
    
    async def validate_directory(self, source_dir: Path, max_workers: int = 10):
        """Validate all cases in a directory."""
        json_files = list(source_dir.glob('*.json'))
        print(f"Processing {len(json_files)} files from {source_dir}...")
        print(f"Output directory: {self.output_dir}")
        print(f"Max parallel workers: {max_workers}")
        print("-" * 60)
        
        semaphore = asyncio.Semaphore(max_workers)
        
        tasks = [self.validate_case(f, semaphore) for f in json_files]
        results = await asyncio.gather(*tasks)
        
        self.results = [r for r in results if r is not None]
        
        print("-" * 60)
        print(self.stats.summary())
        
        # Save results log
        log_path = self.output_dir / "validation_log.json"
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "source_dir": str(source_dir),
                "stats": {
                    "total": self.stats.total,
                    "confirmed_remission": self.stats.confirmed_remission,
                    "probable_remission": self.stats.probable_remission,
                    "spiritual_only": self.stats.spiritual_only,
                    "third_party": self.stats.third_party,
                    "no_healing": self.stats.no_healing,
                    "insufficient_data": self.stats.insufficient_data,
                    "errors": self.stats.errors
                },
                "results": self.results
            }, f, indent=2)
        
        print(f"Results log saved to: {log_path}")
        
        # Count files in output
        confirmed_count = len(list((self.output_dir / "confirmed").glob('*.json')))
        print(f"\n📁 Confirmed remission cases: {confirmed_count} files in {self.output_dir / 'confirmed'}")
        
        if self.include_probable:
            probable_count = len(list((self.output_dir / "probable").glob('*.json')))
            print(f"📁 Probable remission cases: {probable_count} files in {self.output_dir / 'probable'}")


async def main():
    parser = argparse.ArgumentParser(description="Validate NDE cases for physical remission")
    parser.add_argument("source", help="Source directory with filtered cases")
    parser.add_argument("output", help="Output directory for validated cases")
    parser.add_argument("--workers", type=int, default=10, help="Number of parallel workers")
    parser.add_argument("--include-probable", action="store_true", help="Also copy probable cases")
    parser.add_argument("--secrets", type=Path, default=DEFAULT_SECRETS, help="Path to secrets file")
    
    args = parser.parse_args()
    
    source = Path(args.source)
    output = Path(args.output)
    
    if not source.exists():
        print(f"Error: Source directory {source} does not exist")
        return 1
    
    # Load credentials
    creds = load_azure_credentials(args.secrets)
    
    # Create client using same pattern as nde-analysis (exact match)
    client = OpenAI(
        api_key=creds["AZURE_OPENAI_KEY"],
        base_url=creds["AZURE_OPENAI_ENDPOINT"],
    )
    
    model = creds["AZURE_OPENAI_DEPLOYMENT"]
    
    validator = RemissionValidator(
        client=client,
        model=model,
        output_dir=output,
        include_probable=args.include_probable
    )
    await validator.validate_directory(source, max_workers=args.workers)
    
    return 0


if __name__ == "__main__":
    asyncio.run(main())
