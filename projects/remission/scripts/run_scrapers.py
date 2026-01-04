"""
Main runner script for all remission data scrapers.

Usage:
    python run_scrapers.py --all                    # Run all scrapers
    python run_scrapers.py --pmc                    # Run PMC scraper only
    python run_scrapers.py --rrp                    # Run Radical Remission scraper only
"""

import argparse
import logging
import sys
from pathlib import Path

# Add shared to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))

from scrapers import PMCScraper, RadicalRemissionScraper

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_pmc(output_dir: Path, max_articles: int = 100, email: str = None, api_key: str = None):
    """Run PMC case report scraper."""
    logger.info("=" * 60)
    logger.info("Starting PMC Scraper")
    logger.info("=" * 60)
    
    scraper = PMCScraper(output_dir, email=email, api_key=api_key)
    cases = scraper.scrape_all(max_articles=max_articles)
    
    logger.info(f"PMC: Scraped {len(cases)} case reports")
    return cases


def run_rrp(output_dir: Path, max_stories: int = 100, use_selenium: bool = True):
    """Run Radical Remission Project scraper."""
    logger.info("=" * 60)
    logger.info("Starting Radical Remission Project Scraper")
    logger.info("=" * 60)
    
    scraper = RadicalRemissionScraper(output_dir, use_selenium=use_selenium)
    cases = scraper.scrape_all(max_stories=max_stories)
    
    logger.info(f"RRP: Scraped {len(cases)} survivor stories")
    return cases


def main():
    parser = argparse.ArgumentParser(
        description="Scrape spontaneous remission case data from multiple sources"
    )
    
    # Output configuration
    parser.add_argument("--output", "-o", type=Path, default=Path("../../../data"),
                        help="Output directory for scraped data")
    
    # Scraper selection
    parser.add_argument("--all", action="store_true",
                        help="Run all scrapers")
    parser.add_argument("--pmc", action="store_true",
                        help="Run PMC case report scraper")
    parser.add_argument("--rrp", action="store_true",
                        help="Run Radical Remission Project scraper")
    
    # PMC options
    parser.add_argument("--pmc-max", type=int, default=100,
                        help="Max PMC articles to process")
    parser.add_argument("--email", type=str, default=None,
                        help="Email for NCBI (recommended)")
    parser.add_argument("--api-key", type=str, default=None,
                        help="NCBI API key for higher rate limits")
    
    # RRP options
    parser.add_argument("--rrp-max", type=int, default=100,
                        help="Max RRP stories to process")
    parser.add_argument("--no-selenium", action="store_true",
                        help="Disable Selenium for RRP scraping")
    
    args = parser.parse_args()
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Determine which scrapers to run
    run_all = args.all or not (args.pmc or args.rrp)
    
    total_cases = 0
    
    if run_all or args.pmc:
        cases = run_pmc(args.output / "pmc", args.pmc_max, args.email, args.api_key)
        total_cases += len(cases)
    
    if run_all or args.rrp:
        cases = run_rrp(args.output / "radical_remission", args.rrp_max, not args.no_selenium)
        total_cases += len(cases)
    
    logger.info("=" * 60)
    logger.info(f"COMPLETE: Total cases scraped: {total_cases}")
    logger.info(f"Data saved to: {args.output}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
