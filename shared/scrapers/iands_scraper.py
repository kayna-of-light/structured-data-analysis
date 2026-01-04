"""
IANDS (International Association for Near-Death Studies) scraper.

Scrapes NDE accounts from the IANDS research database at research.iands.org.
Handles both standard article pages and archive pages containing multiple entries.

Usage:
    from shared.scrapers import iands
    
    scraper = iands.IANDSScraper(output_dir=Path("data"))
    scraper.scrape_all()
"""

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup, NavigableString, Tag

from .base import (
    BaseScraper,
    ScrapedCase,
    http_get,
    slugify,
    clean_text,
    logger,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

BASE_URL = "https://research.iands.org"
LIST_URL = (
    "https://research.iands.org/ndes/nde-stories/iands-nde-accounts.html?start={offset}"
)
LIST_PAGE_STEP = 100
MAX_OFFSET = 600


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class ListingEntry:
    """Entry from the IANDS listing page."""
    title: str
    date: str
    url: str


# =============================================================================
# LISTING COLLECTION
# =============================================================================

def fetch_listing(offset: int) -> List[ListingEntry]:
    """Fetch one page of the listing."""
    url = LIST_URL.format(offset=offset)
    soup = BeautifulSoup(http_get(url).text, "lxml")
    table = soup.select_one("table")
    entries: List[ListingEntry] = []
    if not table:
        return entries

    for row in table.select("tr"):
        cells = row.find_all("td")
        if len(cells) != 2:
            continue
        link = cells[0].find("a")
        if not link or not link.get("href"):
            continue
        title = link.get_text(strip=True)
        date = cells[1].get_text(strip=True)
        href = urljoin(BASE_URL, link["href"])
        entries.append(ListingEntry(title=title, date=date, url=href))
    return entries


def collect_all_listings() -> List[ListingEntry]:
    """Collect all entries from paginated listing."""
    entries: List[ListingEntry] = []
    seen_urls: set[str] = set()
    for offset in range(0, MAX_OFFSET + LIST_PAGE_STEP, LIST_PAGE_STEP):
        page_entries = fetch_listing(offset)
        if not page_entries:
            break
        for entry in page_entries:
            if entry.url in seen_urls:
                continue
            seen_urls.add(entry.url)
            entries.append(entry)
        if len(page_entries) < LIST_PAGE_STEP:
            break
    return entries


# =============================================================================
# PAGE PARSING UTILITIES
# =============================================================================

def select_title(soup: BeautifulSoup, fallback: str) -> str:
    """Extract title from page."""
    title_el = soup.select_one(".article-title h1") or soup.select_one("h1")
    return title_el.get_text(strip=True) if title_el else fallback


def select_date(soup: BeautifulSoup, fallback: str) -> str:
    """Extract date from page."""
    date_el = soup.select_one(".article-info time") or soup.select_one(".article-info .create")
    if date_el:
        return date_el.get_text(strip=True)
    return fallback


def gather_text_from_nodes(nodes: Iterable[Tag]) -> List[str]:
    """Extract text paragraphs from HTML nodes."""
    paragraphs: List[str] = []
    for node in nodes:
        if not isinstance(node, Tag):
            continue
        for script in node.select("script, style"):
            script.decompose()
        block_candidates = node.find_all(["p", "blockquote", "li", "h3", "h4"]) or [node]
        for block in block_candidates:
            text = block.get_text(" ", strip=True)
            cleaned = re.sub(r"\s+", " ", text).strip()
            if cleaned:
                paragraphs.append(cleaned)
    return paragraphs


# =============================================================================
# STANDARD ARTICLE PARSING
# =============================================================================

def parse_standard_article(soup: BeautifulSoup, entry: ListingEntry) -> dict:
    """Parse a standard single-entry article page."""
    title = select_title(soup, entry.title)
    date = select_date(soup, entry.date)

    nodes: List[Tag] = []
    intro = soup.select_one(".intro-text")
    if intro:
        nodes.append(intro)
    article_body = soup.select_one("[itemprop='articleBody']")
    if article_body and article_body is not intro:
        nodes.append(article_body)
    if not nodes:
        fallback = soup.select_one(".item-page")
        if fallback:
            nodes.append(fallback)

    paragraphs = gather_text_from_nodes(nodes)
    content = "\n\n".join(paragraphs).strip()
    return {"title": title, "date": date, "content": content, "url": entry.url}


# =============================================================================
# ARCHIVE PAGE PARSING
# =============================================================================

def split_archive_segments(container: Tag) -> List[str]:
    """Split archive page into individual entry segments."""
    segments: List[str] = []
    current: List[str] = []
    for child in container.children:
        if isinstance(child, NavigableString):
            if child.strip():
                current.append(str(child))
            continue
        if not isinstance(child, Tag):
            continue
        if child.name == "hr":
            if current:
                html = "".join(current).strip()
                if html:
                    segments.append(html)
                current = []
            continue
        current.append(str(child))
    if current:
        html = "".join(current).strip()
        if html:
            segments.append(html)
    return segments


def parse_archive_segment(html: str, archive_title: str, fallback_date: str, url: str) -> Optional[dict]:
    """Parse a single segment from an archive page."""
    frag = BeautifulSoup(html, "lxml")
    meta_span = None
    for span in frag.select("span"):
        text = span.get_text(" ", strip=True)
        if text.lower().startswith("by"):
            meta_span = span
            break
    if not meta_span:
        return None

    strongs = meta_span.find_all("strong")
    if not strongs:
        return None

    author = strongs[0].get_text(strip=True) if strongs else "Anonymous"
    date_text = strongs[1].get_text(strip=True) if len(strongs) > 1 else fallback_date
    meta_span.decompose()

    for img in frag.find_all("img"):
        img.decompose()

    paragraphs = gather_text_from_nodes(frag.find_all("p"))
    content = "\n\n".join(paragraphs).strip()
    if not content:
        content = frag.get_text("\n\n", strip=True)

    if not content:
        return None

    base_title = archive_title or "Archive entry"
    title = f"{base_title} - {author.strip() or 'Anonymous'}"
    if date_text:
        title = f"{title} ({date_text})"
    return {"title": title, "date": date_text, "content": content, "url": url}


def parse_archive_article(soup: BeautifulSoup, entry: ListingEntry) -> List[dict]:
    """Parse an archive page containing multiple entries."""
    container = soup.select_one(".intro-text") or soup.select_one(".item-page")
    if not container:
        return [parse_standard_article(soup, entry)]

    segments = split_archive_segments(container)
    records: List[dict] = []
    archive_title = select_title(soup, entry.title)
    for segment_html in segments:
        record = parse_archive_segment(segment_html, archive_title, entry.date, entry.url)
        if record:
            records.append(record)
    if not records:
        records.append(parse_standard_article(soup, entry))
    return records


def is_archive_page(entry: ListingEntry, soup: BeautifulSoup) -> bool:
    """Check if page is an archive containing multiple entries."""
    title_text = (select_title(soup, entry.title) or "").lower()
    return "archive through" in title_text or "archive-through" in entry.url.lower()


def fetch_entry_records(entry: ListingEntry) -> List[dict]:
    """Fetch and parse all records from a listing entry."""
    soup = BeautifulSoup(http_get(entry.url).text, "lxml")
    if is_archive_page(entry, soup):
        return parse_archive_article(soup, entry)
    return [parse_standard_article(soup, entry)]


# =============================================================================
# SCRAPER CLASS
# =============================================================================

class IANDSScraper(BaseScraper):
    """
    Scraper for IANDS (International Association for Near-Death Studies).
    
    Scrapes NDE accounts from the IANDS research database, handling
    both standard article pages and archive pages with multiple entries.
    
    Attributes:
        source_name: "iands"
        output_subdir: "iands"
    """
    
    source_name = "iands"
    output_subdir = "iands"
    
    def scrape_all(self, limit: Optional[int] = None) -> List[ScrapedCase]:
        """
        Scrape all entries from IANDS.
        
        Args:
            limit: Maximum number of listing entries to process
            
        Returns:
            List of scraped cases
        """
        self.logger.info("Collecting listing entries...")
        entries = collect_all_listings()
        self.logger.info(f"Discovered {len(entries)} listing entries")
        
        if limit is not None:
            entries = entries[:limit]
        
        results: List[ScrapedCase] = []
        total_written = 0
        
        for entry in entries:
            try:
                records = fetch_entry_records(entry)
            except Exception as exc:
                self.logger.error(f"Failed to fetch {entry.url}: {exc}")
                continue
            
            for idx, record in enumerate(records, start=1):
                slug_hint = slugify(entry.title)
                if len(records) > 1:
                    slug_hint = f"{slug_hint}-{idx:03d}"
                
                case = self._record_to_case(record, slug_hint)
                path = self._save_case(case, slug_hint)
                
                results.append(case)
                total_written += 1
                self.logger.info(f"  wrote {path}")
        
        self.logger.info(f"Finished writing {total_written} JSON files to {self.output_dir}")
        return results
    
    def _record_to_case(self, record: dict, slug_hint: str) -> ScrapedCase:
        """Convert parsed record to ScrapedCase."""
        return ScrapedCase(
            source="iands",
            source_id=slug_hint,
            url=record.get("url", ""),
            title=record.get("title", ""),
            content=record.get("content", ""),
            date_published=record.get("date"),
            metadata={},
        )
    
    def _save_case(self, case: ScrapedCase, slug_hint: str) -> Path:
        """Save case to output directory."""
        slug = slugify(slug_hint or case.title) or "entry"
        path = self.ensure_unique_path(slug)
        return case.save(self.output_dir, path.name)


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    """Command-line entry point for IANDS scraper."""
    parser = argparse.ArgumentParser(description="Scrape IANDS NDE accounts")
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("data"),
        help="Output directory (default: data)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Only process the first N listing entries (useful for testing)",
    )
    args = parser.parse_args()
    
    scraper = IANDSScraper(output_dir=args.output)
    scraper.scrape_all(limit=args.limit)


if __name__ == "__main__":
    main()
