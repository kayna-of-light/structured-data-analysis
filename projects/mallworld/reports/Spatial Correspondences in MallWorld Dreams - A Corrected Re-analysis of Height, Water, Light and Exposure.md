# Spatial Correspondences in MallWorld Dreams: A Corrected Re-analysis of Height, Water, Light and Exposure

*Report of the October 2026 audit. It replaces the spatial sections of four archived reports: "Correspondential Structure in Collective Dream Space" (§3), "Vertical World Structure in MallWorld Dreams", "Ontological Versus Cultural Structure in MallWorld" and "Emergent Structure in Recurring Dream Environments" (§3.1). The archived reports are in `reports/archive/`. The withdrawn figures are listed in Appendix B and in `docs/STATISTICAL_AUDIT_2026-10.md`.*

## Abstract

**Background**: Swedenborg's doctrine of correspondences holds that the surroundings of a spirit correspond to its interior state. Applied to recurring dream environments, it predicts systematic links between spatial features (height, water, light, exposure) and the felt atmosphere of a place. Archived reports on the r/TheMallWorld corpus described these links as robust: "vertical position ρ = 0.25–0.30, replicated across splits", water "2.6×", exposure "3.5×". An audit found that the main analyses had been run on a population that included 750 non-dream posts. It also found headline figures that no notebook produced, and every test treating locations from the same dream as independent.

**Methods**: The study uses 1,918 dream reports with at least one coded location (8,685 locations, 1,303 authors), after removing non-dream posts and exact duplicates. Associations between GPT-5.2-coded features and location atmosphere were estimated with logistic regression, with standard errors clustered by dream and adjustment for log narrative length. Height effects were re-estimated with location type controlled, without location types that are vertical by definition, and within dreams by conditional logit. Robustness to authors and time was re-examined with permutation nulls and an equivalence margin.

**Results**:
- **Height.** The relation is not a gradient. Underground locations are negative more often than ground-level ones (76.0% vs 58.3%; OR 1.69–2.29 across specifications), including when basements, caves and subways are excluded. Elevated locations are not better than ground (65.2%; OR 1.29–1.35). Within a dream, going up does not improve the atmosphere (OR 0.88 per level, 95% CI 0.72–1.07). The correlation is ρ = 0.064 (0.007–0.114), not 0.25–0.30.
- **Water.** Turbid water goes with negative atmospheres: 84.4% vs 43.0% (OR 7.19). Clear vs murky water in free text gives 20.6% vs 73.1% negative.
- **Light.** Darker light goes with worse atmospheres (ρ = −0.49; OR 3.94 per step). So does cold white light compared with warm light (70.8% vs 33.1% negative), but warm light is not more common above ground.
- **Exposure.** Exposed locations, mostly bathrooms, are more often negative: 87.1% vs 53.5% (OR 6.35).
- **Cleanliness.** The association with height disappears once location type is controlled (OR 1.02).
- **Location type.** Location type carries atmosphere information beyond each dream's overall tone, and the location-type association is equivalent across time (ΔV = +0.015, 90% CI −0.002 to 0.040).

**Conclusions**:
- **Hits at the level of pattern fit:** the framework's qualitative correspondences (turbid water, darkness and cold light, exposure).
- **Partial hit:** its vertical correspondence holds only below ground.
- **Misses:** "higher is better" and "warm light above".
- **Not supported:** a vertical gradient in cleanliness.

None of these tests separates the framework from ordinary associations of murk, darkness and exposure with unpleasantness. Most of them use codes that GPT-5.2 inferred rather than read directly.

**Keywords**: MallWorld, collective dreams, correspondences, Swedenborg, vertical symbolism, clustered regression, narrative length, reproducibility audit

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| Dream reports (N=1,918 primary; 3,732 posts extracted) | r/TheMallWorld (Reddit) | `data/mallworld/` |
| Structured extraction | GPT-5.2 via Azure OpenAI, schema `models/questionnaire.py` | `projects/mallworld/structured/` |
| Verified loader | `scripts/mallworld_dataset.py` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/scripts/mallworld_dataset.py) |
| Population audit | `notebooks/01_data_audit.ipynb` | Repository |
| Spatial analyses | `notebooks/02_spatial_affective_correspondences.ipynb` | Repository |
| Robustness and time | `notebooks/05_robustness_time_and_nde_comparison.ipynb` | Repository |
| Reliability | `notebooks/08_extraction_reliability.ipynb`, `validation/` | Repository |

---

## 1. Introduction

### 1.1 Background

r/TheMallWorld is an online community in which people describe recurring dreams of vast, interconnected malls, hotels, schools and transit spaces. Its 3,732 posts were coded with GPT-5.2 into locations, connections, entities and qualities. Earlier work on this corpus reported strong correspondences between space and atmosphere and presented them as support for Swedenborg's framework.

The October 2026 audit (`docs/STATISTICAL_AUDIT_2026-10.md`) found that the main thesis population of 2,678 posts included 453 questions, 167 AI-generated visualisations, 38 map-only posts and other non-dreams. Together these supplied 23.3% of its locations (notebook 01, D1). Several headline figures appear in no notebook output. All tests counted locations from the same dream as independent observations. This report re-estimates the spatial claims on a defined population, with methods that respect the structure of the data.

### 1.2 Theoretical Framework

In *Heaven and Hell* (Swedenborg, 1758), the things that appear around angels and spirits correspond to their interiors (§§173–176). Light in heaven corresponds to wisdom, and heat to love (§§126–140). The project framework (CLAUDE.md §9) reads vertical space as discrete degrees: higher states above, lower states and proximity to self-love below. Water is a standard correspondence for truth in Swedenborg's exegesis: clear when the truth is genuine, turbid when it is falsified. Read as hypotheses about dream environments, these give testable predictions:

| Correspondence | Prediction | What would count as a miss |
|---|---|---|
| Height ↔ state | Lower locations more negative, higher locations less negative than ground | No difference, or elevated no better than ground |
| Water ↔ truth | Turbid water more negative than clear water | No difference |
| Light ↔ wisdom; heat ↔ love | Dark and cold light more negative; warm light more common above | No difference; warm light not more common above |
| Exposure ↔ shame | Exposed locations more negative | No difference |
| Cleanliness ↔ purity, by height | Dirt more common below | No height difference after location type |

The archived analyses did not state these predictions before testing them. This report therefore treats them as **confirmatory in direction but not pre-registered**. The pre-registered tests are reported separately.

**Competing readings.** Murky water, darkness, dirt and exposure are unpleasant in ordinary experience, and dream narratives are written by people who share those associations. A cultural or psychological account predicts the same signs. The tests here can establish **pattern fit**. They cannot establish that the framework, rather than ordinary association, produces the pattern.

### 1.3 Aims

1. Define the analysis population and its measurement limits.
2. Re-estimate each spatial correspondence with dream-clustered inference and length adjustment.
3. Separate correspondences of *height* from properties of particular *location types*.
4. Re-examine the robustness claims about authors and time.

---

## 2. Methods

### 2.1 Data Sources

All 3,732 extracted posts were loaded through the verified loader `scripts/mallworld_dataset.py`. It checks every comparison against the schema's enumerations, keys entities and interactions by dream *and* location, and marks duplicates.

The **primary population** contains dream reports (`dream_report` or `dream_report_with_map`) with at least one location, excluding 8 exact duplicate submissions. That gives N=1,918 dreams, 8,685 locations and 1,303 authors.

The median report has 150 words. Length correlates with the number of locations (ρ = 0.55), and the share of locations with a coded atmosphere rises from 31.1% to 61.9% across length quartiles (notebook 01, D2).

### 2.2 Coding Scheme

**Atmosphere** is collapsed to a valence:
- negative: threatening, oppressive, uncomfortable, wrong, eerie, chaotic;
- non-negative: neutral, welcoming, peaceful;
- excluded: nostalgic and not mentioned.

**Vertical position** is mapped to below ground (lowest, lower), ground, and above ground (upper, uppermost).

Every rate in this report is conditional on the feature being coded. Coverage, as a share of all 8,685 locations, is:
- atmosphere 49.4%, vertical level 34.3%, light 18.3%;
- light temperature 8.3%, cleanliness 7.9%;
- privacy status 4.1%, somatic response 3.0%.

**Priming.** The extraction prompt labelled several fields with their framework meaning. Warm light "indicates Charity/Good". Exposure is "shameful" or "hellish". Verticality was to be inferred from location type. A third of underground-coded locations (32.5%) are basements, caves, subways, parking structures or generic "underground" places (notebook 01, D5).

**Reliability.** Inter-coder reliability of the fields is reported in §4.4 and in the companion reliability report.

### 2.3 Statistical Analysis

**Units and clustering.** Locations are nested in dreams: atmosphere ICC1 = 0.31 within dreams, a design effect of about 1.6 (notebook 01, D3). Associations are therefore estimated by logistic regression with standard errors clustered by dream, or with dream-level bootstrap intervals.

**Height.** Every model adjusts for log word count. Height effects are estimated in five specifications:
- crude;
- length-adjusted;
- with location type controlled;
- without intrinsically vertical location types;
- within dreams, by conditional logit.

**Effect sizes.** Cramér's V is reported with a bias correction (Bergsma, 2013) where tables are sparse.

**Robustness to authors and time.** Author and time effects are examined with:
- permutation nulls that shuffle atmospheres globally, within author and within dream;
- a median-date split with a dream bootstrap;
- an equivalence margin of |ΔV| < 0.05 fixed in advance.

**Test status.** These analyses are re-estimations of archived claims, not new confirmatory tests, and no multiplicity correction is applied to them. Effect sizes and intervals carry the weight.

---

## 3. Results

### 3.1 Height: Worse Below, Not Better Above

The archived computations reproduce exactly: notebook 09's "pre-registered" ρ = 0.055 and notebook 07's ρ = 0.067. The vertical report's ρ = 0.12 and the thesis's ρ = 0.25–0.30 appear in no output (notebook 02, C1).

On the primary population, 1,605 locations in 667 dreams have both a level and a valence.

| Level | Negative atmosphere (95% CI) | Positive atmosphere |
|-------------------------|----------------------|----------------------|
| Underground | 76.0% (70.3–81.7) | 9.6% |
| Ground | 58.3% (54.2–62.3) | 11.7% |
| Elevated | 65.2% (60.1–70.2) | 14.9% |

Underground locations are more often negative than ground locations in every specification:
- length-adjusted OR 2.29;
- location type controlled OR 1.79;
- intrinsically vertical types removed OR 1.69–1.76.

Elevated locations are also more often negative than ground (OR 1.29–1.35, p = 0.03–0.08). Within the same dream, a higher location is not less negative (conditional logit OR 0.88 per level, 95% CI 0.72–1.07; 111 dreams). The overall rank correlation is ρ = +0.064 (95% CI 0.007–0.114).

**Finding (statistically supported):** Atmosphere is worst below ground and best at ground level. The underground penalty survives length adjustment, location-type control and removal of basements and caves. There is no improvement above ground. **Verdict: partial hit** ("below is worse"), **miss** ("higher is better").

### 3.2 Water: Turbid Water Goes With Negative Atmospheres

The archived thesis's water-clarity × atmosphere figures ("45% vs 17%") were never computed. Computed here for the first time (notebook 02, C2):

| Water | Negative atmosphere | Positive atmosphere |
|-------------------------|----------------------|----------------------|
| Clean (pools, fountains, clear) | 43.0% | 37.6% |
| Dirty or turbid | 84.4% | 7.4% |

- **Dirty vs clean:** OR 7.19; 9.58 with location type; 6.93 without floods, tsunamis and turbulent sea.
- **Clarity in the free-text field:** clear water 20.6% negative, murky water 73.1% (Fisher OR 10.5, p = 7 × 10⁻⁵; 60 locations in 50 dreams).
- **By height:** dirty water is also more common underground (52.8% vs 18.1% at ground; OR 4.89; 3.26 without intrinsically vertical types).

**Finding (statistically supported):** Turbid water goes with negative atmospheres, and clear water with benign ones. **Verdict: hit (pattern fit).** It does not discriminate the framework from the ordinary association of murk with unpleasantness.

### 3.3 Light: Darkness and Cold Light

| Light | Negative atmosphere |
|-------------------------|----------------------|
| Bright natural | 26.2% |
| Artificial or mixed | 57.0% |
| Dim or flickering | 82.2% |
| Dark or absent | 94.8% |

The darker the light, the more negative the atmosphere: ρ = −0.49 (95% CI −0.53 to −0.44); OR 3.94 per step after length and location type. Light and atmosphere are often coded from the same sentence.

Light temperature, the framework's marker for love:
- **Atmosphere:** negative under cold white light in 70.8% of locations and under warm light in 33.1% (OR 4.88; 5.09 with location type).
- **By height:** warm light makes up 41.7% of temperature-coded light underground, 67.6% at ground and 55.6% above ground. The archived summary ticked "warm above, cold below" as "correct, Strong" without a test (notebook 02, C3).

**Finding (statistically supported):** Darkness and cold light go with negative atmospheres. Warm light is not more common above ground. **Verdict: hit (pattern fit)** for light quality and temperature; **miss** for warm light above. The light-temperature field was primed by the prompt.

### 3.4 Exposure

Among locations with a coded privacy status:
- **Bathrooms:** exposed in 84.0% of bathrooms and 14.3% of other locations. Archived notebook 09 printed 85.5% vs 14.2%; the thesis's "44.2% vs 7.5%" has no source.
- **Atmosphere:** exposed locations are negative in 87.1% of cases and private ones in 53.5% (OR 6.35). Among bathrooms alone the figures are 92.3% vs 50.0% (n=62).
- **"3.5× threatening" was a different quantity.** The thesis's figure was exposure by vertical level: 35.0% underground (n=20, 95% CI 12–58%) against 15.3–18.8% elsewhere, with overlapping intervals.

**Finding (statistically supported):** Exposure goes with negative atmosphere. **Verdict: hit (pattern fit),** weakened by priming. The prompt called exposure "shameful" and peaceful seclusion "innocent". The claim that exposure concentrates below ground is **underdetermined** (n=20).

### 3.5 Cleanliness, Somatic Distress, Decay and Compounding

- **Cleanliness.** The correlation with height is ρ = +0.238 (95% CI 0.099–0.359; 277 locations), against the archived 0.302.
  - Without intrinsically vertical types it falls to ρ = +0.111 (−0.034 to 0.250).
  - With location type controlled, the underground OR for dirt is 1.02 (p = 0.97).
  - Dirty places are negative in 95.4% of cases (OR 39.7), which is close to definitional.
- **Somatic distress.**
  - By level: 4.7% underground, 1.9% at ground, 3.3% elevated (OR 2.09, p = 0.007).
  - Not significant once sudden awakenings are excluded (OR 1.76, p = 0.11).
- **Abandoned or decaying buildings** (the thesis's "anomalous perceptual states").
  - By level: 7.1% underground, 4.1% at ground, 2.6% elevated (OR 2.13).
  - With location type controlled: OR 1.64, p = 0.06.
- **Compounding.** Negative atmosphere rises from 63.6% with no marker to 93.3% with three (ρ = −0.122).
  - Adjusted for each other, four markers carry independent weight: underground (OR 1.55), dirty water (2.48), exposure (3.34) and somatic distress (3.00).
  - Cold light does not (1.15, p = 0.39).
  - The thesis's "1.86" was the mean of the 21 locations with three markers.

**Finding (statistically supported):** Dirt belongs to particular location types, not to height. The associations of somatic distress and decay with lower levels are small and fragile. **Verdicts:**
- cleanliness by height: **not supported**;
- somatic distress: **weak partial support**;
- decay: **underdetermined**.

"Compounding" is the sum of separate associations.

### 3.6 Location Type, Movement and the Course of a Dream

**Location type.** Location type is associated with atmosphere (clustered joint test χ²(32) = 166, p = 5 × 10⁻²⁰). Concrete places are most often negative: basements 91.9%, public bathrooms 90.0%, hospitals 81.2%, schools 80.2%. Mountains (39.4%), restaurants (43.3%) and mall stores (44.5%) are least often negative. The archived 70 × 10 tables had 72–74% of cells with expected counts below 5 (notebook 02, C9; notebook 05, R1).

**Movement.** Upward and downward moves are nearly balanced (552 vs 487, p = 0.047). The direction of a move does not predict the change in atmosphere (ρ = +0.007) or the destination's atmosphere (ρ = +0.046).

**Course of a dream.** Atmosphere worsens modestly through a dream:
- mean within-dream slope −0.083 (95% CI −0.148 to −0.017);
- 56.4% of 594 dreams decline and 41.6% rise.

**Finding (statistically supported):** Location type matters, and atmosphere worsens slightly over a dream. Movement direction does not. **Verdict: underdetermined** for the decline, which fits both a framework reading (vastation) and the ordinary arc of a remembered dream.

### 3.7 Robustness to Authors and Time

**Location type × atmosphere.** The archived table reproduces: χ² = 1,729.52, df = 621, V = 0.212. Of its cells, 74% have an expected count below 5. Restricted to the 41 types with at least 20 coded locations:

| V | Value |
|-------------------------|----------------------|
| Observed | 0.195 |
| Labels shuffled at random | 0.100 |
| Shuffled within author | 0.121 |
| Shuffled within dream (99th percentile) | 0.129 (0.138) |

So location type carries information beyond each dream's tone. "Within-author" shuffling is mostly within-dream shuffling, because 53.6% of locations come from single-dream authors.

**Time.** Across a median-date split, V is 0.214 earlier and 0.229 recent (ΔV = +0.015, 90% CI −0.002 to 0.040), equivalent within ±0.05. The underground penalty holds in both periods (earlier OR 2.56, 1.56–4.20). Its ratio across periods (0.79, 0.40–1.57) is too imprecise to show equivalence. The thesis's "all Cochran's Q p > 0.50" appears in no output (notebook 05, R3).

**Finding (statistically supported):** The location–atmosphere association is not an author artifact, and it is equivalent across time. **Interpretation:** robustness to authors and time cannot separate a shared cultural schema from a correspondential structure. Both predict stability.

---

## 4. Discussion

### 4.1 Summary of Findings

| Correspondence | Result | Verdict |
|-------------------------|----------------------|----------------------|
| Below ground worse than ground | 76.0% vs 58.3% negative; OR 1.69–2.29 | Partial hit |
| Above ground better than ground | 65.2% vs 58.3%; within-dream OR 0.88 | Miss |
| Turbid water worse than clear | 84.4% vs 43.0%; OR 7.19 | Hit (pattern fit) |
| Dark and cold light worse | ρ = −0.49; cold vs warm OR 4.88 | Hit (pattern fit; primed) |
| Warm light above ground | 41.7% / 67.6% / 55.6% | Miss |
| Exposure worse | 87.1% vs 53.5%; OR 6.35 | Hit (pattern fit; primed) |
| Dirt below ground | OR 1.02 with location type | Not supported |
| Somatic distress below | OR 2.09; 1.76 (n.s.) without awakenings | Weak partial support |

### 4.2 Interpretation

The archived reports presented an elevation gradient as the backbone of the evidence ("ρ = 0.25–0.30, replicated"). That gradient does not exist in these data. What exists is a penalty for going below ground and no reward for going above it. In correspondential terms, this is half the vertical prediction. The lower, natural or infernal, direction is marked; the higher one is not.

One framework-consistent reading follows from where the corpus starts. MallWorld dreams begin in malls (25.6% of first locations), at ground level. If the environment reflects the dreamer's state, a dreamer whose state is "natural" would find ground the most fitting level. Height would then not be experienced as ascent into heaven. This reading is **interpretation**. It was formed after seeing the data and is not a test.

The qualitative correspondences behave as predicted: turbid water, darkness, cold light and exposure. They are also what an ordinary reading of these words predicts. Several were primed by the extraction prompt, and the coder usually read them from the same sentence as the atmosphere. Their status is pattern fit, not discrimination between explanations.

### 4.3 Implications

- **Inference.** Location-level χ² tests and correlations on this corpus must be replaced by dream-clustered estimates. Every archived p-value was too small.
- **Population.** Analyses must state their population. The thesis's inclusion of AI images and questions altered both rates and associations.
- **Height vs place.** Height effects must be separated from location-type effects. Basements are not merely "low places".

### 4.4 Limitations

- **Same-source coding.** Features and atmosphere are coded from the same narrative by the same model. Associations show that the *reports* are coherent, not that the dream environments had these properties.
- **Measured reliability** (notebook 08). Where both a blind second coder and GPT-5.2 rated a feature, values agree well:
  - atmosphere valence κ 0.75 (negative vs not κ 0.74–0.89);
  - vertical level κ 0.84;
  - light κ 0.90.

  However, GPT-5.2 rated atmosphere at 58.0% of locations against the second coder's 29.0%, and vertical level at 51.0% against 20.8%. It inferred them from events and location types. Prevalence figures, and associations that rest on inferred ratings, are therefore **convention-dependent**. Overall κ including "not mentioned" is 0.42 for both atmosphere valence and vertical level.
- **Priming.** Light temperature, exposure and verticality were labelled with framework meanings in the prompt.
- **Coverage.** Most markers are coded for under 10% of locations, and only in longer, more vivid reports.
- **Not pre-registered.** The predictions in §1.2 were not registered before these data were analysed. Their direction follows the framework, but the analyst had seen the archived results.

### 4.5 Future Directions

- **Pre-register a fresh test of the height correspondence** on posts submitted after a cut-off date, stating the ground-level pattern in advance.
- **Re-extract with a neutral prompt.** Remove framework meanings from the extraction prompt and re-extract a sample. Compare light temperature and exposure associations.
- **Require explicit evidence for atmosphere and level,** or code inferred and explicit values separately, so that prevalence can be stated without convention dependence.

---

## 5. Conclusion

Corrected, the spatial evidence in MallWorld is smaller and more specific than the archived reports claimed:
- **Hits at the level of pattern fit:** turbid water, darkness, cold light and exposure go with negative atmospheres.
- **Partial hit:** the vertical correspondence holds only below ground.
- **Misses:** "higher is better" and "warm light above".
- **Not supported:** a vertical gradient in cleanliness.
- **Robustness:** the location–atmosphere structure is shared across authors and stable over time.

None of these results distinguishes Swedenborg's correspondences from ordinary associations. The pre-registered tests in the companion report were designed to be sharper, but they share the same limitation.

---

## References

Bergsma, W. (2013). A bias-correction for Cramér's V and Tschuprow's T. *Journal of the Korean Statistical Society*, 42(3), 323–328.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika*, 73(1), 13–22.

Swedenborg, E. (2000). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation. (Original work published 1758)

---

## Appendix A: Statistical Summary

| Test | Estimate | Interval | n (dreams) |
|-------------------------|----------------------|----------------------|----------------------|
| Height × valence, ρ | +0.064 | 0.007–0.114 | 1,605 (667) |
| Underground vs ground, OR (length-adjusted) | 2.29 | — | 1,605 (667) |
| Within-dream level, conditional logit OR | 0.88 | 0.72–1.07 | 111 dreams |
| Dirty vs clean water, OR | 7.19 | — | — |
| Murky vs clear (free text), Fisher OR | 10.5 | p = 7 × 10⁻⁵ | 60 (50) |
| Light darkness, ρ | −0.49 | −0.53 to −0.44 | — |
| Cold vs warm light, OR | 4.88 | — | — |
| Exposed vs private, OR | 6.35 | — | — |
| Cleanliness × height, ρ | +0.238 | 0.099–0.359 | 277 |
| Location type, clustered joint χ²(32) | 166 | p = 5 × 10⁻²⁰ | — |
| Within-dream slope of valence | −0.083 | −0.148 to −0.017 | 594 dreams |
| Location-type V, recent − earlier | +0.015 | 90% CI −0.002 to 0.040 | 3,985 |

Intervals marked "—" are printed in the notebook cell outputs. ORs are from dream-clustered logistic regressions adjusted for log word count.

## Appendix B: Withdrawn Figures

| Archived claim | Why withdrawn | Corrected |
|-------------------------|----------------------|----------------------|
| Vertical ρ = 0.25–0.30, "replicated across splits" | Hand-typed banner; not significant in either holdout split | ρ = +0.064; not monotone |
| Vertical report ρ = 0.12; elevated mean 2.77; n = 570/1,547/819; df = 15 | In no output (computed: 0.067, 2.61, 263/678/401, df = 18) | §3.1 |
| Water "2.6×", "45% vs 17%" | "45% vs 17%" never computed | §3.2 |
| Light "ordering matches predictions exactly", V = 0.483 | Different table and population | §3.3 |
| Warm light above ticked "correct, Strong" | Non-monotone; no test | Miss |
| Bathrooms "44.2% vs 7.5% (6.0×)" | No source | 84.0% vs 14.3% of coded locations |
| Exposure "3.5× threatening atmosphere" | Was exposure by level, n = 20 | Exposure vs atmosphere OR 6.35 |
| "Anomalous perceptual states 7.3% vs 2.2%" | Field is building state (abandoned or decaying) | §3.5 |
| Compounding "2.53 vs 1.86" | 1.86 was three-marker locations only | §3.5 |
| "Ascending destinations better, ρ = 0.10, p = 0.016" | Does not survive clustering | ρ = +0.046 (n.s.) |
| Ascent/descent "1,220 vs 1,224, perfect balance" | Not reproducible | 552 vs 487 |
| χ² = 1,677 / 1,737.99 with V = 0.21 as "robust" | 72–74% sparse cells; nested data | Clustered χ²(32) = 166; within-dream null |
| "Within-author null less than half the observed V" | Within-author ≈ within-dream; not reproducible | Null 62% of observed |
| "Correspondential effect sizes stable (all Cochran's Q p > 0.50)" | In no output | Equivalence test, §3.7 |
