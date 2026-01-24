"""
Shared scraper modules.

This package provides scrapers for all data sources used across
the NDE and remission analysis projects.

Available scrapers:
- nderf: Near Death Experience Research Foundation (nderf.org)
- iands: International Association for Near-Death Studies
- pmc: PubMed Central (via OAI-PMH and E-utilities)
- mallworld: r/TheMallWorld subreddit dream reports
- radical_remission: Radical Remission Project database (future)
- lourdes: Lourdes Medical Bureau documented cases (future)
- ions: Institute of Noetic Sciences (future)
"""

from .base import (
    get_session,
    http_get,
    slugify,
    clean_text,
    pad_id,
    ScrapedCase,
    BaseScraper,
    logger,
)

from .nderf_scraper import NDERFScraper
from .iands_scraper import IANDSScraper
from .pmc_scraper import PMCScraper
from .radical_remission_scraper import RadicalRemissionScraper


def __getattr__(name: str):
    # Lazy imports to avoid `python -m shared.scrapers.reddit_scraper` warnings.
    if name == "RedditScraper":
        from .reddit_scraper import RedditScraper

        return RedditScraper
    if name == "MallWorldScraper":
        from .mallworld_scraper import MallWorldScraper

        return MallWorldScraper
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)

__all__ = [
    # Base utilities
    "get_session",
    "http_get",
    "slugify",
    "clean_text",
    "pad_id",
    # Data structures
    "ScrapedCase",
    "BaseScraper",
    # Scraper classes
    "NDERFScraper",
    "IANDSScraper",
    "PMCScraper",
    "RadicalRemissionScraper",
    "RedditScraper",
    "MallWorldScraper",
    # Logging
    "logger",
]

