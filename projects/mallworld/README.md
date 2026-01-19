# Mall World Analysis Project

Structured phenomenological analysis of the "Mall World" shared dream topography through the lens of Swedenborgian correspondences.

## Research Overview

This project applies systematic questionnaire-based analysis to dream reports from r/TheMallWorld, extracting structured data about:

- **Location Types**: Mall, Airport, Hotel, Train Station, School, Library, Beach, Basement
- **Architectural Features**: Elevators, escalators, levels, tunnels, parking garages
- **Sensory Qualities**: Lighting, colors, textures, hyper-reality
- **Emotional Tone**: Anxiety, peace, dread, confusion, familiarity
- **Spiritual Correspondences**: Mapping phenomena to Swedenborgian ontology

### Theoretical Framework

The analysis interprets dream topography through Swedenborg's **Science of Correspondences**, treating the Mall World as perception of the **World of Spirits**—the intermediate spiritual state. Key correspondences include:

| Dream Location | Swedenborgian Correspondence |
|---------------|------------------------------|
| The Mall | Marketplace; exchange of affections and knowledges |
| The Airport | Elevation of understanding; intellectual ascent |
| The Red Hotel | Babylon; love of self; dominion |
| Dirty Bathrooms | Excrementitious hells; exposure of internal state |
| The University | Gymnasium; place of instruction |
| The Ocean/Tsunami | Boundary of the natural; inundation by falsities |
| The Basement | Lower Earth; vastation; corporeal memory |

## Data Sources

| Source | Cases | Status |
|--------|-------|--------|
| [r/TheMallWorld](https://reddit.com/r/TheMallWorld) | TBD | 🔄 Scraping needed |

## Project Structure

```
mallworld/
├── extract.py                 # Structured data extraction script
├── models/
│   └── questionnaire.py       # Mall World questionnaire Pydantic schema
├── registries/                # Dataset registry YAML files
├── structured/                # Structured analysis output
├── notebooks/                 # Analysis notebooks
├── reports/                   # Generated reports
└── scripts/                   # Utility scripts
```

## Questionnaire Schema

The questionnaire extracts structured data including:

### Location Categories
- **Primary Location**: Mall, Airport, Hotel, Train Station, School, Beach, etc.
- **Sub-locations**: Food court, bathroom, elevator, escalator, parking garage
- **Connectivity**: How locations connect (tunnels, trains, walking)

### Phenomenological Features
- **Architectural Qualities**: Circular, multi-level, infinite, labyrinthine
- **Sensory Experience**: Lighting (dim/bright), colors, textures
- **Reality Quality**: Hyper-real, dreamlike, solid, shifting

### Emotional/Spiritual Content
- **Emotional Tone**: Anxiety, peace, dread, confusion, familiarity
- **Transaction Attempts**: Buying, eating, finding (success/failure)
- **Movement**: Vertical (elevator/escalator), horizontal (walking/transit)
- **Beings Encountered**: People, entities, guides, threatening figures

### Swedenborgian Mapping
- **Correspondence Category**: Which spiritual state the experience maps to
- **Vastation Indicators**: Signs of spiritual sorting/purging
- **Proprium Markers**: Self-love vs. spiritual orientation indicators

## Usage

### Running Extraction

From the project directory, run the extraction script:

```bash
cd projects/mallworld
python extract.py --datasets [dataset] --max-concurrency 4 --log-level INFO
```

Common options:
- `--datasets mallworld` — select which datasets to process
- `--limit 25` — process only first 25 cases for testing
- `--dry-run` — list files without calling Azure OpenAI
- `--overwrite` — regenerate existing extractions

### Running Analysis

Open Jupyter notebooks in the `notebooks/` directory:

```bash
cd notebooks
jupyter notebook
```

## Key Research Questions

1. **Topographical Consistency**: How consistent are location descriptions across dreamers?
2. **Correspondence Validation**: Do dream features map consistently to Swedenborgian correspondences?
3. **Emotional Clustering**: Do specific locations correlate with specific emotional states?
4. **Vertical Movement**: What patterns emerge in elevator/escalator experiences?
5. **Transaction Failure**: How often do commerce/eating attempts fail, and what does this signify?

## Related

- [Framework Documentation](../../README.md) - How to set up new projects
- [Shared Core Library](../../shared/) - Common scrapers and analysis utilities
- [Data Repository](../../data/) - Unified data storage
- [Literary Compilation](https://github.com/marconian/literary-compilation) - Theoretical framework (Swedenborgian knowledge graph)
- [Theoretical Analysis](../../docs/external/The%20Spiritual%20Topography%20of%20the%20Late%20Modern%20Soul.md) - Full correspondential analysis document
