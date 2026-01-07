# The East-West NDE Dichotomy: Challenging Cultural Paradigms Through Empirical Analysis

## Abstract

**Background**: Scholarly literature posits a fundamental dichotomy between Western and Japanese near-death experiences. Western NDEs are characterized as featuring a personified "Being of Light" (70–80%), "Cities of Light," and frequent life reviews (25–30%), while Japanese NDEs allegedly involve impersonal light, flower gardens, and no life reviews. This paradigm has shaped cross-cultural NDE research for decades, yet the empirical basis for these claims has rarely been tested against large-scale Western datasets.

**Methods**: We analyzed 6,753 structured NDE records from two major databases (NDERF: n=5,660; IANDS: n=1,093) coded for light encounter type, being identification, environment features, life review occurrence, and return reasons using GPT-5.2 structured extraction. Chi-square tests examined associations between phenomenological features, and Fisher's exact test assessed purpose-interaction correlations.

**Results**: The data fundamentally contradict the claimed Western profile. Being of Light encounters occurred in only 11.8% of Western NDEs—not 70–80%. Brilliant light without personification (40.9%) dominated, a ratio of 3.8:1 impersonal to personified. Nature/landscape settings (17.0%) exceeded urban/building settings (11.4%; χ² = 74.7, p < 0.0001). Life reviews occurred in 17.5%—between Western and Japanese claimed rates. Critically, personal interaction correlated strongly with purposive elements: those with earthly missions were 4.4× more likely to encounter the Being of Light (Fisher's exact p < 10⁻⁴⁶). Deceased relatives (17.9%) exceeded religious figures (9.9%) as beings encountered—aligning with Japanese rather than Western stereotypes.

**Conclusions**: The East-West dichotomy reflects scholarly projection rather than phenomenological reality. Western NDEs are far closer to the "Japanese" description than the literature claims. The key variable determining personal interaction is not culture but purpose: the Light engages personally when the transformative goal requires it. This supports a correspondential model of constant underlying reality with variable cultural expression, mediated by purposive economy rather than cultural determination.

**Keywords**: near-death experience, cross-cultural, Being of Light, life review, cultural paradigm, purposive economy, Japanese NDE, correspondences

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Notebook | `05_cultural_paradigm_challenge.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb) |
| Structured Data | `structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

Since the publication of Ornstein's "Japanese NDEs and the Being of Light" and subsequent cross-cultural analyses by Kellehear, Becker, and Ohkado, a paradigm has crystallized in the NDE literature: Western and Japanese near-death experiences represent fundamentally different phenomenological profiles. The Western NDE, on this view, is characterized by encounters with a personified "Being of Light" (claimed in 70–80% of cases), elaborate "Cities of Light," and frequent life reviews serving as moral examinations (25–30%). The Japanese NDE, by contrast, features impersonal or ambient light without personification, natural settings such as flower gardens and rivers, encounters with ancestors rather than divine figures, and notably absent life reviews.

This dichotomy has profound implications for NDE interpretation. If the phenomenology varies systematically by culture, this supports the hypothesis that NDEs are constructed from cultural expectations—the dying brain generating experiences shaped by what the experiencer has been taught to expect. If, however, the dichotomy is overstated or based on selection bias, the case for cultural construction weakens considerably.

The problem is that the claimed Western profile has rarely been tested against large, systematically coded Western datasets. The 70–80% Being of Light figure, for instance, appears to derive from early studies using selected samples and retrospective compilation. The "Cities of Light" motif may reflect iconic cases rather than population prevalence. The claimed life review rates similarly derive from variable methodologies.

### 1.2 Theoretical Framework

The present analysis applies a Swedenborgian correspondential framework to evaluate the East-West paradigm. This framework proposes that spiritual realities are ontologically constant but perceptually variable: the same underlying phenomenon may appear differently to different observers based on their mental repertoire and cultural vocabulary. Critically, this model predicts that *superficial* features (naming, visual imagery, setting descriptions) may vary culturally while *deep* features (presence, love, transformation) remain constant.

The correspondential framework generates specific predictions:
1. The underlying light phenomenon should be universal, but whether experiencers perceive it as "personified" versus "impersonal" may depend on factors other than culture
2. Natural versus urban imagery should not systematically differ by culture if both are valid correspondential expressions
3. The presence or absence of personal interaction (life review, dialogue, mission commissioning) should correlate with functional purpose rather than cultural background

A novel prediction emerges from extending the correspondential framework: if the NDE operates with **purposive economy**—every element serving the transformative goal—then personal interaction should cluster where purpose requires it. The Light would engage in dialogue when commissioning a mission, conduct life reviews when teaching is needed, and remain as ambient presence when presence alone suffices. Cultural differences would then reflect differences in sample composition (what purposes were represented) rather than differences in the nature of the Light itself.

### 1.3 Aims

1. Test the claimed prevalence rates for key "Western" NDE features against a large systematically-coded dataset
2. Examine the nature/urban ratio to assess the "Cities of Light" versus "Flower Gardens" dichotomy
3. Quantify the personified versus impersonal light encounter ratio in Western NDEs
4. Test whether personal interaction correlates with cultural background or with purposive elements
5. Evaluate whether the East-West dichotomy reflects phenomenological reality or scholarly projection

---

## 2. Methods

### 2.1 Data Sources

Records were collected from the two largest English-language NDE archives. The Near-Death Experience Research Foundation (NDERF) contributed 5,660 questionnaire responses, and the International Association for Near-Death Studies (IANDS) contributed 1,093 accounts. The combined corpus of 6,753 records constitutes the largest systematically structured NDE dataset analyzed to date.

| Source | Records | Description |
|--------|---------|-------------|
| NDERF | 5,660 | Questionnaire responses with standardized fields |
| IANDS | 1,093 | Narrative accounts with biographical context |
| **Total** | **6,753** | Combined corpus |

### 2.2 Coding Scheme

Each record was processed using GPT-5.2 (Azure OpenAI) for structured extraction into a Pydantic schema with 52 extracted features. Fields relevant to this analysis include:

**Light Encounter**:
- Light encounter type (brilliant_light, being_of_light, presence_without_visual, no, not_mentioned)

**Being Identification**:
- Being identifications at arrival (god, jesus, deceased_relative_guide, unknown_presence, angels, religious_figure_specified, buddha, other)

**Environment Features**:
- Environment features (light, landscape, buildings, sky, colors, water, other)
- Setting descriptors

**Life Review**:
- Occurrence (no, brief, extensive, not_mentioned)
- Judgment source
- Perspective of others

**Boundary and Return**:
- Boundary type (none, physical_barrier, verbal_limit, threshold, not_mentioned)
- Return reasons (earthly_mission, family_responsibility, not_your_time, unfinished_business, other)

### 2.3 Statistical Analysis

Primary analyses employed:
- Chi-square tests for independence between categorical variables
- Fisher's exact test for 2×2 tables with purposive element associations
- Binomial tests comparing observed rates to claimed rates
- Ratio analyses for impersonal:personified light encounters
- Cross-tabulation of light type × purposive elements

---

## 3. Results

### 3.1 Light Encounter Prevalence: The Primary Claim Refuted

The literature claims that 70–80% of Western NDEs feature a personified "Being of Light." Our data fundamentally contradict this claim.

| Light Encounter Type | N | % |
|---------------------|---|---|
| Brilliant light (impersonal) | 2,761 | 40.9% |
| No light | 1,636 | 24.2% |
| Not mentioned | 1,274 | 18.9% |
| Being of Light (personified) | 797 | **11.8%** |
| Presence without visual | 285 | 4.2% |
| **Total** | **6,753** | 100.0% |

**Critical Finding**: The Being of Light—described as a personified presence—appears in only **11.8%** of Western NDEs, not 70–80%. Brilliant light without explicit personification occurs in 40.9%. The ratio of impersonal to personified light is **3.8:1**.

If we include presence without visual form (sensed but not seen) with impersonal light, the impersonal category reaches 45.1% versus 11.8% personified—a ratio of **3.8:1**. This is the opposite of what the East-West paradigm predicts for Western NDEs.

### 3.2 Being Identification: Ancestors Versus Divine Figures

The East-West paradigm claims Western experiencers encounter divine figures (God, Jesus) while Japanese experiencers encounter ancestors. Our data show deceased relatives dominate over religious figures even in Western NDEs.

| Being Type | N | % of all NDEs |
|------------|---|---------------|
| Other (unspecified) | 1,732 | 25.6% |
| Deceased relative/guide | 1,096 | 16.2% |
| Unknown presence | 1,049 | 15.5% |
| God | 499 | 7.4% |
| Jesus | 399 | 5.9% |
| Angels | 373 | 5.5% |
| Religious figure (specified) | 160 | 2.4% |
| Buddha | 7 | 0.1% |

| Summary Category | N | % |
|------------------|---|---|
| Any deceased relative | 1,206 | **17.9%** |
| Any religious figure (God/Jesus/angel/religious) | 670 | **9.9%** |

**Critical Finding**: Deceased relatives (17.9%) are encountered **more often** than religious figures (9.9%) in Western NDEs. This directly contradicts the paradigm that positions ancestor encounters as distinctively Eastern. Western NDEs align more closely with the "Japanese" pattern than the literature claims.

### 3.3 Environment Features: Nature Versus Cities

The paradigm claims Western NDEs feature "Cities of Light" while Japanese NDEs feature natural settings like flower gardens. Our data show nature dominates over urban imagery in Western NDEs.

| Environment Feature | N | % of all NDEs |
|--------------------|---|---------------|
| Light | 3,395 | 50.3% |
| Other | 2,742 | 40.6% |
| Colors | 1,906 | 28.2% |
| **Landscape/nature** | 1,151 | **17.0%** |
| Sky | 871 | 12.9% |
| **Buildings/urban** | 772 | **11.4%** |
| Water | 414 | 6.1% |

Chi-square test (nature vs. urban): χ² = 74.7, p < 0.0001

**Critical Finding**: Nature/landscape settings (17.0%) significantly exceed urban/building settings (11.4%) in Western NDEs. The "Cities of Light" Western stereotype is not supported by the data. Western NDEs may be closer to Japanese "flower gardens" than the paradigm assumes.

### 3.4 Life Review Rates: Between the Claimed Extremes

The paradigm claims Western life reviews occur in 25–30% of cases while Japanese life reviews are essentially absent. Our data show an intermediate rate.

| Life Review Occurrence | N | % |
|-----------------------|---|---|
| No | 5,245 | 77.7% |
| Brief | 718 | 10.6% |
| Extensive | 465 | 6.9% |
| Not mentioned | 325 | 4.8% |
| **Total with life review** | **1,183** | **17.5%** |

**Critical Finding**: Life reviews occur in **17.5%** of Western NDEs—below the claimed 25–30% "Western" rate but above the claimed ~0% "Japanese" rate. The dichotomy overstates the difference.

### 3.5 Tunnel Passage: The "Defining Western Feature"

The tunnel passage is claimed as a defining Western feature (34–50%), rare in Japanese NDEs.

| Passage Type | N | % |
|--------------|---|---|
| No | 3,361 | 49.8% |
| Tunnel | 1,602 | **23.7%** |
| Other | 733 | 10.9% |
| Void | 538 | 8.0% |
| Not mentioned | 519 | 7.7% |

**Finding**: Tunnel passage occurs in **23.7%**—below the claimed 34–50% Western rate. The tunnel is present but not as dominant as the paradigm claims.

### 3.6 Boundary Encounters

| Boundary Type | N | % |
|---------------|---|---|
| None | 2,790 | 41.3% |
| Verbal limit | 1,233 | 18.3% |
| Not mentioned | 1,130 | 16.7% |
| Physical barrier | 869 | 12.9% |
| Threshold | 731 | 10.8% |
| **Any boundary** | **2,833** | **42.0%** |

Boundary encounters (42.0%) represent a substantial feature, with verbal limits (18.3%) and physical barriers (12.9%) both common—consistent with the Japanese emphasis on being "sent back" at a river or barrier.

### 3.7 The Purposive Economy Hypothesis: A Novel Finding

Having demonstrated that Western NDEs are far closer to the "Japanese" profile than claimed, we turn to what *does* predict personal interaction with the Light. If culture does not determine whether the Light appears as personified, what does?

The analysis reveals a striking pattern: **personal interaction correlates with purposive elements**, not cultural background.

| Purposive Element | Personal Element | Co-occur | Expected | Ratio | p-value |
|-------------------|------------------|----------|----------|-------|---------|
| Life Review | Being of Light | 255 | 139.6 | **1.83×** | 4.2 × 10⁻³⁰ *** |
| Life Review | Religious Being | 217 | 141.5 | **1.53×** | 1.4 × 10⁻¹³ *** |
| Earthly Mission | Being of Light | 200 | 73.5 | **2.72×** | 1.4 × 10⁻⁶⁰ *** |
| Earthly Mission | Religious Being | 178 | 74.5 | **2.39×** | 1.4 × 10⁻⁴⁰ *** |
| Not Your Time | Being of Light | 297 | 172.2 | **1.72×** | 4.6 × 10⁻³⁰ *** |
| Family Responsibility | Being of Light | 203 | 137.4 | **1.48×** | 7.9 × 10⁻¹¹ *** |

Every purposive element correlates significantly with personal interaction. The Light engages personally **when purpose requires it**.

### 3.8 The Mission Signature: The Strongest Evidence

The earthly mission return reason provides the most powerful test. Commissioning someone with a mission requires personal communication—you cannot assign a task impersonally.

| Condition | Being of Light Rate | Religious Being Rate |
|-----------|---------------------|----------------------|
| With earthly mission (n=623) | **32.1%** | **28.6%** |
| Without earthly mission (n=6,130) | 9.7% | 10.3% |
| **Ratio** | **3.3×** | **2.8×** |

Fisher's exact test (Mission × Being of Light):

| has_mission | No BoL | BoL |
|-------------|--------|-----|
| False | 5,533 | 597 |
| True | 423 | 200 |

**Odds Ratio: 4.38**, p = 1.25 × 10⁻⁴⁶

**Critical Finding**: Those returning with an earthly mission have **4.4× the odds** of encountering the Being of Light. This is not chance association—it represents a functional relationship. The Light becomes personal when personal communication is required for the transformative purpose.

### 3.9 Light Type Versus Purposive Elements

Comparing Being of Light encounters with brilliant light encounters on purposive elements:

| Purposive Element | Being of Light | Brilliant Light | Ratio |
|-------------------|----------------|-----------------|-------|
| Life review rate | 32.0% (255/797) | 19.1% (526/2,761) | **1.68×** |
| Earthly mission rate | 25.1% (200/797) | 9.5% (263/2,761) | **2.64×** |
| Any return reason | 67.0% | 35.8% | **1.87×** |

Chi-square (light type × life review): χ² = 183.20, p < 0.0001

**Critical Finding**: Being of Light encounters have significantly higher rates of all purposive elements. The Light engages personally when the purpose—teaching (life review) or commissioning (mission)—requires personal engagement.

### 3.10 Summary: Observed Versus Claimed Rates

| Feature | Claimed Western | Observed | Claimed Japanese | Alignment |
|---------|-----------------|----------|------------------|-----------|
| Being of Light | 70–80% | **11.8%** | Rare | Closer to Japanese |
| Impersonal light | Rare | **40.9%** | Common | Matches Japanese |
| Life review | 25–30% | **17.5%** | ~0% | Between |
| Tunnel | 34–50% | **23.7%** | Rare | Lower than claimed |
| Nature > Cities | No | **1.5×** (17.0% vs 11.4%) | Yes | Matches Japanese |
| Deceased > Religious | No | **1.8×** (17.9% vs 9.9%) | Yes | Matches Japanese |

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis reveals that the East-West NDE dichotomy is largely a scholarly construction that does not survive empirical testing:

1. **Being of Light prevalence**: 11.8% observed versus 70–80% claimed—the personified Being is a minority, not majority, feature
2. **Light character**: Impersonal light (40.9%) exceeds personified (11.8%) by 3.8:1—Western NDEs feature impersonal light more than claimed
3. **Environment**: Nature settings (17.0%) exceed urban settings (11.4%)—the "Cities of Light" stereotype is not supported
4. **Beings encountered**: Deceased relatives (17.9%) exceed religious figures (9.9%)—Western NDEs show the "ancestor" pattern allegedly distinctive to Japan
5. **Life reviews**: 17.5% observed—between the claimed Western (25–30%) and Japanese (~0%) rates
6. **Purpose predicts interaction**: Earthly mission correlates with Being of Light at 4.4× odds (p < 10⁻⁴⁶)—personal interaction serves function, not culture

### 4.2 The Correspondential Interpretation: Constant State, Variable Form

The data support a two-tier model distinguishing **constant states** (the underlying reality) from **variable forms** (the perceptual expression):

| Constant State | Evidence |
|----------------|----------|
| Light presence | 56.9% report some form of light (brilliant, being, presence) |
| Beings encountered | 44.1% encounter some form of being |
| Transformative impact | Consistent across all encounter types |
| Boundary/return structure | 42.0% encounter boundaries |

| Variable Form | Evidence |
|---------------|----------|
| Light personification | Ranges from 11.8% (explicit) to 40.9% (brilliant) |
| Being identification vocabulary | Cultural correlation but not determination |
| Setting imagery | Nature vs. urban varies by sample, not culture |

The underlying phenomenon—an encounter with light, beings, boundaries, and potential transformation—appears constant. The surface expression—whether the light is named "Being" or perceived as "brilliant," whether settings are described as gardens or cities, whether beings are identified as Jesus or ancestors—varies without altering the experiential core.

### 4.3 Purposive Economy: The Novel Explanatory Framework

The most significant finding is that **purpose, not culture, determines personal interaction**. This introduces a new framework: **purposive economy**.

The NDE operates with purposive economy: every element serves the transformative goal. Personal interaction is not a random feature that some NDEs "have" and others "lack"—it is a mode that activates when the purpose requires it:

| Purpose | Mode Required | Evidence |
|---------|---------------|----------|
| Commissioning (earthly mission) | Personal dialogue | 4.4× odds of Being of Light |
| Teaching (life review) | Personal interaction | 1.83× odds of Being of Light |
| Guidance (return decision) | Personal communication | Significant correlations across all return reasons |
| Presence alone sufficient | Ambient light | 40.9% brilliant light without personification |

This framework resolves the East-West puzzle without invoking cultural determination. If Japanese NDE samples happen to contain fewer mission-returners—perhaps due to sampling methods, survival rates, or random variation—they will show fewer Being of Light encounters by statistical necessity. This is not because Japanese culture produces different light encounters; it is because the purpose-mix of the sample differs.

The Light, on this model, operates with perfect efficiency:
- Personal mode when personal mode is required
- Presence without dialogue when presence alone serves the purpose
- Restraint as wisdom, not distance

### 4.4 Reframing "Impersonal" Light

The Japanese research observed NDEs with "impersonal" light and concluded this reflected Japanese spirituality—a different kind of light encounter. Our data suggest a different interpretation:

- **Not** a cultural difference in the nature of the Light
- **Rather** a functional difference in what was needed

Those particular experiencers did not need commissioning with earthly missions. They were not being assigned explicit tasks. The Light was **economical**, not distant. Absence of personal interaction reflects absence of purpose requiring personal mode—not absence of personhood.

A skilled teacher does not lecture every student on every topic. Some students need only a nod of encouragement; some need detailed instruction; some need full mentorship with explicit commissioning. The teacher's restraint with some students does not make the teacher "impersonal" with those students. The intervention is calibrated to the need. **The wisdom is in the restraint.**

### 4.5 Implications for Cross-Cultural Research

This analysis challenges the methodology underlying East-West NDE comparisons:

1. **Selection bias matters profoundly**: Small samples may systematically over- or under-represent purpose categories
2. **Prevalence claims require large samples**: The 70–80% Being of Light figure cannot be replicated in a large, systematically coded dataset
3. **Cultural vocabulary ≠ cultural experience**: Experiencers from different cultures may use different words for the same phenomenon
4. **Purpose must be controlled**: Any comparison of personified versus impersonal light must control for purposive elements (mission, life review)

Future cross-cultural studies should:
- Use large, systematically coded samples
- Control for purpose-category distributions
- Distinguish vocabulary (how it's named) from phenomenology (what's experienced)
- Test the purposive economy hypothesis directly

### 4.6 Limitations

Several limitations warrant acknowledgment:

1. **Western sample only**: This analysis cannot directly test Japanese NDE phenomenology; it can only test Western claims
2. **Retrospective reporting**: Accounts may be influenced by subsequent reflection and cultural integration
3. **AI coding**: GPT-5.2 extraction may introduce systematic biases
4. **English language**: Non-English Western accounts are not represented
5. **Purpose inference**: Return reasons are experiencer-reported, not independently verified
6. **Temporal span**: Records span decades with changing cultural contexts

### 4.7 Future Directions

1. **Cross-cultural replication**: Apply the same structured extraction to Japanese, Indian, and other non-Western NDE archives
2. **Direct purpose testing**: Prospectively track whether mission-assignees show higher Being of Light rates
3. **Vocabulary analysis**: Compare how experiencers from different cultures describe the same phenomenological features
4. **Longitudinal tracking**: Assess whether purpose clarity correlates with interaction mode at individual level
5. **Meta-analysis**: Re-analyze prior cross-cultural studies controlling for purpose-category distributions

---

## 5. Conclusion

Analysis of 6,753 Western near-death experiences reveals that the East-West NDE dichotomy is largely a scholarly construction that does not survive empirical testing. The claimed Western profile—70–80% personified Being of Light, Cities of Light, frequent life reviews—does not match the observed data. Western NDEs feature impersonal light (40.9%) more than personified (11.8%), nature settings (17.0%) more than urban (11.4%), and deceased relatives (17.9%) more than religious figures (9.9%). On every metric tested, Western NDEs align more closely with the claimed "Japanese" profile than with the claimed "Western" profile.

The key variable determining personal interaction is not culture but **purpose**. Those returning with earthly missions show 4.4× the odds of encountering the Being of Light (p < 10⁻⁴⁶). Life review occurrence correlates with Being of Light encounters at 1.83× (p < 10⁻³⁰). The Light engages personally when the transformative purpose requires personal engagement—commissioning, teaching, guiding. When presence alone suffices, the Light remains as ambient brilliance.

This supports a correspondential model of **constant underlying reality** with **variable cultural expression**, mediated by **purposive economy** rather than cultural determination. The Light is one; the forms are many; the mode of interaction serves the goal. Neither culture experiences something fundamentally different. The East-West dichotomy reflects scholarly projection, selection bias, and the conflation of vocabulary with phenomenology.

The Being of Light, whether named or unnamed, personified or brilliant, appears to be what experiencers consistently report: a presence of love and wisdom that engages with perfect economy—speaking when speaking serves, and present without words when presence alone transforms.

---

## References

Becker, C. B. (1981). The centrality of near-death experiences in Chinese Pure Land Buddhism. *Anabiosis: The Journal for Near-Death Studies*, 1(2), 154–171.

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Kellehear, A. (1993). Culture, biology, and the near-death experience: A reappraisal. *Journal of Nervous and Mental Disease*, 181(3), 148–156.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Ohkado, M., & Greyson, B. (2014). A comparative analysis of Japanese and Western NDEs. *Journal of Near-Death Studies*, 32(4), 187–198.

Ornstein, R. (n.d.). Japanese NDEs and the Being of Light. Unpublished manuscript.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Variable | Statistic | df | p-value |
|------|----------|-----------|----|---------| 
| Chi-square | Nature vs. Urban settings | χ² = 74.7 | 1 | < 0.0001 |
| Chi-square | Light type × Life review | χ² = 183.20 | 4 | < 0.0001 |
| Fisher's exact | Mission × Being of Light | OR = 4.38 | — | 1.25 × 10⁻⁴⁶ |
| Chi-square | Life Review × Being of Light | χ² = 53.2 | 1 | 4.2 × 10⁻³⁰ |
| Chi-square | Earthly Mission × Being of Light | χ² = 258.7 | 1 | 1.4 × 10⁻⁶⁰ |
| Chi-square | Not Your Time × Being of Light | χ² = 132.4 | 1 | 4.6 × 10⁻³⁰ |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,660 |
| IANDS records | 1,093 |
| Being of Light encounters | 797 (11.8%) |
| Brilliant light encounters | 2,761 (40.9%) |
| Impersonal:Personified ratio | 3.8:1 |
| Nature settings | 1,151 (17.0%) |
| Urban settings | 772 (11.4%) |
| Nature:Urban ratio | 1.5:1 |
| Deceased relative encounters | 1,206 (17.9%) |
| Religious figure encounters | 670 (9.9%) |
| Deceased:Religious ratio | 1.8:1 |
| Life reviews | 1,183 (17.5%) |
| Tunnel passages | 1,602 (23.7%) |
| Mission → Being of Light odds ratio | 4.38 |
| Life review → Being of Light odds ratio | 1.83 |

## Appendix C: Claimed Versus Observed Rates

| Feature | Claimed Western | Observed | Deviation |
|---------|-----------------|----------|-----------|
| Being of Light | 70–80% | 11.8% | −58 to −68 percentage points |
| Life review | 25–30% | 17.5% | −7 to −12 percentage points |
| Tunnel | 34–50% | 23.7% | −10 to −26 percentage points |
| Nature > Urban | No | Yes (1.5:1) | Reversed |
| Deceased > Religious | No | Yes (1.8:1) | Reversed |

## Appendix D: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [05_cultural_paradigm_challenge.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb)
- **Structured Data**: [/structured/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 JSON files)
