# Structured Data Analysis Framework - AI Agent Instructions

## Critical: Research Integrity Principles

This project uses **Swedenborg's theological framework** as the theoretical lens for testing hypotheses. This does NOT mean:
- Confirming the framework because the researcher believes it
- Hedging against the framework to appear "objective"
- Swinging between these positions based on perceived user intent

**Honest research means:**
1. **Report what the data shows** — statistical patterns, effect sizes, significance levels
2. **Report what the data does not show** — what remains underdetermined or ambiguous
3. **Distinguish levels of claims:**
   - **Statistically supported**: p < 0.05, with effect size and test details
   - **Reasonable interpretation**: consistent with the data but not proven by it
   - **Speculative**: depends on accepting the theoretical framework
4. **Take the framework seriously enough to test it properly** — not dismissively, not reverently
5. **Do not adjust conclusions based on what you think the user wants to hear**

The neutral position is accuracy, not equidistance between confirmation and skepticism.

---

## Project Overview

This repository provides a **general-purpose framework** for converting scraped text datasets into structured data and performing systematic analysis using LLM-powered extraction. The framework supports research projects that:

1. **Scrape** data from various sources (web pages, databases, documents)
2. **Extract** structured data from unstructured text using Azure OpenAI
3. **Analyze** the structured data with statistical and qualitative methods

### Current Research Projects

| Project | Description | Data Sources |
|---------|-------------|--------------|
| **[NDE Analysis](projects/nde/)** | Near-death experience phenomenology | NDERF (~3,500), IANDS (~600) |
| **[Remission Analysis](projects/remission/)** | Spontaneous remission and psycho-spiritual transformation | PubMed Central, Radical Remission Project |

### Collaboration

This repository works in close collaboration with [literary-compilation](https://github.com/marconian/literary-compilation) for theoretical frameworks and interpretive lenses. Statistical findings from this project provide empirical evidence for concepts in the knowledge graph.

---

## Repository Architecture

```
structured-data-analysis/
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
│   ├── nderf/                         # ~3,500 NDERF experiences
│   ├── iands/                         # ~600 IANDS experiences
│   ├── pmc/                           # PubMed Central case reports
│   └── radical_remission/             # Radical Remission testimonials
│
├── projects/                          # ANALYSIS PROJECTS
│   └── [project_name]/                # Individual project
│       ├── extract.py                 # Structured extraction script
│       ├── models/questionnaire.py    # Pydantic schema for extraction
│       ├── registries/                # Dataset registry YAML files
│       ├── notebooks/                 # Analysis notebooks
│       ├── reports/                   # Generated reports (markdown)
│       ├── scripts/                   # Project-specific utilities
│       └── structured/                # Extraction output (JSON)
│
├── docs/                              # Documentation
│   ├── REPORT_WRITING_GUIDELINES.md   # Academic report structure
│   └── plans/                         # Planning documents
│
├── secrets/                           # API credentials (gitignored)
│   └── azure_openai.env               # Azure OpenAI credentials
│
└── tests/                             # Unit tests
```

---

## Core Concepts

### 1. Questionnaire Schema (Pydantic Models)

Each project defines a **questionnaire schema** as Pydantic models in `models/questionnaire.py`. These models:
- Define the structure of extracted data
- Use enums for categorical responses
- Include `Field(description=...)` for LLM guidance
- Inherit from `QuestionnaireBaseModel` with `extra="forbid"`

**Example pattern:**
```python
from pydantic import BaseModel, Field
from enum import Enum

class MentionResponse(str, Enum):
    YES_EXPLICIT = "yes_explicit"
    IMPLIED = "implied"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"

class MyResponse(BaseModel):
    feature_present: MentionResponse = Field(
        description="Was the feature explicitly mentioned or implied?"
    )
```

### 2. Registry System

Projects use **YAML registry files** to define which data files to analyze without duplicating data:

```yaml
# projects/my_project/registries/dataset.yaml
name: dataset_full
description: Complete dataset for analysis
version: "1.0.0"

datasets:
  source_name:
    description: Data source description
    source_path: ../../../data/source_name
    files: "*"           # or list of specific files
    exclude: []          # patterns to exclude
```

### 3. Extraction Pipeline

The `StructuredExtractor` class handles:
- Loading files via registries
- Parallel processing with configurable concurrency
- Azure OpenAI structured output parsing
- Progress tracking and resumption
- Error handling with retry logic

### 4. Data Flow

```
Raw Data (data/)
    ↓ extract.py + Azure OpenAI
Structured JSON (projects/*/structured/)
    ↓ Jupyter notebooks
Statistical Analysis (projects/*/notebooks/)
    ↓ Report generation
Markdown Reports (projects/*/reports/)
```

---

## Development Guidelines

### Creating a New Project

1. **Create project structure:**
```bash
mkdir -p projects/my_project/{models,registries,notebooks,reports,scripts,structured}
```

2. **Define questionnaire schema** in `models/questionnaire.py`
3. **Create extract.py** following the pattern in existing projects
4. **Create registry YAML files** in `registries/`
5. **Run extraction:** `python extract.py --max-concurrency 4`
6. **Create analysis notebooks** in `notebooks/`

### Extraction Script Pattern

```python
#!/usr/bin/env python3
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import MyResponseModel

SUPPORTED_DATASETS = ("source1", "source2")

SYSTEM_PROMPT = """
You are an expert researcher analyzing [domain].
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

### Command Line Options for extract.py

| Flag | Description |
|------|-------------|
| `--datasets source1 source2` | Select specific datasets to process |
| `--limit 25` | Process only first N cases (for testing) |
| `--dry-run` | List files without calling Azure OpenAI |
| `--overwrite` | Regenerate existing extractions |
| `--max-concurrency 4` | Parallel processing threads |
| `--log-level INFO` | Logging verbosity |

---

## Report Writing Standards

Follow the guidelines in [docs/REPORT_WRITING_GUIDELINES.md](docs/REPORT_WRITING_GUIDELINES.md):

### Report Structure

```
TITLE: [Descriptive Phrase]: [Methodology Subtitle]
│
├── ABSTRACT (Background, Methods, Results, Conclusions, Keywords)
├── DATA PROVENANCE TABLE
├── 1. INTRODUCTION (Background, Theoretical Framework, Aims)
├── 2. METHODS (Data Sources, Coding Scheme, Statistical Analysis)
├── 3. RESULTS (One finding per subsection: Narrative → Table → Finding Statement)
├── 4. DISCUSSION (Summary, Interpretation, Implications, Limitations, Future)
├── 5. CONCLUSION
├── REFERENCES
└── APPENDICES
```

### Statistical Reporting

- Always include: test statistic, df, p-value
- Format: `(χ² = 2845.61, df = 15, p < 0.0001)`
- Sample sizes: `n=443` (subset), `N=6,753` (total)
- Percentages: one decimal place `73.4%`

### Finding Statements

After each table, include a bolded interpretive statement:
```markdown
**Critical Finding**: The variable achieves **94.6% accuracy**. This represents...
```

---

## Notebook Conventions

### Naming Convention

Notebooks follow a numbered naming scheme:
- `01_being_of_light_analysis.ipynb`
- `02_normative_path_validation.ipynb`
- `03_volunteer_soul_profile.ipynb`

### Standard Imports

```python
import json
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Project paths
PROJECT_ROOT = Path.cwd().parent
DATA_ROOT = PROJECT_ROOT.parent / "data"
STRUCTURED_ROOT = PROJECT_ROOT / "structured"
```

### Loading Structured Data

```python
def load_structured_data(source: str) -> list[dict]:
    """Load all structured JSON files for a source."""
    source_dir = STRUCTURED_ROOT / source
    data = []
    for path in sorted(source_dir.glob("*.json")):
        with open(path) as f:
            data.append(json.load(f))
    return data

nderf_data = load_structured_data("nderf")
df = pd.DataFrame(nderf_data)
```

---

## Azure OpenAI Configuration

### Credentials File

Create `secrets/azure_openai.env`:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-05-01-preview
```

### Structured Output

The framework uses Azure OpenAI's **structured output** feature:
- Pydantic schemas are converted to JSON Schema
- The model is constrained to return valid JSON matching the schema
- Validation errors trigger automatic retry

---

## Scraper Development

### Adding a New Data Source

1. Create scraper in `shared/scrapers/[source]_scraper.py`
2. Inherit from `BaseScraper`
3. Implement `scrape()` method returning `List[ScrapedCase]`
4. Save output to `data/[source]/`

### ScrapedCase Schema

```python
@dataclass
class ScrapedCase:
    """Standardized output for all scrapers."""
    id: str
    title: str
    content: str
    source: str
    url: str
    scraped_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)
```

### HTTP Utilities

Use shared utilities from `shared/scrapers/base.py`:
- `http_get(url)` — Fetch with retry logic and rate limiting
- `slugify(text)` — Convert to URL-safe filename
- `clean_text(text)` — Normalize whitespace and encoding

---

## Testing

### Running Tests

```bash
pytest tests/
pytest tests/test_extractor.py -v
```

### Test Structure

```
tests/
├── test_extractor.py      # Extraction pipeline tests
├── test_registry.py       # Registry loader tests
└── test_scrapers.py       # Scraper unit tests
```

---

## Dependencies

### Core Dependencies (requirements.txt)

| Package | Purpose |
|---------|---------|
| `pydantic>=2.5` | Schema validation |
| `openai>=1.30` | Azure OpenAI client |
| `python-dotenv` | Environment loading |
| `requests` | HTTP requests |
| `beautifulsoup4` | HTML parsing |
| `pandas`, `numpy`, `scipy` | Data analysis |
| `matplotlib`, `seaborn` | Visualization |
| `jupyter` | Notebooks |

### Environment Setup

```bash
# Using pip
pip install -r requirements.txt

# Using conda
conda env create -f environment.yml
conda activate consciousness-research
```

---

## File Format Standards

### JSON Data Files

Each scraped/extracted file follows this structure:
```json
{
  "id": "unique_identifier",
  "title": "Document Title",
  "content": "Full text content...",
  "source": "dataset_name",
  "url": "https://source.url/path",
  "scraped_at": "2025-01-15T10:30:00Z",
  "metadata": {
    "additional": "fields"
  }
}
```

### Structured Output Files

Extraction output mirrors the Pydantic schema with additional metadata:
```json
{
  "_extraction_metadata": {
    "schema_name": "NDEAnalysisResponse",
    "schema_hash": "abc123...",
    "extracted_at": "2025-01-15T10:30:00Z",
    "model": "gpt-4o"
  },
  "field1": "value1",
  "field2": "value2"
}
```

---

## Common Patterns

### Enum Usage in Questionnaires

For categorical responses, prefer specific enums over booleans:

```python
class MentionResponse(str, Enum):
    YES_EXPLICIT = "yes_explicit"  # Directly stated
    IMPLIED = "implied"             # Inferrable from context
    NO = "no"                       # Explicitly negated
    NOT_MENTIONED = "not_mentioned" # No information
```

### Field Descriptions for LLM Guidance

Include detailed descriptions to guide extraction:

```python
light_encounter: LightEncounter = Field(
    description="""Type of light encounter. Select ONE value.
    Precedence: being_of_light > brilliant_light > presence_without_visual
    If the experiencer describes both brilliant light AND a being of light,
    select being_of_light - the being inherently indicates presence of light."""
)
```

### List Fields for Multiple Items

Use `List[Enum]` for multi-select responses:

```python
greeting_type: List[GreetingType] = Field(
    default_factory=list,
    description="Types of greeting upon arrival. Empty list means not mentioned."
)
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Azure API rate limits | Reduce `--max-concurrency` |
| Missing credentials | Check `secrets/azure_openai.env` exists |
| Registry path errors | Verify `source_path` is relative to registry file |
| Validation errors | Check Pydantic schema against actual output |
| Encoding issues | `http_get()` auto-detects encoding |

### Debugging Extraction

1. Run with `--limit 1` to test single file
2. Check `--dry-run` output for file resolution
3. Enable `--log-level DEBUG` for verbose output
4. Inspect structured output JSON for schema compliance

---

## Contributing

### Code Style

- Use `black` for formatting (line length 100)
- Use `ruff` for linting
- Type hints required for public APIs
- Docstrings for all public functions

### Pull Request Checklist

- [ ] Tests pass (`pytest tests/`)
- [ ] Code formatted (`black .`)
- [ ] Lint clean (`ruff .`)
- [ ] Documentation updated
- [ ] Questionnaire changes documented

---

## Quick Reference

### Run Extraction
```bash
cd projects/nde
python extract.py --datasets nderf iands --max-concurrency 4
```

### Run Analysis Notebook
```bash
cd projects/nde/notebooks
jupyter notebook 01_being_of_light_analysis.ipynb
```

### Load Registry
```python
from shared.registry import load_registry
registry = load_registry(Path("registries/nderf.yaml"))
files = registry.resolve_paths(Path("../../data"))
```

### Statistical Test
```python
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"χ² = {chi2:.2f}, df = {dof}, p = {p:.4f}")
```
