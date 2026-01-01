"""
Main runner script for all remission data scrapers.

Usage:
    python run_scrapers.py --all                    # Run all scrapers
    python run_scrapers.py --pmc                    # Run PMC scraper only
    python run_scrapers.py --lourdes                # Run Lourdes scraper only
    python run_scrapers.py --rrp                    # Run Radical Remission scraper only
    python run_scrapers.py --ions --pdf path.pdf    # Run IONS with PDF
"""

import argparse
import logging
import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from scrapers import PMCScraper, LourdesScraper, RadicalRemissionScraper, IONSScraper

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


def run_lourdes(output_dir: Path):
    """Run Lourdes/Miracle Hunter scraper."""
    logger.info("=" * 60)
    logger.info("Starting Lourdes Scraper")
    logger.info("=" * 60)
    
    scraper = LourdesScraper(output_dir)
    cases = scraper.scrape_all()
    
    logger.info(f"Lourdes: Scraped {len(cases)} miracle cases")
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


def run_ions(output_dir: Path, pdf_path: Path = None, rehydrate: bool = True):
    """Run IONS bibliography scraper."""
    logger.info("=" * 60)
    logger.info("Starting IONS Bibliography Scraper")
    logger.info("=" * 60)
    
    scraper = IONSScraper(output_dir, pdf_path=pdf_path)
    cases = scraper.scrape_all(rehydrate=rehydrate)
    
    logger.info(f"IONS: Processed {len(cases)} citations")
    return cases


def main():
    parser = argparse.ArgumentParser(
        description="Scrape spontaneous remission case data from multiple sources"
    )
    
    # Output configuration
    parser.add_argument("--output", "-o", type=Path, default=Path("data/scraped"),
                        help="Output directory for scraped data")
    
    # Scraper selection
    parser.add_argument("--all", action="store_true",
                        help="Run all scrapers")
    parser.add_argument("--pmc", action="store_true",
                        help="Run PMC case report scraper")
    parser.add_argument("--lourdes", action="store_true",
                        help="Run Lourdes/Miracle Hunter scraper")
    parser.add_argument("--rrp", action="store_true",
                        help="Run Radical Remission Project scraper")
    parser.add_argument("--ions", action="store_true",
                        help="Run IONS bibliography scraper")
    
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
    
    # IONS options
    parser.add_argument("--pdf", type=Path, default=None,
                        help="Path to IONS bibliography PDF")
    parser.add_argument("--no-rehydrate", action="store_true",
                        help="Skip PubMed lookup for IONS citations")
    
    args = parser.parse_args()
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Determine which scrapers to run
    run_all = args.all or not (args.pmc or args.lourdes or args.rrp or args.ions)
    
    total_cases = 0
    
    if run_all or args.pmc:
        cases = run_pmc(args.output, args.pmc_max, args.email, args.api_key)
        total_cases += len(cases)
    
    if run_all or args.lourdes:
        cases = run_lourdes(args.output)
        total_cases += len(cases)
    
    if run_all or args.rrp:
        cases = run_rrp(args.output, args.rrp_max, not args.no_selenium)
        total_cases += len(cases)
    
    if run_all or args.ions:
        cases = run_ions(args.output, args.pdf, not args.no_rehydrate)
        total_cases += len(cases)
    
    logger.info("=" * 60)
    logger.info(f"COMPLETE: Total cases scraped: {total_cases}")
    logger.info(f"Data saved to: {args.output}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
