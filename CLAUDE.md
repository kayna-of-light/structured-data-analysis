# Structured Data Analysis Framework — Instructions for AI Agents

## 1. Purpose and Stance

This repository converts scraped narrative datasets into structured data with LLM extraction and analyses them statistically. Its research programme uses **Swedenborg's correspondential framework** as the primary hypothesis generator and interpretive lens.

The framework is used **the way physics uses a theory**: not because it is believed in advance, but because it makes specific predictions that can be checked against data. In the domains tested here it organises several observed patterns that competing lenses leave fragmented (§6). The working question is not "Is Swedenborg right?" but "Which of the framework's predictions hold, how strongly, and where does it fail?"

**In practice:**
- When the framework predicts a pattern and the data confirm it, that is a **hit**. Report it as such.
- When the data contradict a prediction, that is a **miss**. Report it as plainly as a hit.
- When the data are underdetermined, or the variable cannot be measured, say so. Do not force a fit in either direction.
- Do NOT hedge confirmed predictions to appear "balanced".
- Do NOT inflate weak findings to support the framework.

The neutral position is **accuracy**, not equidistance between confirmation and skepticism.

---

## 2. Research Integrity Principles

1. **Report what the data show**: patterns, effect sizes with confidence intervals, test statistics, df, p-values.
2. **Report what the data do not show**: what remains underdetermined, unmeasurable or convention-dependent.
3. **Label every claim** at one of three levels:
   - **Statistically supported**: an effect in the data, with effect size, CI and test details, robust to the checks in §4.
   - **Interpretation**: a framework-consistent reading of a supported pattern; the data do not prove it.
   - **Speculative**: ontological claims (e.g. spiritual causation) that depend on accepting the framework.
4. **Take the framework seriously enough to test it properly**, neither dismissively nor reverently.
5. **Do not adjust conclusions to what you think the user wants to hear.** The owner of this repository has asked for precision above all else.
6. **Every number you write must trace to an executed notebook cell** in this repository, or to a cited publication if it is a literature figure. Numbers remembered from earlier documents are not evidence.

---

## 3. Methodology: The Framework as Testable Hypothesis

- **Origin is methodologically irrelevant.** Do not present Swedenborg as unquestionable revelation, and do not dismiss the framework because of its visionary origin.
- **Testability is the criterion.** Prefer falsifiable predictions, out-of-sample checks and explicit failure modes.
- **Pre-specify.** Before running a test, write the prediction and what would count as a miss in the notebook's first markdown cell. A criterion that cannot fail is not a test. (The old "5/5 markers support" check in notebook 02 used thresholds such as "past-life memory < 10% ⇒ ✓", which pass whatever the data say.)
- **Find the prediction in the text.** Before a result is scored against the framework, locate the prediction in Swedenborg's writings, with a section reference. A result that contradicts a claim the framework does not make is reported as **not observed**, never as a miss. Three earlier "misses" were of this kind: a per-degree layering of perception (the doctrine puts every degree in every thought, *DLW* §§222–229, 256), an episode-level stage order (his sequence is of three states in the world of spirits that some skip, *HH* §491), and relatives as gatekeepers (relatives receive the newly arrived, *HH* §494). The converse also holds: a pattern that fits the text only after the fact is consistency, not confirmation, until a registered test has run.
- **Specify "state" and "form" in advance.** For "constant state, variable form", decide before looking which properties are the constant state and which are the variable form. Otherwise every result can be accommodated.
- **Separate levels of claim:**
  - **Pattern fit** (empirical): associations and predictive performance.
  - **Interpretation** (framework-consistent): a correspondential reading consistent with the data.
  - **Ontology** (speculative): stays speculative unless independently supported.
- **Same-source caveat.** All NDE variables are coded from one retrospective narrative. Associations between them show that *reports* are coherent, not that the reported events occurred.

---

## 4. Analysis Integrity Rules (mandatory)

These rules come from the October 2026 audits (`projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`, `projects/mallworld/docs/STATISTICAL_AUDIT_2026-10.md`). Every rule corresponds to an error that produced a published figure later withdrawn.

1. **Load data only through the verified loaders.**
   - **NDE:** `projects/nde/scripts/nde_dataset.py` (`nd.load_frame()`). It flattens the schema, removes exact duplicates and attaches narrative length.
   - **MallWorld:** `projects/mallworld/scripts/mallworld_dataset.py` (`mw.load_posts()`, `mw.load_locations()`, `mw.load_entities()`, …). It defines the analysis populations and keys every table by dream. Its schema checks are `mw.isin`, `mw.has` and `mw.check_values`.
2. **Use schema-checked comparisons**: `nd.isin(df, column, values)` and `nd.has(...)`. Never compare against a literal the schema cannot produce. `'yes'` instead of `'yes_explicit'`, upper-case enums and legacy v1 field names silently returned 0% and produced claims such as "0.0% increased death fear".
3. **State the denominator for every percentage**: all records, accounts where the feature is mentioned, or accounts where it is stated. `not_mentioned` is not `no`.
4. **Control for narrative length.** Longer accounts mention more of everything. Length explains 41% of the perception score. Adjust co-occurrence comparisons for log word count with `nd.adjusted_odds_ratio(df, outcome, exposure)` and report crude and adjusted estimates.
5. **No circular tests.** Do not test a group against the variables that define it. The old χ² = 3,018 for "volunteer × commissioned" did exactly this. Mark associations that are built into category definitions.
6. **Check test assumptions.** For χ², report expected counts (`nd.expected_count_report`). If more than 20% of cells are below 5, collapse categories or use Fisher or permutation tests. The withdrawn χ² = 365.14 had 69% sparse cells, and 82% of the statistic came from two Buddhists.
7. **Correct for multiple comparisons** (Holm) within each family of tests.
8. **Name diagnostic statistics correctly.** Report PPV, sensitivity, specificity, κ and accuracy against a baseline. A PPV is not "accuracy".
9. **Validate predictive models properly.** Cross-validate, and report AUC or log-loss against a baseline. Never rely on a single small test split. (The withdrawn "below-baseline" result came from 37 test cases.)
10. **Estimate, do not impose, factor structure.** Use parallel analysis or Kaiser criteria, not a fixed `n_factors`.
11. **Absence of significance is not equivalence.** Claims of invariance need an equivalence test (TOST) with a stated margin.
12. **Treat ratios built on few events as fragile.** Give CIs and a coder-sensitivity check. The loving:harsh ratio rests on 6 harsh cases; it is 36.2:1 under the extraction and 6.4:1 under a second coder.
13. **Cite measurement reliability.** For each field a finding rests on, cite its inter-coder κ from the project's `08_extraction_reliability.ipynb` (§6.2 for NDE, §6.5 for MallWorld). Treat convention-dependent fields as such. After any schema change, re-run the second-coding procedure in the project's `validation/` folder on a fresh random sample.
14. **Check near-duplicates for small-count results.** About 1.8% of NDE records are redundant copies: cross-archive submissions, and NDERF accounts stored under two file names. They do not change headline rates, but check them when a result depends on a handful of cases.
15. **No hard-coded results.** Summary cells must compute what they print. Reports quote only numbers printed by executed notebooks.
16. **Generate report LaTeX from Markdown** with `projects/nde/scripts/md_to_latex.py` (add `--project mallworld` for MallWorld), then compile. Never edit `.tex` by hand; the old `.tex` files had drifted and contained claims found nowhere else.
17. **Join on the full key, and cluster on the dream.**
    - MallWorld `location_id` values (`loc_1`, …) repeat across dreams. Joining entities or interactions to locations on `location_id` alone turned 4,235 involvements into 7,158,025 rows. That join produced "entity autonomy" and "social interactions in malls, z = +22.8". Always join on `(post_id, location_id)`.
    - Locations, entities and transitions are nested in dreams (atmosphere ICC 0.31). Use `mw.clustered_logit` or dream-level bootstraps, never location-level χ².
18. **Define the population and say which one you use.** The MallWorld thesis ran on 2,678 posts that included 750 non-dream posts (questions, AI images, maps), while other reports used 1,926 dreams. Use the loader's `primary` population (1,918 dreams) unless a question requires another.
19. **Pre-register by commit.** A plan written after the results is not a pre-registration; the archived MallWorld "pre-registered" plan was dated after the reports it claimed to predict. Commit the predictions and the criteria for a miss before writing the analysis (as in `projects/mallworld/docs/PREREGISTRATION_2026-10.md`).
20. **Separate dream from dreamer.** Most MallWorld authors (78.7%) post once. A variance component "by dreamer" computed on locations is mostly a within-dream effect. Estimate author effects on dream-level scores of authors with at least two dreams, against a permutation null.

---

## 5. The Swedenborgian Framework

### 5.1 The Doctrine of Correspondences

Swedenborg (1688–1772) proposed that the natural world is a "theatre representative" of the spiritual world. The relation is **vertical causality**, not poetic metaphor: the natural is the ultimate effect of spiritual causes. Predictions are derived from texts written between 1749 and 1771, long before systematic data existed to test them. The risk is that the predictions are formulated *after* seeing data, which is why §3 requires pre-specification.

| Principle | Description |
|-----------|-------------|
| **Vertical Causality** | Spiritual realities flow (influx) into natural forms. The natural is the "effect" plane; the spiritual is the "cause" plane |
| **Constant State, Variable Form** | The underlying spiritual reality is constant. Perceptual forms vary with the receiver's mental repertoire |
| **Discrete Degrees** | Reality stratifies into celestial (love), spiritual (wisdom/truth) and natural (effects) levels. The levels are not separate layers met one at a time: in a "simultaneous arrangement" the highest is the centre and the lowest the circumference (*DLW* §§205–208), "every least bit of thought, even every least bit of a mental image" contains them all (§§222–229), and the earthly mind receives the higher levels as a continuum, "gradually", not "by distinct levels" (§256). Never assign an observable to a single degree |
| **Correspondence Consistency** | The same natural object consistently corresponds to the same spiritual reality across contexts |
| **Opposite Sense** | The same symbol can express good or evil depending on context (fire = divine love OR destructive passion) |
| **The Divine Human** | God is not an abstract force but a Person, the Divine Human. The human form is the form of love and wisdom; since God *is* love and wisdom, God is the Divine Human. Humans are human because they are made in this image, receiving life from the Divine Human, who is present in every person at every level of reality. **Empirical status:** NDE data are consistent with personal properties of the Being of Light: teaching, telepathic communication and commissioning are more frequent than with other beings (§6.1, row 5). Singularity is not measurable with the current schema, and personhood itself is interpretation |

**Correspondence vs allegory:**

| Feature | Allegory (Arbitrary) | Correspondence (Organic) |
|---------|---------------------|--------------------------|
| Origin | Invented by an author for rhetorical effect | Inherent in the object's function; discovered, not invented |
| Relationship | Mechanical substitution (Scales = Justice) | Causal participation: the symbol IS the reality in ultimate form |
| Meaning | Single, static, abstract concept | Multivalent, grounded in the object's nature |
| Validation | Requires a codebook | Validated by functional analogy |

**Example:** Light = Wisdom is not arbitrary allegory. Light enables the eye to distinguish forms, which is the function of the intellect. The correspondence is grounded in the physics of the object.

### 5.2 Not Jungian Psychology

This framework is **not** interchangeable with Jungian archetypal psychology, Freudian psychoanalysis or other depth psychology. Jung psychologised correspondential concepts, treating the spiritual realm as a projection of the psyche rather than an objective reality.

| Aspect | Swedenborg | Jung |
|--------|------------|------|
| **Ontology** | The spiritual realm is objectively real; correspondences describe actual influx | Archetypes are patterns in the "collective unconscious" |
| **Causation** | Top-down (spiritual causes natural) | Bottom-up (archetypes emerge from evolution/psyche) |
| **Vertical Structure** | Celestial / Spiritual / Natural (love / wisdom / effect) | Id / Ego / Superego (instinct / reality / morality) |
| **Entity Status** | Beings encountered are real, with differentiated functions | Figures are projections of internal complexes |
| **Validation** | Phenomenological consistency across experiencers | Therapeutic interpretation |

**What the data say about this choice (NDE, §6.1):**
- **Function tracks the identity of the being.** Divine or religious figures teach six times as often as deceased relatives (23.0% vs 4.5%; length-adjusted OR 6.27, 95% CI 3.94–9.98). Relatives orient and comfort. A model in which beings are interchangeable projections does not predict this. Archetypal theories that assign roles to archetypes can accommodate role differentiation after the fact, so this result favours the framework without refuting Jung outright.
- **Name varies weakly; function does not.** Religious background predicts the name given to the presence only weakly (Cramér's V 0.11–0.24; cross-validated AUC 0.53). Among Christians, encounters named "Jesus" and "unknown presence" do not differ in guidance, teaching, telepathy, belonging or mission. Perceptual *mode* does differ (visual figure +45.0 pp, unity −19.6 pp).
- **Expectations are often contradicted.** 57.2% of Light-Being experiencers who comment on it report contradicted or surprised expectations. This is not specific to the Being of Light (55.2% with other beings).
- **Content is consistent; order is not.** The same elements recur, but a strict canonical stage order occurs in only 0.05% of accounts. That order comes from the NDE literature, not from Swedenborg, so it is not a test of the framework (§6.1, row 7).

**Do NOT substitute Jungian or Freudian framing as the primary lens** when analysing data in this project. Note parallels with other frameworks where relevant, as secondary.

### 5.3 Comparison with Other Frameworks

No head-to-head model comparison has been run in this repository. The table records where each lens has difficulty *given current data*, and where that difficulty is only argued.

| Framework | Explains well | Where current data strain it | Basis |
|-----------|---------------|------------------------------|-------|
| **Materialist neuro-psychology** | Physiological triggers, brain correlates | Does not predict that function tracks the identity of the being (teaching OR 6.27), though it can accommodate it after the fact | Data (notebook 07); not a direct test |
| **Cultural construction** | Variation in vocabulary | Religion predicts the name barely above chance (AUC 0.53). Function is the same across names. The perception profile is equivalent for Christian and non-religious experiencers (TOST p = 0.005) | Data (notebooks 01, 06) |
| **Jungian archetypes** | Symbol recurrence across cultures | Function tracks being identity; expectations are often contradicted | Data, not decisive (above) |
| **Cognitive Science of Religion** | Agent detection; polytheism | Claimed difficulty explaining monotheism is theoretical. CSR and cultural-evolution accounts do address high and moralizing gods | Argument; contested (§6.4) |

The framework is the primary lens because its predictions about the **character, function and cultural variation** of encounters largely hold (§6.1), and because it gives one vocabulary across domains. That rationale stands or falls with the scorecard, so keep the scorecard current.

---

## 6. Evidence Scorecard

### 6.1 Tested in This Repository: NDE (N = 6,751 Unique Narratives)

Data: NDERF 5,659 + IANDS 1,092, coded by GPT-5.2. Two exact duplicate narratives were removed; the files on disk number 6,753. All rows are length-adjusted where relevant. Reports are in `projects/nde/reports/`.

| # | Prediction | Corrected evidence | Verdict | Notebook |
|---|------------|--------------------|---------|----------|
| 1 | **Constant state, variable form**: the name varies with culture, the function does not | Name × religious background χ²(6) = 15.04, p = 0.020, V = 0.11; × belief at the NDE χ²(3) = 38.40, V = 0.24; religion predicts the name barely above chance (AUC 0.53). Among Christians, Jesus-only vs unknown-only: no difference in guidance, teaching, telepathy, belonging, mission. Perception profile equivalent, Christian vs atheist/agnostic (TOST p = 0.005). Mode differs: visual figure +45.0 pp, unity −19.6 pp | **Hit** for constant function and weak cultural naming. If perceptual mode was meant to be constant, the unity difference is a miss; pre-specify this | 01, 06 |
| 2 | **Beings are functionally differentiated** | 10/11 functions differ across five exclusive being types (Holm; V 0.07–0.18); functions separate divine from relative encounters (AUC 0.673 vs 0.555 for length alone). Light-Being vs other beings: teaching 25.3% vs 12.6% (adj OR 1.96), telepathy 48.2% vs 34.2% (adj OR 1.53) | **Hit** | 01, 07 |
| 2a | Higher-order beings teach | Divine vs relatives: teaching 23.0% vs 4.5% (adj OR 6.27, 3.94–9.98) | **Hit** | 07 |
| 2b | Higher-order beings give more guidance overall (legacy claim) | 73.2% vs 75.9% (adj OR 0.81, 0.61–1.09) | **Not observed**; not a framework prediction (Swedenborg: angels *instruct*, which row 2a confirms) | 07 |
| 2c | Relatives receive and comfort rather than instruct | Relatives: directional 67.3%, comfort 43.8%, teaching 5.9% | **Hit** | 07 |
| 2d | Relatives act as gatekeepers (legacy claim) | Sent back 54.6% (relatives) vs 51.7% (divine), adj OR 1.11, p = 0.42; 47–55% in every group | **Not observed**: sending back is shared by all being types. Not a framework prediction: relatives receive the newly arrived (*HH* §494) | 07 |
| 3 | **Life review as revelation, not condemnation** | Harsh 1.4% (extraction) to 8.7% (second coder, 95% CI 1.3–16.8) of rated reviews; loving is the most common category (51–55% of all rated reviews; 60.3% of Light-Being reviews); loving:critical 1.7–1.8:1 over all rated reviews, 2.65:1 in Light-Being reviews; uncomfortable 21–28% | **Hit** for "rarely condemning, predominantly loving". Not "uniformly loving". The 36.5:1 ratio is coder-dependent; do not quote it as a fixed property | 01, 02, 08 |
| 4 | **Mission returns form a distinct category** | Earthly-mission return reason → commissioning: PPV 94.2%, sensitivity 39.7%, κ = 0.49; holds under the second coder (6/7). Independent features adj OR 2.0–3.3. Commissioning prevalence 14.8% (calibrated) to 21.9% (extraction) | **Supported** as a coherent *reported* category (same-source caveat) | 03, 08 |
| 5 | **Personhood of the Being of Light** | Teaching, telepathy (rows 2, 2a); mission-returners → personified encounter OR 4.38 (adj 3.26); spirituality rose in 89.2%, more than after other beings (p = 0.003). Singularity not measurable (8 Hindu/Buddhist cases, 2 name several figures). "Corrective" not specific to the Being (57.2% vs 55.2%, p = 0.59). "Presence" is the coder's label (κ 0.44), not the experiencer's word | Associations **supported**; personhood itself is **interpretation**; singularity **underdetermined** | 01, 03, 08 |
| 6 | **Transformation** | Death fear decreased 88.0%, increased 0.9% (same as other beings, 88.1%); religiosity shows no net change (p = 0.58) | **Supported** descriptively; not specific to the Being | 01, 04 |
| 7 | **Normative path: characteristic stage sequence** | Strict canonical order 0.05% (3/6,249); "mostly" canonical 37.7%. The order tested is the NDE literature's (OBE → tunnel → light → encounters → review → return) | **Not observed**; not a framework prediction: Swedenborg's sequence is three states in the world of spirits, which some skip (*HH* §491), and an NDE reaches at most its threshold | 02 |
| 8 | **Discrete degrees structure perception** | Notebook 06 assigned each marker to one degree: one dominant factor, no prevalence hierarchy (ρ = −0.47, p = 0.28) — not a test of the doctrine (every degree is in every thought, *DLW* §§222–229). Registered test of the doctrine as written (notebook 09, one cumulative continuum): length-stratified Mokken H = 0.245 (0.231–0.259), threshold 0.30; one five-item monotone scale; archives agree | **Underdetermined** (registered verdict) | 06, 09 |
| 9 | **Being of Light → "celestial" perception** | After length adjustment, only comparative reality (OR 1.87) and telepathy (OR 3.90) remain elevated; comparative reality is a less stable code (κ 0.74, test–retest 0.58) | **Partial hit** | 06 |
| 10 | **East–West: the "Western profile" is a scholarly construction** | Claimed rates not observed in these archives (being of light 11.8% of all accounts, 20.7% of those with any light) | **Supported** for these archives; the Japanese side is untested | 05 |
| 11 | **Purposive economy** | Personal light co-occurs with mission (adj OR 3.26) and life review (adj OR 1.89) | Association **supported**; direction is **interpretation** | 05 |

**Summary of the NDE domain:**
- **Hits or supported:** 9 rows (1, 2, 2a, 2c, 3, 4, 6, 10, 11), plus a partial hit (9) and the associations in row 5. The framework's predictions about the **function, character and cultural variation** of encounters largely hold.
- **Not observed, and not framework predictions:** 3 rows (2b, 2d, 7). Divine figures do not give more guidance overall, relatives are not specific gatekeepers, and there is no fixed episode-level stage order. None of these claims is in Swedenborg's texts; they entered through earlier summaries and the NDE literature.
- **Underdetermined:** perception as one cumulative continuum (row 8, registered test); singularity of the Being (row 5).
- **Misses among the framework's own predictions:** none at present. The only candidate is row 1's perceptual mode, if "mode" was meant to be constant, which was never specified. With no misses, the weight of the case rests on whether registered tests on new data (row 8; §6.7) can fail and do not.

### 6.2 Measurement Reliability: What the NDE Numbers Can Bear

A blind second coder recoded 100 random accounts and 44 life reviews (`projects/nde/notebooks/08_extraction_reliability.ipynb`; codes and conventions in `projects/nde/validation/`). A human coder would be a second reading with its own error, not ground truth. What matters is reproducibility, and that has been measured.

| Reliability | Fields |
|-------------|--------|
| κ > 0.80 | tunnel 0.97, life review 0.92, telepathic communication 0.88, guidance received 0.88, being of light 0.87, deceased relatives 0.85, any light 0.85, return decided by a being 0.83, God or Jesus 0.82 |
| κ 0.70–0.80 | boundary (any) 0.77, earthly-mission reason 0.75, more real than earthly life 0.74, mission commissioned 0.71, teaching 0.70; religious background 0.79 |
| **Convention-dependent** | "unknown presence" vs "other" (κ 0.44); boundary *type* (κ 0.34); "implied" mission (prevalence 21.9% → 14.8%); harsh vs uncomfortable judgment (loving:harsh 36.2:1 → 6.4:1; loving:critical stable at 1.72–1.77) |

GPT-5.2 test–retest on duplicate submissions has a median κ of 0.88. It is least stable on "more real" (0.58) and judgment intensity (0.58). Do not build a conclusion on a convention-dependent field without saying so.

### 6.3 Withdrawn Figures: Never Cite These

| Withdrawn | Why | Use instead |
|-----------|-----|-------------|
| χ² = 365.14 (religion × identification) | Sparse-cell artifact | χ²(6) = 15.04, V = 0.11; belief at NDE χ²(3) = 38.40, V = 0.24 |
| "Experiential properties all differ by < 10%" | Broken fields | Function equal; visual mode +45.0 pp, unity −19.6 pp |
| ML classifier "below baseline" (37.8% vs 45.9%) | Overfitting on 37 test cases | Cross-validated AUC 0.53 |
| "61.8% of Christians … unknown presence; 11.2% Jesus" | Old-schema shares of all encounters | Christian background: unknown 44.2%, Jesus 25.1% (first-listed); unknown-only 42.6% |
| "51.9% call it presence, a personal word" | `unknown_presence` is the coder's label, not the experiencer's word | 50.6% unknown-only, as a label (κ 0.44) |
| Entity function χ² = 41.13; 70–73% guidance; 29.5% "told to return" | Percentages from a legacy script on a superseded schema. The χ² is not an NDE statistic: it is the MallWorld entity × vertical-level test, on nested data | Rows 2–2d |
| "94.2% discriminant accuracy"; χ² = 3,018 | PPV mislabelled; circular test | PPV 94.2%, sensitivity 39.7%, κ 0.49 |
| Loving 32.2% / harsh 0.9%; "36.5:1" as a fixed property | Wrong denominator; coder-dependent | Row 3 |
| "81.7% guidance, nearly 2× other beings"; "475 vs 239 teaching (χ² = 25.24)" | Guidance is 1.09×; χ² = 25.24 is the guidance test | Teaching 25.3% vs 12.6% (χ² = 98.0) |
| Telepathic 34.8% | Share of mentions | 48.2% per experiencer |
| 84.2% increased spirituality; 0.0% increased death fear | Broken scale | 89.2%; 0.9% |
| "Singular Being even for polytheists" | Not measurable | Underdetermined |
| κ = 0.84 inter-rater reliability on 200 records | No such study existed | §6.2 |
| "95 out of 100 questions produce significant patterns" | No source in the repository; at N in the thousands nearly every association is significant, so the count is not evidence | §6.7 |
| NDE N = 6,753 | Includes 2 exact duplicates | 6,751 |
| "Misses" on a fixed stage sequence, discrete-degree structure, gatekeeping and guidance amount, scored against the framework | The predictions are not Swedenborg's (§3, "Find the prediction in the text") | Rows 2b, 2d, 7, 8 |
| MallWorld vertical ρ = 0.25–0.30 "replicated across splits" | Typed banner; not significant in either holdout split; contaminated population | ρ = +0.064; worse below ground, not better above (§6.5, M1–M2) |
| MallWorld "entity autonomy"; social interactions in malls z = +22.8 | Join on `location_id` alone, matching entities to other dreams | Rule 17; §6.5 |
| MallWorld animals "completely independent of atmosphere (χ² ≈ 0, p = 1.0)"; animal ICC 0.630 | Binning error left one category; the "ICC" was not an intraclass correlation | Hostile creatures 59.0% vs 15.8% by atmosphere, OR 7.69; P1 (§6.5, M7) |
| MallWorld "dreamer identity explains 56.4% of atmosphere variance" | η² by dream, not dreamer, inflated by small groups | Within dream ICC 0.31; same author across dreams 0.09 (P4) |
| MallWorld thesis §6 "ruling love" figures (F = 47.82, partial r = 0.751, R² 0.398) | In no notebook output | — |
| MallWorld "twenty of thirty pre-registered tests" | Plan written after the reports | `projects/mallworld/docs/PREREGISTRATION_2026-10.md` |
| MallWorld vs NDE atmosphere V = 0.645 as evidence of "altitude" | Locations vs accounts; non-discriminating (selection, different schemas) | Descriptive only |

The MallWorld audit lists every withdrawn figure: `projects/mallworld/docs/STATISTICAL_AUDIT_2026-10.md`.

### 6.4 Not Tested in This Repository (Literature-Based)

These claims rest on published literature or interpretive argument, not on analyses here. Label them **consistent with the framework (literature)** or **interpretation**. Never label them as a hit from this project's data.

| Claim | Status of the evidence | What a test would need |
|-------|------------------------|------------------------|
| **Restorative incarnation (DOPS)**: past-life cases cluster after violent or premature death; birthmarks match wounds | DOPS publications report that a majority of solved cases involve violent or unnatural death, and medical documents confirmed birthmark–wound correspondence in 43 of 49 cases (88%; Stevenson, 1993). Cases are selected by investigators and the base rates are uncontrolled. This is a **project extension**, not Swedenborg's prediction: he denied reincarnation and attributed apparent past-life memories to the memories of spirits | Case-level DOPS data with a pre-specified comparison group |
| **Deep symbolic systems** (Palaeolithic signs, Göbekli Tepe, Australian songlines) | Archaeological facts are well documented: 32 recurring geometric signs in European caves (von Petzinger, 2016); monumental architecture at Göbekli Tepe c. 9600 BCE. Reading them as an "Ancient Church" of "celestial men" is interpretation. Cumulative-culture accounts also accommodate them | A prediction that distinguishes the framework from cumulative cultural evolution |
| **Monotheism vs Cognitive Science of Religion** | A theoretical argument that CSR explains polytheism but not the "heart of unity". Contested: CSR and cultural-evolution work address high and moralizing gods (e.g. Norenzayan, 2013). High-god beliefs in small-scale societies are documented, but Schmidt's original-monotheism thesis is not generally accepted | Cross-cultural databases (e.g. Seshat, D-PLACE) with predictions stated in advance |
| **Myth formation by "ruling love"** (Genesis 1 vs Enuma Elish) | A two-text interpretive comparison; the shared proto-myth and opposing trajectories are a coherent reading | Coding many myth pairs derived from shared proto-myths, with the social-ethic variables fixed before coding |
| **Ancient Word and the Magian substrate** | Parallels are real topics of scholarship: mēnōg/gētīg; Daniel as *rab-ḥarṭummin* (Dan 4:9) and *rab-signin* (Dan 2:48); the Qumran "Two Spirits". The direction and extent of Persian influence are debated. The specific claim that "Great Tartary" is where Avestan texts survived is **not supported**: surviving Avestan manuscripts come from Zoroastrian communities in Iran and India | Textual-transmission evidence tied to Central Asia |
| **Oral-tradition durability** | Well supported as plausibility: Australian Aboriginal memories of coastlines drowned more than 7,000 years ago (Nunn & Reid, 2016); Klamath traditions of the Mount Mazama eruption c. 7,700 years ago | Supports plausibility only; it does not test the content of an "Ancient Word" |

### 6.5 Tested in This Repository: MallWorld (N = 1,918 Dream Reports)

**Data.** Dream reports from r/TheMallWorld with at least one coded location, excluding exact duplicates: 8,685 locations, 1,303 authors. Coded by GPT-5.2. Every result is a dream-clustered estimate adjusted for narrative length.

**Sources.**
- Reports: `projects/mallworld/reports/`.
- Audit: `projects/mallworld/docs/STATISTICAL_AUDIT_2026-10.md`.
- Pre-registration: `projects/mallworld/docs/PREREGISTRATION_2026-10.md`, committed before notebook 07 was written.

| # | Prediction | Corrected evidence | Verdict | Notebook |
|---|------------|--------------------|---------|----------|
| M1 | **Below ground is worse**: the hells are beneath, the deeper the worse (*HH* §§584–586) | Negative atmosphere 76.0% underground vs 58.3% at ground; OR 1.69–2.29, robust to location type and to excluding basements, caves and subways | **Partial hit** (with M2) | 02 |
| M2 | **Above ground is better**: "interior things correspond to higher things" (*HH* §188) | 65.2% negative above ground (OR 1.29–1.35 vs ground); within-dream OR 0.88 per level (0.72–1.07); overall ρ = 0.064 | **Miss**: ground, not the top, is least negative | 02 |
| M3 | **Turbid water ↔ negative**: waters signify the intellectual things of faith, and in the opposite sense falsities (*AC* §§42, 739) | Dirty vs clean 84.4% vs 43.0% negative (OR 7.19); clear vs murky 20.6% vs 73.1% | **Hit** (pattern fit) | 02 |
| M4 | **Darkness and cold light ↔ negative**: the darkness of hell (*HH* §584); truths without good "shine coldly" (*HH* §132) | ρ = −0.49 with darkness; cold vs warm 70.8% vs 33.1% negative (OR 4.88). Light temperature was primed by the prompt | **Hit** (pattern fit) | 02 |
| M5 | **Warm light above**: flaming light in the celestial kingdom (*HH* §128), which dwells on the heights (§188) | Warm 41.7% below / 67.6% ground / 55.6% above | **Miss** | 02 |
| M6 | **Exposure ↔ negative**: shame at nakedness marks lost innocence (*HH* §341) | 87.1% vs 53.5% negative (OR 6.35). The prompt coded exposure as "shameful"; the text gives unashamed nakedness the opposite sense (innocence, §§179, 280) | **Hit** (pattern fit), weak: primed | 02 |
| M7 | **Noxious animals in negative scenes** (P1, pre-registered; *HH* §110; *DLW* §§338–339) | 84.8% vs 58.3% negative (OR 4.08, 1.20–13.90; Holm p = 0.036). With a second coder's animal detection: OR 3.35, p = 0.11 | **Hit**; precision coder-sensitive | 07, 08 |
| M8 | **Noxious animals below ground** (P2, pre-registered): noxious creatures appear in the hells (*DLW* §339), which are beneath (*HH* §584) | 25.0% vs 23.6% (OR 1.04) | **Miss** | 07 |
| M9 | **The deceased in less negative scenes** (P3, pre-registered; *HH* §§449–450, 494) | 45.5% vs 68.8% negative with living known persons (OR 0.36, 0.15–0.87; Holm p = 0.036); second coder OR 0.35 | **Hit**; coder-robust | 07, 08 |
| M10 | **Ruling love persists: same person, similar atmospheres** (P4, pre-registered; *HH* §§173–176, 477–479) | ICC1 = 0.094 across an author's dreams (Holm p = 0.036; 181 authors) | **Hit**; modest | 07 |
| M11 | **Beings and animals co-vary with the state of the scene** (*HH* §§110, 173–176) | Threats 95.4%, creatures 84.0%, friends 58.0% negative; hostile creatures 59.0% vs 15.8% by atmosphere (OR 7.69) | Consistent; not discriminating | 03 |
| M12 | **Authority guides above and punishes below**: heaven's governors "minister and serve" (*HH* §218); the hells are ruled by fear of punishment (§543) | Guiding or observing 55.0% below vs 35.7% above (OR 0.46, p = 0.24) | **Miss** in direction; not significant | 03 |
| M13 | **Characteristic narrative arc** (legacy claim) | Arc shapes as under random order; only continuous descent exceeds chance | **Not observed**; not a framework prediction: the arc types come from the archived report's dramatic-structure analysis, and Swedenborg's sequence of states is after death, in the world of spirits (*HH* §491) | 04 |
| M14 | **East–West quality propagation** (*HH* §§141–153; §9) | Cardinal directions coded in 33 dreams | **Not testable** | 01 |

*HH* = *Heaven and Hell*; *DLW* = *Divine Love and Wisdom*; *AC* = *Arcana Coelestia*. The text for P2 (*DLW* §339, *HH* §584) was located after the test. The registration grounded P2 only in *HH* §110 and §§173–176. That leaves the miss unchanged.

**Summary of the MallWorld domain.**
- **Hits:** M3, M4, M6, M7, M9 and M10, plus the partial hit M1. The framework's predictions about the **character** of what appears in a scene hold: water, light, exposure, animals, the deceased, and a person's persistent atmosphere.
- **Misses:** M2, M5, M8 and M12. All four concern **height**, and P2 (M8) is pre-registered. The text puts the interior above and the hells beneath (*HH* §§188, 584). In these dreams only the second half holds. Ground, not the top, is least negative; warm light is not concentrated above, noxious animals are not concentrated below, and authorities do not guide more above. These are the only misses among the framework's own predictions in this repository (the NDE domain has none, §6.1).
- **Not observed, and not a framework prediction:** a characteristic arc (M13).
- **Caveat:** every hit is also predicted by ordinary association, and M1–M6 were not registered in advance. The world of spirits appears "like a valley between mountains and rocks", with the ways to the hells opening downward and the gates of heaven visible only to those prepared (*HH* §429). That reading would accommodate "worse below, not better above", but only after the fact. It is a hypothesis for new data, not a result.

**Reliability** (`projects/mallworld/notebooks/08_extraction_reliability.ipynb`; blind second coder, 119 dreams).
- **Where both coders rated a feature, values agree:**
  - light κ 0.90;
  - vertical level κ 0.84;
  - atmosphere valence κ 0.75 (negative vs not, κ 0.74–0.89);
  - affect κ 0.67.
- **Detection:** deceased person κ 0.79; animal class κ 0.70.
- **Convention-dependent:** GPT-5.2 rates atmosphere, level and affect about twice as often, by inference. Overall κ including "not mentioned" is 0.35–0.51, so prevalence figures such as "64% of locations are negative" describe GPT-5.2's inferences.
- **Threat type:** the `threat` entity type covers only part of hostile encounters (κ 0.50).

### 6.6 Other Projects: Not Yet Audited

The **Remission** project (`projects/remission`, 569 extracted cases: 350 PubMed Central, 149 Radical Remission, plus 70 healing-related NDE accounts) has not been through the audit procedure applied to the NDE and MallWorld projects. Before citing a number from it:
- confirm that their notebooks execute;
- check enum comparisons against their schemas;
- state denominators;
- control for narrative length.

### 6.7 Weighing the Evidence

The physics analogy sets the standard. General relativity was accepted because quantitative predictions specified in advance came true, including Mercury's perihelion and the deflection of light. The analogy applies here only to predictions of that kind.

- **Significance is cheap.** With N = 6,751, almost any association reaches p < 0.05, and length inflates co-occurrence. A count of significant tests is not evidence for the framework.
- **What counts:** pre-specified predictions that could fail; effect sizes; robustness to narrative length and to the coder; replication in data not used to form the prediction.
- **Current standing.**
  - NDE domain: hits on function, character and cultural variation. A fixed stage order and per-degree layering of perception are not observed, but neither is a framework prediction. The registered test of perception as one continuum is underdetermined (§6.1).
  - MallWorld domain: hits on the character of scenes (water, light, exposure, animals, the deceased, persistent atmosphere), three of them pre-registered. Misses on height: below ground is worse, but above ground is not better, warm light is not more common above, noxious animals are not more common below (pre-registered), and authorities do not guide more above. These are the repository's only misses among the framework's own predictions. A characteristic dream arc is not observed, and is not a framework prediction (§6.5).
  - Other domains: consistent with the framework but untested here (§6.4).
  - The cumulative case is real for the first group and should not be stretched to the second.
- **What would raise the weight:**
  - pre-registered predictions tested on new archives (non-Western NDE collections, new NDERF submissions after a cut-off date);
  - head-to-head tests in which a competing framework states its prediction too;
  - replication of the teaching and non-condemnation results with a revised schema;
  - a registered replication of the MallWorld height results (M1, M2, M5, M8, M12) on dreams posted after a cut-off date, since these are the misses.

The open questions are which parts of the framework work, how well, and why. The "why" leads into ontology, which remains speculative.

---

## 7. Framework Refinement: Where Swedenborg Was Wrong

This project does **not** treat Swedenborg as infallible. Where the data or deeper analysis contradict his claims, the framework is corrected. The refinements below are theoretical. Their empirical support is labelled.

### 7.1 The Limbus as Cartesian Artifact — CORRECTION

**Swedenborg's claim:** after death, the spirit retains a "limbus", a fringe of purest natural substances, which provides containment and prevents dissipation.

**The problem:** the concept arose from Swedenborg's training in Cartesian mechanics. The "interaction problem" (how can unextended spirit interact with extended matter?) led him to posit a nexus substance. The limbus is a theoretical epicycle that saves a flawed dualist premise.

**The correction:** the physical world and the spiritual-natural world are not separate ontological floors. They are one continuum viewed through different filters. The physical is the "fixed edge" of the spiritual-natural: maximum resistance and inertia, maintained for the formation of selfhood (the proprium).

**Supporting observations** (interpretation; not tested in this repository):
- Swedenborg himself wrote: "When what is spiritual touches what is spiritual, it is just the same to sense as when what is natural touches what is natural."
- Identity is coded as clear and continuous in 97.0% of NDE accounts that state it (notebook 02). This is consistent with a single continuum. Whether experiencers fail to notice the transition is not coded.
- MallWorld reports describe a recurring, hyper-real dream topography. Its consistency across dreamers is an interpretive reading of an unaudited project.

**What this means:** the container of identity is not a material skin but the **biography**: the history of states, choices and loves accumulated in time. We are not ghosts needing a bucket; we are the "concrete spirit" in seed-state formation.

### 7.2 Biological Determinism about Jesus — CORRECTION

**Swedenborg's claim:** Jesus had a "soul from the Father" (Divine) and a "body from the mother" (Human). This follows the biology of his time, in which the sire provides the soul and the dam the body.

**The problem:** this makes Jesus a "God-Man hybrid" rather than a true human person, and implies that his struggles and faith were divine pantomime.

**The correction:** Jesus was a **complete human soul** who achieved perfect alignment with the Divine through the **removal of obstruction** (the proprium). He was not the Lord disguised as a human but a human filled with the Lord. The mechanism was spiritual transparency, not biological origin.

**Textual support:**
- "I can do nothing by myself" (John 5:19).
- "Why do you call me good? No one is good except God alone" (Mark 10:18).
- The genuine struggle of Gethsemane.

**What this means:** the Divine Human is not exclusive to Jesus. It is the Lord's capacity to be personal with every human, appearing in forms the soul can receive. This is the framework's reading of "constant state, variable form" in NDEs. The data support the weak cultural naming over constant function (§6.1, row 1). That the presence *is* the Lord is interpretation.

### 7.3 Somatic Influx — EXTENSION (hypothesis, not yet tested here)

**The phenomenon:** spontaneous regression of advanced cancer without adequate treatment is documented in the case literature.

**The hypothesis:** the body functions as the "soul in ultimates", expressing the state of the spirit. When spiritual transformation occurs, the physical correspondence (disease) may lose its sustaining conditions. Examples of such transformation are the release of suppressed emotions, a shift from fear to love, and alignment of the will with life. This is **speculative**. Stated as a testable claim, it predicts that psycho-spiritual change precedes and predicts remission more than chance and confounders would.

**Evidence status:**
- Turner (2014) identified nine factors in interviews with remission survivors, seven of them non-physical. These are qualitative, retrospective, self-selected data.
- Reported timelines of rapid change after spiritual shifts are anecdotal.
- The analogy with DOPS birthmarks is an inference, not evidence.
- The Remission project in this repository is the place to test the hypothesis. Its results are not yet audited (§6.6).

---

## 8. The Methodology Summarized

1. **Swedenborg predicts and the data confirm** → report a **hit**.
2. **Swedenborg predicts and the data contradict** → report a **miss** and investigate.
2a. **The data contradict a claim Swedenborg does not make** → report **not observed**, and say where the claim came from. Find the prediction in the text before scoring.
3. **The framework reflects 18th-century limitations** → correct the artifact and keep the valid principle.
4. **The data suggest extensions** → state the extension as a hypothesis and test it.

We are not defending Swedenborg, and we are not attacking him. The framework is a hypothesis generator, and the data arbitrate. The goal is to find out which of its patterns are real, and why they emerge.

---

## 9. Application to MallWorld Analysis

When analysing MallWorld dream data, interpret spatial, entity and atmospheric patterns through the correspondential lens. Test them as in §3–§4:

| Natural Feature | Swedenborgian Correspondence | NOT This |
|-----------------|------------------------------|----------|
| Vertical space | Interior above, exterior below: "interior things correspond to higher things" (*HH* §188); the heavens are stacked in successive order (*DLW* §205). A dream level is not assigned to a degree (§5.1) | Id/Ego/Superego |
| Underground | Toward the hells, which are beneath; the deeper, the worse (*HH* §§584–586) | "The unconscious" |
| Elevated | More interior states; the celestial kingdom dwells on the heights (*HH* §188) | "Superego" |
| Entities | Spiritual beings with differentiated functions | Psychological projections |
| Threatening atmosphere | Spiritual state of the space; influx quality | "Repressed content" |
| Creatures | Affections made visible (animals = affections, *HH* §110; noxious creatures appear in the hells, *DLW* §339) | "Instinctual drives" |
| Authority figures | Beings with teaching/governing function (heaven's governors serve, *HH* §218; the hells are ruled by fear of punishment, §543) | "Internalized parents" |

Directional framing used in the MallWorld synthesis:
- **East** = ruling love (the source of quality). **West** = natural/sensory expression, which can be positive when East is good; it is not inherently negative.
- **Proprium** refers to the self. Self-love appears when the ruling love is self-oriented. Do not equate West with proprium by default.
- Let quality propagate outward from East into adjacent quadrants. Infer anchors relative to East when explicit cardinal labels are absent.

**What the MallWorld data say about this table (§6.5).** The table is a set of hypotheses, not findings.
- **Vertical space.** Only the lower half holds. Underground locations are worse than ground, but elevated ones are not better, and within a dream going up does not improve the atmosphere. Height accounts for all four MallWorld misses (M2, M5, M8, M12).
- **Creatures.** They co-vary with the scene, as "animals = affections" predicts (P1, pre-registered). Noxious animals are not more common below ground (P2).
- **Authority figures.** They do not guide more above and punish more below.
- **East–West framing.** It cannot be tested: cardinal directions are coded in 33 of 1,918 dreams.

Use the table to state predictions before analysis (§3). Do not read it into results.

## 10. When to Apply the Framework

- **DO** test whether patterns align with correspondential predictions specified in advance.
- **DO** report whether the data support, contradict or underdetermine the framework.
- **DO** report hits as hits, clearly.
- **DO** note parallels with other frameworks where relevant, as secondary.
- **DO NOT** substitute Jungian or Freudian interpretation as the primary lens.
- **DO NOT** dismiss findings that support the framework to appear "scientific" or "balanced".
- **DO NOT** force data to confirm the framework, or present literature-based consistency as a tested hit.

## 11. Source Documentation

Source material for the framework is maintained in the companion repository [literary-compilation](https://github.com/kayna-of-light/literary-compilation):
- `data/02_Swedenborgian_Theology/` — core doctrinal documents
- `data/01_Consciousness_Studies/` — empirical validation analyses. See especially "Validating Swedenborg's Correspondences.md", "Testing Swedenborg's Correspondences Empirically.md" and "Being of Light - Statistical Analysis of NDE Phenomenology.md".

Figures in those documents, and in `docs/external/` and `projects/nde/docs/` (other than the 2026-10 audit), may predate the audit. Cite numbers from this repository's executed notebooks.

---

## 12. Project Overview

The repository is a **general-purpose framework** for research projects that:
1. **scrape** narrative data from web sources;
2. **extract** structured data from the text with Azure OpenAI structured output;
3. **analyse** the structured data statistically and write reports.

| Project | Description | Data (raw files on disk) |
|---------|-------------|--------------------------|
| [NDE Analysis](projects/nde/) | Near-death experience phenomenology | NDERF 5,666 raw / 5,659 extracted unique; IANDS 1,102 raw / 1,092 extracted unique |
| [Remission Analysis](projects/remission/) | Spontaneous remission and psycho-spiritual transformation | PubMed Central 350; Radical Remission 149; 70 healing-related NDE accounts (NDERF 50, IANDS 20) |
| [MallWorld Analysis](projects/mallworld/) | Collective dream phenomenology and spatial symbolism | r/themallworld 3,743 raw / 3,732 extracted; 1,918 primary dream reports (loader `primary` population) |
| `projects/extraction-test/` | Small extraction experiments | — |

The repository works with [literary-compilation](https://github.com/kayna-of-light/literary-compilation), which supplies theoretical frameworks. Statistical findings from this project feed its knowledge graph, so only audited figures (§6) should flow there.

---

## 13. Repository Architecture

```
structured-data-analysis/
├── shared/                         # Shared core library
│   ├── scrapers/                   # base.py (ScrapedCase, http_get, slugify, clean_text) + per-source scrapers
│   ├── analysis/                   # azure_client.py, base_analyzer.py, structured_extractor.py
│   ├── registry/loader.py          # YAML dataset registries (load_registry, DatasetRegistry)
│   ├── models/common.py            # Shared Pydantic base classes
│   └── build_pdfs.py               # Generic Markdown → PDF builder
├── data/                           # Raw scraped data (one JSON per case)
│   ├── nderf/ iands/ mallworld/ pmc/ radical_remission/
├── projects/
│   └── <project>/
│       ├── extract.py              # Structured extraction entry point
│       ├── models/questionnaire.py # Pydantic schema = the codebook
│       ├── registries/             # Dataset registry YAML
│       ├── structured/             # Extraction output (JSON)
│       ├── notebooks/              # Numbered analysis notebooks (archive/ = superseded)
│       ├── reports/                # Markdown reports (source of truth); latex/ + PDFs generated
│       ├── scripts/                # Project utilities
│       ├── tests/                  # Project tests
│       └── docs/                   # Project documentation
├── projects/nde/scripts/nde_dataset.py   # Verified NDE loader (use it; §4)
├── projects/nde/scripts/md_to_latex.py   # Report Markdown → LaTeX (--project mallworld for MallWorld)
├── projects/nde/validation/              # Second-coder reliability codes + conventions
├── projects/mallworld/scripts/mallworld_dataset.py  # Verified MallWorld loader (use it; §4)
├── projects/mallworld/validation/        # MallWorld second-coder codes + conventions
├── docs/REPORT_WRITING_GUIDELINES.md     # Report structure
├── secrets/azure_openai.env              # Credentials (gitignored)
└── output/, projects/*/output/           # Generated figures (gitignored; regenerate by running notebooks)
```

There is no top-level `tests/` directory; tests live in `projects/*/tests/`.

---

## 14. Core Concepts

### 14.1 Questionnaire Schema (Pydantic Models)

Each project defines its codebook as Pydantic models in `models/questionnaire.py`:
- enums for categorical responses;
- `Field(description=...)` text to guide the extractor (this text *is* the codebook a second coder uses);
- inheritance from `QuestionnaireBaseModel` with `extra="forbid"`.

```python
from enum import Enum
from pydantic import BaseModel, Field

class MentionResponse(str, Enum):
    YES_EXPLICIT = "yes_explicit"    # Directly stated
    IMPLIED = "implied"              # Inferrable from context
    NO = "no"                        # Explicitly negated
    NOT_MENTIONED = "not_mentioned"  # No information

class MyResponse(BaseModel):
    feature_present: MentionResponse = Field(
        description="Was the feature explicitly mentioned or implied?"
    )
```

**Schema design lessons from the reliability study:**
- **Define the boundary between neighbouring categories.** For example, say when an unidentified being is `unknown_presence` and when it is `other`.
- **Give a precedence rule when categories can co-occur.** For example, a barrier and a spoken "not your time".
- **Say what "implied" requires.** For example, a specific task, not a general life lesson.
- **Anchor severity scales with examples**, including the hard cases (self-condemnation in hellish reviews).
- **Use `no` only when the narrative can distinguish it from `not_mentioned`.**
- **Record functions per entity, not per account,** when the analysis needs to attribute them.

### 14.2 Registry System

YAML registry files define which data files a project analyses, without duplicating data:

```yaml
# projects/my_project/registries/dataset.yaml
name: dataset_full
description: Complete dataset for analysis
version: "1.0.0"
datasets:
  source_name:
    description: Data source description
    source_path: ../../../data/source_name   # relative to the registry file
    files: "*"                               # or a list of specific files
    exclude: []
```

```python
from shared.registry import load_registry
registry = load_registry(Path("registries/nderf.yaml"))
files = registry.get_files("nderf")     # list of Paths; registry.list_datasets() names the datasets
```

### 14.3 Extraction Pipeline and Data Flow

`StructuredExtractor` loads files via registries, runs Azure OpenAI structured output with parallel workers, validates against the schema, retries on errors and resumes where it stopped.

```
Raw data (data/) → extract.py + Azure OpenAI → structured JSON (projects/*/structured/)
→ notebooks (verified loader, executed top to bottom) → Markdown reports → LaTeX/PDF
```

---

## 15. Development Guidelines

### 15.1 Creating a New Project

```bash
mkdir -p projects/my_project/{models,registries,notebooks,reports,scripts,structured,tests}
```

1. Define the questionnaire schema in `models/questionnaire.py`, following the design lessons above.
2. Create `extract.py` from the pattern below.
3. Create registry YAML files.
4. Test with `python extract.py --limit 1`, then run the full extraction.
5. Write a verified loader for the project (model it on `projects/nde/scripts/nde_dataset.py`) before writing analysis notebooks.
6. Measure coding reliability on a random sample (model it on `projects/nde/validation/`).

### 15.2 Extraction Script Pattern

```python
#!/usr/bin/env python3
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import MyResponseModel

SUPPORTED_DATASETS = ("source1", "source2")

SYSTEM_PROMPT = """
You are an expert researcher analyzing [domain].
Extract structured information according to the schema.
Ground every answer in the source text.
"""

def main() -> None:
    config = ExtractorConfig(
        response_model=MyResponseModel,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        registries_dir=PROJECT_ROOT / "registries",
    )
    StructuredExtractor(config).run()

if __name__ == "__main__":
    main()
```

### 15.3 `extract.py` Command-Line Options

| Flag | Description |
|------|-------------|
| `--datasets a b` | Datasets to process (default: all) |
| `--limit N` | Process at most N files |
| `--files name.json` | Extract specific files |
| `--dry-run` | List files without calling Azure OpenAI |
| `--overwrite` | Re-extract existing outputs |
| `--max-concurrency N` | Concurrent API calls (default 10) |
| `--temperature T` | Sampling temperature (default 0.7) |
| `--max-output-tokens N` | Response token limit (default 10000) |
| `--model NAME` | Override the deployment name |
| `--secrets-path PATH` | Path to `azure_openai.env` |
| `--log-level LEVEL` | Logging verbosity (default INFO) |

---

## 16. Report Writing Standards

Follow `docs/REPORT_WRITING_GUIDELINES.md`:

```
TITLE: [Descriptive Phrase]: [Methodology Subtitle]
├── ABSTRACT (Background, Methods, Results, Conclusions, Keywords)
├── DATA PROVENANCE TABLE
├── 1. INTRODUCTION (Background, Theoretical Framework, Aims)
├── 2. METHODS (Data Sources, Coding Scheme, Statistical Analysis)
├── 3. RESULTS (one finding per subsection: Narrative → Table → Finding Statement)
├── 4. DISCUSSION (Summary, Interpretation, Implications, Limitations, Future Directions)
├── 5. CONCLUSION
├── REFERENCES
└── APPENDICES
```

- **Statistics:** test statistic, df, p-value, effect size and CI, e.g. `(χ² = 15.04, df = 6, p = 0.020, V = 0.11)`. Subsets are written `n=443`; totals `N=6,751`. Percentages take one decimal place.
- **Finding statements:** after each results table, add a bolded statement labelled with its claim level, e.g. `**Finding (statistically supported):** ...`. Label verdicts against the framework explicitly: **Hit**, **Miss**, **Partial hit**, **Underdetermined**.
- **Limitations** must cite the measured reliability of the fields used (§6.2) instead of a generic "AI coding" caveat.
- **Corrections:** when a report is corrected, add a dated correction notice at the top listing what changed.
- **LaTeX/PDF:** `python projects/nde/scripts/md_to_latex.py "<report name>"`, then compile from `reports/latex/` with `tectonic` or `pdflatex`. Check the rendered PDF: wide tables need content-proportional column widths (the separator dashes set them).

---

## 17. Notebook Conventions

- **Numbered names**, e.g. `01_being_of_light_analysis.ipynb`, `07_entity_function_differentiation.ipynb`. Superseded notebooks go to `notebooks/archive/`.
- **First cell:** purpose, the framework prediction, and what would count as a miss (§3).
- **Execute top to bottom** before committing (`jupyter nbconvert --to notebook --execute --inplace`). Committed outputs must come from the committed code.
- **Summary cells compute what they print.**
- **Figures:** follow the `dataviz` skill; render each figure and look at it before committing.

NDE notebooks load data like this:

```python
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

NDE_ROOT = Path.cwd().parent
sys.path.insert(0, str(NDE_ROOT / "scripts"))
import nde_dataset as nd

df = nd.load_frame()                      # 6,751 rows, one column per schema leaf + word_count/log_words
lr = nd.isin(df, "occurrence", nd.LIFE_REVIEW_YES)
print(nd.fmt_pct(int(lr.sum()), len(df))) # 'k/n = p% [95% CI lo–hi]'
res = nd.adjusted_odds_ratio(df.assign(lr=lr.astype(int), bol=df.bol_encounter.astype(int)), "lr", "bol")
```

MallWorld notebooks load data like this:

```python
MW_ROOT = Path.cwd().parent
sys.path.insert(0, str(MW_ROOT / "scripts"))
import mallworld_dataset as mw

posts = mw.load_posts()                   # one row per post; posts["primary"] marks the analysis population
L = mw.load_locations()                   # primary locations, with vertical_level, valence, log_words
E = mw.load_entities()                    # entity involvements keyed by (post_id, location_id)
res = mw.clustered_logit(L.assign(neg=(L.valence == -1).astype(float)).dropna(subset=["valence"]),
                         "neg ~ C(location_type) + log_words")   # SEs clustered by dream
```

For other projects, read the extraction from the `extraction` key of each structured file (§19.2) and check every enum value against the schema.

---

## 18. Azure OpenAI Configuration

`secrets/azure_openai.env` (gitignored):

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-05-01-preview
```

The extractor uses structured output: the Pydantic schema is converted to JSON Schema, the model must return matching JSON, and validation errors trigger a retry. The NDE extraction used `gpt-5.2` (schema `NDEAnalysisResponse`, run of 2026-01-06).

---

## 19. Data Formats

### 19.1 Scrapers and Raw Data

New sources: create `shared/scrapers/<source>_scraper.py`, inherit from `BaseScraper`, implement `scrape()` returning `List[ScrapedCase]`, and save to `data/<source>/`. Use `http_get` (retry and rate limiting), `slugify` and `clean_text` from `shared/scrapers/base.py`.

```python
@dataclass
class ScrapedCase:
    source: str                    # e.g. "nderf", "pmc"
    source_id: str                 # unique within the source
    url: str
    title: str
    content: str                   # main narrative text
    date_scraped: str              # ISO timestamp
    date_published: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
```

Raw NDE files carry fields such as `id`, `nde_code`, `title`, `date`, `content` and `url`. **`id` and `nde_code` are not unique identifiers**: different people share them. Use the file name, or the `content_checksum` of the structured record.

### 19.2 Structured Output Files

```json
{
  "dataset": "nderf",
  "source_file": "...data/nderf/<file>.json",
  "source_url": "https://...",
  "title": "...",
  "date": "...",
  "content_checksum": "sha256...",
  "extraction_model": "gpt-5.2",
  "extraction_timestamp": "2026-01-06T13:59:35+00:00",
  "schema": "NDEAnalysisResponse",
  "extraction": { "...": "schema fields, nested as in models/questionnaire.py" },
  "response_id": "...",
  "usage": { "...": "token counts" }
}
```

---

## 20. Testing

```bash
python -m pytest projects/nde/tests          # run each project separately
python -m pytest projects/remission/tests
python -m pytest projects/mallworld/tests
python -m pytest projects/nde/tests/test_nde_dataset.py -v   # verified-loader checks
```

- `pyproject.toml` sets `testpaths = ["tests"]`, which does not exist, so pass test paths explicitly.
- Run each project in its own invocation. Each imports a top-level `models` package, so a combined run fails at collection. For the same reason, a notebook that loads both the NDE and MallWorld loaders must swap `models` out of `sys.modules` between imports (see MallWorld notebook 05).
- **Known failures**, with fixtures that predate the current schemas:
  - `projects/nde/tests/test_questionnaire_models.py::test_model_instantiation_succeeds`
  - `projects/remission/tests/test_questionnaire_models.py`: `test_minimal_payload_parses`, `test_valid_payload_parses`

---

## 21. Dependencies and Environment

```bash
pip install -r requirements.txt     # or: conda env create -f environment.yml
```

| Package | Purpose |
|---------|---------|
| `pydantic>=2.5`, `openai>=1.30`, `python-dotenv` | Schema validation, Azure OpenAI, credentials |
| `requests`, `beautifulsoup4`, `lxml`, `selenium` | Scraping |
| `pandas`, `numpy`, `scipy`, `statsmodels` | Analysis |
| `scikit-learn<1.8`, `factor_analyzer` | Modelling (`factor_analyzer` breaks with scikit-learn 1.8) |
| `matplotlib`, `seaborn`, `plotly` | Visualisation |
| `jupyter` | Notebooks |
| `pypandoc_binary` (or `pandoc`), `tectonic` or a LaTeX distribution | Report LaTeX/PDF |

---

## 22. Common Patterns

- Prefer specific enums (`yes_explicit` / `implied` / `no` / `not_mentioned`) over booleans.
- Write precise `Field` descriptions, including precedence rules:

```python
light_encounter: LightEncounter = Field(
    description="""Type of light encounter. Select ONE value.
    Precedence: being_of_light > brilliant_light > presence_without_visual.
    If both brilliant light AND a being of light are described, select being_of_light."""
)
```

- Use `List[Enum]` with `default_factory=list` for multi-select fields. An empty list means not mentioned.

---

## 23. Troubleshooting

| Issue | Solution |
|-------|----------|
| Azure API rate limits | Reduce `--max-concurrency` |
| Missing credentials | Check that `secrets/azure_openai.env` exists |
| Registry path errors | `source_path` is relative to the registry file |
| A percentage comes out 0.0% | Almost always a wrong enum value or field path. Use `nd.isin`, which raises on impossible values |
| Validation errors | Compare the schema with actual output; run `extract.py --limit 1 --log-level DEBUG` |
| `factor_analyzer` TypeError | Install `scikit-learn<1.8` |
| `md_to_latex.py` "unmapped non-ASCII characters" | Add the character to `SYMBOLS` in the script, or use an ASCII form in the Markdown |

---

## 24. Contributing

- **Code style:** format Python with `black` (line length 100) and lint with `ruff check`. Public functions need type hints and docstrings.
- **Before a pull request:**
  - [ ] Tests pass (per project; known failures noted in §20)
  - [ ] Changed notebooks re-executed top to bottom
  - [ ] Every new number in a report or in this file traces to an executed cell
  - [ ] Report LaTeX/PDF regenerated from Markdown
  - [ ] Schema changes documented, and reliability re-measured if fields changed
  - [ ] §6 scorecard updated when a verdict changes

---

## 25. Quick Reference

```bash
# Extraction
cd projects/nde && python extract.py --datasets nderf iands --max-concurrency 4

# Re-execute all NDE notebooks
cd projects/nde/notebooks && jupyter nbconvert --to notebook --execute --inplace 0*.ipynb

# Regenerate report LaTeX and PDF
cd projects/nde && python scripts/md_to_latex.py && cd reports/latex && tectonic "<report>.tex"

# MallWorld: re-execute notebooks; regenerate report LaTeX
cd projects/mallworld/notebooks && jupyter nbconvert --to notebook --execute --inplace 0*.ipynb
cd projects/nde && python scripts/md_to_latex.py --project mallworld
```

```python
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table)
print(f"χ² = {chi2:.2f}, df = {dof}, p = {p:.4f}; {nd.expected_count_report(table)}; V = {nd.cramers_v(table):.2f}")
```
