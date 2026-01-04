"""
Base scraper utilities shared across all data sources.

This module provides:
- Thread-safe HTTP session management
- Retry logic with exponential backoff
- Common text processing utilities
- Base scraper class with standardized patterns
- ScrapedCase dataclass for uniform output schema
"""

import json
import logging
import re
import time
import threading
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

# =============================================================================
# CONFIGURATION
# =============================================================================

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/118.0 Safari/537.36"
)
REQUEST_DELAY = 0.5  # Default delay between requests (seconds)
MAX_RETRIES = 5
RETRY_BACKOFF_BASE = 1.0

# Thread-local session storage
_thread_local = threading.local()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# =============================================================================
# HTTP UTILITIES
# =============================================================================

def get_session() -> requests.Session:
    """
    Get thread-local requests session with proper headers.
    
    Creates a new session if one doesn't exist for the current thread.
    Sessions are reused within threads for connection pooling.
    
    Returns:
        Thread-local requests.Session instance
    """
    session = getattr(_thread_local, "session", None)
    if session is None:
        session = requests.Session()
        session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        _thread_local.session = session
    return session


def http_get(
    url: str,
    delay: float = REQUEST_DELAY,
    timeout: int = 90,
    max_retries: int = MAX_RETRIES,
) -> requests.Response:
    """
    Fetch URL with retry logic and rate limiting.
    
    Implements exponential backoff for transient failures and
    automatic encoding detection for pages with incorrect headers.
    
    Args:
        url: URL to fetch
        delay: Delay after successful request (seconds)
        timeout: Request timeout (seconds)
        max_retries: Maximum number of retry attempts
        
    Returns:
        Response object
        
    Raises:
        requests.RequestException: If all retries fail
    """
    session = get_session()
    last_error: Optional[Exception] = None
    
    for attempt in range(max_retries):
        try:
            response = session.get(url, timeout=timeout)
            response.raise_for_status()
            
            # Fix encoding issues - many pages declare ISO-8859-1 
            # even though the bytes are actually UTF-8
            if response.encoding and response.encoding.lower() == "iso-8859-1":
                response.encoding = response.apparent_encoding or response.encoding
            
            time.sleep(delay)
            return response
            
        except requests.RequestException as exc:
            last_error = exc
            if attempt == max_retries - 1:
                break
            backoff = RETRY_BACKOFF_BASE * (2 ** attempt)
            logger.warning(f"Request failed (attempt {attempt + 1}), retrying in {backoff}s: {exc}")
            time.sleep(backoff)
    
    raise last_error if last_error else RuntimeError(f"Failed to fetch {url}")


# =============================================================================
# TEXT PROCESSING UTILITIES
# =============================================================================

_SLUG_PATTERN = re.compile(r"[^a-z0-9]+")
_WHITESPACE_PATTERN = re.compile(r"\s+")


def slugify(text: str, max_length: int = 100) -> str:
    """
    Convert text to URL-safe slug.
    
    Args:
        text: Text to convert
        max_length: Maximum length of resulting slug
        
    Returns:
        Lowercase alphanumeric string with hyphens
    """
    text = text.lower()
    text = _SLUG_PATTERN.sub("-", text)
    text = text.strip("-")
    return text[:max_length] or "entry"


def clean_text(text: str) -> str:
    """
    Normalize whitespace in text.
    
    Collapses multiple whitespace characters to single space
    and strips leading/trailing whitespace.
    
    Args:
        text: Text to clean
        
    Returns:
        Cleaned text
    """
    return _WHITESPACE_PATTERN.sub(" ", text).strip()


def pad_id(record_id: str, width: int = 5) -> str:
    """
    Zero-pad numeric ID for consistent sorting.
    
    Args:
        record_id: ID to pad
        width: Minimum width
        
    Returns:
        Zero-padded ID if numeric, original otherwise
    """
    if record_id and record_id.isdigit():
        return record_id.zfill(width)
    return record_id


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class ScrapedCase:
    """
    Standardized container for a scraped case/experience.
    
    This provides a common schema across all data sources while preserving
    source-specific metadata. Used for both NDE experiences and remission cases.
    
    Attributes:
        source: Data source identifier (e.g., "nderf", "iands", "pmc")
        source_id: Unique ID within source (e.g., entry number, PMCID)
        url: Original source URL
        title: Title or name of the case
        content: Main narrative/text content
        date_scraped: ISO timestamp when scraped
        date_published: Original publication date if known
        metadata: Source-specific metadata as dict
    """
    # Core identifiers
    source: str
    source_id: str
    url: str
    
    # Case metadata
    title: str
    date_scraped: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    date_published: Optional[str] = None
    
    # Content
    content: str = ""
    
    # Source-specific metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    def save(self, output_dir: Path, filename: Optional[str] = None) -> Path:
        """
        Save case to JSON file.
        
        Args:
            output_dir: Directory to save to
            filename: Optional custom filename (default: {source_id}.json)
            
        Returns:
            Path to saved file
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if filename is None:
            filename = f"{slugify(self.source_id)}.json"
        
        filepath = output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
        
        return filepath


# =============================================================================
# BASE SCRAPER CLASS
# =============================================================================

class BaseScraper:
    """
    Base class for all data scrapers.
    
    Provides common functionality for output management, logging,
    and the scraping interface. Subclasses should override:
    - source_name: Identifier for this data source
    - output_subdir: Subdirectory name for output files
    - scrape_all(): Main scraping entry point
    
    Attributes:
        output_dir: Directory where scraped data is saved
        logger: Logger instance for this scraper
    """
    
    source_name: str = "base"
    output_subdir: str = "raw"
    
    def __init__(self, output_dir: Path):
        """
        Initialize scraper.
        
        Args:
            output_dir: Base output directory (subdir will be appended)
        """
        self.output_dir = output_dir / self.output_subdir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(f"{__name__}.{self.source_name}")
    
    def scrape_all(self) -> List[ScrapedCase]:
        """
        Scrape all available cases from this source.
        
        Subclasses must override this method.
        
        Returns:
            List of scraped cases
        """
        raise NotImplementedError("Subclasses must implement scrape_all()")
    
    def save_case(self, case: ScrapedCase) -> Path:
        """
        Save a scraped case to the output directory.
        
        Args:
            case: Case to save
            
        Returns:
            Path to saved file
        """
        return case.save(self.output_dir)
    
    def ensure_unique_path(self, base_slug: str, extension: str = ".json") -> Path:
        """
        Generate a unique file path, avoiding overwrites.
        
        If the base path exists, appends incrementing numbers
        until a unique path is found.
        
        Args:
            base_slug: Base filename (without extension)
            extension: File extension (default: .json)
            
        Returns:
            Unique file path
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        candidate = base_slug
        counter = 1
        while True:
            path = self.output_dir / f"{candidate}{extension}"
            if not path.exists():
                return path
            counter += 1
            candidate = f"{base_slug}-{counter:03d}"


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    # HTTP utilities
    "get_session",
    "http_get",
    # Text utilities
    "slugify",
    "clean_text",
    "pad_id",
    # Data structures
    "ScrapedCase",
    # Base classes
    "BaseScraper",
    # Logging
    "logger",
    # Constants
    "USER_AGENT",
    "REQUEST_DELAY",
    "MAX_RETRIES",
]
