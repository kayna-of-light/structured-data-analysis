"""
Base scraper utilities shared across all data sources.
"""

import json
import logging
import re
import time
import threading
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/118.0 Safari/537.36"
)
REQUEST_DELAY = 0.5  # Default delay between requests
MAX_RETRIES = 5
RETRY_BACKOFF_BASE = 1.0

# Thread-local session storage
thread_local = threading.local()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_session() -> requests.Session:
    """Get thread-local requests session with proper headers."""
    session = getattr(thread_local, "session", None)
    if session is None:
        session = requests.Session()
        session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        thread_local.session = session
    return session


def http_get(url: str, delay: float = REQUEST_DELAY, timeout: int = 90) -> requests.Response:
    """
    Fetch URL with retry logic and rate limiting.
    
    Args:
        url: URL to fetch
        delay: Delay after successful request
        timeout: Request timeout in seconds
        
    Returns:
        Response object
        
    Raises:
        requests.RequestException: If all retries fail
    """
    session = get_session()
    last_error: Optional[Exception] = None
    
    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(url, timeout=timeout)
            response.raise_for_status()
            
            # Fix encoding issues
            if response.encoding and response.encoding.lower() == "iso-8859-1":
                response.encoding = response.apparent_encoding or response.encoding
            
            time.sleep(delay)
            return response
            
        except requests.RequestException as exc:
            last_error = exc
            if attempt == MAX_RETRIES - 1:
                break
            backoff = RETRY_BACKOFF_BASE * (2 ** attempt)
            logger.warning(f"Request failed (attempt {attempt + 1}), retrying in {backoff}s: {exc}")
            time.sleep(backoff)
    
    raise last_error if last_error else RuntimeError(f"Failed to fetch {url}")


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:100] or "entry"


def clean_text(text: str) -> str:
    """Normalize whitespace in text."""
    return re.sub(r"\s+", " ", text).strip()


@dataclass
class ScrapedCase:
    """
    Standardized container for a scraped remission case.
    
    This provides a common schema across all data sources while preserving
    source-specific metadata.
    """
    # Core identifiers
    source: str  # e.g., "pmc", "rrp", "lourdes", "ions"
    source_id: str  # Unique ID within source (e.g., PMCID, profile slug)
    url: str  # Original source URL
    
    # Case metadata
    title: str
    date_scraped: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    date_published: Optional[str] = None
    
    # Content - the raw text/data
    content: str = ""  # Main narrative/article text
    
    # Medical details (when available)
    diagnosis: Optional[str] = None
    diagnosis_date: Optional[str] = None
    outcome: Optional[str] = None
    
    # Source-specific metadata stored as dict
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    def save(self, output_dir: Path, filename: Optional[str] = None) -> Path:
        """
        Save case to JSON file.
        
        Args:
            output_dir: Directory to save to
            filename: Optional custom filename (default: source_id.json)
            
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


class BaseScraper:
    """Base class for all remission data scrapers."""
    
    source_name: str = "base"
    output_subdir: str = "raw"
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir / self.output_subdir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(f"{__name__}.{self.source_name}")
    
    def scrape_all(self) -> List[ScrapedCase]:
        """Scrape all available cases. Override in subclasses."""
        raise NotImplementedError
    
    def save_case(self, case: ScrapedCase) -> Path:
        """Save a scraped case to the output directory."""
        return case.save(self.output_dir)
