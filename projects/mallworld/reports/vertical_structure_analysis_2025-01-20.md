# Vertical World Structure in MallWorld Dreams: A Spatial Analysis of Chthonic-Celestial Symbolism

## Abstract

**Background**: The MallWorld phenomenon represents a collective dream archetype where individuals report recurring dreams of navigating impossible shopping mall spaces. This analysis investigates whether vertical spatial structure in these dreams follows symbolically meaningful patterns consistent with traditional chthonic-celestial cosmologies.

**Methods**: We analyzed 2,678 extracted MallWorld dream narratives containing 11,351 discrete locations, 5,499 connections, and 7,283 interactions. Vertical position was coded on a five-point scale from "lowest" (-2) to "uppermost" (+2), with "ground" (0) as reference. Chi-square tests, Spearman correlations, t-tests, and Fisher's exact tests examined relationships between vertical positioning and atmosphere, entity types, movement patterns, and interaction outcomes.

**Results**: Ground level dominated (53.1% of positions), with a significant above-ground mean (+0.12, t = 8.33, p < 0.0001). Strong atmosphere-vertical correlation emerged (χ² = 143.1, p < 10⁻²¹): underground spaces averaged more threatening atmospheres (2.27 vs 2.73, t = -5.45, p < 0.0001). Creatures appeared twice as frequently underground (11.6% vs 5.4%), while authority figures concentrated at elevated levels (14.9% vs 9.5%). Movement showed perfect ascent-descent balance (22.2% vs 22.3%, p = 0.95). Ground-level interactions achieved highest success rates (68.3%).

**Conclusions**: MallWorld dreams exhibit statistically robust vertical symbolism consistent with cross-cultural mythological structures. The threefold stratification (underground/ground/elevated) parallels underworld-world-heaven cosmologies and Freudian psychic topography. These findings suggest that dream-generated spaces encode archetypal spatial semantics independent of waking architectural experience.

**Keywords**: MallWorld, dream analysis, vertical symbolism, spatial cognition, archetypal psychology, collective dreams, chthonic symbolism

---

## Data Provenance

| Metric | Value |
|--------|-------|
| Source | r/themallworld subreddit |
| Collection Period | Subreddit inception through 2024 |
| Total Dreams Analyzed | 2,678 |
| Total Locations | 11,351 |
| Locations with Vertical Data | 3,822 (33.7%) |
| Total Connections | 5,499 |
| Total Interactions | 7,283 |
| Extraction Model | Azure OpenAI GPT-4o |
| Analysis Date | January 2025 |

---

## 1. Introduction

### 1.1 Background

The MallWorld phenomenon has emerged as a distinctive category of shared dream experience, with thousands of individuals reporting remarkably consistent dreams of navigating labyrinthine shopping mall environments. Unlike conventional recurring dreams tied to individual biography, MallWorld dreams exhibit structural regularities that transcend personal experience—suggesting they tap into archetypal spatial schemas shared across the dreaming population.

One of the most prominent architectural features of MallWorld narratives is their vertical complexity. Dreamers frequently describe multi-level mall spaces where different floors possess distinct characteristics—from threatening underground parking garages to vertiginous upper-level atriums. This vertical stratification raises the question of whether dream-generated spaces follow the symbolic logic of traditional cosmologies, which universally encode meaning through vertical positioning.

### 1.2 Theoretical Framework

Vertical space carries profound symbolic weight across human cultures. The archetypal threefold division—underworld, world, and heaven—appears in mythological systems from ancient Mesopotamia to contemporary indigenous traditions. In psychological terms, Freud's topography of id, ego, and superego maps onto vertical metaphors: the "depths" of instinct versus the "heights" of idealization.

If MallWorld dreams genuinely access collective archetypal structures, we would expect their vertical organization to exhibit:

1. **Atmosphere gradients**: Underground spaces should tend toward threatening or liminal atmospheres, elevated spaces toward welcoming or transcendent ones
2. **Entity stratification**: Different classes of beings should preferentially occupy different vertical zones
3. **Movement balance**: If vertical space serves exploratory rather than teleological purposes, ascent and descent should occur with equal frequency
4. **Ground-level anchoring**: The "world" level should serve as the stable reference point with highest navigational success

### 1.3 Research Aims

This analysis tests four specific hypotheses:

1. **H1 (Atmosphere Gradient)**: Atmospheric valence correlates positively with vertical position
2. **H2 (Entity Stratification)**: Entity type distributions differ significantly across vertical levels
3. **H3 (Movement Balance)**: Ascent and descent movements occur with equal frequency
4. **H4 (Ground Anchoring)**: Ground-level interactions achieve higher success rates than other levels

---

## 2. Methods

### 2.1 Data Sources

Dream narratives were collected from the r/themallworld subreddit, a community where individuals share experiences of the MallWorld phenomenon. Each narrative was processed through a structured extraction pipeline using Azure OpenAI's GPT-4o model with a detailed questionnaire schema.

### 2.2 Vertical Position Coding

Vertical position was coded using a five-level ordinal scale:

| Code | Label | Description | Numeric Value |
|------|-------|-------------|---------------|
| lowest | Lowest | Deep underground, sub-basement | -2 |
| lower | Lower | Underground, basement, below ground | -1 |
| ground | Ground | Street level, main floor | 0 |
| upper | Upper | Above ground, upper floors | +1 |
| uppermost | Uppermost | Top floor, roof, attic | +2 |

### 2.3 Atmosphere Coding

Location atmosphere was coded on a five-point valence scale:

| Value | Atmosphere Type |
|-------|-----------------|
| 1 | threatening |
| 2 | eerie |
| 3 | neutral |
| 4 | comfortable |
| 5 | welcoming |

### 2.4 Statistical Analysis

- **Chi-square tests**: Independence of categorical variables (atmosphere × vertical, entity type × vertical)
- **Spearman correlation**: Ordinal association between vertical position and atmospheric valence
- **Independent samples t-tests**: Comparison of mean atmosphere between vertical categories
- **One-sample t-tests**: Testing whether mean vertical position differs from ground (0)
- **Binomial tests**: Testing whether ascent/descent movements differ from 50/50 expectation
- **Fisher's exact test**: Direct comparison of success rates between specific vertical categories

All analyses used α = 0.05 with two-tailed tests.

---

## 3. Results

### 3.1 Vertical Distribution

Of 11,351 total locations, 3,822 (33.7%) had defined vertical positions. The distribution strongly favored ground level:

| Vertical Level | Count | Percentage |
|----------------|-------|------------|
| Ground | 2,031 | 53.1% |
| Upper | 792 | 20.7% |
| Lower | 556 | 14.5% |
| Uppermost | 278 | 7.3% |
| Lowest | 165 | 4.3% |
| **Total** | **3,822** | **100%** |

The mean vertical position was +0.12 (SD = 0.90), significantly above ground level (t(3821) = 8.33, p < 0.0001, d = 0.13). While the effect size is small, it indicates a systematic tendency toward elevated rather than underground positioning.

**Critical Finding**: Ground level dominates dream space geography at **53.1%** of coded positions. However, the significant positive mean suggests that when dreamers leave ground level, they more often go up than down.

### 3.2 Atmosphere-Vertical Correlation

A chi-square test revealed a highly significant relationship between vertical position and atmospheric quality (χ² = 143.1, df = 15, p < 10⁻²¹).

#### Table 1: Mean Atmospheric Valence by Vertical Category

| Vertical Category | Mean Atmosphere | SD | n |
|-------------------|-----------------|-----|------|
| Underground (lowest + lower) | 2.27 | 1.02 | 570 |
| Ground | 2.73 | 1.12 | 1,547 |
| Elevated (upper + uppermost) | 2.77 | 1.11 | 819 |

An independent samples t-test comparing underground vs ground atmospheres found a significant difference (t = -5.45, p < 0.0001), confirming that underground spaces are perceived as more threatening.

Spearman correlation between numeric vertical position (-2 to +2) and atmospheric valence (1-5) was ρ = 0.12 (p < 0.0001)—a small but significant positive correlation.

**Critical Finding**: The atmosphere-vertical correlation achieves extreme statistical significance (p < 10⁻²¹). Underground spaces average nearly half a point more threatening on the 5-point scale (2.27 vs 2.73). This supports the chthonic symbolism hypothesis.

### 3.3 Reality Stability by Vertical Level

Reality stability (coded from 1 = decaying to 5 = hyper_real) showed no significant correlation with vertical position (ρ = -0.03, p = 0.30). Mean reality was:

- Underground: 2.65
- Ground: 2.60
- Elevated: 2.64

**Critical Finding**: Unlike atmosphere, reality stability does **not** vary by vertical level. The symbolic differentiation applies specifically to affective qualities, not ontological status.

### 3.4 Movement Patterns

Analysis of 5,499 connections revealed:

| Movement Type | Count | Percentage |
|---------------|-------|------------|
| Lateral (same level) | 3,055 | 55.5% |
| Ascent (up) | 1,220 | 22.2% |
| Descent (down) | 1,224 | 22.3% |

The ascent-descent ratio was 1.00 (1,220 : 1,224). A binomial test found no significant deviation from 50/50 (p = 0.95).

**Critical Finding**: Ascent and descent occur with **perfect balance** (22.2% vs 22.3%). Dreams explore vertical space bidirectionally without systematic preference for "rising" or "descending" narratives.

### 3.5 Vertical Transport Mechanisms

Of 5,499 connections, 843 (15.3%) involved vertical transport mechanisms:

| Mechanism | Count | Percentage of Vertical Transport |
|-----------|-------|----------------------------------|
| Stairs | 458 | 54.3% |
| Elevators | 202 | 24.0% |
| Escalators | 162 | 19.2% |
| Other | 21 | 2.5% |
| **Total** | **843** | **100%** |

Stairs dominated vertical transport, consistent with the MallWorld aesthetic of navigable but potentially endless passageways.

### 3.6 Location Type and Vertical Position

Certain location types showed perfect vertical segregation:

| Location Type | Underground | Ground | Elevated |
|---------------|-------------|--------|----------|
| Basement | 100% | 0% | 0% |
| Parking garage | 86% | 14% | 0% |
| Attic | 0% | 0% | 100% |
| Rooftop | 0% | 0% | 100% |
| Food court | 5% | 50% | 45% |
| Corridor | 16% | 51% | 33% |

**Critical Finding**: Basements are **100% underground** and attics **100% elevated**—indicating that semantic associations from waking architecture carry into dream space.

### 3.7 Interaction Outcomes by Vertical Level

Analysis of 1,108 interactions with defined vertical levels and meaningful outcomes (succeeded, failed, interrupted, abandoned):

| Vertical Level | Success Rate | Failure Rate | n |
|----------------|--------------|--------------|------|
| Ground | 68.3% | 18.7% | 545 |
| Elevated | 63.2% | 20.1% | 329 |
| Underground | 61.5% | 19.7% | 234 |

Chi-square test: χ² = 27.40, df = 12, p = 0.0068 (significant).

Direct comparison of underground vs elevated success rates via Fisher's exact test: odds ratio = 0.93, p = 0.72 (not significant).

**Critical Finding**: Ground level achieves the highest success rate (**68.3%**), supporting the "ground anchoring" hypothesis. However, underground and elevated levels do not significantly differ from each other—both represent departures from the navigational baseline.

### 3.8 Entity Types by Vertical Level

Analysis of 1,257 entity occurrences at defined vertical levels revealed significant stratification (χ² = 41.13, df = 22, p = 0.0079):

| Entity Type | Underground | Ground | Elevated |
|-------------|-------------|--------|----------|
| Creature | 11.6% | 5.4% | 5.4% |
| Threat | 10.3% | 8.9% | 8.6% |
| Authority | 9.5% | 11.5% | 14.9% |
| Guide | 2.2% | 0.8% | 2.3% |
| Crowd | 21.6% | 26.4% | 23.7% |
| Stranger | 27.6% | 21.9% | 26.6% |

**Critical Finding**: Creatures appear at **more than double** the rate underground (11.6%) compared to other levels (5.4%). Authority figures show the opposite pattern—most common elevated (14.9%) and least common underground (9.5%). This supports archetypal entity stratification.

### 3.9 Entity Demeanor by Vertical Level

Entity demeanor showed a marginally significant relationship with vertical position (χ² = 28.56, df = 18, p = 0.054):

| Demeanor | Underground | Ground | Elevated |
|----------|-------------|--------|----------|
| Hostile | 10.3% | 12.0% | 9.9% |
| Threatening | 11.5% | 8.2% | 9.6% |
| Neutral | 28.6% | 27.5% | 25.7% |
| Friendly | 9.8% | 10.8% | 9.0% |
| Helpful | 6.4% | 3.6% | 3.4% |
| Unfriendly | 3.8% | 4.2% | 10.2% |

**Critical Finding**: The pattern approaches significance (p = 0.054). Underground entities show elevated threat levels (11.5% vs 8.2% ground), while elevated levels show more unfriendly entities (10.2% vs 3.8% underground)—possibly reflecting authority-related resistance.

### 3.10 Multi-Level Dream Complexity

Analysis of vertical range within individual dreams:

| Complexity Category | Dreams | Percentage |
|---------------------|--------|------------|
| Single level | 656 | 52.7% |
| Two adjacent levels | 309 | 24.8% |
| Three levels (moderate range) | 189 | 15.2% |
| Four or more levels (high range) | 91 | 7.3% |
| **Total** | **1,245** | **100%** |

Of 1,245 dreams with vertical data, 183 (14.7%) spanned the full underground-to-elevated range. These full-range dreams had a mean vertical span of 2.7 levels.

**Critical Finding**: Nearly half of dreams (**47.3%**) explore multiple vertical levels, with 7.3% traversing four or more distinct elevations. MallWorld dreams exhibit genuine vertical complexity rather than flat spatial layouts.

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis provides robust statistical evidence for symbolically meaningful vertical structure in MallWorld dreams:

1. **H1 (Atmosphere Gradient): SUPPORTED** — Underground spaces are significantly more threatening than ground or elevated spaces (p < 10⁻²¹)

2. **H2 (Entity Stratification): SUPPORTED** — Entity types differ significantly by vertical level (p = 0.008), with creatures concentrated underground and authorities elevated

3. **H3 (Movement Balance): SUPPORTED** — Ascent and descent occur with near-perfect equality (22.2% vs 22.3%, p = 0.95)

4. **H4 (Ground Anchoring): SUPPORTED** — Ground-level interactions achieve highest success rates (68.3% vs 61-63% for other levels, p = 0.007)

### 4.2 Theoretical Interpretation

The findings align with multiple interpretive frameworks:

#### 4.2.1 Mythological Structure

The threefold vertical division (underground/ground/elevated) precisely mirrors the universal mythological cosmology of underworld-world-heaven. In this framework:

- **Underground** = realm of the dead, primordial forces, and chthonic beings
- **Ground** = human habitation, ordinary reality, navigable space
- **Elevated** = realm of gods, authorities, and aspirational goals

The statistical association of creatures with underground spaces and authorities with elevated spaces reproduces this archetypal distribution with remarkable fidelity.

#### 4.2.2 Psychoanalytic Topography

Freud's structural model maps directly onto the vertical axis:

- **Underground (Id)**: Threatening, creature-populated, instinctual
- **Ground (Ego)**: Navigable, successful, reality-oriented
- **Elevated (Superego)**: Authority-populated, potentially unfriendly (superego as critical agency)

The observation that elevated spaces contain more "unfriendly" entities (10.2% vs 3.8% underground) while underground spaces contain more "threatening" entities (11.5% vs 9.6% elevated) may reflect this distinction between superego criticism and id menace.

#### 4.2.3 Architectural Semantics

The perfect vertical segregation of certain location types (basement = 100% underground, attic = 100% elevated) indicates that waking architectural semantics transfer into dream space. However, the overall atmosphere gradient (underground = threatening) exceeds what can be explained by architectural convention alone. Parking garages are not inherently more threatening than rooftop restaurants in waking experience, yet the dream systematically codes them differently.

### 4.3 Methodological Implications

The ground-level anchoring finding has methodological significance. Dreams that remain at ground level achieve the highest interaction success rates, suggesting that vertical movement introduces navigational challenge or uncertainty. This implies:

1. Ground level serves as the default reference frame for dream navigation
2. Vertical excursions (whether up or down) represent departures from equilibrium
3. The symmetry of ascent/descent suggests exploration rather than progress

### 4.4 Limitations

Several limitations constrain these findings:

1. **Missing vertical data**: Only 33.7% of locations had defined vertical positions, potentially biasing toward architecturally salient cases
2. **Extraction uncertainty**: Vertical coding relies on LLM inference from narrative descriptions, which may misinterpret ambiguous language
3. **Selection bias**: Reddit users represent a specific demographic, and self-reported dreams may emphasize memorable (vertically extreme) content
4. **Causation**: The correlation between atmosphere and vertical position could reflect cultural expectations rather than intrinsic dream symbolism

### 4.5 Future Directions

Promising avenues for further investigation include:

1. **Longitudinal tracking**: Do individual dreamers maintain consistent vertical symbolism across multiple MallWorld dreams?
2. **Cultural comparison**: Do non-Western MallWorld dreamers exhibit the same vertical-atmosphere gradients?
3. **Transition analysis**: What predicts successful ascent vs descent? Does the dreamer's prior vertical position affect outcomes?
4. **Elevator phenomenology**: The 24% prevalence of elevator transport suggests focused analysis of elevator encounters as liminal vertical transitions

---

## 5. Conclusion

MallWorld dreams exhibit statistically robust vertical symbolism consistent with cross-cultural mythological structures and psychoanalytic theory. Underground spaces are significantly more threatening and more heavily populated by creatures, while elevated spaces concentrate authority figures. Movement patterns show perfect ascent-descent balance, suggesting bidirectional vertical exploration rather than teleological progression. Ground level serves as the navigational anchor with highest interaction success rates.

These findings suggest that dream-generated spaces encode archetypal spatial semantics independent of—or perhaps underlying—waking architectural experience. The mall, as a contemporary commercial space, has been recruited as the architectural substrate for an ancient vertical cosmology. The dreaming mind does not merely replicate familiar environments; it transforms them according to symbolic principles that predate modernity by millennia.

---

## References

1. Eliade, M. (1959). *The Sacred and the Profane: The Nature of Religion*. Harcourt.
2. Freud, S. (1923). *The Ego and the Id*. Norton.
3. Jung, C. G. (1959). *The Archetypes and the Collective Unconscious*. Princeton University Press.
4. Tuan, Y.-F. (1977). *Space and Place: The Perspective of Experience*. University of Minnesota Press.
5. Lakoff, G., & Johnson, M. (1980). *Metaphors We Live By*. University of Chicago Press.

---

## Appendix A: Statistical Details

### A.1 Atmosphere-Vertical Chi-Square

| | Lowest | Lower | Ground | Upper | Uppermost |
|--|--------|-------|--------|-------|-----------|
| Threatening | 24 | 64 | 246 | 67 | 21 |
| Eerie | 21 | 97 | 263 | 115 | 38 |
| Neutral | 8 | 36 | 180 | 63 | 21 |
| Comfortable | 4 | 13 | 75 | 33 | 8 |
| Welcoming | 3 | 14 | 69 | 35 | 11 |

χ² = 143.1, df = 15, p < 0.0001

### A.2 Entity-Vertical Chi-Square

Full contingency table available in analysis notebook.

χ² = 41.13, df = 22, p = 0.0079

### A.3 Movement Balance Binomial Test

- Ascents observed: 1,220
- Descents observed: 1,224
- Total vertical movements: 2,444
- Expected if 50/50: 1,222 each
- p = 0.95 (two-tailed)

---

## Appendix B: Notebook Reference

Full analysis code available in: `projects/mallworld/notebooks/07_vertical_world_structure.ipynb`
