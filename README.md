# Structured Data Analysis Framework

A general-purpose framework for converting scraped text datasets into structured data and performing systematic analysis using LLM-powered extraction.

## Overview

This repository provides a coherent and common base for research projects that:
1. **Scrape** data from various sources (web pages, databases, documents)
2. **Extract** structured data from unstructured text using LLM-powered questionnaires
3. **Analyze** the structured data with statistical and qualitative methods

The framework includes reusable components for web scraping, Azure OpenAI integration, data registry management, and extensible questionnaire schemas. Projects can be added to analyze any type of narrative or document corpus.

### Current Projects

- **[NDE Analysis](projects/nde/)**: Structured analysis of near-death experience narratives from NDERF and IANDS databases
- **[Remission Analysis](projects/remission/)**: Statistical analysis of spontaneous remission cases and their relationship to psycho-spiritual transformation

### Key Features

- **Shared Scrapers**: Reusable web scraping utilities with a common base class
- **LLM-Powered Extraction**: Azure OpenAI integration with Pydantic schema validation
- **Registry System**: YAML-based dataset management to avoid data duplication
- **Project Isolation**: Each project has its own questionnaire schema, analysis scripts, and outputs
- **Parallel Processing**: Configurable concurrency for efficient batch processing

## Repository Structure

```
remission-analysis/                    # Framework root
├── shared/                            # SHARED CORE LIBRARY
│   ├── scrapers/                      # Common scraper utilities
│   │   ├── base.py                    # BaseScraper, ScrapedCase, http utilities
│   │   └── [source]_scraper.py        # Source-specific scrapers
│   ├── analysis/                      # Azure OpenAI analysis utilities
│   │   ├── azure_client.py            # Credential management
│   │   ├── base_analyzer.py           # BaseAnalyzer class
│   │   └── structured_extractor.py    # Generic extraction pipeline
│   ├── registry/                      # Dataset registry management
│   │   └── loader.py                  # YAML registry loader
│   └── models/                        # Shared Pydantic models
│       └── common.py                  # Base model classes
│
├── data/                              # UNIFIED DATA REPOSITORY
│   └── [source]/                      # One directory per data source
│
├── projects/                          # ANALYSIS PROJECTS
│   └── [project_name]/                # Individual project
│       ├── extract.py                 # Structured extraction script
│       ├── models/                    # Project-specific questionnaire schema
│       │   └── questionnaire.py       # Pydantic models for extraction
│       ├── registries/                # Dataset registry YAML files
│       ├── notebooks/                 # Analysis notebooks
│       ├── reports/                   # Generated reports
│       ├── scripts/                   # Project-specific utilities
│       ├── structured/                # Extraction output (JSON)
│       └── README.md                  # Project documentation
│
├── docs/                              # General documentation
├── tests/                             # Unit tests
└── secrets/                           # API credentials (gitignored)
```

## Getting Started

### Prerequisites

- Python 3.10+
- Azure OpenAI API access (for LLM-powered extraction)
- pip or conda for package management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/marconian/remission-analysis.git
cd remission-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# Or with conda:
conda env create -f environment.yml
```

3. Configure Azure OpenAI credentials (create `secrets/azure_openai.env`):
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-05-01-preview
```

## Creating a New Project

To create a new analysis project using this framework:

### 1. Create Project Structure

```bash
mkdir -p projects/my_project/{models,registries,notebooks,reports,scripts,structured}
touch projects/my_project/{README.md,extract.py}
touch projects/my_project/models/__init__.py
touch projects/my_project/models/questionnaire.py
```

### 2. Define Your Questionnaire Schema

Create Pydantic models in `projects/my_project/models/questionnaire.py`:

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class MyResponseModel(BaseModel):
    """Your structured extraction schema."""
    
    # Define fields relevant to your research question
    topic: str = Field(description="Main topic of the document")
    sentiment: Optional[str] = Field(description="Overall sentiment")
    key_points: List[str] = Field(default_factory=list)
    # ... add more fields as needed
```

### 3. Create Extraction Script

Create `projects/my_project/extract.py` following the pattern:

```python
#!/usr/bin/env python3
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import MyResponseModel

SUPPORTED_DATASETS = ("my_datasource",)

SYSTEM_PROMPT = """
You are an expert researcher analyzing [your domain].
Extract structured information according to the schema.
Ground every answer in the source text.
"""

def main() -> None:
    config = ExtractorConfig(
        response_model=MyResponseModel,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        registries_dir=PROJECT_ROOT / "registries",
    )
    
    extractor = StructuredExtractor(config)
    extractor.run()

if __name__ == "__main__":
    main()
```

### 4. Create Dataset Registries

Create YAML files in `projects/my_project/registries/`:

```yaml
# my_datasource.yaml
name: my_datasource_full
description: My dataset for analysis
source: my_datasource
mode: all
```

### 5. Add Your Data Source Scraper (Optional)

If you need a new data source, create a scraper in `shared/scrapers/`:

```python
from shared.scrapers.base import BaseScraper, ScrapedCase

class MySourceScraper(BaseScraper):
    def scrape(self) -> List[ScrapedCase]:
        # Implement your scraping logic
        pass
```

### 6. Run Your Analysis

```bash
cd projects/my_project
python extract.py --max-concurrency 4 --log-level INFO
```

### 7. Create Analysis Notebooks

Add Jupyter notebooks to `projects/my_project/notebooks/` for statistical analysis and visualization.

## Workflow

### 1. Data Collection (Scraping)

Scrapers are located in `shared/scrapers/`. Run source-specific scrapers to collect data:

```bash
python shared/scrapers/my_source_scraper.py
```

Data is saved to `data/[source]/` directory.

### 2. Structured Extraction

Each project has an `extract.py` script that processes raw data through Azure OpenAI:

```bash
cd projects/[project_name]
python extract.py --max-concurrency 4 --log-level INFO
```

Common flags:
- `--datasets source1 source2` — select specific datasets
- `--limit 25` — process a sample for validation
- `--dry-run` — list files without calling Azure
- `--overwrite` — regenerate existing extractions

Structured output is saved to `projects/[project_name]/structured/`.

### 3. Statistical Analysis

Use Jupyter notebooks in `projects/[project_name]/notebooks/` for analysis:

```bash
cd projects/[project_name]/notebooks
jupyter notebook analysis.ipynb
```

## Common Patterns

### Registry System

Projects use YAML registry files to define which data files to analyze without duplicating data:

```yaml
# projects/my_project/registries/my_source.yaml
name: my_source_full
description: Complete dataset for analysis
source: my_source  # references data/my_source/
mode: all          # or specify file lists
```

Load registries in Python:

```python
from shared.registry import load_registry
from pathlib import Path

registry = load_registry(Path("registries/my_source.yaml"))
files = registry.resolve_paths(Path("../../data"))
```

### Extraction Pipeline

All extraction scripts follow the same pattern:
1. Define Pydantic schema (questionnaire)
2. Configure `ExtractorConfig` with schema and prompts
3. Initialize `StructuredExtractor`
4. Run extraction with parallel processing
5. Output structured JSON files

## Collaboration

This repository works in close collaboration with the [literary-compilation](https://github.com/marconian/literary-compilation) project for theoretical frameworks and interpretive lenses.

## Related Projects

- [nde-data-analysis](https://github.com/marconian/nde-data-analysis) — Parent project methodology

## License

MIT License
