"""Deprecated: MallWorld-specific wrapper.

This module is kept for backwards compatibility. New code should use
`shared.scrapers.reddit_scraper.RedditScraper` and pass `--subreddit` / `--dataset`.

CLI Usage (preferred):
    python -m shared.scrapers.reddit_scraper --subreddit TheMallWorld --dataset mallworld
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from .base import ScrapedCase
from .reddit_scraper import RedditScraper


class MallWorldScraper(RedditScraper):
    """Backwards-compatible alias for the old MallWorld scraper."""

    def __init__(
        self,
        output_dir: Path,
        request_delay: float = 2.0,
        min_content_length: int = 100,
    ) -> None:
        super().__init__(
            output_dir=output_dir,
            subreddit="TheMallWorld",
            dataset="mallworld",
            request_delay=request_delay,
            min_content_length=min_content_length,
        )
    

def main() -> None:
    """Deprecated entry point; forwards to the generic Reddit scraper."""

    scraper = MallWorldScraper(output_dir=Path(__file__).parent.parent.parent / "data")
    cases = scraper.scrape_all(max_posts=None, sort="new")
    print(f"\nScraping complete! Total posts saved: {len(cases)}")
    print(f"Output directory: {scraper.output_dir}")
    print(f"Total posts in directory: {len(list(scraper.output_dir.glob('*.json')))}")


if __name__ == "__main__":
    main()
