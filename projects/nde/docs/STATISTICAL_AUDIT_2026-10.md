# Statistical Audit of the NDE Notebooks and Reports (October 2026)

**Date:** 2026-10-05 (follow-up analyses added 2026-10-06, §9)
**Scope:** `projects/nde/notebooks/01–06*.ipynb` (and the follow-up notebooks 07–08, §9); the five reports in `projects/nde/reports/` (Markdown), their LaTeX sources in `reports/latex/`, and the PDFs.
**Supersedes:** `NOTEBOOK_AUDIT_REPORT.md` (January 2026). That audit was run on the extraction schema before the 2026-01-06 schema change, and its figures do not reproduce on the current data. For example, "84.8% no external condemnation" corresponds to nothing in the current schema. On current data, 36.6% of classifiable life reviews have an external evaluator, and harsh evaluation occurs in 1.4% of rated reviews.

---

## 1. Summary

Every notebook was re-derived from the structured JSON through a single, schema-checked loader. All six now execute top-to-bottom without errors. Each report was rewritten from its notebook's outputs.

The main problems found were:

1. **Silent schema mismatches.** Comparisons against enum values that do not exist (`'yes'` instead of `'yes_explicit'`, upper-case values, legacy v1 field names, wrong field paths) returned 0% or empty results. Several of these feed headline claims: "0.0% increased death fear", "experiential properties all differ by < 10%", "belonging shows no association", "0 death memories".
2. **Wrong denominators.** Examples: shares of mentions reported as shares of experiencers; "not mentioned" counted as "no"; life-review percentages computed over all 6,753 records.
3. **Invalid or circular tests.** These include a χ² test where 69% of cells had expected counts below 5, goodness-of-fit tests on overlapping counts, and tests of a group against the variables that define it. A positive predictive value was also reported as "accuracy", and a 2-factor solution was imposed rather than estimated.
4. **No control for narrative length.** Longer accounts mention more of every feature. Length explains 41% of the perception score, and it inflates every co-occurrence comparison.
5. **Hard-coded or unanalysed claims.** Notebook 04's summary printed percentages that were computed nowhere. The old Sequential Structure LaTeX/PDF reported sequence statistics that no notebook computed ("tunnel preceded light in 73.2%", "life reviews after beings 68.4%", "boundary preceded return 89.3%", "r = 0.34"). The old Mission LaTeX/PDF described a "linear discriminant analysis" that was never run. The East-West report stated an inter-rater reliability of κ = 0.84, but no reliability study existed anywhere in the repository. One has since been run (§9.2).

Several framework predictions hold after correction, some with different numbers. Others are withdrawn. Section 6 gives the scorecard.

---

## 2. Audit Method

| Step | What was done |
|---|---|
| Verified loader | `scripts/nde_dataset.py`. Gives unambiguous column names (colliding leaf names are prefixed with their parent). `check_values()` raises on any value not in the Pydantic schema. `isin`/`has` handle list fields. Dataset is taken from the `dataset` field, not from the file name. Provides Wilson CIs, Cramér's V, expected-count reports, and length-adjusted odds ratios. Tested in `tests/test_nde_dataset.py`. |
| Deduplication | Two narratives appear twice with identical content (`content_checksum`). Each is counted once: **N = 6,751** (NDERF 5,659; IANDS 1,092). |
| Dataset labels | 4 IANDS records were labelled NDERF because the file-name test `'nderf' in name` matched "wo**nderf**ul". |
| Denominators | Each percentage uses the cases where the question can be answered. The denominator is stated with the figure, and a 95% Wilson CI is given. |
| Tests | Expected-count checks, then permutation or collapsed tables where needed. McNemar for paired features; Fisher exact with Holm correction for multiple comparisons. Wilcoxon on the correct 5-level ordinal scales. TOST for claims of equivalence. Tetrachoric correlations and parallel analysis for factor retention. Cross-validated log-loss and AUC for classifiers. |
| Narrative length | Word count of the source narrative. Associations are reported crude and adjusted for log word count (logistic or OLS). |
| Circularity | Tests of a group against its defining variables are labelled as circular and not counted as evidence. |
| Report cross-check | Every number in the five reports was compared programmatically with the notebooks' printed outputs. The only numbers left unmatched are quoted earlier values, model and version names, years, and simple arithmetic derivations such as n = 6,751 − 695. |
| LaTeX/PDF | `.tex` files are now generated from the Markdown by `scripts/md_to_latex.py`. PDFs are compiled with tectonic, so the Markdown is the single source. |

---

## 3. Notebook Corrections

Each notebook has an "Audit corrections (2026-10-05)" cell with the full list. The main items:

### 01 — Being of Light

| Previous claim | Corrected | Verdict |
|---|---|---|
| Religion × identification χ² = 365.14 | 69% of cells have expected count < 5. The Buddha column (2 Buddhists) contributes 82% of the statistic. Collapsed table: χ²(6) = 15.04, p = 0.020, V = 0.113. Belief at time of NDE: χ²(3) = 38.40, V = 0.235 | Association weak; statistic withdrawn |
| "Experiential properties identical — all differences < 10%" | Christian background, Jesus-only (102) vs unknown-only (175). Guidance, teaching, telepathy, belonging and mission do not differ. Being-of-light coding differs by +45.0 pp (Holm p < 0.001) and unity by −19.6 pp (Holm p = 0.016) | Function constant; mode differs |
| ML classifier "below baseline" (37.8% vs 45.9%) | The previous model was a random forest trained on n = 183 with a test set of 37, and ages were imputed. A religion-only model with cross-validation gives accuracy 0.463 vs prior 0.464, log-loss 1.238 vs 1.246, and AUC 0.527 (0.602 using belief at the time of the NDE) | Religion predicts the name barely above chance |
| 54.7% "no external judgment" | "Not mentioned" had been counted as "no judgment". Of classifiable reviews, 55.9% (205/367) involve an external evaluator | Reversed |
| Loving 32.2%, harsh 0.9%, ratio 36.5:1 | Of rated reviews (n = 242): loving 60.3%, neutral 16.9%, uncomfortable 21.1%, harsh 1.7%. Loving:harsh 36.5:1 (95% CI 14.0–135.8); loving:critical 2.65:1 | Ratio holds; context added |
| Telepathic 34.8% | That figure was a share of mentions. Per experiencer: 48.2% vs 34.2% for other-being encounters (adjusted OR 1.53) | Corrected |
| Guidance 81.7%, "nearly 2× other beings" | Guidance 81.7% vs 74.9% (1.09×; χ² = 25.24; adjusted OR 1.34). Teaching is the 2× difference: 25.3% vs 12.6% (χ² = 98.0; adjusted OR 1.96) | Corrected |
| 0.0% increased death fear | The scale used values that do not exist. Correct figures: 0.9% increased, 88.0% decreased (n = 117). Other-being encounters: 88.1% decreased (p = 0.65) | Corrected; not specific to the Being |
| 84.2% increased spirituality | 89.2% (n = 305). Larger rise than after other-being encounters (mean +1.58 vs +1.33, p = 0.003) | Corrected; effect is larger |
| "Singular Being even for polytheists" | No schema field measures this. Only 8 Hindu/Buddhist cases exist, and 2 of them name several figures | Withdrawn (not measurable) |
| "Corrects expectations" | Expectation contradicted 57.2% vs 55.2% for other beings (OR 1.08, p = 0.59) | Not specific to the Being |

### 02 — Normative Path

| Previous claim | Corrected | Verdict |
|---|---|---|
| Agency × willingness χ² = 4,824.8 | That statistic included co-missing data. With both stated: χ²(9) = 1,389.0, V = 0.37. The notebook had also printed "independent" when p < 0.05 | Corrected |
| Mission commissioned 0%; covenant 0.7%; empathetic review 0% | The comparison used `'yes'`, which is not a schema value. Correct figures: 21.9%, 1.3%, and perspective of others 18.0% of life reviews | Corrected |
| "Death fear decreases significantly" (hard-coded) | Computed: 84.7% decreased, 4.0% increased (n = 327) | Now computed |
| "5/5 markers support" | The support thresholds could not fail (e.g. past-life memory < 10% ⇒ ✓) | Replaced by an explicit statement of what each marker can test |
| "Sequential ordering generally maintained" | Never analysed. Canonical order: strict 3/6,249 (0.05%), mostly 37.7%, partial 54.3%, radical 7.9% | **Miss** for a fixed sequence |
| — | Not self-chosen return 70.1% of stated; reluctant 49.4%; deceased relatives 17.9%; identity clear 97.0%; past-life memory 4.4%; intermission 1.0%; hellish realm 2.8% | Descriptive |

### 03 — Volunteer Soul

| Previous claim | Corrected | Verdict |
|---|---|---|
| "94.2% discriminant accuracy" | This is a positive predictive value. Sensitivity 39.7%, specificity 99.3%, accuracy 86.2% vs 78.1% baseline, κ = 0.49 | Relabelled |
| χ² = 3,018 (volunteer × commissioned), 599.2 (× volunteer language) | Both test variables that define the group | Circular; not evidence |
| Belonging χ² = 0.0; "life transformation no association" | Wrong field path, and the second field does not exist. Belonging: χ² = 252.1, V = 0.19 | Reversed |
| "Has death memory: 0" | 36 cases (19 violent) | Corrected |
| Volunteer detection rule | The Methods rule would flag 898 cases; the rule actually used flags 695 | Documented |
| — | Independent features, length-adjusted ORs 2.0–3.3; mission → Being of Light OR 4.38 (adjusted 3.26) | Supported |

### 04 — Conceptual Framework

Many cells used legacy v1 field names, which evaluate to 0%, while "✓ VALIDATED" was printed regardless. The final summary printed ten hard-coded percentages that were computed nowhere. Specific errors:
- `atheist` and `agnostic` substring matches counted the same 429 records twice.
- The "Spirituality ↑ while Religiosity ↓" pattern was printed without a test.
- The Jesus-vs-Unknown comparison used broken fields and diluted denominators.
- The ML model had target leakage.

All were replaced with computed analyses:
- Religiosity shows no net change in 1,168 pairs (up 20.2%, down 19.9%, p = 0.58). In the four-level subset it rises (30.2% vs 18.6%).
- In life reviews, experiencer tone is love 163 vs shame 169.

### 05 — Cultural Paradigm (East-West)

| Previous claim | Corrected | Verdict |
|---|---|---|
| κ = 0.84 inter-rater reliability (report) | No such study existed. A blind second coding has since been run (§9.2): κ = 0.85–0.87 for light and relatives, 0.34 for boundary type | Removed; replaced by measured values |
| Deceased (17.9%) ≈ 2× religious figures (9.9%) | God and Jesus had been omitted. Correct range 13.8–19.9% depending on definition (McNemar: p < 10⁻¹⁰, p = 0.26, p = 0.002) | Definition-dependent; "inversion" withdrawn |
| Brilliant light = "impersonal", 3.8:1 | 57.0% of these accounts identify beings and 56.9% report communication | Relabelling withdrawn |
| Nature vs urban χ² = 74.7 | Goodness-of-fit test on overlapping counts. McNemar χ² = 107.4, p < 10⁻²⁴ | Finding holds; test corrected |
| Tunnel and boundary "independent, r = −0.02" | OR 2.43, φ = 0.19; adjusted OR 2.24 | Reversed |
| Life review × BoL χ² = 53.2 "p < 10⁻³⁰" | χ² (Yates) = 129.8 | Corrected |
| Boundary type × agency χ² = 3,724.7 | That statistic included "none"/"not mentioned". With both stated: χ²(6) = 683.8, V = 0.35. Partly definitional | Corrected; caveat |
| Cells 22–46 (legacy-schema re-run) | Every metric 0.0%; two ZeroDivisionErrors | Removed |
| — | BoL 11.8% of all (20.7% with any light); life review 17.5%; tunnel 23.7%; mission → BoL adjusted OR 3.26; boundary content ORs adjusted 1.28–3.07 | Computed |

### 06 — Perception (Discrete Degrees)

| Previous claim | Corrected | Verdict |
|---|---|---|
| Two factors = "internal differentiation" | The solution was imposed. On raw data, Kaiser, parallel analysis and tetrachoric eigenvalues (4.11, 0.89) all give 1 factor. After length control there is weak sub-structure (eigenvalues 1.07 and 1.04 vs thresholds 1.06 and 1.02), and it is not aligned with the degrees | **Miss** (H3) |
| Right skew "exactly what the theory predicts" | Independent markers would also be right-skewed (skew 0.33 vs 0.82 observed). The excess of zeros (27.4% vs 8.2%) is the signature of a common factor | Not diagnostic |
| Prevalence hierarchy (implicit) | ρ = −0.47, p = 0.28. The most and least prevalent markers are both "spiritual" | **Miss** (H1) |
| Construct validity KMO 0.817 | Holds raw (KR-20 0.738). Controlling for length, mean r falls from 0.29 to 0.15. Six markers still cohere (15/15 significant); telepathy does not | Supported for six markers |
| BoL d = 0.589, "all seven markers elevated" | Adjusted for length: +0.39 markers (95% CI 0.28–0.49). Only comparative reality (OR 1.87) and telepathy (OR 3.90) remain elevated. Memory (0.74) and thought speed (0.78) reverse | Partial |
| Cultural invariance from ANOVA p = 0.92 | TOST: Christian − atheist/agnostic = −0.005 (95% CI −0.38 to +0.37), equivalent within ±0.5 markers (p = 0.005); length-adjusted +0.02 | **Hit** (Christian vs non-religious) |
| N 6,135 / 618; notebook "05"; "principal axis" | N 5,659 / 1,092; notebook 06; extraction method is minres | Corrected |

---

## 4. Report Corrections

| Report | Main changes |
|---|---|
| Being of Light | All items in §3/01. Light-Being subset now defined explicitly (n = 1,881; only 31.8% coded `being_of_light`). Length-adjusted ORs and CIs added. |
| Sequential Structure (retitled *Evaluating the Normative Path Model*) | Sequence analysed for the first time. Life-review ratios computed within life reviews: 36.2:1 loving:harsh, 1.72:1 loving:critical. Denominators corrected. Markers classified by what they can test. |
| Mission-Based Returns | Confusion matrix replaces "accuracy". Circular tests labelled. Belonging association restored. Detection rule documented. Length-adjusted ORs. |
| East-West Dichotomy | κ claim removed. "Western" scoped to these archives (country known for 12.3%; 27.3% of those non-Western). Brilliant-light relabelling withdrawn. Deceased vs religious comparison is definition-dependent. McNemar test. Tunnel–boundary association. Boundary–agency caveat. Japanese profile marked as untested. |
| Direct Perception | All items in §3/06, plus the length-controlled construct analysis. Palaeolithic paragraph marked as speculative. Strawman alternatives removed. |

The LaTeX files had drifted from the Markdown, and some contained claims that appear in neither the Markdown nor any notebook (§1). All four are regenerated from the corrected Markdown, and the four PDFs are recompiled. The Direct Perception report never had a LaTeX/PDF version; it can be generated with `python scripts/md_to_latex.py "<report name>"`.

---

## 5. Remaining Limitations (apply to every result)

1. **Coding reliability.** All variables are model-coded features of one retrospective narrative. A human coder would not provide ground truth, but reproducibility can be measured, and it was (§9.2). Against a blind second coder, the median κ is 0.83 across 15 fields, and GPT-5.2 test–retest κ is 0.88. Four results depend on codebook conventions that the schema leaves open: "unknown presence" vs "other" (κ 0.44), "implied" mission (prevalence 21.9% → 14.8%), boundary type (κ 0.34), and the harsh/uncomfortable line (loving:harsh 36.2:1 → 6.4:1).
2. **"Not mentioned" is not "absent".** Prevalence figures computed over all records are lower bounds of what was experienced; figures over stated cases may be biased toward salient experiences.
3. **Self-selected archives.** These are not population prevalence estimates.
4. **Narrative length.** Adjusting for word count is a partial control, because length may itself reflect experiential richness.
5. **Sparse subgroups.** Non-Christian religious backgrounds have n = 14–43 in the identified subset; country is known for 12.3%.

---

## 6. Framework Scorecard (NDE domain, after correction)

Labels follow `CLAUDE.md`. **Statistically supported** means the pattern is in the data. **Interpretation** means a correspondential reading that is consistent with the data. **Speculative** means it depends on the framework.

| Prediction | Corrected evidence | Verdict |
|---|---|---|
| Constant state, variable form (Being of Light) | The name varies weakly with background (V = 0.11–0.24), and most encounters stay unnamed (50.6% unknown-only). Functional properties do not differ by name. The perception profile is equivalent for Christian and non-religious experiencers (TOST p = 0.005) | **Hit** (statistically supported). The statistics previously cited for it (χ² = 365.14, "< 10%", "below-baseline ML") are withdrawn |
| Functional differentiation of beings | Light-Being encounters: teaching 2.0× (adjusted OR 1.96), telepathy adjusted OR 1.53, guidance 1.09× (adjusted OR 1.34). Exclusive being types (notebook 07): 10/11 functions differ; divine vs relatives teaching OR 6.27; guidance overall OR 0.81 | **Hit** for differentiation and teaching (statistically supported). "More guidance overall" is a miss |
| Relatives as gatekeepers | Sent back in 54.6% of relatives-only vs 51.7% of divine-only accounts (adjusted OR 1.11, p = 0.42); 47–55% in every group | **Miss**: sending back is shared by all being types |
| Non-condemning review | Harsh 1.7% of rated Light-Being reviews and 1.4% of all rated reviews (loving:harsh about 36:1). A blind second coder gives 8.7% harsh (CI 1.3–16.8), loving:harsh 6.4:1. Uncomfortable evaluation 21–28%; loving:critical 1.7–2.7:1, stable across coders | **Hit** for "rarely condemning, predominantly loving". The 36:1 magnitude is coder-dependent. Not supported as "uniformly loving" |
| Mission returns as a category | PPV 94.2%, κ = 0.49. Independent features associate with adjusted ORs of 2.0–3.3. Mission → BoL adjusted OR 3.26. Commissioning prevalence calibrated to the second coder is 14.8% (vs 21.9%); the return-reason link holds under both coders | **Supported** as a coherent reported category. "94.2% accuracy" withdrawn |
| Personhood of the Being | Teaching, telepathy and commissioning associations hold. "Presence" is the majority label. Singularity is not measurable. "Corrective" is not specific to the Being | Associations supported; personhood itself is **interpretation** |
| Transformation | Spirituality ↑ 89.2% (larger than after other beings); death fear ↑ 0.9%. Religiosity shows no net change | **Supported** (descriptive) |
| Normative path: characteristic sequence | Strict canonical order in 0.05% of accounts | **Miss** |
| Normative path: continuation markers | Rare reincarnation content; preserved identity; encounters with the dead | Consistent, but mostly non-discriminating |
| East-West: Western profile is a scholarly construction | Claimed rates not observed in these archives | **Supported** for these archives. The Japanese side is untested |
| Purposive economy | Personal Light co-occurs with mission and life review (adjusted ORs 3.26, 1.89) | Association supported; direction is **interpretation** |
| Discrete degrees in perception | One dominant factor; no prevalence hierarchy | **Miss** (H1, H3) |
| Being of Light → "celestial" perception | Only the two celestial markers survive length adjustment | **Partial hit** |

---

## 7. Claims Elsewhere That the Corrected Analysis Contradicts

These documents were **not edited** in the first pass of this audit because they are outside the notebooks and reports. They cite figures that no longer hold. (`CLAUDE.md` was rewritten on 2026-10-06 with the owner's permission to match §6 and §9.)

**`CLAUDE.md`** ("Empirical Support" and "Summary" sections):

| CLAUDE.md states | Corrected |
|---|---|
| χ² = 365.14 (constant state, variable form) | Sparse-cell artifact. Valid: χ²(6) = 15.04, p = 0.020, V = 0.113; belief at NDE χ²(3) = 38.40, V = 0.235 |
| "61.8% of Christians … 'unknown presence' (only 11.2% say 'Jesus')" | Those were shares of *all* Light-Being encounters in an archived old-schema notebook (`archive/conceptual_framework_deep_dive.ipynb`). Christian background, current data: unknown presence 44.2%, Jesus 25.1% (first-listed label); unknown-only 42.6% |
| Experiential properties "all differences below 10%" | Function does not differ; visual-being coding (+45 pp) and unity (−20 pp) do |
| ML classifier below baseline (37.8% vs 45.9%) | An artifact of overfitting. Religion predicts the name barely above chance (AUC 0.53) |
| Entity function χ² = 41.13, p = 0.008; 70–73% guidance; 29.5% "told to return" | Not produced by any notebook. Tested in notebook 07: beings are differentiated (AUC 0.673) and divine figures teach far more (OR 6.27), but they do not give more guidance (73.2% vs 75.9%), and relatives are not specific gatekeepers (OR 1.11, p = 0.42) |
| Mission "94.2% accuracy"; χ² = 3018.1 | PPV 94.2% (accuracy 86.2% vs 78.1% baseline, κ = 0.49); χ² circular |
| Loving 32.2% / harsh 0.9%, 36.5:1 | Of rated reviews: loving 60.3%, harsh 1.7%. 36.5:1 is arithmetically correct (CI 14.0–135.8) but coder-dependent: a blind second coder gives 6.4:1 over all rated reviews. Loving:critical 2.65:1 (Light-Being reviews), 1.7–1.8:1 (all), stable |
| Singular Being "even polytheists" | Not measurable (8 cases; 2 name several figures) |
| "81.7% guidance rate, nearly 2× other beings" | Guidance 1.09×; teaching is 2× |
| "475 vs 239 teaching instances (χ² = 25.24)" | χ² = 25.24 is the guidance test; teaching 25.3% vs 12.6%, χ² = 98.0 |
| Telepathic 34.8% | Per experiencer 48.2% (vs 34.2%) |
| "Corrective — delivers what the experiencer did NOT expect" | Not specific to the Being (57.2% vs 55.2%, p = 0.59) |
| 51.9% "unknown presence" | Holds as first-listed label; 50.6% unknown-only. But the label is the coder's, not the experiencer's, and its boundary with "other" is unreliable (κ 0.44), so it cannot show that experiencers prefer a "personal word" |
| Mission-returners 4.4× odds (p < 10⁻⁴⁶) | Holds (OR 4.38; length-adjusted 3.26) |
| 84.2% increased spirituality; 0.0% increased death fear | 89.2%; 0.9% |
| NDE sample 6,753 | 6,751 unique narratives |

**`docs/external/The Epistemic Architecture of Post-Materialist Inquiry_ ….md`** repeats χ² = 365.14, "< 10% variation" and the ML result.

**`projects/nde/docs/notebook_reanalysis_plan.md`** cites "61.8% transcend categories".

---

## 8. Reproducing the Analysis

```bash
pip install -r requirements.txt          # scikit-learn < 1.8 (factor_analyzer compatibility)
cd projects/nde/notebooks
jupyter nbconvert --to notebook --execute --inplace 0*.ipynb   # includes 07 and 08
cd ..
python -m pytest tests/test_nde_dataset.py
python scripts/md_to_latex.py            # regenerate reports/latex/*.tex from the Markdown
cd reports/latex && tectonic "<report>.tex"   # or pdflatex
```

**Known test failure.** `tests/test_questionnaire_models.py::test_model_instantiation_succeeds` fails both before and after this audit. Its fixture payload predates the current schema, and this audit did not change it.

---

## 9. Follow-up Analyses (2026-10-06)

Two items the first pass left open were analysed in new notebooks, each with a report.

### 9.1 Entity Function Differentiation (notebook 07)

The `CLAUDE.md` figures for this prediction (χ² = 41.13; 70–73% guidance; 29.5% "told to return") were not produced by any notebook. Guidance and return are recorded per account, so functions were attributed to five exclusive being types (accounts with one kind of being, n = 2,634).

- Ten of 11 functions differ across types after Holm correction (V 0.07–0.18). The function profile separates divine from relative encounters beyond narrative length (cross-validated AUC 0.673 vs 0.555).
- Divine figures teach far more than relatives (23.0% vs 4.5%; length-adjusted OR 6.27, 3.94–9.98). They also communicate telepathically more (OR 1.83) and commission missions more (OR 1.62). They do **not** give more guidance overall (OR 0.81).
- Relatives give directional guidance (67.3%) and comfort (43.8%) and rarely teach (5.9%).
- Sending the experiencer back is shared by all being types (47–55%). It is not specific to relatives (OR 1.11 vs divine, p = 0.42).
- The unknown presence is functionally closer to divine figures than to relatives, but so are angels and other beings.

Report: `reports/Functional Differentiation of Beings in NDE - Testing Role Specialisation.md`.

### 9.2 Extraction Reliability (notebook 08)

A blind second coder (Claude) recoded 100 random accounts on 15 fields and 44 life reviews (40 random plus all 6 GPT-harsh). It saw the same text GPT-5.2 received, with the schema's field descriptions as the codebook. Codes and conventions are in `validation/`.

- Median κ across binary fields is 0.83. Nine fields are above 0.80: tunnel, life review, telepathy, guidance, being of light, deceased relatives, any light, return by a being, God or Jesus. Five fields are 0.70–0.77: boundary, earthly-mission reason, more real, mission, teaching.
- **Convention-dependent results:**
  - "unknown presence" (κ 0.44): its boundary with "other" is undefined;
  - mission commissioning: the "implied" codes are liberal, and the calibrated prevalence is 14.8% (12.2–18.4) vs 21.9%;
  - boundary type (κ 0.34): there is no precedence rule when a barrier and a spoken limit co-occur;
  - judgment intensity: weighted κ 0.74, but the harsh boundary is unstable. Harsh is 8.7% (1.3–16.8) vs 1.4% and loving:harsh is 6.4:1 vs 36.2:1, while loving:critical is stable (1.77 vs 1.72).
- **Near-duplicates:** 125 pairs and 121 redundant records (1.8%; lower bound), including the same NDERF account stored under two file names. Removing them moves headline rates by less than 0.5 percentage points.
- **GPT-5.2 test–retest** on duplicate pairs: median κ 0.88 on near-identical text and 0.75 on all pairs. It is least stable on "more real" and judgment intensity.

The first-pass limitation "no human validation" is therefore replaced by measured reliability in every report. Report: `reports/Extraction Reliability - Independent Second Coding of NDE Narratives.md`.
