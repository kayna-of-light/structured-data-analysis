"""Run full IONS scraper and save output."""
import sys
from pathlib import Path
import shutil

sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.ions_scraper import IONSScraper

# Clean previous output
output_dir = Path('data/test_output/ions')
if output_dir.exists():
    shutil.rmtree(output_dir)
    
s = IONSScraper(Path('data/test_output'))
cases = s.scrape_all(rehydrate=True)

print(f'Scraped {len(cases)} cases')
for case in cases:
    content_type = case.metadata.get("content_type", "unknown")
    print(f'  - {case.title[:50]}... ({len(case.content)} chars, {content_type})')
