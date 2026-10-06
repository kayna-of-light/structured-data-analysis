# Reliability of MallWorld Dream Coding: Blind Second Coding of 119 Dream Reports

*New report, October 2026. The archived thesis stated that "extraction reliability was validated through manual review". No record of that review exists in the repository. This report is the first measurement.*

## Abstract

**Background**: Every MallWorld statistic is a GPT-5.2 code of a self-reported dream. How much these codes reflect the text rather than the coder had not been measured. The question matters most for location atmosphere, the outcome of nearly every test, and for the small-count codes behind the pre-registered tests.

**Methods**: A blind second coder (Claude) recoded 119 dream reports from their text alone. The coder used the schema's enumerations and the extraction prompt, with written conventions where the schema is silent. The extracted location list served only to align locations.
- **Set A:** 50 random primary dreams (253 locations).
- **Set B:** the 69 dreams behind pre-registered tests P1 and P3.

The codes were committed before any comparison. Agreement was measured with Cohen's κ, with 95% intervals from a bootstrap over dreams, on all locations and on locations both coders rated. The pre-registered tests were re-estimated with the second coder's codes. Eight exact duplicate submissions gave a test–retest check of GPT-5.2.

**Results**:
- **Values reproduce.** Where both coders judged that the text describes a feature, values agree well: atmosphere valence κ = 0.75, negative vs not κ = 0.74 (set A) and 0.89 (set B), vertical level κ = 0.84, light κ = 0.90, affect κ = 0.67.
- **Coverage does not.** GPT-5.2 rates features about twice as often, inferring them from events and location types. It rated atmosphere at 58.0% of locations against 29.0%, vertical level at 51.0% against 20.8%, and affect at 49.4% against 19.2%. Including "not mentioned", κ is 0.42 for atmosphere valence and 0.35 for affect.
- **Entities.**
  - Deceased-person detection: κ = 0.79.
  - Animal class: κ = 0.70, with the pre-registered word lists counting 15 of 34 noxious-animal locations where no living animal was present.
  - Threat entity type vs "hostile entity present": κ = 0.50 (0.71 counting any hostile-demeanor entity).
- **Pre-registered tests under the second coder.**
  - P3 holds (OR 0.35, p = 0.012).
  - P1 keeps its size (OR 3.35) but not its significance (p = 0.11).

**Conclusions**: The *values* GPT-5.2 assigns are reproducible. *Whether* a location has an atmosphere, level or affect is convention-dependent. Prevalence figures such as "64% of locations are negative" describe GPT-5.2's inferences. The deceased results are robust; the animal result is robust in size and fragile in precision.

**Keywords**: inter-rater reliability, Cohen's kappa, large language model annotation, dream reports, MallWorld, measurement error, coder sensitivity

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| Dream reports | r/TheMallWorld (Reddit) | `data/mallworld/` |
| First coder | GPT-5.2 via Azure OpenAI | `projects/mallworld/structured/` |
| Second coder | Claude (blind to the extraction's codes) | `validation/second_coder_codes.jsonl` (commit `498e86f4`) |
| Conventions and procedure | `validation/README.md` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/mallworld/validation/) |
| Analysis | `notebooks/08_extraction_reliability.ipynb` | Repository |
| Duplicate test–retest | `notebooks/01_data_audit.ipynb` (D7) | Repository |

---

## 1. Introduction

### 1.1 Background

Large language models can code text at scale, and their codes are measurements with error. In the NDE project a blind second coder showed that most fields were reproducible at κ ≥ 0.77. It also showed that a few findings depended on codebook conventions rather than on stable measurement (NDE reliability report).

The MallWorld extraction prompt asked the coder to capture "subtle sensory details" and to *infer* verticality from location types. It also attached framework meanings to several fields. Its codes may therefore reflect inference as much as reading. Human coders are not a gold standard either, so the useful question is reproducibility: would an independent, competent reading of the same text with the same codebook produce the same codes?

### 1.2 Theoretical Framework

Cohen's κ measures agreement beyond chance (Cohen, 1960). Two kinds of disagreement are distinguished:
- disagreement about **value**, where both coders rate a feature and assign different values;
- disagreement about **coverage**, where one coder rates a feature and the other judges the text silent.

Random value error weakens associations. Coverage differences change prevalence. They can also change associations if the extra ratings differ systematically from the explicit ones.

### 1.3 Aims

1. Measure value and coverage agreement on the fields the findings rest on.
2. Test the pre-registered results (P1, P3) under the second coder's codes.
3. Map each finding to the reliability of its fields.

---

## 2. Methods

### 2.1 Data Sources and Samples

| Set | Dreams | Selection |
|-------------------------|----------------------|----------------------|
| A | 50 (253 locations; 245 in text-only posts) | Random over the 1,918 primary dreams, `default_rng(20261008)` |
| B | 69 (474 locations) | All 27 noxious-animal and 18 deceased-person dreams behind P1 and P3, plus 27 of 81 gentle-animal dreams (`default_rng(20261009)`) |

One dream is in both sets. Set B is selected on the extraction's codes. The coder therefore knew that each set B dream contained an animal or a deceased person, but not where or which kind.

### 2.2 Coding Procedure and Variables

**What the coder saw.** The coder saw each post's title and text, and the extracted location list (`location_id`, `location_type`, `location_name`) for alignment only. GPT-5.2 also saw images; the second coder did not, and 2 image-only posts are excluded.

**Fields.**
- **Set A:** atmosphere, vertical level, light and affect per location; hostile entity and deceased person per dream.
- **Set B:** atmosphere, living animals present, and deceased person present, per location.

**Conventions** are documented in `validation/README.md`. The central one: atmosphere, level and affect are coded only where the text states them. Animals are counted only when living and present: not similes, toys, models, word fragments or feared absences. Codes were appended batch by batch and committed (`498e86f4`) before the comparison notebook was written.

### 2.3 Statistical Analysis

**Agreement.** Cohen's κ with a 95% CI from 2,000 bootstrap resamples of dreams. Agreement is reported on all locations, including "not mentioned", and on locations both coders rated.

**Pre-registered models under the second coder.** The registered models were re-fitted with the second coder's detection, its atmosphere, or both. Mixing coders is unbiased for detection. Mixing the second coder's atmosphere with GPT-5.2's comparison group works against P3, as shown in §3.1.

---

## 3. Results

### 3.1 Location Codes

| Field | GPT-5.2 rated | Second coder rated | κ, all locations (95% CI) | κ, both rated (n) |
|-------------------------|----------------------|----------------------|----------------------|----------------------|
| Atmosphere (10 values) | 58.0% | 29.0% | 0.36 (0.27–0.47) | — |
| Atmosphere valence | 58.0% | 29.0% | 0.42 (0.30–0.53) | 0.75 (63) |
| Atmosphere, negative vs not | — | — | — | 0.74 (63) |
| Vertical level (7 values) | 51.0% | 20.8% | 0.42 (0.29–0.57) | 0.84 (49) |
| Vertical, below/ground/above/not | — | — | 0.51 (0.39–0.64) | — |
| Light (9 values) | 20.0% | 10.6% | 0.61 (0.46–0.74) | 0.90 (25) |
| Affective response (10 values) | 49.4% | 19.2% | 0.35 (0.25–0.46) | 0.67 (44) |

These are the 245 text-only locations of set A, in 47 dreams.

GPT-5.2's additional atmosphere ratings, at locations the second coder judged silent, are negative less often than its ratings where both coders rated: 58.9% of 73 against 82.5% of 63. In set B, negative-vs-not agreement where both rated is κ = 0.89 (96.8%; 156 locations in 59 dreams).

**Finding (statistically supported):** When both coders judge that a location's atmosphere, level or light is described, they assign the same value (κ 0.74–0.90). GPT-5.2 rates these features about twice as often, by inference. **Interpretation:** values are reproducible; coverage, and therefore prevalence, is **convention-dependent**.

### 3.2 Dream-Level Entities

| Field | GPT-5.2 | Second coder | κ |
|-------------------------|----------------------|----------------------|----------------------|
| `threat` entity vs hostile entity present | 7 dreams | 13 of 47 | 0.50 |
| Any hostile or threatening entity vs hostile entity present | 17 dreams | 13 of 47 | 0.71 |
| Deceased person | 0 | 0 of 47 | — |

**Finding (statistically supported):** GPT-5.2 types many hostile beings (cult members, guards) as `authority`, `crowd` or `other` with a hostile demeanor rather than as `threat`. Analyses of the `threat` label cover only part of hostile encounters.

### 3.3 Small-Count Codes Behind the Pre-registered Tests

| Field (set B, 474 locations, 69 dreams) | κ (95% CI) | Agreement |
|-------------------------|----------------------|----------------------|
| Deceased person at the location | 0.79 (0.66–0.94) | 97.9% |
| Animal class (none, gentle, noxious, both) | 0.70 (0.60–0.79) | 92.8% |

GPT-5.2 coded 22 deceased-person locations and the second coder 28; 20 are shared.

Of 34 locations the word lists classed as noxious, the second coder found a living noxious animal at 19 and no living animal at 15. Examples of the 15:
- "worm hole";
- "worried about sharks";
- "like rats";
- "ant-headed dream makers".

Of 40 gentle locations, 27 matched and 13 had no living animal. Examples: a whale-shark model, fish wallpaper, a "dog park".

| Test | GPT-5.2 codes | Second-coder detection, GPT-5.2 atmosphere | GPT-5.2 detection, second-coder atmosphere | Both from the second coder |
|-------------------------|----------------------|----------------------|----------------------|----------------------|
| P1 (within set B) | OR 3.36 (0.82–13.82), p = 0.046 | OR 3.35 (0.48–23.36), p = 0.11 | OR 4.87 (0.74–32.07), p = 0.050 | OR 3.28 (0.22–50.16), p = 0.20 |
| P3 | OR 0.35 (0.14–0.85), p = 0.010 | OR 0.35 (0.14–0.87), p = 0.012 | OR 0.19 (0.06–0.60), p = 0.002 | — |

The p-values are one-sided, in the registered direction.

**Finding (statistically supported):** P3 is robust to the coder. P1's effect size is stable (OR ≈ 3.3–4.9). Its significance depends on a word-list detector with a 44% false-positive rate for noxious animals.

### 3.4 GPT-5.2 Test–Retest

Eight posts were submitted twice and extracted independently (notebook 01, D7):
- location types agree in all 8 pairs, and the number of locations in 7;
- the set of atmospheres agrees fully in 5 of 8 (mean Jaccard 0.75).

**Finding (statistically supported):** GPT-5.2 is consistent about places and less consistent about atmosphere, matching the coverage disagreement in §3.1.

---

## 4. Discussion

### 4.1 Summary of Findings

| Reliability | Fields |
|-------------------------|----------------------|
| κ > 0.80 where both coded | light 0.90, vertical level 0.84, atmosphere negative vs not 0.89 (set B) |
| κ 0.70–0.80 | deceased person 0.79, atmosphere valence 0.75 (set A), animal class 0.70, hostile entity (any) 0.71 |
| κ < 0.70 or convention-dependent | affect 0.67 (both coded); coverage of atmosphere, level and affect (κ 0.35–0.51 including "not mentioned"); `threat` type 0.50 |

### 4.2 Interpretation

The extraction is reliable about *what* a described atmosphere, level or light is, and unreliable about *whether* one is described. The prompt invited inference: verticality from location type, and "subtle sensory details" as state markers. GPT-5.2 followed it.

For the findings this has three consequences:
1. **Prevalence statements are statements about GPT-5.2's inferences.** Examples are the share of negative locations and the share of locations with a level.
2. **Associations estimated on GPT-5.2's codes include inferred ratings.** Where both coders rated, they agree. The inferred ratings are less often negative, so they dilute rather than create negative associations.
3. **The pre-registered deceased result is robust, and the animal result is robust in size.** The animal result needs coder-based detection before its precision can be trusted.

### 4.3 Implications

- **Cite by field.** MallWorld findings should cite the reliability of their fields from this report, in the form of the NDE reliability table (CLAUDE.md §6.2).
- **Separate inferred from explicit codes.** A revised schema should code inferred and explicit atmosphere and level separately, or require explicit evidence.
- **Detect animals with a coder.** Animal detection should be done by a coder, not by word lists.

### 4.4 Limitations

- **Not ground truth.** The second coder is a language model from a different family, not a human, and neither coder is ground truth. There is no adjudicating third coder.
- **Framework awareness.** The second coder knew the framework and the registered predictions. Its conventions were conservative, coding only explicit statements. That choice determines the coverage gap. A coder allowed to infer would have agreed with GPT-5.2 more often about coverage.
- **Sample sizes.** Set A gives 245 locations; agreement among both-rated locations rests on 25–63 locations, so intervals are wide.
- **Images.** Images were not available to the second coder.

### 4.5 Future Directions

1. **Measure inferred atmosphere directly.** Recode a sample with a convention that permits inference, to estimate how reproducible GPT-5.2's inferred atmospheres are.
2. **Rerun the duplicate-pair test** on any re-extraction.
3. **Re-measure after any schema change.** Repeat the second coding on a fresh random sample (CLAUDE.md §4.13).

---

## 5. Conclusion

GPT-5.2's MallWorld codes reproduce well where the text states a feature (κ 0.74–0.90) and diverge where the coder must decide whether the text implies one. Prevalence figures are convention-dependent.
- **P3 (the deceased):** robust to the coder.
- **P1 (animals):** robust in size, fragile in precision.
- **The archived claim** of validation "through manual review" has no record. This report replaces it with a measured reliability.

---

## References

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Krippendorff, K. (2004). *Content Analysis: An Introduction to Its Methodology* (2nd ed.). Sage.

---

## Appendix A: Statistical Summary

| Comparison | κ (95% CI) | Agreement | n (dreams) |
|-------------------------|----------------------|----------------------|----------------------|
| Atmosphere, 10 values | 0.36 (0.27–0.47) | 56.7% | 245 (47) |
| Atmosphere valence incl. not coded | 0.42 (0.30–0.53) | 64.9% | 245 (47) |
| Atmosphere coded at all | 0.38 (0.25–0.52) | 66.9% | 245 (47) |
| Valence, both rated | 0.75 (0.48–0.94) | 93.7% | 63 (33) |
| Negative vs not, both rated (set A) | 0.74 (0.46–0.94) | 93.7% | 63 (33) |
| Negative vs not, both rated (set B) | 0.89 (0.79–0.97) | 96.8% | 156 (59) |
| Vertical, both coded | 0.84 (0.68–0.96) | 87.8% | 49 (23) |
| Light, both coded | 0.90 (0.76–1.00) | 92.0% | 25 (19) |
| Affect, both coded | 0.67 (0.53–0.81) | 75.0% | 44 (28) |
| Deceased at location (set B) | 0.79 (0.66–0.94) | 97.9% | 474 (69) |
| Animal class (set B) | 0.70 (0.60–0.79) | 92.8% | 474 (69) |
