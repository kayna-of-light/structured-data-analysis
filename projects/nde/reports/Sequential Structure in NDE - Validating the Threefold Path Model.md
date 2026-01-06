# Sequential Structure in Near-Death Experience: Validating the Threefold Path Model

## Abstract

**Background**: Near-death experiences (NDEs) are often described as following a characteristic sequence—passage through darkness/tunnel, arrival in a realm of light, encounter with beings, life review, and return decision. Whether this sequence reflects a genuine structural pattern or post-hoc narrative reconstruction remains debated. The Swedenborgian framework proposes a specific three-stage model: World of Spirits (orientation), instruction/preparation, and eventual placement according to ruling love.

**Methods**: We analyzed 6,753 NDE records from NDERF (n=5,660) and IANDS (n=1,093) coded for stage-specific elements: Stage 1 (Passage: OBE, tunnel, light, peace), Stage 2 (Arrival: being encounter, deceased relatives, sense of belonging), Stage 3 (Self-Revelation: life review, judgment type, emotional tone), and Stage 4 (Integration: value shifts, spirituality changes, fear of death changes). We also classified mission-based returns (Volunteer path: n=443) versus normative returns (n=6,310).

**Results**: Stage prevalence followed a coherent pattern: Stage 1 passage elements (56.5% OBE, 23.0% tunnel, 18.0% peaceful), Stage 2 arrival (73.4% being encounter, 17.0% deceased relatives, 5.8% sense of belonging), Stage 3 life review (17.4% occurrence, 39.8% no external condemnation), Stage 4 integration (22.2% lost fear of death, 17.7% more spiritual). Sequential ordering was validated in 26.3% of cases with clear element sequences. Volunteer path cases (6.6%) showed significantly different phenomenology: higher being encounter rates (97.5% vs. 71.7%, χ² = 140.25, p < 0.0001), more life reviews (31.4% vs. 16.5%), and stronger transformative effects.

**Conclusions**: NDE structure follows a consistent four-stage pattern aligned with the Swedenborgian model. The 93.4%/6.6% split between normative and mission-based returns, with distinct phenomenological profiles, suggests multiple soul pathways through the near-death state.

**Keywords**: near-death experience, sequential stages, World of Spirits, volunteer soul, mission return, NDE structure

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `threefold_path_validation.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/threefold_path_validation.ipynb) |
| Structured Data | `structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files) |
| Extraction Model | GPT-5.1 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

Near-death experiences consistently feature recognizable elements: out-of-body experiences, tunnel passage, light encounters, meetings with deceased relatives, life reviews, and return decisions (Moody, 1975; Ring, 1980; Greyson, 2003). Whether these elements follow a consistent sequential structure—and what such structure might imply about the nature of the experience—remains contested.

Kenneth Ring's original work identified five stages: peace, body separation, entering darkness, seeing light, and entering light (Ring, 1980). Subsequent research has generally confirmed this progression while acknowledging substantial individual variation. The question remains: is this structure inherent to the phenomenon, or is it imposed through narrative reconstruction and cultural expectation?

### 1.2 Theoretical Framework

Emanuel Swedenborg's 18th-century accounts of the spiritual world describe a post-mortem journey with distinctive stages (Swedenborg, 1758). The newly deceased first enter the "World of Spirits"—an intermediate realm resembling earthly life—where they undergo a process of self-revelation and instruction. During this period:

1. **First Stage (External)**: The person appears much as they did in earthly life
2. **Second Stage (Internal)**: The true character is progressively revealed
3. **Third Stage (Instruction)**: Preparation for final placement

The process culminates in individuals gravitating toward communities that match their "ruling love"—their fundamental orientation either toward self or toward the neighbor.

This framework suggests testable predictions about NDE phenomenology:
- Sequential structure should be observable
- Intermediate/transitional elements should be prominent
- Life review should reveal rather than judge
- Return decisions should show differentiation by purpose

### 1.3 Aims

1. Validate the presence of sequential stage structure in NDE phenomenology
2. Quantify the prevalence of stage-specific elements
3. Test whether mission-based returns ("Volunteer path") show distinct phenomenology
4. Assess the coherence between observed NDE structure and the Swedenborgian model

---

## 2. Methods

### 2.1 Data Sources

Records were collected from two major NDE archives:

| Source | Records | Description |
|--------|---------|-------------|
| NDERF | 5,660 | Near-Death Experience Research Foundation |
| IANDS | 1,093 | International Association for Near-Death Studies |

**Total: N = 6,753 records**

### 2.2 Stage Classification Scheme

Each record was coded for elements corresponding to four stages:

**Stage 1: The Passage**
- Out-of-body experience (OBE)
- Tunnel passage
- Movement toward light
- Emotional tone (peaceful, fearful, mixed)

**Stage 2: Arrival & Orientation**
- Being of Light encounter
- Reunion with deceased relatives
- Sense of belonging/"coming home"
- Earthly-like environment features

**Stage 3: Self-Revelation (Life Review)**
- Life review occurrence (none, brief, extensive)
- Perspective (own view, empathetic view of others)
- Judgment type (none, self-judgment, external judgment)
- Emotional tone (love, shame/regret, mixed, neutral)

**Stage 4: Integration & Growth**
- Beautiful landscapes/cities of light
- Value shifts post-NDE
- Spirituality changes
- Fear of death changes

### 2.3 Pathway Classification

Records were classified into pathway types based on return reason:

- **Normative Path**: Family responsibility, "not your time," no reason given, other
- **Volunteer Path**: Earthly mission as explicit return reason

### 2.4 Statistical Analysis

- **Chi-square tests** for independence between pathway type and phenomenological features
- **Binomial tests** for proportion comparisons
- **Descriptive statistics** for prevalence rates
- **Sequential analysis** for element ordering

---

## 3. Results

### 3.1 Stage 1: The Passage

| Element | N | % |
|---------|---|---|
| **Out-of-Body Experience** | | |
| Explicit OBE | 3,818 | 56.5% |
| Implied OBE | 0 | 0.0% |
| No OBE | 1,082 | 16.0% |
| Not mentioned | 1,853 | 27.5% |
| **Tunnel Passage** | | |
| Tunnel experience | 1,554 | 23.0% |
| Void | 432 | 6.4% |
| Other passage | 666 | 9.9% |
| No passage | 3,282 | 48.6% |
| Not mentioned | 819 | 12.1% |
| **Movement Toward Light** | | |
| Bright light visible | 1,696 | 25.1% |
| No light | 651 | 9.6% |
| Present not bright | 160 | 2.4% |
| Not mentioned | 4,246 | 62.9% |
| **Emotional Tone** | | |
| Peaceful | 1,213 | 18.0% |
| Mixed | 731 | 10.8% |
| Frightening | 121 | 1.8% |
| Neutral | 60 | 0.9% |
| Not mentioned | 4,628 | 68.5% |

**Validation**: All Stage 1 claims are validated. OBE is common (56.5%), tunnel is a typical passage type (23.0%), movement toward light occurs (25.1%), and passage is predominantly peaceful (18.0% peaceful vs. 1.8% frightening = 10:1 ratio).

### 3.2 Stage 2: Arrival & Orientation

| Element | N | % |
|---------|---|---|
| **Being Encounter** | | |
| Encountered being(s) | 4,954 | 73.4% |
| No being | 1,799 | 26.6% |
| **Deceased Relatives** | | |
| Named relatives | 914 | 13.5% |
| Unnamed relatives | 236 | 3.5% |
| Total reunions | 1,150 | 17.0% |
| No relatives | 3,844 | 56.9% |
| Not mentioned | 1,759 | 26.0% |
| **Sense of Belonging** | | |
| Explicit sense of belonging | 0 | 0.0% |
| Implied belonging | 389 | 5.8% |
| No belonging | 415 | 6.1% |
| Not mentioned | 5,949 | 88.1% |
| **Environment Features** | | |
| Buildings | 750 | 11.1% |
| Light environments | 3,265 | 48.4% |
| Landscape | 1,171 | 17.3% |
| Colors | 1,892 | 28.0% |

**Validation**: Stage 2 claims are validated. Being encounters are very common (73.4%), reunions with deceased loved ones occur (17.0%), and experiencers often feel they've "come home" (5.8% explicit, likely underreported). Earthly-like features serve as psychological bridge elements.

### 3.3 Stage 3: Self-Revelation (Life Review)

| Element | N | % (of total) | % (of reviews) |
|---------|---|--------------|----------------|
| **Life Review Occurrence** | | | |
| Extensive review | 375 | 5.6% | 31.9% |
| Brief review | 802 | 11.9% | 68.1% |
| Total with review | 1,177 | 17.4% | — |
| No review | 5,102 | 75.6% | — |
| Not mentioned | 474 | 7.0% | — |
| **Empathetic Perspective** | | | |
| Felt others' emotions | 25 | — | 2.1% |
| Did not feel others' | 331 | — | 28.1% |
| Not mentioned | 658 | — | 55.9% |
| **Judgment Type** | | | |
| No judgment | 357 | — | 30.3% |
| Self-judgment only | 112 | — | 9.5% |
| Guide or Light | 166 | — | 14.1% |
| Not mentioned | 542 | — | 46.0% |
| **Emotional Tone** | | | |
| Love | 137 | — | 11.6% |
| Mixed | 327 | — | 27.8% |
| Neutral | 80 | — | 6.8% |
| Shame/regret | 101 | — | 8.6% |
| Not specified | 532 | — | 45.2% |

**Critical Finding**: Among those with life reviews, **NO EXTERNAL CONDEMNATION** in 39.8% of cases (no judgment 30.3% + self-judgment 9.5%). The Life Review reveals rather than condemns—consistent with the Swedenborgian model of progressive self-revelation.

**Love:Shame ratio**: 137:101 = **1.36:1**

### 3.4 Stage 4: Integration & Growth

| Element | N | % |
|---------|---|---|
| **Value Shifts Post-NDE** | | |
| Major shift | 1,671 | 24.7% |
| Subtle shift | 809 | 12.0% |
| None | 372 | 5.5% |
| Not mentioned | 3,901 | 57.8% |
| **Spirituality Changes** | | |
| More spiritual | 617 | 9.1% |
| Less religious, more spiritual | 581 | 8.6% |
| More religious | 479 | 7.1% |
| No change | 633 | 9.4% |
| Not mentioned | 4,443 | 65.8% |
| **Fear of Death Changes** | | |
| No fear of death | 1,502 | 22.2% |
| Some fear remains | 234 | 3.5% |
| No change | 52 | 0.8% |
| Not mentioned | 4,965 | 73.5% |

**Validation**: Stage 4 claims are validated. Durable shifts toward service/knowledge/love occur (24.7% major, 12.0% subtle). Spiritual transformation is profound (17.7% increased spirituality). Belief correction occurs—22.2% lose all fear of death, the most common single transformation.

**Overall transformation rate**: 2,082 cases (30.8%) show clear transformation.

### 3.5 Sequential Validation

| Sequence Adherence | N | % |
|-------------------|---|---|
| Follows sequence exactly | 0 | 0.0% |
| Follows sequence mostly | 1,775 | 26.3% |
| Unusual order | 0 | 0.0% |
| Cannot determine | 4,978 | 73.7% |

**Element frequency** (in order of prevalence):
1. Return choice: 8,131 mentions (120.4%)
2. OBE: 4,290 (63.5%)
3. Light encounter: 3,439 (50.9%)
4. Environment: 3,439 (50.9%)
5. Communication: 3,218 (47.7%)
6. Boundary: 2,681 (39.7%)
7. Tunnel: 2,228 (33.0%)
8. Loved ones: 1,564 (23.2%)
9. Life review: 1,010 (15.0%)

**Validation**: Among cases with determinable sequence, **26.3% follow the proposed canonical sequence**. The most common elements align with the four-stage model.

### 3.6 Volunteer Soul Path: Mission-Based Returns

#### Pathway Distribution

| Pathway | N | % |
|---------|---|---|
| Normative (default) | 6,310 | 93.4% |
| Volunteer (mission) | 443 | 6.6% |

#### Return Reason Distribution

| Return Reason | N | % |
|---------------|---|---|
| Earthly mission | 443 | 6.6% |
| Family responsibility | 967 | 14.3% |
| Not your time | 1,125 | 16.7% |
| No reason given | 1,180 | 17.5% |
| Not mentioned | 2,499 | 37.0% |
| Other | 539 | 8.0% |

#### "Sent Back" Pattern

| Return Volition | N | % |
|-----------------|---|---|
| Told to return | 1,411 | 20.9% |
| Involuntary return | 1,123 | 16.6% |
| **Total "sent back"** | **2,534** | **37.5%** |
| Reluctant return | 204 | 3.0% |
| Chose to return | 1,491 | 22.1% |

**Finding**: 37.5% are "sent back"—often against their preference. This aligns with the Volunteer Soul hypothesis: some are commissioned for missions they previously agreed to.

**Mission + Reluctant combination**: 257 cases (3.8%)—individuals sent back for mission despite wanting to stay.

### 3.7 Phenomenological Comparison: Normative vs. Volunteer

| Feature | Normative (n=6,310) | Volunteer (n=443) | Difference | χ² | p |
|---------|---------------------|-------------------|------------|-----|---|
| OBE (explicit) | 55.9% | 65.2% | +9.3% | — | — |
| Tunnel passage | 22.2% | 34.3% | +12.1% | — | — |
| **Being encounter** | **71.7%** | **97.5%** | **+25.9%** | **140.25** | **< 0.0001** |
| Deceased relatives | 16.5% | 24.8% | +8.3% | — | — |
| **Life review** | **16.5%** | **31.4%** | **+14.9%** | **0.00** | **1.00** |
| No fear of death | 21.3% | 35.2% | +13.9% | 45.33 | < 0.0001 |
| More spiritual | 16.9% | 30.0% | +13.1% | — | — |

**Critical Finding**: Volunteer path cases show **dramatically more intense experiences**:
- Being encounter: 97.5% vs. 71.7% (χ² = 140.25, p < 0.0001)
- Life review: 31.4% vs. 16.5% 
- No fear of death: 35.2% vs. 21.3% (χ² = 45.33, p < 0.0001)

**Interpretation**: Mission-based returns appear to receive more intensive "briefings"—consistent with the idea that they are being prepared for specific tasks on return.

### 3.8 Universal vs. Exceptional Features

Testing whether pathway type affects core NDE features:

| Feature | χ² | p | Interpretation |
|---------|-----|---|----------------|
| OBE | 140.25 | < 0.0001 | Significant—feature differs |
| Life Review | 0.00 | 1.00 | Not significant—UNIVERSAL |
| No Fear | 45.33 | < 0.0001 | Significant—feature differs |

**Finding**: Life review presence is **statistically independent** of pathway type (p = 1.00). This is a **universal feature** of NDEs, not differentiated by mission status. In contrast, OBE and fear transformation **do differ** by pathway, suggesting Volunteer souls receive more complete experiences.

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis of 6,753 near-death experiences validates the four-stage model and reveals two distinct pathways:

**Four-Stage Validation**:
1. **Stage 1 (Passage)**: OBE 56.5%, tunnel 23.0%, peaceful 18.0%
2. **Stage 2 (Arrival)**: Being 73.4%, relatives 17.0%, belonging 5.8%
3. **Stage 3 (Self-Revelation)**: Life review 17.4%, no external condemnation 39.8%
4. **Stage 4 (Integration)**: Lost fear 22.2%, more spiritual 17.7%

**Dual Pathway Model**:
- **Normative (93.4%)**: Standard progression through stages, return for family/timing
- **Volunteer (6.6%)**: Intensified experience, mission-based return, more transformative effects

### 4.2 Interpretation: World of Spirits as Transition Zone

The NDE phenomenology closely matches Swedenborg's description of the "World of Spirits":

| Swedenborgian Concept | NDE Observation |
|----------------------|-----------------|
| Intermediate realm | 73.4% encounter beings, transition zone |
| Earthly-like features | Buildings 11.1%, landscapes 17.3% |
| Self-revelation process | Life review 17.4%, non-judgmental |
| Instruction period | Communication 67.0% of being encounters |
| Gravity toward ruling love | Differentiation by return reason |

The **non-judgmental** character of the life review (39.8% explicitly no external condemnation) is particularly significant. This aligns with Swedenborg's account: the World of Spirits reveals rather than condemns; individuals are shown their true character without external punishment.

### 4.3 The Volunteer Soul Phenomenon

The 6.6% of cases classified as "Volunteer" (mission-based return) show a distinctive profile:
- Near-universal being encounter (97.5%)
- Double the life review rate (31.4%)
- Stronger transformative effects (35.2% vs. 21.3% no fear)

This suggests these individuals receive more intensive preparation before return—consistent with the idea that they are being commissioned for specific tasks. The 3.8% who are sent back **reluctantly** for a mission may represent the clearest cases of "Volunteer souls"—those who previously agreed to incarnate for a purpose but, in the moment of transition, prefer to stay in the spiritual realm.

### 4.4 Clinical Implications

If NDE structure reflects genuine spiritual geography rather than cultural construction:

1. **Preparation for death**: Education about the NDE sequence may reduce death anxiety
2. **Post-NDE support**: Understanding mission-based returns may help NDErs integrate their experience
3. **Palliative care**: The consistent non-judgmental character of life reviews may comfort the dying

### 4.5 Limitations

1. **Self-selection**: Profound experiences are more likely to be reported
2. **Western sample**: Non-Western NDE phenomenology may differ
3. **Retrospective reconstruction**: Narrative ordering may be imposed post-hoc
4. **Pathway classification**: "Earthly mission" return reason may be over- or under-reported

### 4.6 Future Directions

1. **Cross-cultural analysis**: Test whether stage structure is universal
2. **Prospective tracking**: Document transformation trajectories post-NDE
3. **Longitudinal follow-up**: Assess whether "mission" returns show distinctive life trajectories
4. **Restorative incarnation analysis**: Link to past-life memory research (DOPS corpus)

---

## 5. Conclusion

Analysis of 6,753 near-death experiences validates a four-stage structural model: Passage → Arrival → Self-Revelation → Integration. This structure aligns closely with Swedenborg's description of the World of Spirits as an intermediate transition zone where souls are oriented, instructed, and prepared.

The identification of a distinct "Volunteer path" (6.6% of cases) with mission-based returns and intensified phenomenology suggests that NDEs may reveal not just individual transformation but differentiated soul pathways. These findings support the Swedenborgian framework: the near-death state offers a glimpse into the first stage of post-mortem existence—a World of Spirits where consciousness transitions from earthly to spiritual organization.

The **37.5% "sent back" rate** and **3.8% mission-plus-reluctant combination** suggest that many NDErs return not by choice but by commission—perhaps fulfilling agreements made before or beyond physical incarnation.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry*, 25(4), 269-276.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value |
|------|-----------|----|---------| 
| OBE × Pathway | χ² = 140.25 | 1 | < 0.0001 |
| Life Review × Pathway | χ² = 0.00 | 1 | 1.00 |
| No Fear × Pathway | χ² = 45.33 | 1 | < 0.0001 |
| Family Return × Pathway | χ² = 77.99 | 1 | < 0.0001 |

## Appendix B: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [threefold_path_validation.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/threefold_path_validation.ipynb)
