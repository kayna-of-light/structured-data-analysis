# Statistical Audit of the MallWorld Notebooks and Reports (October 2026)

**Date:** 2026-10-06
**Scope:** the 12 archived notebooks (`notebooks/archive/01–11*.ipynb`); the six archived reports (`reports/archive/`); `docs/FINDINGS_LOG.md`; and the archived plans in `docs/`.
**Replaced by:**
- the verified loader `scripts/mallworld_dataset.py`;
- notebooks `01`–`08`;
- the pre-registration `docs/PREREGISTRATION_2026-10.md`;
- four new reports in `reports/`;
- the second-coder set in `validation/`.

---

## 1. Summary

Every archived claim was traced to the notebook cell that produced it, or found to have none. Each claim was then reproduced on its own construction and re-estimated with correct keys, a defined population and inference that respects the nesting of the data. The archived analyses had ten classes of error:

| Class | Error | Example |
|---|---|---|
| A | **Population contamination.** The thesis population (2,678) included 750 non-dream posts: 453 questions, 167 AI images, 38 map-only posts. They supplied 23.3% of its locations. Notebook 08 filtered on nonexistent keys and used all 3,732 posts | Thesis §3 |
| B | **Join bug.** Entities and interactions were joined to locations on `location_id` alone. That key repeats across dreams (`loc_1`, …), so 4,235 entity involvements became 7,158,025 rows and 7,283 interactions became 12,346,344 rows | "Entity autonomy"; social interactions in malls z = +22.82 |
| C | **Hard-coded banners.** Summary cells printed typed numbers that no computation produced | Vertical ρ = 0.25–0.30; authority p = 0.78 |
| D | **Misattributed or unsourced results.** Report figures that appear in no notebook output, or that came from a different analysis | Thesis §6 (F = 47.82, partial r = 0.751); bathroom 44.2% vs 7.5%; "529 vs 456" |
| E | **Non-schema values and binning errors.** Comparisons against values the schema cannot produce, and bins that leave one category | Ruling-love ICC 0.327 ("unsettling", "fear", "dread", "panic"); animal–atmosphere χ² ≈ 0 |
| F | **Circularity and priming.** Associations built into category labels, or into keyword lists that contain the outcome. Framework meanings written into the extraction prompt | Threats → threatening; "predator" keywords included "attack" |
| G | **Nested data, no length control, no multiplicity correction.** χ² and correlations on locations, entities or transitions as if independent; dream-level contrasts confounded by length | Every χ² in the archived reports |
| H | **Post-hoc "pre-registration".** The falsification plan (2026-01-20, 14:59) was written after the reports it claimed to predict (committed 11:57–14:29 the same day) | Thesis "Twenty of thirty pre-registered tests" |
| I | **Unsupported reliability claim.** "Extraction reliability was validated through manual review": no record exists | Thesis §2.2, Appendix C.1 |
| J | **Misses relabelled as hits.** Results contrary to the stated prediction reported as support | Authority function (residuals opposite to prediction) → "entity autonomy ✅"; warm light above (non-monotone) → "✓ correct, Strong" |

**Decision.** All audited analyses use the **primary population**: dream reports (`dream_report` or `dream_report_with_map`) with at least one location, excluding 8 exact duplicates. That is N = 1,918 dreams, 8,685 locations and 1,303 authors.

**Methods.**
- Inference is clustered by dream.
- Co-occurrence models adjust for log narrative length.
- Height effects are separated from location-type effects.

---

## 2. Audit Method

1. **Loader.** Built `scripts/mallworld_dataset.py`. It:
   - checks every comparison against the schema enumerations (`isin` and `has` raise on impossible values);
   - keys entities, interactions and connections by `(post_id, location_id)`;
   - marks duplicates and defines the populations.

   Tests: `projects/mallworld/tests/test_mallworld_dataset.py`.
2. **Tracing.** Dumped every archived notebook's code and outputs, and traced each report figure to its producing cell.
3. **Reproduction.** Reproduced each traced figure on its own construction (notebooks 01–06), then re-estimated it.
4. **Pre-registration.** Registered four new predictions before computing them (`docs/PREREGISTRATION_2026-10.md`, commit `b3f91962`). Tested them in notebook 07 (commit `9dc71071`).
5. **Second coding.** Second-coded 119 dreams blind to the extraction's codes, and committed the codes before comparison (commit `498e86f4`). Compared them in notebook 08.

---

## 3. Notebook Map

| New notebook | Re-derives | Main corrections |
|---|---|---|
| `01_data_audit` | Populations, coverage, nesting, priming, join bug, duplicate test–retest | Classes A, B, F, G established |
| `02_spatial_affective_correspondences` | Archived 07, 09 (H1, P2–P19), 04 §3.1 | Vertical ρ 0.064 (not 0.25–0.30), not monotone; water, light, exposure re-estimated |
| `03_entities_and_animals` | Archived 05, 07 §3.7–3.9, 09 phases 3–4, 8 | Entity autonomy (join); animals independent of atmosphere reversed; ICC 0.630 not an ICC |
| `04_sequences_and_dreamer_effects` | Archived 06, 09 (D2, RL3, R4) | Loops are labels; arcs are chance; dreamer 56.4% is dream; R4 reversed |
| `05_robustness_time_and_nde_comparison` | Archived 11, 10, 09 (C9) | Sparse V, within-author ≈ within-dream; time equivalence; NDE comparison non-discriminating |
| `06_exploratory_report_claims` | Archived 04 | Social-in-malls join bug; no clusters; 7 components, not 4 |
| `07_preregistered_correspondence_tests` | New | P1, P3, P4 hits; P2 miss |
| `08_extraction_reliability` | New | Values reproducible (κ 0.67–0.90 where both coded); coverage convention-dependent; P3 robust, P1 precision coder-sensitive |

Five archived notebooks had no report:
- 01, 02 and 03 (hypothesis testing, functional tests, transit);
- 08 (outcome prediction, ROC-AUC 0.645);
- `10_architectural_correspondence_tests`.

Their figures appear only in `docs/FINDINGS_LOG.md` and the January plans, which are superseded as a whole. They are not re-estimated, except where a report cited them, and must not be cited.

---

## 4. Withdrawn Figures

### 4.1 Spatial correspondences (thesis §3; vertical report; ontological report)

| Withdrawn | Problem | Corrected (notebook) |
|---|---|---|
| Vertical ρ = 0.25–0.30, "replicated across splits" | Typed banner (C); not significant in either holdout split | ρ = +0.064 (0.007–0.114); worse below, not better above (02 C1) |
| Vertical report ρ = 0.12; elevated 2.77; n = 570/1,547/819; df = 15 | Unsourced (D) | 0.067; 2.61; 263/678/401; df = 18 (02 C1) |
| Water "2.6×"; "45% vs 17%" | "45% vs 17%" never computed (D) | Dirty vs clean OR 7.19 (02 C2) |
| Light V = 0.483, "ordering matches exactly" | Different table and population | ρ = −0.49; OR 3.94 per step (02 C3) |
| Warm light above "✓ correct, Strong" | Non-monotone; no test (J) | 41.7 / 67.6 / 55.6% warm: miss (02 C3) |
| Cleanliness ρ = 0.302 with height | Location-type artifact | OR 1.02 with type (02 C4) |
| Bathrooms "44.2% vs 7.5% (6.0×)" | Unsourced (D) | 84.0% vs 14.3% of coded locations (02 C5) |
| Exposure "3.5× threatening atmosphere" | Was exposure by level, n = 20 (D) | Exposure–atmosphere OR 6.35 (02 C5) |
| "Anomalous perceptual states 7.3% vs 2.2%" | Field is building state | Decay OR 1.64 with type, p = 0.06 (02 C6) |
| Compounding "2.53 vs 1.86" | 1.86 was three-marker locations only | 63.6% → 93.3% negative (02 C8) |
| Location type H = 335.73; "functional categories" d = 0.65 | Categories defined after inspecting means | Clustered χ²(32) = 166 (02 C9) |
| Ascending destinations better, ρ = 0.10 | Not robust to clustering | ρ = +0.046 (02 C10) |
| Ascent/descent 1,220 vs 1,224 | Not reproducible | 552 vs 487 (02 C10) |
| χ² = 1,737.99 (V = 0.212), within-author null "less than half" | 74% sparse cells; within-author ≈ within-dream | Within-dream null 0.129 vs 0.195 (05 R1) |
| Time "no drift" (p = 0.54); "all Cochran's Q p > 0.50"; "instability 2021–2023" | Non-significance read as stability; Q unsourced; small early years | Equivalence within ±0.05 (05 R3) |
| MallWorld vs NDE V = 0.645 (abstract) / 0.352 (§7.3) | Locations vs accounts; 6,753 with duplicates; 0.352 unsourced | V = 0.647 dream vs account; non-discriminating (05 R4) |

### 4.2 Entities, animals and dynamics (thesis §§4–6; entity ecology; sequence motifs; exploratory)

| Withdrawn | Problem | Corrected (notebook) |
|---|---|---|
| Entity autonomy: guides 0%, threats 92–94% hostile at all levels; threats 8.6% at all atmospheres | Labels (F); join (B) | Built into labels; too thin to test (03 E3) |
| Authority functions identical at all levels (p = 0.78) | Join (B); own prediction failed (J) | χ²(8) = 9.2, p = 0.33; direction opposite to prediction (03 E3) |
| Entity × vertical χ² = 41.13 | Nested involvements (G). **This is the statistic the earlier CLAUDE.md attributed to the NDE entity-function claim** | Creatures below borderline; authority above not supported (03 E4) |
| Entity × atmosphere χ² = 792 / 330 | Sparse, nested (G) | Clustered rates (03 E2) |
| Family paradox 15.3% vs 9.1% | Narrative length (G) | Family at location OR 1.06 (03 E1) |
| Helpful 49.7% vs hostile 29.7% success; χ² = 48.90 | Denominator; duplicated join | 88.8% vs 57.5%, OR 5.87 (03 E5) |
| Outcome × level χ² = 27.40 | Nested; not robust | No level effect (03 E5) |
| Animal V = 0.513; predator vs cat OR = 106:1 | Circular keywords (F); zero cell | V = 0.492; OR unbounded (03 E6) |
| Animals "completely independent of atmosphere (χ² ≈ 0, p = 1.0)" | Binning error left one category; placeholder (E) | Hostile creatures 59.0% vs 15.8%, OR 7.69 (03 E6) |
| Animal ICC = 0.630; H = 70.91; η² = 0.605 | Not an ICC; within-dream; proper ICC 0.207 omitted (J) | ICC 0.130, p = 0.30 (03 E6) |
| Animal 89.5% between dreamers; r = 0.753 | Single-dream authors have zero deviation | r = 0.135, p = 0.62 (03 E6) |
| Dreamer explains 56.4%, location 7.1% | Dream, not dreamer; small-group inflation | Dream ICC 0.314; author 0.094–0.183; type 0.058 (04 S5) |
| Ruling-love ICC = 0.327 | Non-schema values (E); within-dream | ICC 0.041, p = 0.22 (04 S6) |
| R4 partial ρ = 0.007, "strongly supports ruling love" | Null read as support; significant alternative unreported (J) | Affect predicts next atmosphere, OR 1.62 within dreams (04 S6) |
| Thesis §6: F = 47.82, η² = 0.136; partial r 0.751, 0.312, 0.186, 0.164, 0.261; R² 0.398; congruence 65.2%, χ² = 54.17; dream 1–2 r = 0.456; ICC t = 8.41 | In no notebook output (D) | — |
| Loops 30.2%, traps 19.5%, "other" loop hub 58.7% | Repeated labels | 2–5 points above a shuffled null (04 S2) |
| Markov "other" stationary 31.7%; mall "gravitational centre"; parking "isolated" | Label frequency | 04 S3 |
| Oscillatory arcs dominate; monotone rare | Same under random order | Excess continuous descent only (04 S4) |
| Worsening 529 vs 456, p = 0.0010 | Unsourced; output was 1,080 vs 931, unclustered | 175 vs 130 dreams, p = 0.012 (04 S4) |
| Four dream archetypes; four latent dimensions | k imposed; silhouette ≤ 0.16; parallel analysis 7 | 06 X2–X3 |
| Social interactions in malls z = +22.82; escape suppressed | Join (B) | OR 1.14, n.s. (06 X1) |
| School self-transition 6.38× | Composition | 3.79 vs 2.32 shuffled (06 X4) |
| "Twenty of thirty pre-registered tests" | Not pre-registered (H) | `PREREGISTRATION_2026-10.md` |
| "Validated through manual review" | No record (I) | Notebook 08 |

---

## 5. Framework Scorecard (MallWorld, after correction)

Each prediction was located in Swedenborg's text before it was scored (`CLAUDE.md` §3, "Find the prediction in the text"). A result that contradicts a claim the texts do not make is reported as **not observed**, not as a miss. *HH* = *Heaven and Hell*; *DLW* = *Divine Love and Wisdom*; *AC* = *Arcana Coelestia*.

| # | Prediction | Text | Evidence | Verdict | Notebook |
|---|---|---|---|---|---|
| M1 | Below ground worse than ground | Hells beneath, deeper is worse (*HH* §§584–586) | 76.0% vs 58.3% negative; OR 1.69–2.29, robust to type | **Partial hit** | 02 |
| M2 | Above ground better than ground | "Interior things correspond to higher things" (*HH* §188) | 65.2% vs 58.3%; within-dream OR 0.88 | **Miss** | 02 |
| M3 | Turbid water ↔ negative | Waters = things of faith; opposite sense falsities (*AC* §§42, 739) | OR 7.19; clear vs murky 20.6% vs 73.1% | **Hit** (pattern fit) | 02 |
| M4 | Darkness and cold light ↔ negative | Darkness of hell (*HH* §584); truths without good shine coldly (§132) | ρ = −0.49; cold vs warm OR 4.88 (primed) | **Hit** (pattern fit) | 02 |
| M5 | Warm light above | Flaming light of the celestial kingdom (*HH* §128), on the heights (§188) | 41.7 / 67.6 / 55.6% | **Miss** | 02 |
| M6 | Exposure ↔ negative | Shame at nakedness marks lost innocence (*HH* §341); unashamed nakedness = innocence (§§179, 280) | OR 6.35 (primed) | **Hit** (pattern fit), weak | 02 |
| M7 | Noxious animals in negative scenes (P1) | *HH* §110; *DLW* §§338–339 | OR 4.08, Holm p = 0.036; second coder OR ≈ 3.3, p = 0.11 | **Hit** (pre-registered; precision coder-sensitive) | 07, 08 |
| M8 | Noxious animals below (P2) | Noxious creatures appear in the hells (*DLW* §339), which are beneath (*HH* §584); located after the test | OR 1.04 (0.31–3.54) | **Miss** (pre-registered) | 07 |
| M9 | Deceased in less negative scenes (P3) | *HH* §§449–450, 494 | OR 0.36, Holm p = 0.036; second coder OR 0.35 | **Hit** (pre-registered; coder-robust) | 07, 08 |
| M10 | Ruling love: consistent atmospheres within a person (P4) | *HH* §§173–176, 477–479 | ICC1 0.094, Holm p = 0.036 | **Hit** (pre-registered; modest) | 07 |
| M11 | Beings co-vary with the scene | *HH* §§110, 173–176 | Threats 95.4%, creatures 84.0%, friends 58.0% negative | Consistent (non-discriminating) | 03 |
| M12 | Authority guides above, punishes below | Heaven's governors serve (*HH* §218); hells ruled by fear of punishment (§543) | 55.0% below vs 35.7% above guiding or observing | **Miss** in direction (n.s.) | 03 |
| M13 | Characteristic arc or sequence | None. The arc types are the archived sequence report's; Swedenborg's sequence of states is after death (*HH* §491) | Arcs as under random order; excess descent only | **Not observed**; not a framework prediction | 04 |
| M14 | East–West quality propagation | *HH* §§141–153 | Cardinal directions in 33 dreams | **Not testable** | 01 |

Every hit is pattern fit: each is also predicted by ordinary association, the same-source caveat applies, and the predictions in M1–M6 were not registered in advance. Predictions about the **character** of what appears in a scene hold. Predictions about **height** hold only for "worse below ground". All four misses (M2, M5, M8, M12) concern height, and one of them (M8) was pre-registered. The NDE domain has no misses among the framework's own predictions (`CLAUDE.md` §6.1, after the October 2026 verdict revisions), so these are the clearest failures of the framework's own predictions in the repository.

A reading of the world of spirits as "a valley between mountains and rocks", with the ways to the hells opening downward and the gates of heaven visible only to those prepared (*HH* §429), would accommodate "worse below, not better above". It was found after the results. It is a hypothesis for dreams posted after a cut-off date, not a rescue of M2.

---

## 6. Remaining Limitations (apply to every result)

- **Same-source coding.** Features, beings and atmosphere are coded from one narrative by one model.
- **Coverage is convention-dependent.** GPT-5.2 rates atmosphere, level and affect about twice as often as a coder requiring explicit statements (notebook 08). Prevalence figures describe GPT-5.2's inferences.
- **Priming.** The extraction prompt attached framework meanings to light temperature, exposure, somatic distress, reality stability, transit mode and authority nature.
- **Self-selection.** The corpus is self-selected by a community defined by uncanny mall dreams.
- **Single-post authors.** 78.7% of authors posted once. Author-level questions rest on the 21.3% who posted more.

---

## 7. Reproducing the Analysis

```bash
python -m pytest projects/mallworld/tests          # loader tests
cd projects/mallworld/notebooks && jupyter nbconvert --to notebook --execute --inplace 0*.ipynb
```

Notebook 07 implements the registration exactly. Its permutation seeds are fixed. Notebook 08 re-draws both second-coding samples and asserts that they match the coded dreams.
