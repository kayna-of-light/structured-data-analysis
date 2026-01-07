# Repository Reorganization Plan

## Executive Summary

Transform `remission-analysis` and `nde-analysis` into a unified workspace with:
1. A **shared core library** for common functionality
2. A **unified data repository** for externally scraped data
3. **Subset registers** instead of duplicate datasets
4. Domain-specific **analysis modules** that import from core

This eliminates code duplication, establishes a single source of truth for scraped data, and enables consistent tooling across analysis domains.

---

## Current State Analysis

### nde-analysis/
```
nde-analysis/
├── nderf_scraper.py          # 869 lines - duplicates http_get, slugify, etc.
├── iands_scraper.py          # 287 lines - duplicates http_get, slugify, etc.
├── analyze_experiences.py    # 379 lines - Azure OpenAI analysis
├── models/
│   └── questionnaire.py      # 1141 lines - NDE-specific Pydantic models
├── data/
│   ├── nderf/                # ~3500 files - FULL NDERF dataset
│   └── iands/                # ~600 files - FULL IANDS dataset
└── output/
    └── analysis/             # Analysis results
```

**Issues:**
- `nderf_scraper.py` and `iands_scraper.py` have ~100 lines of duplicated utility code
- No base scraper class - each scraper reinvents the wheel
- Data is fully scraped into local folders

### remission-analysis/
```
remission-analysis/
├── scrapers/
│   ├── base.py               # 178 lines - BaseScraper, ScrapedCase, utilities
│   ├── pmc_scraper.py
│   ├── radical_remission_scraper.py
│   ├── lourdes_scraper.py
│   └── ions_scraper.py
├── analyze_cases.py          # 438 lines - Azure OpenAI analysis
├── models/
│   └── questionnaire.py      # 2055 lines - Remission-specific Pydantic models
├── data/
│   ├── nderf/                # ~50 files - SUBSET of nde-analysis/data/nderf
│   ├── iands/                # ~25 files - SUBSET of nde-analysis/data/iands
│   ├── pmc_cases/            # PMC case reports
│   └── rrp_cases/            # Radical Remission Project cases
└── output/
    └── analysis/             # Analysis results
```

**Strengths:**
- `scrapers/base.py` provides good abstraction
- `ScrapedCase` dataclass provides consistent schema

**Issues:**
- Duplicates NDERF/IANDS data files (should reference the authoritative copy)
- Analysis script nearly identical to nde-analysis version
- Models could share common base enums

---

## Proposed Architecture

### New Directory Structure

```
workspace-root/
├── shared/                           # SHARED CORE LIBRARY
│   ├── __init__.py
│   ├── scrapers/
│   │   ├── __init__.py
│   │   ├── base.py                  # BaseScraper, ScrapedCase, http utilities
│   │   ├── nderf_scraper.py         # NDERF scraper (from nde-analysis)
│   │   ├── iands_scraper.py         # IANDS scraper (from nde-analysis)
│   │   ├── pmc_scraper.py           # PubMed Central (from remission-analysis)
│   │   ├── radical_remission_scraper.py  # RadicalRemission.com
│   │   ├── lourdes_scraper.py       # Lourdes Medical Bureau
│   │   └── ions_scraper.py          # IONS database
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── azure_client.py          # Azure OpenAI client wrapper
│   │   └── base_analyzer.py         # BaseAnalyzer class
│   ├── registry/
│   │   ├── __init__.py
│   │   └── loader.py                # Registry file loader and resolver
│   └── models/
│       ├── __init__.py
│       └── common.py                # Shared enums (MentionResponse, etc.)
│
├── data/                            # UNIFIED DATA REPOSITORY
│   ├── nderf/                       # ~3500 files - authoritative NDERF data
│   ├── iands/                       # ~600 files - authoritative IANDS data
│   ├── pmc/                         # PMC case reports
│   ├── radical_remission/           # Radical Remission Project
│   ├── lourdes/                     # Lourdes Medical Bureau
│   └── ions/                        # IONS Spontaneous Remission Project
│
├── nde-analysis/                    # NDE ANALYSIS MODULE
│   ├── analyze_experiences.py       # Domain-specific analysis
│   ├── models/
│   │   └── questionnaire.py         # NDE questionnaire (imports shared)
│   ├── registries/                  # DATASET REGISTRIES
│   │   ├── nderf.yaml               # Full NDERF dataset reference
│   │   └── iands.yaml               # Full IANDS dataset reference
│   ├── structured/                  # Structured data extraction output
│   └── notebooks/
│
└── remission-analysis/              # REMISSION ANALYSIS MODULE
    ├── analyze_cases.py             # Domain-specific analysis
    ├── models/
    │   └── questionnaire.py         # Remission questionnaire (imports shared)
    ├── registries/                  # DATASET REGISTRIES
    │   ├── nderf_healing.yaml       # Subset of NDERF for healing analysis
    │   ├── iands_healing.yaml       # Subset of IANDS for healing analysis
    │   ├── pmc.yaml                 # Full PMC dataset reference
    │   ├── radical_remission.yaml   # Full RRP dataset reference
    │   ├── lourdes.yaml             # Full Lourdes dataset reference
    │   └── ions.yaml                # Full IONS dataset reference
    ├── structured/                  # Structured data extraction output
    └── notebooks/
```

---

## Implementation Plan

### Phase 1: Create Shared Core Library

#### 1.1 Create `shared/` directory structure
```
mkdir shared
mkdir shared/scrapers
mkdir shared/analysis
mkdir shared/models
```

#### 1.2 Migrate scraper base utilities
**Source:** `remission-analysis/scrapers/base.py`
**Target:** `shared/scrapers/base.py`

The existing `base.py` is well-designed. Enhancements:
- Add type hints throughout
- Add docstrings for Sphinx documentation
- Export via `__init__.py`

#### 1.3 Migrate NDERF/IANDS scrapers
**Sources:**
- `nde-analysis/nderf_scraper.py`
- `nde-analysis/iands_scraper.py`

**Target:** `shared/scrapers/`

Changes required:
- Remove duplicated utility functions (use base.py)
- Convert to class-based scrapers extending `BaseScraper`
- Update imports and paths

#### 1.4 Create shared Azure OpenAI client
**Extract from:** `analyze_experiences.py` and `analyze_cases.py`
**Target:** `shared/analysis/azure_client.py`

Both analyzers have nearly identical code for:
- Loading Azure credentials from env files
- Building OpenAI client
- Handling rate limits and retries
- Structured output parsing

Create a reusable `AzureOpenAIAnalyzer` base class.

#### 1.5 Create shared model enums
**Target:** `shared/models/common.py`

Both questionnaire files define identical enums:
- `MentionResponse`
- `QuestionnaireBaseModel`

Extract these to shared module.

---

### Phase 2: Consolidate Data Repository

#### 2.1 Create unified `data/` directory
The authoritative data location will be:
```
workspace-root/data/
```

#### 2.2 Move data from nde-analysis
```bash
# Move authoritative NDERF data
mv nde-analysis/data/nderf data/nderf

# Move authoritative IANDS data  
mv nde-analysis/data/iands data/iands
```

#### 2.3 Remove duplicate data from remission-analysis
```bash
# Remove duplicate NDERF subset
rm -rf remission-analysis/data/nderf

# Remove duplicate IANDS subset
rm -rf remission-analysis/data/iands
```

#### 2.4 Move remission-specific data
```bash
# Move PMC data to shared
mv remission-analysis/data/pmc_cases data/pmc_cases

# Move other remission data
mv remission-analysis/data/rrp_cases data/rrp_cases
```

---

### Phase 3: Implement Dataset Registries

Dataset registries define which files from the shared data repository belong to a particular analysis context. They can reference an entire dataset OR specify individual files.

#### 3.1 Registry Schema Design

**File:** `shared/registry/loader.py`
```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from pathlib import Path
import yaml

class DatasetRegistry(BaseModel):
    """Defines a dataset or subset for analysis."""
    name: str
    description: str
    source: str  # e.g., "nderf", "iands", "pmc"
    mode: Literal["all", "subset"] = "all"
    
    # For mode="subset", list specific files
    files: Optional[List[str]] = None
    
    # Optional metadata
    selection_criteria: Optional[str] = None
    created: Optional[str] = None
    
    def resolve_paths(self, data_root: Path) -> List[Path]:
        """Convert registry to list of absolute file paths."""
        source_dir = data_root / self.source
        
        if self.mode == "all":
            # Return all JSON files in the source directory
            return sorted(source_dir.glob("*.json"))
        else:
            # Return only specified files
            return [source_dir / f for f in self.files if (source_dir / f).exists()]

def load_registry(registry_path: Path) -> DatasetRegistry:
    """Load a registry YAML file."""
    with open(registry_path) as f:
        data = yaml.safe_load(f)
    return DatasetRegistry(**data)

def load_all_registries(registries_dir: Path) -> List[DatasetRegistry]:
    """Load all registry files from a directory."""
    registries = []
    for path in registries_dir.glob("*.yaml"):
        registries.append(load_registry(path))
    return registries
```

#### 3.2 Registry File Examples

**Full Dataset Reference (mode: all)**

```yaml
# nde-analysis/registries/nderf.yaml
name: nderf_full
description: Complete NDERF dataset for NDE analysis
source: nderf
mode: all
```

```yaml
# nde-analysis/registries/iands.yaml
name: iands_full
description: Complete IANDS dataset for NDE analysis
source: iands
mode: all
```

**Subset with Specific Files (mode: subset)**

```yaml
# remission-analysis/registries/nderf_healing.yaml
name: nderf_healing
description: NDERF cases selected for healing/remission analysis
source: nderf
mode: subset
selection_criteria: >
  Cases selected based on mention of healing, remission,
  or physical recovery during or after the NDE experience.
files:
  - 00081_d-nde-35.json
  - 00409_randi-s-nde.json
  - 00638_annie-m-nde-20875.json
  - 00706_daniel-rs-nde-2364.json
  # ... (50 files total)
```

```yaml
# remission-analysis/registries/pmc.yaml
name: pmc_full
description: PubMed Central spontaneous remission case reports
source: pmc
mode: all
```

#### 3.3 Update Analysis Scripts to Use Registries

```python
from shared.registry.loader import load_all_registries, DatasetRegistry
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).parent.parent
DATA_ROOT = WORKSPACE_ROOT / "data"
REGISTRIES_DIR = Path(__file__).parent / "registries"

def collect_jobs_from_registries() -> List[AnalysisJob]:
    """Collect analysis jobs from all registry files."""
    jobs = []
    
    for registry in load_all_registries(REGISTRIES_DIR):
        source_files = registry.resolve_paths(DATA_ROOT)
        
        for path in source_files:
            jobs.append(AnalysisJob(
                dataset=registry.source,
                registry_name=registry.name,
                source_path=path,
                target_path=ANALYSIS_DIR / f"{registry.name}-{path.name}",
            ))
    
    return jobs
```

---

### Phase 4: Update Import Paths

#### 4.1 Update nde-analysis imports

**Before:**
```python
# nde-analysis/analyze_experiences.py
from models import NDEAnalysisResponse
```

**After:**
```python
# nde-analysis/analyze_experiences.py
from shared.analysis.base_analyzer import BaseAnalyzer
from shared.models.common import MentionResponse
from models import NDEAnalysisResponse
```

#### 4.2 Update remission-analysis imports

**Before:**
```python
# remission-analysis/analyze_cases.py
from models import RemissionAnalysisResponse

# remission-analysis/scrapers/pmc_scraper.py
from .base import BaseScraper, ScrapedCase, http_get
```

**After:**
```python
# remission-analysis/analyze_cases.py
from shared.analysis.base_analyzer import BaseAnalyzer
from shared.models.common import MentionResponse
from models import RemissionAnalysisResponse

# remission-analysis/scrapers/pmc_scraper.py
from shared.scrapers.base import BaseScraper, ScrapedCase, http_get
```

#### 4.3 Update Python path configuration

**Option A: pyproject.toml (recommended)**
```toml
[tool.setuptools]
packages = ["shared", "nde_analysis", "remission_analysis"]

[project]
name = "consciousness-research"
```

**Option B: VS Code workspace settings**
```json
{
    "python.analysis.extraPaths": ["${workspaceFolder}/shared"]
}
```

---

### Phase 5: Migrate ALL Scrapers to Shared Core

All scrapers move to `shared/scrapers/` and import from `base.py`.

#### 5.1 Scraper Migration Table

| Source | Target | Changes |
|--------|--------|---------|
| `nde-analysis/nderf_scraper.py` | `shared/scrapers/nderf_scraper.py` | Remove duplicate utils, use base.py |
| `nde-analysis/iands_scraper.py` | `shared/scrapers/iands_scraper.py` | Remove duplicate utils, use base.py |
| `remission-analysis/scrapers/pmc_scraper.py` | `shared/scrapers/pmc_scraper.py` | Update imports |
| `remission-analysis/scrapers/radical_remission_scraper.py` | `shared/scrapers/radical_remission_scraper.py` | Update imports |
| `remission-analysis/scrapers/lourdes_scraper.py` | `shared/scrapers/lourdes_scraper.py` | Update imports |
| `remission-analysis/scrapers/ions_scraper.py` | `shared/scrapers/ions_scraper.py` | Update imports |

#### 5.2 Scraper Invocation

Scrapers can be run from workspace root:
```bash
# Scrape NDERF data to data/nderf/
python -m shared.scrapers.nderf_scraper --output data/nderf

# Scrape PMC data to data/pmc/
python -m shared.scrapers.pmc_scraper --output data/pmc
```

#### 5.3 Shared Scraper Interface

All scrapers follow the same pattern:
```python
# shared/scrapers/example_scraper.py
from shared.scrapers.base import BaseScraper, ScrapedCase, http_get

class ExampleScraper(BaseScraper):
    source_name = "example"
    
    def scrape_all(self) -> List[ScrapedCase]:
        # Implementation
        pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("data/example"))
    args = parser.parse_args()
    
    scraper = ExampleScraper(args.output)
    cases = scraper.scrape_all()
    print(f"Scraped {len(cases)} cases")
```

---

## File Mapping Summary

| Source | Destination | Action |
|--------|-------------|--------|
| `nde-analysis/data/nderf/*` | `data/nderf/*` | Move (authoritative) |
| `nde-analysis/data/iands/*` | `data/iands/*` | Move (authoritative) |
| `remission-analysis/data/nderf/*` | DELETE | Replace with registry |
| `remission-analysis/data/iands/*` | DELETE | Replace with registry |
| `remission-analysis/data/pmc_cases/*` | `data/pmc/*` | Move |
| `remission-analysis/data/rrp_cases/*` | `data/radical_remission/*` | Move |
| `remission-analysis/scrapers/base.py` | `shared/scrapers/base.py` | Move + enhance |
| `nde-analysis/nderf_scraper.py` | `shared/scrapers/nderf_scraper.py` | Move + refactor |
| `nde-analysis/iands_scraper.py` | `shared/scrapers/iands_scraper.py` | Move + refactor |
| `remission-analysis/scrapers/pmc_scraper.py` | `shared/scrapers/pmc_scraper.py` | Move |
| `remission-analysis/scrapers/radical_remission_scraper.py` | `shared/scrapers/radical_remission_scraper.py` | Move |
| `remission-analysis/scrapers/lourdes_scraper.py` | `shared/scrapers/lourdes_scraper.py` | Move |
| `remission-analysis/scrapers/ions_scraper.py` | `shared/scrapers/ions_scraper.py` | Move |
| Common Azure client code | `shared/analysis/azure_client.py` | Extract + create |
| Common enums | `shared/models/common.py` | Extract + create |
| NEW | `shared/registry/loader.py` | Create |

---

## Registry Generation Script

To generate initial registry files from existing data:

```python
# scripts/generate_registries.py
"""Generate registry files from existing subset data."""

import yaml
from pathlib import Path
from datetime import datetime

def generate_subset_registry(
    name: str,
    description: str, 
    source: str,
    current_data_dir: Path,
    output_path: Path,
    selection_criteria: str = None
):
    """Generate a subset registry YAML from existing directory."""
    files = sorted([f.name for f in current_data_dir.glob("*.json")])
    
    registry = {
        "name": name,
        "description": description,
        "source": source,
        "mode": "subset",
        "created": datetime.now().isoformat(),
        "files": files
    }
    if selection_criteria:
        registry["selection_criteria"] = selection_criteria
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        yaml.dump(registry, f, default_flow_style=False, sort_keys=False)
    
    print(f"Generated {output_path} with {len(files)} files")

def generate_full_registry(
    name: str,
    description: str,
    source: str,
    output_path: Path
):
    """Generate a full dataset registry (mode: all)."""
    registry = {
        "name": name,
        "description": description,
        "source": source,
        "mode": "all",
        "created": datetime.now().isoformat(),
    }
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        yaml.dump(registry, f, default_flow_style=False, sort_keys=False)
    
    print(f"Generated {output_path}")

# Generate nde-analysis registries (full datasets)
generate_full_registry(
    name="nderf_full",
    description="Complete NDERF dataset for NDE analysis",
    source="nderf",
    output_path=Path("nde-analysis/registries/nderf.yaml")
)

generate_full_registry(
    name="iands_full",
    description="Complete IANDS dataset for NDE analysis",
    source="iands",
    output_path=Path("nde-analysis/registries/iands.yaml")
)

# Generate remission-analysis registries (subsets and full)
generate_subset_registry(
    name="nderf_healing",
    description="NDERF cases selected for healing/remission analysis",
    source="nderf",
    current_data_dir=Path("remission-analysis/data/nderf"),
    output_path=Path("remission-analysis/registries/nderf_healing.yaml"),
    selection_criteria="Cases with healing, remission, or recovery mentions"
)

generate_full_registry(
    name="pmc_full",
    description="PubMed Central spontaneous remission case reports",
    source="pmc",
    output_path=Path("remission-analysis/registries/pmc.yaml")
)
```

---

## Testing Strategy

### Unit Tests
1. Test register loading and path resolution
2. Test shared scraper utilities
3. Test Azure client wrapper

### Integration Tests
1. Verify analysis scripts work with register-based file selection
2. Verify scrapers write to correct data directories
3. Verify imports resolve correctly across modules

### Migration Validation
1. Compare analysis output before/after migration
2. Verify no data loss during moves
3. Verify subset registers contain exactly the files that were in the duplicate directories

---

## Rollback Plan

If issues arise during migration:

1. **Data preserved in git history** - All moves are commits, revertible
2. **Original structure documented** - This plan captures the pre-migration state
3. **Incremental migration** - Each phase can be completed independently

---

## Success Criteria

- [ ] No duplicate utility functions across scrapers
- [ ] Single authoritative location for each scraped dataset
- [ ] Subset analyses use registers, not duplicated files
- [ ] All existing analyses produce identical output
- [ ] New analysis domains can be added by creating a register + questionnaire

---

## Timeline

| Phase | Estimated Time | Dependencies |
|-------|----------------|--------------|
| Phase 1: Shared Core | 2-3 hours | None |
| Phase 2: Data Consolidation | 1 hour | Phase 1 |
| Phase 3: Subset Registers | 1-2 hours | Phase 2 |
| Phase 4: Import Updates | 1 hour | Phase 1 |
| Phase 5: Scraper Migration | 1 hour | Phase 1 |
| Testing & Validation | 1-2 hours | All phases |

**Total:** 7-11 hours

---

## Next Steps

1. Review and approve this plan
2. Create `shared/` directory structure
3. Begin Phase 1 implementation
4. Generate register files before deleting duplicate data
