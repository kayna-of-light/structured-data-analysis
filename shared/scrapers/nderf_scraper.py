"""
NDERF (Near Death Experience Research Foundation) scraper.

Scrapes experiences from nderf.org via both:
1. Static HTML pages (/Experiences/*.html)
2. JSON API endpoint (search.nderf.org/api/experience)

Usage:
    from shared.scrapers import nderf
    
    scraper = nderf.NDERFScraper(output_dir=Path("data"))
    scraper.scrape_all()
    
    # Or scrape specific targets
    scraper.scrape_targets(["12345", "https://www.nderf.org/..."])
"""

import argparse
import functools
import json
import posixpath
import re
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qs, parse_qsl, urljoin, urlparse, urlunparse, urlencode

from bs4 import BeautifulSoup, NavigableString, Tag

from .base import (
    BaseScraper,
    ScrapedCase,
    http_get,
    slugify,
    clean_text,
    pad_id,
    logger,
    REQUEST_DELAY,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

INDEX_PAGES = [
    "https://www.nderf.org/site_index.htm",
    "https://www.nderf.org/site_index_2.htm",
    "https://www.nderf.org/site_index_3.htm",
    "https://www.nderf.org/site_index_4.htm",
]
ARCHIVE_ROOT = "https://www.nderf.org/Archives/NDERF_NDEs.html"
ARCHIVE_LIST_PAGE = "https://www.nderf.org/Archives/archivelist.htm"
API_ENDPOINT = "https://search.nderf.org/api/experience"
DEFAULT_WORKERS = 8


# =============================================================================
# HELPER DATACLASS
# =============================================================================

@dataclass
class DetailTask:
    """Task representing a single page to scrape."""
    url: str
    kind: str  # "static" or "api"
    entry_id: Optional[str] = None


# =============================================================================
# URL UTILITIES
# =============================================================================

def normalize_html(html: str) -> str:
    """Strip garbage before HTML doctype/structure."""
    stripped = html.lstrip()
    lower = stripped.lower()
    for token in ("<!doctype", "<html", "<head", "<body"):
        idx = lower.find(token)
        if idx > 0:
            stripped = stripped[idx:]
            lower = stripped.lower()
            break
    return stripped


def fetch_soup(url: str) -> BeautifulSoup:
    """Fetch URL and return parsed BeautifulSoup."""
    html = normalize_html(http_get(url).text)
    soup = BeautifulSoup(html, "lxml")
    if soup.find("body") is None or len(soup.get_text("", strip=True)) < 40:
        soup = BeautifulSoup(html, "html.parser")
    return soup


def canonicalize_url(url: str) -> str:
    """Normalize NDERF URL for deduplication."""
    parsed = urlparse(url)
    scheme = "https"
    netloc = parsed.netloc.lower()
    if netloc in {"nderf.org", "www.nderf.org"}:
        netloc = "www.nderf.org"
    path = parsed.path or "/"
    path = posixpath.normpath(path)
    if not path.startswith("/"):
        path = "/" + path
    if parsed.path.endswith("/") and not path.endswith("/"):
        path += "/"
    query = ""
    if parsed.query:
        pairs = [(key.lower(), value) for key, value in parse_qsl(parsed.query, keep_blank_values=True)]
        query = urlencode(sorted(pairs))
    return urlunparse((scheme, netloc, path, "", query, ""))


def is_api_link(url: str) -> bool:
    """Check if URL is an API-style experience link."""
    lower = url.lower()
    if "experience.html" in lower and "entrynum=" in lower:
        return True
    return lower.startswith(API_ENDPOINT.lower())


def is_static_link(url: str) -> bool:
    """Check if URL is a static experience page."""
    lower = url.lower()
    return "/experiences/" in lower and lower.endswith(".html")


def is_archive_link(url: str) -> bool:
    """Check if URL is an archive listing page."""
    lower = url.lower()
    return "/archives/" in lower and lower.endswith(".html")


def parse_entrynum(url: str) -> Optional[str]:
    """Extract ENTRYNUM parameter from URL."""
    query = parse_qs(urlparse(url).query)
    if "ENTRYNUM" in query:
        return query["ENTRYNUM"][0]
    if "entrynum" in query:
        return query["entrynum"][0]
    return None


# =============================================================================
# LINK COLLECTION
# =============================================================================

def fetch_archive_pages() -> set[str]:
    """Collect all archive listing page URLs."""
    pages: set[str] = set()
    try:
        soup = fetch_soup(ARCHIVE_LIST_PAGE)
    except Exception as exc:
        logger.warning(f"Failed to fetch archive list {ARCHIVE_LIST_PAGE}: {exc}")
        return {canonicalize_url(ARCHIVE_ROOT)}

    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if not href:
            continue
        url = canonicalize_url(urljoin(ARCHIVE_LIST_PAGE, href))
        if is_archive_link(url):
            pages.add(url)
    if not pages:
        pages.add(canonicalize_url(ARCHIVE_ROOT))
    return pages


def collect_listing_links() -> Tuple[set[str], set[str], set[str]]:
    """Collect all experience URLs from index and archive pages."""
    static_urls: set[str] = set()
    api_urls: set[str] = set()
    archive_pages: set[str] = fetch_archive_pages()

    for page_url in INDEX_PAGES:
        soup = fetch_soup(page_url)
        anchors = soup.select("ul.sitemap_list a") or soup.find_all("a")
        for anchor in anchors:
            href = anchor.get("href")
            if not href:
                continue
            url = canonicalize_url(urljoin(page_url, href))
            if is_api_link(url):
                api_urls.add(url)
            elif is_static_link(url):
                static_urls.add(url)
            elif is_archive_link(url):
                archive_pages.add(url)
    return static_urls, api_urls, archive_pages


def collect_archive_links(archive_pages: Iterable[str]) -> Tuple[set[str], set[str]]:
    """Collect experience URLs from archive pages."""
    static_urls: set[str] = set()
    api_urls: set[str] = set()
    for page_url in archive_pages:
        try:
            soup = fetch_soup(page_url)
        except Exception as exc:
            logger.warning(f"Failed to fetch archive {page_url}: {exc}")
            continue
        for anchor in soup.find_all("a"):
            href = anchor.get("href")
            if not href:
                continue
            url = canonicalize_url(urljoin(page_url, href))
            if is_api_link(url):
                api_urls.add(url)
            elif is_static_link(url):
                static_urls.add(url)
    return static_urls, api_urls


def build_tasks(static_urls: set[str], api_urls: set[str]) -> List[DetailTask]:
    """Build list of scraping tasks from collected URLs."""
    tasks: List[DetailTask] = []
    for url in sorted(static_urls):
        tasks.append(DetailTask(url=url, kind="static"))
    for url in sorted(api_urls):
        entry_id = parse_entrynum(url)
        tasks.append(DetailTask(url=url, kind="api", entry_id=entry_id))
    return tasks


# =============================================================================
# HTML PARSING UTILITIES
# =============================================================================

TITLE_ID_PATTERN = re.compile(
    r"^(?P<title>.+?)\s+(?:NDE(?:-Like)?|ADC|OBE)\s+(?P<id>\d+)$",
    re.IGNORECASE,
)
BREADCRUMB_NUMBER_PATTERN = re.compile(r"(\d+)")
LEADING_HEADING_PATTERN = re.compile(
    r"^(experience description|background information|nde elements)[:\-\s]*",
    re.IGNORECASE,
)


def extract_title_and_id(soup: BeautifulSoup, fallback: str) -> tuple[str, Optional[str]]:
    """Extract title and ID from page."""
    raw_title = fallback
    if soup.title and soup.title.string:
        raw_title = clean_text(soup.title.string)
    else:
        heading = soup.select_one("h1, h2, h3")
        if heading:
            raw_title = clean_text(heading.get_text(" ", strip=True))

    match = TITLE_ID_PATTERN.match(raw_title)
    if match:
        return match.group("title").strip(" -"), match.group("id")
    return raw_title or "NDERF Experience", None


def ensure_title_has_nde_suffix(title: str, nde_code: Optional[str]) -> str:
    """Ensure title includes NDE code suffix."""
    title = (title or "NDERF Experience").strip()
    if not nde_code:
        return title
    nde_phrase = f"nde {nde_code}".lower()
    if nde_phrase in title.lower():
        return title
    if title.lower().endswith(" nde"):
        return f"{title} {nde_code}"
    return f"{title} NDE {nde_code}"


def extract_numeric_id(*candidates: Optional[str]) -> Optional[str]:
    """Extract first numeric ID from candidates."""
    for text in candidates:
        if not text:
            continue
        match = re.search(r"(\d+)", text)
        if match:
            return match.group(1)
    return None


def extract_breadcrumb_codes(soup: BeautifulSoup) -> Tuple[Optional[str], Optional[str]]:
    """Extract ID codes from breadcrumb navigation."""
    crumb = soup.select_one("ul.breadcrumbs li:last-child")
    if not crumb:
        return None, None
    text = clean_text(crumb.get_text(" ", strip=True))
    if not text:
        return None, None
    numbers = BREADCRUMB_NUMBER_PATTERN.findall(text)
    if not numbers:
        return None, None
    start_code = numbers[0]
    end_code = numbers[-1]
    if start_code == end_code:
        end_code = None
    return start_code, end_code


def select_content_section(soup: BeautifulSoup) -> Tag:
    """Select the main content container."""
    for selector in [
        "section.section_offset",
        "div.section_offset",
        "div.container",
        "body",
    ]:
        node = soup.select_one(selector)
        if node:
            return node
    return soup


def looks_like_question_span(span: Tag) -> bool:
    """Check if span appears to be a Q&A question."""
    style = (span.get("style") or "").lower()
    class_list = [c.lower() for c in span.get("class", [])]
    if "#009999" in style:
        return True
    if any(c == "exp-p" for c in class_list):
        return True
    if any(c.startswith("m") and c[1:].isdigit() and c != "m103" for c in class_list):
        return True

    text = clean_text(span.get_text(" ", strip=True))
    if not text:
        return False
    lower = text.lower()
    if lower.startswith("experience description"):
        return True
    if lower.startswith("background information"):
        return True
    if lower.startswith("nde elements"):
        return True
    if len(text) <= 180 and (text.endswith(":") or text.endswith("?")):
        return True
    return False


def get_node_text(node) -> str:
    """Get text from BeautifulSoup node."""
    if isinstance(node, NavigableString):
        return clean_text(str(node))
    if isinstance(node, Tag):
        return clean_text(node.get_text(" ", strip=True))
    return ""


def extract_content_from_section(section: Tag) -> str:
    """Extract narrative content from page section."""
    def strip_heading(text: str) -> str:
        return re.sub(
            r"^(experience description|background information|nde elements)[:\-\s]*",
            "",
            text,
            flags=re.IGNORECASE,
        ).strip()

    exp_span: Optional[Tag] = None
    for span in section.find_all("span"):
        value = clean_text(span.get_text(" ", strip=True))
        if value.lower().startswith("experience description"):
            exp_span = span
            break

    paragraphs: List[str] = []
    if exp_span:
        first_text = strip_heading(clean_text(exp_span.get_text(" ", strip=True)))
        if first_text:
            paragraphs.append(first_text)
        for sibling in exp_span.next_siblings:
            if isinstance(sibling, NavigableString):
                snippet = clean_text(str(sibling))
            elif isinstance(sibling, Tag):
                if looks_like_question_span(sibling):
                    break
                snippet = clean_text(sibling.get_text(" ", strip=True))
            else:
                snippet = ""
            if not snippet:
                continue
            lower = snippet.lower()
            if lower.startswith("background information") or lower.startswith("nde elements"):
                break
            paragraphs.append(snippet)
        if paragraphs:
            return "\n\n".join(paragraphs).strip()

    # Fallback: Extract everything before "background information"
    section_html = str(section)
    lower_html = section_html.lower()
    marker = "background information"
    idx = lower_html.find(marker)
    if idx != -1:
        desc_html = section_html[:idx]
    else:
        desc_html = section_html
    frag = BeautifulSoup(desc_html, "lxml")
    fallback: List[str] = []
    for tag in frag.find_all(["p", "div", "blockquote", "span"]):
        if tag.name == "span" and looks_like_question_span(tag):
            continue
        text = clean_text(tag.get_text(" ", strip=True))
        if not text:
            continue
        lower_text = text.lower()
        if lower_text.startswith("background information") or lower_text.startswith("nde elements"):
            break
        if lower_text.startswith("experience description"):
            text = strip_heading(text)
            if not text:
                continue
        fallback.append(text)
    return "\n\n".join(fallback).strip()


def trim_leading_heading(text: str) -> str:
    """Remove leading heading markers from text."""
    text = text.lstrip()
    while True:
        match = LEADING_HEADING_PATTERN.match(text)
        if not match:
            break
        text = text[match.end():].lstrip(" -:\u00a0")
    return text


def collect_answer(span: Tag) -> str:
    """Collect answer text following a question span."""
    parts: List[str] = []
    for sibling in span.next_siblings:
        if isinstance(sibling, Tag):
            if sibling.name == "br":
                if parts:
                    break
                continue
            if sibling.name == "span" and looks_like_question_span(sibling):
                break
            text = get_node_text(sibling)
        else:
            text = clean_text(str(sibling))
        if text:
            parts.append(text)
    if parts:
        return clean_text(" ".join(parts)).strip(" -:\u00a0")

    parent = span.parent
    if parent:
        parent_text = clean_text(parent.get_text(" ", strip=True))
        question_text = clean_text(span.get_text(" ", strip=True))
        remainder = parent_text[len(question_text):].strip(" -:\u00a0")
        if remainder:
            return remainder
    return ""


def extract_elements(section: Tag) -> "OrderedDict[str, str]":
    """Extract Q&A elements from section."""
    elements: "OrderedDict[str, str]" = OrderedDict()
    for span in section.find_all("span"):
        if not looks_like_question_span(span):
            continue
        question = clean_text(span.get_text(" ", strip=True)).rstrip(":").strip()
        if not question:
            continue
        lower_question = question.lower()
        if "experience description" in lower_question:
            continue
        if "background information" in lower_question:
            continue
        if "nde elements" in lower_question:
            continue
        answer = collect_answer(span)
        if not answer:
            continue
        if question in elements:
            existing = elements[question]
            if answer not in existing:
                elements[question] = f"{existing} | {answer}"
        else:
            elements[question] = answer
    return elements


DATE_KEYS = [
    "Date NDE Occurred",
    "Date Of NDE",
    "Date NDE Occurred (if known)",
    "Date NDE Occurred?",
    "Date NDE Occured",
    "Date",
    "Date Posted",
]


def pick_date(elements: Dict[str, str], fallback: Optional[str] = None) -> Optional[str]:
    """Find date from Q&A elements."""
    for key in DATE_KEYS:
        if key in elements and elements[key]:
            return elements[key]
    return fallback


# =============================================================================
# RECORD PARSING
# =============================================================================

def parse_static_record(task: DetailTask) -> Optional[dict]:
    """Parse a static HTML experience page."""
    soup = fetch_soup(task.url)
    url_path = Path(urlparse(task.url).path)
    fallback_title = clean_text(url_path.stem.replace("_", " ").replace("-", " ")).title() or "NDERF Experience"
    title, derived_id = extract_title_and_id(soup, fallback_title)
    breadcrumb_id, breadcrumb_nde_code = extract_breadcrumb_codes(soup)
    section = select_content_section(soup)
    content = extract_content_from_section(section)
    elements = extract_elements(section)
    entry_id = breadcrumb_id or derived_id or extract_numeric_id(title, task.url)
    if not entry_id:
        entry_id = slugify(url_path.stem)
    nde_code = breadcrumb_nde_code or derived_id or ""
    title = ensure_title_has_nde_suffix(title, nde_code)
    gender = elements.get("Gender")
    date = pick_date(elements)
    if not content:
        content = clean_text(section.get_text(" ", strip=True))
    content = trim_leading_heading(content)
    return {
        "id": entry_id,
        "nde_code": nde_code or "",
        "title": title,
        "date": date or "",
        "gender": gender or "",
        "content": content,
        "elements": elements,
        "source_url": task.url,
    }


def fetch_api_payload(entry_id: str) -> dict:
    """Fetch experience data from API."""
    url = f"{API_ENDPOINT}?ENTRYNUM={entry_id}"
    response = http_get(url)
    return response.json()


def parse_api_record(task: DetailTask) -> Optional[dict]:
    """Parse an API-sourced experience."""
    entry_id = task.entry_id or parse_entrynum(task.url)
    if not entry_id:
        raise ValueError(f"Missing ENTRYNUM for {task.url}")
    payload = fetch_api_payload(entry_id)
    experiences = payload.get("experiences") or []
    if not experiences:
        return None
    experience = experiences[0]
    qa_items = experience.get("qa") or []
    elements: "OrderedDict[str, str]" = OrderedDict()
    for item in qa_items:
        question = item.get("p")
        answer = item.get("a")
        if question and answer:
            elements[clean_text(str(question))] = clean_text(str(answer))
    date = pick_date(elements, experience.get("POSTDATE") or experience.get("EXPDATE"))
    gender = payload.get("GENDER") or elements.get("Gender")
    content = clean_text(experience.get("EXPERIENCE", ""))
    title = payload.get("POSTNAME") or payload.get("alias") or f"NDERF Entry {entry_id}"
    return {
        "id": entry_id,
        "nde_code": "",
        "title": title,
        "date": date or "",
        "gender": gender or "",
        "content": content,
        "elements": elements,
        "source_url": task.url,
    }


# =============================================================================
# SCRAPER CLASS
# =============================================================================

class NDERFScraper(BaseScraper):
    """
    Scraper for NDERF (Near Death Experience Research Foundation).
    
    Scrapes experiences from nderf.org via both static HTML pages
    and the JSON API endpoint.
    
    Attributes:
        source_name: "nderf"
        output_subdir: "nderf"
    """
    
    source_name = "nderf"
    output_subdir = "nderf"
    
    def __init__(self, output_dir: Path, workers: int = DEFAULT_WORKERS):
        """
        Initialize NDERF scraper.
        
        Args:
            output_dir: Base directory for output
            workers: Number of concurrent worker threads
        """
        super().__init__(output_dir)
        self.workers = workers
    
    def scrape_all(
        self,
        limit: Optional[int] = None,
        replace_existing: bool = False,
    ) -> List[ScrapedCase]:
        """
        Scrape all experiences from NDERF.
        
        Args:
            limit: Maximum number of experiences to scrape
            replace_existing: Whether to overwrite existing files
            
        Returns:
            List of scraped cases
        """
        self.logger.info("Collecting listing links...")
        index_static, index_api, archive_pages = collect_listing_links()
        archive_static, archive_api = collect_archive_links(archive_pages)
        
        static_urls = index_static | archive_static
        api_urls = index_api | archive_api
        tasks = build_tasks(static_urls, api_urls)
        
        self.logger.info(
            f"Discovered {len(static_urls)} static pages, {len(api_urls)} API entries, "
            f"{len(tasks)} total tasks"
        )
        
        if limit is not None:
            tasks = tasks[:limit]
        
        return self._process_tasks(tasks, replace_existing)
    
    def scrape_targets(
        self,
        targets: List[str],
        replace_existing: bool = True,
    ) -> List[ScrapedCase]:
        """
        Scrape specific targets (URLs or entry IDs).
        
        Args:
            targets: List of URLs or entry IDs to scrape
            replace_existing: Whether to overwrite existing files
            
        Returns:
            List of scraped cases
        """
        tasks = self._build_manual_tasks(targets)
        self.logger.info(f"Processing {len(tasks)} targeted pages")
        return self._process_tasks(tasks, replace_existing)
    
    def _build_manual_tasks(self, targets: List[str]) -> List[DetailTask]:
        """Build tasks from manual target list."""
        tasks: List[DetailTask] = []
        seen: set[tuple[str, str]] = set()
        
        for token in targets:
            token = token.strip()
            if not token or token.startswith("#"):
                continue
            task = self._task_from_token(token)
            if task:
                key = (task.kind, canonicalize_url(task.url))
                if key not in seen:
                    seen.add(key)
                    tasks.append(task)
        
        return tasks
    
    def _task_from_token(self, token: str) -> Optional[DetailTask]:
        """Create task from URL or entry ID."""
        if not token:
            return None
        if token.startswith("http://") or token.startswith("https://"):
            url = canonicalize_url(token)
            if is_api_link(url):
                entry_id = parse_entrynum(url)
                return DetailTask(url=url, kind="api", entry_id=entry_id)
            if is_static_link(url):
                return DetailTask(url=url, kind="static")
            raise ValueError(f"Unrecognized NDERF URL: {token}")
        if token.isdigit():
            entry_id = token
            url = canonicalize_url(f"https://www.nderf.org/experience.html?entrynum={entry_id}")
            return DetailTask(url=url, kind="api", entry_id=entry_id)
        raise ValueError(f"Unsupported target token: {token}")
    
    def _process_tasks(
        self,
        tasks: List[DetailTask],
        replace_existing: bool,
    ) -> List[ScrapedCase]:
        """Process list of scraping tasks with concurrent workers."""
        if not tasks:
            self.logger.info("No tasks to process")
            return []
        
        results: List[ScrapedCase] = []
        written = 0
        
        worker_fn = functools.partial(
            self._process_single_task,
            replace_existing=replace_existing,
        )
        
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = [executor.submit(worker_fn, task) for task in tasks]
            for future in as_completed(futures):
                result = future.result()
                if result["status"] == "ok":
                    written += 1
                    case = result["case"]
                    results.append(case)
                    self.logger.info(f"[{written}] {result['task'].kind.upper()} saved -> {result['path']}")
                elif result["status"] == "skip":
                    self.logger.debug(f"Skipping {result['task'].url} (no record)")
                else:
                    self.logger.error(f"Failed to process {result['task'].url}: {result.get('error')}")
        
        self.logger.info(f"Finished writing {written} JSON files to {self.output_dir}")
        return results
    
    def _process_single_task(
        self,
        task: DetailTask,
        replace_existing: bool = False,
    ) -> Dict:
        """Process a single scraping task."""
        try:
            if task.kind == "static":
                record = parse_static_record(task)
            else:
                record = parse_api_record(task)
            
            if not record:
                return {"status": "skip", "task": task}
            
            case = self._record_to_case(record)
            path = self._save_case(case, replace_existing)
            return {"status": "ok", "task": task, "case": case, "path": path}
            
        except Exception as exc:
            return {"status": "error", "task": task, "error": exc}
    
    def _record_to_case(self, record: dict) -> ScrapedCase:
        """Convert parsed record to ScrapedCase."""
        return ScrapedCase(
            source="nderf",
            source_id=record["id"],
            url=record["source_url"],
            title=record["title"],
            content=record["content"],
            date_published=record.get("date"),
            metadata={
                "nde_code": record.get("nde_code", ""),
                "gender": record.get("gender", ""),
                "elements": record.get("elements", {}),
            },
        )
    
    def _save_case(self, case: ScrapedCase, replace_existing: bool) -> Path:
        """Save case to output directory."""
        title_slug = slugify(case.title)
        record_id = pad_id(case.source_id)
        
        if record_id:
            filename = f"{record_id}_{title_slug or 'experience'}.json"
        else:
            filename = f"{title_slug or 'experience'}.json"
        
        if replace_existing:
            path = self.output_dir / filename
        else:
            path = self.ensure_unique_path(filename.replace(".json", ""))
        
        return case.save(self.output_dir, path.name)


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    """Command-line entry point for NDERF scraper."""
    parser = argparse.ArgumentParser(description="Scrape NDERF experiences")
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("data"),
        help="Output directory (default: data)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only process the first N experiences (useful for testing)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help="Number of worker threads (default: %(default)s)",
    )
    parser.add_argument(
        "--target",
        dest="targets",
        action="append",
        help="Specific URL or ENTRYNUM to download (can be repeated)",
    )
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Overwrite previously downloaded files",
    )
    args = parser.parse_args()
    
    scraper = NDERFScraper(output_dir=args.output, workers=args.workers)
    
    if args.targets:
        scraper.scrape_targets(args.targets, replace_existing=args.replace_existing)
    else:
        scraper.scrape_all(limit=args.limit, replace_existing=args.replace_existing)


if __name__ == "__main__":
    main()
