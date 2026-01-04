# NDE Analysis Project

Structured analysis of Near-Death Experience (NDE) narratives using LLM-powered questionnaire extraction.

## Research Overview

This project applies systematic questionnaire-based analysis to NDE testimonials from major research databases, extracting structured data about:
- NDE phenomenology (out-of-body experiences, tunnels, light encounters, life reviews)
- Entities encountered and messages received
- Life review content and perspective
- Aftereffects and spiritual transformations
- Greyson scale elements and estimated scores
- Veridical perception claims

The structured data enables statistical analysis of NDE patterns, entity encounters, transformative effects, and correlations with healing outcomes.

## Data Sources

| Source | Cases | Status |
|--------|-------|--------|
| [NDERF](https://nderf.org) | ~3,500 | ✅ Complete |
| [IANDS](https://iands.org) | ~600 | ✅ Complete |

## Project Structure

```
nde/
├── extract.py                 # Structured data extraction script
├── models/
│   └── questionnaire.py       # NDE questionnaire Pydantic schema
├── registries/                # Dataset registry YAML files
│   ├── nderf.yaml
│   └── iands.yaml
├── structured/                # Structured analysis output
├── notebooks/                 # Analysis notebooks
│   ├── nde_statistical_analysis.ipynb
│   ├── volunteer_soul_profile.ipynb
│   ├── volunteer_discriminant_analysis.ipynb
│   ├── threefold_path_validation.ipynb
│   ├── light_being_analysis.ipynb
│   ├── ohkado_pattern_analysis.ipynb
│   └── conceptual_framework_deep_dive.ipynb
├── reports/                   # Generated reports
│   ├── nderf_healing_report.md
│   ├── nderf_healing_report_v2.md
│   ├── iands_healing_report.md
│   └── iands_healing_report_v2.md
└── scripts/                   # Utility scripts
    └── filter_healing_cases.py
```

## Questionnaire Schema

The NDE questionnaire extracts structured data across multiple domains:

- **Out-of-Body Experience**: Vantage point, observations, veridical elements
- **Passage/Tunnel**: Type, movement sensation, destination
- **Light Encounter**: Characteristics, being identification, communication
- **Life Review**: Presence, perspective, emotional content
- **Entity Encounters**: Types, relationships, messages received
- **Knowledge/Revelation**: Cosmic knowledge, future visions, purpose
- **Return/Decision**: Choice vs. sent back, reasons, reluctance
- **Aftereffects**: Psychological changes, spiritual development, abilities
- **Mission/Purpose**: Sense of purpose, specific tasks, timeline

## Usage

### Running Extraction

From the project directory, run the extraction script:

```bash
cd projects/nde
python extract.py --datasets nderf iands --max-concurrency 4 --log-level INFO
```

Common options:
- `--datasets nderf iands` — select which datasets to process
- `--limit 25` — process only first 25 cases for testing
- `--dry-run` — list files without calling Azure OpenAI
- `--overwrite` — regenerate existing extractions

### Running Analysis

Open Jupyter notebooks in the `notebooks/` directory:

```bash
cd notebooks
jupyter notebook nde_statistical_analysis.ipynb
```

### Using Registries

The project uses YAML registry files to define which cases to analyze:

```python
from shared.registry import load_registry
from pathlib import Path

registry = load_registry(Path("registries/nderf.yaml"))
files = registry.resolve_paths(Path("../../data"))
```

## Key Findings

See the reports in `reports/` for detailed analysis results, including:
- Healing case identification and patterns
- Statistical analysis of NDE phenomenology
- Volunteer soul profile discriminant analysis

## Related

- [Framework Documentation](../../README.md) - How to set up new projects  
- [Shared Core Library](../../shared/) - Common scrapers and analysis utilities
- [Remission Project](../remission/) - Spontaneous remission analysis
- [Data Repository](../../data/) - Unified data storage
- [Literary Compilation](https://github.com/marconian/literary-compilation) - Theoretical framework collaboration
