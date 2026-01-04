# Remission Analysis Project

Statistical analysis of spontaneous remission cases and their relationship to psycho-spiritual transformation.

## Overview

This project investigates the hypothesis that psycho-spiritual transformation may be temporally—and perhaps causally—related to spontaneous remission. Using LLM-powered structured extraction from medical case reports and patient narratives, we analyze the relationship between spiritual transformation and physical healing.

## Key Finding

Among 138 cases with clear temporal ordering, psychological transformation preceded physical remission in **85.5%** of cases (χ² = 69.59, p < 0.001). Surrender events were associated with 100% transformation prevalence and 98.3% spiritual connection.

📖 **Full Thesis**: [Psycho-Spiritual Transformation and Spontaneous Remission](reports/Psycho-Spiritual%20Transformation%20and%20Spontaneous%20Remission.md)

## Data Sources

| Source | Type | Status |
|--------|------|--------|
| PubMed Central | Medical case reports | 🔄 In Progress |
| Radical Remission Project | Patient testimonials | 🔄 In Progress |
| NDERF/IANDS (healing subset) | NDE-linked remissions | ✅ Registry defined |

## Project Structure

```
remission/
├── extract.py                 # Structured data extraction script
├── models/
│   └── questionnaire.py       # Remission questionnaire Pydantic schema
├── registries/                # Dataset registry YAML files
│   ├── nde_analysis.yaml
│   └── remission_analysis.yaml
├── structured/                # Structured analysis output
├── notebooks/                 # Analysis notebooks
│   ├── remission_statistical_analysis.ipynb
│   └── thesis_visualizations.ipynb
├── reports/                   # Generated reports
│   └── Psycho-Spiritual Transformation and Spontaneous Remission.md
└── scripts/                   # Utility scripts
    ├── analyze_pmc_results.py
    ├── run_pmc_scrape.py
    ├── validate_remission_cases.py
    └── ... (additional utilities)
```

## Questionnaire Schema

The remission questionnaire extracts structured data including:

### Medical Ground Truth
- **Diagnosis**: Cancer type, stage, histology
- **Treatment History**: Conventional treatments received
- **Remission Classification**: Complete, partial, stable disease
- **Verification Tier**: Medical records, imaging, pathology

### Psycho-Spiritual Factors (Turner's 9 Factors)
1. Radically changing diet
2. Taking control of health
3. Following intuition
4. Using herbs/supplements
5. Releasing suppressed emotions
6. Increasing positive emotions
7. Embracing social support
8. Deepening spiritual connection
9. Having strong reasons for living

### Anomalous Experiences
- NDE/STE during illness
- Spiritual experiences
- Premonitions or visions
- Healing imagery

### Temporal Analysis
- Transformation-remission temporal ordering
- Surrender events
- Turning points

## Usage

### Running Analysis

```bash
# From workspace root
cd projects/remission
python analyze_cases.py --datasets pmc radical_remission --max-concurrency 4
```

### Using Registries

```python
from shared.registry import load_registry
from pathlib import Path

registry = load_registry(Path("registries/remission_analysis.yaml"))
files = registry.resolve_paths(Path("../../data"))
```

## Theoretical Framework

This project is situated within a post-materialist framework that treats consciousness as potentially causally efficacious in physical processes. The analysis draws on:

- **Kelly Turner's 9 Radical Remission Factors** (1,500+ cases)
- **Swedenborgian correspondential ontology** (disease-spirit correspondence)
- **Psychoneuroimmunology literature**
- **Everson & Cole Spontaneous Regression criteria** (1966)

## Related

- [Shared Core Library](../../shared/) - Common scrapers, analysis utilities
- [NDE Project](../nde/) - Near-death experience analysis
- [Data Repository](../../data/) - Unified data storage
