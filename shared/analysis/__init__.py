"""
Shared analysis utilities for NDE and Remission analysis projects.

This package provides common functionality for Azure OpenAI analysis:
- azure_client: Azure OpenAI client wrapper with retry logic
- base_analyzer: Base class for structured output analysis
- structured_extractor: Generic extraction pipeline
"""

from .azure_client import (
    load_azure_credentials,
    create_azure_client,
    AzureConfig,
)
from .base_analyzer import (
    AnalysisJob,
    BaseAnalyzer,
)
from .structured_extractor import (
    ExtractorConfig,
    ExtractionJob,
    StructuredExtractor,
    build_user_prompt,
)

__all__ = [
    # Azure client utilities
    "load_azure_credentials",
    "create_azure_client",
    "AzureConfig",
    # Base analyzer
    "AnalysisJob",
    "BaseAnalyzer",
    # Structured extractor
    "ExtractorConfig",
    "ExtractionJob",
    "StructuredExtractor",
    "build_user_prompt",
]
