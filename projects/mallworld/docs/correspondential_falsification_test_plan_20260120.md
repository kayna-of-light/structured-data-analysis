# MallWorld Correspondential Falsification Test Plan (Preregisterable)

**Date**: 2026-01-20  
**Scope**: MallWorld (r/themallworld) structured dataset + existing extraction schema  
**Purpose**: Specify *falsifiable* tests of Swedenborgian correspondential predictions in MallWorld dream reports, separating (a) empirical pattern-fit from (b) metaphysical/ontological claims.

---

## 0. Epistemic Stance (What This Plan Assumes / Does Not Assume)

- This plan does **not** assume Swedenborg’s framework is true because of how it arose (visions, experiences, etc.). Origin is treated as methodologically irrelevant.
- The plan treats the framework as a **hypothesis-generator with constraints** (correspondence consistency, discrete degrees, functional differentiation of entities, “constant state / variable form”).
- Success criterion is not “Swedenborg proved”; it is whether the framework yields **out-of-sample** structure and predictive constraints that baselines do not.
- Ontological claims (e.g., “spiritual causation”) are kept distinct from empirical results.

---

## 1. Data + Inclusion Criteria

### 1.1 Dataset
- Source: `projects/mallworld/structured/` outputs (LLM-extracted) derived from `data/mallworld/`.

### 1.2 Inclusion
- A dream is eligible per analysis if it has the required fields present for that analysis (below).
- Primary analyses use listwise inclusion for required fields; sensitivity analyses test robustness to missingness.

### 1.3 Unit of analysis
- Dream-level for most outcomes.
- Location-level for atmosphere/reality/vertical-position distributions.
- Encounter-level for entity role/demeanor/behavior analyses.

---

## 2. Pre-Specified Correspondential Predictions (Falsifiable)

### H1 — Discrete Degrees: Vertical Position ↔ Atmosphere Gradient
**Prediction** (directional):
- Lower vertical positions (underground) have more threatening/oppressive atmospheres than ground.
- Higher vertical positions (upper/uppermost) have more comfortable/welcoming atmospheres than ground.

**Operationalization**
- IV: `vertical_position` (ordered categories mapped to numeric -2..+2).
- DV: `atmosphere` (ordered 1..5).

**Primary test**
- Spearman correlation ($\rho$) between vertical_position and atmosphere.
- Ordinal regression (proportional odds) with controls (below).

**Controls / confounds**
- Location type (e.g., parking_garage/basement vs rooftop/attic are mechanically vertical).
- Dream length (number of locations) to reduce “salience-only” bias.

**Falsification criteria**
- Correlation is non-positive in the full dataset and in both of two holdout splits.
- Or: effect disappears (CI includes ~0 and practical effect below threshold) after controlling for location type.

**Practical effect threshold**
- Pre-register a minimal meaningful effect: e.g., $|\rho| \ge 0.05$ or OR per +1 vertical step ≥ 1.10.

---

### H2 — Proprium Proximity: Underground ↔ Decay/Instability of “Reality”
**Prediction** (directional):
- Underground locations show lower `reality_stability` (more decaying/shifting) than ground/elevated.

**Operationalization**
- IV: vertical_position.
- DV: reality_stability (ordered scale if present).

**Primary test**
- Ordinal regression of reality_stability on vertical_position.

**Falsification criteria**
- No difference between underground vs non-underground in both holdouts.

Note: If reality_stability is sparse, preregister this as “secondary” and require a minimum N.

---

### H3 — Entity Functional Differentiation by Degree
**Prediction** (directional):
- “Creatures” (affections made visible in lower form) concentrate below ground more than at/above ground.
- “Authority” (governing/teaching function) concentrates above ground more than below.

**Operationalization**
- IV: vertical category collapsed into {underground, ground, elevated}.
- DV: entity_type distribution.

**Primary test**
- Chi-square test for independence + standardized residuals.
- Multinomial regression of entity_type on vertical category controlling for location type.

**Falsification criteria**
- Direction reverses (authority more underground than elevated, creatures more elevated than underground) in both holdouts.
- Or: associations vanish once controlling for location type.

---

### H4 — “Constant State / Variable Form” Within MallWorld
**Prediction**
- Across different surface labels (e.g., different location labels within “other”), the *functional signature* remains stable.

**Operationalization**
- Define “functional signature” for a location label as a vector:
  - atmosphere distribution,
  - entity-type mix,
  - interaction mix,
  - outcome rates,
  - transit-mode mix.

**Primary test**
- Cluster labels by semantic name vs cluster by functional signature.
- Measure alignment: adjusted mutual information (AMI) or silhouette.

**Falsification criteria**
- Functional signatures are not stable (high variance) and do not generalize across splits.

---

## 3. Out-of-Sample Prediction Tests (Key Guardrail)

### 3.1 Holdout design
- Split dreams into Train/Validation/Test with fixed seed.
- Additionally, do time-agnostic random splits and “short vs long dream” splits as robustness.

### 3.2 Predictive tasks
- Predict atmosphere category from vertical + location + entity mix.
- Predict success/escape from atmosphere + interaction type + entity demeanor + vertical.

### 3.3 Baselines
- Majority-class baseline.
- “No-vertical” ablation baseline.
- Permuted-vertical negative control (shuffle vertical labels within dreams).

**Decision rule**
- A correspondential feature passes if it improves test-set performance meaningfully over ablations.

---

## 4. Multiple Comparisons + Robustness

- Pre-register primary hypotheses H1–H3.
- Use FDR correction for secondary hypothesis families.
- Report effect sizes (ORs, $\rho$, Cramér’s V) with CIs.
- Sensitivity analyses:
  - exclude mechanically vertical labels (basement/attic) to test “semantic-only” effect
  - re-run with only explicit mentions vs LLM-inferred positions (if available)

---

## 5. Deliverables

1. A single notebook implementing this plan end-to-end.
2. A short report section per hypothesis:
   - **Prediction** → **Test** → **Effect size** → **Holdout replication** → **Falsification status**.
3. A “what the data does NOT show” section listing failed predictions.

---

## 6. Interpretation Rules

- If a prediction holds robustly, it is reported as **statistically supported**.
- Any Swedenborgian mapping language is marked as **reasonable interpretation** unless the test was explicitly pre-registered and replicated.
- Ontological claims are labeled **speculative** regardless of statistical strength.
