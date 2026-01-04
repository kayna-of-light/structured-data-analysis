"""
PubMed Central (PMC) OAI-PMH Harvester.

Scrapes open-access articles from PubMed Central via the OAI-PMH protocol
and E-utilities API. Primarily used for harvesting case reports.

API Documentation:
- OAI-PMH: https://www.ncbi.nlm.nih.gov/pmc/tools/oai/
- E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25500/

Usage:
    from shared.scrapers import pmc
    
    scraper = pmc.PMCScraper(
        output_dir=Path("data"),
        email="your@email.com",  # Recommended
        api_key="your-ncbi-api-key",  # Optional, increases rate limit
    )
    
    # Search with custom query
    cases = scraper.scrape_all(
        query='spontaneous remission cancer',
        max_articles=100,
    )
"""

import argparse
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlencode

from .base import BaseScraper, ScrapedCase, http_get, clean_text, logger


# =============================================================================
# CONFIGURATION
# =============================================================================

# E-utilities endpoints
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# PMC Open Access API for PDF downloads
PMC_OA_URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"

# Rate limiting for NCBI (they request max 3 requests/second without API key)
NCBI_DELAY = 0.34  # ~3 requests/second


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class PMCRecord:
    """Parsed PMC record from article XML."""
    pmcid: str
    pmid: Optional[str] = None
    doi: Optional[str] = None
    title: str = ""
    abstract: str = ""
    body_text: str = ""
    article_type: str = ""
    journal: str = ""
    pub_date: Optional[str] = None
    authors: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    raw_xml: str = ""
    pdf_path: Optional[str] = None
    has_full_text: bool = False


# =============================================================================
# SCRAPER CLASS
# =============================================================================

class PMCScraper(BaseScraper):
    """
    Harvests articles from PubMed Central.
    
    Uses E-utilities (esearch/efetch) for searching and fetching full text,
    and the Open Access API for downloading PDFs when available.
    
    Attributes:
        source_name: "pmc"
        output_subdir: "pmc"
    """
    
    source_name = "pmc"
    output_subdir = "pmc"
    
    def __init__(
        self,
        output_dir: Path,
        email: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Initialize PMC scraper.
        
        Args:
            output_dir: Base output directory
            email: Email for NCBI (recommended for higher rate limits)
            api_key: NCBI API key (allows 10 requests/second instead of 3)
        """
        super().__init__(output_dir)
        self.email = email
        self.api_key = api_key
        
        # Build base params for E-utilities
        self.eutils_params: Dict[str, str] = {}
        if email:
            self.eutils_params["email"] = email
        if api_key:
            self.eutils_params["api_key"] = api_key
    
    def search_pmc(self, query: str, max_results: int = 10000) -> List[str]:
        """
        Search PMC for articles matching query.
        
        Args:
            query: PubMed/PMC search query
            max_results: Maximum number of results to retrieve
            
        Returns:
            List of PMCIDs
        """
        params = {
            **self.eutils_params,
            "db": "pmc",
            "term": query,
            "retmax": str(max_results),
            "rettype": "xml",
            "usehistory": "n",
        }
        
        url = f"{ESEARCH_URL}?{urlencode(params)}"
        self.logger.info(f"Searching PMC: {query[:80]}...")
        
        response = http_get(url, delay=NCBI_DELAY)
        
        # Parse response for IDs
        root = ET.fromstring(response.content)
        ids = [id_elem.text for id_elem in root.findall(".//Id") if id_elem.text]
        
        self.logger.info(f"Found {len(ids)} PMC IDs")
        return ids
    
    def fetch_article_xml(self, pmcid: str) -> Optional[str]:
        """
        Fetch full article XML from PMC via efetch.
        
        Args:
            pmcid: PMC ID (with or without "PMC" prefix)
            
        Returns:
            Raw XML string or None if not available
        """
        # Remove PMC prefix for efetch
        pmc_num = pmcid.upper().replace("PMC", "")
        
        params = {
            **self.eutils_params,
            "db": "pmc",
            "id": pmc_num,
            "rettype": "xml",
            "retmode": "xml",
        }
        
        url = f"{EFETCH_URL}?{urlencode(params)}"
        
        try:
            response = http_get(url, delay=NCBI_DELAY)
            return response.text
        except Exception as e:
            self.logger.warning(f"Failed to fetch {pmcid}: {e}")
            return None
    
    def parse_article_xml(self, xml_text: str, pmcid: str) -> Optional[PMCRecord]:
        """
        Parse PMC article XML into structured record.
        
        Args:
            xml_text: Raw XML from efetch
            pmcid: PMC ID for the article
            
        Returns:
            Parsed PMCRecord or None if parsing fails
        """
        try:
            root = ET.fromstring(xml_text.encode('utf-8'))
        except ET.ParseError as e:
            self.logger.error(f"XML parse error for {pmcid}: {e}")
            return None
        
        record = PMCRecord(pmcid=pmcid, raw_xml=xml_text)
        
        # Find the article element (may be namespaced or not)
        article = None
        for tag in ["article", "{https://jats.nlm.nih.gov/ns/archiving/1.3/}article"]:
            article = root.find(f".//{tag}")
            if article is not None:
                break
        
        if article is None:
            article = root.find(".//article")
            if article is None:
                self.logger.warning(f"No article element found in {pmcid}")
                return record
        
        # Extract article type
        record.article_type = article.get("article-type", "")
        
        # Extract title
        title_elem = article.find(".//article-title") or article.find(".//{*}article-title")
        if title_elem is not None:
            record.title = clean_text("".join(title_elem.itertext()))
        
        # Extract abstract
        abstract_elem = article.find(".//abstract") or article.find(".//{*}abstract")
        if abstract_elem is not None:
            record.abstract = clean_text("".join(abstract_elem.itertext()))
        
        # Extract body text
        body_elem = article.find(".//body") or article.find(".//{*}body")
        if body_elem is not None:
            record.body_text = clean_text("".join(body_elem.itertext()))
        
        # Extract IDs
        for art_id in article.findall(".//article-id") + article.findall(".//{*}article-id"):
            id_type = art_id.get("pub-id-type", "")
            if id_type == "pmid" and art_id.text:
                record.pmid = art_id.text
            elif id_type == "doi" and art_id.text:
                record.doi = art_id.text
        
        # Extract journal
        journal_elem = article.find(".//journal-title") or article.find(".//{*}journal-title")
        if journal_elem is not None and journal_elem.text:
            record.journal = clean_text(journal_elem.text)
        
        # Extract publication date
        pub_date_elem = article.find(".//pub-date") or article.find(".//{*}pub-date")
        if pub_date_elem is not None:
            year = pub_date_elem.findtext("year") or pub_date_elem.findtext("{*}year")
            month = pub_date_elem.findtext("month") or pub_date_elem.findtext("{*}month")
            day = pub_date_elem.findtext("day") or pub_date_elem.findtext("{*}day")
            parts = [p for p in [year, month, day] if p]
            if parts:
                record.pub_date = "-".join(parts)
        
        # Extract authors
        for contrib in article.findall(".//contrib[@contrib-type='author']") + \
                       article.findall(".//{*}contrib[@contrib-type='author']"):
            surname = contrib.findtext(".//surname") or contrib.findtext(".//{*}surname")
            given = contrib.findtext(".//given-names") or contrib.findtext(".//{*}given-names")
            if surname:
                name = f"{given} {surname}".strip() if given else surname
                record.authors.append(name)
        
        # Extract keywords
        for kwd in article.findall(".//kwd") + article.findall(".//{*}kwd"):
            if kwd.text:
                record.keywords.append(clean_text(kwd.text))
        
        return record
    
    def download_pdf(self, pmcid: str) -> Optional[str]:
        """
        Download PDF for a PMC article using the Open Access API.
        
        Args:
            pmcid: PMC ID (with or without prefix)
            
        Returns:
            Path to downloaded PDF or None if not available
        """
        # Ensure we have PMC prefix
        if not pmcid.upper().startswith("PMC"):
            pmcid = f"PMC{pmcid}"
        
        params = {"id": pmcid}
        url = f"{PMC_OA_URL}?{urlencode(params)}"
        
        try:
            response = http_get(url, delay=NCBI_DELAY)
            root = ET.fromstring(response.content)
            
            # Check for error
            error = root.find(".//error")
            if error is not None:
                return None  # Article not open access
            
            # Find PDF link
            pdf_link = root.find(".//link[@format='pdf']")
            if pdf_link is None:
                return None
            
            pdf_url = pdf_link.get("href")
            if not pdf_url:
                return None
            
            # Convert FTP to HTTPS
            if pdf_url.startswith("ftp://ftp.ncbi.nlm.nih.gov/"):
                pdf_url = pdf_url.replace(
                    "ftp://ftp.ncbi.nlm.nih.gov/",
                    "https://ftp.ncbi.nlm.nih.gov/"
                )
            
            # Download PDF
            pdf_response = http_get(pdf_url, delay=NCBI_DELAY)
            
            # Save to pdfs subdirectory
            pdf_dir = self.output_dir / "pdfs"
            pdf_dir.mkdir(parents=True, exist_ok=True)
            
            pdf_filename = f"{pmcid}.pdf"
            pdf_path = pdf_dir / pdf_filename
            pdf_path.write_bytes(pdf_response.content)
            
            self.logger.info(f"Downloaded PDF: {pdf_filename} ({len(pdf_response.content)} bytes)")
            return str(pdf_path)
            
        except Exception as e:
            self.logger.debug(f"Could not download PDF for {pmcid}: {e}")
            return None
    
    def save_raw_xml(self, pmcid: str, xml_text: str) -> str:
        """Save raw XML to file for later reprocessing."""
        xml_dir = self.output_dir / "raw_xml"
        xml_dir.mkdir(parents=True, exist_ok=True)
        
        xml_path = xml_dir / f"{pmcid}.xml"
        xml_path.write_text(xml_text, encoding="utf-8")
        return str(xml_path)
    
    def record_to_case(self, record: PMCRecord) -> ScrapedCase:
        """Convert PMCRecord to standardized ScrapedCase."""
        # Determine content type
        if record.has_full_text and record.pdf_path:
            content_type = "full_text_with_pdf"
        elif record.pdf_path:
            content_type = "pdf_only"
        elif record.has_full_text:
            content_type = "full_text"
        elif record.abstract:
            content_type = "abstract_only"
        else:
            content_type = "metadata_only"
        
        return ScrapedCase(
            source="pmc",
            source_id=record.pmcid,
            url=f"https://www.ncbi.nlm.nih.gov/pmc/articles/{record.pmcid}/",
            title=record.title,
            date_published=record.pub_date,
            content=f"{record.abstract}\n\n{record.body_text}".strip(),
            metadata={
                "pmid": record.pmid,
                "doi": record.doi,
                "article_type": record.article_type,
                "journal": record.journal,
                "authors": record.authors,
                "keywords": record.keywords,
                "pdf_path": record.pdf_path,
                "has_raw_xml": bool(record.raw_xml),
                "content_type": content_type,
            }
        )
    
    def scrape_all(
        self,
        query: str,
        max_articles: int = 1000,
        download_pdfs: bool = True,
        require_full_text: bool = True,
    ) -> List[ScrapedCase]:
        """
        Scrape articles from PMC matching query.
        
        Args:
            query: PubMed/PMC search query
            max_articles: Maximum number of articles to process
            download_pdfs: Whether to download PDFs for open access articles
            require_full_text: Whether to skip articles without full text
            
        Returns:
            List of scraped cases
        """
        cases: List[ScrapedCase] = []
        stats = {
            "total": 0,
            "with_full_text": 0,
            "with_pdf": 0,
            "abstract_only": 0,
            "failed": 0,
        }
        
        # Search for articles
        pmcids = self.search_pmc(query, max_results=max_articles)
        stats["total"] = len(pmcids)
        
        self.logger.info(f"Processing {len(pmcids)} articles...")
        
        for i, pmcid in enumerate(pmcids):
            if i > 0 and i % 25 == 0:
                self.logger.info(
                    f"Progress: {i}/{len(pmcids)} - "
                    f"{stats['with_full_text']} full text, "
                    f"{stats['with_pdf']} PDFs"
                )
            
            # Ensure PMC prefix
            if not pmcid.upper().startswith("PMC"):
                pmcid = f"PMC{pmcid}"
            
            # Fetch full text XML
            xml = self.fetch_article_xml(pmcid)
            if xml is None:
                stats["failed"] += 1
                continue
            
            # Parse article
            record = self.parse_article_xml(xml, pmcid)
            if record is None:
                stats["failed"] += 1
                continue
            
            # Check if we got full text
            record.has_full_text = len(record.body_text) > 500
            if require_full_text and not record.has_full_text:
                stats["abstract_only"] += 1
                self.logger.debug(f"Skipping {pmcid} - no full text")
                continue
            
            stats["with_full_text"] += 1
            
            # Save raw XML
            self.save_raw_xml(pmcid, xml)
            
            # Try to download PDF
            if download_pdfs:
                pdf_path = self.download_pdf(pmcid)
                if pdf_path:
                    record.pdf_path = pdf_path
                    stats["with_pdf"] += 1
            
            # Convert to case
            case = self.record_to_case(record)
            
            # Save to disk
            self.save_case(case)
            cases.append(case)
        
        # Log final statistics
        self.logger.info(f"\nScraping complete:")
        self.logger.info(f"  - Total processed: {len(cases)}/{stats['total']}")
        self.logger.info(f"  - With full text: {stats['with_full_text']}")
        self.logger.info(f"  - With PDF: {stats['with_pdf']}")
        self.logger.info(f"  - Abstract only: {stats['abstract_only']}")
        self.logger.info(f"  - Failed: {stats['failed']}")
        
        return cases


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    """Command-line entry point for PMC scraper."""
    parser = argparse.ArgumentParser(description="Scrape PMC articles")
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("data"),
        help="Output directory (default: data)",
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        required=True,
        help="PubMed/PMC search query",
    )
    parser.add_argument(
        "--max", "-m",
        type=int,
        default=100,
        help="Maximum articles to process (default: 100)",
    )
    parser.add_argument(
        "--email", "-e",
        type=str,
        default=None,
        help="Email for NCBI (recommended)",
    )
    parser.add_argument(
        "--api-key", "-k",
        type=str,
        default=None,
        help="NCBI API key",
    )
    parser.add_argument(
        "--no-pdfs",
        action="store_true",
        help="Skip PDF downloads",
    )
    args = parser.parse_args()
    
    scraper = PMCScraper(args.output, email=args.email, api_key=args.api_key)
    cases = scraper.scrape_all(
        query=args.query,
        max_articles=args.max,
        download_pdfs=not args.no_pdfs,
    )
    
    print(f"\nScraped {len(cases)} cases to {scraper.output_dir}")


if __name__ == "__main__":
    main()
