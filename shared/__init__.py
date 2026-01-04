"""
Shared core library for consciousness research data analysis.

This package provides:
- Common scraper utilities and base classes (scrapers/)
- Azure OpenAI analysis infrastructure (analysis/)
- Dataset registry management (registry/)
- Shared Pydantic models and enums (models/)
"""

__version__ = "1.0.0"

from . import scrapers
from . import registry
from . import analysis
from . import models

__all__ = [
    "scrapers",
    "registry",
    "analysis",
    "models",
]
