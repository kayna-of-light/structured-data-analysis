"""
Miracle Hunter / Lourdes Scraper for documented healing cases.

Miracle Hunter (miraclehunter.com) catalogs forensically verified miracle healings,
particularly those documented by the Lourdes Medical Bureau.

Target URLs:
- Lourdes miracles: http://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles1.html
  (through miracles4.html)

The Lourdes Medical Bureau (Bureau Médical) has documented 70 officially recognized 
miracle healings since 1858, each with rigorous medical investigation.
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from scrapers.base import BaseScraper, ScrapedCase, http_get, clean_text, slugify, logger


# Lourdes miracles pages
LOURDES_BASE_URL = "http://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/"
LOURDES_PAGES = [
    "miracles1.html",  # Miracles 1-20
    "miracles2.html",  # Miracles 21-40
    "miracles3.html",  # Miracles 41-60
    "miracles4.html",  # Miracles 61-70
]

# Other documented miracle categories
OTHER_CATEGORIES = {
    "fatima": "http://www.miraclehunter.com/marian_apparitions/approved_apparitions/fatima/miracles.html",
    "guadalupe": "http://www.miraclehunter.com/marian_apparitions/approved_apparitions/guadalupe/miracles.html",
}


@dataclass
class LourdesMiracle:
    """Parsed Lourdes miracle case."""
    number: int  # Official miracle number (1-70)
    name: str
    date_healed: Optional[str] = None
    date_declared: Optional[str] = None  # When officially recognized
    diagnosis: str = ""
    description: str = ""
    country: str = ""
    age_at_healing: Optional[str] = None
    source_url: str = ""


class LourdesScraper(BaseScraper):
    """
    Scrapes documented miracle healings from Miracle Hunter.
    
    Focus on Lourdes Medical Bureau cases as they have the most rigorous
    forensic documentation.
    """
    
    source_name = "lourdes"
    output_subdir = "lourdes"
    
    def __init__(self, output_dir: Path):
        super().__init__(output_dir)
    
    def scrape_lourdes_page(self, page_url: str) -> List[LourdesMiracle]:
        """
        Parse a single Lourdes miracles page.
        
        Args:
            page_url: URL to the miracles page
            
        Returns:
            List of parsed miracle cases
        """
        self.logger.info(f"Fetching {page_url}")
        
        response = http_get(page_url)
        soup = BeautifulSoup(response.text, "lxml")
        
        # The Lourdes pages have miracle descriptions in paragraphs
        # Each miracle starts with "Name" (bold/heading) followed by details
        miracles = self._parse_from_paragraphs(soup, page_url)
        
        return miracles
    
    def _parse_from_paragraphs(self, soup: BeautifulSoup, source_url: str) -> List[LourdesMiracle]:
        """
        Parse miracles from paragraph elements.
        
        Structure varies across pages:
        - Pages 1-2: "Mrs Name SURNAME Born in YYYY..."  (all in one paragraph)
        - Pages 3-4: "Name SURNAME" then "Born..." then "Cured..." (separate paragraphs)
        
        Entries are separated by [Back to Top] links on the page.
        """
        miracles: List[LourdesMiracle] = []
        
        # Get all paragraphs
        paragraphs = soup.find_all("p")
        
        current_miracle: Optional[LourdesMiracle] = None
        
        for p in paragraphs:
            text = p.get_text(strip=True)
            if not text or len(text) < 5:
                continue
            
            # Skip navigation/boilerplate text
            if text.startswith("Back to Top") or text == "[Back to Top]":
                continue
            
            # Skip Table of Contents paragraphs (contain numbered lists like "1.Mrs Catherine...")
            # These have many numbered entries without actual content
            if re.match(r"^\d+\.\s*(?:Mrs?\.?\s+|Sister\s+)?[A-Z]", text):
                # Check if this is a TOC (multiple numbered items, no "Born" info for each)
                numbered_items = len(re.findall(r"\d+\.\s*(?:Mrs?\.?\s+|Sister\s+)?[A-Z][a-z]+", text))
                if numbered_items > 3:
                    self.logger.debug(f"Skipping TOC paragraph with {numbered_items} items")
                    continue
            
            # Check if this paragraph contains [Back to Top] - marks end of THIS entry
            # The [Back to Top] appears at the END of an entry's paragraph
            if "[Back to Top]" in text:
                # Remove the marker to get clean text for this entry
                text = text.replace("[Back to Top]", "").strip()
            
            # Remove decorative separators (lines of dashes)
            text = re.sub(r'^[-–—]+', '', text).strip()
            
            # Skip if text is now empty or just separators
            if not text or re.match(r'^[-–—\s]+$', text):
                continue
            
            # Note: After cleanup, the full_match below will handle creating entries
            
            # Pattern 1: Full entry in one paragraph (pages 1-2)
            # "Mrs Catherine LATAPIE Born in 1820 Lived in..."
            # Also handles "Sister EUGENIAMarie MABILLE, Born in1855"
            full_match = re.match(
                r"^(?:Mrs?\.?\s+|Sister\s+)?([A-Z][a-zA-Z\-\'\s]+?)"
                r"(?:nee\s+[A-Z]+,?\s*)?"
                r"(?:,?\s*[Bb]orn|,?\s*[Ll]ived|,?\s*[Cc]ured)",
                text
            )
            
            # Pattern 2: Just a name line (pages 3-4)
            # "Henriette BRESSOLLES" (short paragraph, just name)
            name_only_match = re.match(
                r"^(?:Mrs?\.?\s+|Sister\s+)?([A-Z][a-zA-Z\-\' ]+[A-Z]+)$",
                text
            )
            
            if full_match:
                # Save previous miracle if exists
                if current_miracle and current_miracle.name:
                    miracles.append(current_miracle)
                
                name = full_match.group(1).strip()
                # Clean up names like "EUGENIAMarie MABILLE" -> "Marie MABILLE"
                # These have religious name followed by birth name
                if re.match(r'^[A-Z]+[a-z]', name):  # e.g., "EUGENIAMarie"
                    name_parts = re.split(r'(?<=[A-Z])(?=[A-Z][a-z])', name, 1)
                    if len(name_parts) > 1:
                        name = name_parts[1]  # Take the second part (birth name)
                
                number = len(miracles) + 1
                
                current_miracle = LourdesMiracle(
                    number=number,
                    name=clean_text(name),
                    description=clean_text(text),
                    source_url=source_url
                )
                self._extract_dates_from_text(current_miracle, text)
                
            elif name_only_match and len(text) < 50:
                # This is just a name - start new miracle
                if current_miracle and current_miracle.name:
                    miracles.append(current_miracle)
                
                name = name_only_match.group(1)
                number = len(miracles) + 1
                
                current_miracle = LourdesMiracle(
                    number=number,
                    name=clean_text(name),
                    description="",
                    source_url=source_url
                )
                
            elif current_miracle:
                # This is continuation text for current miracle
                current_miracle.description += " " + clean_text(text)
                # Try to extract dates from this text too
                self._extract_dates_from_text(current_miracle, text)
        
        # Don't forget the last miracle
        if current_miracle and current_miracle.name:
            miracles.append(current_miracle)
        
        # Now extract diagnoses from descriptions
        for miracle in miracles:
            self._extract_diagnosis(miracle)
        
        return miracles
    
    def _extract_dates_from_text(self, miracle: LourdesMiracle, text: str) -> None:
        """Extract dates from text into miracle object."""
        # Cured date: "Cured 1st. March 1858" or "Cured on the 3rd. July 1924"
        if not miracle.date_healed:
            cured_match = re.search(
                r"Cured\s+(?:on\s+)?(?:in\s+)?(?:the\s+)?(?:\d+(?:st|nd|rd|th)?\.?\s+)?(\w+\.?\s+\d{4}|\d{4})",
                text
            )
            if cured_match:
                miracle.date_healed = cured_match.group(1)
        
        # Declaration date: "Miracle on 18th January 1862"
        if not miracle.date_declared:
            declared_match = re.search(
                r"Miracle\s+(?:on\s+)?(?:the\s+)?(\d+(?:st|nd|rd|th)?\.?\s+\w+\.?\s+\d{4})",
                text
            )
            if declared_match:
                miracle.date_declared = declared_match.group(1)
        
        # Birth year: "Born in 1820" or "Born on 14th. October 1889"
        if not miracle.age_at_healing:
            birth_match = re.search(r"Born\s+(?:in\s*|on\s+\d+(?:st|nd|rd|th)?\.?\s+\w+\s+)?(\d{4})", text)
            if birth_match:
                miracle.age_at_healing = f"Born {birth_match.group(1)}"
    
    def _extract_diagnosis(self, miracle: LourdesMiracle) -> None:
        """Extract diagnosis/condition from miracle description."""
        desc = miracle.description.lower()
        
        # Common conditions in Lourdes cases
        conditions = [
            ("tuberculosis", "Tuberculosis"),
            ("tubercular", "Tuberculosis"),
            ("paralysis", "Paralysis"),
            ("paralyzed", "Paralysis"),
            ("blindness", "Blindness"),
            ("blind", "Blindness"),
            ("cancer", "Cancer"),
            ("tumor", "Tumor"),
            ("tumour", "Tumor"),
            ("multiple sclerosis", "Multiple Sclerosis"),
            ("sclerosis", "Multiple Sclerosis"),
            ("gangrene", "Gangrene"),
            ("peritonitis", "Peritonitis"),
            ("abscess", "Abscess"),
            ("fistula", "Fistula"),
            ("sarcoma", "Sarcoma"),
            ("meningitis", "Meningitis"),
            ("lupus", "Lupus"),
            ("ulcer", "Ulcer"),
            ("wound", "Wound"),
            ("fracture", "Fracture"),
            ("eyes", "Eye Condition"),
        ]
        
        for keyword, diagnosis in conditions:
            if keyword in desc:
                miracle.diagnosis = diagnosis
                break
    
    def miracle_to_case(self, miracle: LourdesMiracle) -> ScrapedCase:
        """Convert LourdesMiracle to standardized ScrapedCase."""
        return ScrapedCase(
            source="lourdes",
            source_id=f"lourdes-miracle-{miracle.number:02d}",
            url=miracle.source_url,
            title=f"Lourdes Miracle #{miracle.number}: {miracle.name}",
            date_published=miracle.date_declared,
            content=miracle.description,
            diagnosis=miracle.diagnosis,
            diagnosis_date=miracle.date_healed,
            outcome="complete_remission",  # All Lourdes miracles are verified complete cures
            metadata={
                "miracle_number": miracle.number,
                "name": miracle.name,
                "date_healed": miracle.date_healed,
                "date_declared": miracle.date_declared,
                "country": miracle.country,
                "age_at_healing": miracle.age_at_healing,
                "verification": "Lourdes Medical Bureau",
            }
        )
    
    def scrape_all(self) -> List[ScrapedCase]:
        """Scrape all Lourdes miracle cases."""
        all_miracles: List[LourdesMiracle] = []
        
        # Scrape all Lourdes pages
        for page in LOURDES_PAGES:
            url = urljoin(LOURDES_BASE_URL, page)
            try:
                miracles = self.scrape_lourdes_page(url)
                all_miracles.extend(miracles)
                self.logger.info(f"Found {len(miracles)} miracles on {page}")
            except Exception as e:
                self.logger.error(f"Failed to scrape {url}: {e}")
        
        # Deduplicate by name (lowercase, stripped) - entries appear on multiple pages
        seen_names = set()
        unique_miracles: List[LourdesMiracle] = []
        for m in all_miracles:
            name_key = m.name.lower().strip()
            if name_key not in seen_names:
                seen_names.add(name_key)
                # Assign sequential number to unique miracles
                m.number = len(unique_miracles) + 1
                unique_miracles.append(m)
        
        self.logger.info(f"Found {len(unique_miracles)} unique Lourdes miracles")
        
        # Convert and save
        cases: List[ScrapedCase] = []
        for miracle in sorted(unique_miracles, key=lambda m: m.number):
            case = self.miracle_to_case(miracle)
            self.save_case(case)
            cases.append(case)
        
        return cases


def main():
    """Run Lourdes scraper from command line."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Scrape Lourdes miracle healings")
    parser.add_argument("--output", "-o", type=Path, default=Path("data"),
                        help="Output directory")
    
    args = parser.parse_args()
    
    scraper = LourdesScraper(args.output)
    cases = scraper.scrape_all()
    
    print(f"\nScraped {len(cases)} cases to {scraper.output_dir}")


if __name__ == "__main__":
    main()
