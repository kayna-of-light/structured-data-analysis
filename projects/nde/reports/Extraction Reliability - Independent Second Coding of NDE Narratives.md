# Reliability of Near-Death Experience Narrative Coding: Independent Second Coding, Test–Retest and Duplicate Audit

## Abstract

**Background**: Every statistic in the NDE project is a GPT-5.2 code of a narrative. Earlier reports listed "no human validation" as a limitation. Human coders are not a gold standard for these variables: they disagree with each other and bring their own expectations. What the analyses need is an estimate of measurement reliability, meaning how much the codes would change under an independent, competent reading of the same text with the same codebook.

**Methods**: A blind second coder (Claude) coded 100 randomly drawn accounts on 15 fields. It used only the narrative and the schema's own field descriptions, and never saw the extraction. A further 44 life reviews (40 random, plus all 6 rated harsh) were coded for judgment source and intensity. Agreement was measured with Cohen's κ, Gwet's AC1, bootstrap confidence intervals and exact McNemar tests of prevalence bias. Near-duplicate submissions were detected by text similarity. They were used to estimate GPT-5.2's consistency with itself and to test whether duplicates affect any result.

**Results**: Median κ across 15 binary fields is 0.83. Nine fields exceed 0.80: tunnel 0.97, life review 0.92, telepathic communication 0.88, guidance 0.88, being of light 0.87. "Unknown presence" is the weakest field (κ 0.44), because the schema does not define its boundary with "other". GPT-5.2's "implied" mission codes are liberal: calibrated to the second coder, mission commissioning falls from 21.9% to 14.8% (95% CI 12.2–18.4). Judgment intensity is reproducible as an ordinal scale (weighted κ 0.74) but not at its harsh boundary. Under the second coder, harsh judgment is 8.7% of rated reviews (1.3–16.8) rather than 1.4%, and loving:harsh is 6.4:1 (3.1–43.9) rather than 36.2:1. Loving:critical is unchanged (1.77 vs 1.72). Of the records, 1.8% are redundant copies; removing them moves headline rates by less than 0.5 percentage points. GPT-5.2's test–retest κ on near-identical texts has a median of 0.88.

**Conclusions**: The coding behind most reported findings is reproducible at κ ≥ 0.77. Three results depend on codebook conventions rather than on stable measurement and should be revised: the prevalence of "unknown presence", the prevalence of mission commissioning, and the precise loving:harsh ratio. Boundary *type* is also unreliable. The finding that life reviews are predominantly loving and rarely condemning survives. The 36.5:1 ratio does not.

**Keywords**: inter-rater reliability, Cohen's kappa, Gwet's AC1, large language model annotation, near-death experience, test–retest, measurement error, duplicate detection

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `08_extraction_reliability.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/08_extraction_reliability.ipynb) |
| Second-coder codes | `validation/second_coder_codes.jsonl` (141 accounts) | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/validation/) |
| Coding conventions | `validation/README.md` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) |
| First coder | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |
| Second coder | Claude (blind to the extraction) | Anthropic |

---

## 1. Introduction

### 1.1 Background

Large language models are increasingly used to code text for research. On many annotation tasks they match or exceed trained crowd workers (Gilardi et al., 2023). Their output is still a measurement and has measurement error. In this project every variable is a GPT-5.2 code of a self-reported narrative. The correctness of every downstream statistic therefore depends on how reproducible those codes are.

The earlier reports stated that "no human validation" had been performed and presented this as the open question. That framing assumes a human coder would supply the correct answer. For variables such as "was the judgment harsh?" or "was the presence identified?", human coders are a second reading with their own error and expectations, not ground truth (Krippendorff, 2004). Agreement between independent coders measures what matters: how much of a code reflects the text and how much reflects the coder.

### 1.2 Theoretical Framework

Reliability analysis makes no claim about which coder is right. Cohen's κ (Cohen, 1960) measures agreement beyond chance. When a feature is rare, κ can be low even when the coders almost always agree (Feinstein & Cicchetti, 1990), so Gwet's AC1 (Gwet, 2008), which is robust to low prevalence, is reported alongside it. Agreement bounds the measurement error in the data. If two independent coders agree at κ ≈ 0.8, random coding error cannot create a large association, and it can only weaken a real one. Systematic convention differences are different: one coder reading a category more liberally can shift prevalence, and therefore ratios, without lowering κ much. Both kinds of error are examined.

For the framework analyses this matters directly. A hit is only as strong as the measurement of the variables that produce it.

### 1.3 Aims

1. **Quantify** agreement between the GPT-5.2 extraction and a blind second coder on the variables the reported findings rely on.
2. **Identify** systematic differences in prevalence and their causes: coder error or codebook ambiguity.
3. **Test** the robustness of the life-review judgment results, especially the loving:harsh ratio.
4. **Measure** near-duplicate submissions and GPT-5.2's consistency with itself.
5. **Map** each reported finding to the reliability of the fields it rests on.

---

## 2. Methods

### 2.1 Data Sources and Samples

| Sample | Accounts | Selection |
|-------------------|---------|----------------------------|
| Set A | 100 | Simple random sample of all 6,751 records (seed 20261006) |
| Set B | 44 | 40 random from the 428 life reviews with a rated judgment intensity (seed 20261007), plus all 6 rated `harsh_condemning` (census; 2 already drawn) |
| Coded in total | 141 | 3 accounts are in both sets |
| Near-duplicate scan | 6,751 | All records |

The median length in set A (704 words) is close to that of all records (683). The notebook re-draws both samples from their seeds and asserts that they match the coded accounts.

### 2.2 Coding Procedure and Variables

The second coder saw exactly what GPT-5.2 received: dataset, title, reported date and narrative. It never saw an extracted value. The codebook was the schema itself, meaning the `Field(description=...)` text and enum values in `models/questionnaire.py`. Codes were written to `validation/second_coder_codes.jsonl` before any comparison and were not revised afterwards. Where the schema is silent, the coder followed conventions recorded in `validation/README.md`. For example, a spoken "not your time" takes precedence over a co-present barrier when choosing the boundary type.

**Set A (15 fields)**: light encounter (5 categories); unknown presence; God or Jesus; deceased relatives; guidance received; teaching; telepathic communication; life review (extensive, brief, no, not mentioned); tunnel; boundary encounter (5 categories); return agency (5 categories); mission commissioned; earthly-mission return reason; environment more real than earthly life; religious background (9 categories).

**Set B**: life review occurrence; judgment source (self, being of light, guide or entity, deceased relative, none, not mentioned); judgment intensity (loving/gentle, neutral, uncomfortable, harsh/condemning, not applicable, not specified).

### 2.3 Statistical Analysis

- Percentage agreement, Cohen's κ and Gwet's AC1 per field; 95% CIs from 2,000 bootstrap resamples of accounts
- Exact McNemar (binomial) test of prevalence bias per binary field (McNemar, 1947), with Holm correction (Holm, 1979)
- Linear-weighted κ (Cohen, 1968) for the ordinal judgment scale
- Population estimate of judgment intensity under the second coder: the GPT-5.2 category shares among the 428 rated reviews are multiplied by the second coder's distribution within each category (census for harsh, random draw otherwise), with a 5,000-draw stratified bootstrap
- Calibrated mission prevalence: the GPT-5.2 explicit and implied shares are multiplied by the second coder's confirmation rate in each category, with bootstrap CIs
- Near-duplicate detection: word-trigram TF-IDF cosine similarity on the full narrative (≥ 0.5), or on the first 200 words (≥ 0.6) when both accounts have at least 30 words before appended questionnaire text; groups formed by union-find
- GPT-5.2 test–retest κ on duplicate pairs, which were extracted independently

---

## 3. Results

### 3.1 Agreement on 100 Random Accounts

| Field | GPT-5.2 + | Coder + | Agreement | Cohen's κ (95% CI) | AC1 |
|----------------------------|---------|---------|---------|------------------|---------|
| Tunnel | 24 | 25 | 99.0% | 0.97 (0.91–1.00) | 0.98 |
| Life review | 15 | 15 | 98.0% | 0.92 (0.79–1.00) | 0.97 |
| Telepathic communication | 31 | 28 | 95.0% | 0.88 (0.76–0.98) | 0.91 |
| Guidance received | 58 | 54 | 94.0% | 0.88 (0.78–0.96) | 0.88 |
| Being of light | 14 | 13 | 97.0% | 0.87 (0.70–1.00) | 0.96 |
| Deceased relatives | 22 | 21 | 95.0% | 0.85 (0.72–0.97) | 0.92 |
| Any light encounter | 62 | 63 | 93.0% | 0.85 (0.73–0.95) | 0.87 |
| Return decided by a being | 37 | 35 | 92.0% | 0.83 (0.70–0.93) | 0.85 |
| God or Jesus | 14 | 19 | 95.0% | 0.82 (0.65–0.96) | 0.93 |
| Boundary (any type) | 43 | 40 | 89.0% | 0.77 (0.63–0.89) | 0.79 |
| Earthly-mission return reason | 6 | 7 | 97.0% | 0.75 (0.39–1.00) | 0.97 |
| More real than earthly life | 13 | 8 | 95.0% | 0.74 (0.47–0.94) | 0.94 |
| Mission commissioned | 20 | 12 | 92.0% | 0.71 (0.49–0.88) | 0.89 |
| Teaching | 14 | 13 | 93.0% | 0.70 (0.45–0.88) | 0.91 |
| **Unknown presence** | **13** | **21** | **84.0%** | **0.44 (0.20–0.66)** | **0.78** |
| Light encounter (5 categories) | | | 77.0% | 0.67 (0.56–0.78) | 0.72 |
| Return agency (5 categories) | | | 77.0% | 0.69 (0.58–0.79) | 0.72 |
| Religious background (9 categories) | | | 90.0% | 0.79 (0.67–0.90) | 0.89 |

No prevalence difference survives Holm correction. The largest asymmetry is mission commissioning: 20 vs 12, with all 8 discordant accounts coded by GPT-5.2 only (exact p = 0.008, Holm p = 0.12).

**Critical Finding**: The median κ across binary fields is **0.83**, in the "almost perfect" band of Landis and Koch (1977). The variables behind most reported findings agree at κ ≥ 0.77: light, beings, deceased relatives, telepathy, guidance, life review, tunnel, boundary presence and return agency. At this level random coding error cannot produce the large associations reported in notebooks 01–07; it can only weaken them. Only "unknown presence" falls below 0.6.

### 3.2 Why "Unknown Presence" Disagrees

The second coder flagged 12 unidentified beings that GPT-5.2 did not code as `unknown_presence`. GPT-5.2 coded 10 of them as `other`, as angels, or as no being. Counting GPT-5.2's `other` as unknown raises κ only to 0.51. GPT-5.2 is consistent with itself on the field (test–retest κ 0.83, §3.6). The instability therefore lies in the codebook, not inside a coder: the schema does not define where "unknown presence" ends and "other" begins.

**Finding**: "Unknown presence" is a **category label assigned by the coder**, not a word chosen by the experiencer. Its share of identifications cannot be used as evidence about the vocabulary experiencers prefer.

### 3.3 Mission Commissioning Is Over-coded as "Implied"

| GPT-5.2 code | n | Confirmed by second coder |
|--------------|---|---------------------------|
| `yes_explicit` | 7 | 7 (100%) |
| `implied` | 13 | 5 (38.5%) |
| `no` / `not_mentioned` | 80 | 0 |

The eight unconfirmed "implied" codes are general life lessons: love more, forgive, "go, live your life well", "chill out". The schema asks whether the experiencer was given "a specific task/mission". Applied to the full data, GPT-5.2's 21.9% (explicit 10.4% + implied 11.5%) becomes **14.8% (95% CI 12.2–18.4)** under the second coder's reading. The link between an earthly-mission return reason and commissioning holds under both coders (GPT-5.2: 6/6; second coder: 6/7).

**Finding**: Mission commissioning is **overstated by about a third**. The return-reason–commissioning association reported in the Mission-Based Returns report is not affected.

### 3.4 Boundary Type Depends on an Unstated Precedence Rule

| GPT-5.2 \ second coder | Physical barrier | Threshold | Verbal limit |
|------------------------|------------------|-----------|--------------|
| Physical barrier | 3 | 2 | **11** |
| Threshold | 0 | 4 | 1 |
| Verbal limit | 0 | 1 | 14 |

Among the 36 accounts that both coders treat as a boundary, the type agrees in 58% (κ = 0.34). The 11 discordant accounts contain both a barrier and a being who says "not your time". The schema gives no rule for choosing between them.

**Finding**: Boundary **presence** is reliable (κ 0.77); boundary **type** is not. Comparisons between boundary types rest on how the coder resolves co-occurrence. These include the East–West report's boundary-type × return-agency association and the verbal-limit function in the entity-function analysis.

### 3.5 Life-Review Judgment

| GPT-5.2 \ second coder | Loving | Neutral | Uncomfortable | Harsh | Not applicable | n |
|----------------------|---------|---------|-------------|---------|--------------|---------|
| Loving / gentle | 19 | 1 | 1 | 0 | 0 | 21 |
| Neutral | 0 | 2 | 1 | 0 | 2 | 5 |
| Uncomfortable | 2 | 1 | 6 | **3** | 0 | 12 |
| Harsh / condemning | 0 | 0 | 1 | **4** | 1 | 6 |

Agreement on intensity is 70.5% (κ = 0.57, 0.38–0.74). As an ordinal scale, linear-weighted κ is **0.74** (0.57–0.87; n = 41 rated by both). The second coder confirmed 4 of the 6 GPT-5.2 harsh reviews. It also rated 3 of the 12 GPT-5.2 "uncomfortable" reviews as harsh. All three are hellish experiences in which the experiencer condemns themselves. Judgment *source* agrees less well (63.6%, κ = 0.51; external evaluator vs not, κ = 0.58). The main disagreement is GPT-5.2 "guide or entity" against second-coder "being of light" (5 of 18).

Reweighted to the 428 rated life reviews:

| Quantity | GPT-5.2 | Second coder (95% CI) |
|----------|---------|-----------------------|
| Loving / gentle | 50.7% | 55.0% (45.2–66.0) |
| Neutral | 19.9% | 13.8% (2.8–24.9) |
| Uncomfortable | 28.0% | 22.5% (10.6–34.6) |
| Harsh / condemning | 1.4% | **8.7% (1.3–16.8)** |
| Loving : harsh | 36.2 : 1 | **6.4 : 1 (3.1–43.9)** |
| Loving : critical | 1.72 : 1 | 1.77 : 1 (1.14–3.13) |

In 97.2% of bootstrap draws, the second coder's harsh share exceeds GPT-5.2's.

**Critical Finding**: The loving:harsh ratio is **not a stable property of the data**. It rests on 6 harsh cases out of 428, and it moves between roughly 3:1 and 44:1 depending on where a coder draws the uncomfortable/harsh line. Two results are stable under both coders. Loving evaluation is the most common category (51–55%). Loving outnumbers critical evaluation by about 1.7–1.8 to 1. Harsh condemnation is a minority (1.4–8.7%).

### 3.6 Near-Duplicates and GPT-5.2 Test–Retest

| Item | Value |
|----------------------------|----------------------------|
| Flagged pairs | 125 (46 IANDS–NDERF, 58 within NDERF, 21 within IANDS) |
| Records involved | 238 (3.5%) |
| Distinct experiences | 117 |
| Redundant records | **121 (1.8%)** |
| Pairs with near-identical text (similarity ≥ 0.9) | 21 |

Many within-NDERF pairs are the same account stored under two file-name schemes, for example `nderf-05582_greg-w-nde-13225` and `nderf-13225_greg-w-nde`. One re-translated account (`nderf-04781_ken-d-nde-9006` and `nderf-13208_ken-d-nde`) has similarity 0.27 and was not flagged, so 1.8% is a lower bound.

| Headline rate | All records | Duplicates removed | Change |
|---------------|-------------|--------------------|--------|
| Being of light | 11.81% | 11.75% | −0.06 |
| Life review | 17.52% | 17.35% | −0.18 |
| Telepathic communication | 26.97% | 26.52% | −0.46 |
| Mission commissioned | 21.92% | 21.67% | −0.25 |
| Deceased relatives | 17.86% | 17.75% | −0.11 |
| Loving : harsh | 36.2 | 34.2 | −2.0 |
| Loving : critical | 1.72 | 1.71 | −0.01 |

Because each copy was extracted independently, the pairs measure GPT-5.2's consistency with itself. On the 21 near-identical pairs, the median test–retest κ across binary fields is **0.88**. On all 125 pairs, where texts differ in translation, length or appended answers, it is 0.75. The least stable fields are the ones the inter-coder analysis also flags: "more real than earthly life" (0.58 and 0.46) and judgment intensity (0.58 and 0.52).

**Finding**: Duplicates **do not change any reported result**. The extraction is **consistent with itself** on most fields and unstable on the same two fields where the coders disagree.

---

## 4. Discussion

### 4.1 Summary of Findings

1. Median inter-coder κ is 0.83. Nine fields exceed 0.80 and the main phenomenological variables reach κ ≥ 0.77.
2. "Unknown presence" (κ 0.44) is a codebook-dependent label.
3. Mission commissioning is over-coded: 21.9% under GPT-5.2, 14.8% calibrated. The mission-return association is unaffected.
4. Boundary type is unreliable (κ 0.34); boundary presence is reliable (κ 0.77).
5. Judgment intensity is reliable as an ordinal scale (weighted κ 0.74). The loving:harsh ratio is coder-dependent: 36.2:1 under GPT-5.2, 6.4:1 under the second coder (CI 3.1–43.9). Loving:critical is stable at about 1.7–1.8:1.
6. 1.8% of records are redundant copies, with no effect on results.
7. GPT-5.2 test–retest κ has a median of 0.88 on near-identical text.

### 4.2 Interpretation

| Reported finding | Fields it rests on | Reliability | Consequence |
|----------------------------|----------------------------|-------------------------|----------------------------|
| Being of Light properties: communication, guidance, teaching | light, God/Jesus, telepathy, guidance, teaching | κ 0.70–0.88 | Holds |
| "Unknown presence" as the majority identification | being identifications | κ 0.44 | No interpretive weight |
| Judgment character (revelation, not condemnation) | judgment intensity | weighted κ 0.74 | "Rarely condemning, predominantly loving" holds; 36.5:1 does not |
| Normative sequence elements | tunnel, light, life review, boundary | κ 0.77–0.97 | Holds |
| Mission commissioning prevalence | mission commissioned | κ 0.71, liberal "implied" | About 15%, not 22% |
| Mission return → commissioning | return reasons, mission | holds under both coders | Holds |
| East–West: relatives and religious figures | relatives, God/Jesus | κ 0.85, 0.82 | Holds |
| East–West: boundary types | boundary type | κ 0.34 | Not reliable |
| Entity function differentiation | being groups, teaching, agency | κ 0.70–0.88 | Holds; verbal-limit function convention-dependent |
| Hyper-reality ("more real") | comparative reality | κ 0.74, retest 0.58 | Prevalence approximate |

Two kinds of error appear. **Random error** is small for most fields, so the associations reported in the project are not coding noise. **Convention error** is concentrated in four places, and in each the schema leaves a decision open: "unknown" vs "other", implied mission, co-occurring boundary types, and the uncomfortable/harsh line. In each case one coder's reading is not more correct than the other's; the schema simply does not decide the question. Results that depend on those decisions should be reported as convention-dependent.

The second coder knew the research framework. If that knowledge biased it, the bias would favour gentler judgment codes. The disagreements on judgment run the other way, with the second coder coding harsh more often. Framework knowledge therefore does not explain them.

### 4.3 Implications

1. "No human validation" should be replaced in all reports by the measured reliability of the fields each report uses.
2. The loving:harsh ratio should be reported with its coder-dependence, or replaced by the stable loving:critical ratio.
3. Mission-commissioning prevalence should be reported as a range (14.8–21.9%) or restricted to explicit codes.
4. The schema needs five fixes:
   - define `unknown_presence` against `other`;
   - give a precedence rule for co-occurring boundary types;
   - require a specific task for implied missions;
   - anchor `harsh_condemning` with examples, including self-condemnation;
   - merge `no` and `not_mentioned` where narratives cannot distinguish them.
5. The loader should offer a near-duplicate filter for future analyses. Current results are insensitive to it.

### 4.4 Limitations

1. **The second coder is also a language model.** It belongs to a different model family and was blind to the extraction, but its errors may correlate with GPT-5.2's on hard cases.
2. **No adjudication.** With two coders, agreement can be measured but disagreements cannot be resolved; neither coder is a reference standard.
3. **Sample size.** With n = 100, κ intervals are wide (teaching 0.45–0.88). Set B has only 6 harsh cases, so the harsh share has a wide interval.
4. **Framework awareness.** The second coder knew the hypotheses under test. The observed disagreements run against the framework-favourable direction, but this does not exclude bias on other fields.
5. **Fields not tested.** Perceptual-depth markers, aftereffects and before/after measures were not recoded.

### 4.5 Future Directions

1. Re-extract with the schema fixes above and re-measure agreement on a fresh random sample.
2. Add a third coder (a different model or a human panel) to adjudicate disagreements on the four convention-dependent fields.
3. Extend second coding to aftereffects and perceptual markers.
4. Integrate near-duplicate filtering into `nde_dataset.load_frame()` as an option.

---

## 5. Conclusion

The question was never whether a human would agree with the extraction. It was whether the measurement is reproducible. For most variables it is: across 15 fields the median agreement between GPT-5.2 and a blind second coder is κ = 0.83. GPT-5.2 agrees with itself at κ = 0.88 on duplicate submissions. Duplicates affect no result.

Where the measurement is not reproducible, the cause is the codebook rather than the coder, and the affected results are now identified. "Unknown presence" is a label, not a measured preference. Mission commissioning is about 15%, not 22%. Boundary types cannot be compared reliably. Life reviews are predominantly loving and rarely condemning, but the precise 36.5:1 loving:harsh ratio depends on where a coder draws the line and should not be quoted as a property of the phenomenon.

---

## References

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220.

Feinstein, A. R., & Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543–549.

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences*, 120(30), e2305016120.

Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology*, 61(1), 29–48.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

Krippendorff, K. (2004). *Content Analysis: An Introduction to Its Methodology* (2nd ed.). Sage.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions or percentages. *Psychometrika*, 12(2), 153–157.

---

## Appendix A: Statistical Summary

| Test | Value |
|----------------------------|----------------------------|
| Median κ, 15 binary fields (set A, n = 100) | 0.83 (range 0.44–0.97) |
| Gwet's AC1, binary fields | 0.78–0.98 |
| Prevalence bias, mission (exact McNemar) | 8 vs 0 discordant, p = 0.008, Holm p = 0.12 |
| Unknown presence κ (incl. GPT `other`) | 0.44 (0.51) |
| Boundary type κ among both-boundary accounts | 0.34 (n = 36) |
| Judgment intensity κ / linear-weighted κ | 0.57 / 0.74 |
| Judgment source κ | 0.51 |
| Mission commissioning, calibrated | 14.8% (12.2–18.4) vs 21.9% |
| Harsh share, second coder | 8.7% (1.3–16.8) vs 1.4% |
| Loving : harsh, second coder | 6.4 (3.1–43.9) vs 36.2 |
| Loving : critical, second coder | 1.77 (1.14–3.13) vs 1.72 |
| Redundant records | 121 / 6,751 (1.8%) |
| GPT-5.2 test–retest median κ | 0.88 (21 near-identical pairs); 0.75 (125 pairs) |

## Appendix B: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **Analysis Notebook**: [08_extraction_reliability.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/08_extraction_reliability.ipynb)
- **Second-coder codes and conventions**: `projects/nde/validation/`
- **Figures**: `output/08_reliability_agreement.png`, `output/08_reliability_judgment.png` (generated by the notebook)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
