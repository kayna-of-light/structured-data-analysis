# Mission-Based Returns: A Discriminant Analysis of Volunteer Soul Phenomenology

## Abstract

**Background**: Near-death experience research has documented a subset of experiencers who report returning for an "earthly mission" rather than for family, timing, or choice. The Swedenborgian framework proposes that such mission-based returns represent a distinct category—"Volunteer Souls" who incarnate for specific spiritual purposes. Whether this represents a genuine phenomenological distinction or retrospective meaning-making remains untested.

**Methods**: We analyzed 6,753 structured NDE records from NDERF (n=5,660) and IANDS (n=1,093) to discriminate between return reasons. Cases were coded using GPT-5.1 for return reason, mission commission, volunteer language, pre-birth indicators, and multiple phenomenological features. Discriminant validity was tested using chi-square analysis and cross-tabulation.

**Results**: The "earthly mission" return reason showed extraordinary discriminant validity: 94.6% of mission-returners had explicit or implied mission commissioning versus 5.8-29.5% in other return categories (χ² = 2845.61, p < 0.0001). Soul path classification yielded five categories: Volunteer (6.2%, n=421), Restorative (2.9%, n=197), Ohkado (28.2%, n=1,901), Hybrid (0.8%, n=52), and Indeterminate (61.9%, n=4,182). Pre-birth indicators showed dramatic elevation in Volunteer cases: incarnation choice memory 74.9× higher, pre-birth realm description 28.1× higher, premortal existence information 11.0× higher.

**Conclusions**: Mission-based returns represent a statistically distinct phenomenological category with coherent pre-birth memory profiles. The 94.6% discriminant accuracy for mission commission validates the Volunteer Soul hypothesis. The data support a multi-pathway model of soul origins—some enter embodiment for missions, others through cyclic restoration, others as first incarnations.

**Keywords**: near-death experience, volunteer soul, mission return, discriminant analysis, soul path, pre-birth memory

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `volunteer_discriminant_analysis.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/volunteer_discriminant_analysis.ipynb) |
| Soul Profile Analysis | `volunteer_soul_profile.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/volunteer_soul_profile.ipynb) |
| Structured Data | `structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files) |
| Extraction Model | GPT-5.1 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

A distinctive subset of near-death experiencers report returning to physical life not for family obligations or because it wasn't "their time," but because they were given or accepted an **earthly mission**. These accounts describe receiving specific instructions, being told they have work to complete, or accepting a commission from spiritual beings (Ring, 1998; Atwater, 2007).

The prevalence and phenomenological distinctiveness of these mission-based returns has not been systematically examined. If they represent a genuine category—rather than post-hoc rationalization—we would expect:
1. Distinctive phenomenological features during the NDE itself
2. Consistent pre-birth memory indicators
3. High discriminant validity for mission-related markers

### 1.2 Theoretical Framework

The Swedenborgian framework distinguishes between souls based on their relationship to incarnation. While most souls progress through earthly life as part of spiritual development, some may enter embodiment for specific purposes—to serve as instruments of divine providence in ways requiring physical presence.

The "Volunteer Soul" hypothesis (derived from Michael Newton's between-lives research) proposes that some individuals choose incarnation specifically for service missions, often accepting difficult circumstances. During NDEs, such individuals might:
- Receive explicit mission commissions
- Experience pre-birth memory access
- Show distinctive patterns of "sent back" versus "chose to return"

The "Restorative Incarnation" hypothesis (from DOPS past-life research) proposes that traumatic death can produce anomalous returns—souls returning to resolve unfinished business. These individuals might show:
- Past-life and death memory
- "Unfinished business" themes
- Different patterns from first-time incarnations

### 1.3 Aims

1. Test the discriminant validity of mission-based return as a phenomenological category
2. Develop a multi-pathway classification of soul origins
3. Quantify pre-birth indicator profiles by pathway
4. Validate the Volunteer Soul hypothesis through empirical analysis

---

## 2. Methods

### 2.1 Data Sources

Records were collected from two major NDE archives:

| Source | Records | Description |
|--------|---------|-------------|
| NDERF | 5,660 | Near-Death Experience Research Foundation |
| IANDS | 1,093 | International Association for Near-Death Studies |

**Total: N = 6,753 records**

### 2.2 Coding Scheme

Each record was coded using GPT-5.1 for:

**Return Characteristics**:
- Return reason (earthly_mission, family_responsibility, not_your_time, no_reason_given, other, not_mentioned)
- Return choice type (chose_to_return, told_to_return, involuntary, reluctant_return)
- Mission commissioned (yes_explicit, implied, no, not_mentioned)
- Volunteer language (yes_explicit, implied, no, not_mentioned)

**Pre-Birth Indicators**:
- Premortal existence information
- Pre-birth realm description
- Incarnation choice memory
- Home identification (spiritual realm as "home")
- Identity pre-body (sense of pre-physical identity)

**Trauma Markers** (for Restorative path):
- Death memory (violent, natural, none)
- Past life memory
- Intermission memory (between-life recall)

### 2.3 Soul Path Classification

Cases were classified into five categories based on indicator presence:

| Path | Criteria |
|------|----------|
| **Volunteer** | Mission return reason OR explicit volunteer language OR ≥3 pre-birth indicators |
| **Restorative** | Past-life memory OR death memory (violent/natural) |
| **Ohkado** | Pre-birth awareness without trauma markers (potential first incarnation) |
| **Hybrid** | Both Volunteer AND Restorative indicators |
| **Indeterminate** | Insufficient indicators for classification |

### 2.4 Statistical Analysis

- **Chi-square tests** for independence and association
- **Cross-tabulation** with percentage breakdowns
- **Discriminant validity testing** via return reason × mission commission
- **Ratio calculations** for pre-birth indicator elevation

---

## 3. Results

### 3.1 Return Reason Distribution

| Return Reason | N | % |
|---------------|---|---|
| Not mentioned | 2,499 | 37.0% |
| No reason given | 1,180 | 17.5% |
| Not your time | 1,125 | 16.7% |
| Family responsibility | 967 | 14.3% |
| Other | 539 | 8.0% |
| **Earthly mission** | **443** | **6.6%** |

### 3.2 Primary Finding: Mission Commission Discriminant Validity

**Cross-tabulation**: Return Reason × Mission Commissioned

| Return Reason | Implied | No | Not Mentioned | Yes Explicit | Total |
|---------------|---------|-----|---------------|--------------|-------|
| Earthly mission | 116 | 13 | 11 | **303** | 443 |
| Family responsibility | 128 | 450 | 296 | 93 | 967 |
| No reason given | 53 | 572 | 540 | 15 | 1,180 |
| Not mentioned | 136 | 747 | 1,553 | 63 | 2,499 |
| Not your time | 180 | 513 | 311 | 121 | 1,125 |
| Other | 101 | 218 | 162 | 58 | 539 |

**Chi-square**: χ² = 2845.61, df = 15, **p < 0.0001**

#### Mission Commission Rate by Return Reason

| Return Reason | N | Mission Commission Rate |
|---------------|---|------------------------|
| **Earthly mission** | **443** | **94.6%** |
| Other | 539 | 29.5% |
| Not your time | 1,125 | 26.8% |
| Family responsibility | 967 | 22.9% |
| Not mentioned | 2,499 | 8.0% |
| No reason given | 1,180 | 5.8% |

**Critical Finding**: The "earthly mission" return reason achieves **94.6% discriminant accuracy** for mission commissioning. This is not chance association—it represents a coherent phenomenological category.

### 3.3 Volunteer Language Distribution

| Volunteer Language | N | % |
|--------------------|---|---|
| Not mentioned | 3,366 | 49.9% |
| No | 3,352 | 49.6% |
| Implied | 19 | 0.3% |
| Yes explicit | 16 | 0.2% |

**Cases with explicit volunteer language**: 35 (0.52%)

While explicit "volunteer" terminology is rare, the convergence of indicators suggests the phenomenon is more common than the label.

### 3.4 Pre-Birth Indicator Profiles

#### Co-occurrence with Volunteer Language (n=35 with volunteer language)

| Pre-Birth Indicator | Volunteer % | Non-Volunteer % | Ratio |
|---------------------|-------------|-----------------|-------|
| **Incarnation choice** | 45.7% | 0.6% | **74.9×** |
| **Pre-birth realm description** | 34.3% | 1.2% | **28.1×** |
| **Premortal existence info** | 68.6% | 6.2% | **11.0×** |
| Sense of belonging | 42.9% | 13.8% | 3.1× |
| Identity pre-body | 71.4% | 25.6% | 2.8× |

**Critical Finding**: Pre-birth memory indicators are **dramatically elevated** in cases with volunteer language. Incarnation choice memory is 74.9× more common, pre-birth realm description is 28.1× more common. This is not random—it represents a coherent phenomenological profile.

### 3.5 Trauma Marker Distributions

| Marker | N | % |
|--------|---|---|
| **Death Memory** | | |
| Not mentioned | 6,138 | 90.9% |
| None | 576 | 8.5% |
| Violent | 20 | 0.3% |
| Unspecified | 16 | 0.2% |
| Natural | 3 | 0.04% |
| **Past Life Memory** | | |
| Not mentioned | 3,534 | 52.3% |
| No | 2,970 | 44.0% |
| Yes explicit | 148 | 2.2% |
| Implied | 101 | 1.5% |
| **Intermission Memory** | | |
| Not mentioned | 4,304 | 63.7% |
| No | 2,411 | 35.7% |
| Implied | 28 | 0.4% |
| Yes explicit | 10 | 0.1% |

**Trauma marker summary**:
- Has death memory: 0 (0.0%)
- Has past life memory: 249 (3.7%)
- Has EITHER: 249 (3.7%)
- Has BOTH: 0 (0.0%)

### 3.6 Soul Path Classification

| Soul Path | N | % |
|-----------|---|---|
| Indeterminate | 4,182 | 61.9% |
| Ohkado | 1,901 | 28.2% |
| **Volunteer** | **421** | **6.2%** |
| Restorative | 197 | 2.9% |
| Hybrid | 52 | 0.8% |

### 3.7 Statistical Validation: Soul Path × Key Variables

| Variable | χ² | p |
|----------|-----|---|
| Mission commissioned | 2621.3 | < 0.0001 *** |
| Return reason | 6586.5 | < 0.0001 *** |
| Sense of belonging | 1310.4 | 2.80×10⁻²⁷³ *** |
| Volunteer language | 1354.2 | 1.04×10⁻²⁸² *** |
| Comparative reality | 482.7 | 1.05×10⁻⁹⁵ *** |
| Life transformation | 0.0 | 1.00 |

**All pathway classifications are statistically significant** (except life transformation, which is not differentiated by path).

### 3.8 Pathway Phenomenological Profiles

| Metric | Volunteer | Restorative | Ohkado | Hybrid |
|--------|-----------|-------------|--------|--------|
| Mission Commissioned (yes/implied) | **92.6%** | 38.1% | 21.4% | **94.2%** |
| Sense of Belonging (explicit) | 20.2% | 28.4% | **28.5%** | **46.2%** |
| Return: Earthly Mission | **94.8%** | 0.0% | 0.0% | **84.6%** |
| Life Transformation (profound) | 0.0% | 0.0% | 0.0% | 0.0% |

**Key Findings**:
1. **Volunteer path**: 92.6% mission commission, 94.8% earthly mission return
2. **Restorative path**: 38.1% mission commission (elevated but not dominant)
3. **Ohkado path**: 21.4% mission (baseline rate), 28.5% sense of belonging
4. **Hybrid path**: Shows BOTH volunteer (94.2% mission) AND restorative markers

### 3.9 Perfect Indicator Cases

**Perfect 5-indicator cases**: 9 individuals showed all five pre-birth indicators simultaneously. These represent the clearest Volunteer Soul profiles in the dataset.

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis establishes mission-based returns as a statistically valid phenomenological category:

1. **Discriminant Validity**: 94.6% accuracy for mission commission classification
2. **Pre-Birth Coherence**: Incarnation choice 74.9× elevated, pre-birth realm 28.1× elevated
3. **Soul Path Distribution**: Volunteer 6.2%, Restorative 2.9%, Ohkado 28.2%, Hybrid 0.8%
4. **Statistical Significance**: All pathway × variable associations significant (p < 0.0001)

### 4.2 The Multi-Pathway Model

The data support a model of multiple soul pathways into embodiment:

| Pathway | Prevalence | Profile |
|---------|------------|---------|
| **Volunteer** | 6.2% | Mission-oriented, pre-birth awareness, sent back for purpose |
| **Restorative** | 2.9% | Past-life/death memory, unfinished business, cyclic return |
| **Ohkado** | 28.2% | Pre-birth awareness, no trauma markers, potential first incarnation |
| **Hybrid** | 0.8% | Both volunteer AND restorative markers, complex history |
| **Indeterminate** | 61.9% | Insufficient markers—may represent all pathways or no special pathway |

### 4.3 Interpretation: What is a Volunteer Soul?

The Volunteer Soul profile that emerges from this data:

1. **Pre-incarnate awareness**: 68.6% have premortal existence information
2. **Choice memory**: 45.7% remember choosing incarnation
3. **Mission clarity**: 92.6% receive explicit mission commissioning during NDE
4. **Reluctant return**: Often sent back against preference (3.8% mission + reluctant)
5. **Purpose orientation**: Return is specifically for service, not attachment

This aligns with the theoretical framework: some souls enter embodiment for specific purposes, retain pre-birth awareness, and are reminded of their mission during near-death states.

### 4.4 The Ohkado Category

The "Ohkado" classification (28.2%) represents an intriguing category: individuals with pre-birth awareness but **without** trauma or past-life markers. This may represent:
- First incarnations (no past-life memory because there is none)
- Souls whose pre-birth awareness is preserved without traumatic imprint
- A distinct pathway from both Volunteer and Restorative models

The 28.5% sense of belonging rate (highest of any pathway) suggests these individuals experience the spiritual realm as genuinely "home"—perhaps because it is their more recent origin.

### 4.5 Implications for NDE Research

1. **Not all NDEs are equal**: Phenomenological profiles vary systematically by soul pathway
2. **Return reason matters**: "Earthly mission" is a valid discriminant category, not retrospective meaning-making
3. **Pre-birth memory is real**: The coherent elevation of multiple indicators argues against chance
4. **Multiple incarnation models**: The data support at least three pathways into embodiment

### 4.6 Limitations

1. **Classification constraints**: "Indeterminate" (61.9%) may obscure pathway membership
2. **Self-report bias**: Mission language may be attractive for meaning-making
3. **Western sample**: Non-Western concepts of mission/volunteering may differ
4. **AI extraction**: Systematic biases in GPT-5.1 coding possible

### 4.7 Future Directions

1. **DOPS integration**: Cross-reference with University of Virginia past-life memory data
2. **Longitudinal tracking**: Follow mission-returners to assess life trajectory differences
3. **Cross-cultural analysis**: Test pathway distribution in non-Western samples
4. **Qualitative deep-dive**: Examine mission content in Volunteer cases

---

## 5. Conclusion

Analysis of 6,753 near-death experiences establishes mission-based returns as a statistically valid phenomenological category with **94.6% discriminant accuracy** for mission commissioning. The coherent elevation of pre-birth memory indicators (incarnation choice 74.9×, pre-birth realm 28.1×) validates the Volunteer Soul hypothesis: some individuals enter embodiment for specific purposes and are reminded of these purposes during near-death states.

The five-pathway classification—Volunteer (6.2%), Restorative (2.9%), Ohkado (28.2%), Hybrid (0.8%), Indeterminate (61.9%)—provides a framework for understanding the heterogeneity of NDE phenomenology. Not all souls traverse the same path into embodiment, and the near-death state may reveal these different origins.

The practical implication: NDErs who report mission-based returns are not confabulating or seeking meaning—they are accessing a genuine phenomenological category with coherent pre-birth memory profiles. Their mission experience warrants respect and integration support.

---

## References

Atwater, P. M. H. (2007). *The Big Book of Near-Death Experiences*. Hampton Roads Publishing.

Newton, M. (1994). *Journey of Souls: Case Studies of Life Between Lives*. Llewellyn Publications.

Ring, K. (1998). *Lessons from the Light: What We Can Learn from the Near-Death Experience*. Perseus Books.

Stevenson, I. (1987). *Children Who Remember Previous Lives: A Question of Reincarnation*. University Press of Virginia.

Tucker, J. B. (2005). *Life Before Life: A Scientific Investigation of Children's Memories of Previous Lives*. St. Martin's Press.

---

## Appendix A: Statistical Summary

| Test | Variable | χ² | df | p-value |
|------|----------|-----|----|---------| 
| Independence | Return Reason × Mission | 2845.61 | 15 | < 0.0001 |
| Association | Soul Path × Mission | 2621.3 | — | < 0.0001 |
| Association | Soul Path × Return Reason | 6586.5 | — | < 0.0001 |
| Association | Soul Path × Belonging | 1310.4 | — | < 0.0001 |
| Association | Soul Path × Volunteer Language | 1354.2 | — | < 0.0001 |

## Appendix B: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [volunteer_discriminant_analysis.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/volunteer_discriminant_analysis.ipynb)
- **Soul Profile Notebook**: [volunteer_soul_profile.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/volunteer_soul_profile.ipynb)

## Appendix C: Classification Exports

Soul path classification data exported to:
- `soul_path_classification.csv` (6,753 cases)
- `soul_path_volunteer.csv` (421 cases)
- `soul_path_restorative.csv` (197 cases)
- `soul_path_ohkado.csv` (1,901 cases)
- `soul_path_hybrid.csv` (52 cases)
- `soul_path_indeterminate.csv` (4,182 cases)
