"""Run full PMC scrape - only saving cases with full content."""
from pathlib import Path
from scrapers.pmc_scraper import PMCScraper

def main():
    output_dir = Path('data/pmc_cases')
    scraper = PMCScraper(output_dir)
    
    print('Starting PMC scrape for spontaneous remission case reports...')
    print('Only cases with FULL TEXT will be saved.')
    print('This will take ~20-30 minutes due to NCBI rate limits.')
    print()
    
    # Get all available (up to 600)
    cases = scraper.scrape_all(max_articles=600, download_pdfs=True)
    
    print(f'\nDone! Saved {len(cases)} full-text case reports.')

if __name__ == "__main__":
    main()
