# Outcome Prediction in MallWorld Dreams: The Rules of Success and Failure

## Abstract

**Background**: MallWorld dreams feature diverse interactions—navigation, search, escape, transactions—with varying outcomes. Understanding what predicts interaction success reveals the implicit "rules" governing these dream environments and their relationship to waking psychological dynamics.

**Methods**: We analyzed 3,331 interactions with definitive outcomes (succeeded, failed, interrupted, abandoned) from 3,732 MallWorld dream narratives. Predictors included interaction type, atmospheric quality, entity presence and demeanor, reality stability, vertical position, and sequence position. Logistic regression and random forest models quantified feature importance and predictive power.

**Results**: Interaction type was the strongest predictor: observation achieved 85.4% success while search reached only 29.0%. Atmosphere showed profound effects—positive environments yielded 81.3% success versus 57.2% for negative (χ² = 72.3, p < 0.0001). Entity demeanor exhibited a paradoxical pattern: friendly entities correlated with 89.0% success, but indifferent entities showed the worst outcomes (25.8%), worse than hostile entities (57.1%). A strong momentum effect emerged—prior success predicted 68.4% subsequent success versus 48.4% after prior failure (χ² = 57.4, p < 0.0001). Multivariate models achieved ROC-AUC of 0.67.

**Conclusions**: MallWorld dreams operate according to discoverable rules that privilege passive attention over active seeking, reward environmental attunement, and punish indifference more than hostility. These patterns suggest dream logic follows relational and emotional dynamics rather than purely physical constraints.

**Keywords**: MallWorld, dream analysis, outcome prediction, machine learning, entity demeanor, momentum effect, atmosphere

---

## Data Provenance

| Metric | Value |
|--------|-------|
| Source | r/themallworld subreddit |
| Total Dreams | 3,732 |
| Total Interactions | 7,558 |
| Interactions with Definitive Outcomes | 3,331 (44.1%) |
| Baseline Success Rate | 62.5% |
| Entity-Interaction Pairs | 1,865 |
| Analysis Date | January 2025 |

---

## 1. Introduction

### 1.1 Background

The MallWorld phenomenon presents a unique opportunity for studying dream logic at scale. Thousands of individuals report dreams of navigating labyrinthine mall environments, and within these narratives, they attempt various interactions—searching for exits, navigating corridors, engaging with entities, conducting transactions. Some succeed; many fail.

The question of what predicts success in these dream interactions is not merely academic. If MallWorld dreams exhibit consistent "rules" governing outcomes, this would suggest either:

1. **Shared psychological dynamics**: Common cognitive-emotional patterns that shape dream outcomes across individuals
2. **Archetypal logic**: Underlying narrative structures that constrain dream possibilities
3. **Environmental semantics**: Consistent relationships between dream features and action outcomes

### 1.2 Research Questions

This analysis addresses four questions from the advisory plan:

1. **What predicts interaction success?** — Which features (location, atmosphere, entity presence, sequence position) correlate with successful outcomes?
2. **Does early success beget later success?** — Is there momentum in dream outcomes?
3. **Which features matter most?** — How do predictors rank in importance?
4. **Do different rules apply in different contexts?** — Are escape success predictors different from search success predictors?

### 1.3 Theoretical Framework

Dream outcomes may be governed by multiple logics:

- **Physical logic**: Success depends on environmental constraints (doors, distances, obstacles)
- **Social logic**: Success depends on entity relationships (help, hindrance, indifference)
- **Emotional logic**: Success depends on affective state (fear, confidence, desperation)
- **Narrative logic**: Success depends on story structure (rising action requires failure, resolution requires success)

We make no a priori commitment to which logic dominates.

---

## 2. Methods

### 2.1 Outcome Classification

Interactions were classified into six outcome categories:

| Outcome | Count | Percentage |
|---------|-------|------------|
| not_mentioned | 2,769 | 36.6% |
| succeeded | 2,082 | 27.5% |
| ongoing | 1,458 | 19.3% |
| failed | 776 | 10.3% |
| interrupted | 388 | 5.1% |
| abandoned | 85 | 1.1% |

For modeling, we retained "meaningful" outcomes: succeeded, failed, interrupted, and abandoned (n = 3,331). Success was defined as outcome = "succeeded" (binary coding).

### 2.2 Predictor Variables

| Predictor | Type | Levels/Range |
|-----------|------|--------------|
| Interaction type | Categorical | 9 types (navigation, escape, search, etc.) |
| Atmosphere | Categorical → Ordinal | 11 types → 3 valence levels |
| Entity presence | Binary | Has/does not have entities |
| Entity demeanor | Categorical → Ordinal | 9 demeanors → 3 valence levels |
| Reality stability | Categorical | 5 levels (solid, shifting, etc.) |
| Vertical position | Categorical | 5 levels (lowest to uppermost) |
| Sequence position | Ordinal | Interaction index within dream |
| Prior success | Binary/Continuous | Had prior success / prior success rate |

### 2.3 Statistical Methods

- **Chi-square tests**: Independence of categorical predictors from outcome
- **Spearman correlation**: Association of ordinal/continuous predictors with binary outcome
- **Logistic regression**: Multivariate modeling with odds ratios
- **Random forest**: Non-linear modeling with feature importance
- **Cross-validation**: 5-fold CV for model performance estimation

---

## 3. Results

### 3.1 Success Rate by Interaction Type

Interaction type was the strongest predictor of success:

| Interaction Type | n | Success Rate | Rank |
|------------------|---|--------------|------|
| Observation | 350 | 85.4% | 1 |
| Social | 349 | 76.2% | 2 |
| Other | 76 | 69.7% | 3 |
| Navigation | 791 | 66.2% | 4 |
| Transaction | 168 | 64.3% | 5 |
| Task | 554 | 60.5% | 6 |
| Conflict | 205 | 60.5% | 7 |
| Escape | 538 | 53.2% | 8 |
| Search | 300 | 29.0% | 9 |

Chi-square test: χ² = 534.2, df = 24, p < 0.0001

**Critical Finding**: Observation succeeds nearly **3 times more often** than search (85.4% vs 29.0%). The dream rewards passive witnessing and punishes active seeking.

### 3.2 Success Rate by Atmosphere

Atmosphere showed a strong gradient:

| Atmosphere | n | Success Rate |
|------------|---|--------------|
| Welcoming | 166 | 84.9% |
| Peaceful | 65 | 78.5% |
| Nostalgic | 47 | 72.3% |
| Neutral | 366 | 70.8% |
| Eerie | 303 | 66.7% |
| Chaotic | 249 | 61.0% |
| Threatening | 503 | 54.3% |
| Wrong | 94 | 54.3% |
| Uncomfortable | 328 | 53.0% |
| Oppressive | 159 | 52.2% |

Grouping by valence:

| Valence | n | Success Rate |
|---------|---|--------------|
| Positive | 278 | 81.3% |
| Neutral | 366 | 70.8% |
| Negative | 1,636 | 57.2% |

Chi-square test: χ² = 72.3, df = 2, p < 0.0001

**Critical Finding**: Atmosphere valence creates a **24 percentage point** success gap. Environmental mood is nearly as predictive as interaction type.

### 3.3 Success Rate by Entity Presence

| Entity Presence | n | Success Rate |
|-----------------|---|--------------|
| With entities | 1,520 | 66.6% |
| Without entities | 1,811 | 59.0% |

Chi-square test: χ² = 20.1, df = 1, p < 0.0001

**Critical Finding**: Entity presence correlates with **higher** success rates (+7.6%), contrary to the assumption that entities create obstacles.

### 3.4 Success Rate by Entity Type

| Entity Type | n | Success Rate |
|-------------|---|--------------|
| Guide | 27 | 88.9% |
| Shadow | 6 | 83.3% |
| Child | 45 | 77.8% |
| Coworker | 8 | 75.0% |
| Stranger | 497 | 72.2% |
| Deceased | 25 | 72.0% |
| Friend | 44 | 68.2% |
| Known person | 131 | 67.2% |
| Crowd | 311 | 66.6% |
| Other | 105 | 65.7% |
| Creature | 88 | 62.5% |
| Threat | 169 | 62.1% |
| Family member | 116 | 58.6% |
| Authority | 286 | 57.0% |
| Watcher | 3 | 33.3% |

Chi-square test: χ² = 37.6, df = 16, p = 0.0017

**Critical Finding**: Guides achieve **88.9%** success—the highest of any entity type. Even threat entities (62.1%) outperform family members (58.6%).

### 3.5 Success Rate by Entity Demeanor

| Demeanor | n | Success Rate |
|----------|---|--------------|
| Friendly | 227 | 89.0% |
| Helpful | 100 | 87.0% |
| Neutral | 483 | 75.2% |
| Watching | 39 | 64.1% |
| Threatening | 142 | 58.5% |
| Hostile | 254 | 57.1% |
| Confusing | 120 | 50.8% |
| Unfriendly | 155 | 44.5% |
| **Indifferent** | 66 | **25.8%** |

Grouping by valence:

| Valence | n | Success Rate |
|---------|---|--------------|
| Positive | 327 | 88.4% |
| Neutral | 708 | 65.8% |
| Negative | 551 | 53.9% |

Chi-square test: χ² = 109.4, df = 2, p < 0.0001

**Critical Finding**: Indifferent entities yield the **worst** outcomes (25.8%)—dramatically worse than hostile (57.1%) or threatening (58.5%) entities. Being ignored is worse than being attacked.

### 3.6 Momentum Effect

Analysis of sequential outcomes within dreams:

| Prior Outcome | n | Current Success Rate |
|---------------|---|---------------------|
| After success | 1,404 | 68.4% |
| After failure | 448 | 48.4% |

Spearman correlation (prior success rate × current success): ρ = 0.204, p < 0.0001
Chi-square test: χ² = 57.4, df = 1, p < 0.0001

**Critical Finding**: Prior success increases subsequent success by **20 percentage points**. Dreams exhibit strong autocorrelation in outcomes—momentum is real.

### 3.7 Reality Stability

| Reality | n | Success Rate |
|---------|---|--------------|
| Decaying | 7 | 100.0% |
| Hyper-real | 106 | 72.6% |
| Solid | 1,447 | 65.9% |
| Shifting | 409 | 57.5% |
| Plastic | 18 | 50.0% |

Chi-square test: χ² = 18.7, df = 4, p = 0.0009

**Critical Finding**: Solid reality supports success (65.9%), while shifting reality undermines it (57.5%). Stability enables agency.

### 3.8 Vertical Position

| Vertical | n | Success Rate |
|----------|---|--------------|
| Ground | 551 | 68.1% |
| Upper | 219 | 64.8% |
| Lower | 173 | 64.2% |
| Uppermost | 110 | 60.0% |
| Lowest | 63 | 55.6% |

Chi-square test: χ² = 6.0, df = 4, p = 0.20 (NOT significant)

**Critical Finding**: Unlike atmosphere, **vertical position does not significantly predict success**. The vertical-atmosphere correlation found in earlier analysis does not translate into outcome prediction.

### 3.9 Multivariate Models

#### Logistic Regression

5-Fold Cross-Validation ROC-AUC: 0.671 (±0.043)

| Feature | Odds Ratio | Direction |
|---------|------------|-----------|
| type_search | 0.220 | ↓ Harmful |
| type_observation | 2.881 | ↑ Helpful |
| atmos_valence | 1.510 | ↑ Helpful |
| has_entities | 1.325 | ↑ Helpful |
| reality_solid | 1.255 | ↑ Helpful |
| type_social | 1.234 | ↑ Helpful |
| type_escape | 0.632 | ↓ Harmful |
| type_task | 0.767 | ↓ Harmful |
| type_conflict | 0.767 | ↓ Harmful |
| type_transaction | 0.815 | ↓ Harmful |

Model accuracy: 66.9% (baseline: 62.5%)

**Critical Finding**: Search interaction has OR = 0.22—it reduces success odds by **78%**. Observation has OR = 2.88—it nearly triples success odds.

#### Random Forest Feature Importance

| Feature | Importance |
|---------|------------|
| type_search | 0.226 |
| atmos_valence | 0.168 |
| seq_position | 0.166 |
| type_observation | 0.119 |
| reality_solid | 0.085 |
| has_entities | 0.075 |

Model accuracy: 68.6%

### 3.10 Context-Specific Rules

#### Escape Interactions (n = 538, 53.2% success)

| Context | Success Rate |
|---------|--------------|
| Chaotic atmosphere | 70.5% |
| Welcoming atmosphere | 100.0% |
| Threatening atmosphere | 50.7% |
| With entities | 58.5% |
| Without entities | 47.5% |

**Critical Finding**: Chaos **enables** escape (70.5%), while threatening atmospheres hinder it (50.7%). Disorder opens exit routes.

#### Search Interactions (n = 300, 29.0% success)

| Context | Success Rate |
|---------|--------------|
| House location | 66.7% |
| School location | 11.8% |
| Neutral atmosphere | 41.2% |
| Oppressive atmosphere | 11.1% |

**Critical Finding**: Searches in familiar spaces (house: 66.7%) dramatically outperform institutional spaces (school: 11.8%).

---

## 4. Discussion

### 4.1 The Rules of MallWorld

The data reveal six consistent "rules" governing dream outcomes:

#### Rule 1: Watch, Don't Search
Observation succeeds 3x more often than search. The dream environment rewards passive attention and punishes active seeking. This aligns with the phenomenology of dream states, where directed intention often fails while receptive awareness permits experience.

#### Rule 2: Atmosphere Is Destiny
A 24 percentage point gap separates positive from negative atmospheres. Environmental mood is nearly as predictive as interaction type. This suggests dream outcomes are governed more by affective context than by physical constraints.

#### Rule 3: Success Breeds Success
Prior success increases subsequent success by 20 points. Dreams exhibit momentum—once things go well, they tend to continue well; once they go badly, recovery is difficult. This autocorrelation suggests dream narratives have inertial properties.

#### Rule 4: Indifference Is Worse Than Hostility
The most surprising finding: indifferent entities yield 25.8% success versus 57.1% for hostile entities. Being ignored is more damaging than being attacked. This suggests dream success requires relational engagement—even negative attention outperforms no attention.

#### Rule 5: Chaos Enables Escape
Chaotic atmospheres yield 70.5% escape success versus 50.7% for threatening atmospheres. Disorder creates opportunities that structured threat forecloses. This paradox suggests that the "rules" of the dream environment can be broken when the environment itself breaks down.

#### Rule 6: Reality Anchors Action
Solid reality (65.9%) outperforms shifting reality (57.5%). Stability enables agency; instability undermines it. This aligns with waking intuitions but quantifies the effect.

### 4.2 Theoretical Implications

#### Against Physical Logic
Vertical position—a clearly physical feature—does not predict success. Meanwhile, atmosphere—an affective feature—strongly predicts success. This suggests dream outcomes follow emotional rather than physical logic.

#### Relational Primacy
The indifference finding points to relational primacy in dream outcomes. Entities that engage (even hostilely) enable action; entities that disengage foreclose it. Dreams may be fundamentally social-relational spaces, where isolation is more disabling than opposition.

#### Narrative Structure
The momentum effect suggests dreams follow narrative logic where early events constrain later possibilities. Failed dreams tend to continue failing; successful dreams tend to continue succeeding. This autocorrelation resembles story structure more than random walks.

### 4.3 Limitations

1. **Binary outcome coding**: The succeeded/not-succeeded dichotomy obscures gradations of success and failure
2. **Missing predictors**: Personal dreamer characteristics, dream frequency, and individual history are not captured
3. **Extraction uncertainty**: LLM-based outcome coding may misinterpret ambiguous narratives
4. **Selection bias**: Reddit reports may emphasize dramatic (high-failure) dreams
5. **Modest predictive power**: ROC-AUC of 0.67 indicates substantial unexplained variance

### 4.4 Future Directions

1. **Momentum mechanisms**: What breaks negative momentum? What initiates positive momentum?
2. **Entity demeanor dynamics**: Do entity demeanors change within dreams? Does demeanor predict outcome only on first encounter?
3. **Search failure modes**: Why is search so uniquely difficult? What distinguishes successful searches?
4. **Individual differences**: Do some dreamers show consistently higher success rates?

---

## 5. Conclusion

MallWorld dreams operate according to discoverable rules that privilege passive attention over active seeking, reward environmental attunement, and—paradoxically—punish indifference more than hostility. Success is predicted by interaction type (observation > search), atmosphere (positive > negative), entity demeanor (friendly > hostile > indifferent), and prior outcomes (success breeds success).

These patterns suggest dream logic follows relational and emotional dynamics rather than purely physical constraints. The dream mall is not just a spatial environment but a social-emotional field where mood, engagement, and momentum shape what is possible. The dreamer who succeeds is not the one who searches hardest, but the one who attends, relates, and rides the wave of prior success.

---

## References

1. Hartmann, E. (1998). *Dreams and Nightmares: The New Theory on the Origin and Meaning of Dreams*. Perseus.
2. Domhoff, G. W. (2003). *The Scientific Study of Dreams*. APA Press.
3. Revonsuo, A. (2000). The reinterpretation of dreams: An evolutionary hypothesis of the function of dreaming. *Behavioral and Brain Sciences*, 23(6), 877-901.
4. Barrett, D. (2001). *The Committee of Sleep*. Crown.

---

## Appendix A: Model Specifications

### Logistic Regression
- Solver: lbfgs
- Max iterations: 1000
- Regularization: L2 (default)
- Cross-validation: 5-fold stratified

### Random Forest
- Estimators: 100
- Max depth: 10
- Random state: 42
- Cross-validation: 5-fold stratified

---

## Appendix B: Notebook Reference

Full analysis code available in: `projects/mallworld/notebooks/08_outcome_prediction_modeling.ipynb`
