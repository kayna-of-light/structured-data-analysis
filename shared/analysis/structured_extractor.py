"""Generic structured data extraction pipeline using Azure OpenAI.

This module provides a reusable pipeline for extracting structured data from
text narratives using Azure OpenAI's structured output feature. Projects
provide their own Pydantic response model and system prompt.

Supports multi-modal extraction with images when available in source data.

Usage:
    from shared.analysis.structured_extractor import StructuredExtractor, ExtractorConfig
    from models import MyResponseModel

    config = ExtractorConfig(
        response_model=MyResponseModel,
        system_prompt="You are an expert...",
        supported_datasets=("dataset1", "dataset2"),
        enable_images=True,  # Enable image download and inclusion
    )
    extractor = StructuredExtractor(config)
    asyncio.run(extractor.run(args))
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import logging
import os
import random
from dataclasses import dataclass, field
from datetime import datetime, timezone
from functools import partial
from hashlib import sha256
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
)

import httpx
import requests
from dotenv import dotenv_values
from openai import APIStatusError, OpenAI, OpenAIError, RateLimitError
from pydantic import BaseModel, ValidationError

# Type variable for the response model
T = TypeVar("T", bound=BaseModel)

DEFAULT_API_VERSION = "2024-05-01-preview"


@dataclass
class ExtractorConfig:
    """Configuration for the structured extractor."""

    response_model: Type[BaseModel]
    """Pydantic model class for structured output parsing."""

    system_prompt: str
    """System prompt instructing the model how to extract data."""

    supported_datasets: Tuple[str, ...]
    """Tuple of supported dataset directory names."""

    data_root: Path = field(default_factory=lambda: Path.cwd() / "data")
    """Root directory containing dataset folders."""

    output_root: Path = field(default_factory=lambda: Path.cwd() / "structured")
    """Root directory for analysis output."""

    secrets_path: Path = field(default_factory=lambda: Path.cwd() / "secrets" / "azure_openai.env")
    """Path to Azure OpenAI credentials file."""

    schema_name: Optional[str] = None
    """Optional schema name for output metadata (defaults to model class name)."""

    user_prompt_suffix: str = "\nProvide the most accurate structured responses possible."
    """Suffix appended to user prompts."""

    registries_dir: Optional[Path] = None
    """Optional path to registries directory for registry-based loading."""

    use_registries: bool = True
    """If True, load files from registries instead of direct directory access."""

    # Image support configuration
    enable_images: bool = False
    """If True, download and include images in extraction requests."""
    
    max_images: int = 4
    """Maximum number of images to include per request (to manage token costs)."""
    
    image_cache_dir: Optional[Path] = None
    """Optional directory to cache downloaded images. If None, images are not cached."""
    
    image_detail: str = "auto"
    """Image detail level for OpenAI vision: 'auto', 'low', or 'high'."""


@dataclass(slots=True)
class ExtractionJob:
    """Represents a single file to be processed."""

    dataset: str
    source_path: Path
    target_path: Path


def _read_json(path: Path) -> Mapping[str, object]:
    """Read JSON file and return contents."""
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


# =============================================================================
# IMAGE HANDLING
# =============================================================================

async def download_image(
    url: str,
    cache_dir: Optional[Path] = None,
    timeout: float = 30.0,
) -> Optional[Tuple[bytes, str]]:
    """Download an image from a URL with content-based caching (async version).
    
    Uses SHA256 hash of image content as filename to avoid downloading
    duplicates from different URLs. Extension preserves media type.
    
    Args:
        url: Image URL to download
        cache_dir: Optional directory to cache images (defaults to repo_root/cache)
        timeout: Request timeout in seconds
        
    Returns:
        Tuple of (image bytes, media type) or None if download fails
    """
    # Check if URL already in cache (URL-based lookup for fast check)
    if cache_dir:
        url_hash = sha256(url.encode()).hexdigest()[:16]
        url_marker = cache_dir / f".url_{url_hash}"
        if url_marker.exists():
            # Read the content hash from the marker file
            content_hash = url_marker.read_text().strip()
            # Find the actual cached file
            cached_files = list(cache_dir.glob(f"{content_hash}.*"))
            if cached_files:
                cache_path = cached_files[0]
                ext = cache_path.suffix
                media_type = _get_media_type(ext)
                logging.debug(f"Using cached image: {cache_path.name}")
                return cache_path.read_bytes(), media_type
    
    # For Reddit images, check if available in Internet Archive (many old images deleted from Reddit)
    archive_url = None
    if "i.redd.it" in url or "preview.redd.it" in url:
        try:
            # Check Wayback Machine availability (async)
            wayback_api = f"https://archive.org/wayback/available?url={url}"
            async with httpx.AsyncClient() as client:
                wayback_response = await client.get(wayback_api, timeout=5)
                wayback_data = wayback_response.json()
            
            closest = wayback_data.get("archived_snapshots", {}).get("closest")
            if closest and closest.get("available"):
                archive_url = closest["url"]
                logging.debug(f"Archive available for {url.split('/')[-1]}")
        except Exception as exc:
            logging.debug(f"Wayback check failed for {url}: {exc}")
    
    # Try archive first if available, then fallback to direct URL
    urls_to_try = [archive_url, url] if archive_url else [url]
    
    async with httpx.AsyncClient() as client:
        for attempt_url in urls_to_try:
            try:
                headers = {
                    "User-Agent": "MallWorldResearch/1.0 (Academic research)",
                    "Accept": "image/*",
                }
                response = await client.get(attempt_url, headers=headers, timeout=timeout)
                response.raise_for_status()
            
                # Determine media type from content-type header or original URL
                content_type = response.headers.get("content-type", "")
                if "jpeg" in content_type or "jpg" in content_type:
                    media_type = "image/jpeg"
                    ext = ".jpg"
                elif "png" in content_type:
                    media_type = "image/png"
                    ext = ".png"
                elif "gif" in content_type:
                    media_type = "image/gif"
                    ext = ".gif"
                elif "webp" in content_type:
                    media_type = "image/webp"
                    ext = ".webp"
                else:
                    # Fallback to original URL extension (not archive URL)
                    ext = Path(url.split("?")[0]).suffix.lower() or ".jpg"
                    media_type = _get_media_type(ext)
                
                image_bytes = response.content
                
                # Cache if enabled - use content hash to avoid duplicates
                if cache_dir:
                    content_hash = sha256(image_bytes).hexdigest()
                    cache_path = cache_dir / f"{content_hash}{ext}"
                    
                    # Check if this content already cached (content deduplication)
                    if cache_path.exists():
                        logging.debug(f"Image content already cached: {cache_path.name}")
                    else:
                        # Save image to cache
                        cache_path.parent.mkdir(parents=True, exist_ok=True)
                        cache_path.write_bytes(image_bytes)
                        source = "archive" if attempt_url == archive_url else "reddit"
                        logging.debug(f"Cached new image from {source}: {cache_path.name}")
                    
                    # Create URL marker for fast lookup next time
                    url_hash = sha256(url.encode()).hexdigest()[:16]
                    url_marker = cache_dir / f".url_{url_hash}"
                    url_marker.write_text(content_hash)
                
                return image_bytes, media_type
                
            except Exception as exc:
                # If archive failed, try direct URL; if direct failed, return None
                if attempt_url == archive_url:
                    logging.debug(f"Archive download failed for {url.split('/')[-1]}, trying Reddit")
                    continue
                else:
                    logging.debug("Failed to download image %s: %s", url, exc)
                    return None
    
    # All attempts failed
    return None


def _get_media_type(ext: str) -> str:
    """Get media type from file extension."""
    ext = ext.lower().lstrip(".")
    return {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp",
    }.get(ext, "image/jpeg")


def encode_image_base64(image_bytes: bytes) -> str:
    """Encode image bytes to base64 string."""
    return base64.b64encode(image_bytes).decode("utf-8")


def build_image_content(
    image_bytes: bytes,
    media_type: str,
    detail: str = "auto",
) -> Dict[str, Any]:
    """Build OpenAI image content block.
    
    Args:
        image_bytes: Raw image bytes
        media_type: MIME type (e.g., 'image/jpeg')
        detail: Detail level ('auto', 'low', 'high')
        
    Returns:
        Dictionary formatted for Azure OpenAI Responses API
    """
    b64_data = encode_image_base64(image_bytes)
    # Azure OpenAI Responses API uses 'input_image' type
    return {
        "type": "input_image",
        "image_url": f"data:{media_type};base64,{b64_data}",
        "detail": detail,
    }


async def fetch_images_for_extraction(
    image_urls: List[str],
    max_images: int = 4,
    cache_dir: Optional[Path] = None,
    detail: str = "auto",
) -> List[Dict[str, Any]]:
    """Download images and prepare them for OpenAI API (async version).
    
    Args:
        image_urls: List of image URLs to download
        max_images: Maximum number of images to include
        cache_dir: Optional cache directory
        detail: Image detail level
        
    Returns:
        List of image content blocks for OpenAI API
    """
    image_contents: List[Dict[str, Any]] = []
    failed_count = 0
    
    for url in image_urls[:max_images]:
        result = await download_image(url, cache_dir=cache_dir)
        if result:
            image_bytes, media_type = result
            content = build_image_content(image_bytes, media_type, detail)
            image_contents.append(content)
        else:
            failed_count += 1
    
    # Log summary if any images were processed
    if image_urls:
        success_count = len(image_contents)
        if failed_count > 0:
            logging.debug(f"Images: {success_count} retrieved, {failed_count} unavailable")
    
    return image_contents


# =============================================================================
# PROMPT BUILDING
# =============================================================================

def build_user_prompt(
    *,
    title: str,
    date: Optional[str],
    dataset: str,
    source_url: Optional[str],
    content: str,
    suffix: str = "",
) -> str:
    """Build the user prompt for extraction.

    Args:
        title: Document title or name
        date: Optional date string
        dataset: Dataset identifier
        source_url: Optional source URL
        content: Main text content to analyze
        suffix: Optional suffix to append

    Returns:
        Formatted user prompt string
    """
    header_lines = [
        f"Dataset: {dataset}",
        f"Title: {title.strip() or 'Untitled'}",
    ]
    if date:
        header_lines.append(f"Reported date: {date}")
    if source_url:
        header_lines.append(f"Source URL: {source_url}")
    header_lines.append("Narrative:")
    header_lines.append(content.strip())
    if suffix:
        header_lines.append(suffix)
    return "\n\n".join(header_lines)


def load_azure_credentials(config_path: Path) -> Dict[str, str]:
    """Load Azure OpenAI credentials from environment and/or file.

    Checks environment variables first, then loads from the config file.
    File values take precedence over environment variables.

    Args:
        config_path: Path to the credentials .env file

    Returns:
        Dictionary with credential keys

    Raises:
        RuntimeError: If required credentials are missing
    """
    collected: Dict[str, str] = {}

    # Check environment variables first
    for key in (
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_KEY",
        "AZURE_OPENAI_API_KEY",  # Alternative key name
        "AZURE_OPENAI_DEPLOYMENT",
        "AZURE_OPENAI_API_VERSION",
    ):
        env_value = os.getenv(key)
        if env_value:
            collected[key] = env_value

    file_values: Dict[str, str] = {}

    # Load from file (takes precedence)
    if config_path.exists():
        file_values = {k: v for k, v in dotenv_values(config_path).items() if v}
        collected.update(file_values)

    # Normalize key names (support both KEY and API_KEY)
    # IMPORTANT: file values must take precedence over environment variables.
    if file_values.get("AZURE_OPENAI_KEY"):
        collected["AZURE_OPENAI_KEY"] = file_values["AZURE_OPENAI_KEY"]
        collected["AZURE_OPENAI_API_KEY"] = file_values["AZURE_OPENAI_KEY"]
    elif file_values.get("AZURE_OPENAI_API_KEY"):
        collected["AZURE_OPENAI_KEY"] = file_values["AZURE_OPENAI_API_KEY"]
        collected["AZURE_OPENAI_API_KEY"] = file_values["AZURE_OPENAI_API_KEY"]
    else:
        if "AZURE_OPENAI_API_KEY" not in collected and collected.get("AZURE_OPENAI_KEY"):
            collected["AZURE_OPENAI_API_KEY"] = collected["AZURE_OPENAI_KEY"]
        elif "AZURE_OPENAI_KEY" not in collected and collected.get("AZURE_OPENAI_API_KEY"):
            collected["AZURE_OPENAI_KEY"] = collected["AZURE_OPENAI_API_KEY"]

    # Validate required credentials
    missing = [
        key
        for key in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT")
        if not collected.get(key)
    ]
    if not collected.get("AZURE_OPENAI_KEY") and not collected.get("AZURE_OPENAI_API_KEY"):
        missing.append("AZURE_OPENAI_KEY")

    if missing:
        raise RuntimeError(
            f"Missing Azure OpenAI credentials: {', '.join(missing)}. "
            f"Set environment variables or create {config_path}"
        )

    collected.setdefault("AZURE_OPENAI_API_VERSION", DEFAULT_API_VERSION)
    return collected


def create_azure_client(creds: Dict[str, str], model_override: Optional[str] = None) -> Tuple[OpenAI, str]:
    """Create Azure OpenAI client from credentials.

    Args:
        creds: Credentials dictionary from load_azure_credentials()
        model_override: Optional model/deployment name override

    Returns:
        Tuple of (OpenAI client, model name)
    """
    endpoint = creds["AZURE_OPENAI_ENDPOINT"]
    api_key = creds.get("AZURE_OPENAI_API_KEY") or creds.get("AZURE_OPENAI_KEY", "")
    deployment = model_override or creds["AZURE_OPENAI_DEPLOYMENT"]

    # Azure Foundry OpenAI-compatible endpoint: base_url should already include /openai/v1/
    client = OpenAI(base_url=endpoint, api_key=api_key)

    return client, deployment


class StructuredExtractor:
    """Generic structured data extraction pipeline.

    This class provides the full extraction workflow:
    1. Collect jobs from dataset directories
    2. Build prompts from source files
    3. Call Azure OpenAI with structured output
    4. Save results to output directory
    """

    def __init__(self, config: ExtractorConfig):
        """Initialize the extractor with configuration.

        Args:
            config: ExtractorConfig instance with model, prompts, and paths
        """
        self.config = config
        self.schema_name = config.schema_name or config.response_model.__name__

    def collect_jobs(
        self,
        datasets: Sequence[str],
        *,
        limit: Optional[int] = None,
        file_filter: Optional[List[str]] = None,
    ) -> List[ExtractionJob]:
        """Collect all files to be processed.

        Args:
            datasets: List of dataset names to process
            limit: Optional maximum number of jobs
            file_filter: Optional list of specific file names to include

        Returns:
            List of ExtractionJob instances
        """
        jobs: List[ExtractionJob] = []
        output_dir = self.config.output_root
        output_dir.mkdir(parents=True, exist_ok=True)

        if self.config.use_registries and self.config.registries_dir:
            # Registry-based loading
            from shared.registry import load_registry
            
            for dataset in datasets:
                registry_path = self.config.registries_dir / f"{dataset}.yaml"
                if not registry_path.exists():
                    logging.warning(
                        "Skipping dataset %s because registry %s is missing", 
                        dataset, registry_path
                    )
                    continue
                
                try:
                    registry = load_registry(registry_path)
                    # Get files from all datasets in the registry
                    for reg_dataset_name in registry.list_datasets():
                        files = registry.get_files(reg_dataset_name)
                        for path in sorted(files):
                            # Apply file filter if specified
                            if file_filter and path.name not in file_filter:
                                continue
                            
                            target_name = f"{dataset}-{path.name}"
                            jobs.append(
                                ExtractionJob(
                                    dataset=dataset,
                                    source_path=path,
                                    target_path=output_dir / target_name,
                                )
                            )
                except Exception as e:
                    logging.error("Error loading registry %s: %s", registry_path, e)
                    continue
        else:
            # Direct directory access (legacy mode)
            for dataset in datasets:
                source_dir = self.config.data_root / dataset
                if not source_dir.exists():
                    logging.warning(
                        "Skipping dataset %s because %s is missing", dataset, source_dir
                    )
                    continue

                for path in sorted(source_dir.glob("*.json")):
                    # Apply file filter if specified
                    if file_filter and path.name not in file_filter:
                        continue
                    
                    target_name = f"{dataset}-{path.name}"
                    jobs.append(
                        ExtractionJob(
                            dataset=dataset,
                            source_path=path,
                            target_path=output_dir / target_name,
                        )
                    )

        if limit is not None and limit >= 0:
            jobs = jobs[:limit]

        return jobs

    async def request_extraction(
        self,
        client: OpenAI,
        *,
        model: str,
        prompt: str,
        system_prompt: str,
        temperature: float,
        max_output_tokens: int,
        images: Optional[List[Dict[str, Any]]] = None,
        retries: int = 3,
    ) -> Tuple[BaseModel, Optional[Mapping[str, object]], Optional[str]]:
        """Call Azure OpenAI with structured output and return parsed response.

        Args:
            client: OpenAI client instance
            model: Model/deployment name
            prompt: User prompt content
            system_prompt: System prompt content
            temperature: Sampling temperature
            max_output_tokens: Maximum response tokens
            images: Optional list of image content blocks for vision
            retries: Number of retry attempts

        Returns:
            Tuple of (parsed response model, usage dict, response ID)

        Raises:
            RuntimeError: If all retries fail
        """
        backoff = 2.0
        last_error: Optional[str] = None

        # Build user content - text only or multimodal
        if images:
            # Multimodal: text + images (Azure Responses API uses 'input_text' type)
            user_content: List[Dict[str, Any]] = [{"type": "input_text", "text": prompt}]
            user_content.extend(images)
        else:
            # Text only
            user_content = prompt  # type: ignore

        for attempt in range(1, retries + 1):
            try:
                loop = asyncio.get_running_loop()
                call = partial(
                    client.responses.parse,
                    model=model,
                    input=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    text_format=self.config.response_model,
                    temperature=temperature,
                    max_output_tokens=max_output_tokens,
                )
                response = await loop.run_in_executor(None, call)

                analysis = response.output_parsed
                if analysis is None:
                    raise ValueError("No structured output returned")
                usage = None
                if getattr(response, "usage", None):
                    usage_obj = response.usage
                    if hasattr(usage_obj, "model_dump"):
                        usage = usage_obj.model_dump() # type: ignore
                    else:
                        usage = json.loads(json.dumps(usage_obj))
                return analysis, usage, getattr(response, "id", None)

            except RateLimitError as exc:
                last_error = str(exc)
                wait_time = 60.0  # Azure rate limits benefit from longer waits
                logging.warning(
                    "Rate limited (attempt %d/%d), waiting %.0fs: %s",
                    attempt,
                    retries,
                    wait_time,
                    exc,
                )
                await asyncio.sleep(wait_time)

            except (OpenAIError, ValidationError) as exc:
                last_error = str(exc)
                logging.warning(
                    "Extraction attempt %d/%d failed: %s", attempt, retries, exc
                )
                if attempt < retries:
                    wait_time = backoff + random.random()
                    await asyncio.sleep(wait_time)
                    backoff *= 2

        raise RuntimeError(last_error or "Unknown Azure OpenAI failure")

    async def process_job(
        self,
        job: ExtractionJob,
        *,
        client: Optional[OpenAI],
        model: str,
        temperature: float,
        max_output_tokens: int,
        semaphore: asyncio.Semaphore,
        overwrite: bool,
        dry_run: bool,
    ) -> str:
        """Process a single extraction job.

        Args:
            job: ExtractionJob to process
            client: OpenAI client (None for dry run)
            model: Model name
            temperature: Sampling temperature
            max_output_tokens: Max response tokens
            semaphore: Concurrency limiter
            overwrite: Whether to overwrite existing files
            dry_run: Whether to skip actual API calls

        Returns:
            Status string: 'success', 'skipped', 'empty', 'error', 'dry_run'
        """
        if not overwrite and job.target_path.exists():
            logging.debug("Skipping %s (already exists)", job.target_path.name)
            return "skipped"

        try:
            data = _read_json(job.source_path)
        except (json.JSONDecodeError, IOError) as exc:
            logging.error("Failed to read %s: %s", job.source_path, exc)
            return "error"

        # Extract fields from source data
        title = str(data.get("title") or job.source_path.stem).strip() or "Untitled"
        date = str(data.get("date") or data.get("reported_date") or "").strip() or None
        content = str(
            data.get("content") or data.get("narrative") or data.get("text") or ""
        ).strip()
        source_url = str(data.get("source_url") or data.get("url") or "").strip() or None
        
        # Extract image URLs from metadata if available
        metadata = data.get("metadata", {})
        if isinstance(metadata, dict):
            image_urls: List[str] = metadata.get("image_urls", [])
        else:
            image_urls = []

        # Allow posts with images even if no text content (for image-only posts)
        if not content and not image_urls:
            logging.warning("No content or images in %s; skipping", job.source_path)
            return "empty"

        prompt = build_user_prompt(
            title=title,
            date=date,
            dataset=job.dataset,
            source_url=source_url,
            content=content if content else "(No text content - see attached images)",
            suffix=self.config.user_prompt_suffix,
        )

        checksum = sha256(content.encode("utf-8")).hexdigest()

        # Fetch images if enabled and URLs available
        images: Optional[List[Dict[str, Any]]] = None
        images_included: List[str] = []
        if self.config.enable_images and image_urls:
            images = await fetch_images_for_extraction(
                image_urls=image_urls,
                max_images=self.config.max_images,
                cache_dir=self.config.image_cache_dir,
                detail=self.config.image_detail,
            )
            if images:
                images_included = image_urls[:len(images)]
                logging.debug("Including %d images for %s", len(images), job.source_path.name)

        if dry_run:
            img_msg = f" (with {len(images_included)} images)" if images_included else ""
            logging.info("Dry-run: would extract %s%s", job.source_path, img_msg)
            return "dry_run"

        if client is None:
            raise RuntimeError("Azure OpenAI client required when not in dry-run mode")

        async with semaphore:
            try:
                analysis, usage, response_id = await self.request_extraction(
                    client,
                    model=model,
                    prompt=prompt,
                    system_prompt=self.config.system_prompt,
                    temperature=temperature,
                    max_output_tokens=max_output_tokens,
                    images=images,
                )
            except Exception as exc:
                logging.error("Extraction failed for %s: %s", job.source_path, exc)
                return "error"

        # Build output payload
        payload = {
            "dataset": job.dataset,
            "source_file": str(job.source_path),
            "source_url": source_url,
            "title": title,
            "date": date,
            "content_checksum": checksum,
            "extraction_model": model,
            "extraction_timestamp": datetime.now(timezone.utc).isoformat(),
            "schema": self.schema_name,
            "images_included": images_included,
            "extraction": analysis.model_dump(mode="json"),
            "response_id": response_id,
            "usage": usage,
        }

        job.target_path.parent.mkdir(parents=True, exist_ok=True)
        job.target_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        logging.info("Extracted %s -> %s", job.source_path.name, job.target_path.name)
        return "success"

    async def run_pipeline(self, args: argparse.Namespace) -> Dict[str, int]:
        """Run the extraction pipeline.

        Args:
            args: Parsed command line arguments

        Returns:
            Dictionary of status counts
        """
        datasets = args.datasets or list(self.config.supported_datasets)
        jobs = self.collect_jobs(datasets, limit=args.limit, file_filter=args.files)

        if not jobs:
            logging.warning("No files found to process.")
            return {}

        logging.info("Collected %d jobs to process.", len(jobs))

        client: Optional[OpenAI] = None
        model_name = args.model or "dry-run"

        if not args.dry_run:
            secrets_path = Path(args.secrets_path) if args.secrets_path else self.config.secrets_path
            creds = load_azure_credentials(secrets_path)
            client, model_name = create_azure_client(creds, args.model)

        semaphore = asyncio.Semaphore(max(1, args.max_concurrency))

        tasks = [
            asyncio.create_task(
                self.process_job(
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

        stats: Dict[str, int] = {}
        for task in asyncio.as_completed(tasks):
            status = await task
            stats[status] = stats.get(status, 0) + 1

        return stats

    def create_parser(self, description: Optional[str] = None) -> argparse.ArgumentParser:
        """Create argument parser for the extractor.

        Args:
            description: Optional parser description

        Returns:
            Configured ArgumentParser
        """
        parser = argparse.ArgumentParser(
            description=description or f"Structured extraction using {self.schema_name}",
        )
        parser.add_argument(
            "--datasets",
            nargs="+",
            default=list(self.config.supported_datasets),
            choices=list(self.config.supported_datasets),
            help="Datasets to process (default: all).",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Maximum number of files to process.",
        )
        parser.add_argument(
            "--files",
            nargs="+",
            default=None,
            help="Specific file names to extract (e.g., 'i-tried-to-scream.json'). Filters across all selected datasets.",
        )
        parser.add_argument(
            "--max-concurrency",
            type=int,
            default=10,
            help="Maximum concurrent Azure OpenAI calls (default: 10).",
        )
        parser.add_argument(
            "--temperature",
            type=float,
            default=0.7,
            help="Sampling temperature (default: 0.7).",
        )
        parser.add_argument(
            "--max-output-tokens",
            type=int,
            default=10000,
            help="Maximum response tokens (default: 10000).",
        )
        parser.add_argument(
            "--model",
            type=str,
            default=None,
            help="Override Azure OpenAI deployment name.",
        )
        parser.add_argument(
            "--secrets-path",
            type=str,
            default=None,
            help="Path to azure_openai.env file.",
        )
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Re-extract even if output exists.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="List files without calling Azure OpenAI.",
        )
        parser.add_argument(
            "--log-level",
            default="INFO",
            choices=["DEBUG", "INFO", "WARNING", "ERROR"],
            help="Logging verbosity (default: INFO).",
        )
        return parser

    def run(self, argv: Optional[Sequence[str]] = None) -> None:
        """Main entry point for the extractor.

        Args:
            argv: Optional command line arguments (defaults to sys.argv)
        """
        parser = self.create_parser()
        args = parser.parse_args(argv)

        logging.basicConfig(
            level=getattr(logging, args.log_level),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        
        # Suppress noisy third-party loggers
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("openai").setLevel(logging.WARNING)

        try:
            stats = asyncio.run(self.run_pipeline(args))
        except KeyboardInterrupt:
            logging.error("Interrupted by user")
            raise SystemExit(1)
        except Exception as exc:
            logging.error("Pipeline aborted: %s", exc)
            raise SystemExit(1)

        if not stats:
            logging.info("No work performed.")
            return

        summary = ", ".join(f"{k}={v}" for k, v in sorted(stats.items()))
        logging.info("Extraction complete: %s", summary)
