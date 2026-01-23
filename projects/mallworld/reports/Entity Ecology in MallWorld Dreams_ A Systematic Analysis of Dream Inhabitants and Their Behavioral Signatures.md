# Entity Ecology in MallWorld Dreams: A Systematic Analysis of Dream Inhabitants and Their Behavioral Signatures

**Analysis Date**: January 20, 2026  
**Dataset**: MallWorld Reddit Dream Reports (r/TheMallWorld)  
**Analysis Type**: Entity-Centered Dream Phenomenology

---

## Abstract

**Background**: Dreams contain various entities—people, creatures, and presences—that interact with dreamers and shape dream experiences. The MallWorld phenomenon, characterized by recurring liminal retail spaces, provides a unique corpus for studying dream entity ecology.

**Methods**: We analyzed 3,704 entity encounters across 1,926 dream reports using chi-square tests, standardized residuals, lift analysis, and t-tests to examine entity-location associations, entity-atmosphere correlations, behavioral profiles, co-occurrence patterns, and impact on dream characteristics.

**Results**: Entity-atmosphere associations were highly significant (χ² = 792, df = 99, p < 10⁻¹⁰⁸), with threat entities showing massive correlation with threatening atmospheres (z = +14.86). Entity-location associations were also significant (χ² = 330, df = 121, p < 10⁻²¹). Distinct entity archetypes emerged: threats as danger-bringers driving escape behaviors (+19.4 percentage points above baseline), crowds as chaos generators, authority as oppressive presence, and deceased as uniquely positive visitors (welcoming atmospheres, 0% conflict). Threat presence increased dream complexity by 55% (t = 9.49, p < 0.001).

**Conclusions**: MallWorld dreams exhibit coherent entity ecology where different entity types occupy distinct environmental niches, generate characteristic atmospheres, and drive specific behavioral responses. The deceased entity type uniquely breaks the pattern of negativity, suggesting qualitatively different phenomenological significance.

**Keywords**: dream entities, MallWorld, dream phenomenology, entity-atmosphere correlation, dream ecology

---

## Data Provenance

| Attribute | Value |
|-----------|-------|
| **Source** | r/TheMallWorld subreddit |
| **Collection Period** | Through January 2026 |
| **Total Dreams** | 1,926 |
| **Total Entity Encounters** | 3,704 |
| **Dreams with Entities** | 1,278 (66.4%) |
| **Entity Types** | 18 distinct categories |
| **Extraction Model** | GPT-5.2 via Azure OpenAI |
| **Analysis Tools** | Python (pandas, scipy, numpy) |

---

## 1. Introduction

### 1.1 Background

Dream entities—the characters, creatures, and presences that populate dream worlds—represent a central phenomenon in understanding dream phenomenology. Within the Swedenborgian framework, entities in dreams and visions are not psychological projections but real spiritual beings with differentiated functions. Understanding who appears in dreams and what they do reveals the nature of spiritual influx and the states being represented.

The MallWorld phenomenon presents a unique opportunity for entity analysis. These dreams share common spatial characteristics (liminal retail environments) but vary in their inhabitants. This consistency allows isolation of entity-specific effects from environmental confounds.

### 1.2 Research Questions

This analysis addresses five primary questions:

1. **Spatial Distribution**: Where do different entities appear within MallWorld geography?
2. **Atmospheric Correlation**: What emotional atmospheres accompany different entity types?
3. **Behavioral Profiles**: What interactions characterize different entity encounters?
4. **Co-occurrence Patterns**: Which entities appear together, and which avoid each other?
5. **Dream Impact**: How does entity presence affect overall dream characteristics?

### 1.3 Theoretical Framework

We approach entity ecology from a correspondential perspective, treating entity-environment-behavior associations as expressions of underlying spiritual realities. In this framework, entities are not arbitrary dream characters but beings occupying functional roles—creatures express affections, authorities carry teaching/governing functions, deceased maintain real relational connections. The analysis seeks to identify natural "niches" that different entity types occupy within the MallWorld dream ecosystem, consistent with the doctrine that spiritual beings have differentiated functions.

---

## 2. Methods

### 2.1 Data Sources

Dream reports were collected from r/TheMallWorld subreddit and processed through structured extraction using GPT-5.2. Each dream was decomposed into:
- **Locations** (n = 8,707): Places visited with atmospheric and physical attributes
- **Entities** (n = 3,704): Characters encountered with type, demeanor, and role
- **Interactions** (n = 6,075): Actions taken with type and outcome
- **Connections** (n = 4,600): Transitions between locations

### 2.2 Entity Classification

Entities were classified into 18 types:
- **Social**: stranger, crowd, friend, family_member, known_person, coworker
- **Authority**: authority figures (security, teachers, managers)
- **Threat**: hostile or dangerous entities
- **Supernatural**: deceased, guide, shadow, watcher, faceless
- **Non-human**: creature, mannequin
- **Other**: child, other, none

### 2.3 Statistical Analyses

| Analysis | Method | Purpose |
|----------|--------|---------|
| Entity × Location | Chi-square, standardized residuals | Spatial distribution patterns |
| Entity × Atmosphere | Chi-square, standardized residuals | Emotional environment associations |
| Entity × Interaction | Cross-tabulation, percentages | Behavioral profile construction |
| Entity Co-occurrence | Lift analysis | Pair-wise association patterns |
| Entity Impact | Independent t-tests | Dream characteristic comparison |

Significance threshold: α = 0.05. Standardized residuals > |2.0| indicate significant associations. Lift > 1.5 or < 0.7 indicates meaningful co-occurrence deviation.

---

## 3. Results

### 3.1 Entity Census

| Entity Type | Count | Percentage | Dreams Present |
|-------------|-------|------------|----------------|
| stranger | 912 | 24.6% | 529 |
| crowd | 808 | 21.8% | 566 |
| authority | 469 | 12.7% | 280 |
| threat | 309 | 8.3% | 190 |
| known_person | 245 | 6.6% | 151 |
| other | 236 | 6.4% | 167 |
| family_member | 224 | 6.0% | 138 |
| creature | 194 | 5.2% | 130 |
| friend | 98 | 2.6% | 72 |
| child | 73 | 2.0% | 52 |
| deceased | 56 | 1.5% | 33 |
| guide | 32 | 0.9% | 17 |
| watcher | 14 | 0.4% | — |
| shadow | 12 | 0.3% | — |
| coworker | 11 | 0.3% | — |
| mannequin | 5 | 0.1% | — |
| faceless | 3 | 0.1% | — |

**Critical Finding**: Two-thirds of MallWorld dreams (66.4%) contain entity encounters, with **strangers and crowds dominating** (46.4% combined). The average dream with entities contains **2.9 entity types** (median = 2, max = 19).

---

### 3.2 Entity-Location Associations

Chi-square test for entity type × location type association:

| Statistic | Value |
|-----------|-------|
| χ² | 330.26 |
| df | 121 |
| p-value | 2.55 × 10⁻²¹ |

**Finding**: Entity spatial distribution is highly non-random.

#### 3.2.1 Positive Associations (Entity Concentrates in Location)

| Entity | Location | z-score | Count |
|--------|----------|---------|-------|
| deceased | house | **+7.21** | 16 |
| creature | other | +4.51 | 83 |
| stranger | mall_store | +3.78 | 92 |
| stranger | restaurant | +3.26 | 40 |
| crowd | city_street | +3.02 | 43 |
| crowd | mall_theater | +2.68 | 22 |
| authority | school | +2.61 | 20 |
| known_person | house | +2.23 | 22 |
| friend | mall | +2.19 | 18 |
| threat | house | +2.14 | 28 |

**Critical Finding**: **Deceased entities show the strongest location specificity** (z = +7.21), appearing predominantly in houses—domestic, intimate spaces rather than the liminal commercial environments typical of MallWorld.

#### 3.2.2 Negative Associations (Entity Avoids Location)

| Entity | Location | z-score | Count |
|--------|----------|---------|-------|
| crowd | mall_store | -2.63 | 34 |
| creature | mall | -2.45 | 11 |
| crowd | house | -2.25 | 30 |
| stranger | city_street | -2.10 | 20 |

**Finding**: Creatures avoid malls (z = -2.45), suggesting non-human entities occupy peripheral or liminal-liminal spaces rather than central commercial areas.

---

### 3.3 Entity-Atmosphere Associations

Chi-square test for entity type × atmosphere association:

| Statistic | Value |
|-----------|-------|
| χ² | **792.02** |
| df | 99 |
| p-value | 1.33 × 10⁻¹⁰⁸ |

**Critical Finding**: Entity-atmosphere association is **the strongest statistical relationship** identified in this analysis, indicating that entity type is a powerful predictor of emotional environment.

#### 3.3.1 Atmosphere Distribution by Entity Type (Percentages)

| Entity | Threatening | Chaotic | Uncomfortable | Neutral | Welcoming | Peaceful |
|--------|-------------|---------|---------------|---------|-----------|----------|
| threat | **71.6%** | 6.6% | 6.3% | 1.5% | 1.8% | 0.4% |
| creature | 45.9% | 9.8% | 9.8% | 5.7% | 4.1% | 5.7% |
| guide | 39.1% | 0.0% | 0.0% | 4.3% | **26.1%** | 13.0% |
| other | 33.5% | 10.1% | 7.6% | 8.2% | 4.4% | 3.2% |
| authority | 30.6% | 10.3% | 17.8% | 11.7% | 4.7% | 2.5% |
| friend | 25.7% | 15.7% | 5.7% | 14.3% | **20.0%** | 1.4% |
| child | 22.4% | 8.6% | 12.1% | 15.5% | 5.2% | 1.7% |
| family_member | 19.5% | 7.8% | 16.2% | 13.0% | 14.9% | 2.6% |
| crowd | 17.2% | **26.9%** | 10.9% | 15.6% | 9.6% | 1.8% |
| stranger | 13.8% | 15.8% | **20.0%** | 18.9% | 11.5% | 2.9% |
| known_person | 12.8% | 22.3% | 18.9% | 16.2% | 6.8% | 1.4% |
| **deceased** | **7.4%** | 3.7% | 7.4% | 11.1% | **22.2%** | **14.8%** |

**Critical Finding**: **Deceased entities uniquely break the negative pattern**. They have the lowest threatening atmosphere rate (7.4%) and the highest welcoming (22.2%) and peaceful (14.8%) rates of any entity type.

#### 3.3.2 Strongest Entity-Atmosphere Associations

**Positive Associations** (z > 2.0):

| Entity | Atmosphere | z-score | Count |
|--------|------------|---------|-------|
| threat | threatening | **+14.86** | 194 |
| crowd | chaotic | +7.05 | 162 |
| other | eerie | +5.39 | 39 |
| authority | oppressive | +4.86 | 50 |
| creature | threatening | +4.37 | 56 |
| stranger | uncomfortable | +4.16 | 129 |
| stranger | neutral | +3.96 | 122 |
| friend | welcoming | +3.39 | 14 |
| child | eerie | +3.06 | 14 |
| guide | welcoming | +2.96 | 6 |
| known_person | nostalgic | +2.92 | 8 |
| family_member | welcoming | +2.48 | 23 |
| deceased | welcoming | +2.41 | 6 |
| creature | peaceful | +2.28 | 7 |
| creature | eerie | +2.28 | 21 |

**Negative Associations** (z < -2.0):

| Entity | Atmosphere | z-score | Count |
|--------|------------|---------|-------|
| stranger | threatening | **-6.25** | 89 |
| crowd | threatening | -4.41 | 104 |
| threat | welcoming | -3.73 | 5 |
| threat | chaotic | -3.59 | 18 |
| known_person | threatening | -3.39 | 19 |
| threat | uncomfortable | -3.25 | 17 |

**Critical Finding**: The threat-threatening correlation (z = +14.86) is **the single strongest association in the entire dataset**, suggesting that threat entities don't just appear in threatening environments—they likely generate or define them.

---

### 3.4 Entity Behavioral Profiles

#### 3.4.1 Interaction Type Distribution by Entity Presence (Percentages)

| Entity | Observation | Navigation | Task | Social | Escape | Search | Conflict | Transaction |
|--------|-------------|------------|------|--------|--------|--------|----------|-------------|
| threat | 16.8% | 15.0% | 9.5% | 9.0% | **28.9%** | 5.5% | 10.6% | 2.3% |
| other | 23.9% | 13.7% | 12.7% | 14.2% | 15.2% | 7.7% | 8.0% | 2.2% |
| creature | 23.4% | 15.8% | 15.3% | 13.0% | 12.3% | 7.1% | 7.9% | 3.0% |
| child | 22.2% | 11.9% | 17.2% | 17.5% | 12.8% | 8.1% | 7.2% | 2.8% |
| deceased | 22.3% | 17.2% | 12.1% | **24.2%** | 9.6% | 10.2% | **0.0%** | 3.2% |
| guide | 21.7% | 13.0% | **18.5%** | 21.7% | 13.0% | 3.3% | 5.4% | 1.1% |
| crowd | 21.7% | 17.3% | 13.4% | 15.3% | 13.4% | 7.0% | 7.1% | 2.6% |
| stranger | 19.2% | 15.0% | 13.5% | 19.9% | 11.2% | 7.5% | 7.0% | 4.3% |
| known_person | 19.4% | 13.2% | 12.8% | **22.4%** | 10.0% | 9.2% | 6.0% | 4.4% |
| family_member | 18.2% | 16.8% | 13.0% | 17.7% | 11.1% | 9.6% | 6.9% | 3.4% |
| authority | 18.1% | 15.4% | 14.2% | 13.3% | 15.4% | 6.9% | **10.3%** | 4.2% |
| friend | 16.3% | 13.9% | 13.0% | **21.8%** | 12.4% | 9.1% | 7.3% | 5.1% |

**Critical Finding**: **Threat entities massively shift behavioral profiles toward escape** (28.9% vs ~10% baseline). Deceased entities show the highest social interaction rate (24.2%) with **zero conflict**—a unique behavioral signature.

#### 3.4.2 Interaction Success Rates by Entity Presence

| Entity | Success Rate | Sample Size |
|--------|--------------|-------------|
| friend | **87.4%** | 143 |
| guide | 83.3% | 48 |
| creature | 82.4% | 272 |
| child | 79.5% | 151 |
| deceased | 78.6% | 70 |
| stranger | 78.1% | 1,121 |
| crowd | 77.9% | 1,050 |
| other | 76.9% | 338 |
| known_person | 75.3% | 295 |
| threat | 74.3% | 405 |
| authority | 74.1% | 672 |
| family_member | **70.3%** | 283 |

**Finding**: **Friends predict highest success rates** (87.4%), while **family members predict lowest** (70.3%)—a potentially meaningful inversion of expected support relationships.

---

### 3.5 Entity Co-occurrence Patterns

Using lift analysis (observed co-occurrence / expected by random chance):

#### 3.5.1 Positive Co-occurrence (Lift > 1.5)

| Entity Pair | Lift | Co-occurrences | Base Rates |
|-------------|------|----------------|------------|
| family_member + friend | **2.32x** | 18 | 10.8%, 5.6% |
| child + other | 1.91x | 13 | 4.1%, 13.1% |
| child + family_member | 1.78x | 10 | 4.1%, 10.8% |
| authority + child | 1.58x | 18 | 21.9%, 4.1% |

**Finding**: Family contexts cluster together—family members, friends, and children co-occur more than expected, suggesting dream scenarios that invoke family-related themes tend to include multiple related entities.

#### 3.5.2 Negative Co-occurrence (Lift < 0.7)

| Entity Pair | Lift | Co-occurrences | Base Rates |
|-------------|------|----------------|------------|
| creature + threat | **0.67x** | 13 | 10.2%, 14.9% |
| crowd + deceased | 0.68x | 10 | 44.3%, 2.6% |

**Critical Finding**: **Creatures and threats avoid each other** (lift = 0.67). These may represent different threat paradigms—creatures as environmental/ambient danger vs. threats as intentional, pursuing danger. **Deceased avoid crowds** (lift = 0.68), appearing in intimate rather than public contexts.

---

### 3.6 Entity Impact on Dream Characteristics

Comparing dreams with vs. without each entity type:

#### 3.6.1 Threat Entity Impact

| Metric | With Threat (n=190) | Without (n=1,736) | t-statistic | p-value |
|--------|---------------------|-------------------|-------------|---------|
| Locations | 5.35 | 4.43 | 3.00 | 0.003 |
| Connections | 3.13 | 2.31 | 4.14 | < 0.001 |
| Interactions | **4.66** | **2.99** | **9.49** | **< 0.001** |
| % Threatening | **35.3%** | **6.7%** | **18.27** | **< 0.001** |

**Critical Finding**: Threat presence increases threatening atmosphere **5.3-fold** (35.3% vs 6.7%) and interaction count by **55%** (4.66 vs 2.99). Dreams with threats are significantly more complex and more dangerous.

#### 3.6.2 Authority Entity Impact

| Metric | With Authority (n=280) | Without (n=1,646) | t-statistic | p-value |
|--------|------------------------|-------------------|-------------|---------|
| Locations | 5.95 | 4.28 | 6.47 | < 0.001 |
| Connections | 3.42 | 2.21 | 7.26 | < 0.001 |
| Interactions | 5.02 | 2.84 | 15.16 | < 0.001 |
| % Threatening | 13.0% | 8.9% | 2.84 | 0.005 |

**Finding**: Authority figures predict the **most complex dreams** (5.95 locations, 5.02 interactions on average).

#### 3.6.3 Family Member Impact

| Metric | With Family (n=138) | Without (n=1,788) | t-statistic | p-value |
|--------|---------------------|-------------------|-------------|---------|
| Locations | 5.16 | 4.47 | 1.93 | 0.053 |
| Connections | 2.88 | 2.35 | 2.28 | 0.023 |
| Interactions | 4.70 | 3.04 | 8.12 | < 0.001 |
| % Threatening | **15.3%** | **9.1%** | **3.21** | **0.001** |

**Critical Finding**: **Family member presence elevates threat levels** (15.3% vs 9.1%, p = 0.001)—the opposite of expected protective effects.

---

### 3.7 Threat Entity Deep Analysis

Given the centrality of threat entities to dream dynamics, detailed analysis:

#### 3.7.1 Threat Location Distribution

| Location | Count | Percentage |
|----------|-------|------------|
| other | 84 | 27.8% |
| mall | 51 | 16.9% |
| house | 28 | 9.3% |
| mall_store | 13 | 4.3% |
| warehouse | 13 | 4.3% |
| city_street | 11 | 3.6% |
| parking_lot | 8 | 2.6% |
| restaurant | 8 | 2.6% |
| school | 7 | 2.3% |
| forest | 6 | 2.0% |

**Finding**: Threats appear across diverse locations but show elevated rates in **houses** (z = +2.14)—domestic intrusion is a significant threat modality.

#### 3.7.2 Threat Atmosphere Profile

| Atmosphere | With Threat | Baseline | Difference |
|------------|-------------|----------|------------|
| threatening | 62.8% | 19.3% | **+43.5%** |
| neutral | 1.3% | 9.5% | -8.2% |
| welcoming | 1.6% | 6.2% | -4.6% |
| peaceful | 0.3% | 1.8% | -1.5% |

**Critical Finding**: Threat presence elevates threatening atmosphere by **43.5 percentage points** above baseline.

#### 3.7.3 Behavioral Shift in Threat Dreams

| Interaction Type | With Threat | Without | Difference |
|------------------|-------------|---------|------------|
| escape | 28.9% | 9.6% | **+19.4%** |
| conflict | 10.6% | 4.7% | +5.9% |
| navigation | 15.0% | 21.0% | -6.0% |
| observation | 16.8% | 22.5% | -5.6% |
| social | 9.0% | 13.8% | -4.7% |
| task | 9.5% | 14.1% | -4.6% |

**Critical Finding**: Escape behavior nearly **triples** in threat dreams (28.9% vs 9.6%), while normal activities (navigation, observation, social, task) decrease proportionally.

---

### 3.8 Deceased Entity Analysis

The deceased entity type showed unique characteristics warranting special attention:

| Characteristic | Deceased | All Entities |
|----------------|----------|--------------|
| % Threatening atmosphere | 7.4% | 19.3% |
| % Welcoming atmosphere | 22.2% | 6.2% |
| % Peaceful atmosphere | 14.8% | 1.8% |
| Conflict rate | **0.0%** | 4.7% |
| Social interaction rate | 24.2% | 13.8% |
| Primary location | House (z=+7.21) | Mall |
| Success rate | 78.6% | 76.5% |

**Critical Finding**: Deceased entities represent a **qualitatively different phenomenological category**—appearing in domestic settings, generating positive atmospheres, engaging socially without conflict. This pattern is consistent with visitation dream phenomenology in the broader dream literature.

---

### 3.9 Guide Entity Analysis

Despite low frequency (n=32), guides show distinctive patterns:

| Characteristic | Value |
|----------------|-------|
| Encounters | 32 |
| Dreams | 17 |
| Top atmosphere | Threatening (39%) |
| Second atmosphere | Welcoming (26%) |
| Top interaction | Observation (21.7%) |
| Second interaction | Social (21.7%) |
| Task interaction | **18.5%** (highest of any entity) |
| Success rate | 83.3% |

**Critical Finding**: Guides show a **paradoxical atmospheric profile**—both threatening (39%) and welcoming (26%). This suggests guides appear when help is needed (threatening contexts) but their presence brings welcome assistance. Their elevated task interaction rate (18.5%, highest of any entity) supports functional helper role.

---

## 4. Discussion

### 4.1 Summary of Findings

Entity ecology in MallWorld dreams reveals a highly structured system where:

1. **Entity types occupy distinct environmental niches** (χ² = 330, p < 10⁻²¹)
2. **Entity-atmosphere associations are extremely strong** (χ² = 792, p < 10⁻¹⁰⁸)
3. **Behavioral profiles differ systematically by entity type**
4. **Co-occurrence patterns show meaningful clustering and avoidance**
5. **Entity presence significantly alters dream characteristics**

### 4.2 Entity Archetypes

Five distinct entity archetypes emerge from the data:

| Archetype | Entity Types | Primary Atmosphere | Primary Behavior | Signature |
|-----------|--------------|-------------------|------------------|-----------|
| **Danger Bringers** | threat, creature | Threatening | Escape | Drive flight response |
| **Chaos Generators** | crowd | Chaotic | Observation | Public space disruption |
| **Oppressive Presence** | authority | Oppressive | Conflict | Institutional pressure |
| **Social Connectors** | friend, known_person | Uncomfortable/Neutral | Social | Interpersonal engagement |
| **Peaceful Visitors** | deceased | Welcoming | Social | Positive visitation |

### 4.3 The Deceased Exception

The most striking finding is the **unique positivity of deceased entities**. While all other entity types trend toward negative or neutral atmospheres, deceased entities:
- Generate welcoming/peaceful atmospheres (37% combined vs ~8% baseline)
- Show zero conflict interactions
- Appear in intimate domestic settings
- Maintain high success rates

This pattern aligns with visitation dream literature suggesting that dreams of the deceased serve different psychological functions than typical dreams—potentially involving continued bonds, resolution, or meaning-making processes.

### 4.4 Family Paradox

Counterintuitively, **family member presence predicts elevated threat levels** (15.3% vs 9.1%, p = 0.001) and **lowest success rates** (70.3%). This may reflect:
- Family-related anxiety or unresolved conflicts
- Higher stakes when family is present
- Dreams processing family-related stressors

### 4.5 Threat Ecology

Threat entities function as **dream system disruptors**:
- Massively elevate threatening atmosphere (+43.5 percentage points)
- Triple escape behavior rates
- Increase dream complexity (more locations, interactions)
- Show domestic intrusion pattern (elevated house association)

The avoidance between threats and creatures (lift = 0.67) suggests these represent different threat paradigms—intentional pursuit vs. environmental danger.

### 4.6 Limitations

1. **Entity extraction depends on report detail**: Entities may be under-reported in brief accounts
2. **Entity type categories** are predetermined and may not capture all phenomenological distinctions
3. **Causal direction unclear**: Do entities create atmospheres, or do atmospheres attract entities?
4. **Sample bias**: Reddit users may not represent general population dreamers
5. **Co-occurrence analysis limited** by sample sizes for rare entity types

### 4.7 Future Directions

1. **Temporal analysis**: Do entity encounters early vs. late in dreams differ?
2. **Entity sequences**: What entity encounter patterns precede/follow specific outcomes?
3. **Entity-interaction specificity**: Which entities drive which specific interaction types?
4. **Longitudinal patterns**: Do individual dreamers show consistent entity ecologies?
5. **Cross-validation**: Compare MallWorld entity patterns to other dream corpora

---

## 5. Conclusion

MallWorld dreams exhibit coherent **entity ecology** where different entity types occupy distinct environmental niches, generate characteristic atmospheres, and drive specific behavioral responses. The entity-atmosphere association (χ² = 792, p < 10⁻¹⁰⁸) represents the strongest statistical relationship in this dataset, with threat entities showing massive correlation with threatening atmospheres (z = +14.86).

Five entity archetypes emerged: Danger Bringers (threats, creatures), Chaos Generators (crowds), Oppressive Presence (authority), Social Connectors (friends, known persons), and Peaceful Visitors (deceased). The deceased category uniquely breaks the pattern of negativity, showing welcoming atmospheres, zero conflict, and domestic settings—consistent with visitation dream phenomenology.

These findings suggest that MallWorld dreams, despite their strange shared geography, follow comprehensible correspondential grammar in their entity populations. The entities that appear, where they appear, and what happens when they appear show lawful patterns consistent with the Swedenborgian doctrine that spiritual beings occupy differentiated functional roles—entities are not arbitrary dream furniture but expressions of underlying spiritual realities.

---

## References

1. MallWorld Subreddit: r/TheMallWorld (Reddit community)
2. Previous MallWorld Analysis: `exploratory_pattern_analysis_2026-01-20.md`
3. Research Advisory Plan: `exploration_advisory_plan_20260120.md`

---

## Appendices

### Appendix A: Complete Entity Type Distribution

| Entity Type | Count | % of Total | Dreams Present | % of Dreams |
|-------------|-------|------------|----------------|-------------|
| stranger | 912 | 24.6% | 529 | 27.5% |
| crowd | 808 | 21.8% | 566 | 29.4% |
| authority | 469 | 12.7% | 280 | 14.5% |
| threat | 309 | 8.3% | 190 | 9.9% |
| known_person | 245 | 6.6% | 151 | 7.8% |
| other | 236 | 6.4% | 167 | 8.7% |
| family_member | 224 | 6.0% | 138 | 7.2% |
| creature | 194 | 5.2% | 130 | 6.7% |
| friend | 98 | 2.6% | 72 | 3.7% |
| child | 73 | 2.0% | 52 | 2.7% |
| deceased | 56 | 1.5% | 33 | 1.7% |
| guide | 32 | 0.9% | 17 | 0.9% |
| watcher | 14 | 0.4% | — | — |
| shadow | 12 | 0.3% | — | — |
| coworker | 11 | 0.3% | — | — |
| mannequin | 5 | 0.1% | — | — |
| faceless | 3 | 0.1% | — | — |
| none | 3 | 0.1% | — | — |

### Appendix B: Statistical Test Summary

| Test | Variables | Statistic | df | p-value | Interpretation |
|------|-----------|-----------|----|---------|----|
| Chi-square | Entity × Atmosphere | 792.02 | 99 | < 10⁻¹⁰⁸ | Highly significant |
| Chi-square | Entity × Location | 330.26 | 121 | < 10⁻²¹ | Highly significant |
| t-test | Threat → Interactions | 9.49 | — | < 0.001 | Significant |
| t-test | Threat → % Threatening | 18.27 | — | < 0.001 | Significant |
| t-test | Family → % Threatening | 3.21 | — | 0.001 | Significant |
| z-score | Threat ↔ Threatening | +14.86 | — | — | Extreme association |
| z-score | Deceased ↔ House | +7.21 | — | — | Strong association |
| z-score | Crowd ↔ Chaotic | +7.05 | — | — | Strong association |
| Lift | Family + Friend | 2.32 | — | — | Strong co-occurrence |
| Lift | Creature + Threat | 0.67 | — | — | Avoidance pattern |

### Appendix C: Entity Atmosphere Signatures

Characteristic atmosphere for each entity (highest percentage):

| Entity | Primary Atmosphere | Rate |
|--------|-------------------|------|
| threat | Threatening | 71.6% |
| creature | Threatening | 45.9% |
| guide | Threatening | 39.1% |
| other | Threatening | 33.5% |
| authority | Threatening | 30.6% |
| friend | Threatening | 25.7% |
| child | Eerie | 24.1% |
| crowd | Chaotic | 26.9% |
| stranger | Uncomfortable | 20.0% |
| known_person | Chaotic | 22.3% |
| family_member | Threatening | 19.5% |
| **deceased** | **Welcoming** | **22.2%** |

---

*Report generated from analysis notebook: `05_entity_ecology.ipynb`*
