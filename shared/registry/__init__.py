"""
Registry-based dataset management.

This package provides a YAML-based registry system for managing datasets
across projects without duplicating files.
"""

from .loader import (
    DatasetConfig,
    DatasetRegistry,
    load_registry,
    create_registry,
)

__all__ = [
    "DatasetConfig",
    "DatasetRegistry",
    "load_registry",
    "create_registry",
]
