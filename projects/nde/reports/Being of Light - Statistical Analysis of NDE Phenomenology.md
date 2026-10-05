# The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology

> **Correction notice (2026-10-05).** This report was revised after a statistical audit of the underlying notebooks (`docs/STATISTICAL_AUDIT_2026-10.md`). Several headline results in the earlier version were produced by coding errors or invalid tests and have been corrected or withdrawn: the χ² = 365.14 for religion × identification (a sparse-cell artifact; the valid association is weak), "experiential properties identical — all differences below 10%" (an artifact of broken fields; three properties differ by more than 10 points), "0.0% increased death fear" (a broken scale; 0.9%), "54.7% no external judgment" (unmentioned sources were counted as "no judgment"; 55.9% of classifiable reviews involve an external evaluator), the "singular Being even for polytheists" finding (not measurable with the schema), and the "below-baseline" machine-learning result (overfitting on 37 test cases). Findings that hold — rare harsh judgment, more teaching and telepathy in Light-Being encounters, a majority "unknown presence" identification, and a larger spirituality increase — are reported with confidence intervals and narrative-length adjustment. The LaTeX and PDF versions were regenerated from this corrected text.

## Abstract

Near-death experiences frequently involve encounters with a "Being of Light" described in terms evoking divine presence. The Swedenborgian correspondential framework proposes that the Being is a constant reality whose *identification* is culturally mediated ("constant state, variable form"). We tested this against 6,751 structured NDE records (NDERF n=5,659; IANDS n=1,092; two exact duplicates removed) coded by GPT-5.2 structured extraction.

Encounters identified as a divine figure or an unidentified presence occurred in 27.9% of NDEs (95% CI 26.8–28.9); only a third of these were coded as a visual *being of light*. Half (50.6%) were identified only as an "unknown presence". Religious background was weakly associated with the name used (χ² = 15.04, df = 6, p = 0.020, Cramér's V = 0.11; the previously reported χ² = 365.14 was a sparse-cell artifact). When the evaluation during a life review was rated, harsh condemnation was rare (1.7%; loving 60.3%, uncomfortable 21.1%), giving a loving:harsh ratio of 36.5:1 (95% CI 14–136) but a loving:critical ratio of 2.7:1. Light-Being encounters involved more teaching (25.3% vs 12.6%) and telepathic communication (48.2% vs 34.2%) than encounters with other beings only, differences that survived adjustment for narrative length. Comparing Christians who named the Being "Jesus" with those who named it "unknown presence", guidance, teaching, telepathy, belonging and mission did not differ, but visual-being coding (+45 percentage points) and unity experience (−20 pp) did. Death fear fell in 88.0% and rose in 0.9% of Light-Being experiencers who stated both levels; this did not differ from other-being encounters. Spirituality rose in 89.2%, with a larger increase than after other-being encounters (p = 0.003).

The data support a weak cultural shaping of vocabulary over a functionally similar encounter, consistent with "constant state, variable form", but they also show that the name covaries with the *mode* of the encounter. Several previously reported confirmations do not survive correction.

**Keywords:** near-death experience, Being of Light, correspondences, religious experience, cultural mediation, Swedenborg

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Being of Light Analysis | `01_being_of_light_analysis.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb) |
| Conceptual Framework Analysis | `04_conceptual_framework_theory.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files; 6,751 unique narratives) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

The "Being of Light" stands among the most iconic elements of near-death experience phenomenology. Raymond Moody's foundational research identified this figure as a brilliant light experienced as a personal presence—characterized by unconditional love and apparently complete knowledge of the experiencer's life (Moody, 1975). Studies across cultures have confirmed the prevalence of light-related experiences in NDEs (van Lommel, 2010; Greyson, 2021), yet the interpretation of these encounters remains contested.

Experiencers from different religious backgrounds identify this presence differently: Christians often report seeing Jesus or God, Hindus may perceive Krishna or a goddess, while secular experiencers describe an "unknown presence" or "pure light". Skeptics read this variation as cultural construction; religious traditionalists sometimes read it as literal visitation by their tradition's figures. A third possibility is that identification varies while the experiential character remains constant.

### 1.2 Theoretical Framework

The analysis uses Emanuel Swedenborg's doctrine of correspondences as a hypothesis generator (Swedenborg, 1758). The doctrine proposes that spiritual realities present themselves through forms drawn from the recipient's mental repertoire. On this model, the Being of Light is what Swedenborg termed the "Divine Human"; a Christian's repertoire supplies Jesus, a Hindu's Krishna, an atheist's "light" or "presence". The spiritual reality is constant; the perceptual form varies.

This generates testable predictions: (1) identification should vary with religious background (cultural mediation); (2) the qualitative character of the encounter should not; (3) experiencers using different labels should report the same experiential properties.

### 1.3 Aims

The primary aim is to test whether identification varies with religious background while the properties of the encounter remain constant. Secondary aims are to quantify identifications, characterize judgment during life reviews, compare communication and guidance with encounters involving other beings, and examine transformative effects.

---

## 2. Methods

### 2.1 Data Sources

Records came from the Near-Death Experience Research Foundation (NDERF, 5,659 accounts) and the International Association for Near-Death Studies (IANDS, 1,092 accounts). Two narratives appeared twice with identical content and were counted once (N = 6,751). Both archives consist of self-selected online submissions; country is stated for only 12% of accounts.

### 2.2 Coding Scheme

Each record was processed with GPT-5.2 (Azure OpenAI) into the Pydantic schema in `models/questionnaire.py` (131 leaf fields). No human validation of the extraction has been performed. Relevant fields: `light_encounter`, `being_identifications` (multi-select), `communication_modes`, `guidance_types`, life-review `judgment_source`, `judgment_intensity` and experiencer `emotional_tone`, before/after levels of death fear, spirituality and religiosity, and religious background and belief at the time of the NDE.

### 2.3 Operational Definition of the Light-Being Subset

A record was included if `being_identifications` contained God, Jesus, a specified religious figure, the Buddha, or an "unknown presence" (n = 1,881). This differs from the separate field `light_encounter = being_of_light` (n = 797, used in the East-West report). Only 31.8% of the Light-Being subset was coded `being_of_light`; 35.7% was coded brilliant light, 12.2% presence without visual, and **14.5% no light at all**. The subset is best described as *encounters identified as a divine figure or an unidentified presence*. Comparison group: records with only other beings (deceased relatives, angels, other; n = 1,898).

### 2.4 Statistical Analysis

Proportions are reported with Wilson 95% confidence intervals and explicit denominators (cases where the field was "not mentioned" are excluded where stated). Associations: χ² tests with expected-count checks, Cramér's V, Fisher exact tests, permutation tests for sparse tables, Holm correction for families of comparisons. Before/after changes: Wilcoxon signed-rank tests on 5-level ordinal scales. Light-Being accounts are 45% longer than other-being accounts (median 1,028 vs 710 words); between-group differences are therefore also reported as odds ratios adjusted for log narrative word count. Prediction: cross-validated logistic regression scored by log-loss and AUC.

---

## 3. Results

### 3.1 Prevalence and Composition

The Light-Being subset comprised 1,881 NDEs (27.9%, 95% CI 26.8–28.9); 1,898 (28.1%) involved other beings only and 2,972 (44.0%) no identified being. 59.0% of Light-Being encounters involved the Light Being alone and 41.0% also other beings.

Across all records, 40.9% described brilliant light, 11.8% a being of light, and 4.2% a presence without visual form; 24.2% reported no light and 18.9% did not address it.

### 3.2 Presence by Religious Background, Gender and Age

| Religious background | n | Light-Being presence | 95% CI |
|---|---|---|---|
| Christian | 1,282 | 39.7% | 37.1–42.4 |
| Jewish | 38 | 28.9% | 17.0–44.8 |
| Spiritual not religious | 22 | 27.3% | 13.2–48.2 |
| Other | 115 | 24.3% | 17.4–32.9 |
| Atheist/agnostic | 100 | 24.0% | 16.7–33.2 |
| Muslim | 43 | 9.3% | 3.7–21.6 |
| Not mentioned | 5,122 | 25.2% | 24.0–26.4 |

Presence varied by religious background (six groups with adequate expected counts: χ² = 35.25, df = 5, p < 0.0001, Cramér's V = 0.15). It did not vary by gender (31.4% vs 30.9%; χ² = 0.07, df = 1, p = 0.79) or age group (χ² = 4.25, df = 3, p = 0.24; age is reported for 23% of records, median age 15).

**Finding:** Light-Being presence is **not** uniform across religious backgrounds — highest among Christians, lowest among Muslims (small n). Accounts that state a religion are about three times longer than those that do not, so these rates are not representative of the whole archive.

### 3.3 Hindu and Buddhist Experiencers ("Singularity")

Only 29 records have a Hindu or Buddhist background; 8 include a Light-Being identification (27.6%, 95% CI 14.7–45.7). The schema records *which kinds* of being were identified, not *how many*, so singularity cannot be measured. Among the 8 cases, two name more than one divine figure (Buddha + Guanyin + angels; God + Jesus) and one describes "four intelligent beings".

**Finding:** the earlier claim that "polytheists encounter a singular transcendent entity" is **not supported by this dataset**; the question is underdetermined.

### 3.4 Guidance, Teaching and Communication

Rates are per experiencer; guidance and communication are coded per NDE, not per being.

| Element | Light Being | Other beings only | χ² (df = 1) | Length-adjusted OR (95% CI) |
|---|---|---|---|---|
| Significant guidance | 81.7% | 74.9% | 25.24 | 1.34 (1.14–1.57) |
| Teaching guidance | 25.3% | 12.6% | 98.0 | 1.96 (1.64–2.35) |
| Life guidance | 36.3% | 27.9% | 30.5 | 1.28 (1.11–1.48) |
| Informational guidance | 37.8% | 31.8% | 14.9 | 1.19 (1.04–1.36) |
| Comfort | 35.7% | 31.6% | 7.0 | 1.03 (0.90–1.19) |
| Directional guidance | 46.5% | 48.0% | 0.8 | 0.93 (0.81–1.05) |
| Telepathic communication | 48.2% | 34.2% | 75.6 | 1.53 (1.33–1.76) |
| Nonverbal communication | 40.2% | 28.0% | 62.2 | 1.50 (1.30–1.73) |
| Normal speech | 30.5% | 40.1% | 38.0 | 0.69 (0.60–0.79) |

**Finding (statistically supported):** guidance is modestly more frequent in Light-Being encounters (ratio 1.09). **Teaching** is about twice as frequent (25.3% vs 12.6%), and telepathic and nonverbal communication are more frequent while ordinary speech is less frequent; all of these survive adjustment for narrative length. (The earlier report's "telepathic 34.8%" was a share of mentions, not of experiencers.)

### 3.5 Being Identification

Half of Light-Being encounters (951/1,881 = 50.6%, 95% CI 48.3–52.8) were identified only as an unknown presence. By first-listed identification: unknown presence 51.9%, God 22.5%, Jesus 18.9%, specified religious figure 6.5%, Buddha 0.3% (the first-listed figure depends on the order in which the extractor listed items; 50.6% is the order-independent value).

**Religious background and naming.** The previously reported χ² = 365.14 (df = 32) used a table in which 69% of cells had expected counts below 5; 82% of the statistic came from the two Buddhists who named the Buddha (expected count 0.01). A permutation test (2,000 shuffles, p = 0.0005) confirms that an association exists. On a collapsed table meeting the test's assumptions (n = 590 with known religion):

| Religion group | God | Jesus | Named figure | Unknown presence |
|---|---|---|---|---|
| Christian (n=509) | 21.8% | 25.1% | 8.8% | 44.2% |
| Non-religious (n=30) | 10.0% | 10.0% | 13.3% | 66.7% |
| Other religion (n=51) | 19.6% | 9.8% | 13.7% | 56.9% |

χ² = 15.04, df = 6, p = 0.020, Cramér's V = 0.11. Using belief at the time of the NDE instead, Christians identify an unknown presence only in 38.0% of encounters versus 61.5–64.3% for atheist/agnostic, spiritual-not-religious and other experiencers (χ² = 38.40, df = 3, p < 0.0001, V = 0.24).

**Finding (statistically supported):** cultural background shapes naming, weakly to moderately, and an "unknown presence" is the most common identification in every group.

### 3.6 Do Different Names Go with Different Properties?

**All Light-Being encounters, named figure (n = 930) vs unknown presence only (n = 951)** (Fisher tests, Holm-corrected over 11 properties): no difference in guidance (81.5% vs 81.9%), telepathy (49.7% vs 46.8%), loving judgment among rated reviews (62.0% vs 54.6%), love tone (19.9% vs 24.0%), unity (34.9% vs 38.3%) or belonging (32.0% vs 30.6%). Named-figure encounters more often involve teaching (29.6% vs 21.0%), mission commissioning (43.2% vs 33.8%), pleasant valence (51.4% vs 44.4%) and, most strongly, a visual *being of light* coding (44.9% vs 19.0%).

**Christians (belief at the time of the NDE): Jesus only (n = 102) vs unknown presence only (n = 175).**

| Property | Jesus only | Unknown only | Difference (pp) | 95% CI | Holm p |
|---|---|---|---|---|---|
| Guidance received | 84.3% | 82.3% | +2.0 | −7.0 to 11.1 | 1.00 |
| Teaching guidance | 23.5% | 22.3% | +1.2 | −9.0 to 11.5 | 1.00 |
| Telepathic communication | 52.0% | 50.3% | +1.7 | −10.5 to 13.9 | 1.00 |
| Sense of belonging | 29.4% | 34.3% | −4.9 | −16.2 to 6.4 | 1.00 |
| Mission commissioned | 45.1% | 41.1% | +4.0 | −8.1 to 16.1 | 1.00 |
| Loving judgment (rated; n=9 vs 16) | 55.6% | 56.2% | −0.7 | wide | 1.00 |
| Life review | 16.7% | 28.6% | −11.9 | −21.8 to −2.1 | 0.26 |
| Pleasant valence (stated) | 63.6% | 49.7% | +13.9 | 1.9 to 26.0 | 0.26 |
| Coded as visual being of light | 62.7% | 17.7% | +45.0 | 34.1 to 56.0 | <0.001 |
| Unity experience | 46.1% | 65.7% | −19.6 | −31.6 to −7.7 | 0.016 |

Using religious *background* gives the same pattern (life review −16.0 pp, Holm p = 0.022; unity −21.5 pp, Holm p = 0.005).

**Finding (mixed).** The earlier statement that "all differences fall below 10%" compared six properties of which three were broken (0% vs 0%) and three used all encounters as the denominator (e.g. "loving judgment 4.9% vs 5.0%"). Correctly measured, the **functional** profile — guidance, teaching, telepathy, belonging, mission — is statistically indistinguishable between the labels, which is consistent with "constant state, variable form". But the **mode** of the encounter differs: "Jesus" encounters are far more often a visual luminous figure, and "unknown presence" encounters more often involve unity. Confidence intervals of about ±10 points exclude large functional differences but not moderate ones.

### 3.7 Life Review and Judgment

Among the 453 Light-Being encounters with a life review (24.1%):

**Who evaluated.** Of 367 reviews with a stated source, 55.9% (95% CI 50.7–60.9) involved an external evaluator (Being of Light 121, guide 84) and 44.1% none or self-judgment. The previous "54.7% no external condemnation" counted the 86 unstated sources as "no judgment".

**Character of the evaluation** (242 rated reviews):

| Intensity | Light-Being life reviews | Reviews where the Being of Light evaluated (n = 146 rated) |
|---|---|---|
| Loving/gentle | 60.3% (54.1–66.3) | 75.3% (67.8–81.6) |
| Neutral | 16.9% | 6.8% |
| Uncomfortable | 21.1% (16.4–26.6) | 15.8% (10.7–22.5) |
| Harsh/condemning | 1.7% (0.6–4.2) | 2.1% (0.7–5.9) |
| Loving : harsh | 36.5 : 1 (95% CI 14.0–135.8) | 36.7 : 1 (12.2–180.5) |
| Loving : (uncomfortable + harsh) | 2.65 : 1 (1.93–3.69) | 4.23 : 1 (2.74–6.76) |

Among self-judgments, 43.6% were rated loving/gentle (17/39).

**Experiencer emotional tone** (305 reviews with tone specified): mixed 48.9%, shame/regret 23.6%, love 21.6%, neutral 5.9% — love and shame are about equally common (0.92 : 1).

**Christians** (religious background, n = 147 reviews): 52.6% of classifiable reviews had no external evaluator; 65.7% of rated evaluations were loving (1 harsh, 12 uncomfortable); love tone 25, shame/regret 22.

**Finding (statistically supported, magnitude corrected).** Condemnation is rare: harsh evaluation occurs in about 2% of rated reviews, and when the Being of Light itself evaluates, three-quarters of evaluations are loving. The 36.5:1 ratio is arithmetically correct but rests on four harsh cases; one evaluation in five is uncomfortable. The data support "evaluation occurs and is predominantly non-condemning", not "no external evaluation", and the experiencer's own feeling is mixed rather than predominantly loving.

### 3.8 Expectation versus Experience

Where stated, the experience was coded as inconsistent with doctrine for 33.3% of Christian Light-Being life-review experiencers (n = 78; a further 50% partially consistent), and as contradicting or surprising personal expectations for 43.5% (n = 85). Across all Light-Being encounters, 57.2% of those stating it report contradicted or surprised expectations — no different from other-being encounters (55.2%; Fisher OR 1.08, p = 0.59).

**Finding:** the consistency fields describe the experience as a whole and do not say that the departure concerned judgment, so "expected judgment, found love" is an **interpretation**. Expectation violation is common, but not specific to the Being of Light.

### 3.9 Transformative Effects

Before/after levels are compared only where both are stated, a subset biased toward people whose levels changed.

| Measure | Light Being | Other beings only |
|---|---|---|
| Death fear: n with both levels | 117 | 84 |
| Decreased / increased | 88.0% / 0.9% (1 case) | 88.1% / 3.6% |
| Mean (0 none – 4 severe) | 2.52 → 0.31 (Wilcoxon p < 10⁻¹⁷) | 2.51 → 0.26 |
| Spirituality: n | 305 | 175 |
| Increased / decreased | 89.2% / 1.0% | 85.7% / 1.1% |
| Mean change (0 none – 4 central) | +1.58 | +1.33 (Mann-Whitney p = 0.003) |
| Ending at "central" | 37.7% | 14.9% |
| Religiosity: increased / decreased | 26.0% / 23.9% (n = 439; p = 0.55) | — |

Among Light-Being experiencers stating a value shift, 67.2% describe it as major.

**Findings.** Death fear falls in nearly all who report both levels, and rises in 0.9% (the previous "0.0%" came from a scale that dropped the "significant" and "severe" levels). The fear reduction does **not** differ from other-being encounters (p = 0.65). The spirituality increase is **larger** after Light-Being encounters (+1.58 vs +1.33 levels; p = 0.003, robust to narrative length), and far more end at the top level. Institutional religiosity does not change on average.

### 3.10 Denominations

Among Christians (belief at the time of the NDE) with denomination stated, any identification of Jesus: Catholic 21.7% (n = 120), Evangelical/Baptist 20.8% (n = 24), Mainline Protestant 26.8% (n = 41), Mormon/LDS 46.2% (n = 13). Catholic vs Evangelical: Fisher p = 1.00. With 24 Evangelicals, only very large differences are detectable; similar rates are not evidence of equivalence.

### 3.11 Prediction of the Name from Religion

The earlier random forest (religion, gender, age with missing ages set to 30) was trained on the 183 cases with a reported age and tested on 37; its below-baseline accuracy (37.8% vs 45.9%) reflects overfitting. A religion-only logistic regression on all 590 cases with known background, 5-fold cross-validated, matched the no-information baseline on accuracy (46.3% vs 46.4%) and slightly improved log-loss (1.238 vs 1.246); for unknown-vs-named the AUC was 0.53 (0.60 using belief at the time of the NDE, n = 719).

**Finding:** religion carries modest information about the label — consistent with the weak χ² association — but does not determine it.

---

## 4. Discussion

### 4.1 Summary of Corrected Findings

1. About half of Light-Being encounters are identified only as an unknown presence, in every religious group.
2. Religious background shapes the name, but weakly (V ≈ 0.11–0.24).
3. The functional profile (guidance, teaching, telepathy, belonging, mission) does not differ between "Jesus" and "unknown presence" encounters among Christians; the mode (visual figure vs unity) does.
4. Harsh condemnation is rare (~2% of rated evaluations); evaluation is predominantly loving but often uncomfortable, and experiencers' own feelings are mixed.
5. Teaching and telepathic communication are more frequent in Light-Being encounters than with other beings, robust to narrative length.
6. Death-fear reduction is common but not specific to the Being of Light; the spirituality increase is larger after Light-Being encounters.

### 4.2 Assessment against the Framework

| Prediction | Result | Verdict |
|---|---|---|
| Identification varies with culture | V ≈ 0.11–0.24 | **Hit** (weak effect) |
| A constant core beneath variable names | Functional properties equal; mode differs | **Partial hit** |
| Non-condemning evaluation | Harsh ≈ 2%; uncomfortable ≈ 21% | **Hit** for non-condemnation; "unconditional love" overstated |
| Singular Being across traditions | Not measurable; 2/8 Hindu/Buddhist cases name several figures | **Underdetermined** |
| Distinct teaching function of the Being | Teaching 2×, robust to length | **Hit** |
| Transformation specific to the Being | Fear: no; spirituality magnitude: yes | **Mixed** |

### 4.3 The Two-Tier Model, Revisited

"Constant state, variable form" receives partial support. The *functions* experiencers attribute to the Being are the same whatever they call it, and cultural background shifts the name only weakly. But the name is not a free-floating label: it tracks how the encounter is perceived — a luminous personal figure versus a formless presence with a sense of unity. Whether that perceptual mode belongs to the variable "form" or to the constant "state" must be specified in advance for the model to be tested rather than accommodated. If mode is part of form, the data fit the model well; if the model predicts identical phenomenology under any label, the unity difference is a miss.

### 4.4 Limitations

All variables are LLM extractions from self-selected online narratives; no human validation has been performed. Many fields are "not mentioned" for most records, and the Light-Being subset is defined from identifications rather than from a luminous-being field. Religious background is known for only 24% of records, and those accounts are much longer, so religion-based comparisons apply to a selected subgroup. Before/after measures are retrospective and selected toward change. The sample is predominantly Western; Hindu, Buddhist and Muslim subgroups are very small. Narrative length is an imperfect proxy for reporting detail; adjusted estimates reduce but cannot eliminate this confound.

### 4.5 Future Directions

A pre-registered definition of which phenomenological properties count as "state" and which as "form"; human validation of a random subsample of extractions; schema fields that record the *number* of beings of light and attribute communication and guidance to specific beings; and non-Western archives with adequate Hindu, Buddhist and Muslim samples.

---

## 5. Conclusion

In 6,751 near-death experiences, about half of encounters with a divine figure or presence are identified only as an "unknown presence", and religious background shapes the name used only weakly. Among Christians, encounters named "Jesus" and encounters named "unknown presence" share the same functional profile — guidance, teaching, telepathy, belonging, commissioning — but differ in perceptual mode. Condemnation is rare and evaluation predominantly gentle, though not uniformly loving. These results are consistent with a constant reality perceived through variable forms, with the important qualification that the form appears to include how the encounter is experienced, not only what it is called. Several earlier confirmations — the χ² of 365, "all differences below 10%", "0.0% increased fear", the singularity of the Being for polytheists, and below-baseline machine-learning accuracy — were artifacts and have been withdrawn.

---

## References

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value |
|------|-----------|----|---------|
| Religion (6 groups) × Light-Being presence | χ² = 35.25, V = 0.15 | 5 | < 0.0001 |
| Gender × presence | χ² = 0.07 | 1 | 0.79 |
| Age group × presence | χ² = 4.25 | 3 | 0.24 |
| Light Being vs other: significant guidance | χ² = 25.24; adj. OR 1.34 | 1 | < 0.0001 |
| Light Being vs other: teaching | χ² = 98.0; adj. OR 1.96 | 1 | < 10⁻²² |
| Light Being vs other: telepathy | χ² = 75.6; adj. OR 1.53 | 1 | < 10⁻¹⁷ |
| Religion × identification, full table (invalid: 69% cells E < 5) | χ² = 365.14 | 32 | permutation p = 0.0005 |
| Religion × identification, collapsed | χ² = 15.04, V = 0.11 | 6 | 0.020 |
| Belief at NDE × unknown presence only | χ² = 38.40, V = 0.24 | 3 | < 0.0001 |
| Jesus-only vs unknown-only: unity | Fisher, Holm-corrected | — | 0.016 |
| Death fear before vs after (Light Being) | Wilcoxon | — | < 10⁻¹⁷ |
| Spirituality change, Light Being vs other only | Mann-Whitney | — | 0.003 |
| Religion → name, cross-validated AUC | 0.53 (background), 0.60 (belief) | — | — |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,751 |
| Light-Being encounters | 1,881 (27.9%) |
| … coded as visual being of light | 31.8% |
| Unknown presence only | 50.6% |
| External evaluator, classifiable life reviews | 55.9% |
| Harsh evaluation, rated life reviews | 1.7% |
| Loving : harsh | 36.5 : 1 (95% CI 14–136) |
| Loving : critical (uncomfortable + harsh) | 2.65 : 1 |
| Teaching, Light Being vs other | 25.3% vs 12.6% |
| Death fear decreased / increased (both stated) | 88.0% / 0.9% |
| Spirituality increased (both stated) | 89.2% |

## Appendix C: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebooks**: [01_being_of_light_analysis.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb), [04_conceptual_framework_theory.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
