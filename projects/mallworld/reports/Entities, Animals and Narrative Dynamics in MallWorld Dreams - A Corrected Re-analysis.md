# Entities, Animals and Narrative Dynamics in MallWorld Dreams: A Corrected Re-analysis

*Report of the October 2026 audit. It replaces four archived reports: "Entity Ecology in MallWorld Dreams", "Sequence Motifs in MallWorld Dreams", "Emergent Structure in Recurring Dream Environments", and §§4–6 of "Correspondential Structure in Collective Dream Space". The archived reports are in `reports/archive/`. The withdrawn figures are listed in Appendix B and in `docs/STATISTICAL_AUDIT_2026-10.md`.*

## Abstract

**Background**: The archived MallWorld reports made strong claims about the beings, animals and dynamics of dream environments:
- entities behave "autonomously", the same at every level and atmosphere;
- animals are "completely independent of environmental atmosphere" and "represent the dreamer" (ICC 0.630);
- dreamer identity explains 56.4% of atmosphere variance;
- dreams fall into four archetypes and loop through "trap" locations.

The audit found that these claims rest on a join that attached each entity to locations from other dreams, a binning error, label repetition, and variance components that confuse the dream with the dreamer.

**Methods**: The study uses 1,918 primary dream reports, 3,696 entity involvements and 6,056 interactions, keyed correctly by dream and location. Every archived figure is first reproduced on its own construction and then re-estimated. Re-estimation uses unique entity-type occurrences, logistic regression clustered by dream and adjusted for narrative length, chance-corrected variance components, within-dream permutation nulls, conditional logit, silhouette and bootstrap stability for clusters, and parallel analysis for components.

**Results**:
- **Entities.** Threats, creatures and authority figures appear in negative scenes (95.4%, 84.0% and 79.9% negative). Friends appear in the least negative scenes (58.0%). "Guides 0% hostile, threats 94% hostile" follows from the labels, and the "flat" profiles across levels came from the join bug. Authority functions do not follow the framework's prediction (guiding or observing 55.0% below ground vs 35.7% above; OR 0.46, p = 0.24).
- **Animals: independence reversed.** The archived "independence" was a single-category table filled in as χ² = 0. Corrected, hostile creatures appear at 59.0% of negative locations and 15.8% of non-negative ones (OR 7.69, 1.55–38.3).
- **Animals: dreamer clustering withdrawn.** The "ICC 0.630" was not an intraclass correlation. A proper estimate is 0.130 (p = 0.30; 8 authors).
- **Atmosphere variance.** "Dreamer 56.4%" was a within-dream effect inflated by small groups. Corrected:
  - within dream: ICC 0.314;
  - same author across dreams: 0.094–0.183;
  - location type: 0.058.
- **Narrative dynamics.**
  - Arc shapes are what random ordering produces, except that continuous descent is more common than chance.
  - "Loops" and "traps" are repeated type labels, mostly "other", only 2–5 points above a shuffled null.
  - The four "archetypes" have silhouettes of 0.11–0.16, which indicates no cluster structure.
  - "Social interactions in malls, z = +22.8" came from the join bug; corrected, OR 1.14 (n.s.).

**Conclusions**:
- **Fits the framework:** beings and animals co-vary with the state of the scene, as the framework holds that surroundings correspond to the state of those present. The archived reports had inverted this with a bug.
- **Miss:** authority functions do not differentiate by height.
- **Not observed, and not a framework prediction:** a characteristic arc. Arcs are not structured beyond chance, but Swedenborg's texts predict no dream arc.
- **Withdrawn:** most dynamical "discoveries" (Markov attractors, loop hubs, archetypes) restate label frequencies.

**Keywords**: MallWorld, dream entities, animal correspondences, Swedenborg, variance components, join error, clustered inference, narrative arcs

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| Dream reports (N=1,918 primary) | r/TheMallWorld (Reddit) | `data/mallworld/` |
| Structured extraction | GPT-5.2 via Azure OpenAI | `projects/mallworld/structured/` |
| Verified loader | `scripts/mallworld_dataset.py` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/scripts/mallworld_dataset.py) |
| Entities and animals | `notebooks/03_entities_and_animals.ipynb` | Repository |
| Sequences and dreamer effects | `notebooks/04_sequences_and_dreamer_effects.ipynb` | Repository |
| Exploratory report claims | `notebooks/06_exploratory_report_claims.ipynb` | Repository |
| Reliability | `notebooks/08_extraction_reliability.ipynb` | Repository |

---

## 1. Introduction

### 1.1 Background

Dreams in the MallWorld corpus are populated: 66.5% of primary dream reports contain at least one coded entity (3,696 involvements in 1,275 dreams). Entities are recorded inside interactions, so one entity can appear several times. Their dreams also unfold in sequences of locations. The archived reports drew far-reaching conclusions from both: entity "autonomy", animals as "dreamer affections", atmosphere as a projection of "ruling love", and a "grammar" of dream movement.

The audit (notebook 01, D6) found that `location_id` values such as `loc_1` repeat across dreams. Joining entities to locations on that key alone produced 7,158,025 rows from 4,235 involvements. Each entity was compared with environments from other people's dreams, so any "invariance across environments" built on that join is guaranteed.

### 1.2 Theoretical Framework

In Swedenborg's account, the things that appear around spirits correspond to their interior state (*Heaven and Hell* §§173–176). Animals in particular correspond to affections: gentle and useful animals to good affections, fierce and harmful ones to evil affections (§110). Beings encountered after death have differentiated functions. Newcomers are met by friends (§494) and attended by angels (§§449–450). A person's ruling love persists (§§477–479).

This gives directional expectations for dream entities:
- **Co-variation:** beings and animals should co-vary with the quality of the scene, not be independent of it.
- **Persistence:** a person's environments should be somewhat consistent across dreams.
- **Function:** functions of beings should differ in the expected direction, for example guiding above and blocking or punishing below. In heaven the governors "minister and serve" (§218); the hells are ruled by fear of punishment, with the more wicked set over the rest (§543).

The texts give no characteristic order of scenes within a dream. Swedenborg's sequence of states is the three states after death in the world of spirits, which some skip (§491). Arc types are therefore tested here as claims of the archived sequence report, not as framework predictions (`CLAUDE.md` §3, "Find the prediction in the text").

The archived reports did not state these expectations in advance. In several places they reinterpreted results against them. The tests registered in advance are reported in the companion report on pre-registered tests.

### 1.3 Aims

1. Reproduce each archived entity, animal, variance and sequence figure on its own construction, and identify what it measured.
2. Re-estimate the answerable questions with the correct key, clustered inference and length adjustment.
3. Record which claims are built into the coding categories.

---

## 2. Methods

### 2.1 Data Sources

The data are 1,918 primary dream reports (8,685 locations, 1,303 authors), loaded through the verified loader. Entities and interactions are keyed by `(post_id, location_id)`.

### 2.2 Coding Scheme

**Labels with built-in behaviour.** Several entity types carry their behaviour in their labels:
- `threat` (schema comment: "hostile entity");
- `guide` ("someone helpful");
- `watcher` ("observer entity").

Associations between these types and demeanor, or between threats and threatening atmospheres, are partly definitional. They are reported as coder consistency.

**Atmosphere** is the loader's valence:
- negative: threatening, oppressive, uncomfortable, wrong, eerie, chaotic;
- non-negative: neutral, welcoming, peaceful.

**Animal classes** use the whole-word lists fixed in the pre-registration (`docs/PREREGISTRATION_2026-10.md`).

### 2.3 Statistical Analysis

**Units.** Rates of entity types at locations use unique (dream, location, entity type) triples.

**Inference.** Inference is clustered by dream throughout, with logistic regression adjusted for log word count.

**Variance components.** These are reported as:
- chance-corrected η², against permutation nulls;
- ICC1 within dreams;
- ICC1 across dreams of the same author.

**Sequences.** Sequences follow list order. Where `visit_order` is given for every location of a dream, it agrees with list order in 98.0% of dreams. Sequence claims are tested against nulls that shuffle labels across the corpus or order within each dream.

**Clustering and components.**
- Clustering is assessed with silhouette width and bootstrap adjusted Rand index.
- Principal components are retained by parallel analysis.

---

## 3. Results

### 3.1 Dream-Level Effects of Entities Are Mostly Narrative Length

The archived dream-level figures reproduce (notebook 03, E1). Dreams with a threat have more locations (5.39 vs 4.44) and a higher share of threatening locations (35.3% vs 6.7%). Dreams with a family member also have a higher share (15.3% vs 9.0%). But dreams with entities are longer: the median is 232 words with a threat against 143 without. Length adjustment changes the picture:

| Entity in the dream | Location coded threatening, length-adjusted OR (95% CI) |
|-------------------------|----------------------|
| Threat | 5.14 (4.11–6.43) |
| Authority | 1.34 (1.06–1.68) |
| Family member | 1.28 (0.92–1.77); 1.01 among dreams with any entity |

Where a family member actually appears, the location is negative in 68.6% of cases, against 67.2% for other locations in dreams with entities (OR 1.06, p = 0.77).

**Finding (statistically supported):** Threats go with threatening locations, which is close to definitional. The "family paradox" is withdrawn: it compared entity-rich long dreams with short dreams that have no entities.

### 3.2 Entity Types and the Atmosphere of the Scene

| Entity type | Locations | Dreams | Negative atmosphere (95% CI) |
|-------------------------|----------------------|----------------------|----------------------|
| Threat | 219 | 166 | 95.4% (93–98) |
| Creature | 100 | 86 | 84.0% (76–92) |
| Authority | 279 | 210 | 79.9% (75–85) |
| Crowd | 547 | 420 | 72.6% (69–76) |
| Family member | 121 | 102 | 68.6% (61–77) |
| Stranger | 499 | 370 | 66.3% (62–71) |
| Friend | 50 | 45 | 58.0% (44–72) |

The archived χ² = 792 (df = 99) treated nested involvements as independent, and 53% of the cells in its table have an expected count below 5.

**Finding (statistically supported):** Threats, creatures and authority figures appear in negative scenes; friends, strangers and family in less negative ones. **Interpretation:** this fits the correspondence of surroundings to the state of those present. It also fits the ordinary reading that a hostile guard makes a scene unpleasant. The deceased are tested in the pre-registered report (P3, a hit).

### 3.3 "Entity Autonomy" Is a Join Artifact and a Definition

| Claim | Archived basis | Corrected |
|-------------------------|----------------------|----------------------|
| Guides 0% hostile, threats 92–94% hostile "at all levels" | Labels; join bug | Guides 0.0% (32 involvements, 17 dreams); threats 93.8% (306, 187); built into the labels |
| Hostility flat across levels | Join on `location_id` only: 19.7 / 19.5 / 19.6% (7,158,006 rows) | Correct key: 21.8 / 20.2 / 19.5% (4,208 rows); within types, CIs up to 53 points wide |
| Threats present at 8.6% of every atmosphere | Join bug | 7.6% of negative, 0.5% of neutral, 1.1% of positive locations |
| Guides at 5.2–5.3% of every level | Join bug | 18 located guide involvements in 10 dreams; not estimable |
| Authority functions identical at all levels (p = 0.78) | Join bug | χ²(8) = 9.2, p = 0.33, 27% sparse cells; see below |

The archived notebook stated a prediction for authority figures before the join was introduced: guiding and observing above; blocking, pursuing and punishing below. Its own correctly joined run gave χ²(8) = 13.42, p = 0.098, with residuals *opposite* to the prediction. The thesis instead reported the join result and labelled it as support for entity autonomy. On the primary population, the guiding-or-observing share of authority functions is 55.0% below ground, 43.1% at ground and 35.7% above ground (above vs below OR 0.46, 0.12–1.71, p = 0.24; 134 involvements in 93 dreams).

**Finding (statistically supported):** No evidence for entity autonomy, and none against it: the data are too thin to show either invariance or variation. **Verdicts:**
- entity autonomy: **underdetermined**;
- authority function by height: **miss in direction, not significant**.

### 3.4 Entity Types by Height

The archived χ² = 41.13 (df = 22, p = 0.0079) reproduces exactly on its own construction: 1,245 involvements nested in 535 dreams, up to 16 per dream. Earlier project documents attributed this statistic to the NDE entity-function claim. It belongs to the MallWorld vertical report.

On unique (dream, location, type) triples, creatures are 8.3% of entity types below ground, 4.6% at ground and 5.9% above ground (below vs ground OR 1.90, 1.00–3.61, p = 0.05). Authority figures are 10.6% / 11.3% / 14.5% (above vs ground OR 1.33, p = 0.18).

**Finding (statistically supported):** Creatures lean slightly below ground (borderline). Authority figures are not more common above. The archived "creatures below, authority above" was not pre-registered: its plan was written after the vertical report. **Verdicts:**
- creatures below: **borderline (exploratory)**;
- authority above: **not supported**.

The registered test that noxious animals appear below ground was a **miss** (P2).

### 3.5 Interactions

Outcomes are coded for 48.1% of interactions.
- **Helpful vs hostile entities.** With a helpful or friendly entity, 88.8% of interactions succeed; with a hostile or threatening one, 57.5% (clustered, length-adjusted OR 5.87, 3.77–9.13). The thesis's 49.7% vs 29.7% included "not mentioned" and "ongoing" in the denominator, and duplicated interactions through a join.
- **Entity type.** Success differs by entity type (joint χ²(11) = 31.6, p = 0.0009). The archived ranking with "family lowest" does not reproduce.
- **Height.** Success does not differ by level (OR 0.82 below and 0.79 above, vs ground).
- **The deceased.** None of the 52 interactions involving a deceased person is a conflict. At the base rate (5.6%), 2.9 conflicts would be expected; the probability of none is 0.050.

**Finding (statistically supported):** Help makes tasks succeed, which is not a framework test. The absence of conflict with the deceased is in the framework's direction (*Heaven and Hell* §494) but weak, and was not specified in advance.

### 3.6 Animals

**Type and demeanor.** On the primary population the archived keyword scheme gives V = 0.500. That scheme filed "attack", "aggressive" and "evil" under predators and monsters, and matched by substring. With behaviour words removed and whole-word matching, V = 0.492: the association does not depend on the circular keywords. "Predator vs cat OR = 106:1" rests on a zero cell (cats 0 of 17 hostile), so the OR is unbounded. With the pre-registered classes, 46.4% of noxious and 11.5% of gentle creatures are hostile (OR 6.69, 1.98–22.6).

**Atmosphere.** The archived test cut dream means on a 1–5 scale at −0.5 and 0.5, so every creature fell into one bin. The notebook printed "Insufficient data for chi-square" and then set χ² = 0 and p = 1. The thesis reported that placeholder as "complete independence". Corrected:

| Location atmosphere | Hostile creatures (95% CI) | n (dreams) |
|-------------------------|----------------------|----------------------|
| Negative | 59.0% (48.0–70.1) | 105 (74) |
| Non-negative | 15.8% (0.0–37.7) | 19 (14) |

The OR is 7.69 (1.55–38.3), p = 0.013. Across 92 dreams, creatures are also more hostile where the other entities are hostile (r = 0.317, p = 0.002).

**Dreamer clustering.**
- **Archived "ICC" (0.630; 0.616 on the primary population).** It divides the variance of author means over all authors, 80 of 117 of whom have one creature, by that variance plus the mean within-author variance. It is not an intraclass correlation.
- **Authors with more than one creature.** Of the 37 such authors, 29 have them all in one dream.
- **Omitted result.** The archived notebook's own proper estimate (0.207, 95% CI 0.000–0.620, "consistency not established") was left out of the thesis.
- **Corrected.** ICC1 = 0.130, permutation p = 0.30 (21 dreams, 8 authors).
- **"89.5% between dreamers, within-dreamer r = 0.753."** In the same data, 76 of 92 dreams come from authors with one such dream, whose deviation is zero by construction. Within authors who have more, r = 0.135 (p = 0.62).

**Finding (statistically supported):** Animal type predicts demeanor, which is close to definitional. Animals co-vary with the atmosphere of the scene and with the other beings in it. Whether they cluster by dreamer cannot be estimated. **Verdicts:**
- "independence from atmosphere": **reversed**;
- dreamer clustering: **underdetermined**.

**Interpretation:** co-variation is what the framework predicts (*Heaven and Hell* §110, §§173–176). The archived reading, that animals are "independent of the environment" and "represent the dreamer", was built on a bug and also departed from the framework.

### 3.7 Who Explains the Atmosphere?

The archived η² values reproduce: dream 0.544 (archived 0.564) and location type 0.068 (archived 0.071). With 4,293 locations in 1,376 dreams, a grouping that explains nothing yields η² = 0.320.

| Source | Estimate |
|-------------------------|----------------------|
| Same dream (ICC1) | 0.314 (chance-corrected η² 0.329) |
| Same author, different dreams (ICC1) | 0.183 on the 5-point scale (573 dreams, 185 authors); 0.094 on the valence scale (P4, a hit) |
| Location type (chance-corrected η²) | 0.058 |

**Other archived "ruling love" figures.**
- **Congruent fear across a dreamer's locations (archived ICC 0.327).** The archived test used two non-schema atmosphere values and three non-schema affect values. On schema values, consistency across a dreamer's dreams is ICC1 = 0.041 (p = 0.22).
- **The R4 null (partial ρ = 0.007).** The same cell printed a significant alternative specification (ρ = 0.053, p = 0.0077), which was not reported. Corrected, negative affect at one location predicts a negative atmosphere at the next, beyond the current atmosphere. The OR is 2.09 (1.59–2.75) across 1,740 pairs, and 1.62 (1.09–2.42) within dreams.
- **No source.** The thesis's figures for "ruling love markers" (F = 47.82, η² = 0.136), "partial r = 0.751", hierarchical R² 0.398, congruence χ² = 54.17 and "partial r = 0.186 / 0.261" appear in no notebook output.

**Finding (statistically supported):** Atmosphere clusters strongly within a dream. It clusters weakly but reliably within an author's different dreams, and that author-level clustering is larger than the effect of location type. **Interpretation:** persistence across a person's dreams fits the framework's ruling love (*Heaven and Hell* §§477–479), and equally fits temperament or writing style.

The R4 reversal is **interpretation**: affect leading the next scene fits the principle that surroundings follow the state of the person. The archived test assumed the opposite and read a null as strong support. This analysis is exploratory, and affect is the least reliable field (κ 0.67 where both coders coded it).

### 3.8 Narrative Dynamics

- **Entries and exits.** Dreams begin in malls far more often than they end there (25.6% vs 5.8% of first vs last locations). They end in the residual category "other" far more often than they begin there (35.9% vs 15.6%). "Other" covers 2,217 distinct place names. **Descriptive**; the corpus starts in malls by definition.
- **"Loops" and "traps."**
  - The archived figures reproduce (43.7%, 30.4%, 19.6% of dreams), but they count repeated type labels, not returns. Of the "traps", 66.1% are the label "other".
  - Against a null that shuffles labels across the corpus, the excess is 2–5 percentage points (repeat 43.7% vs 38.5%).
  - Connections leading back to an earlier location occur in 23.7% of dreams with connections.
- **Markov dynamics.** The stationary share of "other" (30.7%) restates its frequency as a transition target (29.2%). "Attractors", "gravitational centres" and first-passage times describe label frequencies.
- **Arcs.**
  - Shuffling each dream's atmospheres into random order reproduces the archived arc distribution almost exactly: complex 36.0% vs 35.0%, rise–fall 17.9% vs 18.8%, descent–recovery 17.4% vs 18.9%.
  - The only departure is an excess of continuous descent: 7.4% against a null range of 3.2–6.9%, and 8.6% (3.5–6.7%) with all negative atmospheres included.
  - The archived transition count reproduces (927 vs 1,075, p = 0.0010) but treats transitions as independent. With the dream as the unit, 175 dreams worsen on balance and 130 improve (p = 0.012). The report's "529 vs 456" appears in no output.
- **Archetypes and components.**
  - Silhouette widths are 0.11–0.16 for k = 2–8, which indicates no cluster structure. k = 4 is preferred by no criterion.
  - The four clusters partly separate long from short reports: median 521 vs 98 words; η² of log length 0.266.
  - Parallel analysis retains 7 components, not 4.
- **Social space.** "Social interactions are dramatically elevated in malls (z = +22.82)" came from the join bug. Corrected: 14.3% vs 12.9%, OR 1.14 (p = 0.22).

**Finding (statistically supported):** Apart from a modest within-dream decline, an excess of continuous descent, and some adjacency of same-type locations beyond composition (school lift 3.79 vs 2.32 under shuffling), the archived dynamical structure restates label frequencies and chance. **Verdict:**
- **Not observed:** a characteristic arc or stage sequence. This is not a framework prediction: the arc types come from the archived report's dramatic-structure analysis, not from Swedenborg (§1.2). The NDE project reached the same conclusion about stage order.
- **Underdetermined:** the decline.

---

## 4. Discussion

### 4.1 Summary of Findings

| Claim | Result | Verdict |
|-------------------------|----------------------|----------------------|
| Beings co-vary with the scene | Threats 95.4%, creatures 84.0%, friends 58.0% negative | Fits framework (non-discriminating) |
| Entity autonomy | Join artifact; current data too thin | Underdetermined |
| Authority guides above, punishes below | 55.0% below vs 35.7% above guiding or observing | Miss in direction (n.s.) |
| Animals independent of atmosphere | Hostile creatures 59.0% vs 15.8%, OR 7.69 | Reversed |
| Animals cluster by dreamer | ICC 0.130, p = 0.30, 8 authors | Underdetermined |
| Dreamer explains 56.4% | Dream 0.314; author 0.094–0.183; type 0.058 | Withdrawn; author effect a hit (P4) |
| No conflict with the deceased | 0 of 52 vs 2.9 expected, p = 0.050 | Weak, framework direction |
| Characteristic arc or stage sequence | Same as random order, except more descent | Not observed (not a framework prediction) |
| Four archetypes; four dimensions | Silhouette ≤ 0.16; 7 components | Withdrawn |

### 4.2 Interpretation

The largest change concerns animals. The archived thesis made animals its "strongest signal". Its argument was that animals are independent of the environment and cluster by dreamer, and so represent the dreamer's affections rather than the place. Both premises were artifacts. Corrected, animals behave as Swedenborg's own rule predicts: fierce, hostile animals appear in negative scenes and alongside hostile beings. In the framework, what appears around a person corresponds to the state of those present (*Heaven and Hell* §110, §§173–176). The data show co-variation of animals with the scene. Whether that scene's state is the dreamer's own cannot be separated with these data, because only 8 authors have creatures in more than one dream.

The same pattern holds for beings generally, and for the dreamer's affect leading the next scene. MallWorld environments are coherent wholes: beings, animals, affect and atmosphere move together. That coherence is what correspondence predicts. It is also what any well-formed narrative, and any coder reading a single sentence, would produce. The data establish **pattern fit**, not mechanism.

Where the framework makes a prediction about height, it fails:
- authority function by height (wrong direction);
- creatures below (borderline), with noxious animals below a registered miss.

No characteristic arc is found, but the texts predict none, so that result is not scored against the framework. In the NDE project, the structural "misses" turned out not to be Swedenborg's predictions, and no miss among the framework's own predictions remains there (`CLAUDE.md` §6.1). The height results in MallWorld are therefore the clearest failures of the framework's own predictions in the repository. The spatial report reaches the same conclusion for atmosphere and light.

### 4.3 Implications

- **Keys.** Any analysis joining entities, interactions or connections to locations must key on `(post_id, location_id)`. The loader enforces this.
- **Variance components.** These must be corrected for chance and must separate the dream from the dreamer. With 79% of authors posting once, "dreamer" effects are mostly dream effects.
- **Sequences.** Sequence claims need a shuffled-order null. Claims about "other" need a check that they are not artifacts of a residual category.

### 4.4 Limitations

- **Same-source coding.** All variables are coded from one narrative by one model.
- **Measured reliability** (notebook 08):
  - **Threat type.** It agrees only moderately with a second coder's "hostile entity present" (κ 0.50; κ 0.71 when any hostile-demeanor entity counts). Analyses using the `threat` label alone cover only part of hostile encounters.
  - **Atmosphere and affect.** Where both coders rated, κ is 0.75 for atmosphere and 0.67 for affect. GPT-5.2 rated both about twice as often, by inference.
- **Small groups.** Animal, guide, deceased and authority-function results rest on 10–100 dreams each.
- **Exploratory status.** Except where cross-referenced to the pre-registered tests, every analysis here is a re-estimation, not a registered test.

### 4.5 Future Directions

- **Code functions per entity.** Code entity functions (guiding, blocking, punishing) per entity with a defined boundary, and test authority function by height on posts collected after a cut-off date.
- **Detect animals with a coder.** Replace word lists with coder judgements and pre-register the animal–atmosphere and animal–dreamer tests.
- **Follow repeat dreamers.** Collect repeated dreams from the same authors to separate dreamer from dream.

---

## 5. Conclusion

The archived picture of autonomous entities, dreamer-bound animals and a structured dream grammar does not survive correction.
- **What remains:** beings, animals and affect co-vary with the atmosphere of the scene. Fierce animals and hostile beings appear in negative scenes, and friends and the deceased in less negative ones. This fits the framework's claim that surroundings correspond to the state of those present, and it reverses the archived "independence".
- **Height:** authority function by height is a miss. No characteristic arc is found, and none is predicted by the texts.
- **Dynamics:** most dynamical structure is chance or label frequency.

---

## References

Bergsma, W. (2013). A bias-correction for Cramér's V and Tschuprow's T. *Journal of the Korean Statistical Society*, 42(3), 323–328.

Horn, J. L. (1965). A rationale and test for the number of factors in factor analysis. *Psychometrika*, 30(2), 179–185.

Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika*, 73(1), 13–22.

Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53–65.

Swedenborg, E. (2000). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation. (Original work published 1758)

Swedenborg, E. (2005). *Heaven and its Wonders and Hell* (J. C. Ager, Trans.). Project Gutenberg, eBook #17368. (Original work published 1758). Quotations in this report follow this translation.

---

## Appendix A: Statistical Summary

| Test | Estimate | Interval / p | n |
|-------------------------|----------------------|----------------------|----------------------|
| Threat in dream → threatening location, OR | 5.14 | 4.11–6.43 | primary |
| Family member present at location → negative, OR | 1.06 | p = 0.77 | — |
| Authority guiding or observing, above vs below, OR | 0.46 | 0.12–1.71, p = 0.24 | 134 (93 dreams) |
| Creature share, below vs ground, OR | 1.90 | 1.00–3.61, p = 0.05 | 953 (478 dreams) |
| Success, helpful vs hostile entity, OR | 5.87 | 3.77–9.13 | 665 involvements |
| Hostile creature, negative vs non-negative atmosphere, OR | 7.69 | 1.55–38.3, p = 0.013 | 124 |
| Creature hostility, author ICC1 | 0.130 | p = 0.30 | 21 dreams, 8 authors |
| Atmosphere, within-dream ICC1 | 0.314 | — | dreams with ≥ 2 coded locations |
| Atmosphere, across-dream author ICC1 (5-point) | 0.183 | — | 573 dreams, 185 authors |
| Next location negative, negative affect, OR (within dream) | 1.62 | 1.09–2.42, p = 0.017 | 183 dreams |
| Dreams worsening vs improving | 175 vs 130 | p = 0.012 | 896 dreams |
| k-means silhouette, k = 2–8 | 0.11–0.16 | — | 1,918 |
| Components retained (parallel analysis) | 7 | — | 20 features |
| Social interaction in mall, OR | 1.14 | 0.92–1.42 | primary |

## Appendix B: Withdrawn Figures

| Archived claim | Why withdrawn | Corrected |
|-------------------------|----------------------|----------------------|
| Entity autonomy: guides 0%, threats 92–94% hostile at all levels; authority p = 0.78 | Labels; join bug | §3.3 |
| Entity × vertical χ² = 41.13 (attributed elsewhere to NDE) | Nested involvements; a MallWorld statistic | §3.4 |
| Entity × atmosphere χ² = 792 (df = 99), χ² = 330 (df = 121) | Sparse and nested | §3.2 |
| "Family paradox" 15.3% vs 9.1% | Length and entity presence | §3.1 |
| Helpful 49.7% vs hostile 29.7% success (χ² = 48.90) | Denominator; duplicated join | 88.8% vs 57.5% |
| "Friends 87.4%, family lowest 70.3%" | Not reproducible | §3.5 |
| Animal type V = 0.513; predator vs cat OR = 106:1 | Circular keywords; zero cell | V = 0.492; OR unbounded |
| Animals independent of atmosphere (χ² ≈ 0, p = 1.0) | Binning error; placeholder value | OR 7.69 |
| Animal ICC = 0.630; H = 70.91; η² = 0.605 | Not an ICC; within-dream; proper ICC omitted | ICC 0.130 (p = 0.30) |
| Animal variance 89.5% between dreamers; r = 0.753 | Single-dream authors have zero deviation | r = 0.135 (p = 0.62) |
| Dreamer explains 56.4%, location 7.1% | Dream, not dreamer; small-group inflation | §3.7 |
| Ruling-love ICC = 0.327 | Non-schema values; within-dream | ICC 0.041 (p = 0.22) |
| R4 partial ρ = 0.007 "strongly supports ruling love" | Null read as support; significant alternative unreported | §3.7 |
| F = 47.82, η² = 0.136; partial r 0.751, 0.312, 0.186, 0.261; R² 0.398; χ² = 54.17 | In no notebook output | — |
| Loops 30.2%, traps 19.5%, "other" hub 58.7% | Repeated labels | §3.8 |
| "Other" stationary state 31.7%; mall "gravitational centre" | Label frequency | §3.8 |
| Oscillatory arcs dominate; monotone arcs rare | Same under random order | §3.8 |
| Worsening 529 vs 456 (p = 0.0010) | In no output; output was 1,080 vs 931, not clustered | 175 vs 130 dreams |
| Four dream archetypes; four latent dimensions | No cluster structure; number imposed | §3.8 |
| Social interactions in malls z = +22.82 | Join bug | OR 1.14 |
