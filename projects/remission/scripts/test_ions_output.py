"""Test IONS scraper output."""
import sys
from pathlib import Path

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.ions_scraper import IONSScraper

s = IONSScraper(Path('data/test_output'))
entries_file = Path('data/test_output/ions_entries.json')
citations = s.parse_manual_entries(entries_file)

# Convert to cases and show content
for c in citations:
    s.rehydrate_citation(c)
    case = s.citation_to_case(c)
    print("\n" + "=" * 60)
    print(f"Title: {case.title[:60]}...")
    print(f"URL: {case.url}")
    print(f"Content Type: {case.metadata.get('content_type')}")
    print(f"Content ({len(case.content)} chars):")
    content_preview = case.content[:500] + "..." if len(case.content) > 500 else case.content
    print(content_preview)
