# Spontaneous Remission Data Analysis

Python toolkit for collecting, structuring, and analyzing spontaneous remission case data using LLM-powered questionnaire analysis.

## Project Overview

This project applies the same methodology as [nde-data-analysis](https://github.com/marconian/nde-data-analysis) to the domain of spontaneous remission research. The goal is to create a structured database that enables statistical analysis of the relationship between psycho-spiritual transformation and physical healing.

### Core Hypothesis

The **Somatic Influx** hypothesis: Profound spiritual transformation acts as a consistent causal precursor to spontaneous remission. The physical body is the "soul in ultimates" — disease corresponds to spiritual states, and healing follows spiritual resolution.

### Correspondential Framework

This project operates from a Swedenborgian understanding of illness and healing. Key principles:

| Principle | Description |
|-----------|-------------|
| **Body = Soul in Ultimates** | The physical body is the outermost expression of spiritual state, not disconnected from it |
| **Will is Receptive** | The will does not *produce* falsities—it *receives* and accepts them from the spiritual environment |
| **Vulnerability Model** | Illness represents vulnerability to falsity, not direct causation by soul deficiency |
| **True Healing ≠ Physical Survival** | True healing is reception of spiritual life; physical outcome is secondary |
| **Death is Not Evil** | The dead body represents what the soul *laid off*—falsities and external states, not the soul itself |

**Key Finding**: 85.5% of cases with clear temporal ordering showed spiritual transformation *preceding* physical remission (p < 0.000001). The transformation IS the healing; physical remission is evidence, not the goal.

📖 **Full Thesis**: [The Somatic Influx - A Correspondential Theory of Illness and Healing](docs/thesis/The%20Somatic%20Influx%20-%20A%20Correspondential%20Theory%20of%20Illness%20and%20Healing.md)  
📄 **Framework Summary**: [Correspondential Framework for Illness and Healing](docs/Correspondential%20Framework%20for%20Illness%20and%20Healing.md)

### Data Sources (Planned)

| Source | Type | Priority |
|--------|------|----------|
| Radical Remission Project | Patient testimonials | High |
| IONS Spontaneous Remission Database | Medical case reports | High |
| Lourdes Medical Bureau | Verified miraculous healings | High |
| NDERF (healing subset) | NDE-linked remissions | Medium |
| PubMed Case Reports | Medical literature | Medium |
| HealthTalk.org (DIPEx) | Patient narratives | Low-Medium |

## Project Structure

```
remission-analysis/
├── data/                    # Raw scraped data (JSON per case)
│   ├── radicalremission/    # Radical Remission Project cases
│   ├── ions/                # IONS database cases
│   ├── lourdes/             # Lourdes Medical Bureau cases
│   └── pubmed/              # Medical case reports
├── output/
│   └── analysis/            # LLM-analyzed cases
├── models/
│   └── questionnaire.py     # Pydantic schema for structured analysis
├── docs/                    # Research documents & reports
│   └── reports/             # Generated analysis reports
├── secrets/                 # Azure OpenAI credentials (gitignored)
├── tests/                   # Unit tests
└── scripts/                 # Utility scripts
```

## Workflow

### 1. Data Collection (Scraping)

```powershell
# TBD: Source-specific scrapers
python radicalremission_scraper.py
python pubmed_scraper.py
```

### 2. Structured Analysis

```powershell
# Analyze cases using Azure OpenAI with structured questionnaire
python analyze_cases.py --max-concurrency 4 --log-level INFO
```

Key flags:
- `--datasets radicalremission ions` — select specific datasets
- `--limit 25` — process a sample for validation
- `--dry-run` — list files without calling Azure
- `--overwrite` — regenerate existing analyses

### 3. Statistical Analysis

```powershell
# TBD: Analysis notebooks and scripts
python correspondence_analysis.py
python factor_analysis.py
```

## Azure OpenAI Setup

Create `secrets/azure_openai.env`:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-05-01-preview
```

## Questionnaire Schema

The structured questionnaire captures:

### Medical Metadata
- Diagnosis (ICD-10, histology, stage)
- Treatment history (conventional, alternative)
- Prognosis given
- Verification tier (1-4)

### Remission Event
- Remission type (complete, partial)
- Time to remission
- Verification method
- Speed of remission

### Psycho-Spiritual Factors (9 Factors + Extensions)
1. Dietary change
2. Taking control of health
3. Following intuition
4. Supplements/herbs
5. Releasing suppressed emotions
6. Increasing positive emotions
7. Embracing social support
8. Deepening spiritual connection
9. Having strong reasons for living

### Anomalous Experience (NDE/STE)
- Experience type
- Greyson score (estimated)
- Identity shift
- Veridical perception

### Existential Shift Markers
- Authenticity shift
- Fear-to-love shift
- Surrender event

## Validation Scoring

Cases are assigned a validation score (0-100) based on:

| Tier | Classification | Criteria |
|------|----------------|----------|
| 1 | Medically Verified | Biopsy + scans + doctor names |
| 2 | Clinically Supported | Detailed medical terminology + confirmation |
| 3 | Self-Reported (Detailed) | Diagnosis + outcome, lacking medical specifics |
| 4 | Anecdotal | Vague descriptions, hearsay |

## Research Questions

This database enables testing of:

1. **Causal Sequence**: Does spiritual transformation consistently precede remission?
2. **Factor Analysis**: Which of the 9 factors (or combinations) predict complete remission?
3. **Correspondence Testing**: Do specific spiritual states map to specific conditions?
4. **Placebo Transcendence**: Do remission rates exceed placebo baselines?
5. **Time-to-Remission**: Does transformation depth correlate with healing speed?

## Key Analysis Findings

Analysis of 569 cases (219 testimonial, 350 clinical) reveals:

### Transformation Precedes Remission

| Metric | Finding |
|--------|---------|
| Clear temporal ordering cases | 117 |
| Transformation preceded remission | **85.5%** |
| Statistical significance | p < 0.000001 |

### Surrender as Opening to Influx

| Metric | With Surrender | Without | Difference |
|--------|----------------|---------|------------|
| Transformation rate | 100.0% | 90.1% | +9.9% |
| Spiritual connection | 98.3% | 67.1% | **+31.2%** |

### Fear-to-Love Shift

| Metric | Finding |
|--------|---------|
| Cases with shift | 106/219 (48.4%) |
| Spiritual connection rate | 94.3% |
| Transformation narrative | 100.0% |

### True Healing Indicators

| Indicator | Prevalence |
|-----------|------------|
| Has transformation narrative | 92.7% |
| Spiritual connection | 75.3% |
| Fear-to-love shift | 48.4% |
| Surrender event | 26.5% |
| **At least one spiritual indicator** | **78.1%** |

**Interpretation**: The will's opening (surrender, fear→love) precedes and enables healing. Physical remission follows spiritual transformation as consequence, not cause.

## Related Projects

- [nde-data-analysis](https://github.com/marconian/nde-data-analysis) — Parent project methodology
- [literary-compilation](https://github.com/marconian/literary-compilation) — Theoretical framework

## License

MIT License
