"""
IONS (Institute of Noetic Sciences) Bibliography Scraper.

Targets the IONS Spontaneous Remission Bibliography, originally compiled by
Brendan O'Regan and Caryle Hirshberg (1993), documenting over 3,500 cases
from the medical literature.

Primary resources:
- Original book: "Spontaneous Remission: An Annotated Bibliography"
- PDF version: Available through IONS archives
- Online citations database: May require institutional access

This scraper focuses on extracting bibliographic citations and rehydrating
them via PubMed/PMC to get full article text and PDFs where available.
"""

import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlencode

try:
    import pdfplumber
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

from scrapers.base import BaseScraper, ScrapedCase, http_get, clean_text, slugify, logger


# NCBI E-utilities endpoints
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
ELINK_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
PMC_OA_URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"  # OA API for PDF links
NCBI_DELAY = 0.34  # Rate limit: ~3 requests/second

# Known IONS resources
IONS_RESOURCES = {
    "main_site": "https://noetic.org",
    "library": "https://noetic.org/research/",
}


@dataclass
class BibliographyCitation:
    """A citation from the IONS Spontaneous Remission Bibliography."""
    citation_id: str  # Internal ID for this citation
    authors: List[str] = field(default_factory=list)
    title: str = ""
    journal: str = ""
    year: Optional[int] = None
    volume: Optional[str] = None
    pages: Optional[str] = None
    diagnosis: str = ""
    abstract: str = ""
    full_text: str = ""  # Full article text if available from PMC
    pmid: Optional[str] = None  # PubMed ID if found
    pmcid: Optional[str] = None  # PubMed Central ID if available
    doi: Optional[str] = None
    raw_citation: str = ""  # Original citation string
    pdf_path: Optional[str] = None  # Path to downloaded PDF file
    raw_xml: str = ""  # Raw XML response from PMC (for debugging/reprocessing)


class IONSScraper(BaseScraper):
    """
    Scrapes/parses the IONS Spontaneous Remission Bibliography.
    
    Strategy:
    1. Parse PDF bibliography if available
    2. Extract citations and key metadata (diagnosis, outcome)
    3. Re-hydrate citations via PubMed to get full text where possible
    """
    
    source_name = "ions"
    output_subdir = "ions"
    
    def __init__(self, output_dir: Path, pdf_path: Optional[Path] = None):
        """
        Initialize IONS scraper.
        
        Args:
            output_dir: Base output directory
            pdf_path: Path to local IONS bibliography PDF (if available)
        """
        super().__init__(output_dir)
        self.pdf_path = pdf_path
        
        if pdf_path and not PDF_AVAILABLE:
            self.logger.warning(
                "pdfplumber not available. Install with: pip install pdfplumber"
            )
    
    def parse_pdf_bibliography(self, pdf_path: Path) -> List[BibliographyCitation]:
        """
        Parse citations from the IONS bibliography PDF.
        
        The bibliography is organized by diagnosis/condition, with citations
        in standard academic format.
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of parsed citations
        """
        if not PDF_AVAILABLE:
            self.logger.error("pdfplumber required to parse PDF")
            return []
        
        citations: List[BibliographyCitation] = []
        current_diagnosis = ""
        citation_buffer: List[str] = []
        citation_count = 0
        
        self.logger.info(f"Parsing PDF: {pdf_path}")
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    text = page.extract_text() or ""
                    lines = text.split("\n")
                    
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        
                        # Detect section headers (diagnoses)
                        # Headers are typically in CAPS or bold
                        if self._is_diagnosis_header(line):
                            # Save any buffered citation
                            if citation_buffer:
                                cit = self._parse_citation_text(
                                    "\n".join(citation_buffer),
                                    current_diagnosis,
                                    citation_count
                                )
                                if cit:
                                    citations.append(cit)
                                    citation_count += 1
                                citation_buffer = []
                            
                            current_diagnosis = self._clean_diagnosis(line)
                            continue
                        
                        # Detect start of new citation
                        # Usually starts with author name (LastName, Initials)
                        if self._is_citation_start(line):
                            # Save previous citation
                            if citation_buffer:
                                cit = self._parse_citation_text(
                                    "\n".join(citation_buffer),
                                    current_diagnosis,
                                    citation_count
                                )
                                if cit:
                                    citations.append(cit)
                                    citation_count += 1
                            citation_buffer = [line]
                        else:
                            # Continue current citation
                            citation_buffer.append(line)
                
                # Don't forget the last citation
                if citation_buffer:
                    cit = self._parse_citation_text(
                        "\n".join(citation_buffer),
                        current_diagnosis,
                        citation_count
                    )
                    if cit:
                        citations.append(cit)
        
        except Exception as e:
            self.logger.error(f"Error parsing PDF: {e}")
        
        self.logger.info(f"Extracted {len(citations)} citations from PDF")
        return citations
    
    def _is_diagnosis_header(self, line: str) -> bool:
        """Check if line is a diagnosis/condition section header."""
        # Headers are often uppercase, short, and don't contain common citation words
        if len(line) > 100:
            return False
        
        # Check for common diagnosis patterns
        diagnosis_indicators = [
            r"^[A-Z][A-Z\s\-]+$",  # ALL CAPS
            r"^(?:CANCER|CARCINOMA|TUMOR|SARCOMA|LYMPHOMA|LEUKEMIA)",
            r"^(?:Chapter|Section)\s+\d+",
        ]
        
        for pattern in diagnosis_indicators:
            if re.match(pattern, line):
                return True
        
        return False
    
    def _clean_diagnosis(self, line: str) -> str:
        """Clean and normalize diagnosis header."""
        # Remove chapter/section numbers
        line = re.sub(r"^(?:Chapter|Section)\s+\d+[:\s]*", "", line)
        return clean_text(line.title())
    
    def _is_citation_start(self, line: str) -> bool:
        """Check if line starts a new citation."""
        # Citations typically start with author: LastName, X.X.
        author_pattern = r"^[A-Z][a-z]+(?:[-'][A-Z][a-z]+)?,\s*[A-Z]\."
        return bool(re.match(author_pattern, line))
    
    def _parse_citation_text(self, text: str, diagnosis: str, idx: int) -> Optional[BibliographyCitation]:
        """
        Parse a citation text block into structured data.
        
        Args:
            text: Raw citation text
            diagnosis: Current diagnosis section
            idx: Citation index for ID
            
        Returns:
            Parsed citation or None
        """
        text = clean_text(text)
        if len(text) < 20:  # Too short to be valid
            return None
        
        citation = BibliographyCitation(
            citation_id=f"ions-{idx:05d}",
            diagnosis=diagnosis,
            raw_citation=text
        )
        
        # Parse authors (before first title marker)
        # Format: LastName, I.I., LastName, I.I., & LastName, I.I.
        author_match = re.match(
            r"^((?:[A-Z][a-z]+(?:[-'][A-Z][a-z]+)?,\s*[A-Z]\.(?:[A-Z]\.)?(?:,?\s*(?:&\s*)?)?)+)",
            text
        )
        if author_match:
            author_text = author_match.group(1)
            # Split into individual authors
            authors = re.findall(r"([A-Z][a-z]+(?:[-'][A-Z][a-z]+)?),\s*([A-Z]\.(?:[A-Z]\.)?)", author_text)
            citation.authors = [f"{last}, {initials}" for last, initials in authors]
        
        # Parse year (typically in parentheses after authors)
        year_match = re.search(r"\((\d{4})\)", text)
        if year_match:
            citation.year = int(year_match.group(1))
        
        # Parse title (typically after year, before journal)
        # Titles end with a period and journal names are often italicized or followed by comma+volume
        title_match = re.search(r"\)\.\s*(.+?)\.\s*(?:[A-Z]|$)", text)
        if title_match:
            citation.title = clean_text(title_match.group(1))
        
        # Parse journal
        journal_match = re.search(
            r"\.([A-Z][^,]+(?:Journal|Lancet|JAMA|BMJ|Cancer|Medicine|Surgery|Oncology)[^,]*),?\s*(\d+)?",
            text, re.IGNORECASE
        )
        if journal_match:
            citation.journal = clean_text(journal_match.group(1))
            if journal_match.group(2):
                citation.volume = journal_match.group(2)
        
        # Parse pages
        pages_match = re.search(r"(\d+)[–-](\d+)", text)
        if pages_match:
            citation.pages = f"{pages_match.group(1)}-{pages_match.group(2)}"
        
        return citation
    
    def rehydrate_citation(self, citation: BibliographyCitation) -> bool:
        """
        Attempt to find PubMed ID for a citation and retrieve full content.
        
        Steps:
        1. Search PubMed for matching article to get PMID
        2. Convert PMID to PMCID if available in PMC
        3. Fetch full article XML from PMC and store raw XML
        4. Download PDF if available in PMC
        5. Fall back to abstract from PubMed if no PMC access
        
        Args:
            citation: Citation to look up
            
        Returns:
            True if content was retrieved
        """
        if not citation.title:
            return False
        
        # Step 1: Search PubMed for PMID
        pmid = self._search_pubmed_for_pmid(citation)
        if not pmid:
            return False
        
        citation.pmid = pmid
        content_retrieved = False
        
        # Step 2: Try to get PMCID
        pmcid = self._get_pmcid_from_pmid(pmid)
        if pmcid:
            citation.pmcid = pmcid
            
            # Step 3: Fetch full XML from PMC (store raw)
            raw_xml, full_text = self._fetch_pmc_content(pmcid)
            if raw_xml:
                citation.raw_xml = raw_xml
                if full_text:
                    citation.full_text = full_text
                    content_retrieved = True
                    self.logger.debug(f"Got full text for {pmid} ({len(full_text)} chars)")
            
            # Step 4: Download PDF
            pdf_path = self._download_pmc_pdf(pmcid, citation.citation_id)
            if pdf_path:
                citation.pdf_path = str(pdf_path)
                content_retrieved = True
                self.logger.debug(f"Downloaded PDF for {pmcid}: {pdf_path}")
        
        # Step 5: Fall back to abstract from PubMed if no full text
        if not citation.full_text:
            abstract = self._fetch_pubmed_abstract(pmid)
            if abstract:
                citation.abstract = abstract
                content_retrieved = True
                self.logger.debug(f"Got abstract for {pmid} ({len(abstract)} chars)")
        
        return content_retrieved
    
    def _search_pubmed_for_pmid(self, citation: BibliographyCitation) -> Optional[str]:
        """Search PubMed for a matching article and return PMID."""
        # Try multiple search strategies, from most specific to most general
        
        # Helper to extract meaningful keywords from title
        def extract_keywords(title: str, max_words: int = 5) -> str:
            # Remove punctuation and split
            import string
            cleaned = title.translate(str.maketrans("", "", string.punctuation))
            words = [w for w in cleaned.split() 
                    if len(w) > 3 
                    and w.lower() not in {'from', 'with', 'that', 'this', 'have', 'been', 
                                          'were', 'case', 'cases', 'report', 'review', 
                                          'study', 'analysis', 'preliminary'}
                    and not w.isdigit()]  # Skip years/numbers
            return " ".join(words[:max_words])
        
        # Strategy 1: Key title words + author + year (most reliable)
        if citation.title and citation.authors and citation.year:
            title_keywords = extract_keywords(citation.title)
            first_author = citation.authors[0].split(",")[0]
            query = f"{title_keywords}[Title] AND {first_author}[Author] AND {citation.year}[pdat]"
            pmid = self._execute_pubmed_search(query)
            if pmid:
                return pmid
        
        # Strategy 2: Key title words + author (no year constraint)
        if citation.title and citation.authors:
            title_keywords = extract_keywords(citation.title)
            first_author = citation.authors[0].split(",")[0]
            query = f"{title_keywords}[Title] AND {first_author}[Author]"
            pmid = self._execute_pubmed_search(query)
            if pmid:
                return pmid
        
        # Strategy 3: Full title quoted (for exact matches)
        if citation.title:
            query = f'"{citation.title}"[Title]'
            pmid = self._execute_pubmed_search(query)
            if pmid:
                return pmid
        
        return None
    
    def _execute_pubmed_search(self, query: str) -> Optional[str]:
        """Execute a PubMed search query and return first PMID."""
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": "1",
            "rettype": "xml",
        }
        
        try:
            response = http_get(f"{ESEARCH_URL}?{urlencode(params)}", delay=NCBI_DELAY)
            pmid_match = re.search(r"<Id>(\d+)</Id>", response.text)
            if pmid_match:
                return pmid_match.group(1)
        except Exception as e:
            self.logger.debug(f"PubMed search failed: {e}")
        
        return None
    
    def _get_pmcid_from_pmid(self, pmid: str) -> Optional[str]:
        """
        Convert PMID to PMCID using elink.
        
        Only returns PMCID if the article itself is available in PMC
        (not just citing articles).
        """
        params = {
            "dbfrom": "pubmed",
            "db": "pmc",
            "id": pmid,
            "retmode": "xml",
            "linkname": "pubmed_pmc",  # Direct PMC link, not citations
        }
        
        try:
            response = http_get(f"{ELINK_URL}?{urlencode(params)}", delay=NCBI_DELAY)
            
            # Parse XML to find PMC ID in the correct linkset
            root = ET.fromstring(response.content)
            
            # Look for LinkSetDb with LinkName "pubmed_pmc" (full text available)
            for linksetdb in root.findall(".//LinkSetDb"):
                linkname = linksetdb.find("LinkName")
                if linkname is not None and linkname.text == "pubmed_pmc":
                    # Get first linked PMC ID
                    link_id = linksetdb.find(".//Link/Id")
                    if link_id is not None and link_id.text:
                        return f"PMC{link_id.text}"
            
            self.logger.debug(f"No PMC full text available for PMID {pmid}")
            
        except Exception as e:
            self.logger.debug(f"PMCID lookup failed: {e}")
        
        return None
    
    def _fetch_pmc_content(self, pmcid: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Fetch full article XML from PMC and extract text.
        
        Args:
            pmcid: PMC identifier (e.g., "PMC1234567")
            
        Returns:
            Tuple of (raw_xml, extracted_text) - either may be None
        """
        pmc_num = pmcid.upper().replace("PMC", "")
        
        params = {
            "db": "pmc",
            "id": pmc_num,
            "rettype": "xml",
            "retmode": "xml",
        }
        
        try:
            response = http_get(f"{EFETCH_URL}?{urlencode(params)}", delay=NCBI_DELAY)
            raw_xml = response.text
            extracted_text = self._extract_text_from_pmc_xml(raw_xml)
            return raw_xml, extracted_text
        except Exception as e:
            self.logger.debug(f"PMC fetch failed for {pmcid}: {e}")
        
        return None, None
    
    def _download_pmc_pdf(self, pmcid: str, citation_id: str) -> Optional[Path]:
        """
        Download PDF from PMC if available using the OA API.
        
        The OA API returns links to PDFs for open-access articles.
        
        Args:
            pmcid: PMC identifier (e.g., "PMC1234567")
            citation_id: Citation ID for filename
            
        Returns:
            Path to downloaded PDF or None if not available
        """
        import requests
        from scrapers.base import get_session
        
        # Create pdfs subdirectory
        pdf_dir = self.output_dir / "pdfs"
        pdf_dir.mkdir(parents=True, exist_ok=True)
        
        pdf_path = pdf_dir / f"{citation_id}_{pmcid}.pdf"
        
        # Skip if already downloaded
        if pdf_path.exists():
            return pdf_path
        
        try:
            # Query OA API for PDF link
            oa_url = f"{PMC_OA_URL}?id={pmcid}"
            response = http_get(oa_url, delay=NCBI_DELAY)
            
            # Parse XML response
            root = ET.fromstring(response.content)
            
            # Find PDF link in response
            pdf_url = None
            for link in root.findall('.//link'):
                if link.get('format') == 'pdf':
                    pdf_url = link.get('href', '')
                    break
            
            if not pdf_url:
                self.logger.debug(f"No PDF link found in OA API for {pmcid}")
                return None
            
            # Convert FTP URL to HTTPS
            if pdf_url.startswith('ftp://ftp.ncbi.nlm.nih.gov/'):
                pdf_url = pdf_url.replace('ftp://ftp.ncbi.nlm.nih.gov/', 
                                         'https://ftp.ncbi.nlm.nih.gov/')
            
            # Download PDF
            session = get_session()
            pdf_response = session.get(pdf_url, timeout=120)
            
            # Verify it's a PDF
            if pdf_response.content[:4] != b'%PDF':
                self.logger.debug(f"Response for {pmcid} is not a valid PDF")
                return None
            
            # Save PDF
            with open(pdf_path, 'wb') as f:
                f.write(pdf_response.content)
            
            self.logger.info(f"Downloaded PDF: {pdf_path.name} ({len(pdf_response.content)} bytes)")
            return pdf_path
            
        except Exception as e:
            self.logger.debug(f"PDF download failed for {pmcid}: {e}")
        
        return None
    
    def _extract_text_from_pmc_xml(self, xml_text: str) -> Optional[str]:
        """
        Extract readable text from PMC article XML.
        
        Note: Some publishers restrict full text in XML format.
        In those cases, only title/abstract may be available.
        """
        try:
            root = ET.fromstring(xml_text.encode('utf-8'))
        except ET.ParseError:
            return None
        
        text_parts = []
        
        # Extract title
        title_elem = root.find(".//article-title")
        if title_elem is not None:
            title_text = self._get_element_text(title_elem)
            if title_text:
                text_parts.append(f"Title: {title_text}")
        
        # Extract abstract - check multiple possible locations
        abstract_parts = []
        for abs_path in [".//abstract//p", ".//abstract"]:
            for abs_elem in root.findall(abs_path):
                abs_text = self._get_element_text(abs_elem)
                if abs_text and len(abs_text) > 20:
                    abstract_parts.append(abs_text)
        if abstract_parts:
            text_parts.append(f"\nAbstract:\n{' '.join(abstract_parts)}")
        
        # Extract body text (may be empty if publisher restricts)
        body_parts = []
        for section in root.findall(".//body//sec"):
            # Get section title
            sec_title = section.find("title")
            if sec_title is not None:
                sec_title_text = self._get_element_text(sec_title)
                if sec_title_text:
                    body_parts.append(f"\n## {sec_title_text}\n")
            
            # Get paragraphs
            for p in section.findall(".//p"):
                p_text = self._get_element_text(p)
                if p_text and len(p_text) > 10:
                    body_parts.append(p_text)
        
        if body_parts:
            text_parts.append("\n" + "\n\n".join(body_parts))
        
        # Only return if we got meaningful content (more than just title)
        full_text = "\n".join(text_parts)
        if len(full_text) > 100:  # More than just a title
            return full_text
        
        return None
    
    def _get_element_text(self, elem) -> str:
        """Recursively extract text from an XML element."""
        text_parts = []
        if elem.text:
            text_parts.append(elem.text)
        for child in elem:
            text_parts.append(self._get_element_text(child))
            if child.tail:
                text_parts.append(child.tail)
        return "".join(text_parts).strip()
    
    def _fetch_pubmed_abstract(self, pmid: str) -> Optional[str]:
        """Fetch abstract from PubMed."""
        params = {
            "db": "pubmed",
            "id": pmid,
            "rettype": "abstract",
            "retmode": "xml",
        }
        
        try:
            response = http_get(f"{EFETCH_URL}?{urlencode(params)}", delay=NCBI_DELAY)
            
            # Parse abstract from XML
            root = ET.fromstring(response.content)
            abstract_elem = root.find(".//AbstractText")
            if abstract_elem is not None and abstract_elem.text:
                return abstract_elem.text
        except Exception as e:
            self.logger.debug(f"PubMed abstract fetch failed: {e}")
        
        return None
    
    def citation_to_case(self, citation: BibliographyCitation) -> ScrapedCase:
        """Convert BibliographyCitation to standardized ScrapedCase."""
        # Build content from available info - prefer full text over abstract
        content_parts = []
        
        if citation.full_text:
            # Full text from PMC already includes title and abstract
            content_parts.append(citation.full_text)
        else:
            # Fall back to title + abstract
            if citation.title:
                content_parts.append(f"Title: {citation.title}")
            if citation.abstract:
                content_parts.append(f"\nAbstract:\n{citation.abstract}")
        
        if citation.raw_citation:
            content_parts.append(f"\nOriginal Citation:\n{citation.raw_citation}")
        
        # Determine best URL - prefer PMC for full text access
        url = ""
        if citation.pmcid:
            url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{citation.pmcid}/"
        elif citation.pmid:
            url = f"https://pubmed.ncbi.nlm.nih.gov/{citation.pmid}/"
        elif citation.doi:
            url = f"https://doi.org/{citation.doi}"
        
        # Determine content type for metadata
        has_pdf = bool(citation.pdf_path)
        has_full_text = bool(citation.full_text)
        has_abstract = bool(citation.abstract)
        
        if has_full_text and has_pdf:
            content_type = "full_text_with_pdf"
        elif has_pdf:
            content_type = "pdf_only"
        elif has_full_text:
            content_type = "full_text"
        elif has_abstract:
            content_type = "abstract"
        else:
            content_type = "citation_only"
        
        return ScrapedCase(
            source="ions",
            source_id=citation.citation_id,
            url=url,
            title=citation.title or citation.raw_citation[:100],
            date_published=str(citation.year) if citation.year else None,
            content="\n".join(content_parts),
            diagnosis=citation.diagnosis,
            metadata={
                "authors": citation.authors,
                "journal": citation.journal,
                "volume": citation.volume,
                "pages": citation.pages,
                "pmid": citation.pmid,
                "pmcid": citation.pmcid,
                "doi": citation.doi,
                "pdf_path": citation.pdf_path,
                "has_raw_xml": bool(citation.raw_xml),
                "content_type": content_type,
                "source_bibliography": "IONS Spontaneous Remission Bibliography",
            }
        )
    
    def parse_manual_entries(self, entries_file: Path) -> List[BibliographyCitation]:
        """
        Parse manually transcribed bibliography entries.
        
        For cases where PDF parsing fails or isn't available,
        entries can be provided in a simple text or JSON format.
        
        Args:
            entries_file: Path to entries file
            
        Returns:
            List of parsed citations
        """
        citations: List[BibliographyCitation] = []
        
        if entries_file.suffix == ".json":
            with open(entries_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for idx, entry in enumerate(data):
                citation = BibliographyCitation(
                    citation_id=f"ions-manual-{idx:05d}",
                    **entry
                )
                citations.append(citation)
        
        elif entries_file.suffix in [".txt", ".md"]:
            current_diagnosis = ""
            citation_count = 0
            
            with open(entries_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Section header (starts with #)
                    if line.startswith("#"):
                        current_diagnosis = line.lstrip("#").strip()
                        continue
                    
                    # Parse as citation
                    cit = self._parse_citation_text(line, current_diagnosis, citation_count)
                    if cit:
                        citations.append(cit)
                        citation_count += 1
        
        return citations
    
    def save_raw_xml(self, citation: BibliographyCitation) -> Optional[Path]:
        """
        Save raw XML for a citation that has PMC content.
        
        Args:
            citation: Citation with raw_xml content
            
        Returns:
            Path to saved XML file or None
        """
        if not citation.raw_xml:
            return None
        
        xml_dir = self.output_dir / "raw_xml"
        xml_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{citation.citation_id}_{citation.pmcid or citation.pmid}.xml"
        filepath = xml_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(citation.raw_xml)
        
        return filepath
    
    def scrape_all(self, rehydrate: bool = True) -> List[ScrapedCase]:
        """
        Parse all available IONS bibliography data.
        
        Args:
            rehydrate: Whether to attempt PubMed lookup for citations
            
        Returns:
            List of scraped cases
        """
        citations: List[BibliographyCitation] = []
        
        # Try PDF parsing first
        if self.pdf_path and self.pdf_path.exists():
            citations = self.parse_pdf_bibliography(self.pdf_path)
        
        # Look for manual entries file
        manual_entries = self.output_dir.parent / "ions_entries.json"
        if manual_entries.exists():
            manual_citations = self.parse_manual_entries(manual_entries)
            citations.extend(manual_citations)
        
        if not citations:
            self.logger.warning(
                "No IONS data found. Please provide either:\n"
                "  - PDF path via --pdf argument\n"
                "  - Manual entries in data/ions_entries.json"
            )
            return []
        
        self.logger.info(f"Processing {len(citations)} citations...")
        
        # Statistics
        stats = {
            "total": len(citations),
            "rehydrated": 0,
            "with_full_text": 0,
            "with_pdf": 0,
            "with_abstract_only": 0,
            "citation_only": 0,
        }
        
        # Optionally rehydrate via PubMed
        if rehydrate:
            for i, citation in enumerate(citations):
                if i % 50 == 0:
                    self.logger.info(f"Rehydrating: {i}/{len(citations)}")
                
                if self.rehydrate_citation(citation):
                    stats["rehydrated"] += 1
                    
                    # Save raw XML if available
                    if citation.raw_xml:
                        self.save_raw_xml(citation)
                    
                    # Track content types
                    if citation.pdf_path:
                        stats["with_pdf"] += 1
                    if citation.full_text:
                        stats["with_full_text"] += 1
                    elif citation.abstract:
                        stats["with_abstract_only"] += 1
                else:
                    stats["citation_only"] += 1
            
            self.logger.info(f"Rehydration complete:")
            self.logger.info(f"  - Rehydrated: {stats['rehydrated']}/{stats['total']}")
            self.logger.info(f"  - With full text: {stats['with_full_text']}")
            self.logger.info(f"  - With PDF: {stats['with_pdf']}")
            self.logger.info(f"  - Abstract only: {stats['with_abstract_only']}")
            self.logger.info(f"  - Citation only: {stats['citation_only']}")
        
        # Convert and save
        cases: List[ScrapedCase] = []
        for citation in citations:
            case = self.citation_to_case(citation)
            self.save_case(case)
            cases.append(case)
        
        return cases


def main():
    """Run IONS scraper from command line."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Parse IONS Spontaneous Remission Bibliography")
    parser.add_argument("--output", "-o", type=Path, default=Path("data"),
                        help="Output directory")
    parser.add_argument("--pdf", "-p", type=Path, default=None,
                        help="Path to IONS bibliography PDF")
    parser.add_argument("--no-rehydrate", action="store_true",
                        help="Skip PubMed lookup for citations")
    
    args = parser.parse_args()
    
    scraper = IONSScraper(args.output, pdf_path=args.pdf)
    cases = scraper.scrape_all(rehydrate=not args.no_rehydrate)
    
    print(f"\nProcessed {len(cases)} citations to {scraper.output_dir}")


if __name__ == "__main__":
    main()
