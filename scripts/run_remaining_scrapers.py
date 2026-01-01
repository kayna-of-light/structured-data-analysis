"""Run Lourdes and Radical Remission scrapers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.lourdes_scraper import LourdesScraper
from scrapers.radical_remission_scraper import RadicalRemissionScraper

def run_lourdes():
    print("=" * 60)
    print("LOURDES MIRACLE HUNTER SCRAPER")
    print("=" * 60)
    
    output_dir = Path('data/lourdes_cases')
    scraper = LourdesScraper(output_dir)
    cases = scraper.scrape_all()
    
    print(f"\nScraped {len(cases)} Lourdes cases")
    
    # Show samples
    for case in cases[:3]:
        print(f"  - {case.title[:60]}...")
    
    return cases

def run_rrp():
    print("\n" + "=" * 60)
    print("RADICAL REMISSION PROJECT SCRAPER")
    print("=" * 60)
    
    output_dir = Path('data/rrp_cases')
    scraper = RadicalRemissionScraper(output_dir)
    cases = scraper.scrape_all()
    
    print(f"\nScraped {len(cases)} RRP cases")
    
    # Show samples
    for case in cases[:3]:
        content_len = len(case.content)
        print(f"  - [{content_len:,} chars] {case.title[:50]}...")
    
    return cases

if __name__ == "__main__":
    lourdes_cases = run_lourdes()
    rrp_cases = run_rrp()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Lourdes miracles: {len(lourdes_cases)}")
    print(f"Radical Remission stories: {len(rrp_cases)}")
    print(f"Total: {len(lourdes_cases) + len(rrp_cases)}")
