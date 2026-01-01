"""Test PMC scraper with targeted case report search."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.pmc_scraper import PMCScraper

def main():
    output_dir = Path("data/test_output")
    
    scraper = PMCScraper(output_dir)
    
    # Test with small batch first
    print("Testing PMC scraper with 10 articles...")
    cases = scraper.scrape_all(max_articles=10, download_pdfs=True)
    
    print(f"\n{'='*60}")
    print(f"Scraped {len(cases)} cases")
    print(f"{'='*60}")
    
    for case in cases[:5]:
        content_type = case.metadata.get("content_type", "unknown")
        content_len = len(case.content)
        has_pdf = "✓" if case.metadata.get("pdf_path") else "✗"
        print(f"  [{content_type}] [PDF:{has_pdf}] {case.title[:60]}...")

if __name__ == "__main__":
    main()
