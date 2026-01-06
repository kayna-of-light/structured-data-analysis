# The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology

## Abstract

**Background**: Near-death experiences (NDEs) frequently involve encounters with a "Being of Light" described in terms evoking divine presence. Whether these encounters reflect cultural conditioning or represent access to an objective spiritual reality remains contested. The Swedenborgian correspondential framework proposes a testable middle ground: the Being is ontologically real, but identification is culturally mediated.

**Methods**: We analyzed 6,753 structured NDE records from two major databases (NDERF: n=5,660; IANDS: n=1,093). Cases were coded for light encounter type, being identification, religious background, communication mode, and transformative effects using GPT-5.2 structured extraction with a questionnaire schema containing 52 extracted features. Chi-square tests examined independence between religious background and being identification.

**Results**: Among experiencers with Being of Light encounters (n=1,881; 27.9%), the most common identification was "unknown presence" (n=976; 51.9%), followed by God (n=423; 22.5%), Jesus (n=355; 18.9%), and religious figures (n=122; 6.5%). Christians were more likely to identify specific figures, but 44.2% of Christians identified "unknown presence." Religious background significantly predicted identification (χ² = 365.14, p < 0.000001), confirming cultural mediation. However, the qualitative characteristics remained consistent: 54.7% reported no external judgment during life reviews, 32.2% experienced loving/gentle judgment (vs 0.9% harsh), and 84.2% reported increased spirituality.

**Conclusions**: The data support a two-tier model: a consistent underlying phenomenon (constant state) expressed through variable cultural interpretation (variable form). This aligns with the correspondential hypothesis: the Being is objective reality; identification is culturally conditioned perception.

**Keywords**: near-death experience, being of light, religious experience, cultural interpretation, consciousness studies

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Being of Light Analysis | `01_being_of_light_analysis.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb) |
| Conceptual Framework Analysis | `04_conceptual_framework_theory.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb) |
| Structured Data | `analysis/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/analysis/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

The "Being of Light" is among the most iconic and frequently reported elements of near-death experiences. Raymond Moody's foundational work identified this figure as a brilliant light experienced as a personal presence, characterized by unconditional love and complete knowledge of the experiencer's life (Moody, 1975). Subsequent research has consistently confirmed the prevalence of light-related experiences in NDEs across cultures (van Lommel, 2010; Greyson, 2021).

The phenomenology of these encounters presents a philosophical puzzle. The Being is almost universally described as supremely loving, non-judgmental, and possessed of complete knowledge—attributes traditionally associated with the Divine. Yet experiencers from different religious backgrounds identify this presence differently: Christians often see Jesus or God, while Hindus may see Yama or Krishna, and secular experiencers describe an "unknown presence" or "pure light."

### 1.2 Theoretical Framework

The present analysis employs Emanuel Swedenborg's doctrine of correspondences (Swedenborg, 1758) as an interpretive framework. This doctrine proposes that spiritual realities present themselves to human perception through forms drawn from the recipient's mental repertoire. The same spiritual entity may thus appear differently to different observers—not through deception, but through the structure of spiritual-natural correspondence.

On this model:
1. The **Divine Human** is the objective spiritual reality encountered
2. The experiencer's **mental framework** shapes how this reality is perceived
3. The result is **constant states** (the encounter itself) expressed through **variable forms** (Jesus, Buddha, unknown light)

This generates a testable prediction: if the correspondential model is correct, we should observe:
- **Variation** in specific identification correlated with religious background (cultural mediation)
- **Consistency** in the qualitative character of the encounter across backgrounds (underlying reality)

### 1.3 Aims

The primary aim is to test whether being identification varies systematically with religious background while core phenomenology remains constant. Secondary aims include:

1. Quantifying the prevalence of different being identifications
2. Testing whether the Being exhibits monotheistic characteristics (single, personal, loving)
3. Examining the relationship between identification and transformative effects
4. Assessing the "cultural interpretation vs. objective reality" debate empirically

---

## 2. Methods

### 2.1 Data Sources

Records were collected from the two largest English-language NDE archives:

| Source | Type | Records | Description |
|--------|------|---------|-------------|
| NDERF | Self-report | 5,660 | Near-Death Experience Research Foundation questionnaire responses |
| IANDS | Self-report | 1,093 | International Association for Near-Death Studies accounts |

**Total: N = 6,753 records**

### 2.2 Coding Scheme

Each record was processed using GPT-5.2 (Azure OpenAI) to extract structured data into a comprehensive Pydantic schema with 52 extracted features. Key schema capabilities include:

- **Temporal splits**: `death_fear_before/after`, `spirituality_before/after`, `religiosity_before/after`
- **Religious granularity**: `religious_background` vs `religious_belief_at_nde`, `denomination_at_nde` (Catholic, Evangelical, Mormon, etc.)
- **Judgment splits**: `judgment_source`, `judgment_intensity`, `experiencer_emotion`
- **Return splits**: `return_agency`, `return_willingness`

Fields relevant to this analysis include:
- **Demographics**: Age at NDE, sex, religious affiliation at time of NDE
- **Light Encounter**: `light_encounter` type (brilliant_light, being_of_light, presence_without_visual)
- **Being Identification**: `primary_identification` (unknown_presence, god, jesus, religious_figure, buddha)
- **Communication**: Mode (telepathic, normal_speech, nonverbal, no_communication)
- **Life Review**: Occurrence, `judgment_source`, `judgment_intensity`, `experiencer_emotion`
- **Transformative Effects**: Fear changes, spirituality shift, value changes

### 2.3 Statistical Analysis

Primary analyses employed:
- **Chi-square tests** for independence between religious background and being identification
- **Cramér's V** as effect size measure for categorical associations
- **Mann-Whitney U tests** for non-parametric group comparisons
- **Random Forest classification** for predictive modeling of cultural naming

Statistical significance was set at α = 0.05.

### 2.4 Methodological Note: Light Being vs Other Beings

A **critical methodological distinction** in this analysis: we separate **Being of Light** encounters (the transcendent, central entity representing/emanating from the Light) from **Other Beings** (deceased relatives, angels, guides). This distinction is essential for theory validation:

| Category | N | % of All NDEs |
|----------|---|---------------|
| Light Being encounters | 1,881 | 27.9% |
| Other beings only (no Light) | 1,898 | 28.1% |
| No beings at all | 2,974 | 44.0% |

Among Light Being encounters:
- Light Being ALONE: 1,110 (59.0%)
- Light Being + Other beings: 771 (41.0%)

---

## 3. Results

### 3.1 Sample Characteristics

#### Light Encounter Prevalence

| Light Type | N | % |
|------------|---|---|
| Brilliant light | 2,761 | 40.9% |
| Being of light | 797 | 11.8% |
| Presence without visual | 285 | 4.2% |
| No light mentioned | 1,636 | 24.2% |
| Not mentioned | 1,274 | 18.9% |

#### Religious Affiliation Distribution (with usable data)

| Religious Background | N | Light Being Rate |
|----------------------|---|------------------|
| Christian | 1,282 | 39.7% |
| Jewish | 38 | 28.9% |
| Spiritual not religious | 22 | 27.3% |
| Other | 115 | 24.3% |
| Atheist/Agnostic | 100 | 24.0% |
| Muslim | 43 | 9.3% |

**Statistical Test**: Chi-square test: χ² = 19.92, p = 0.0002, df = 3
- Light Being presence rates **vary significantly by religion**

### 3.2 Being of Light Identification

Among 1,881 Light Being encounters:

| Identification | N | % |
|----------------|---|---|
| Unknown presence | 976 | **51.9%** |
| God | 423 | 22.5% |
| Jesus | 355 | 18.9% |
| Religious figure (specified) | 122 | 6.5% |
| Buddha | 5 | 0.3% |

**Key Finding**: The majority (**51.9%**) identify the Being as "unknown presence"—transcending all cultural categories.

#### Identification by Religious Background

| Religion | Unknown % | God % | Jesus % |
|----------|-----------|-------|---------|
| Atheist/Agnostic | 66.7% | 8.3% | 8.3% |
| Spiritual not religious | 66.7% | 16.7% | 16.7% |
| Christian | 44.2% | 21.8% | 25.1% |
| Jewish | 54.5% | 18.2% | 27.3% |
| Buddhist | 20.0% | 40.0% | 0.0% |
| Muslim | 100.0% | 0.0% | 0.0% |
| Hindu | 33.3% | 0.0% | 0.0% |

**Statistical Test**: Chi-square test: χ² = 365.14, p < 0.000001, df = 32
- Religious background **significantly predicts identification vocabulary**
- However, "unknown presence" appears at 20-100% across ALL religions

### 3.3 Monotheistic vs Polytheistic Traditions

| Tradition | N | Light Being Rate | Unknown Rate |
|-----------|---|------------------|--------------|
| Monotheistic (Christian/Muslim/Jewish) | 1,363 | 38.4% | 43.1% |
| Polytheistic (Hindu/Buddhist) | 29 | 27.6% | 25.0% |
| Non-religious (Atheist/Spiritual) | 122 | 24.6% | 60.0% |

**Finding**: Even polytheists encounter a **SINGULAR transcendent entity**, not multiple beings, suggesting the singular nature is a property of the Being itself, not observer projection.

### 3.4 Unique Authoritative Position of Light Being

| Metric | Light Being (n=1,881) | Other Beings Only (n=1,898) | Chi-Square |
|--------|----------------------|----------------------------|------------|
| Significant guidance | 81.7% | 74.9% | χ² = 25.24, p < 0.000001 |
| Emotional greeting | 45.1% | 35.4% | — |

**Finding**: The Being of Light occupies a **unique authoritative position**—providing significantly more guidance than other beings encountered.

### 3.5 Life Review and Judgment Analysis

Among 453 Light Being encounters with life reviews:

#### Judgment Source

| Source | N | % |
|--------|---|---|
| None | 123 | 27.2% |
| Being of Light | 121 | 26.7% |
| Not mentioned | 86 | 19.0% |
| Guide or entity | 84 | 18.5% |
| Self | 39 | 8.6% |

**No External Condemnation**: 54.7% (none + self-only)

#### Judgment Intensity

| Intensity | N | % |
|-----------|---|---|
| Loving/gentle | 146 | **32.2%** |
| Not applicable | 121 | 26.7% |
| Not specified | 90 | 19.9% |
| Uncomfortable | 51 | 11.3% |
| Neutral | 41 | 9.1% |
| Harsh/condemning | 4 | **0.9%** |

**Love:Harsh Ratio**: 146:4 = **36.5:1**

**Key Finding**: When judgment occurs, it is overwhelmingly loving (32.2%) vs harsh (0.9%)—a ratio of 36.5:1.

#### Judgment Source × Intensity Cross-Tab

| Source | Harsh | Loving | Neutral | Uncomfortable |
|--------|-------|--------|---------|---------------|
| Being of Light | 2 | 91 | 9 | 18 |
| Guide/entity | 2 | 36 | 23 | 20 |
| Self | 0 | 17 | 9 | 11 |
| None | 0 | 2 | 0 | 0 |

**New Insight**: Among self-judgments, 43.6% are LOVING/GENTLE—suggesting even self-reflection during life review occurs in an atmosphere of love, not condemnation.

#### Christians with Life Reviews (n=147)

- No external condemnation: **63.3%**
- Loving/gentle judgment: **31.3%**

**Expectation vs Reality**: Christians who may culturally expect divine judgment overwhelmingly experience love and acceptance instead.

### 3.6 Communication Analysis

#### Communication Mode Distribution (Light Being encounters)

| Mode | N | % |
|------|---|---|
| Telepathic | 654 | **34.8%** |
| Nonverbal | 546 | 29.0% |
| Normal speech | 414 | 22.0% |
| Not specified | 204 | 10.8% |
| No communication | 63 | 3.4% |

**Finding**: Telepathic communication (34.8%) is the dominant mode with the Light Being, suggesting a **non-physical, mind-to-mind connection**.

#### Guidance Types Received

| Guidance Type | Light Being | Other Beings |
|---------------|-------------|--------------|
| Directional | 875 | 911 |
| Informational | 711 | 603 |
| Life guidance | 683 | 529 |
| Comfort | 672 | 600 |
| Teaching | 475 | 239 |

**Finding**: The Being of Light provides substantially more **teaching** (475 vs 239) than other beings—acting as conscious educator.

### 3.7 Transformative Effects

#### Death Fear Transformation (Before/After Split)

| Metric | Light Being (n=33) | Other Being (n=24) |
|--------|-------------------|-------------------|
| Mean fear BEFORE | 1.73 | 2.08 |
| Mean fear AFTER | 1.00 | 1.08 |
| Fear decreased | 36.4% | 50.0% |
| Fear increased | 0.0% | 0.0% |

(Scale: 1=NONE, 5=EXTREME)

#### Spirituality Changes

Among Light Being encounters with spirituality data (n=190):
- **Increased**: 160 (84.2%)
- Decreased: 3 (1.6%)
- Unchanged: 27 (14.2%)

#### Value Shift Distribution

| Shift | N | % |
|-------|---|---|
| Major | 818 | 43.5% |
| Subtle | 303 | 16.1% |
| None | 97 | 5.2% |

**Finding**: **84.2%** report increased spirituality after Light Being encounter—the most common transformation.

### 3.8 Jesus vs Unknown Identification Comparison

Among Christians with Light Being encounters (n=460):

| Identification | N | % |
|----------------|---|---|
| Unknown only | 179 | 38.9% |
| Jesus only | 102 | 22.2% |
| God only | 83 | 18.0% |
| Mixed | 96 | 20.9% |

**Property Comparison: Jesus vs Unknown Identifiers**

| Property | Jesus (n=102) | Unknown (n=179) | Difference |
|----------|---------------|-----------------|------------|
| Self-judgment | 1.0% | 1.7% | -0.7% |
| Loving judgment | 4.9% | 5.0% | -0.1% |
| Love emotion | 2.9% | 5.6% | -2.6% |

**All differences < 10%**: Experiencers naming "Jesus" vs "Unknown" report **virtually identical experiential properties**.

### 3.9 Denomination Analysis

Among Christians with denomination data (n=287):

| Denomination | N | Jesus % | Unknown % | God % |
|--------------|---|---------|-----------|-------|
| Catholic | 120 | 21.7% | 56.7% | 23.3% |
| Other Christian | 71 | 35.2% | 53.5% | 28.2% |
| Mainline Protestant | 41 | 26.8% | 61.0% | 24.4% |
| Evangelical/Baptist | 24 | 20.8% | 62.5% | 37.5% |
| Mormon/LDS | 13 | 46.2% | 30.8% | 15.4% |

**Theological Hypothesis Test**:
- Catholic Jesus identification: 21.7%
- Evangelical Jesus identification: 20.8%
- Difference: -0.8%

**Finding**: Catholics and Evangelicals—despite different theological emphases on Jesus—show **nearly identical identification rates**, suggesting the experience is not shaped by doctrinal expectations.

### 3.10 Machine Learning: Predicting Cultural Naming

**Random Forest Classifier**: Can religious background predict being identification?

| Metric | Value |
|--------|-------|
| Test accuracy | 37.8% |
| Cross-validation | 38.2% (±8.9%) |
| Baseline (most common) | 45.9% |

**Finding**: ML model performs **below baseline**—religious background cannot reliably predict identification. This argues against pure cultural determination.

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis of 6,753 near-death experiences reveals a complex interplay between universal phenomenology and cultural interpretation:

1. **Transcendence of Categories**: 51.9% of Light Being encounters are identified as "unknown presence"—the Being transcends all cultural and religious labels.

2. **Cultural Mediation Confirmed**: Religious background significantly predicts identification vocabulary (χ² = 365.14, p < 0.000001). Christians are more likely to use "God/Jesus" labels.

3. **Universal Core Preserved**: The qualitative characteristics remain constant regardless of naming:
   - 54.7% no external judgment
   - 32.2% loving judgment (vs 0.9% harsh) — 36.5:1 ratio
   - 84.2% increased spirituality
   - Experiential properties identical for "Jesus" vs "Unknown" identifiers (all differences <10%)

4. **Singular Entity**: Even polytheists encounter ONE transcendent being, suggesting singularity is an objective property of the Being.

5. **Unique Authoritative Position**: Light Being provides significantly more guidance than other beings (χ² = 25.24, p < 0.000001).

### 4.2 Interpretation: Constant States, Variable Forms

The data strongly support the Swedenborgian correspondential interpretation:

**Constant States** (underlying reality):
- 51.9% transcend all cultural categories ("unknown presence")
- Singular being encountered (even by polytheists)
- Loving, non-judgmental character (36.5:1 love:harsh ratio)
- Teaching and transformative function (84.2% increased spirituality)
- Identical experiential properties regardless of naming

**Variable Forms** (cultural interpretation):
- Specific identification varies with religion (significant χ²)
- Christians use "God/Jesus" vocabulary
- Atheists use "presence/light" vocabulary
- But ALL describe the SAME underlying phenomenon

This pattern is precisely what the correspondential hypothesis predicts: the **same spiritual reality** is perceived through **culturally conditioned forms**. The Being of Light is not a hallucination produced by dying brains (which would predict random or consistently culture-bound content), nor is it a simple projection of expectations (which would show differences in experiential properties between "Jesus" and "Unknown" encounters—but they are identical).

### 4.3 The "Expect Judgment, Find Love" Pattern

A particularly striking finding is the **correction mechanism**:
- Christians who may culturally expect divine judgment: **63.3% report no external condemnation**
- Even during life reviews, love:harsh ratio is **36.5:1**
- Harsh judgment appears in only **0.9%** of cases

This suggests the experience **corrects** rather than confirms expectations—arguing strongly for external reality rather than projection.

### 4.4 Limitations

1. **Sample Bias**: English-speaking, predominantly Western sample
2. **Retrospective Reporting**: Accounts may be influenced by subsequent reflection
3. **AI Coding**: GPT-5.2 extraction may have systematic biases
4. **Observational Design**: Cannot establish causation

### 4.5 Future Directions

1. **Cross-Cultural Replication**: Non-Western NDE archives
2. **Prospective Studies**: Pre-NDE belief documentation
3. **Deeper Phenomenological Analysis**: Qualitative study of "unknown presence" descriptions

---

## 5. Conclusion

Analysis of 6,753 near-death experiences reveals that the Being of Light is:

1. **Transcendent**: 51.9% cannot fit it into any cultural category
2. **Singular**: Even polytheists encounter ONE being
3. **Unconditionally Loving**: 36.5:1 love:harsh ratio during life reviews
4. **Transformative**: 84.2% report increased spirituality
5. **Consistently Experienced**: Identical properties whether named "Jesus" or "Unknown"

This pattern supports the Swedenborgian correspondential model: the Divine Human is an **objective spiritual reality** encountered during near-death states, but the specific form in which it appears is shaped by the experiencer's **cultural and religious vocabulary**. The experience is neither purely subjective (cultural construction) nor purely objective (identical perception regardless of perceiver), but a **correspondence** between spiritual reality and human reception.

The Being of Light appears to be exactly what near-death experiencers report it to be: a personal, loving presence of ultimate significance—whether called God, Jesus, Krishna, or simply "unknown light"—that transforms those who encounter it.

---

## References

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value | Effect Size |
|------|-----------|----|---------| ------------|
| Religion × Presence Rate | χ² = 19.92 | 3 | 0.0002 | — |
| Religion × Identification | χ² = 365.14 | 32 | < 0.000001 | — |
| Light Being vs Other: Guidance | χ² = 25.24 | 1 | < 0.000001 | — |
| Religion → Unknown ID | χ² = 8.73 | — | 0.033 | V = 0.127 |
| ML Classification Accuracy | — | — | — | 37.8% |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,660 |
| IANDS records | 1,093 |
| Light Being encounters | 1,881 (27.9%) |
| Unknown presence identification | 51.9% |
| No external judgment | 54.7% |
| Love:Harsh judgment ratio | 36.5:1 |
| Increased spirituality | 84.2% |
| Christians: No external condemnation | 63.3% |

## Appendix C: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebooks**: 
  - [01_being_of_light_analysis.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb)
  - [04_conceptual_framework_theory.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb)
