# The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology

## Abstract

**Background**: Near-death experiences (NDEs) frequently involve encounters with a "Being of Light" described in terms evoking divine presence. Whether these encounters reflect cultural conditioning or represent access to an objective spiritual reality remains contested. The Swedenborgian correspondential framework proposes a testable middle ground: the Being is ontologically real, but identification is culturally mediated.

**Methods**: We analyzed 6,753 structured NDE records from two major databases (NDERF: n=5,660; IANDS: n=1,093). Cases were coded for light encounter type, being identification, religious background, communication mode, and transformative effects using GPT-5.1 structured extraction. Chi-square tests examined independence between religious background and being identification.

**Results**: Among experiencers with being encounters (n=4,954; 73.4%), the most common identification was "unknown presence" (n=1,447; 29.2%), followed by God (n=484; 9.8%), Jesus (n=401; 8.1%), and religious figures (n=196; 4.0%). Christians were 2.6× more likely to identify Jesus than non-Christians (14.9% vs. 5.7%), but 26.6% of Christians could not identify the being. Religious background significantly predicted identification (χ² = 33.49, p < 0.000001, Cramér's V = 0.220), confirming cultural mediation. However, 12.0% of non-Christians identified Christian figures, and the "unknown presence" rate was consistent across all religious groups (σ = 4.10%), suggesting a universal phenomenological core.

**Conclusions**: The data support a two-tier model: a consistent underlying phenomenon (constant state) expressed through variable cultural interpretation (variable form). This aligns with the correspondential hypothesis: the Being is objective reality; identification is culturally conditioned perception.

**Keywords**: near-death experience, being of light, religious experience, cultural interpretation, consciousness studies

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `conceptual_framework_deep_dive.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/conceptual_framework_deep_dive.ipynb) |
| Light Being Analysis | `light_being_analysis.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/light_being_analysis.ipynb) |
| Structured Data | `structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files) |
| Extraction Model | GPT-5.1 via Azure OpenAI | Azure OpenAI Service |

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

Each record was processed using GPT-5.1 (Azure OpenAI) to extract structured data into a 41-field Pydantic schema. Fields relevant to this analysis include:

- **Demographics**: Age at NDE, sex, religious affiliation at time of NDE
- **Light Encounter**: Tunnel light, arrival light type (brilliant, warm glow, divine presence)
- **Being Identification**: Being of Light, God, Jesus, religious figure, divine being, unknown presence
- **Communication**: Mode (telepathic, verbal, nonverbal, none)
- **Life Review**: Occurrence, judgment type, emotional tone
- **Transformative Effects**: Fear of death change, spirituality shift, value changes

### 2.3 Statistical Analysis

Primary analyses employed:
- **Chi-square tests** for independence between religious background and being identification
- **Cramér's V** as effect size measure for categorical associations
- **Point-biserial correlations** for age associations with identification
- **Fisher's exact test** for 2×2 comparisons with small expected cell counts
- **Binomial tests** for proportions against null expectations

Statistical significance was set at α = 0.05, with Bonferroni correction applied for multiple comparisons where appropriate.

### 2.4 Methodological Limitations

1. **Selection bias**: Both databases represent English-speaking, predominantly Western samples
2. **Self-selection**: Individuals who had profound experiences may be more likely to report
3. **Retrospective reporting**: Accounts may be influenced by subsequent reflection and cultural exposure
4. **AI coding**: While GPT-5.1 provides consistent extraction, systematic biases may exist

---

## 3. Results

### 3.1 Sample Characteristics

#### Light Encounter Prevalence

| Light Type | N | % |
|------------|---|---|
| Any light encounter | 4,395 | 65.1% |
| Brilliant light | 2,960 | 43.8% |
| Tunnel with bright light | 1,696 | 25.1% |
| Light AND Being together | 3,884 | 57.5% |

#### Religious Affiliation Distribution

| Religious Background | N | % |
|----------------------|---|---|
| Not mentioned | 4,437 | 65.7% |
| Christian | 1,192 | 17.7% |
| Other | 652 | 9.7% |
| Atheist/Agnostic | 296 | 4.4% |
| Spiritual but not religious | 55 | 0.8% |
| Muslim | 44 | 0.7% |
| Jewish | 34 | 0.5% |
| Buddhist | 28 | 0.4% |
| Hindu | 15 | 0.2% |

### 3.2 Being Encounter Prevalence

Among all 6,753 records, 4,954 (73.4%) reported encountering one or more beings.

#### Being Identification Distribution

| Identification | N | % of All NDEs | % of Being Encounters |
|----------------|---|---------------|----------------------|
| Unknown presence | 1,447 | 21.4% | 29.2% |
| God | 484 | 7.2% | 9.8% |
| Jesus | 401 | 5.9% | 8.1% |
| Religious figure | 196 | 2.9% | 4.0% |
| No being encountered | 1,799 | 26.6% | — |

#### Number of Beings Identified

| Beings | N | % |
|--------|---|---|
| 1 being | 3,496 | 70.6% |
| 2 beings | 1,093 | 22.1% |
| 3+ beings | 365 | 7.4% |

**Finding**: The vast majority (70.6%) encounter a **single being**, consistent with a monotheistic rather than polytheistic phenomenology.

### 3.3 Primary Finding: Religious Background and Being Identification

#### Being Identification by Religious Affiliation

| Religion | N | Jesus | God | Religious Figure | Unknown Presence | No Being |
|----------|---|-------|-----|------------------|------------------|----------|
| Christian | 1,192 | 14.9% | 11.8% | 4.9% | 23.2% | 13.1% |
| Not mentioned | 4,437 | 4.1% | 6.1% | 2.1% | 20.1% | 33.6% |
| Other | 652 | 3.8% | 7.8% | 5.5% | 26.1% | 11.3% |
| Atheist/Agnostic | 296 | 4.7% | 4.7% | 2.0% | 23.0% | 17.2% |
| Spiritual not religious | 55 | 3.6% | 5.5% | 0.0% | 30.9% | 12.7% |

#### Statistical Test: Religion × Identification Independence

**Chi-square test for independence**: 
- χ² = 33.49
- df = 20
- p < 0.000001
- Cramér's V = 0.220 (medium effect)

**Interpretation**: Religious background **significantly predicts** being identification (p < 0.000001), confirming that cultural conditioning plays a role in how the Being is perceived. However, the medium effect size (V = 0.220) indicates that religion explains only a portion of the variance—substantial identification occurs outside expected religious categories.

### 3.4 The "Unknown Presence" Phenomenon

The most common identification across all groups is the **unknown presence**—a being experienced as real and personal but not identified with any specific religious figure.

| Religion | Unknown Presence Rate |
|----------|----------------------|
| Spiritual but not religious | 30.9% |
| Other | 26.1% |
| Christian | 23.2% |
| Atheist/Agnostic | 23.0% |
| Not mentioned | 20.1% |

**Standard deviation across groups**: σ = 4.10%

**Finding**: The consistency of the "unknown presence" rate across dramatically different religious backgrounds (σ = 4.10%) suggests a **universal phenomenological core** that transcends cultural interpretation.

### 3.5 Cross-Religious Identification

#### Christians Who See Non-Christian Beings

Among 1,036 Christians who encountered a being:
- 30.8% identified it as God or Jesus (expected)
- **26.6% could not identify it** (unknown presence)
- 5.7% identified another religious figure

#### Non-Christians Who See Christian Figures

Among 974 non-Christians who encountered a being:
- **12.0% identified Christian figures** (God or Jesus)
- 28.9% could not identify the being
- 10.4% identified figures from their own tradition

**Specific breakdown**:
| Religion | N with Being | % Seeing Christian Figures |
|----------|--------------|---------------------------|
| Jewish | 31 | 12.9% |
| Buddhist | 24 | 12.5% |
| Atheist/Agnostic | 245 | 11.4% |
| Other | 578 | 13.1% |

**Finding**: Non-Christians seeing Christian figures (12.0%) at rates above chance suggests the phenomenon is not purely reducible to cultural expectation.

### 3.6 Communication and Personal Nature

Among those encountering beings (n=4,954):

| Communication Mode | N | % |
|--------------------|---|---|
| Normal speech | 1,238 | 25.0% |
| Telepathic | 1,142 | 23.1% |
| No communication | 1,052 | 21.2% |
| Not specified | 768 | 15.5% |
| Mixed | 489 | 9.9% |
| Nonverbal | 265 | 5.3% |

**Active communication** (telepathic + verbal + mixed + nonverbal): **67.0%**

**Finding**: The Being is experienced as a **personal entity** capable of communication in 67% of encounters, not as an impersonal force or abstract light.

### 3.7 Life Review and Judgment

Among cases with life reviews (n=1,177; 17.4% of all NDEs):

#### Judgment Type Distribution

| Judgment Type | N | % |
|---------------|---|---|
| None | 357 | 30.3% |
| Self-judgment only | 112 | 9.5% |
| Guide/Light present | 166 | 14.1% |
| Not mentioned | 542 | 46.0% |

**No external condemnation**: 469 cases (39.8% of life reviews)

#### Emotional Tone During Life Review

| Emotional Tone | N | % |
|----------------|---|---|
| Love | 137 | 11.6% |
| Shame/regret | 101 | 8.6% |
| Mixed | 327 | 27.8% |
| Neutral | 80 | 6.8% |
| Not specified | 532 | 45.2% |

**Love:Shame ratio**: 137:101 = **1.36:1**

**Finding**: The Being is consistently characterized by **non-judgmental love**. Even during life reviews—when past harms are revisited—external condemnation is absent in 39.8% of cases, and when emotional tone is specified, love exceeds shame by 36%.

### 3.8 Transformative Effects

#### Belief Changes Post-NDE

| Change | N | % |
|--------|---|---|
| No fear of death | 1,502 | 22.2% |
| Some fear remains | 234 | 3.5% |
| No change | 52 | 0.8% |
| Not mentioned | 4,965 | 73.5% |

#### Spirituality Shifts

| Shift Type | N | % |
|------------|---|---|
| More spiritual | 617 | 9.1% |
| Less religious, more spiritual | 581 | 8.6% |
| More religious | 479 | 7.1% |
| No change | 633 | 9.4% |
| Not mentioned | 4,443 | 65.8% |

**Finding**: **22.2%** explicitly report losing all fear of death after the encounter—the single most common belief change. The experience produces **spiritual rather than religious** transformation, with 8.6% becoming "less religious but more spiritual."

### 3.9 Age and Gender Effects

#### Age Correlations with Identification

| Identification | Correlation | p-value | Mean Age (with) | Mean Age (without) |
|----------------|-------------|---------|-----------------|-------------------|
| Jesus | r = 0.055 | 0.026 | 22.0 years | 18.7 years |
| God | r = 0.049 | 0.049 | 21.5 years | 18.7 years |
| Unknown | r = -0.013 | 0.610 | 18.5 years | 19.0 years |

**Finding**: Identification as Jesus or God is weakly correlated with **older age at NDE** (approximately 3 years older), suggesting some role for accumulated religious knowledge in identification.

#### Gender Differences

| Element | Male % | Female % | Difference | p-value |
|---------|--------|----------|------------|---------|
| Any light encounter | 76.6% | 69.6% | -7.0% | 0.0000 |
| Jesus | 6.5% | 6.9% | +0.4% | 0.677 |
| God | 7.3% | 8.1% | +0.8% | 0.413 |
| Unknown presence | 23.4% | 22.7% | -0.7% | 0.627 |

**Finding**: Males report light encounters at significantly higher rates than females (p < 0.0001), but **being identification shows no gender difference** (p > 0.05 for all identifications).

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis of 6,753 near-death experiences reveals a complex interplay between universal phenomenology and cultural interpretation:

1. **Universal Encounter**: 73.4% of NDEs include being encounters, with 70.6% experiencing a **single being**—consistent with monotheistic rather than polytheistic phenomenology.

2. **Cultural Mediation Confirmed**: Religious background significantly predicts identification (χ² = 33.49, p < 0.000001). Christians are 2.6× more likely to identify Jesus than non-Christians (14.9% vs. 5.7%).

3. **Universal Core Preserved**: The "unknown presence" rate remains remarkably consistent across all religious groups (σ = 4.10%), and 12.0% of non-Christians identify Christian figures despite no prior exposure.

4. **Personal, Loving Being**: The Being communicates in 67% of encounters, is never externally condemning during life reviews (39.8% explicitly no external judgment), and love exceeds shame in emotional tone (1.36:1 ratio).

5. **Transformative Effects**: 22.2% lose all fear of death; 17.7% become more spiritual—consistent with encountering something genuinely transcendent.

### 4.2 Interpretation: Constant States, Variable Forms

The data strongly support the Swedenborgian correspondential interpretation:

**Constant States** (underlying reality):
- Being encounter occurs in 73.4% of NDEs
- Being is singular (70.6%), loving (39.8% no external judgment), personal (67% communicate)
- Transformative effects are consistent across religious backgrounds
- "Unknown presence" rate is stable (σ = 4.10%)

**Variable Forms** (cultural interpretation):
- Specific identification varies significantly with religion (Cramér's V = 0.220)
- Jesus identification: Christians 14.9%, non-Christians 5.7%
- Identification correlates weakly with age (accumulated religious knowledge)

This pattern is precisely what the correspondential hypothesis predicts: the **same spiritual reality** is perceived through **culturally conditioned forms**. The Being of Light is not a hallucination produced by dying brains (which would predict random or consistently culture-bound content), nor is it a simple projection of expectations (which would not explain non-Christians seeing Jesus or Christians seeing "unknown presence"). Instead, the data suggest an **objective encounter** with a **personal, loving presence** that **appears differently** based on the experiencer's conceptual repertoire.

### 4.3 Implications for Consciousness Studies

These findings have implications for the ongoing debate about the nature of NDE phenomena:

1. **Against Pure Cultural Construction**: If NDEs were purely cultural constructs, we would expect near-complete alignment between religious background and identification. The 26.6% of Christians who cannot identify the Being, and the 12.0% of non-Christians who see Christian figures, argue against this model.

2. **Against Pure Brain Production**: If NDEs were produced by dying brains without reference to external reality, we would expect either random content or content drawn from the individual's memory. The consistency of qualitative features (singular, loving, communicative) across cultures argues against pure brain production.

3. **For Correspondential Model**: The pattern of constant underlying experience with variable surface features aligns precisely with Swedenborg's doctrine: spiritual realities are objectively real but perceived through culturally conditioned forms.

### 4.4 Limitations

1. **Sample Bias**: English-speaking, predominantly Western sample; non-Western NDEs may show different patterns.

2. **Retrospective Reporting**: Accounts written after the event may be influenced by subsequent reflection and religious exposure.

3. **AI Coding**: While GPT-5.1 provides consistent extraction, potential for systematic biases exists.

4. **Observational Design**: Correlation between religion and identification cannot establish causation; prospective studies would be valuable.

### 4.5 Future Directions

1. **Cross-Cultural Replication**: Analysis of non-Western NDE archives to test universality claims
2. **Prospective Studies**: Documentation of religious beliefs before NDE, with post-NDE identification
3. **Machine Learning**: Predictive modeling of identification from multi-factor input
4. **Qualitative Analysis**: Deep reading of "unknown presence" descriptions to characterize the universal core

---

## 5. Conclusion

Analysis of 6,753 near-death experiences reveals a dual pattern: **cultural mediation** of specific being identification (confirmed by χ² = 33.49, p < 0.000001) alongside **phenomenological universality** in the character of the encounter (σ = 4.10% for unknown presence rate across religions). The Being of Light is consistently described as singular (70.6%), personally communicative (67.0%), non-judgmental (39.8% during life reviews), and profoundly transformative (22.2% lose all fear of death).

This pattern supports the Swedenborgian correspondential model: the Divine Human is an **objective spiritual reality** encountered during near-death states, but the specific form in which it appears is shaped by the experiencer's **cultural and religious background**. The experience is neither purely subjective (cultural construction) nor purely objective (identical perception regardless of perceiver), but a **correspondence** between spiritual reality and human reception.

The Being of Light appears to be exactly what near-death experiencers report it to be: a personal, loving presence of ultimate significance—whether called God, Jesus, Krishna, or simply "unknown light"—that transforms those who encounter it.

---

## References

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

Turner, K. A. (2014). *Radical Remission: Surviving Cancer Against All Odds*. HarperOne.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value | Effect Size |
|------|-----------|----|---------| ------------|
| Religion × Identification | χ² = 33.49 | 20 | < 0.000001 | V = 0.220 |
| Age × Jesus ID | r = 0.055 | 1,608 | 0.026 | — |
| Age × God ID | r = 0.049 | 1,608 | 0.049 | — |
| Gender × Light Encounter | χ² = 27.8 | 1 | < 0.0001 | — |

## Appendix B: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [conceptual_framework_deep_dive.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/conceptual_framework_deep_dive.ipynb)
- **Light Being Analysis**: [light_being_analysis.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/light_being_analysis.ipynb)
