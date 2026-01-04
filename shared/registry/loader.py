"""
Registry-based dataset management.

This module provides a YAML-based registry system for managing datasets
across projects. Instead of duplicating data files, projects define
YAML registry files that reference a canonical data source.

Usage:
    from shared.registry import DatasetRegistry
    
    # Load a registry
    registry = DatasetRegistry.load("nde_analysis_registry.yaml")
    
    # Get file paths
    nderf_files = registry.get_files("nderf")
    
    # Check if a file is included
    is_included = registry.includes("nderf", "12345_john-doe.json")
"""

import fnmatch
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Set, Union

import yaml


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class DatasetConfig:
    """Configuration for a single dataset in a registry."""
    
    name: str
    description: str
    source_path: Path
    files: Union[str, List[str]]  # "*" for all, or list of specific files
    
    # Optional filters
    exclude_patterns: List[str] = field(default_factory=list)
    
    def get_file_paths(self) -> List[Path]:
        """
        Get list of actual file paths matching the configuration.
        
        Returns:
            List of Path objects for matching files
        """
        if not self.source_path.exists():
            raise FileNotFoundError(f"Source path does not exist: {self.source_path}")
        
        if self.files == "*":
            # Include all files (except excluded patterns)
            all_files = list(self.source_path.glob("*.json"))
        elif isinstance(self.files, list):
            # Include specific files
            all_files = []
            for pattern in self.files:
                if "*" in pattern or "?" in pattern:
                    # Glob pattern
                    all_files.extend(self.source_path.glob(pattern))
                else:
                    # Exact filename
                    filepath = self.source_path / pattern
                    if filepath.exists():
                        all_files.append(filepath)
        else:
            raise ValueError(f"Invalid files specification: {self.files}")
        
        # Apply exclusion patterns
        if self.exclude_patterns:
            filtered = []
            for fp in all_files:
                exclude = False
                for pattern in self.exclude_patterns:
                    if fnmatch.fnmatch(fp.name, pattern):
                        exclude = True
                        break
                if not exclude:
                    filtered.append(fp)
            all_files = filtered
        
        return sorted(all_files)
    
    def includes(self, filename: str) -> bool:
        """
        Check if a specific file is included in this dataset.
        
        Args:
            filename: Name of file to check (not full path)
            
        Returns:
            True if file is included
        """
        # Check exclusion patterns first
        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(filename, pattern):
                return False
        
        if self.files == "*":
            return True
        
        if isinstance(self.files, list):
            for pattern in self.files:
                if "*" in pattern or "?" in pattern:
                    if fnmatch.fnmatch(filename, pattern):
                        return True
                elif filename == pattern:
                    return True
        
        return False


@dataclass
class DatasetRegistry:
    """
    Registry of datasets for a project.
    
    A registry defines which files from shared data sources are used
    by a specific project, allowing projects to share a canonical
    data store without duplicating files.
    """
    
    name: str
    description: str
    version: str
    datasets: Dict[str, DatasetConfig] = field(default_factory=dict)
    
    # Base path for resolving relative source paths
    base_path: Optional[Path] = None
    
    @classmethod
    def load(cls, registry_path: Union[str, Path], base_path: Optional[Path] = None) -> "DatasetRegistry":
        """
        Load registry from YAML file.
        
        Args:
            registry_path: Path to YAML registry file
            base_path: Base path for resolving relative source paths.
                       If None, uses the registry file's directory.
                       
        Returns:
            Loaded DatasetRegistry
        """
        registry_path = Path(registry_path)
        if not registry_path.exists():
            raise FileNotFoundError(f"Registry file not found: {registry_path}")
        
        with open(registry_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        # Determine base path for resolving relative paths
        if base_path is None:
            base_path = registry_path.parent
        
        # Parse registry metadata
        registry = cls(
            name=data.get("name", registry_path.stem),
            description=data.get("description", ""),
            version=data.get("version", "1.0.0"),
            base_path=base_path,
        )
        
        # Parse datasets
        for dataset_name, dataset_data in data.get("datasets", {}).items():
            # Resolve source path relative to base
            source_path = dataset_data.get("source_path", "")
            if source_path:
                source_path = base_path / source_path
            else:
                raise ValueError(f"Dataset '{dataset_name}' missing source_path")
            
            # Parse files specification
            files = dataset_data.get("files", "*")
            
            # Parse exclusion patterns
            exclude = dataset_data.get("exclude", [])
            
            config = DatasetConfig(
                name=dataset_name,
                description=dataset_data.get("description", ""),
                source_path=source_path,
                files=files,
                exclude_patterns=exclude,
            )
            registry.datasets[dataset_name] = config
        
        return registry
    
    def get_dataset(self, name: str) -> DatasetConfig:
        """
        Get configuration for a specific dataset.
        
        Args:
            name: Dataset name
            
        Returns:
            DatasetConfig for the dataset
            
        Raises:
            KeyError: If dataset not found
        """
        if name not in self.datasets:
            raise KeyError(f"Dataset '{name}' not found in registry")
        return self.datasets[name]
    
    def get_files(self, dataset_name: str) -> List[Path]:
        """
        Get file paths for a dataset.
        
        Args:
            dataset_name: Name of dataset
            
        Returns:
            List of file paths
        """
        return self.get_dataset(dataset_name).get_file_paths()
    
    def includes(self, dataset_name: str, filename: str) -> bool:
        """
        Check if a file is included in a dataset.
        
        Args:
            dataset_name: Name of dataset
            filename: Name of file to check
            
        Returns:
            True if file is included
        """
        return self.get_dataset(dataset_name).includes(filename)
    
    def iter_files(self, dataset_name: str) -> Iterator[Path]:
        """
        Iterate over files in a dataset.
        
        Args:
            dataset_name: Name of dataset
            
        Yields:
            File paths
        """
        yield from self.get_files(dataset_name)
    
    def list_datasets(self) -> List[str]:
        """Get list of dataset names."""
        return list(self.datasets.keys())
    
    def summary(self) -> Dict[str, int]:
        """
        Get summary of file counts per dataset.
        
        Returns:
            Dict mapping dataset name to file count
        """
        return {name: len(config.get_file_paths()) 
                for name, config in self.datasets.items()}
    
    def save(self, output_path: Union[str, Path]) -> None:
        """
        Save registry to YAML file.
        
        Args:
            output_path: Path to write YAML file
        """
        data = {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "datasets": {},
        }
        
        for name, config in self.datasets.items():
            # Convert source path to relative if possible
            source_path = str(config.source_path)
            if self.base_path:
                try:
                    source_path = str(config.source_path.relative_to(self.base_path))
                except ValueError:
                    pass  # Keep absolute path
            
            dataset_data = {
                "description": config.description,
                "source_path": source_path,
                "files": config.files,
            }
            if config.exclude_patterns:
                dataset_data["exclude"] = config.exclude_patterns
            
            data["datasets"][name] = dataset_data
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def load_registry(path: Union[str, Path]) -> DatasetRegistry:
    """
    Load a dataset registry from file.
    
    Args:
        path: Path to registry YAML file
        
    Returns:
        Loaded DatasetRegistry
    """
    return DatasetRegistry.load(path)


def create_registry(
    name: str,
    description: str,
    datasets: Dict[str, Dict],
    base_path: Optional[Path] = None,
) -> DatasetRegistry:
    """
    Create a new registry programmatically.
    
    Args:
        name: Registry name
        description: Registry description
        datasets: Dict mapping dataset names to config dicts
        base_path: Base path for source paths
        
    Returns:
        New DatasetRegistry
    """
    registry = DatasetRegistry(
        name=name,
        description=description,
        version="1.0.0",
        base_path=base_path,
    )
    
    for ds_name, ds_config in datasets.items():
        source_path = ds_config.get("source_path", "")
        if base_path and source_path:
            source_path = base_path / source_path
        
        config = DatasetConfig(
            name=ds_name,
            description=ds_config.get("description", ""),
            source_path=Path(source_path) if source_path else Path(),
            files=ds_config.get("files", "*"),
            exclude_patterns=ds_config.get("exclude", []),
        )
        registry.datasets[ds_name] = config
    
    return registry


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    "DatasetConfig",
    "DatasetRegistry",
    "load_registry",
    "create_registry",
]
