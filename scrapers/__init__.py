# Spontaneous Remission Data Scrapers
"""
Scrapers for collecting spontaneous remission case data from:
- PMC (PubMed Central) - Peer-reviewed case reports via OAI-PMH
- Radical Remission Project - Clinical survivor narratives
- Lourdes/Miracle Hunter - Forensically verified healing cases
- IONS Bibliography - Legacy research citations
"""

from scrapers.base import BaseScraper, ScrapedCase, http_get, clean_text, slugify
from scrapers.pmc_scraper import PMCScraper
from scrapers.lourdes_scraper import LourdesScraper
from scrapers.radical_remission_scraper import RadicalRemissionScraper
from scrapers.ions_scraper import IONSScraper

__all__ = [
    "BaseScraper",
    "ScrapedCase",
    "PMCScraper",
    "LourdesScraper",
    "RadicalRemissionScraper",
    "IONSScraper",
    "http_get",
    "clean_text",
    "slugify",
]
