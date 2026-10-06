# Pre-registered Correspondential Tests in MallWorld Dreams: Animals, the Deceased and Ruling Love

*New report, October 2026. The predictions were registered in `docs/PREREGISTRATION_2026-10.md`, committed (`b3f91962`) before the analysis notebook was written or run. This report replaces the archived "pre-registered" plan `docs/correspondential_falsification_test_plan_20260120.md`. That plan was written after the reports whose findings it claimed to predict.*

## Abstract

**Background**: Swedenborg's framework makes three predictions about dream environments that the archived MallWorld analyses either never tested correctly or tested with a join error:
- harmful animals appear where the scene is evil-toned and gentle animals where it is good-toned;
- the deceased are met in benign circumstances;
- a person's ruling love persists, so the same person meets similar atmospheres across dreams.

These were registered as falsifiable predictions before any test was computed.

**Methods**: The data are 1,918 primary MallWorld dream reports. Animal classes were fixed in advance as whole-word lists of gentle and noxious animals. The deceased were identified by the extraction's entity type.
- **P1, P3 (outcome):** a negative location atmosphere, modelled by logistic regression with standard errors clustered by dream and adjustment for narrative length.
- **P2 (secondary):** noxious animals more often underground.
- **P4:** a one-way ICC of dream atmosphere within authors, with 5,000 permutations.
- **Multiplicity and checks:** P1, P3 and P4 formed a Holm family, one-sided at α = 0.05. Sensitivity analyses were registered. A blind second coder later recoded the 69 dreams behind P1 and P3.

**Results**:
- **P1 (hit).** Noxious-animal locations are negative in 84.8% of cases, gentle-animal locations in 58.3% (OR 4.08, 95% CI 1.20–13.90; Holm p = 0.036).
- **P2 (miss).** Noxious animals are not more often underground (25.0% vs 23.6%; OR 1.04).
- **P3 (hit).** Locations with a deceased person are negative in 45.5% of cases, against 68.8% with living family and friends (OR 0.36, 0.15–0.87; Holm p = 0.036).
- **P4 (hit).** Authors meet consistent atmospheres across different dreams (ICC1 = 0.094; Holm p = 0.036).
- **Second coder.** P3 is robust to the coder. P1 keeps its effect size (OR ≈ 3.3 under every combination of coders) but loses significance once the word lists' false positives are removed (one-sided p = 0.11).

**Conclusions**: Three of three primary predictions are hits, and the secondary prediction is a miss. The hits establish **pattern fit**: the dreams behave as the correspondences predict. They do not discriminate the framework from ordinary associations: vermin are unpleasant, lost loved ones are emotionally significant, and temperament and style persist. The P1 effect needs replication with coder-based animal detection.

**Keywords**: pre-registration, MallWorld, Swedenborg, animal correspondences, deceased, ruling love, intraclass correlation, coder sensitivity

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| Dream reports (N=1,918 primary) | r/TheMallWorld (Reddit) | `data/mallworld/` |
| Structured extraction | GPT-5.2 via Azure OpenAI | `projects/mallworld/structured/` |
| Pre-registration | `docs/PREREGISTRATION_2026-10.md` (commit `b3f91962`) | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/docs/PREREGISTRATION_2026-10.md) |
| Analysis | `notebooks/07_preregistered_correspondence_tests.ipynb` | Repository |
| Coder sensitivity | `notebooks/08_extraction_reliability.ipynb`, `validation/` | Repository |

---

## 1. Introduction

### 1.1 Background

The archived MallWorld thesis described its plan as pre-registered. The plan file was written on 2026-01-20 at 14:59, after the vertical, entity, sequence and exploratory reports had been committed the same day, and its hypotheses restated patterns already seen. Three framework predictions had never been tested correctly:
- **Animals.** The archived animal–atmosphere test put every creature in one category and reported the empty test as "complete independence".
- **The deceased.** Figures on the deceased came from a smaller, older population.
- **Ruling love.** Author consistency was never separated from within-dream clustering.

These three were registered before any computation.

### 1.2 Theoretical Framework

- **Animals.** Animals correspond to affections: gentle and useful animals to good affections, fierce and harmful ones to evil affections (Swedenborg, 1758, *Heaven and Hell* §110). Appearances around spirits correspond to their interiors (§§173–176).
- **The deceased.** After death people meet friends and acquaintances (§494), and the newly arrived are received with kindness (§§449–450).
- **Ruling love.** A person's ruling love persists (§§477–479), and the surroundings of a spirit correspond to it.
- **Animals and height (P2).** Noxious creatures "appear in the hells" as correspondences of the lusts of those there (*Divine Love and Wisdom* §339), and the hells are beneath (*Heaven and Hell* §584). The registration cited only §110 and §§173–176 for P2. These two passages were located after the test, when every prediction was checked against the text (`CLAUDE.md` §3, "Find the prediction in the text"). They confirm that P2 is the framework's own prediction, so its miss stands.

If MallWorld environments express the state of the scene and of the person, three things follow:
- harmful animals should appear in negative scenes;
- the deceased should appear in less negative scenes than living acquaintances;
- a person's dreams should share an atmosphere.

**Competing readings.** Each prediction is also made by ordinary associations, stated in advance in the registration:
- vermin and predators are unpleasant;
- the deceased are emotionally significant and often comforting;
- temperament and writing style are stable.

A hit is therefore pattern fit, not discrimination. A miss counts against the framework regardless.

### 1.3 Aims

To test P1–P4 exactly as registered, and to report sensitivity analyses and coder sensitivity separately, without changing the verdicts.

---

## 2. Methods

### 2.1 Data Sources

The data are the primary population of the verified loader: 1,918 dream reports with at least one location, after removing exact duplicates.

### 2.2 Coding Scheme

**Atmosphere.** It is negative if coded threatening, oppressive, uncomfortable, wrong, eerie or chaotic, and non-negative if neutral, welcoming or peaceful. Nostalgic and uncoded locations are excluded.

**Animal classes.** A location carries a class if a listed word (whole word) appears in the description or name of an entity interacting there, or in the location's own description. "Hot dog(s)" is removed first, and locations matching both classes are excluded.
- **Gentle** (48 words), for example cat, dog, horse, bird, fish, rabbit, deer.
- **Noxious** (54 words), for example snake, spider, rat, insect, wolf, shark, bear.

**The deceased (P3).** A location is "deceased" if an entity there is of type `deceased`. It is "living known" if there is none and an entity is a known person, family member or friend.

**Author consistency (P4).** Authors with at least two dreams that have a scored atmosphere. A dream's score is the mean valence of its coded locations.

### 2.3 Statistical Analysis

**Model (P1–P3).** Logistic regression of the outcome on the class indicator and log word count, with standard errors clustered by dream.

**Author consistency (P4).** A one-way ICC1 with a permutation p-value from 5,000 shuffles of author labels.

**Decision rules.**
- **Primary family:** P1, P3 and P4 under Holm correction, one-sided in the predicted direction at α = 0.05.
- **P2:** secondary, one-sided, outside the family.
- **Sensitivity analyses:** excluding locations with a `threat` entity; animals from entity descriptions only; adding location type. These were registered and do not change verdicts.

**Coder sensitivity** was added after the tests, in response to the audit rule on small-count results (CLAUDE.md §4.12). A blind second coder recoded all dreams contributing to P1 and P3 (27 noxious-animal dreams, 18 deceased-person dreams) and 27 of the 81 gentle-animal dreams.

---

## 3. Results

### 3.1 P1: Noxious vs Gentle Animals

| Class | Locations | Negative atmosphere |
|-------------------------|----------------------|----------------------|
| Noxious | 33 | 84.8% |
| Gentle | 96 | 58.3% |

The two classes span 105 dreams. OR = 4.08 (95% CI 1.20–13.90), one-sided p = 0.0124, Holm p = 0.036.

Sensitivity:
- excluding locations with a `threat` entity: OR 4.20;
- animals from entity descriptions only: OR 8.82 (n=66);
- with location type: OR 3.88 (two-sided p = 0.055).

**Finding (statistically supported):** Noxious animals appear in negative scenes far more often than gentle animals. **Verdict: hit.**

### 3.2 P2: Noxious Animals and Height (Secondary)

Of located animal locations, 25.0% of noxious (n=20) and 23.6% of gentle (n=55) are underground. OR = 1.04 (0.31–3.54), one-sided p = 0.47.

**Finding (statistically supported):** Animal class is not related to height. **Verdict: miss.** It matches the absence of an elevation gradient in the spatial report. The interval is wide (OR 0.31–3.54, 75 located animal locations), so the miss excludes only a large effect.

### 3.3 P3: The Deceased vs Living Known Persons

| Persons present | Locations | Negative atmosphere |
|-------------------------|----------------------|----------------------|
| A deceased person | 22 (18 dreams) | 45.5% |
| Living known persons only | 266 | 68.8% |

OR = 0.36 (95% CI 0.15–0.87), one-sided p = 0.012, Holm p = 0.036. With location type added: OR 0.27.

**Finding (statistically supported):** Scenes with a deceased person are less often negative than scenes with living family and friends. **Verdict: hit.**

### 3.4 P4: Author Consistency

Across 563 dreams from 181 authors with at least two scored dreams, ICC1 = 0.094. The permutation null has a mean of 0.000 and a 95th percentile of 0.072; p = 0.0176, Holm p = 0.036.

**Finding (statistically supported):** The same author meets somewhat consistent atmospheres across different dreams. **Verdict: hit.** The effect is modest. It is far below the archived claim that "dreamer identity explains 56.4%", which mistook the dream for the dreamer.

### 3.5 Coder Sensitivity (Added After the Tests)

**Detection agreement.**
- **Deceased person at a location:** κ = 0.79. GPT-5.2 found 22 such locations and the second coder 28, of which 20 are shared.
- **Animal class:** κ = 0.70. The word lists flagged 15 of 34 noxious-animal locations, and 13 of 40 gentle ones, where the second coder found no living animal. The causes were similes, word fragments, feared-but-absent animals, animal-headed beings and models.

**Atmosphere agreement.** Where both coders rated the atmosphere at these locations, negative-vs-not agreement was 93–100%.

| Test | GPT-5.2 codes | Second-coder detection | Second-coder detection and atmosphere |
|-------------------------|----------------------|----------------------|----------------------|
| P1 (within the 69 recoded dreams) | OR 3.36, one-sided p = 0.046 | OR 3.35, p = 0.11 | OR 3.28, p = 0.20 |
| P3 | OR 0.35, p = 0.010 | OR 0.35, p = 0.012 | OR 0.19, p = 0.002 (atmosphere only) |

**Finding (statistically supported):** P3 is robust to a different coder. P1's effect size is robust (OR ≈ 3.3 throughout). Its significance depends on a detector that over-counts noxious animals, by 15 of 34 locations. **Interpretation:** the registered verdict stands. The P1 effect is real in size but not yet secure in precision.

---

## 4. Discussion

### 4.1 Summary of Findings

| # | Prediction | Result | Verdict |
|-------------------------|----------------------|----------------------|----------------------|
| P1 | Noxious animals in negative scenes | 84.8% vs 58.3%; OR 4.08; Holm p = 0.036 | Hit (precision coder-sensitive) |
| P2 | Noxious animals underground | 25.0% vs 23.6%; OR 1.04 | Miss |
| P3 | The deceased in less negative scenes | 45.5% vs 68.8%; OR 0.36; Holm p = 0.036 | Hit (coder-robust) |
| P4 | Consistent atmospheres within authors | ICC1 0.094; Holm p = 0.036 | Hit |

### 4.2 Interpretation

The three primary hits share a structure. The quality of what appears in a dream scene (its animals, its people, the person dreaming it) goes with the quality of the scene's atmosphere. That is the core correspondential claim: surroundings correspond to the state of those present.

The archived reports had reached the opposite conclusion about animals, "independence from atmosphere", through a binning error. They then built an interpretation on it. Corrected and tested in advance, the result runs in the framework's direction.

The miss concerns height, as do the misses in the spatial report. The framework places noxious creatures in the hells and the hells beneath (*Divine Love and Wisdom* §339; *Heaven and Hell* §584), and these dreams do not place harmful animals below ground. Across the MallWorld reports, predictions about the **character** of what appears in a scene hold. Of the predictions about **height**, only "worse below ground" holds. In the NDE project, the earlier structural "misses" (stage order, per-degree layering) turned out not to be Swedenborg's predictions. The MallWorld height results are therefore the clearest misses of the framework's own predictions in this repository.

These tests establish pattern fit only. Each hit was predicted in advance by an ordinary association that the registration named. They raise the weight of the framework's qualitative predictions in this domain only to the extent that those predictions could have failed and did not.

### 4.3 Implications

- **Replication.** P1 should be replicated with coder-based animal detection, on posts submitted after a cut-off date.
- **Discriminating tests.** The next registration should include a prediction on which the framework and ordinary association disagree. One candidate is the dreamer's affect leading the next scene (notebook 04), stated before the data are examined.

### 4.4 Limitations

- **Same-source coding.** Animals, persons and atmosphere are coded from the same text, often the same sentence.
- **Measured reliability** (notebook 08):
  - deceased detection κ 0.79;
  - animal-class detection κ 0.70, with a 44% false-positive rate for the noxious list;
  - atmosphere negative-vs-not κ 0.74–0.89 where both coders rated.

  GPT-5.2 rates atmosphere about twice as often as a coder who requires explicit affect. The tests therefore include inferred atmospheres.
- **Small samples.** P1 rests on 33 noxious locations and P3 on 22 deceased locations in 18 dreams; the intervals are wide.
- **Analyst knowledge.** The analyst had read the archived claims, although not correct estimates of these relations, before registering.

### 4.5 Future Directions

1. **Replicate P1–P4 on new posts,** with coder-based animal and deceased detection and a neutral extraction prompt.
2. **Register a discriminating test:** affect leading the next scene within dreams.
3. **Collect repeated dreams from the same authors** to strengthen P4.

---

## 5. Conclusion

Tested as registered, MallWorld dreams fit three of the framework's correspondences:
- harmful animals in negative scenes;
- the deceased in less negative scenes;
- consistent atmospheres within a person.

They fail its vertical placement of harmful animals. The hits are pattern fit, not proof of mechanism. The P1 effect is coder-sensitive in precision but not in size.

---

## References

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika*, 73(1), 13–22.

Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420–428.

Swedenborg, E. (2000). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation. (Original work published 1758)

Swedenborg, E. (2005). *Angelic Wisdom Concerning the Divine Love and the Divine Wisdom* (J. C. Ager, Trans.). Project Gutenberg, eBook #16627. (Original work published 1763). Quotations in this report follow this translation.

---

## Appendix A: Statistical Summary

| Test | Estimate (95% CI) | One-sided p | Holm p | n |
|-------------------------|----------------------|----------------------|----------------------|----------------------|
| P1 noxious vs gentle, negative atmosphere | OR 4.08 (1.20–13.90) | 0.0124 | 0.036 | 129 locations, 105 dreams |
| P2 noxious vs gentle, underground | OR 1.04 (0.31–3.54) | 0.47 | — | 75 located |
| P3 deceased vs living known, negative atmosphere | OR 0.36 (0.15–0.87) | 0.012 | 0.036 | 288 locations |
| P4 author ICC1 | 0.094 (null 95th pct 0.072) | 0.0176 | 0.036 | 563 dreams, 181 authors |
| P1 sensitivity: + location type | OR 3.88 | two-sided 0.055 | — | — |
| P1 sensitivity: excluding threat entities | OR 4.20 | — | — | — |
| P1 sensitivity: entity descriptions only | OR 8.82 | — | — | 66 |
| P3 sensitivity: + location type | OR 0.27 | — | — | — |

## Appendix B: Archived Claims Addressed

| Archived claim | Status |
|-------------------------|----------------------|
| "Pre-registered" falsification plan (2026-01-20) | Written after the reports; superseded by `PREREGISTRATION_2026-10.md` |
| Animals "completely independent of environmental atmosphere (χ² ≈ 0, p = 1.0)" | Binning error; P1 hit in the opposite direction |
| Deceased "appear regardless of atmospheric conditions" | P3 hit: less negative scenes |
| "Dreamer identity explains 56.4% of atmosphere variance" | Dream, not dreamer; author ICC 0.094 |
