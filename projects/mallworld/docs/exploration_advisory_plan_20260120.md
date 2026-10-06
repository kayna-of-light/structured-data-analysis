> **SUPERSEDED, 2026-10-06.** This document predates the October 2026 audit (`STATISTICAL_AUDIT_2026-10.md`). Its figures were computed on a contaminated population, with a join that matched entities to other dreams, or not at all, and none may be cited. Notebook numbers refer to `../notebooks/archive/`.

# MallWorld Exploratory Analysis: Advisory Plan

**Date**: January 20, 2026  
**Status**: Active research planning document  
**Context**: Following completion of initial exploratory pattern discovery (notebook 04)

---

## Executive Summary

This document outlines six major research directions for continued exploratory analysis of the MallWorld dataset. The analysis completed to date has established that MallWorld dream environments exhibit coherent internal structure across multiple dimensions. This plan identifies the most promising avenues for deepening our understanding of that structure.

**Recommended priority**: Entity Ecology → Sequence Motifs → Vertical World Structure

---

## Completed Analysis (as of 2026-01-20)

### Notebooks Completed

| Notebook | Focus | Key Findings |
|----------|-------|--------------|
| 01_swedenborgian_hypothesis_testing | Framework-driven hypotheses | Initial hypothesis tests |
| 02_corrected_functional_hypothesis_testing | Corrected statistical methods | H1-H6 hypothesis results |
| 03_transit_deep_analysis | Transit patterns | Passive-vertical OR=4.35, mode hierarchy, temporal arc |
| 04_exploratory_pattern_discovery | Unsupervised pattern discovery | 10 major pattern categories discovered |

### Key Established Findings

1. **Location-Atmosphere Coherence** (χ² = 1677, p < 10⁻¹²⁶)
   - Natural spaces → peaceful
   - Liminal spaces → uncomfortable/oppressive
   - Commercial spaces → neutral

2. **Reality Stability Gradient** (χ² = 426, p < 10⁻¹⁰)
   - Natural → hyper_real/solid
   - Domestic → shifting
   - Commercial → plastic
   - Underground → decaying

3. **Four Dream Archetypes** (K-means, k=4)
   - Wanderers (5%): exploratory, horizontal
   - Static (40%): minimal movement
   - Threatened (16%): fleeing, high threat
   - Directed (39%): purposeful, ascending tendency

4. **Atmospheric Deterioration** (t = -3.35, p = 0.0008)
   - Dreams systematically worsen over time
   - Welcoming drops 8.7% → 4.1%
   - Threatening rises 8.0% → 10.6%

5. **Transit Grammar**
   - Blocked → Failed (86% confidence)
   - Passive mode correlates with vertical movement (OR = 4.35)
   - Mode×Connection highly non-independent (χ² = 4318)

6. **Mall as Social Space**
   - Social interactions: z = +22.8 in mall
   - Transactions: z = -18.2 in mall (suppressed)
   - Transactions occur in mall_stores, not mall commons

---

## Research Direction 1: Entity Ecology

### Priority: HIGH (Recommended First)

### Rationale
We have 3,704 entity encounters across 18 entity types. Initial analysis showed entity-interaction associations (χ² = 211, p < 10⁻¹⁷), but entities remain largely unexplored. Entities are the "characters" of dreams—understanding their ecology should illuminate dream narrative structure.

### Research Questions

1. **Spatial Distribution**: Where do different entities appear?
   - Entity type × Location type associations
   - Are threats concentrated in specific locations?
   - Do guides appear in transition spaces?

2. **Atmospheric Correlation**: What atmospheres accompany different entities?
   - Entity type × Atmosphere associations
   - Do threats CREATE threatening atmospheres or APPEAR IN them?

3. **Entity Behavioral Profiles**: What happens when different entities are present?
   - Interaction outcome rates by entity presence
   - Transit mode distribution by entity type
   - Dream trajectory changes when specific entities appear

4. **Entity Co-occurrence**: Which entities appear together?
   - Entity-entity lift analysis (partially done in notebook 04)
   - Entity cluster identification
   - "Hostile cast" vs "neutral cast" dreams

5. **Entity Impact on Dream Outcomes**:
   - Does guide presence predict dream success?
   - Does threat presence predict atmospheric deterioration?
   - Entity count × dream complexity relationships

### Proposed Methods
- Chi-square tests for entity × location, entity × atmosphere
- Logistic regression: entity presence predicting outcomes
- Correlation analysis: entity count vs dream characteristics
- Sequence analysis: entity appearance timing within dreams

### Expected Deliverables
- Entity profile table (comprehensive characterization)
- Entity-location heatmap
- Entity impact on outcomes analysis
- Entity co-occurrence network

---

## Research Direction 2: Sequence Motif Discovery

### Priority: HIGH

### Rationale
Dreams are sequential experiences. We've analyzed aggregate patterns, but not the sequential structure of individual dreams. Identifying common sequences could reveal narrative templates.

### Research Questions

1. **Common Location Sequences**: What 2-gram, 3-gram, 4-gram sequences recur?
   - Most frequent transition pairs
   - Recurring multi-step paths
   - "Entry points" and "exit points" of the dream world

2. **Markov Chain Modeling**: Can we model dreams as probabilistic state machines?
   - Transition probability matrix
   - Stationary distribution (where do dreams "settle"?)
   - Absorbing states (terminal locations?)

3. **Narrative Arc Detection**: Do dreams follow recognizable dramatic structures?
   - Rising action → climax → resolution patterns?
   - Complication sequences (atmosphere worsening → resolution?)
   - Failed resolution patterns

4. **Loop and Trap Detection**: How common are stuck patterns?
   - Location revisit analysis
   - True loops (A → B → A) vs spirals (A → B → A')
   - Escape from loops—what enables exit?

5. **Motif Clustering**: Are there recurring "story types"?
   - Sequence similarity clustering
   - Template identification
   - Variation within templates

### Proposed Methods
- N-gram frequency analysis
- Markov chain construction and analysis
- Sequence alignment algorithms (edit distance)
- Hidden Markov Model for narrative state inference

### Expected Deliverables
- Top-50 recurring sequences table
- Markov transition matrix visualization
- Loop frequency and characteristics report
- Narrative template catalog

---

## Research Direction 3: Outcome Prediction Modeling

### Priority: MEDIUM-HIGH

### Rationale
We know interaction success rates vary (transaction 46% vs search 16%), but we don't know what predicts success within interaction types. Understanding success predictors could reveal the "rules" of MallWorld.

### Research Questions

1. **What Predicts Interaction Success?**
   - Location type effect on success
   - Atmosphere effect on success
   - Entity presence effect on success
   - Position in dream sequence effect

2. **Does Early Success Beget Later Success?**
   - Autocorrelation in outcome sequences
   - Momentum effects
   - Recovery from failure

3. **Feature Importance Ranking**: Which factors matter most?
   - Random forest feature importance
   - SHAP values for interpretability
   - Interaction effects

4. **Context-Specific Models**: Do different rules apply in different contexts?
   - Escape success predictors (vs general success)
   - Transaction success predictors
   - Navigation success predictors

### Proposed Methods
- Logistic regression with interaction terms
- Random forest classification
- SHAP analysis for interpretability
- Stratified analysis by interaction type

### Expected Deliverables
- Success predictor ranking table
- Feature importance visualization
- Context-specific success models
- "Rules of success" summary

---

## Research Direction 4: Location Deep Profiles

### Priority: MEDIUM

### Rationale
We've established that locations have characteristic atmospheres. But each major location type deserves comprehensive profiling—what is the full "personality" of a mall, a school, a basement?

### Research Questions

1. **Complete Location Characterization**: For each major location type:
   - Atmosphere distribution
   - Reality stability distribution
   - Entity population (who appears here?)
   - Interaction types (what happens here?)
   - Transit modes (how do people arrive/leave?)
   - Outcomes (success rates)
   - Network role (hub, bridge, dead-end?)

2. **Location Taxonomies**: Can locations be meaningfully grouped?
   - Hierarchical clustering of location profiles
   - Natural groupings that emerge
   - Anomalous locations that don't fit

3. **Location Function vs Location Type**: Same type, different function?
   - Mall_store variety (clothing vs electronics vs food)
   - School variety (classroom vs hallway vs cafeteria)
   - Functional subtypes

### Proposed Methods
- Comprehensive cross-tabulation
- Radar charts for location profiles
- Hierarchical clustering on location features
- Subtype analysis within categories

### Expected Deliverables
- Location profile cards (top 20 locations)
- Location taxonomy dendrogram
- Functional classification scheme
- Location "personality" summary

---

## Research Direction 5: Affective Dynamics

### Priority: MEDIUM

### Rationale
We have affective_response and somatic_response fields that capture emotional and bodily experiences. These are underexplored and could illuminate the experiential texture of MallWorld dreams.

### Research Questions

1. **Affective Triggers**: What locations/entities/events trigger specific affects?
   - Anxiety triggers
   - Curiosity triggers
   - Delight triggers
   - Horror triggers

2. **Affective Propagation**: Do affects spread through dreams?
   - Does anxiety at location N predict anxiety at N+1?
   - Affective momentum
   - Affective "reset" events

3. **Somatic Experiences**: When do bodily sensations occur?
   - Paralysis conditions
   - Ejection conditions
   - Glitching conditions
   - Somatic → affective relationships

4. **Affective-Outcome Relationships**: Does affect predict behavior/success?
   - Anxiety → escape attempts?
   - Curiosity → exploration?
   - Affect as mediator of location-outcome relationships

### Proposed Methods
- Chi-square for affect × location, affect × entity
- Sequence analysis of affective states
- Logistic regression: affect predicting outcomes
- Mediation analysis

### Expected Deliverables
- Affective trigger catalog
- Somatic experience conditions
- Affect propagation analysis
- Affect-outcome model

---

## Research Direction 6: Vertical World Structure

### Priority: MEDIUM

### Rationale
MallWorld dreams feature prominent vertical structure—basements, underground spaces, rooftops, elevators. We've found passive transit correlates with vertical movement (OR = 4.35). But vertical structure deserves dedicated analysis.

### Research Questions

1. **Vertical Distribution**: How are features distributed by vertical level?
   - Underground vs surface vs elevated
   - Atmosphere by vertical position
   - Entity distribution by vertical position
   - Reality stability by vertical position

2. **Vertical Movement Patterns**: What predicts ascent vs descent?
   - Who ascends? Who descends?
   - Ascent outcomes vs descent outcomes
   - Vertical movement and atmosphere change

3. **Vertical Symbolism**: Are there consistent patterns?
   - Underground = threat/decay?
   - Elevation = escape/clarity?
   - Vertical position as dream state indicator

4. **Multi-Level Structures**: How do dreams use vertical complexity?
   - Mall levels, building floors
   - Elevator sequences
   - Basement-to-roof trajectories

### Proposed Methods
- Cross-tabulation by vertical position
- Vertical trajectory analysis
- Correlation: vertical change × atmosphere change
- Case study of multi-level dreams

### Expected Deliverables
- Vertical distribution tables
- Vertical movement outcome analysis
- Vertical symbolism pattern summary
- Multi-level dream characteristics

---

## Implementation Priority Matrix

| Direction | Information Value | Feasibility | Data Richness | Priority |
|-----------|------------------|-------------|---------------|----------|
| Entity Ecology | High | High | 3,704 entities | **1st** |
| Sequence Motifs | High | Medium | 4,600 connections | **2nd** |
| Vertical Structure | Medium-High | High | vertical_position field | **3rd** |
| Outcome Prediction | Medium-High | Medium | 6,075 interactions | 4th |
| Location Profiles | Medium | High | 8,707 locations | 5th |
| Affective Dynamics | Medium | Medium | Sparse fields | 6th |

---

## Recommended Execution Order

### Phase 1 (Immediate)
- **Notebook 05**: Entity Ecology Deep Analysis
  - Complete entity profiling
  - Entity-location-atmosphere triangulation
  - Entity impact on outcomes

### Phase 2 (Near-term)
- **Notebook 06**: Sequence Motif Discovery
  - N-gram analysis
  - Markov modeling
  - Loop/trap detection

### Phase 3 (Follow-up)
- **Notebook 07**: Vertical World Structure
  - Vertical distribution analysis
  - Vertical movement patterns
  - Integration with entity and sequence findings

### Phase 4 (As needed)
- Additional notebooks for outcome prediction, location profiles, affective dynamics based on what emerges from Phases 1-3

---

## Success Criteria

Analysis will be considered successful if it:

1. **Discovers novel patterns** not visible in individual dream reports
2. **Quantifies relationships** with appropriate statistical tests
3. **Generates testable hypotheses** for future investigation
4. **Maintains research integrity** by reporting what data show, not what we expect
5. **Produces documented, reproducible analysis** in well-structured notebooks

---

## Notes on Research Integrity

Per project guidelines, all analysis should:

1. **Report what the data shows** — statistical patterns, effect sizes, significance
2. **Report what the data does not show** — underdetermined, ambiguous findings
3. **Distinguish claim levels**:
   - Statistically supported (p < 0.05 with test details)
   - Reasonable interpretation (consistent but not proven)
   - Speculative (requires additional assumptions)
4. **Not adjust conclusions based on expected outcomes**

The goal is accuracy, not confirmation or skepticism.

---

*Document maintained as living reference for MallWorld exploratory analysis project.*
