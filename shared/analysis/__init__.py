"""
Shared analysis utilities for NDE and Remission analysis projects.

This package provides common functionality for Azure OpenAI analysis:
- structured_extractor: Generic extraction pipeline with Azure client utilities
- base_analyzer: Base class for structured output analysis
"""

from .base_analyzer import (
    AnalysisJob,
    BaseAnalyzer,
)
from .structured_extractor import (
    ExtractorConfig,
    ExtractionJob,
    StructuredExtractor,
    build_user_prompt,
    load_azure_credentials,
    create_azure_client,
)

__all__ = [
    # Azure client utilities (from structured_extractor)
    "load_azure_credentials",
    "create_azure_client",
    # Base analyzer
    "AnalysisJob",
    "BaseAnalyzer",
    # Structured extractor
    "ExtractorConfig",
    "ExtractionJob",
    "StructuredExtractor",
    "build_user_prompt",
]
