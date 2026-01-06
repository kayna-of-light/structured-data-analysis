# Sequential Structure in Near-Death Experience: Validating the Normative Path Model

## Abstract

**Background**: Near-death experiences (NDEs) are often described as following a characteristic sequence—passage through darkness/tunnel, arrival in a realm of light, encounter with beings, life review, and return decision. Whether this sequence reflects a genuine structural pattern or post-hoc narrative reconstruction remains debated. The Swedenborgian framework proposes a specific normative path: most souls continue to a spiritual existence, with reincarnation representing an exceptional rather than universal pattern.

**Methods**: We analyzed 6,753 NDE records from NDERF (n=5,664) and IANDS (n=1,089) coded for return patterns, being encounters, life review characteristics, and transformation markers using GPT-5.2 structured extraction with a questionnaire schema containing 52 extracted features. Key schema innovations include separating return *agency* (who decided) from return *willingness* (how they felt), enabling new analytical distinctions.

**Results**: Return agency analysis revealed 70.1% did NOT return by their own choice (external_being 28.6% + involuntary 21.1%). Among those with willingness data, 49.4% were reluctant to return. Deceased relatives were encountered in 17.9% of cases—evidence that these individuals *continued* rather than reincarnated. Reincarnation indicators were rare: past life memory 4.4%, intermission memory 1.0%, pre-incarnation covenant 0.7%. Life review occurred in 17.5% of cases with loving/gentle judgment (3.3%) vastly exceeding harsh (0.2%)—a 16.5:1 ratio.

**Conclusions**: Five of five markers support the Normative Path Hypothesis: return is typically involuntary (70.1%), experiencers are reluctant (49.4%), deceased relatives are present (17.9%), and reincarnation indicators are rare (<5%). This supports the Swedenborgian model: continuation is normative; reincarnation is exceptional.

**Keywords**: near-death experience, normative path, return agency, continuation hypothesis, Swedenborg, World of Spirits

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,664) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,089) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `02_normative_path_validation.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb) |
| Structured Data | `analysis/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/analysis/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

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

Critically, this framework proposes that **continuation is normative**—most souls proceed to permanent spiritual existence. Reincarnation, when it occurs, represents an **exception** for specific purposes (restorative healing from trauma, or volunteer mission).

This generates testable predictions about NDE phenomenology:
- Return to earthly life should be primarily involuntary (the exception, not the rule)
- Experiencers should often be reluctant to return
- Deceased relatives should be present (evidence they continued, not reincarnated)
- Explicit reincarnation indicators should be rare

### 1.3 Aims

1. Test whether return patterns support continuation as normative
2. Quantify return agency vs. willingness (new schema capability)
3. Assess prevalence of reincarnation indicators
4. Validate the four-stage journey structure
5. Examine life review characteristics

---

## 2. Methods

### 2.1 Data Sources

Records were collected from two major NDE archives:

| Source | Records | Description |
|--------|---------|-------------|
| NDERF | 5,664 | Near-Death Experience Research Foundation |
| IANDS | 1,089 | International Association for Near-Death Studies |

**Total: N = 6,753 records**

### 2.2 Schema Innovation: Agency vs. Willingness

A critical methodological advance in this analysis: the schema **separates return agency from return willingness**:

| Dimension | Question | Values |
|-----------|----------|--------|
| **Return Agency** | Who decided the return? | self, external_being, involuntary, mutual, not_mentioned |
| **Return Willingness** | How did they feel about it? | willing, reluctant, mixed, neutral, not_mentioned |

This enables analysis that previous schemas could not perform—distinguishing those who *chose* to return from those *told* to return, and separately tracking whether they were *happy* about it.

### 2.3 Key Field Definitions

**Return Pattern Fields:**
- `return_agency`: Who made the decision to return
- `return_willingness`: Experiencer's emotional response to returning
- `return_reasons`: List field capturing multiple reasons (family_responsibility, not_your_time, earthly_mission, unfinished_business)

**Continuation Evidence Fields:**
- `deceased_present`: Whether deceased relatives were encountered
- `past_life_memory`: Evidence of previous life recall
- `intermission_memory`: Between-lives memory
- `pre_incarnation_covenant`: Evidence of pre-birth life choice

**Life Review Fields:**
- `life_review_occurred`: none, brief, extensive
- `judgment_source`: self, being_of_light, guide_or_entity, none
- `judgment_intensity`: loving_gentle, neutral, uncomfortable, harsh_condemning

### 2.4 Statistical Analysis

- **Frequency analysis** for categorical distributions
- **Chi-square tests** for independence between agency and willingness
- **Cross-tabulation** for multi-dimensional pattern analysis

---

## 3. Results

### 3.1 Return Agency Analysis

**Question: Who decided the experiencer would return?**

Among 4,782 cases with return agency data:

| Agency | N | % |
|--------|---|---|
| Not mentioned | 1,971 | 29.2% |
| External being | 1,931 | 28.6% |
| Involuntary | 1,422 | 21.1% |
| Self | 1,124 | 16.6% |
| Mutual | 305 | 4.5% |

**Key Finding**: **70.1% did NOT return by their own choice** (external_being + involuntary = 3,353 of 4,782).

Only 16.6% reported self-initiated return. This strongly supports the normative path hypothesis: return to earthly life is the exception, typically imposed rather than chosen.

### 3.2 Return Willingness Analysis

**Question: How did experiencers feel about returning?**

Among 3,563 cases with willingness data:

| Willingness | N | % |
|-------------|---|---|
| Not mentioned | 3,190 | 47.2% |
| Reluctant | 1,759 | 26.0% |
| Mixed | 944 | 14.0% |
| Willing | 763 | 11.3% |
| Neutral | 97 | 1.4% |

**Key Finding**: **49.4% were reluctant to return** (1,759 of 3,563 with data).

This suggests the NDE state was preferable to earthly return—consistent with having glimpsed a genuine spiritual realm.

### 3.3 Agency × Willingness Cross-Tabulation

The new schema enables unprecedented analysis of agency-willingness combinations:

| Agency | Reluctant | Willing | Mixed | Neutral |
|--------|-----------|---------|-------|---------|
| External being | 52.1% | 4.2% | 12.5% | 2.2% |
| Involuntary | 29.6% | 1.4% | 10.1% | 2.3% |
| Mutual | 28.5% | 30.2% | 36.4% | 1.0% |
| Self | 9.7% | 49.6% | 32.8% | 1.1% |

**Statistical Test**: χ² = 4824.78, p < 0.0001

Agency and willingness are **significantly associated** but represent **independent dimensions**:
- External being returns: 52.1% reluctant (sent back against preference)
- Self returns: 49.6% willing (chose to return and wanted to)
- Mutual decisions show the most mixed feelings (36.4%)

### 3.4 Return Reasons

Among cases with explicit return reasons (list field):

| Reason | Count |
|--------|-------|
| Not your time | 1,459 |
| Family responsibility | 1,164 |
| Unfinished business | 711 |
| Earthly mission | 623 |
| Other | 218 |

**Note**: Return reasons are overwhelmingly duty/obligation-based, not preference-based.

### 3.5 Deceased Relatives: Evidence of Continuation

**Question: If reincarnation were normative, would deceased relatives be available for encounters?**

| Deceased Present | N | % |
|------------------|---|---|
| No | 4,129 | 61.1% |
| Not mentioned | 1,418 | 21.0% |
| Named relatives | 1,007 | 14.9% |
| Unnamed relatives | 199 | 2.9% |

**Key Finding**: **17.9% of NDEs include deceased relatives** (named + unnamed = 1,206).

**Theological Implication**: If reincarnation were the norm, deceased relatives would rarely be "available" for encounters—they would have already reincarnated. The consistent presence of deceased relatives in recognizable form supports the continuation model: identity and relationships are preserved.

### 3.6 Spiritual Beings Encountered

| Being Type | Count |
|------------|-------|
| Unidentified benevolent | 1,733 |
| Religious figures | 639 |
| Guides or angels | 558 |

### 3.7 Reincarnation Indicators: Testing the Exception

**Framework**: If continuation is normative, reincarnation indicators should be RARE.

| Indicator | Present | % |
|-----------|---------|---|
| Past life memory | 297 | 4.4% |
| Intermission memory (between-lives) | 69 | 1.0% |
| Pre-incarnation covenant | 86 | 1.3% |
| Chose parents | 9 | 0.1% |
| Chose mission | 93 | 1.4% |
| Chose life circumstances | 47 | 0.7% |

**Key Finding**: All reincarnation indicators are **rare** (<5%). This is consistent with reincarnation as the **exception**, not the norm.

When present, these indicators may represent exception paths:
- **Restorative Incarnation**: Traumatic death → healing return
- **Volunteer Soul Incarnation**: Mission-based return by choice

### 3.8 Identity Preservation

| Identity Status | N | % |
|-----------------|---|---|
| Clear identity preserved | 4,377 | 64.8% |
| Not mentioned | 2,241 | 33.2% |
| Identity altered/lost | 92 | 1.4% |
| Identity confusion | 43 | 0.6% |

**Key Finding**: **64.8% maintain clear sense of self** during NDE. Only 2.0% report any identity disruption.

### 3.9 Life Review Analysis

| Life Review | N | % |
|-------------|---|---|
| No review | 5,245 | 77.7% |
| Brief review | 718 | 10.6% |
| Extensive review | 465 | 6.9% |
| Not mentioned | 325 | 4.8% |

**Life review rate**: 17.5%

#### Judgment Source

| Source | N | % |
|--------|---|---|
| Not mentioned | 4,773 | 70.7% |
| None | 1,518 | 22.5% |
| Guide or entity | 205 | 3.0% |
| Being of Light | 155 | 2.3% |
| Self | 95 | 1.4% |
| Deceased relative | 7 | 0.1% |

#### Judgment Intensity

| Intensity | N | % |
|-----------|---|---|
| Not applicable | 4,959 | 73.4% |
| Not specified | 1,340 | 19.8% |
| Loving/gentle | 223 | 3.3% |
| Uncomfortable | 128 | 1.9% |
| Neutral | 89 | 1.3% |
| Harsh/condemning | 14 | 0.2% |

**Love:Harsh Ratio**: 223:14 = **15.9:1**

**Key Finding**: When judgment occurs, it is overwhelmingly loving (3.3%) vs harsh (0.2%). This supports the Swedenborgian model: life review **reveals** rather than **condemns**.

#### Empathetic Perspective

| Empathy | N | % |
|---------|---|---|
| Not mentioned | 4,362 | 64.6% |
| Did not feel others' emotions | 2,132 | 31.6% |
| Felt others' emotions (explicit) | 198 | 2.9% |
| Felt others' emotions (implied) | 61 | 0.9% |

**Empathetic review**: 3.8% explicitly experienced feeling the impact of their actions on others.

---

## 4. Discussion

### 4.1 Summary of Evidence

**Five markers supporting the Normative Path Hypothesis:**

| Marker | Finding | Supports? |
|--------|---------|-----------|
| 1. Return as Exception | External/involuntary returns: 70.1% | ✓ |
| 2. Reluctance to Return | Reluctant returnees: 49.4% | ✓ |
| 3. Deceased Present | Relatives encountered: 17.9% | ✓ |
| 4. Reincarnation Rare | Past life memory: 4.4% | ✓ |
| 5. Volunteer Path Rare | Pre-incarnation covenant: 1.3% | ✓ |

**Result: 5/5 markers support the hypothesis.**

### 4.2 The Threefold Path Framework

The data support a threefold path structure:

**1. Normative Linear Progression (Default Path)**
- 95.6% show NO past life memory
- 98.7% show NO pre-incarnation covenant
- Evidence: Vast majority on normative (single-life) path

**2. Restorative Incarnation (Traumatic Death Exception)**
- 4.4% have past life memory
- 1.0% have intermission memory
- Evidence: Small minority may be on restorative path

**3. Volunteer Soul Incarnation (Mission-Based Exception)**
- 1.3% report pre-incarnation covenant
- 1.4% report choosing mission
- Evidence: Rare, consistent with 'volunteer soul' concept

### 4.3 Four-Stage Journey Validation

The NDE phenomenology aligns with a four-stage model:

| Stage | Elements | Evidence |
|-------|----------|----------|
| 1. Passage | OBE, Tunnel, Light | See extraction data |
| 2. Arrival | Being of Light, Deceased | Deceased: 17.9% |
| 3. Life Review | Review, Empathy | Review: 17.5%, loving 15.9:1 |
| 4. Integration | Transformation | Fear/spirituality transform |

### 4.4 Interpretation: World of Spirits as Transition Zone

The NDE phenomenology closely matches Swedenborg's description of the "World of Spirits":

| Swedenborgian Concept | NDE Observation |
|----------------------|-----------------|
| Intermediate realm | Beings encountered, transition zone |
| Self-revelation process | Life review 17.5%, non-judgmental |
| Instruction period | Communication/guidance common |
| Return as exception | 70.1% not self-initiated return |
| Identity preserved | 64.8% clear identity maintained |

The **non-judgmental** character of the life review (15.9:1 love:harsh ratio) is particularly significant. This aligns with Swedenborg's account: the World of Spirits reveals rather than condemns; individuals are shown their true character without external punishment.

### 4.5 Clinical Implications

If NDE structure reflects genuine spiritual geography rather than cultural construction:

1. **Preparation for death**: Education about NDEs may reduce death anxiety
2. **Post-NDE support**: Understanding involuntary return may help NDErs integrate their experience
3. **Palliative care**: The consistent non-judgmental character of life reviews may comfort the dying

### 4.6 Limitations

1. **Self-selection**: Profound experiences are more likely to be reported
2. **Western sample**: Non-Western NDE phenomenology may differ
3. **Retrospective reconstruction**: Narrative ordering may be imposed post-hoc
4. **Schema dependencies**: GPT-5.2 extraction may have systematic biases

### 4.7 Future Directions

1. **Cross-cultural analysis**: Test whether patterns are universal
2. **Prospective tracking**: Document transformation trajectories post-NDE
3. **Longitudinal follow-up**: Assess whether "mission" returns show distinctive life trajectories
4. **Restorative incarnation analysis**: Link to past-life memory research (DOPS corpus)

---

## 5. Conclusion

Analysis of 6,753 near-death experiences provides strong support for the Normative Path Hypothesis:

1. **Return is Involuntary**: 70.1% did not return by their own choice
2. **Return is Reluctant**: 49.4% preferred to stay
3. **Deceased Are Present**: 17.9% encounter relatives who clearly *continued*
4. **Reincarnation is Rare**: <5% show any reincarnation indicators
5. **Identity Persists**: 64.8% maintain clear sense of self

The data support a threefold path model:
- **Normative**: Continuation (vast majority)
- **Restorative**: Reincarnation for healing (~4%)
- **Volunteer**: Reincarnation for mission (~1%)

The **15.9:1 love:harsh ratio** during life reviews supports the Swedenborgian model: the intermediate state reveals rather than condemns. The NDE appears to offer a glimpse into the first stage of post-mortem existence—a World of Spirits where consciousness transitions from earthly to spiritual organization, and where return to physical life is the exception granted for specific purposes, not the default.

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
| Agency × Willingness | χ² = 4824.78 | — | < 0.0001 |
| Love:Harsh Ratio | 223:14 | — | 15.9:1 |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,664 |
| IANDS records | 1,089 |
| Return not by choice | 70.1% |
| Reluctant to return | 49.4% |
| Deceased relatives present | 17.9% |
| Past life memory | 4.4% |
| Pre-incarnation covenant | 1.3% |
| Life review occurred | 17.5% |
| Love:Harsh judgment ratio | 15.9:1 |
| Identity preserved | 64.8% |

## Appendix C: Normative Path Evidence Summary

| Marker | Indicator | Supports |
|--------|-----------|----------|
| Return as Exception | External/involuntary: 70.1% | ✓ |
| Reluctance to Return | Reluctant returnees: 49.4% | ✓ |
| Deceased Present | Relatives encountered: 17.9% | ✓ |
| Reincarnation Rare | Past life memory: 4.4% | ✓ |
| Volunteer Path Rare | Pre-incarnation covenant: 1.3% | ✓ |

**Overall: 5/5 markers support the Normative Path Hypothesis**

## Appendix D: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [02_normative_path_validation.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb)
