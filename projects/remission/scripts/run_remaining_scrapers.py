"""Run Lourdes and Radical Remission scrapers."""
import sys
from pathlib import Path

# Add shared to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))

from scrapers.radical_remission_scraper import RadicalRemissionScraper

def run_rrp():
    print("\n" + "=" * 60)
    print("RADICAL REMISSION PROJECT SCRAPER")
    print("=" * 60)
    
    output_dir = Path('../../data/radical_remission')
    scraper = RadicalRemissionScraper(output_dir)
    cases = scraper.scrape_all()
    
    print(f"\nScraped {len(cases)} RRP cases")
    
    # Show samples
    for case in cases[:3]:
        content_len = len(case.content)
        print(f"  - [{content_len:,} chars] {case.title[:50]}...")
    
    return cases

if __name__ == "__main__":
    rrp_cases = run_rrp()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Radical Remission stories: {len(rrp_cases)}")
    print(f"Total: {len(rrp_cases)}")
