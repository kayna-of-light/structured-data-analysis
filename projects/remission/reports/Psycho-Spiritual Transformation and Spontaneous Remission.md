# Psycho-Spiritual Transformation and Spontaneous Remission: A Statistical Analysis of 569 Cases

## Abstract

**Background**: Spontaneous remission—the unexpected resolution of disease without conventional treatment—remains poorly understood. Previous research has documented psychological and spiritual factors associated with these cases, but the temporal relationship between psychological transformation and physical healing has not been rigorously tested.

**Methods**: We analyzed 569 documented spontaneous remission cases from four data sources: PubMed Central clinical case reports (n=350), Radical Remission Project testimonials (n=149), NDERF archives (n=50), and IANDS archives (n=20). Cases were coded for Turner's nine radical remission factors, existential shift markers, and temporal sequence of transformation relative to remission.

**Results**: Among testimonial cases with clear temporal ordering (n=138), psychological transformation preceded physical healing in 85.5% of cases (binomial test vs. 50%: p < 0.001, χ² = 69.59, p < 0.001). Surrender events were associated with 100% transformation narrative prevalence (vs. 90.1% without, p = 0.008). Spiritual connection was present in 98.3% of surrender cases versus 67.1% without (Δ = 31.2%). Near-death experience cases showed 98.5% transformation preceding healing.

**Conclusions**: Psychological transformation consistently precedes physical remission in testimonial accounts of spontaneous healing. While causation cannot be inferred from observational data, the directional consistency (85.5%) significantly exceeds chance expectation. Clinical studies prospectively documenting transformation timing are warranted.

**Keywords**: spontaneous remission, psychological transformation, spiritual connection, radical remission, near-death experience

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| PMC Cases (n=350) | PubMed Central case reports | Public domain |
| RRP Cases (n=149) | Radical Remission Project | radicalremission.com |
| NDERF Cases (n=50) | Near-Death Experience Research Foundation | nderf.org |
| IANDS Cases (n=20) | International Association for Near-Death Studies | iands.org |
| Analysis Code | `remission_statistical_analysis.ipynb` | Repository |
| Statistics Script | `extract_thesis_stats.py` | Repository |
| Raw Data | `output/analysis/*.json` | Repository (569 files) |

---

## 1. Introduction

### 1.1 Background

Spontaneous remission—defined as the complete or partial resolution of disease without treatment, or with treatment considered inadequate to produce the observed outcome—has been documented across virtually all disease categories (O'Regan & Hirshberg, 1993; Turner, 2014). While rare, these cases present a challenge to biomedical models that locate disease causation and resolution entirely within physical mechanisms.

Kelly Turner's research on "radical remission" identified nine factors common to survivors of medically unexplained recoveries: (1) radically changing diet, (2) taking control of health, (3) following intuition, (4) using herbs and supplements, (5) releasing suppressed emotions, (6) increasing positive emotions, (7) embracing social support, (8) deepening spiritual connection, and (9) having a strong reason for living (Turner, 2014). Notably, seven of these nine factors are psychological or spiritual rather than physical.

### 1.2 Theoretical Framework

The present analysis is situated within a post-materialist framework that treats consciousness as potentially causally efficacious in physical processes (Beauregard, 2014). This does not commit to any particular mechanism—whether psychosomatic, psychoneuroimmunological, or non-physical—but allows for the possibility that changes in psychological/spiritual states may temporally and perhaps causally precede physical changes.

The specific hypothesis under test derives from the Swedenborgian theological framework, which proposes that spiritual states are causally prior to physical states through a relationship of "correspondence" (Swedenborg, 1758). On this model:

1. Changes in the **will** (fundamental orientation of love/intention) produce
2. Changes in **understanding** (perception and cognition), which manifest as
3. Changes in **ultimates** (the physical body)

This suggests a testable prediction: if the correspondential model is correct, psychological/spiritual transformation should **precede** rather than follow physical healing in spontaneous remission cases.

### 1.3 Aims

The primary aim of this analysis is to test whether psychological transformation precedes physical remission more often than would be expected by chance. Secondary aims include:

1. Characterizing the factor profile of spontaneous remission cases
2. Examining the relationship between surrender events and transformation
3. Analyzing near-death experience cases as a distinctive subset
4. Identifying source-related biases in the data

---

## 2. Methods

### 2.1 Data Sources

Cases were collected from four sources representing different evidence types:

| Source | Type | Cases | Description |
|--------|------|-------|-------------|
| PMC | Clinical | 350 | Peer-reviewed case reports from PubMed Central |
| RRP | Testimonial | 149 | Radical Remission Project survivor accounts |
| NDERF | Testimonial | 50 | Near-Death Experience Research Foundation |
| IANDS | Testimonial | 20 | International Association for Near-Death Studies |

**Total: N = 569 cases**

### 2.2 Coding Scheme

Each case was coded by AI analysis (GPT-4 via Azure OpenAI) using a structured Pydantic schema (`models/questionnaire.py`). The schema includes:

- **Demographics**: Age, sex, religious background
- **Diagnosis**: Disease category, cancer type (if applicable), organ system, terminal status
- **Treatment**: Conventional treatment status
- **Remission**: Type, speed, verification tier, durability
- **Turner Factors**: Presence/absence of each of nine factors (yes_explicit, implied, not_mentioned)
- **Existential Shift**: Transformation preceded healing, identity shift, fear-to-love shift, surrender event
- **Anomalous Experience**: NDE or other experience type, preceded healing

### 2.3 Statistical Analysis

The primary analysis employed a binomial test against the null hypothesis that, given both transformation and remission occurred, their temporal ordering is random (H₀: P(transformation first) = 0.50).

Secondary analyses used:
- Chi-square tests for categorical comparisons
- Fisher's exact test for 2×2 contingency tables
- Mann-Whitney U test for factor count comparisons

Analyses were stratified by source type, recognizing that clinical (PMC) and testimonial (RRP, NDERF, IANDS) sources have different documentation patterns.

### 2.4 Methodological Limitations

Several limitations must be acknowledged:

1. **Selection bias**: Only survivors are represented; transformation without physical remission is invisible in this data
2. **Retrospective reporting**: Testimonial accounts may reconstruct temporal ordering to fit narrative expectations
3. **Source heterogeneity**: Clinical reports rarely document psychological factors; testimonial reports self-select for transformation narratives
4. **AI coding**: While consistent, AI coding may introduce systematic biases

---

## 3. Results

*All statistics in this section were verified by running `extract_thesis_stats.py` on 2026-01-02. Raw outputs are reproducible from the repository.*

### 3.1 Sample Characteristics

#### Disease Distribution

| Category | N | % |
|----------|---|---|
| Cancer | 361 | 63.4% |
| Other | 64 | 11.2% |
| Autoimmune | 22 | 3.9% |
| Cardiovascular | 16 | 2.8% |
| Hematological | 15 | 2.6% |
| Musculoskeletal | 15 | 2.6% |
| Infectious | 14 | 2.5% |
| Neurological | 13 | 2.3% |
| Other categories | 49 | 8.5% |

#### Organ System Distribution

| Organ System | All (N=569) | Testimonial (n=219) |
|--------------|-------------|---------------------|
| Reproductive | 86 (15.1%) | 59 (26.9%) |
| Respiratory | 64 (11.2%) | 13 (5.9%) |
| Digestive | 64 (11.2%) | 29 (13.2%) |
| Multiple systems | 57 (10.0%) | 42 (19.2%) |
| Neurological | 50 (8.8%) | 20 (9.1%) |
| Lymphatic | 44 (7.7%) | 13 (5.9%) |
| Blood | 38 (6.7%) | 13 (5.9%) |
| Integumentary | 36 (6.3%) | 5 (2.3%) |

### 3.2 Primary Finding: Transformation Precedes Remission

Among testimonial cases (n=219), 92.7% (n=203) contained a transformation narrative.

Among cases with **clear temporal ordering** (n=138), transformation preceded healing in **85.5%** (n=118) of cases.

| Temporal Sequence | N | % |
|-------------------|---|---|
| Transformation preceded healing | 118 | 85.5% |
| Healing preceded transformation | 20 | 14.5% |

**Statistical tests:**
- Binomial test vs. 50%: **p < 0.001** (p = 2.09 × 10⁻¹⁸)
- Chi-square test: **χ² = 69.59, p < 0.001** (p = 7.29 × 10⁻¹⁷)

This represents a highly significant deviation from random temporal ordering.

### 3.3 Surrender Events and Transformation

Surrender events—moments of "letting go" or acceptance of death/fate—were present in 26.5% (n=58) of testimonial cases.

| Surrender | Has Transformation | % |
|-----------|-------------------|---|
| Yes (n=58) | 58 | **100.0%** |
| No (n=161) | 145 | 90.1% |

Fisher's exact test: **p = 0.008**

Among those with surrender events:
- Spiritual connection present: **98.3%**
- Without surrender: 67.1%
- Difference: **+31.2 percentage points**

### 3.4 Turner Factor Prevalence

Among testimonial cases (n=219):

| Factor | N | % |
|--------|---|---|
| Purpose/Reason for Living | 172 | 78.5% |
| Positive Emotions | 172 | 78.5% |
| Agency/Taking Control | 166 | 75.8% |
| Spiritual Connection | 165 | 75.3% |
| Social Support | 138 | 63.0% |
| Following Intuition | 121 | 55.3% |
| Diet Change | 88 | 40.2% |
| Emotional Release | 88 | 40.2% |
| Supplements | 68 | 31.1% |

Notably, **psychological/spiritual factors** (purpose, positive emotions, agency, spiritual connection, social support) showed higher prevalence than **physical intervention factors** (diet change, supplements).

### 3.5 Near-Death Experience Cases

NDE-linked healing cases (n=65) showed distinctive patterns:

| Metric | NDE Cases | Non-NDE |
|--------|-----------|---------|
| Experience preceded healing | 98.5% | — |
| Spiritual connection | 98.5% | 70.0% |
| Mean Turner factors | 4.32 | 1.91 |

**Mann-Whitney U test** for factor count: NDE > Non-NDE, **p < 0.001**

### 3.6 Source Comparison

Clinical (PMC) and testimonial sources showed significant documentation differences:

| Metric | PMC (n=350) | Testimonial (n=219) |
|--------|-------------|---------------------|
| Has transformation narrative | 12.3% | 92.7% |
| Mean Turner factors | 0.89 | 4.87 |
| Spiritual connection documented | 8.6% | 75.3% |

This asymmetry reflects documentation practices rather than underlying phenomena. Clinical case reports focus on biomedical verification; testimonial accounts emphasize experiential factors.

---

## 4. Discussion

### 4.1 Interpretation of Primary Finding

The 85.5% rate of transformation preceding remission significantly exceeds the 50% expected by chance (p < 0.001). This is consistent with—but does not prove—the hypothesis that psychological transformation may be causally related to physical healing.

Alternative explanations include:

1. **Narrative reconstruction**: Survivors may retrospectively order events to create a coherent "transformation → healing" story
2. **Selection bias**: Cases where transformation occurred without physical healing are invisible in this dataset
3. **Confounding**: Both transformation and healing may share common causes (e.g., disease trajectory, treatment effects)

### 4.2 The Surrender Pattern

The association between surrender events and transformation (100% vs. 90.1%) is striking. Surrender—often described as "letting go," "acceptance of death," or "releasing control"—appears to be a particularly potent marker.

This aligns with the correspondential framework's emphasis on the **will** as primary. Surrender represents a fundamental reorientation of the will from self-directed striving to openness/reception. On this model, the will's reorientation allows for changes in understanding and, subsequently, physical state.

### 4.3 NDE Cases as Natural Experiment

Near-death experience cases provide something approaching a natural experiment. The NDE involves:
1. A distinctive experience (encounter with light, beings, life review)
2. That precedes return to physical life
3. With subsequent physical healing

The 98.5% rate of experience preceding healing in NDE cases, combined with 98.5% spiritual connection, suggests that intense spiritual experiences may be particularly associated with healing outcomes—though selection bias (only survivors are represented) limits causal inference.

### 4.4 Source Bias and Triangulation

The dramatic difference between clinical and testimonial sources (12.3% vs. 92.7% transformation narratives) does not mean clinical cases lack transformation—it means clinical reports don't document it.

This suggests a triangulation strategy:
- **Clinical sources** verify that spontaneous remissions occur physically
- **Testimonial sources** document the experiential/psychological dimension
- Neither alone captures the full picture

### 4.5 Limitations and Future Directions

**Critical limitations:**

1. **No causal inference**: Observational data cannot establish causation
2. **Survivorship bias**: We cannot see transformation without physical survival
3. **Retrospective design**: Temporal ordering is self-reported
4. **AI coding**: Potential for systematic errors

**Future research should:**

1. Prospectively document psychological state changes during disease course
2. Include non-remission comparison groups
3. Use validated psychological instruments (not retrospective narrative)
4. Examine biomarkers alongside psychological measures

---

## 5. Conclusion

In 569 cases of spontaneous remission, psychological transformation preceded physical healing in 85.5% of testimonial cases with clear temporal ordering—a rate significantly exceeding chance expectation (p < 0.001). Surrender events were associated with 100% transformation prevalence and 98.3% spiritual connection.

These findings are consistent with models proposing that psychological/spiritual changes may be temporally—and perhaps causally—prior to physical healing in spontaneous remission. However, the observational nature of this data precludes causal inference, and significant methodological limitations exist.

The data support further investigation of the temporal relationship between psychological transformation and physical healing, ideally through prospective designs with appropriate controls.

---

## References

### Primary Sources

- Beauregard, M. (2014). The primordial psyche. *Journal of Consciousness Studies*, 21(7-8), 132-157.
- O'Regan, B., & Hirshberg, C. (1993). *Spontaneous remission: An annotated bibliography*. Institute of Noetic Sciences.
- Swedenborg, E. (1758). *Heaven and its wonders and hell*. Swedenborg Foundation.
- Turner, K. (2014). *Radical remission: Surviving cancer against all odds*. HarperOne.

### Data Sources

- PubMed Central (PMC): https://www.ncbi.nlm.nih.gov/pmc/
- Radical Remission Project: https://radicalremission.com/
- Near-Death Experience Research Foundation (NDERF): https://www.nderf.org/
- International Association for Near-Death Studies (IANDS): https://iands.org/

### Analysis Repository

- GitHub: `remission-analysis` repository
- Primary notebook: `remission_statistical_analysis.ipynb`
- Statistics verification: `extract_thesis_stats.py`
- Data schema: `models/questionnaire.py`

---

## Appendix A: Statistical Summary

### A.1 Primary Analysis

| Test | Statistic | p-value | Effect |
|------|-----------|---------|--------|
| Binomial (transformation first vs. 50%) | 118/138 | p < 0.001 | 85.5% |
| Chi-square (transformation first) | χ² = 69.59 | p < 0.001 | — |
| Fisher's exact (surrender × transformation) | OR = ∞ | p = 0.008 | — |

### A.2 Source Distribution

| Source | N | % | Type |
|--------|---|---|------|
| PMC | 350 | 61.5% | Clinical |
| RRP | 149 | 26.2% | Testimonial |
| NDERF | 50 | 8.8% | Testimonial |
| IANDS | 20 | 3.5% | Testimonial |

### A.3 Key Rates

| Metric | Testimonial (n=219) |
|--------|---------------------|
| Has transformation narrative | 92.7% |
| Transformation preceded (clear cases) | 85.5% |
| Surrender present | 26.5% |
| Spiritual connection | 75.3% |
| Spiritual connection given surrender | 98.3% |

---

*Document generated from verified statistical analysis of 569 spontaneous remission cases. All statistics derived from `extract_thesis_stats.py` run on the full dataset.*
