"""
Azure OpenAI client wrapper with retry logic and credential management.

Provides a consistent interface for Azure OpenAI across all analysis scripts.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

from dotenv import dotenv_values
from openai import AzureOpenAI

logger = logging.getLogger(__name__)

DEFAULT_API_VERSION = "2024-05-01-preview"


@dataclass
class AzureConfig:
    """Azure OpenAI configuration."""
    endpoint: str
    api_key: str
    deployment: str
    api_version: str = DEFAULT_API_VERSION
    
    def create_client(self) -> AzureOpenAI:
        """Create an Azure OpenAI client with this configuration."""
        return AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
        )


def load_azure_credentials(
    config_path: Optional[Path] = None,
    *,
    require_all: bool = True,
) -> Dict[str, str]:
    """
    Load Azure OpenAI credentials from environment and/or config file.
    
    Priority (highest to lowest):
    1. Config file values (if provided and exists)
    2. Environment variables
    
    Args:
        config_path: Path to .env file with credentials
        require_all: If True, raise error if required credentials missing
        
    Returns:
        Dict with credential keys and values
        
    Raises:
        RuntimeError: If require_all=True and required credentials missing
        FileNotFoundError: If config_path specified but doesn't exist
    """
    collected: Dict[str, str] = {}
    
    # Required keys
    required_keys = (
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_KEY",
        "AZURE_OPENAI_DEPLOYMENT",
    )
    
    # Optional keys with defaults
    optional_keys = {
        "AZURE_OPENAI_API_VERSION": DEFAULT_API_VERSION,
    }
    
    # First, collect from environment
    for key in required_keys:
        env_value = os.getenv(key)
        if env_value:
            collected[key] = env_value
            
    for key, default in optional_keys.items():
        env_value = os.getenv(key)
        collected[key] = env_value if env_value else default
    
    # Then, override with config file values if provided
    if config_path is not None:
        if not config_path.exists():
            raise FileNotFoundError(
                f"Azure credentials file not found at {config_path}. "
                f"Create this file with AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, "
                f"and AZURE_OPENAI_DEPLOYMENT values."
            )
        
        file_values = dotenv_values(config_path)
        for key, value in file_values.items():
            if value:  # Only override if non-empty
                collected[key] = value
    
    # Check for missing required credentials
    if require_all:
        missing = [key for key in required_keys if not collected.get(key)]
        if missing:
            joined = ", ".join(missing)
            raise RuntimeError(f"Missing Azure OpenAI credentials: {joined}")
    
    return collected


def create_azure_client(
    config_path: Optional[Path] = None,
    *,
    endpoint: Optional[str] = None,
    api_key: Optional[str] = None,
    deployment: Optional[str] = None,
    api_version: Optional[str] = None,
) -> tuple[AzureOpenAI, str]:
    """
    Create an Azure OpenAI client.
    
    Credentials can be provided via:
    1. Explicit parameters (highest priority)
    2. Config file
    3. Environment variables
    
    Args:
        config_path: Path to .env file with credentials
        endpoint: Azure OpenAI endpoint URL
        api_key: Azure OpenAI API key
        deployment: Azure OpenAI deployment name
        api_version: API version (defaults to latest supported)
        
    Returns:
        Tuple of (AzureOpenAI client, deployment name)
        
    Raises:
        RuntimeError: If required credentials are missing
    """
    # Load credentials from file/env
    creds = load_azure_credentials(config_path, require_all=False)
    
    # Override with explicit parameters
    final_endpoint = endpoint or creds.get("AZURE_OPENAI_ENDPOINT")
    final_key = api_key or creds.get("AZURE_OPENAI_KEY")
    final_deployment = deployment or creds.get("AZURE_OPENAI_DEPLOYMENT")
    final_version = api_version or creds.get("AZURE_OPENAI_API_VERSION", DEFAULT_API_VERSION)
    
    # Validate required fields
    missing = []
    if not final_endpoint:
        missing.append("endpoint")
    if not final_key:
        missing.append("api_key")
    if not final_deployment:
        missing.append("deployment")
        
    if missing:
        raise RuntimeError(f"Missing Azure OpenAI credentials: {', '.join(missing)}")
    
    config = AzureConfig(
        endpoint=final_endpoint,
        api_key=final_key,
        deployment=final_deployment,
        api_version=final_version,
    )
    
    logger.info(
        "Creating Azure OpenAI client: endpoint=%s, deployment=%s, version=%s",
        config.endpoint,
        config.deployment,
        config.api_version,
    )
    
    return config.create_client(), config.deployment
