# Ontological Versus Cultural Structure in MallWorld: Robustness Tests for Spatial–Affective Associations

## Abstract

**Background**: MallWorld reports exhibit recurrent spatial motifs (e.g., malls, transit corridors, vertical transitions) alongside marked affective atmospheres (e.g., ominous, neutral, celebratory). A central question is whether observed structure reflects a shared latent “world” regularity (or other cross-person constraint) versus more prosaic explanations such as author-specific style, short-lived cultural fads, or prompt-like imitation.

**Methods**: We analyzed the MallWorld structured extraction outputs using categorical association tests (χ² tests) and effect sizes (Cramér’s V). We then performed a robustness battery intended to directly challenge “cultural artifact” explanations: (1) time-split stability (recent vs. earlier), (2) author-holdout stability (repeated splits by author), (3) sensitivity to prolific authors (dropping top-k contributors), and (4) within-author permutation nulls (shuffling outcomes within author to control author base rates and stylistic priors). Extractions were produced via the project’s structured pipeline; categories coded as `not_mentioned` were excluded per test.

**Results**: Two core associations were examined: (i) location type × atmosphere and (ii) vertical position × atmosphere. In the full in-notebook sample, both were highly non-independent (location type × atmosphere: χ² = 1737.99, df = 621, p = 2.13e-106, V = 0.212, n = 4,306; vertical position × atmosphere: χ² = 203.50, df = 45, p = 4.97e-22, V = 0.144, n = 1,955). These effects were stable across time splits (observed V spread not larger than permuted expectation; p ≈ 0.54–0.56) and across author-holdout splits (train/test V means nearly identical over 300 splits). Within-author permutation nulls were far smaller than observed effects (location type × atmosphere: observed V = 0.170 vs null mean V = 0.059; p = 0.000999; n = 3,992, authors = 930; vertical position × atmosphere: observed V = 0.136 vs null mean V = 0.060; p = 0.000999; n = 2,165, authors = 609).

**Conclusions**: The spatial–affective association signal is not plausibly explained as a pure author-style artifact or a purely time-local cultural fad in this dataset slice. The results support the existence of cross-person regularities linking spatial descriptors (location type; vertical position) to affective atmosphere, warranting deeper model comparison work (e.g., generative cultural-schema models vs. ontological/correspondential hypotheses) and expansion to additional association families (entities, boundaries, interactions).

**Keywords**: MallWorld, dream reports, categorical association, Cramér’s V, robustness, author controls, permutation test, time stability

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| Raw MallWorld corpus | r/themallworld posts (scraped into project `data/mallworld/`) | Local repository data |
| Structured extraction outputs | `projects/mallworld/structured/*.json` | Local repository data |
| Analysis notebook | `projects/mallworld/notebooks/11_ontological_vs_cultural_tests.ipynb` | Local repository |
| Extraction schema | `projects/mallworld/models/questionnaire.py` | Local repository |

---

## 1. Introduction

### 1.1 Background
A recurring difficulty in analyzing collective dream corpora is separating genuine cross-person structure from confounding sources of apparent regularity: shared media templates, subreddit conventions, imitation cascades, and author-level stylistic priors. In MallWorld specifically, spatial language (e.g., “mall”, “hotel”, “hallway”, “escalator”, “stairs”, “underground”) appears intertwined with affective atmospheres (e.g., threatening/ominous vs. calm/neutral). If such couplings are stable across time and generalize across authors, they become less compatible with narrow cultural-fad or “few influential posters” explanations.

### 1.2 Theoretical Framework
This document treats the Swedenborgian correspondential framing as a hypothesis generator rather than an authority claim. The immediate analytic objective is empirical: identify which patterns are robust to strong falsification-style controls. The interpretive question (cultural schema vs. ontological/correspondential structure) is deferred until after robustness and negative control checks.

### 1.3 Aims
1. Test whether location type and atmosphere are statistically associated at non-trivial effect sizes.
2. Test whether vertical position and atmosphere are statistically associated at non-trivial effect sizes.
3. Evaluate whether these effects are stable across time (recent vs. earlier).
4. Evaluate whether these effects generalize across authors and are not driven by a small set of prolific contributors.
5. Evaluate whether the effects survive within-author permutation nulls (controlling for author base rates).

---

## 2. Methods

### 2.1 Data Sources
The dataset comprises MallWorld posts stored locally under `data/mallworld/` with corresponding structured extraction outputs under `projects/mallworld/structured/`. A dream-level metadata table was constructed by joining each structured record to its source JSON, enabling author-based analyses.

Dream-level coverage (in the executed notebook state):
- Dreams: 1,926
- Unique authors (non-null): 1,292
- Dreams with known author: 100.0%
- Dreams with known gender: 1.6%
- Dreams with known age range: 8.6%

### 2.2 Coding Scheme / Variables
Two primary cross-tabs were tested:
- **Location type × Atmosphere**
  - Location type: categorical location label (e.g., mall, hotel, hallway; full enum set in schema)
  - Atmosphere: categorical affective setting descriptor (e.g., ominous, neutral, celebratory; extracted per location)
- **Vertical position × Atmosphere**
  - Vertical position: categorical vertical descriptor (e.g., underground, ground, elevated; extracted per location)
  - Atmosphere: as above

Per project convention, responses coded as `not_mentioned` were treated as missing for that variable and excluded from the corresponding test.

### 2.3 Statistical Analysis
- **Association testing**: χ² test of independence on contingency tables.
- **Effect size**: Cramér’s V with the standard definition $V=\sqrt{\chi^2/(n(k-1))}$ where $k=\min(r,c)$.
- **Robustness tests**:
  1. **Time-split stability**: Split records into “recent” vs “earlier” strata (as defined in-notebook) and measure whether the between-stratum difference in V exceeds a permutation null.
  2. **Author-holdout stability**: Repeated random splits by author, computing V in train vs test halves.
  3. **Prolific-author sensitivity**: Recompute V after dropping the top-k authors by contribution.
  4. **Within-author permutation null**: Shuffle the dependent variable within author (preserving each author’s base rates) and compare observed V to the within-author null distribution.

---

## 3. Results

### 3.1 Location Type × Atmosphere

**Full-sample association** (in-notebook filtered data):

| x | y | n | r×c | χ² | df | p-value | Cramér’s V |
|---|---|---:|---:|---:|---:|---:|---:|
| location_type | atmosphere | 4,306 | 70×10 | 1,737.99 | 621 | 2.13e-106 | 0.212 |

**Time-split stability**:

| Stratum (recent?) | n | Cramér’s V | Observed V spread | Permutation p (spread) |
|---|---:|---:|---:|---:|
| False | 2,086 | 0.1690 | 0.00883 | 0.5422 |
| True | 1,906 | 0.1779 | 0.00883 | 0.5422 |

**Author-holdout stability** (300 author splits):
- V_train mean ± sd: 0.1724 ± 0.0095
- V_test mean ± sd: 0.1714 ± 0.0093
- Median absolute |V_train − V_test|: 0.0126 (90th percentile: 0.0290)

**Sensitivity to prolific authors**:

| Drop top-k authors | n | n_authors | Cramér’s V |
|---:|---:|---:|---:|
| 0 | 3,992 | 930 | 0.1704 |
| 1 | 3,924 | 929 | 0.1707 |
| 5 | 3,716 | 925 | 0.1709 |
| 10 | 3,550 | 920 | 0.1639 |
| 25 | 3,234 | 905 | 0.1590 |
| 50 | 2,859 | 880 | 0.1517 |
| 100 | 2,349 | 830 | 0.1424 |

**Within-author permutation null**:

| n | n_authors | Observed V | Null mean V | Null 90th pct | Null max | p_perm (within-author) |
|---:|---:|---:|---:|---:|---:|---:|
| 3,992 | 930 | 0.1704 | 0.0593 | 0.0678 | 0.0806 | 0.000999 |

**Critical Finding**: Location type and atmosphere are strongly associated (V ≈ 0.17–0.21 depending on analysis slice), and this association remains after stringent controls against (i) time-local drift, (ii) author overfitting, and (iii) author base-rate confounding.

### 3.2 Vertical Position × Atmosphere

**Full-sample association** (in-notebook filtered data):

| x | y | n | r×c | χ² | df | p-value | Cramér’s V |
|---|---|---:|---:|---:|---:|---:|---:|
| vertical_position | atmosphere | 1,955 | 6×10 | 203.50 | 45 | 4.97e-22 | 0.144 |

**Time-split stability**:

| Stratum (recent?) | n | Cramér’s V | Observed V spread | Permutation p (spread) |
|---|---:|---:|---:|---:|
| False | 1,149 | 0.1304 | 0.01367 | 0.5567 |
| True | 1,016 | 0.1441 | 0.01367 | 0.5567 |

**Author-holdout stability** (300 author splits):
- V_train mean ± sd: 0.1388 ± 0.0143
- V_test mean ± sd: 0.1364 ± 0.0137
- Median absolute |V_train − V_test|: 0.0175 (90th percentile: 0.0459)

**Sensitivity to prolific authors**:

| Drop top-k authors | n | n_authors | Cramér’s V |
|---:|---:|---:|---:|
| 0 | 2,165 | 609 | 0.1360 |
| 1 | 2,108 | 608 | 0.1326 |
| 5 | 1,953 | 604 | 0.1298 |
| 10 | 1,836 | 599 | 0.1307 |
| 25 | 1,633 | 584 | 0.1251 |
| 50 | 1,399 | 559 | 0.1279 |
| 100 | 1,068 | 509 | 0.1214 |

**Within-author permutation null**:

| n | n_authors | Observed V | Null mean V | Null 90th pct | Null max | p_perm (within-author) |
|---:|---:|---:|---:|---:|---:|---:|
| 2,165 | 609 | 0.1360 | 0.0600 | 0.0730 | 0.0934 | 0.000999 |

**Critical Finding**: Vertical position is meaningfully associated with atmosphere (V ≈ 0.13–0.14), and the signal persists under time-split, author-holdout, prolific-author drop, and within-author permutation controls.

---

## 4. Discussion

### 4.1 Summary of Findings
- Location type and atmosphere show a robust association across multiple stress tests.
- Vertical position and atmosphere show a robust association across multiple stress tests.
- Time-split analyses do not indicate a meaningful drift in effect size between recent and earlier strata (spread p ≈ 0.54–0.56).
- Author-holdout analyses show near-identical effect sizes in held-out author sets, inconsistent with “a few authors generate the structure.”
- Within-author nulls are substantially smaller than the observed effects, inconsistent with a pure author base-rate explanation.

### 4.2 Interpretation
These results elevate the spatial–affective couplings from “statistically significant” to “robust under adversarial confounds.” However, robustness alone does not uniquely select among explanations. Multiple generative accounts can produce stable cross-person structure:
- cultural schemas that genuinely constrain expression across many authors,
- shared constraints from the reporting medium (common narrative tropes),
- shared phenomenology (including, but not limited to, correspondential/ontological interpretations).

What is now empirically disfavored is a narrow explanation in which the observed associations are primarily an artifact of (i) a small number of prolific authors, or (ii) time-local meme drift, or (iii) author-specific base rates.

### 4.3 Implications
- Methodological: author-controlled permutation tests appear to be a high-leverage validity check for collective narrative corpora.
- Substantive: spatial motifs in MallWorld appear systematically linked to affective atmospheres, supporting the premise that the corpus contains structured regularities worth modeling.

### 4.4 Limitations
1. **Extraction validity**: structured labels depend on LLM extraction; misclassification and category drift remain plausible.
2. **Non-dream or atypical posts**: some items (e.g., AI visualization posts) may enter the corpus; filtering strategy affects estimates.
3. **Sparse demographics**: gender and age metadata are too sparse for strong demographic stratification in this run.
4. **Unit-of-analysis ambiguity**: tests are computed on location instances, not dreams; multi-location dreams may contribute multiple rows.

### 4.5 Future Directions
1. Extend the robustness battery to entity variables (e.g., entity type × demeanor; authority nature × interaction outcomes).
2. Add within-dream negative controls (e.g., shuffling atmosphere labels within each dream) to isolate within-dream narrative coherence effects.
3. Explicitly compare alternative generative models (cultural-schema baseline vs. structured “world” baseline) using held-out predictive performance.

---

## Appendix A: Statistical Summary

| Test | Variable Pair | χ² | df | p-value | Cramér’s V | n |
|------|---------------|---:|---:|---:|---:|---:|
| Independence | location_type × atmosphere | 1,737.99 | 621 | 2.13e-106 | 0.212 | 4,306 |
| Independence | vertical_position × atmosphere | 203.50 | 45 | 4.97e-22 | 0.144 | 1,955 |

## Appendix B: Robustness Summary

| Variable Pair | Robustness Test | Key Result |
|---------------|-----------------|------------|
| location_type × atmosphere | Time split | V: 0.169 vs 0.178; spread p = 0.542 |
| location_type × atmosphere | Author holdout | Train V 0.172 ± 0.009; Test V 0.171 ± 0.009 |
| location_type × atmosphere | Drop top-k authors | V declines gradually (0.170 → 0.142 at k=100), does not vanish |
| location_type × atmosphere | Within-author permutation | Observed V 0.170; null mean 0.059; p = 0.000999 |
| vertical_position × atmosphere | Time split | V: 0.130 vs 0.144; spread p = 0.557 |
| vertical_position × atmosphere | Author holdout | Train V 0.139 ± 0.014; Test V 0.136 ± 0.014 |
| vertical_position × atmosphere | Drop top-k authors | V declines modestly (0.136 → 0.121 at k=100) |
| vertical_position × atmosphere | Within-author permutation | Observed V 0.136; null mean 0.060; p = 0.000999 |
