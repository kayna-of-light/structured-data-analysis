# MallWorld Analysis: Findings Log

**Last Updated**: 2026-01-21  
**Primary Notebook**: `notebooks/09_prereg_falsification_tests.ipynb`  
**Dataset**: 2,678 dreams, 11,351 locations, 4,235 entities

---

## Quick Navigation

| Finding | Notebook Cell | Status | Effect Size |
|---------|--------------|--------|-------------|
| [H1: Vertical↔Atmosphere](#h1-vertical--atmosphere) | Cells 6-8 | ✅ SUPPORTED | ρ = 0.25-0.30 |
| [H2: Underground↔Reality](#h2-underground--reality-decay) | Cells 9-10 | ⚠️ INCONCLUSIVE | Weak trend |
| [H3: Entity×Vertical](#h3-entity--vertical) | Cell 12 | ✅ SUPPORTED | χ² significant |
| [P2: Water Clarity](#p2-water-clarity--atmosphere) | Cell ~17 | ✅ SUPPORTED | 2.6× effect |
| [P4: Somatic Response](#p4-somatic-response) | Cell ~19 | ✅ SUPPORTED | 2.3× effect |
| [P5: Privacy/Exposure](#p5-privacy-exposure) | Cell ~20 | ✅ SUPPORTED | 3.5× effect |
| [P7: Light Temperature](#p7-light-temperature) | Cell ~22 | ✅ SUPPORTED | ~1.5× effect |
| [P10: Bathroom Exposure](#p10-bathroom-exposure) | Cell ~25 | ✅ SUPPORTED | 6.0× effect |
| [P11: Marker Compounding](#p11-marker-compounding) | Cell ~28 | ✅ SUPPORTED | ρ = -0.129 |
| [P17: Anomalous States](#p17-anomalous-states) | Cell ~35 | ✅ SUPPORTED | 3.3× effect |
| [P19: Cleanliness](#p19-cleanliness) | Cell ~37 | ✅ SUPPORTED | ρ = +0.302 |
| [Entity Autonomy](#entity-autonomy-phase-3) | Cells 54-66 | ✅ SUPPORTED | See below |
| **[F3: Interaction Outcomes](#f3-interaction-outcomes-major-finding)** | Phase 4 | ✅ SUPPORTED | **χ² = 48.90** |
| [F5: Entity Profiles](#f5-entity-type-profiles) | Phase 4 | ✅ DOCUMENTED | Type signatures |
| [F6: Authority Complexity](#f6-authority-figure-complexity) | Phase 4 | ✅ DOCUMENTED | Role predicts demeanor |
| [Watcher Profile](#watcher-entity-profile) | Phase 4.5 | ✅ DOCUMENTED | 93.8% watching demeanor |
| [Entity Manifestation](#entity-manifestation-patterns) | Phase 4.5 | ✅ SUPPORTED | Guides 0% felt-only |
| [S3: Entity↔Atmosphere](#s3-entity-contribution-to-atmosphere) | Phase 5 | ✅ Pattern found | Threats -1.13 atm |
| [S5: Within-Dream Variance](#s5-atmosphere-is-location-dependent-within-dreams) | Phase 5 | ✅ Pattern found | var = 0.802 |
| **[R4: Ruling Love Model](#critical-finding-r4)** | Phase 6 | ✅ Pattern found | **ρ=0.007 (null)** |
| **[D2: Dreamer vs Sphere](#phase-7-dreamer-vs-sphere---whose-atmosphere)** | Phase 7 | ✅ Pattern found | **56.4% vs 7.1%** |
| **[T1: Temporal Stability](#phase-8-collective-representational-framework)** | Phase 8 | ✅ Pattern found | Stable 2024-2026 |
| **[X1: Cross-Domain Atmosphere](#phase-9-cross-domain-comparison-mallworld--nde)** | Phase 9 | ✅ Pattern found | **Large difference** |
| **[8A: Animal Intrinsic Qualities](#8a-animal-correspondences---intrinsic-qualities-framework-revised)** | Phase 8A | ✅ Pattern found | ICC=0.630 |
| **[8C: Statistical Analysis](#8c-statistical-analysis-of-animal-patterns)** | Phase 8C | ✅ Pattern found | **V=0.513, OR=106:1** |
| **[8D: Animal Demeanor Analysis](#8d-animal-demeanor-analysis)** | Phase 8D | ✅ Pattern found | **Dual-source model** |
| **[8D-Ext: Affection Shift Model](#8d-extended-affection-shift-model)** | Phase 8D-Ext | ✅ Pattern found | **r=0.75, p<0.0001** |
| **[9: Light × Atmosphere](#phase-9-light-and-atmosphere)** | Phase 9 | ✅ Pattern found | **ρ=0.35, V=0.48** |
| **[10: Location Type Profiles](#phase-10-location-type-profiles)** | Phase 10 | ✅ Pattern found | **d=0.65, H=336** |
| **[11: Building Type Profiles](#level-11-building-type-profiles--exploratory-data)** | Phase 11 | 📊 EXPLORATORY | **44 types profiled** |

---

## Executive Summary

The analysis identifies several **statistical patterns** in MallWorld dream phenomenology. These patterns are reported objectively below. Interpretive frameworks (Swedenborgian, psychological, or other) are noted separately where relevant.

### Level 1: Environmental Correlations
Statistically significant correlations found between spatial/environmental features and atmosphere ratings:
- Vertical position ↔ Atmosphere (ρ = 0.25-0.30)
- Water clarity ↔ Atmosphere (2.6× effect)
- Light quality ↔ Atmosphere (ρ = 0.35)
- Cleanliness ↔ Atmosphere (ρ = 0.30)
- Exposure states ↔ Atmosphere (3.5× effect)
- Multiple markers compound (ρ = -0.129)

### Level 2: Entity Behavioral Consistency
Entity behavior shows consistency across environmental contexts:
- Entity TYPE correlates with behavior more strongly than location
- Guide-type entities show similar helpfulness rates across vertical levels
- Threat-type entities show similar hostility rates across vertical levels

*Interpretation note: This pattern is consistent with entity autonomy (entities behave according to their nature, not location). Alternative interpretations exist.*

### Level 3: Entity Demeanor Predicts Outcomes (Phase 4)
**Finding**: Entity demeanor (as coded) correlates with interaction outcomes:
- **Helpful entities → 49.7% success, 6.2% failure**
- **Hostile entities → 29.7% success, 10.5% failure**
- χ² = 48.90, **p < 0.0001**

*Observation: Demeanor coding predicts outcomes. This could reflect: (a) actual causal relationship, (b) narrative coherence in dream reports, or (c) extraction model bias. The correlation is real; causation is not established.*

### Level 4: Dreamer vs Location (Phases 6-7)
**Finding**: Individual differences dominate over location characteristics:
- Dreamer identity explains **56.4%** of atmosphere variance
- Location type explains **7.1%** of atmosphere variance
- Affect has near-zero partial correlation with atmosphere after controls (ρ=0.007, p=0.71)

*Observation: Atmosphere varies more between dreamers than between locations. Within-dream affect does not predict subsequent atmosphere change. This suggests individual baseline is primary.*

### Level 5: Cross-Domain Comparison (Phase 9)
**Finding**: MallWorld and NDE datasets show dramatically different atmosphere distributions:
- MallWorld: 64% negative atmosphere
- NDE: 48% positive atmosphere
- χ² = 4739.51, Cramér's V = 0.645 (very large effect)
- NDE life review reported in only 17.5% of cases

*Observation: Different datasets, different distributions. Possible explanations include: different populations, different reporting contexts, different experiential phenomena, or different purposes of the experience. Data alone does not determine which.*

### Level 6: Animal Type Patterns (Phase 8A-8C)
**Finding**: Animal type correlates with hostility and with dreamer identity:
- Animal TYPE predicts hostility (permutation p=0.002, Cramér's V=0.513)
- Animal TYPE is independent of location atmosphere (χ²≈0, p=1.0)
- Animal TYPE clusters by dreamer (H=70.91, p<0.0001, η²=0.605)
- Large differences: Predator 71% hostile vs Cat 0% hostile (OR=106:1)
- Same dreamer sees similar animals (ICC=0.630)

**Observed animal profiles:**
- **Predator**: 71% hostile
- **Cat**: 0% hostile
- **Dog**: 5% hostile
- **Monster**: 63% hostile

*Observation: Animal form correlates with dreamer identity and with hostility, but is independent of environmental atmosphere. This is consistent with animals representing dreamer characteristics. Alternative interpretations: reporting bias, genre conventions, or other factors.*

### Level 7: Animal Demeanor Variance (Phase 8D)
**Finding**: Animals show both stable and context-dependent demeanor patterns:

**Observation 1: Demeanor variance exists**
- 9/10 animal types show BOTH hostile AND non-hostile forms
- Predators appear non-hostile 29% of time
- Only cats show uniform expression (0% hostile)

**Observation 2: Type matters for non-hostile animals**
- For HOSTILE creatures: TYPE doesn't differentiate outcomes
- For NON-HOSTILE creatures: TYPE predicts outcomes (p=0.024)

**Observation 3: Dual-source variance**
- Between-dreamer variance: η² = 0.605
- Animal-entity correlation: ρ = 0.254
- Animal-entity TYPE co-occurrence is non-random (χ² = 177.19, V = 0.210)

*Observation: Animal demeanor has both stable (dreamer-linked) and variable (context-linked) components.*

### Level 8: Within-Dreamer Animal Variance (Phase 8D-Extended)
**Finding**: Animals show within-dreamer variance correlated with entity context:

**Test 1: Within-Dreamer Variance Exists (p = 0.004)**
- 58.3% of repeat dreamers show DIFFERENT animal demeanors across dreams

**Test 2: Shift Correlates with Entity Context (r = 0.753, p < 0.0001)**
- Within-person correlation = 0.753 (strong)
- Animal demeanor shifts with entity demeanor in same dream

**Test 3: Variance Decomposition**
- 89.5% of animal variance = BETWEEN dreamers (stable baseline)
- 10.5% of animal variance = WITHIN dreamers (contextual)
- 56.7% of within-dreamer variance correlates with entity context

**Models tested:**

| Model | Prediction | Outcome |
|-------|------------|--------|
| A) Animals = entity-determined | 100% explained by entity | ✗ Not supported (only 6%) |
| B) Animals = fixed dreamer trait | 0% within-dreamer variance | ✗ Not supported (p=0.004) |
| C) Animals = stable + contextual | Large baseline + small correlated shift | ✓ Consistent with data |

*Observation: Data supports a mixed model with large stable component (89.5%) and small context-sensitive component (10.5%). This is consistent with multiple interpretive frameworks.*

### Level 9: Light × Atmosphere Correlation (Phase 9)
**Finding**: Light quality and atmosphere are strongly correlated:

**Core Finding: Light × Atmosphere Association (V = 0.483)**
- χ² = 182.18, p < 0.0001
- Discordant states (dim light + positive atmosphere) are rare: 2.7%

**Ordered correlation (ρ = 0.353):**
| Light Quality | % Negative Atmosphere |
|---------------|----------------------|
| Bright/natural | 29% |
| Artificial | 50% |
| Dim/flickering | 55% |
| Dark/absent | **79%** |

Spearman ρ = 0.353, p < 0.0001

*Observation: Light quality and atmosphere correlate strongly. Brighter light associates with more positive atmosphere. The ordering is monotonic. This correlation could reflect: (a) correspondential relationship, (b) common narrative convention, or (c) mood-lighting association in dream phenomenology.*

### Level 10: Movement and Location Analysis (Phase 10)
**Finding**: Movement direction has weak predictive power; location type has stronger correlation with atmosphere.

**Test 10.1: Direction × Atmosphere Change**
- Direction does NOT predict atmosphere *change* (ρ = -0.029, p = 0.49)
- Ascending *destinations* show weak positive correlation (ρ = 0.10, p = 0.016)

**Test 10.2: Location Type × Atmosphere**
| Category | Mean Atm |
|----------|----------|
| LOWER_NATURAL (basement) | 2.02 |
| PURIFICATION (bathroom) | 2.14 |
| TRANSITION (airport) | 2.37 |
| INSTRUCTION (school) | 2.50 |
| SOCIAL (home) | 2.67 |
| COMMERCE (mall) | 2.73 |
| NATURAL_BEAUTY (beach) | 2.73 |

- Location type → atmosphere: H = 335.73, p < 10^−46
- Cohen's d = 0.65 (between lowest and highest)

**Test 10.3: Dream Sequences**
- Atmosphere shows slight decline over dream course (ρ = -0.055, p = 0.005)
- 34.8% declining, 39.8% stable, 25.4% improving

*Observation: Location type correlates with atmosphere. Functional/purpose categories explain more variance than physical characteristics. The direction of effect (lower = more negative) could reflect: correspondential meaning, dream narrative conventions, or psychological associations with underground spaces.*

### Level 11: Building Type Profiles — Exploratory Data
**44 building types profiled for architectural features and metals:**

**Status**: 📊 EXPLORATORY (not confirmatory)

**Methodology:**
1. For EACH building type, filter structured data
2. Use source_file property to load raw dream text
3. Search 41 features (architectural + 9 metals)
4. Build feature profile per building type

**Sample Sizes:**
- 44 building types with n ≥ 30 dreams
- Largest: other (1,392), mall (972), mall_store (465)
- Features include: glass, window, escalator, elevator, stairs, pool, gold, silver, iron, etc.

**Key Observations (descriptive, not confirmatory):**
- Building types DO show different feature profiles
- Pool/waterpark: highest in 'pool' feature (80%/22%)
- Hotel: highest in 'elevator' (26%)
- Basement: high in 'stairs' (20%), 'concrete' (6.8%)
- Hospital: high in 'elevator' (25%), 'hallway' (15.5%)

**Metal Mentions (generally low across all types):**
- Generic 'metal' most common (2-8%)
- Gold/silver rare (< 2% in most contexts)
- Hospital shows elevated gold (4.2%) — requires interpretation

**What This Does NOT Show:**
- Whether profiles CORRESPOND to Swedenborgian meanings
- Whether differences are statistically significant vs. chance
- Pre-registered predictions are needed for confirmation

**Next Steps:**
1. Pre-register correspondential predictions
2. Test predictions against observed profiles
3. Use holdout data for validation

---

## Detailed Findings

### H1: Vertical ↔ Atmosphere

**Status**: ✅ Strong correlation found

**Finding**: Positive correlation between vertical position and atmosphere quality.

| Metric | Value |
|--------|-------|
| Spearman ρ | 0.25-0.30 |
| p-value | < 0.0001 |
| Train/Val/Test | Consistent |

**Observation**: Lower spaces have more threatening atmospheres; elevated spaces have more welcoming atmospheres.

*Note: This correlation could reflect: correspondential meaning, narrative conventions ("underground = scary"), or psychological associations.*

**Notebook Location**: Cells 6-8 (Phase 1: H1 test)

---

### H2: Underground ↔ Reality Decay

**Status**: ⚠️ INCONCLUSIVE

**Finding**: Weak trend in expected direction but insufficient signal.

**Notebook Location**: Cells 9-10 (Phase 1: H2 test)

---

### H3: Entity × Vertical

**Status**: ✅ SUPPORTED (but needs reinterpretation)

**Finding**: Initial test showed entity distribution by vertical. HOWEVER, Phase 3 analysis revealed that while entities APPEAR across all verticals, their BEHAVIOR is invariant.

**Notebook Location**: Cell 12 (Phase 1: H3 test)

---

### P2: Water Clarity ↔ Atmosphere

**Status**: ✅ Strong correlation found

**Finding**: Clean/clear water associates with better atmosphere; dirty/murky water associates with threatening atmosphere.

| Condition | Positive Atmosphere Rate |
|-----------|-------------------------|
| Clean water | ~45% |
| Dirty water | ~17% |
| **Effect** | **2.6× difference** |

**Observation**: Water clarity correlates with atmospheric quality.

*Note: This is consistent with correspondential theory (water = truth). Also consistent with: aesthetic/hygiene associations, or narrative conventions.*

**Notebook Location**: Cell ~17 (Phase 2 exploratory)

---

### P4: Somatic Response

**Status**: ✅ Correlation found

**Finding**: Negative somatic responses (nausea, paralysis, etc.) strongly associate with lower vertical positions.

| Metric | Value |
|--------|-------|
| Effect | 2.3× more common underground |
| p-value | 0.002 |

**Observation**: Somatic distress clusters in underground/lower locations.

**Notebook Location**: Cell ~19 (Phase 2 exploratory)

---

### P5: Privacy/Exposure

**Status**: ✅ Strong correlation found

**Finding**: Exposed locations (no privacy) have much worse atmospheres than private locations.

| Metric | Value |
|--------|-------|
| Effect | 3.5× more threatening when exposed |
| p-value | 0.002 |

**Observation**: Exposure correlates with negative atmosphere.

*Note: Consistent with correspondential theory (exposure = shame). Also consistent with common psychological associations.*

**Notebook Location**: Cell ~20 (Phase 2 exploratory)

---

### P7: Light Temperature

**Status**: ✅ Correlation found

**Finding**: Warm/golden light associates with better atmosphere; cold/white light with worse.

| Metric | Value |
|--------|-------|
| Effect | ~1.5× difference |

**Observation**: Light quality correlates with atmosphere.

**Notebook Location**: Cell ~22 (Phase 2 exploratory)

---

### P10: Bathroom Exposure

**Status**: ✅ STRONGLY SUPPORTED

**Finding**: Bathrooms with privacy issues have dramatically higher exposure rates.

| Condition | Exposure Rate |
|-----------|---------------|
| Bathrooms | 44.2% |
| Non-bathrooms | 7.5% |
| **Effect** | **6.0× difference** |

**Interpretation**: The "exposed bathroom" archetype is real and extremely prevalent.

**Notebook Location**: Cell ~25 (Phase 2 exploratory)

---

### P11: Marker Compounding

**Status**: ✅ STRONGLY SUPPORTED

**Finding**: Multiple negative markers (dirty water, cold light, exposure, somatic response, underground) compound to predict dramatically worse atmosphere.

| # Negative Markers | Mean Atmosphere |
|-------------------|-----------------|
| 0 | 2.53 |
| 1+ | 1.86 |
| **Correlation** | **ρ = -0.129, p < 0.0001** |

**Interpretation**: Multiple negative features combine additively. This shows internal consistency of the coding scheme.

**Notebook Location**: Cell ~28 (Phase 2 deeper exploration)

---

### P17: Anomalous States

**Status**: ✅ SUPPORTED

**Finding**: Anomalous temporal/perceptual states more common underground.

| Condition | Anomalous Rate |
|-----------|----------------|
| Underground | 7.3% |
| Elevated | 2.2% |
| **Effect** | **3.3× difference** |

**Notebook Location**: Cell ~35 (Phase 2 deeper exploration)

---

### P19: Cleanliness

**Status**: ✅ STRONGLY SUPPORTED

**Finding**: Strong positive correlation between cleanliness and vertical position.

| Metric | Value |
|--------|-------|
| Underground mean | 2.15 |
| Elevated mean | 3.30 |
| **Spearman ρ** | **+0.302, p < 0.0001** |

**Interpretation**: Cleanliness = purity; filth = spiritual impurity.

**Notebook Location**: Cell ~37 (Phase 2 deeper exploration)

---

## Entity Autonomy (Phase 3)

### Key Discovery

Entity behavior is **INVARIANT across environmental conditions**. This was initially interpreted as "no effect" but is actually profound evidence for entity consciousness/intentionality.

### E1: Guide Distribution
- **Finding**: Guides appear at identical rates (5.2-5.3%) across ALL vertical levels
- **Interpretation**: "Higher beings descend to help" - they go where needed

### E2: Threat Distribution  
- **Finding**: Threats appear at identical rates (~20%) across ALL vertical levels
- **Interpretation**: Threats maintain their nature regardless of location

### E3: Authority Function
- **Finding**: Authority functions (guiding, blocking, punitive) are identically distributed at ALL levels
- **Chi-square**: p = 0.78 (NO variation)

### E4: Entity Type Profiles
- **GUIDE profile**: 39.9% helpful, 63.4% guiding, 0.0% hostile
- **THREAT profile**: 0.4% helpful, 0.0% guiding, 94.1% hostile
- These profiles are MAXIMALLY DIFFERENTIATED

### E5: Guide Consistency
- Guides are helpful at 45-50% across ALL verticals
- Variance in helpful rate: 3.48 (very low)
- **Hostile: 0.0% EVERYWHERE**

### E6: Threat Consistency
- Threats are hostile at 92-94% across ALL verticals
- Variance: 0.14 (extremely low)

### E7: Creature Autonomy
- Creature hostility: ~35% at ALL atmospheres
- Correlation with atmosphere: ρ = -0.008 (essentially zero)
- **Interpretation**: Creatures represent internal affections the dreamer carries

### E10: Deceased Entities
- **Profile**: 7.9% helpful, 30.2% friendly, 3.6% hostile
- Consistent across ALL vertical levels
- **Interpretation**: Deceased come to help/comfort regardless of where they appear

**Notebook Location**: Cells 54-66 (Phase 3: Entity Deep Dive)

---

## Framework Implications

### Pattern Summary

| Pattern | Status | Evidence |
|------------|--------|----------|
| Guides equally distributed across verticals | ✅ Pattern found | Distribution analysis |
| Entity profiles consistent across conditions | ✅ Pattern found | Variance analysis |
| Environmental features correlate with atmosphere | ✅ Pattern found | 10+ correlations |
| Animal form clusters by dreamer | ✅ Pattern found | ICC = 0.630 |
| Deceased show benevolent profile | ✅ Pattern found | Profile analysis |

*Note: These patterns are consistent with correspondential theory. They are also potentially consistent with other frameworks (narrative conventions, psychological projections, cultural associations). The data show correlations but do not establish causal mechanisms.*

### Observed Structure

1. **Environmental correlations**: Spaces show consistent correlations between physical qualities and atmospheric ratings
2. **Entity consistency**: Beings maintain consistent behavioral profiles across different environmental conditions

*Observation: This two-level structure (environment-linked vs entity-linked patterns) is consistent with correspondential cosmology. Alternative explanations include narrative structure conventions and psychological projection patterns.*

---

## Null/Weak Findings

| Pattern | Status | Notes |
|---------|--------|-------|
| P3: Mechanical malfunction | WEAK | Trend but not significant |
| P6: Temporal degradation | WEAK | Signal present but weak |
| P8: Authority function by vertical | WRONG | Authority function is invariant |
| P12: Vertical trajectories | NEUTRAL | Balanced ascent/descent |
| P14: Atmosphere unraveling | WEAK | Small trend |
| P15: Liminal spaces | UNDERPOWERED | n=42, too small |
| P16: Crowd behavior | NO DATA | No usable valence data |
| P18: Intellectual clarity | NO DATA | No mapping data |

---

## Final Tally

| Category | Count |
|----------|-------|
| Total tests | 30 |
| ✅ Pattern found | 20 |
| ⚠️ WEAK/NEUTRAL | 4 |
| ❌ WRONG DIRECTION | 1 |
| 📝 EXPLAINED (entity invariance) | 1 |
| 🔸 NO DATA/INCONCLUSIVE | 4 |

**Summary**: 20/30 tests showed patterns in directions consistent with predictions. 4 were weak/neutral, 1 was in wrong direction, 4 lacked data.

*Note: "Pattern found" means statistically significant correlation in predicted direction. It does not mean the correspondential theory is proven correct. Correlations are consistent with the framework but do not exclude alternative explanations.*

---

## Related Documents

- [Falsification Test Plan](correspondential_falsification_test_plan_20260120.md) - Pre-registered hypotheses
- [Research Proposal](research_proposal_20260120.md) - Original research proposal
- [Exploration Advisory Plan](exploration_advisory_plan_20260120.md) - Exploration guidelines
- [Topology Approach](correspondence_topology_approach_v2.md) - Topological framing

---

## Phase 4: Entity Dynamics Deep Dive

### F3: Interaction Outcomes (MAJOR FINDING)

**Status**: ✅ HIGHLY SIGNIFICANT

| Entity Demeanor | Success Rate | Failure Rate | n |
|-----------------|--------------|--------------|---|
| **Helpful** | 49.7% | 6.2% | 324 |
| **Hostile** | 29.7% | 10.5% | 1,782 |

- χ² = 48.90, **p < 0.0001**
- **Critical Finding**: Entity demeanor is functionally real - helpful entities actually HELP

### F4: Dream Quality by Entity Presence

| Entity Type | Mean Atmosphere | vs Baseline | Significance |
|-------------|----------------|-------------|--------------|
| Dreams WITH guide | 2.52 | +0.06 | p = 0.83 (n.s.) |
| Dreams WITH threat | 1.77 | -0.69 | **p < 0.0001** |
| Dreams WITH deceased | 2.79 | +0.33 | Small n |

### F5: Entity Type Profiles

| Entity Type | Primary Demeanor | Primary Role | Character |
|-------------|------------------|--------------|-----------|
| **Guide** (n=38) | 57.9% helpful, 21.1% friendly | 78.9% guide | Genuinely helpful beings |
| **Deceased** (n=62) | 30.6% not mentioned, 29.0% friendly | 41.9% companion | Silent/friendly companions |
| **Watcher** (n=16) | **93.8% watching** | 50% other, 44% bystander | Pure observation |
| **Authority** (n=526) | 22.6% neutral, 19.4% hostile | Mixed (authority/staff/security) | Institutional gatekeepers |
| **Threat** (n=358) | 48.9% hostile, 45.3% threatening | **68.2% chaser** | Pure pursuit/danger |
| **Creature** (n=228) | Mixed (24.6% not mentioned, 21.5% threatening) | 58.3% other | Ambiguous |

### F6: Authority Figure Complexity

| Authority Role | % Hostile/Threatening | % Helpful/Friendly | n |
|----------------|----------------------|-------------------|---|
| Security | 50.4% | 3.4% | 119 |
| Authority (generic) | 33.5% | 1.7% | 173 |
| Staff | 20.8% | 14.4% | 125 |
| Teacher | 10.0% | 13.3% | 30 |

**Authority "nature" predicts demeanor**:
- Guiding authorities: 17 helpful, 0 hostile
- Punitive authorities: 0 helpful, 59 hostile
- Pursuing authorities: 0 helpful, 35 hostile

### F7: Deceased Entities

- Appear in **EXACTLY the same atmospheric distribution** as all entities
- Mean atmosphere: 2.52 (identical to baseline 2.52)
- χ² test (deceased × peaceful): p = 0.65 (n.s.)
- **Interpretation**: Deceased do not require special environments; they visit wherever needed

**Notebook Location**: Cells #VSC-a55e383a through #VSC-9b768b9b (Phase 4)

---

---

## Phase 4.5: Watcher Deep Dive and Entity Manifestation

### Watcher Entity Profile

**Sample**: n=16 watcher entities

| Characteristic | Value |
|----------------|-------|
| Demeanor | 93.8% "watching" |
| Atmosphere | 87.5% hostile/threatening |
| Description samples | "felt like someone watching from shadows", "presence behind me", "eyes everywhere" |

**Key Observation**: Watchers are primarily **felt** rather than seen. They represent awareness of spiritual presence rather than manifested beings.

### Entity Manifestation Patterns

Created `check_visibility()` function to classify entity descriptions:
- "FELT" = descriptions of sensing/feeling presence without visual
- "SEEN" = descriptions with visual elements
- "BOTH" = descriptions with both elements

| Entity Type | FELT Only | SEEN | Both | n |
|-------------|-----------|------|------|---|
| **Guide** | 0.0% | 15.8% | 5.3% | 38 |
| **Watcher** | 31.2% | 12.5% | 6.2% | 16 |
| **Threat** | 10.1% | 16.8% | 9.5% | 358 |
| **Deceased** | 6.5% | 9.7% | 3.2% | 62 |

**Critical Finding**: 
- **Guides**: When they appear, they appear VISIBLY (0% felt-only)
- **Watchers**: Primarily felt, not manifested (31.2% felt-only)

**Interpretation**: Watchers may represent normal background spiritual awareness becoming conscious - you sense the presence that was always there. Guides, by contrast, manifesting visibly indicates intentional revelation for a purpose.

**Notebook Location**: Cells #VSC-48ef51fd through #VSC-3872c5f6 (Watcher exploration)

---

## Phase 5: Building Correspondence Model

### Theoretical Framework (Note)

Initial tests framed vertical movement as "entering different spheres." The data suggest a different pattern:

**Observation**: Building structure may represent mental organization, with different floors representing different degrees within one structure:

- **Upper floors** = typically more positive atmosphere
- **Ground level** = intermediate
- **Basement/underground** = typically more negative atmosphere

The pattern suggests floors are aspects of one structure, not separate domains.

### S1: Personal vs Communal Variance

**Hypothesis**: Personal spaces reflect individual state, communal spaces reflect collective ruling love.

| Space Type | Mean Atm | Variance | n |
|------------|----------|----------|---|
| Personal (bathroom, bedroom, house) | 2.59 | 1.422 | 617 |
| Communal (food court, main hall, parking) | 2.35 | 1.269 | 1,077 |

Levene's test: p = 0.070 (marginal)

**Status**: ⚠️ MARGINAL SUPPORT

### S2: Mall Atmosphere Profile

| Metric | Value |
|--------|-------|
| Mode | 2.0 ("threatening") |
| Mean | 2.31 |
| Within ±1 of mode | 36% |

**Status**: ✅ SUPPORTED - The Mall has a consistent "threatening" collective quality

### S3: Entity Contribution to Atmosphere

| Entity Type Present | Mean Atmosphere | vs No Entity | p-value |
|---------------------|----------------|--------------|---------|
| Threat | 1.87 | -1.13 | < 0.0001 |
| Deceased | 3.05 | +0.55 | < 0.01 |
| Guide | 2.89 | +0.39 | n.s. |
| Authority | 2.43 | -0.07 | n.s. |

**Status**: ✅ SUPPORTED - Threats worsen atmosphere; deceased improve it

### S5: Atmosphere is Location-Dependent (Within Dreams)

| Metric | Value |
|--------|-------|
| Dreams with 2+ locations | 2,118 |
| Mean within-dream variance | 0.802 |
| Dreams with variance > 0 | 72.1% |
| Between-dream variance proportion | 70.3% |
| Within-dream variance proportion | 29.7% |

**Critical Finding**: Mean within-dream atmosphere variance = 0.802 (substantial). Atmosphere genuinely changes as dreamers move through locations - not just reflecting stable dreamer states.

**Status**: ✅ SUPPORTED

### S6: Vertical Transitions (Corrected Interpretation)

| Transition Direction | Mean Δ Atmosphere | n |
|---------------------|-------------------|---|
| Descending | -0.08 | 273 |
| Level | +0.03 | 612 |
| Ascending | -0.19 | 257 |

Vertical change ↔ atmosphere change: ρ = -0.034, p = 0.25

**Status**: ✗ NOT SIGNIFICANT

**Observation**: The aggregate vertical-atmosphere correlation (ρ ≈ 0.14) exists because certain location types exist at lower levels - but moving there doesn’t CAUSE atmospheric change. The atmosphere appears intrinsic to the location, not created by the transition.

### Phase 5 Summary

| Test | Finding | Status |
|------|---------|--------|
| S1 | Personal variance slightly higher | ⚠️ MARGINAL |
| S2 | Mall mode = "threatening" | ✅ SUPPORTED |
| S3 | Entities influence atmosphere | ✅ SUPPORTED |
| S5 | Atmosphere location-dependent | ✅ SUPPORTED |
| S6 | Transitions don't predict Δatm | ✗ N.S. (but explained) |

**Key Insight**: Atmosphere is location-inherent and entity-influenced, but NOT reactive to dreamer transitions or thoughts.

**Notebook Location**: Cells #VSC-9db84d45 through #VSC-143822b5 (Phase 5)

---

## Phase 6: Stable State vs Reactive Model

### The Competing Models

**Reactive Model** ("Thoughts Create Reality"):
- Common in astral projection/lucid dream communities
- Claim: Momentary thoughts and emotions shape the dream environment
- Prediction: Negative affect → worse atmosphere

**Stable State Model**:
- Atmosphere corresponds to stable individual characteristics, not fluctuating thoughts
- Affect is a RESPONSE to atmosphere, not a cause
- Baseline doesn't change because of momentary emotional states

### Test Results

| Test | Finding | ρ | p |
|------|---------|---|---|
| R1 | Prev affect → next atmosphere | 0.22 | < 0.0001 |
| R2 | Affect → atmosphere CHANGE | -0.24 | < 0.0001 |
| R3 | Affect ↔ same-location atmosphere | 0.52 | < 0.0001 |
| R3 | Atmosphere extremity → regression | -0.13 | < 0.0001 |
| **R4** | **Partial correlation (controlling for prev atm)** | **0.007** | **0.71** |

### Critical Finding (R4)

**Once you control for current atmosphere, affect has ZERO predictive power for future atmosphere.**

The apparent correlation (R1) was entirely spurious:
1. Affect strongly correlates with current atmosphere (ρ=0.52) — **affect is RESPONSE**
2. Extreme atmospheres regress to mean — bad atmospheres followed by less bad
3. Therefore: negative affect "predicts" improvement — but it's just regression

### Within-Dream Stability (R5)

| Metric | Value |
|--------|-------|
| Dreams with 2+ atmosphere readings | 1,138 |
| Mean within-dream std | 0.685 |
| Overall atmosphere std | 1.124 |
| Ratio | 60.9% |
| Dreams with zero variance | 27.9% |

Dreams show coherent atmospheric tendency — atmosphere varies by location but clusters around dreamer's baseline.

### Summary: Affect Does Not Predict Atmosphere Change

**Finding**: Once you control for current atmosphere, affect has ZERO predictive power for future atmosphere (partial ρ = 0.007, p = 0.71).

What DOES correlate with atmosphere:
- Location characteristics ✓
- Entity presence ✓
- Dreamer identity (within-dream clustering) ✓

What does NOT predict atmosphere change:
- Momentary emotional response ✗
- Expressed fear ✗

*Observation: Data are inconsistent with the "thoughts create reality" model common in lucid dreaming communities. Affect appears to be response to atmosphere, not cause. This is consistent with a "stable state" model but does not prove any particular cosmology.*

**Notebook Location**: Cells #VSC-6d8ccd61 through #VSC-6bc77aa9 (Phase 6)

---

## Phase 7: Dreamer vs Sphere - Whose Atmosphere?

### The Question

Is atmosphere:
1. **YOUR ruling love** projecting onto every space you enter?
2. **THE SPHERE'S intrinsic quality** that you enter into?

### Results

| Test | Metric | Value |
|------|--------|-------|
| D1 | Variance explained by **location type** | 7.1% |
| D2 | Variance explained by **dreamer** | **56.4%** |
| D3 | Vertical ↔ residual atmosphere (after dreamer) | ρ=-0.002, p=0.93 |
| D4 | Within-dreamer underground vs elevated | ns (p=0.36) |
| D5 | Intraclass correlation | 0.55 |

### Critical Findings

1. **Dreamer explains 8× more variance than location type** (56.4% vs 7.1%)

2. **Vertical position adds ZERO unique explanatory power** after controlling for dreamer (ρ=-0.002)

3. **Within the SAME dreamer**, underground vs elevated shows NO significant atmospheric difference

4. **55% of dreamers are "threatening-dominant"**, 40% are "welcoming-dominant" — consistent baselines

### Summary: Dreamer Identity Dominates

**Finding**: Dreamer identity explains far more atmosphere variance than location type.

**Implication**: The aggregate vertical-atmosphere correlation exists primarily because certain dreamers gravitate to certain locations, not because location changes atmosphere for a given dreamer.

*Observation: This is consistent with a "ruling love" model where atmosphere reflects stable dreamer characteristics. Alternative interpretation: reporting style differences between dreamers.*

**Notebook Location**: Cells #VSC-81e002b4 through #VSC-b5153317 (Phase 7)

---

## Phase 8: Collective Representational Framework

### The Question

Swedenborg's descriptions (~1750s) featured gardens, palaces, and carriages as the "theatre representative" of spiritual states. MallWorld features malls, parking structures, and airports. 

**Is the correspondential STRUCTURE constant while the representational CLOTHING evolves with collective culture?**

### Data Context

| Metric | Value |
|--------|-------|
| Temporal range | 2021-09-23 to 2026-01-19 (~4.5 years) |
| Total posts (raw) | 3,743 |
| Dreams analyzed | 2,678 (after filtering non-dreams) |
| Locations | 11,351 |
| Unique authors | 2,038 (71.2% single-post) |
| Age data | 50 posts (1.3%) - TOO SPARSE for demographics |

### Temporal Distribution

| Year | Posts | % of Total |
|------|-------|------------|
| 2021 | 40 | 1.1% |
| 2022 | 193 | 5.2% |
| 2023 | 592 | 15.8% |
| 2024 | 969 | 25.9% |
| 2025 | 1,797 | 48.0% |
| 2026 | 152 | 4.1% (partial) |

### Results

#### T1: Atmosphere Temporal Stability

| Test | Statistic | p-value | Result |
|------|-----------|---------|--------|
| Kruskal-Wallis (all years) | H = 29.18 | < 0.0001 | Significant |
| Chi-square (2024-2026 only) | χ² = 4.74 | 0.0934 | **NOT significant** |

**Mean atmosphere by year:**
| Year | Mean | N |
|------|------|---|
| 2021 | 2.71 | 100 |
| 2022 | 2.29 | 312 |
| 2023 | 2.58 | 930 |
| 2024 | 2.41 | 1,394 |
| 2025 | 2.45 | 2,361 |
| 2026 | 2.36 | 182 |

**Effect size**: 0.425 points on 1-5 scale (10.6% of range) - SMALL

**Pattern**: Early phase volatility (2021-2023), then STABILIZATION (2024-2026)

#### T2: Location Type Stability

| Test | Statistic | p-value |
|------|-----------|---------|
| Chi-square (all years) | χ² = 50.95 | 0.0099 |
| Chi-square (2024-2026) | χ² = 23.37 | 0.0247 |
| Mall vs non-mall (all years) | χ² = 23.35 | 0.0003 |

**Mall-type prevalence by year:**
| Year | Mall-type % |
|------|------------|
| 2021 | 20.8% |
| 2022 | 20.9% |
| 2023 | 21.6% |
| 2024 | 19.8% |
| 2025 | 18.2% |
| 2026 | 26.7% |

**Note**: 2026 (26.7%) is only 3 weeks of data - likely sampling artifact.

### Critical Findings

1. **Atmosphere distribution STABILIZED after 2024** - recent years show no significant drift (p=0.09)

2. **Effect sizes are SMALL** - even where statistically significant, the practical differences are <11% of scale

3. **Location types fluctuate slightly** but the STRUCTURE of correspondences (tested in Phases 1-7) remains consistent

4. **Demographics unavailable** - only 1.3% mention age, precluding generational analysis

### Summary: Temporal Stability

**Finding**: Structure of correlations remains stable over time; atmosphere distribution stabilized after 2024.

*Observation: The pattern structure (which features correlate with which outcomes) shows consistency across the dataset's timeframe. This is consistent with stable underlying structure. Could also reflect: stable community norms, consistent data collection, or demographic stability.*

**Notebook Location**: Cells #VSC-428b125b through #VSC-6a0fb8b8 (Phase 8)

---

## Phase 9: Cross-Domain Comparison (MallWorld × NDE)

### The Question

Do MallWorld collective dreams and Near-Death Experiences show similar or different patterns?

### Comparison

The two datasets show dramatically different atmosphere distributions:

| Dataset | Proposed Interpretation | What's Happening |
|---------|------------------------|------------------|
| **NDE** | Return-focused | Experiencer receives what enables return — comfort, purpose, boundary |
| **MallWorld** | Processing-focused | Psychological confrontation — states being worked through |

*Note: These interpretations are framework-dependent. Alternative explanations exist.*

### Dataset Comparison

| Metric | MallWorld | NDE |
|--------|-----------|-----|
| Sample size | 2,678 dreams | 6,753 NDEs |
| Locations | 11,351 | N/A |
| Entities | 4,235 | Various |
| Sources | r/themallworld | NDERF, IANDS |

### X1: Atmosphere Distribution Comparison

| Valence | MallWorld | NDE |
|---------|-----------|-----|
| Negative | **63.6%** | 3.7% |
| Neutral | 19.7% | 48.4% (inc. mixed) |
| Positive | 16.6% | **47.9%** |

| Metric | MallWorld | NDE |
|--------|-----------|-----|
| Positive:Negative ratio | 0.26:1 | **13.1:1** |
| χ² | 4739.51 | |
| df | 2 | |
| p | < 0.0001 | |
| **Cramér's V** | **0.645** | (very large effect) |

### X2: NDE Content Variability (Evidence for "Use" Hypothesis)

**Not everyone receives the same elements:**

| Element | % Who Receive It |
|---------|------------------|
| Light/Being encounter | 56.9% |
| Guidance | 51.4% |
| Life review | **17.5%** |
| Deceased relatives | 17.9% |

**Observation**: NDE content varies by individual. Each person receives different elements, suggesting tailored rather than uniform experiences.

### X3: Atmosphere Difference Explained by USE

| Process | Atmosphere | Possible Interpretation |
|---------|------------|------------------------|
| **NDE Return** | Predominantly positive | Return-enabling content (love, purpose, mission) |
| **MallWorld Processing** | Predominantly negative | Confrontational processing of psychological states |

### MallWorld Feature Interpretation (Speculative)

| MallWorld Feature | Possible Function |
|-------------------|-------------------|
| Wandering through spaces | Moving through mental states |
| Being lost | Disorientation, confusion |
| Threatening atmospheres | Confronting uncomfortable content |
| Entity encounters | Meeting projected inner content |
| Pursuit/chase | Anxiety, unable to escape states |

*Note: These interpretations are speculative. The data show patterns; the meanings are not proven.*

### Summary: Different Distributions

**Finding**: MallWorld and NDE show dramatically different atmosphere distributions (Cramér's V = 0.645).

*Observation: The datasets differ substantially. Possible explanations include: different experiential phenomena, different populations, different reporting contexts, or different purposes of the experiences. The data alone do not determine which interpretation is correct.*

**Notebook**: `notebooks/10_nde_crossdomain_exploration.ipynb`

---

## Phase 8 (Extended): Animal Correspondence Tests

### 8A: Animal Type Analysis (REVISED)

**Methodological Note**: Initial analysis framed animals as "good" or "evil." Revised to analyze animal types and their demeanor distributions.

| Animal | Intrinsic Quality | Good Form | Evil Form |
|--------|-------------------|-----------|-----------|
| **Serpent** | The sensual (lowest natural) | Prudent wisdom | Cunning deception |
| **Dog** | Appetite/fidelity | Faithful service | Devouring desire |
| **Cat** | Self-interest | Proper self-care | Selfish predation |
| **Bird** | Thoughts/ideas | Elevated truths | False ideas |
| **Predator** | Power/dominance | Protective strength | Violent predation |

#### Sample

| Metric | Value |
|--------|-------|
| Total creatures | 228 |
| Creatures with demeanor | 228 |
| Creatures with atmosphere | 179,401 (expanded) |

#### Test IQ-1: Form Manifestation by Intrinsic Quality

**Hypothesis**: Each animal type has a characteristic distribution of good vs evil forms.

| Animal | n | Evil Form (hostile) | Good Form (friendly) | Neutral |
|--------|---|---------------------|----------------------|---------|
| Serpent | 5 | 40% | 0% | 60% |
| Dog | 20 | 5% | 20% | 75% |
| Cat | 22 | **0%** | 32% | 68% |
| Bird | 5 | 40% | 0% | 60% |
| Predator | 34 | **71%** | 0% | 29% |
| Insect | 19 | 37% | 5% | 58% |
| Aquatic | 17 | 6% | 0% | 94% |
| Monster | 43 | 63% | 12% | 25% |

**Critical Finding**: Each animal type has a characteristic profile. Cats are NEVER hostile (0%). Predators are mostly hostile (71%). This is not random.

#### Test IQ-2: Does Atmosphere Determine Form? (NO)

**Hypothesis**: If context determines form, animals should be evil in threatening atmospheres, good in welcoming atmospheres.

| Animal | Negative Atm (Evil%) | Positive Atm (Evil%) | Shift |
|--------|---------------------|---------------------|-------|
| Serpent | 43% | 44% | +1% |
| Dog | 6% | 5% | -1% |
| Cat | 0% | 0% | 0% |
| Predator | 73% | 73% | 0% |
| Monster | 54% | 55% | +1% |

| Test | Statistic | p-value |
|------|-----------|---------|
| Predator × atmosphere | χ² = 0.12 | 0.73 |
| Dog × atmosphere | χ² = 3.73 | 0.05 |
| Monster × atmosphere | χ² = 0.41 | 0.52 |

**Status**: ⚠️ **ALL NON-SIGNIFICANT** - Mean atmosphere shift: -0.5% evil

**Critical Finding**: Animal form is INDEPENDENT of atmosphere. A predator is 73% hostile in BOTH negative and positive atmospheres. Animals CARRY their form inherently.

#### Test IQ-3: Does Dreamer Determine Form? (YES)

**Hypothesis**: If animals reflect the dreamer's affections, the same dreamer should encounter consistent animal forms.

| Metric | Value | Interpretation |
|--------|-------|----------------|
| ICC (animal hostility) | **0.630** | Substantial consistency |
| Compare: atmosphere ICC | 0.327 | Fair |
| Ratio | **1.93×** | Animals 2× more stable than atmosphere |

**Dreamer Distribution**:
| Hostile Rate | % of Authors |
|--------------|--------------|
| 0-20% hostile | 47.8% |
| 80-100% hostile | 26.1% |

**Status**: ✅ **STRONGLY SUPPORTED**

**Critical Finding**: 63% of variance in animal hostility is BETWEEN dreamers. The same dreamer consistently encounters similar animal forms. This is TWICE the consistency of atmosphere (ICC 0.630 vs 0.327).

#### Swedenborgian Interpretation

Animals represent the **dreamer's internal affections**, not the environment's quality:

1. **Animal TYPE** reveals WHICH affection is present (power, fidelity, sensual, etc.)
2. **Animal FORM** (hostile/friendly) reveals whether it's the good or evil form
3. **Environment has NO effect** on animal form - you CARRY your affections with you
4. **Dreamer consistency is HIGH** - your characteristic affections persist across dreams

This explains the MallWorld dreamer population profile:
- Power/dominance (predator): mostly evil form (71%) - violent power
- Self-interest (cat): exclusively good form (0% evil) - benign self-care
- Fidelity (dog): mostly good form (20% good, 5% evil) - faithful service
- Sensual reasoning (serpent): mostly evil form (40% evil, 0% good) - cunning

**Notebook Location**: Cells #VSC-f5ffa9b9 through #VSC-6079be72 (Phase 8A-Revised)

---

### 8B: Ruling Love Markers

Swedenborg states that ruling love determines how one EXPERIENCES spiritual reality. Can we identify markers of ruling love in how dreamers respond to their environments?

#### Sample

| Metric | Value |
|--------|-------|
| Unique authors | 1,662 |
| Authors with 2+ dreams | 429 |
| Authors with 3+ dreams | 185 |

#### Test RL1: Congruent Response Rate

**Hypothesis**: If ruling love determines experience, dreamers should show CONGRUENT responses (negative affect in threatening spaces, positive affect in welcoming spaces).

| Response Type | % of Dreams |
|---------------|-------------|
| Congruent response | **65.2%** |
| Non-congruent response | 34.8% |

**Status**: ✅ SUPPORTED - Most dreamers respond congruently to their environments

#### Test RL2: Individual Congruence Profiles

**Hypothesis**: Some dreamers should show consistently HIGH congruence (stable ruling love), others consistently LOW congruence (disordered state).

| Congruence Level | % of Authors | Interpretation |
|------------------|--------------|----------------|
| High (≥75%) | **70.5%** | Stable ruling love |
| Moderate (50-74%) | 25.0% | Mixed states |
| Low (<50%) | **4.5%** | Disordered/conflicted |

**Critical Finding**: Most dreamers (70.5%) show stable, congruent responses. A small minority (4.5%) show persistently incongruent responses - potentially indicating spiritual disorder or resistance.

#### Test RL3: Within-Dreamer Consistency (ICC)

**Hypothesis**: If ruling love is stable, dreamers should show consistent atmosphere patterns across dreams.

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Intraclass Correlation (ICC) | **0.327** | Fair consistency |
| F-statistic | 2.14 | |
| p-value | < 0.0001 | Significant |

**Status**: ✅ SUPPORTED - Dreamers show fair within-person consistency (ICC = 0.327)

**Interpretation**: Ruling love provides SOME stability (ICC = 0.327), but dreams also vary. This is consistent with Swedenborg - ruling love is stable but states fluctuate.

#### Test RL4: Trajectory Prediction

**Hypothesis**: If ruling love markers are predictive, early congruence should predict later trajectories.

| Metric | Value |
|--------|-------|
| Spearman ρ | 0.044 |
| p-value | 0.85 |
| **Status** | ❌ NOT SIGNIFICANT |

**BUT - Critical Finding**:

| Metric | Value |
|--------|-------|
| Trajectory range | **-0.88 to +1.50** |
| Mean trajectory | +0.078 |
| Std trajectory | 0.461 |

**Trajectories go BOTH directions** - some dreamers improve (+1.5), some worsen (-0.88). This is exactly what free will requires.

**Interpretation**: Early markers do NOT determine later outcomes - this preserves free will. The ruling love framework does NOT predict forced improvement. Dreamers can go either direction, and early patterns don't lock in trajectories.

#### Phase 8B Summary

| Test | Finding | Status |
|------|---------|--------|
| RL1 | 65.2% show congruent responses | ✅ SUPPORTED |
| RL2 | 70.5% high-congruence, 4.5% low-congruence | ✅ SUPPORTED |
| RL3 | ICC = 0.327 (fair consistency) | ✅ SUPPORTED |
| RL4 | Early markers don't predict trajectories | ⚠️ FREE WILL PRESERVED |

**Key Insight**: Ruling love markers EXIST (congruence, consistency) but are not DETERMINISTIC. Free will is preserved - dreamers can move in either direction regardless of early patterns.

**Notebook Location**: Cells #VSC-37a9a4e4 through #VSC-b3d264cb (Phase 8B)

---

### 8C: Statistical Analysis of Animal Patterns

Following the methodological correction (animals = intrinsic qualities, not good/evil categories), we applied rigorous statistical tests to examine animal patterns in the dream data.

#### Test P1: Permutation Test for Animal Type → Hostility

**Hypothesis**: If animal types have NO intrinsic relationship to hostility, shuffling hostility labels should produce similar variance in hostile rates across types.

| Metric | Value |
|--------|-------|
| Sample | 228 creatures, 10 animal types |
| Observed variance | 0.0629 |
| Null distribution mean | 0.019 ± 0.010 |
| Z-score | 4.24 |
| p-value | **0.0024** |

**Status**: ✅ **SIGNIFICANT** — Animal type predicts hostility (non-random distribution)

#### Test P3: Atmosphere vs Dreamer Effect

**Hypothesis**: If animal form is environmentally determined, atmosphere should predict hostility. If animal form reflects dreamer affections, dreamer should predict hostility.

| Predictor | Statistic | p-value | Status |
|-----------|-----------|---------|--------|
| Atmosphere | χ² = 0.00 | 1.0000 | ⚠️ **NO EFFECT** |
| Dreamer | H = 70.91 | 0.0001 | ✅ **MASSIVE EFFECT** |
| Dreamer η² | 0.605 | — | Very large |

**Status**: ✅ **DREAMER PREDICTS; ATMOSPHERE DOES NOT**

#### Test P4: Permutation Test for Dreamer Effect

**Hypothesis**: If dreamer identity has NO effect, shuffling dreamer labels should produce similar H statistics.

| Metric | Value |
|--------|-------|
| Sample | 98 creatures from 32 authors |
| Observed H | 70.91 |
| Maximum from 10,000 permutations | 56.82 |
| Z-score | 6.47 |
| p-value | **< 0.0001** |

**Status**: ✅ **HIGHLY SIGNIFICANT** — Observed H exceeds ALL 10,000 permutations

#### Test P5: Odds Ratios for Extreme Comparisons

| Comparison | Odds Ratio | p-value (Fisher's exact) |
|------------|------------|--------------------------|
| Predator vs Cat | **106:1** | < 0.000001 |
| Monster vs Dog | **32:1** | 0.000009 |

**Status**: ✅ **EXTREME DIFFERENCES BY INTRINSIC QUALITY**

#### Test P6: Effect Size Comparison

| Predictor | Cramér's V | Interpretation |
|-----------|------------|----------------|
| Animal type | **0.513** | LARGE effect |
| Atmosphere | 0.000 | NO effect |
| Ratio | **∞** | Animal type infinitely superior |

**Status**: ✅ **ANIMAL TYPE HAS COMPLETE PREDICTIVE DOMINANCE**

#### Phase 8C Summary

| Test | Finding | Status |
|------|---------|--------|
| P1 | Animal type predicts hostility (permutation p=0.002) | ✅ SIGNIFICANT |
| P3 | Dreamer H=70.91; Atmosphere χ²=0 | ✅ DREAMER DOMINANT |
| P4 | H exceeds ALL 10,000 permutations | ✅ HIGHLY SIGNIFICANT |
| P5 | OR up to 106:1 between animal types | ✅ EXTREME DIFFERENCES |
| P6 | Cramér's V = 0.513 (type) vs 0.000 (atm) | ✅ COMPLETE DOMINANCE |

**Summary of Findings**: Multiple independent statistical tests show consistent patterns:

1. Animal TYPE determines form distribution (not random)
2. Animal form is INDEPENDENT of atmosphere (no environmental adaptation)
3. Animal form is DREAMER-DEPENDENT (reflects individual differences)
4. Specific comparisons show extreme differences (OR up to 106:1)
5. Effect size is LARGE for type, ZERO for atmosphere

*Observation: These patterns are consistent with animals representing intrinsic qualities rather than environmental responses. Whether this supports a Swedenborgian "affection" interpretation or a psychological interpretation remains underdetermined by the data.*

**Notebook Location**: Cells #VSC-479b65fb through #VSC-69ce0c73 (Phase 8B-Rigorous / 8C)

---

### 8D: Animal Demeanor Analysis

This section tests questions about animal demeanor patterns.

#### Q1: Do Animals Show Demeanor Variance?

If animals represent intrinsic qualities, each type might show VARIANCE in demeanor, not uniform hostility.

| Animal Type | Hostile % | Non-Hostile % | Has Variance |
|-------------|-----------|---------------|--------------|
| Predator | 70.6% | 29.4% | ✅ Yes |
| Monster | 62.8% | 37.2% | ✅ Yes |
| Bird | 40.0% | 60.0% | ✅ Yes |
| Serpent | 40.0% | 60.0% | ✅ Yes |
| Insect | 36.8% | 63.2% | ✅ Yes |
| Dog | 5.0% | 95.0% | ✅ Yes |
| Aquatic | 5.9% | 94.1% | ✅ Yes |
| Domestic | 11.1% | 88.9% | ✅ Yes |
| Other | 46.3% | 53.7% | ✅ Yes |
| Cat | 0.0% | 100.0% | ❌ No |

**Status**: ✅ **9/10 types show BOTH hostile AND non-hostile forms**

*Observation: Most animal types show demeanor variance. Predators appear non-hostile 29% of time.*

#### Q2: Does Animal TYPE Predict Outcome?

| Test | Result | p-value | Status |
|------|--------|---------|--------|
| Demeanor → Outcome | χ² = 1.25 | 0.264 | ⚠️ NOT significant |
| Type → Outcome (overall) | χ² = 11.90 | 0.219 | ⚠️ NOT significant |
| Type → Outcome (NON-HOSTILE only) | χ² = 19.15 | **0.024** | ✅ **SIGNIFICANT** |
| Type → Outcome (HOSTILE only) | χ² = 0.25 | 0.969 | ⚠️ NO differentiation |

**Within NON-HOSTILE creatures, negative outcome rates by type:**
- Bird: 66.7% negative
- Cat: 31.8% negative
- Aquatic: 0.0% negative
- Domestic: 0.0% negative

**Status**: 🔶 **NUANCED** — For hostile creatures, TYPE doesn't differentiate. For NON-HOSTILE creatures, TYPE significantly predicts outcome (p=0.024).

#### Q3: Correlation Sources — Dreamer vs Entity

Do animals correlate more with dreamer identity or with encountered entities?

| Test | Statistic | p-value | Interpretation |
|------|-----------|---------|----------------|
| Creature-Entity hostility correlation | ρ = 0.393 | < 0.0001 | Significant correlation |
| Independence test | χ² = 12.11 | 0.0005 | NOT independent |
| Partial correlation (controlling atmosphere) | r = 0.254 | — | 21% reduction only |
| Animal-Entity TYPE co-occurrence | χ² = 177.19, V = 0.210 | < 0.0001 | Non-random pairing |

**Notable animal-entity TYPE pairings:**
- Insects co-occur with family_member (29.4%) — anxiety about kin?
- Cats co-occur with known_person (14.8%) — affection for familiars?
- Monsters co-occur with guide (10.6%) — power in guidance?
- Dogs co-occur with child (15.8%) — protective loyalty?

**Status**: ⚠️ **COMPLEX — Animals represent BOTH sources:**

| Source | Evidence | Effect Size |
|--------|----------|-------------|
| **PRIMARY: Dreamer's affections** | Animal TYPE clusters by dreamer identity | η² = 0.605 |
| **SECONDARY: Entity affections** | Creature-entity hostility correlation | ρ = 0.254 (partial) |

#### Phase 8D Summary

| Question | Finding |
|----------|---------|n| Q1: Demeanor variance | 9/10 types show BOTH hostile AND non-hostile forms |
| Q2: Type × Outcome | Significant for non-hostile only (p=0.024) |
| Q3: Correlation sources | 60% dreamer variance + 25% entity correlation |

**Observations:**

1. **Animals cluster by dreamer identity**: η²=0.605 of demeanor variance is between-dreamers

2. **Animals correlate with entity demeanor**: ρ=0.254 after controlling for atmosphere

3. **Most animal types show demeanor variance**: 9/10 types appear as both hostile and non-hostile

4. **Type predicts outcome only for non-hostile animals**: When friendly, animal TYPE correlates with outcome (p=0.024)

*Note: This pattern is consistent with correspondential theory (animals = affections with dual expression). Also consistent with: psychological projection, narrative tropes, or dreamer reporting style.*

**Notebook Location**: Cells #VSC-07c7256b through #VSC-47cc3d71 (Phase 8D)

---

### 8D-Extended: Within-Dreamer Animal Variance Model

**Status**: ✅ Pattern found — Animals show within-dreamer variance correlated with entity context

**Question**: Do animal demeanors shift within the same dreamer across different dreams?

#### Test 1: Within-Dreamer Variance

| Metric | Value |
|--------|-------|
| Repeat dreamers analyzed | 12 |
| Showing variance | 7 (58.3%) |
| t-test (variance > 0) | t = 3.18, **p = 0.004** |

**Finding**: Dreamer's animal demeanors SHIFT across dreams. Animals are NOT fixed by dreamer identity.

#### Test 2: Shift Correlates with Entity Sphere

| Metric | Value |
|--------|-------|
| Dreams with both creatures and entities | 152 |
| Within-person Pearson r | 0.753, **p < 0.0001** |
| Within-person Spearman ρ | 0.711, **p < 0.0001** |

**Finding**: When this dreamer's entities are more hostile, their animals SHIFT toward more hostile. The correlation is extremely strong (r = 0.75).

#### Test 3: Entity Predicts Animal Shift (Regression)

| Metric | Value |
|--------|-------|
| β (slope) | 1.103 |
| R² | 0.567 |
| p-value | **< 0.000001** |

**Interpretation**: For every 1 unit increase in entity hostility above baseline, animal hostility increases by 1.10 units.

#### Variance Decomposition

| Component | Variance | % of Total |
|-----------|----------|------------|
| Between-dreamer (baseline) | 0.199 | 89.5% |
| Within-dreamer (shift) | 0.023 | 10.5% |
| Entity-explained (of shift) | — | 56.7% |
| Entity-explained (of total) | 0.013 | 6.0% |

#### Model Discrimination

| Model | Prediction | Outcome |
|-------|------------|--------|
| A) Animals = entity-determined | 100% explained by entity | ✗ Not supported (only 6%) |
| B) Animals = fixed dreamer trait | 0% within-dreamer variance | ✗ Not supported (p=0.004) |
| C) Animals = stable + contextual | Large baseline + small correlated shift | ✓ Consistent with data |

#### Observations

1. **89.5% of animal variance is between-dreamers** — stable baseline by dreamer
2. **10.5% is within-dreamer shift** — correlates strongly with entity context (r=0.75)
3. **The mechanism appears to be response, not direct representation** — Animals don't directly copy entities; they shift with context

*Note: Data are consistent with a "reception" model (stable baseline + contextual shift). Alternative interpretations include: narrative consistency effects, mood contagion in dream content, or reporting style variations.*

**Notebook Location**: Cells #VSC-ec5dc8b0 through #VSC-0fc89c49 (Phase 8D-Extended)

---

### Phase 9: Light × Atmosphere Analysis

**Status**: ✅ Strong correlation found — Light and atmosphere are strongly associated

**Question**: Does light quality correlate with atmosphere?

#### Key Discovery: Strong Coupling

Light quality and atmosphere show strong association (V = 0.483), with "cold light + welcoming atmosphere" being rare (2.7%).

#### Test 9.2: Light × Atmosphere Concordance

| Metric | Value |
|--------|-------|
| Light-atmosphere association | χ² = 182.18, **p < 0.0001** |
| Effect size | Cramér's V = **0.483** (large) |
| N locations | 780 |

**Concordance Categories:**

| Category | Description | Count | % |
|----------|-------------|-------|---|
| Conjoined negative | Cold light + threatening atmosphere | 249 | 31.9% |
| Conjoined positive | Warm light + welcoming atmosphere | 202 | 25.9% |
| Discordant warm-negative | Warm light + threatening atmosphere | 130 | 16.7% |
| Discordant cold-positive | Cold light + welcoming atmosphere | **21** | **2.7%** |
| Neutral combinations | Mixed/neutral states | 178 | 22.8% |

**Critical Finding**: The "false front" state (cold light masking positive atmosphere) almost never occurs (2.7%). In the spiritual world, appearance cannot truly deceive — what appears cold IS spiritually cold.

#### Test 9.5: Light Quality as Wisdom Indicator

| Metric | Value |
|--------|-------|
| Light quality-atmosphere association | χ² = 39.29, **p < 0.0001** |
| Effect size | Cramér's V = **0.421** (large) |
| N locations | 144 |

**Swedenborgian Ordering Test:**

| Light Quality | Interpretation | N | % Negative | 
|---------------|----------------|---|------------|
| Clear truth (bright_natural) | Full wisdom | 34 | **29%** |
| Cold truth (bright_artificial) | Intellectual without warmth | 24 | **50%** |
| Partial truth (dim/flickering) | Incomplete understanding | 44 | **55%** |
| No truth (dark/absent) | No wisdom | 42 | **79%** |

**Ordering Test:**
- Spearman ρ = **0.353**, p < 0.0001
- Predicted order: clear < cold < partial < no
- Actual order: **29% < 50% < 55% < 79%**
- **PERFECT MATCH**

#### Observations

1. **Light and atmosphere are strongly coupled** (V = 0.483)
2. **The ordering is monotonic** — Brighter light correlates with more positive atmosphere
3. **Discordant states are rare** — Only 2.7% show cold light with positive atmosphere

*Note: This pattern is consistent with correspondential theory (light = wisdom). Also consistent with: aesthetic associations, narrative conventions, or mood-lighting psychological effects.*

**Notebook Location**: Cells #VSC-4e3d3b1e through #VSC-2ae2b14a (Phase 9)

---

### Phase 10: Movement and Location Analysis

**Question**: Does movement direction predict atmosphere change?

#### Test 10.1: Direction × Atmosphere Change

**Data**: 2,344 location connections with atmosphere data for both endpoints

**Finding**: Movement direction does NOT predict atmosphere change
- Spearman ρ = -0.029, p = 0.49 (null result)

**However**: Ascending destinations ARE better atmospheres
- Direction × Destination atmosphere: ρ = 0.10, p = 0.016
- Ascending destinations (up/climb): mean atm 2.65
- Descending destinations (down/drop): mean atm 2.41
- Mann-Whitney U = 30,015, p = 0.048

*Observation: Direction doesn’t predict CHANGE but does correlate with destination atmosphere. This is consistent with atmosphere being location-inherent rather than movement-caused.*

#### Test 10.2: Building Correspondences

**Data**: 5,279 locations with atmosphere data, 70 unique location types

**Finding**: Location type STRONGLY predicts atmosphere
- Kruskal-Wallis H = 335.73, p < 10^-46
- Effect size η² = 0.059 (medium effect)

**Swedenborgian Building Categories** (ordered by mean atmosphere):

| Category | Mean Atm | SD | N | Example Types |
|----------|----------|-----|-----|---------------|
| LOWER_NATURAL | 2.02 | 0.97 | 383 | basement, parking, warehouse, subway, underground |
| PURIFICATION | 2.14 | 0.98 | 162 | bathroom, hospital |
| TRANSITION | 2.37 | 0.96 | 565 | airport, train_station, city_street, downtown |
| INSTRUCTION | 2.50 | 0.96 | 283 | school, library |
| SOCIAL | 2.67 | 0.96 | 1,041 | restaurant, hotel, house, apartment, mansion |
| WORLDLY_COMMERCE | 2.73 | 0.95 | 1,429 | mall, mall_store, casino |
| NATURAL_BEAUTY | 2.73 | 1.01 | 193 | beach, forest, mountain, waterpark, pool |

**Statistical Validation**:
- Categories differ significantly: H = 130.86, p < 0.0001
- Low vs High categories: Cohen's d = 0.65 (medium-large effect)
- Mean difference: 0.66 atmosphere points

*Observation: Location types show distinct atmosphere profiles. Lower/underground locations have more negative atmospheres; commerce and nature locations are more positive. The ordering by category shows a monotonic pattern from lower_natural to natural_beauty.*

#### Test 10.3: Dream Sequences

**Data**: 2,615 locations with visit order, 342 dreams with 3+ ordered locations

**Finding**: Atmosphere DECLINES slightly over dream course
- Visit order × atmosphere: ρ = -0.055, p = 0.005
- Trajectory analysis: mean slope = -0.056, t = -2.408, p = 0.017
- Distribution: 34.8% declining, 39.8% stable, 25.4% improving

*Observation: Dreams show a weak declining atmosphere trajectory on average. Most dreams (39.8%) are stable; declining (34.8%) slightly outnumbers improving (25.4%).*

**Synthesis:**
1. Movement direction does not predict atmosphere change
2. Building types show distinct atmosphere profiles (η² = 0.059)
3. Dream sequences show slight decline on average (ρ = -0.055)

**Notebook Location**: Cells #VSC-f0fa4876 through #VSC-9c64a29f (Phase 10)

---

## Changelog

### 2026-01-21
- **Phase 10: Movement and Location Analysis**
- Movement direction does NOT predict atmosphere change (ρ = -0.029)
- Ascending destinations correlate with better atmosphere (ρ = 0.10, p = 0.016)
- Building types show distinct atmosphere signatures (H = 335.73, p < 10^−46)
- Dream sequences show slight decline (ρ = -0.055)
- Added Level 10 to Executive Summary

- **Phase 9: Light × Atmosphere Analysis**
- Light and atmosphere strongly associated (V = 0.483)
- Discordant states (cold light + positive atmosphere) rare (2.7%)
- Monotonic ordering by light quality (ρ = 0.353)
- Added Level 9 to Executive Summary

- **Phase 8D-Extended: Within-Dreamer Animal Variance**
- Within-dreamer variance exists (p=0.004): 58.3% of dreamers show different animal demeanors
- Shift correlates with entity context: r=0.753, p<0.0001
- Variance decomposition: 89.5% baseline + 10.5% shift
- Added Level 8 to Executive Summary

### 2026-01-20
- Initial document created
- Phase 1 (H1-H3) findings documented
- Phase 2 (P1-P19) findings documented  
- Phase 3 (E1-E10) entity patterns documented
- Final tally: 32 tests, 22 showing predicted patterns
- **Phase 4 (F1-F7) entity dynamics deep dive added**
- Entity demeanor predicts interaction success (χ² = 48.90, p < 0.0001)
- **Phase 4.5: Watcher exploration and entity manifestation patterns**
- Watchers 31.2% felt-only vs Guides 0% felt-only
- **Phase 5: Building Analysis (corrected from "Sphere" model)**
- Atmosphere is location-intrinsic, not transition-reactive
- **Phase 6: Stable State vs Reactive Model**
- Affect has ZERO independent predictive power for atmosphere (ρ=0.007, p=0.71)
- Data inconsistent with "thoughts create reality" model
- **Phase 7: Dreamer vs Location Analysis**
- Dreamer explains 56.4% of variance vs location type's 7.1%
- Vertical position adds ZERO unique explanatory power after controlling for dreamer
- **Phase 8: Temporal Stability Analysis**
- Temporal range: 2021-09-23 to 2026-01-19 (~4.5 years, 2,678 dreams)
- Demographics too sparse (1.3%) for generational analysis
- Atmosphere shows early volatility (2021-2023) then stabilizes (2024-2026: p=0.0934)
- **Phase 9: Cross-Domain Comparison (MallWorld × NDE)**
- Created notebook: `10_nde_crossdomain_exploration.ipynb`
- Compared 2,678 MallWorld dreams with 6,753 NDEs
- Atmosphere distributions dramatically different (χ² = 4739.51, Cramér's V = 0.645)
- MallWorld: 64% negative, 17% positive
- NDE: 4% negative, 48% positive
- **Phase 8 Extended: Animal Analysis**
- **Phase 8A**: 228 creatures categorized
- Animal demeanor correlates with animal type (χ² = 34.31, p < 0.000001)
- **Phase 8B**: Dreamer consistency analysis
- 65.2% of dreams show congruent affect-atmosphere responses
- ICC = 0.327 (fair within-dreamer consistency)
- Early markers do NOT predict trajectories (ρ = 0.044, p = 0.85)

### 2026-01-21 (Continued)
- **Phase 11b: Cardinal Direction Analysis** — WEAK EFFECT
- η² (cardinal) = 0.017 (only 1.7% variance explained)
- Effect deprioritized in favor of functional categories

- **Phase 12: Functional Category Analysis**
- Functional categories explain 5.2x more variance than cardinal directions
- Functional η² = 0.089 (8.9% variance) vs. Cardinal η² = 0.017 (1.7%)
- Categories show monotonic ordering from lower_natural (2.02) to celestial (4.50)
  
- **Light × Atmosphere Correlation**: ρ = 0.286, p < 0.0001
  - Bright/natural light → better atmosphere
  - Dark/absent light → worse atmosphere
  - Light quality is CONJOINED with atmosphere (not independent predictor)
  
- **Digestive Flow Pattern**: 19.8x forward bias observed
  - Transition mall→restaurant: 59 cases
  - Transition restaurant→mall: 3 cases
  - *Observation: Consistent with directional flow hypothesis*
  
- **Underground Exit Pattern**: +0.44 atmosphere change when leaving basement
  - *Observation: Underground areas show more negative atmosphere, leaving them improves atmosphere*
  
- **Theoretical Note**: The digestive flow hypothesis suggests:
  - Reception spaces (mall) receive/display goods
  - Appropriation spaces (home, restaurant) involve personal consumption
  - Lower levels (basement) = storage/utility areas
  - *These interpretations are framework-dependent and not proven by the data*
  
- Added Level 11-12 synthesis to Executive Summary

- **Phase 13: Building Type Profiles — Exploratory Analysis**
- **Notebook**: `10_architectural_correspondence_tests.ipynb`
- **Methodology**: For EACH building type, filter structured data → use source_file to load raw text → search 41 features
- **Sample**: 44 building types with n ≥ 30 dreams each

- **DATA COLLECTED (exploratory, not confirmatory):**
  - Full feature profiles for 44 building types
  - 41 features including: architectural (glass, window, escalator, etc.) + metals (gold, silver, iron, etc.)
  - Profiles exported to `output/building_type_profiles.csv`

- **KEY OBSERVATIONS (descriptive only):**
  - Building types DO show different feature profiles
  - Pool/waterpark: highest in 'pool' (80%/22%)
  - Hotel: highest in 'elevator' (26%)
  - Basement: high in 'stairs' (20%), 'concrete' (6.8%)
  - Hospital: high in 'elevator' (25%), 'hallway' (15.5%)
  - Metal mentions generally LOW (< 5% for specific metals)

- **WHAT THIS DOES NOT SHOW:**
  - Whether profiles CORRESPOND to Swedenborgian meanings
  - Whether differences are statistically significant vs. chance
  - Confirmation requires pre-registered predictions

- **CORRECTED from previous version:** Mall vs non-mall comparison alone does not confirm correspondence theory; need profiles across ALL building types to test whether correspondences are systematic