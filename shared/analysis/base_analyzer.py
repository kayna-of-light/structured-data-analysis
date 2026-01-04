"""
Base analyzer class for structured output analysis.

Provides common functionality for analyzing JSON records with Azure OpenAI,
including retry logic, rate limiting, and result persistence.
"""

from __future__ import annotations

import asyncio
import json
import logging
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import (
    Any,
    Dict,
    Generic,
    List,
    Mapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from openai import APIStatusError, AzureOpenAI, RateLimitError
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

# Type variable for response model
T = TypeVar("T", bound=BaseModel)


@dataclass
class AnalysisJob:
    """Represents a single item to be analyzed."""
    dataset: str
    source_path: Path
    target_path: Path
    registry_name: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AnalysisResult:
    """Result of analyzing a single job."""
    job: AnalysisJob
    status: str  # "success", "skipped", "error", "invalid"
    analysis: Optional[Dict[str, Any]] = None
    usage: Optional[Dict[str, Any]] = None
    response_id: Optional[str] = None
    error: Optional[str] = None
    duration_ms: Optional[int] = None


class BaseAnalyzer(ABC, Generic[T]):
    """
    Abstract base class for structured output analysis.
    
    Subclasses must implement:
    - response_model: The Pydantic model for structured output
    - system_prompt: The system prompt for the LLM
    - build_user_prompt(): Build user prompt from source data
    """
    
    # Subclasses must define these
    response_model: Type[T]
    system_prompt: str
    
    def __init__(
        self,
        client: AzureOpenAI,
        model: str,
        *,
        temperature: float = 0.0,
        max_output_tokens: int = 4096,
        max_retries: int = 3,
        initial_backoff: float = 2.0,
        rate_limit_wait: float = 60.0,
    ):
        """
        Initialize the analyzer.
        
        Args:
            client: Azure OpenAI client
            model: Model deployment name
            temperature: Sampling temperature (0.0 for deterministic)
            max_output_tokens: Maximum tokens in response
            max_retries: Number of retry attempts
            initial_backoff: Initial backoff time for retries
            rate_limit_wait: Wait time when rate limited
        """
        self.client = client
        self.model = model
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff
        self.rate_limit_wait = rate_limit_wait
    
    @abstractmethod
    def build_user_prompt(self, data: Mapping[str, Any], job: AnalysisJob) -> str:
        """
        Build the user prompt from source data.
        
        Args:
            data: Parsed JSON data from source file
            job: The analysis job
            
        Returns:
            User prompt string
        """
        pass
    
    def _read_json(self, path: Path) -> Mapping[str, Any]:
        """Read JSON file and return contents."""
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    
    def _compute_content_hash(self, content: str) -> str:
        """Compute SHA256 hash of content for change detection."""
        return sha256(content.encode("utf-8")).hexdigest()[:16]
    
    async def request_analysis(
        self,
        prompt: str,
    ) -> tuple[T, Optional[Dict[str, Any]], Optional[str]]:
        """
        Call Azure OpenAI with structured output and return the parsed analysis.
        
        Args:
            prompt: User prompt
            
        Returns:
            Tuple of (parsed_response, usage_dict, response_id)
            
        Raises:
            RuntimeError: If all retries fail
        """
        backoff = self.initial_backoff
        last_error: Optional[str] = None
        
        for attempt in range(1, self.max_retries + 1):
            try:
                loop = asyncio.get_running_loop()
                call = partial(
                    self.client.beta.chat.completions.parse,
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                    response_format=self.response_model,
                    temperature=self.temperature,
                    max_tokens=self.max_output_tokens,
                )
                response = await loop.run_in_executor(None, call)
                
                message = response.choices[0].message
                if message.refusal:
                    raise ValueError(f"Model refused: {message.refusal}")
                if message.parsed is None:
                    raise ValueError("No structured output returned")
                
                usage = None
                if response.usage:
                    usage = response.usage.model_dump()
                
                return message.parsed, usage, response.id
                
            except (RateLimitError, APIStatusError) as exc:
                last_error = str(exc)
                
                # Check if rate limited
                is_rate_limited = isinstance(exc, RateLimitError) or (
                    isinstance(exc, APIStatusError) and getattr(exc, "status_code", None) == 429
                )
                
                if attempt == self.max_retries:
                    logger.error(
                        "Analysis failed after %d attempts: %s",
                        self.max_retries,
                        last_error,
                    )
                    break
                
                if is_rate_limited:
                    wait_time = self.rate_limit_wait
                    logger.warning(
                        "Rate limit encountered (attempt %d/%d); waiting %.0fs",
                        attempt,
                        self.max_retries,
                        wait_time,
                    )
                else:
                    wait_time = backoff + random.random()
                    logger.warning(
                        "API error (attempt %d/%d); retrying in %.1fs: %s",
                        attempt,
                        self.max_retries,
                        wait_time,
                        exc,
                    )
                
                await asyncio.sleep(wait_time)
                if not is_rate_limited:
                    backoff *= 2
                    
            except ValidationError as exc:
                last_error = str(exc)
                logger.warning(
                    "Validation error (attempt %d/%d): %s",
                    attempt,
                    self.max_retries,
                    exc,
                )
                if attempt == self.max_retries:
                    break
                await asyncio.sleep(backoff + random.random())
                backoff *= 2
        
        raise RuntimeError(last_error or "Unknown Azure OpenAI failure")
    
    async def process_job(
        self,
        job: AnalysisJob,
        *,
        semaphore: asyncio.Semaphore,
        overwrite: bool = False,
        dry_run: bool = False,
    ) -> AnalysisResult:
        """
        Process a single analysis job.
        
        Args:
            job: The job to process
            semaphore: Concurrency limiter
            overwrite: Whether to overwrite existing results
            dry_run: If True, don't actually call the API
            
        Returns:
            AnalysisResult with status and data
        """
        start_time = datetime.now(timezone.utc)
        
        # Check if already processed
        if not overwrite and job.target_path.exists():
            logger.debug("Skipping %s (already analyzed)", job.target_path.name)
            return AnalysisResult(job=job, status="skipped")
        
        # Read source data
        try:
            data = self._read_json(job.source_path)
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse %s: %s", job.source_path, exc)
            return AnalysisResult(job=job, status="invalid", error=str(exc))
        except IOError as exc:
            logger.error("Failed to read %s: %s", job.source_path, exc)
            return AnalysisResult(job=job, status="error", error=str(exc))
        
        # Build prompt
        try:
            prompt = self.build_user_prompt(data, job)
        except Exception as exc:
            logger.error("Failed to build prompt for %s: %s", job.source_path, exc)
            return AnalysisResult(job=job, status="error", error=str(exc))
        
        if dry_run:
            logger.info("[DRY RUN] Would analyze %s", job.source_path.name)
            return AnalysisResult(job=job, status="skipped")
        
        # Call API with semaphore
        async with semaphore:
            try:
                analysis, usage, response_id = await self.request_analysis(prompt)
                
                # Build result document
                result_doc = {
                    "source_file": str(job.source_path),
                    "dataset": job.dataset,
                    "analyzed_at": datetime.now(timezone.utc).isoformat(),
                    "content_hash": self._compute_content_hash(
                        data.get("content", "") or data.get("narrative", "") or ""
                    ),
                    "model": self.model,
                    "response_id": response_id,
                    "usage": usage,
                    "analysis": analysis.model_dump(),
                }
                
                # Save result
                job.target_path.parent.mkdir(parents=True, exist_ok=True)
                with job.target_path.open("w", encoding="utf-8") as f:
                    json.dump(result_doc, f, indent=2, ensure_ascii=False)
                
                duration_ms = int(
                    (datetime.now(timezone.utc) - start_time).total_seconds() * 1000
                )
                
                logger.info(
                    "Analyzed %s -> %s (%d ms)",
                    job.source_path.name,
                    job.target_path.name,
                    duration_ms,
                )
                
                return AnalysisResult(
                    job=job,
                    status="success",
                    analysis=analysis.model_dump(),
                    usage=usage,
                    response_id=response_id,
                    duration_ms=duration_ms,
                )
                
            except Exception as exc:
                logger.error("Failed to analyze %s: %s", job.source_path, exc)
                return AnalysisResult(job=job, status="error", error=str(exc))
    
    async def process_jobs(
        self,
        jobs: Sequence[AnalysisJob],
        *,
        max_concurrency: int = 4,
        overwrite: bool = False,
        dry_run: bool = False,
    ) -> List[AnalysisResult]:
        """
        Process multiple analysis jobs concurrently.
        
        Args:
            jobs: List of jobs to process
            max_concurrency: Maximum concurrent API calls
            overwrite: Whether to overwrite existing results
            dry_run: If True, don't actually call the API
            
        Returns:
            List of AnalysisResult objects
        """
        semaphore = asyncio.Semaphore(max_concurrency)
        
        tasks = [
            self.process_job(
                job,
                semaphore=semaphore,
                overwrite=overwrite,
                dry_run=dry_run,
            )
            for job in jobs
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Convert exceptions to error results
        final_results: List[AnalysisResult] = []
        for job, result in zip(jobs, results):
            if isinstance(result, Exception):
                final_results.append(
                    AnalysisResult(job=job, status="error", error=str(result))
                )
            else:
                final_results.append(result)
        
        # Log summary
        status_counts = {}
        for r in final_results:
            status_counts[r.status] = status_counts.get(r.status, 0) + 1
        
        logger.info(
            "Batch complete: %s",
            ", ".join(f"{status}={count}" for status, count in status_counts.items()),
        )
        
        return final_results
