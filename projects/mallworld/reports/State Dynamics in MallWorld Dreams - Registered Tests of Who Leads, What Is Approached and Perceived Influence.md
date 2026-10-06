# State Dynamics in MallWorld Dreams: Registered Tests of Who Leads, What Is Approached and Perceived Influence

*New report, October 2026. The predictions were registered in `docs/STATE_DYNAMICS_DESIGN_2026-10.md`, committed (`6be44a3b`) before the analysis notebook was written. Measurement is in `notebooks/09_state_measurement.ipynb`, the tests in `notebooks/10_state_dynamics_tests.ipynb`.*

## Abstract

**Background**: The audited MallWorld analyses averaged each place over everyone who reported it and read dreams as stories. Swedenborg's account describes something else: a common intermediate state, experienced by each visitor through his or her own state. In it, change of place is change of state, and good and light are as the experiencer sees them. This report tests that account on how state evolves, not on averages.

**Methods**: The data are 1,918 dream reports from r/TheMallWorld, coded by GPT-5.2.
- **Measures:** a place's quality (Q) was computed from six coded properties, and the experiencer's evaluation (E) from the coded affect.
- **Units:** the analyses use explicit movements between places, joined on dream and location.
- **Registered tests:** four, one-sided under Holm correction:
  - H1, whether the person leads the place or the place the person (cross-lagged);
  - H2, whether people move toward what they treat as good;
  - H3, whether a presence the experiencer perceives as benign is felt (within-dream);
  - H4, whether what a person moves toward is consistent across his or her dreams.
- **Also run:** two secondary analyses and a contagion check.

**Results**:
- **H1 (hit).** The person's state at one place predicts the quality of the next place (+0.117 SD). The place's quality does not predict the person's next state (−0.003 SD). The difference is +0.121 SD (95% CI 0.020–0.213; Holm p = 0.036).
- **H2 (miss).** A more positive orientation went with *worse* destinations (−0.245 SD per unit, 95% CI −0.436 to −0.055). A post hoc diagnosis shows that 92.7% of negative orientation was distress in better-than-neutral places, not comfort in poor ones. With a rank-correlation index the relation is near zero (−0.070). The index did not measure what a person treats as good.
- **H3 (hit).** Where a being the experiencer perceives as benign is present, the person's state is higher than at his or her other places in the same dream (+0.353 on a −1 to +1 scale, 95% CI 0.221–0.485).
- **H4 (underdetermined).** ICC1 = 0.148 (95% CI −0.056 to 0.353; 38 authors).
- **Contagion check.** The common structural motifs are about as frequent in reports describing childhood or long-standing onset, and in the community's early years, as elsewhere (within ±10 percentage points for 12 and 13 of 13 motifs).

**Conclusions**: In these reports the person leads and the place follows: what comes next reflects the visitor's state more than the visitor's state reflects what was there. That is what the framework predicts and what a simple perceptual account does not. A narrator's mood colouring the next description predicts it too, so the hit is pattern fit. A presence perceived as benign is felt. Whether people move toward what *they* treat as good could not be tested with these codes. The registered attempt came out in the opposite direction. Its index measured distress in ordinary places, and its result does not survive a change of index.

**Keywords**: MallWorld, state dynamics, cross-lagged analysis, pre-registration, Swedenborg, world of spirits, perceived influence, contagion

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| Dream reports (N=1,918 primary) | r/TheMallWorld (Reddit) | `data/mallworld/` |
| Structured extraction | GPT-5.2 via Azure OpenAI | `projects/mallworld/structured/` |
| Verified loader | `scripts/mallworld_dataset.py` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/scripts/mallworld_dataset.py) |
| Design and registration | `docs/STATE_DYNAMICS_DESIGN_2026-10.md` (commit `6be44a3b`) | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/docs/STATE_DYNAMICS_DESIGN_2026-10.md) |
| Measurement | `notebooks/09_state_measurement.ipynb` | Repository |
| Tests | `notebooks/10_state_dynamics_tests.ipynb` | Repository |
| Swedenborg texts | Ager translations of *Heaven and Hell* and *Divine Love and Wisdom* | Project Gutenberg #17368, #16627 |

---

## 1. Introduction

### 1.1 Background

r/TheMallWorld is an online community in which people describe recurring dreams of vast malls, hotels, schools and transit spaces. The October 2026 audit corrected the earlier analyses of this corpus (`docs/STATISTICAL_AUDIT_2026-10.md`). Its scorecard records hits on the *character* of what appears (water, light, exposure, animals, the deceased, a person's persistent atmosphere) and misses on *height*.

Those analyses asked how a kind of place feels on average, pooled over everyone who reported it. They read a dream as a narrative. Neither question is the framework's.

### 1.2 Theoretical Framework

In Swedenborg's account the living are, as to their spirit, already among spirits (*Heaven and Hell* §438). The world of spirits is "an intermediate state" in which people "are brought into one state after another" (§§421–427). Five features of that state bear on these data:
- **Space is state.** "Change of place is nothing else than change of state". Those in like states are near, and the way lengthens or shortens with desire (§§192–195).
- **What appears arises from state.** Surroundings correspond to the interiors of those present (§§173–176). The evil man "desires nothing so much as to be where his evil is" (§547).
- **Influence comes from above and below.** Angels receive the newly arrived and "perform for him all good offices". One who "seeks to get away from these angels" is left by them (§548). Freedom is the ability to choose (§597).
- **Good is as the experiencer sees it.** To those in hell "the light of heaven is thick darkness" (§584). Evil spirits seek what good spirits flee (§429). One ascending beyond his state feels anguish (§35).
- **No degrees are assigned.** No observable is assigned to a single degree (*Divine Love and Wisdom* §§222–229, 256).

**Predictions** (registered; the owner's reading of the framework is recorded in the design document, §6):
1. **H1:** the person's state leads what appears next, more than what appears leads the person's state.
2. **H2:** people move toward what they themselves treat as good.
3. **H3:** a presence the experiencer perceives as benign is felt.
4. **H4:** what a person moves toward is consistent across his or her dreams.

**Competing readings, registered in advance.**
- **Ordinary perception:** the place drives the feeling, which predicts the reverse of H1.
- **Ordinary dream psychology:** everyone moves toward better places, which predicts no effect of orientation in H2.
- **Comfort of company:** predicts H3.
- **Stable temperament or style:** predicts H4.

H3 and H4 are therefore not discriminating.

### 1.3 Aims

1. **Measure** the state of a place and of the experiencer from several coded properties together, and check that the measures behave as measures.
2. **Test** the direction of influence between person and place across movements.
3. **Test** whether movement follows what the experiencer treats as good, and whether a perceived benign presence is felt.
4. **Assess** whether the shared structure of these dreams could be community contagion.

---

## 2. Methods

### 2.1 Data Sources

| Source | Records | Description |
|---|---|---|
| r/TheMallWorld | 1,918 dream reports | Primary population: dream reports with at least one coded location, exact duplicates removed; 8,685 locations; 1,303 authors |
| Connections | 4,590 | Movements between coded locations; 259 lead from a location to itself and are excluded (§3.6) |
| Entities | 3,696 involvements | Beings at a location, with demeanor as the experiencer perceived it |

### 2.2 Measures

**Place quality (Q).** The mean of the scored properties available at a location, each scored −1 / 0 / +1. The scoring was fixed before computation (notebook 09):
- light;
- light warmth;
- cleanliness;
- condition of the place;
- crowd behaviour;
- water.

Atmosphere is left out because it mixes the place with the person; it enters only sensitivity analyses. Q is available at 3,882 locations.

**Experiencer evaluation (E).** The coded affect, plus the rarely coded somatic responses (1.6% of locations). It is available at 43.6% of locations.

**Measurement checks** (notebook 09):
- The properties cohere: median pairwise ρ = 0.365, and every item–rest correlation is positive.
- Q does not track narrative length (r = +0.091).
- A pre-specified homogeneity-analysis check failed as written. The cause was diagnosed after the fact as two near-equal dimensions dominated by rare categories. With rare categories set aside, the data-driven ordering agrees with the scoring (rank correlations +0.63 to +1.00).

**Perceived beings.** A being is perceived as benign when its demeanor is helpful or friendly, and as hostile when it is hostile, threatening or unfriendly.

**Choices.** Movement mode: purposeful (`directed_active`), fleeing, wandering, passive, instant, drifting, struggle.

### 2.3 Statistical Analysis

- **Models:** linear models on the measures, with log word count as a covariate.
- **Inference:** standard errors clustered by dream; bootstraps resample dreams or authors (2,000 resamples, seed 0); permutation tests shuffle author labels (5,000).
- **Holm family:** H1–H4, one-sided at α = 0.05.
- **Verdicts:**
  - **hit:** the predicted direction with Holm p < 0.05;
  - **miss:** the opposite direction with a 95% CI excluding zero, or a 90% CI inside the registered margin;
  - **underdetermined:** otherwise.
- **Sensitivity analyses:** atmosphere added to Q; Q without light warmth; list-order pairs; dream fixed effects; strata of onset mention and community vocabulary.

---

## 3. Results

### 3.1 H1: Does the person lead the place, or the place the person?

On 711 movements in 350 dreams, with Q and E known at both ends, two cross-lagged models were fitted on standardised measures.

| Path | Coefficient (SD) | 95% CI |
|---|---|---|
| Person at t → place at t+1 (given the place at t) | +0.117 | clustered SE 0.035 |
| Place at t → person at t+1 (given the person at t) | −0.003 | clustered SE 0.035 |
| Difference D | +0.121 | 0.020 to 0.213 (bootstrap) |

Each measure persists strongly (0.460 for the place, 0.455 for the person). One-sided p = 0.012, Holm p = 0.036.

**Sensitivity.** The direction holds in every variant; the precision varies.
- **Measure variants:** with atmosphere added to Q, D = +0.102 (p = 0.035); without light warmth, +0.117 (p = 0.007).
- **List-order pairs:** +0.061 (p = 0.081).
- **Dream fixed effects:** +0.065 (p = 0.25; 160 dreams with two or more movements).
- **Strata:** in reports mentioning long-standing onset, +0.361 (p = 0.003); in the rest, +0.068 (p = 0.10).

**Finding (statistically supported):** the person's state at one place predicts the quality of the next place. The quality of a place does not predict the person's next state. **Verdict: hit.**

**Interpretation:** this fits the framework's account that what appears follows the state of the one who is there (*HH* §§173–176, 192, 547). It runs against an account in which the environment drives the feeling. It does not discriminate from a reporting account in which a narrator's mood colours how the next place is described: both are coded from the same narrative.

### 3.2 H2: Does a person move toward what he or she treats as good?

**Measure.** A dream's orientation is the mean of E·Q at its other locations. It is positive when feelings run with the place's quality. 425 purposeful moves in 163 dreams had an estimable orientation; 32.0% of them had a negative orientation.

**Result.** A more positive orientation went with a *worse* destination, given the origin: −0.245 SD per unit (95% CI −0.436 to −0.055). **Verdict: miss** (registered).

**Sensitivity.** The direction is the same with atmosphere added (−0.380), without light warmth (−0.26) and on list-order pairs (−0.19). In reports mentioning long-standing onset it is near zero (−0.007; n = 106).

**Post hoc diagnosis (exploratory; the verdict stands).**
- **What makes an index negative.** Of 482 locations with a negative E·Q product, 92.7% are distress in a better-than-neutral place and 7.3% are comfort in a poor place. A negative orientation therefore mostly means "anxious in an ordinary place", not "treats darkness as good".
- **Overall level.** Adding the dream's mean Q and mean E at the same other locations leaves the estimate unchanged (−0.235, SE 0.149, p = 0.12). The miss is not explained by the dream's overall level.
- **A rank-correlation index.** A Spearman orientation over at least three other locations (257 moves in 81 dreams; 16.7% negative) gives −0.070 (SE 0.110, p = 0.52). The negative relation depends on how orientation is measured.

**Finding:** the registered test is a miss. **Interpretation:** the miss concerns the index more than the principle:
- In these codes, a negative orientation mostly means distress in an ordinary place, which the examples in notebook 09 show to be driven by events.
- Comfort in a poor place, the case the principle is about, occurs at only 35 locations.
- The negative relation does not survive a change of index.

Whether people move toward what *they* treat as good therefore remains untested with this extraction.

### 3.3 H3: Is a presence the experiencer perceives as benign felt?

**Sample.** 864 locations in 175 dreams that have places both with and without a perceived-benign being (225 locations with one).

**Result.** The mean E is +0.082 at locations with a perceived-benign being and −0.329 without. Within dreams, and controlling for perceived-hostile presence, the effect is +0.353 (95% CI 0.221–0.485; Holm p < 0.0001). A perceived-hostile presence lowers E by 0.445.

**Sensitivity.** The result holds without the hostile control (+0.348) and in every stratum (+0.284 to +0.479).

**Finding (statistically supported):** the person's state is higher where a being he or she perceives as benign is present than elsewhere in the same dream. **Verdict: hit.** It is not discriminating: comfort from company predicts the same. The demeanor is the experiencer's perception, so the test says nothing about what the being is.

### 3.4 H4: Is what a person moves toward consistent across his or her dreams?

**Sample.** 116 dreams from 38 authors. The direction of approach is the destination's quality, adjusted for the origin, averaged per dream.

**Result.** ICC1 = 0.148 (permutation null mean 0.000; one-sided p = 0.063; Holm p = 0.126; 95% CI −0.056 to 0.353).

**Sensitivity.** The estimates range from +0.065 to +0.153.

**Finding:** **underdetermined.** The point estimate is of the same order as the registered person-level consistency of atmosphere (P4, ICC1 0.094). The sample is too small to separate it from zero or to show its absence.

### 3.5 Secondary analyses

**H5: Common structure, personal state (descriptive).**

| Feature | ICC1 by author (278 authors, 893 dreams) |
|---|---|
| Mean place quality Q | 0.019 (−0.067 to 0.107) |
| Mean evaluation E | 0.110 (0.027 to 0.190) |
| Mall present | 0.185 (0.111 to 0.263) |
| Hotel present | 0.139 (0.031 to 0.249) |
| Escalator present | 0.130 (0.011 to 0.257) |
| Mean over 13 structural features | 0.073 |
| Mean over the 2 state measures | 0.064 |

What a person dreams of (malls, hotels, escalators) is as person-specific as the state in which he or she dreams it. Most of the state's person-specificity sits in E, not in Q. As registered, this is descriptive. Under the model, a person returning to his or her own layout is the persistent state finding its own place, so person-specific structure does not count against a common state.

**H6: Height, conditional on state.** 226 vertical movements in 164 dreams. The interaction between the experiencer's state and moving up is −0.116 (95% CI −0.364 to 0.133; one-sided p = 0.82). No margin was registered for H6, so the verdict is **underdetermined**. The point estimate runs against the prediction that going up helps only those already in a good state.

**Perceived beings by place quality (descriptive).**

| Place quality | Perceived benign | Perceived hostile |
|---|---|---|
| Q < 0 (1,071 locations) | 3.2% | 15.8% |
| Q > 0 (2,074 locations) | 8.7% | 7.4% |

Perceived-benign beings appear in poor places at about a third of their rate in good places. Perceived-hostile beings appear in good places at about half their rate in poor places.

### 3.6 Deviation from the registration

259 connections lead from a location to itself. They are not movements, and they were excluded, but the registration did not say so. With them included the conclusions are unchanged:
- **H1:** D = +0.107 (95% CI 0.024–0.185, p = 0.010; 801 movements);
- **H2:** −0.229 (−0.415 to −0.042);
- **H4:** ICC1 0.122 (−0.095 to 0.331, p = 0.092).

### 3.7 B1: Is the common structure contagion?

**Splits.** The 13 structural motifs were compared:
- between reports that mention childhood or long-standing onset (252) and the rest;
- between an author's first report and later ones;
- between 2021–2023 (436 reports) and 2024–2026.

All comparisons are adjusted for length.

**Results.**
- **Onset:** 12 of 13 motifs equivalent within ±10 points. Houses are more common in long-standing reports (+8.2 points, 90% CI 3.8–13.0).
- **Era:** 13 of 13 equivalent.
- **First report:** 12 of 13 equivalent. Malls are more common in an author's first report than in later ones (+17.8 points, 14.4–21.5): people arrive with their mall dream, and later reports range more widely.

**Finding:** the shared motifs are as common in reports describing long-standing onset, and in the community's early period, as elsewhere. Contagion is therefore not the main source of the shared structure, within the precision of these splits. The onset flag is a crude text pattern, and a ±10-point margin is wide for motifs below 10% prevalence.

---

## 4. Discussion

### 4.1 Summary of Findings

| # | Question | Result | Verdict |
|---|----------------|------------------------------|--------------|
| H1 | Does the person lead the place? | D = +0.121 SD (0.020–0.213); place → person −0.003 | **Hit** |
| H2 | Do people move toward what they treat as good? | −0.245 SD per unit (−0.436 to −0.055); 92.7% of negative orientation is distress in ordinary places; rank index −0.070 (post hoc) | **Miss** (registered); principle untested |
| H3 | Is a perceived benign presence felt? | +0.353 (0.221–0.485) | **Hit** (not discriminating) |
| H4 | Is approach consistent across a person's dreams? | ICC1 0.148 (−0.056 to 0.353) | **Underdetermined** |
| H5 | Common structure, personal state? | Structure about as person-specific as state | Descriptive |
| H6 | Does going up help only the good? | Interaction −0.116 (−0.364 to 0.133) | **Underdetermined** |
| B1 | Is the structure contagion? | 12–13 of 13 motifs equivalent across onset, era, first report | Not contagion (bias check) |

### 4.2 Interpretation

**H1.** The clearest result concerns the direction of influence. Across movements, the person's state carries forward into what appears next, and the place's quality does not carry into the person's next state. This is what the framework's mechanics predict: surroundings follow the state of the one present, and movement is change of state. An account in which the environment drives emotion predicts the opposite and is not supported. A reporting account, in which the narrator's mood colours later descriptions, predicts the same as the framework. The two cannot be separated with retrospective narratives coded by one model.

**H2.** The owner's principle that good is as the experiencer sees it is the most specific claim tested here. It was not tested in the intended sense. The coded affect tracks events more than a person's relation to light, and comfort in poor places is rare in these codes. The registered miss is reported as a miss. Its diagnosis says the index was the problem: it captured distress in ordinary places, and its result does not survive a rank-based index. The principle needs a measure that the current extraction does not provide.

**H3.** A presence the person perceives as benign is felt. As a test of influence it establishes the effect. It cannot say what the being is or why the effect occurs.

**The earlier height misses.** H6 asked the height question in the conditional form that §35 suggests. Its estimate points the other way and is imprecise. The earlier height misses (M2, M5, M8, M12) stand.

### 4.3 Implications

- **Whose state:** analyses of this corpus should follow the person's state across movements rather than average places across visitors.
- **Measuring orientation:** the principle that good is relative to the experiencer needs a code for the person's attraction or aversion to the place itself, separate from event-driven feeling.
- **Contagion:** the contagion check suggests the shared motifs predate or stand apart from community exposure. That makes common-structure questions worth asking with better person-level data.

### 4.4 Limitations

- **Same-source coding.** All measures are coded by one model from one narrative. Where both a blind second coder and GPT-5.2 rated, κ is 0.75 for atmosphere, 0.90 for light and 0.67 for affect. GPT-5.2 rated atmosphere and affect about twice as often, by inference (notebook 08).
- **Priming.** The extraction prompt attached framework meanings to light warmth, affect, somatic distress and movement mode. Results without light warmth are reported.
- **The measures.** E rests on one coded field. The pre-specified scaling check of Q failed as written (diagnosed in notebook 09). One undisclosed exclusion (self-loops) is reported in §3.6.
- **Power.** H4 rests on 38 authors and H6 on 226 movements.
- **Prior exposure.** The analyst had seen the earlier height results and the affect → atmosphere result (notebook 04, R4) before registration.

### 4.5 Future Directions

- **Code orientation directly:** for each place, whether the person wants to stay, return or leave, and why. Test H2 again with that code.
- **Separate mood from description:** code the narrator's present-tense evaluation separately from the description of the place, to separate the framework's reading of H1 from narrative colouring.
- **Collect repeat dreamers:** to give H4 the power it lacks.
- **Use a holdout:** test H1 and H3 on posts made after 19 January 2026, which no analysis has used.

---

## 5. Conclusion

Treated as a state that each visitor enters from his or her own state, MallWorld shows a clear direction of influence: the person leads, and the place follows. That is the framework's prediction, and the one ordinary perception does not make, though a narrator's mood colouring the description makes it too. A presence perceived as benign is felt. The principle that good is as the experiencer sees it could not be tested with these codes: the registered attempt came out in the opposite direction, but its index measured event-driven distress, not orientation. The shared motifs of these dreams do not look like community contagion.

---

## References

Swedenborg, E. (2005). *Angelic Wisdom Concerning the Divine Love and the Divine Wisdom* (J. C. Ager, Trans.). Project Gutenberg, eBook #16627. (Original work published 1763)

Swedenborg, E. (2005). *Heaven and its Wonders and Hell* (J. C. Ager, Trans.). Project Gutenberg, eBook #17368. (Original work published 1758). Quotations in this report follow this translation.

---

## Appendix A: Statistical Summary

| Test | Estimate | 95% CI | One-sided p | Holm p | n |
|---|---|---|---|---|---|
| H1 (D) | +0.121 | 0.020 to 0.213 | 0.012 | 0.036 | 711 movements, 350 dreams |
| H2 | −0.245 | −0.436 to −0.055 | 0.994 | 0.994 | 425 moves, 163 dreams |
| H3 | +0.353 | 0.221 to 0.485 | < 0.0001 | < 0.0001 | 864 locations, 175 dreams |
| H4 (ICC1) | +0.148 | −0.056 to 0.353 | 0.063 | 0.126 | 116 dreams, 38 authors |
| H6 (interaction) | −0.116 | −0.364 to 0.133 | 0.82 | — | 226 movements, 164 dreams |
