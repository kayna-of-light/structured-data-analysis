# Direct Perception Through Discrete Degrees: Empirical Analysis of Perceptual Depth in Near-Death Experiences

> **Correction notice (2026-10-05).** This report was revised after a statistical audit (`docs/STATISTICAL_AUDIT_2026-10.md`). The original statistics were mostly computed correctly, but several conclusions went beyond them. Changes:
> 1. **Factor structure.** The two-factor solution was imposed (`n_factors = 2`), not found. Every retention criterion gives one factor, so "internal differentiation" is withdrawn.
> 2. **Score distribution.** The right-skewed distribution was called "exactly what discrete degree theory predicts". Seven *independent* markers with these prevalences would also be right-skewed, so the skew is not diagnostic.
> 3. **Narrative length.** Length explains 41% of the score variance and was not controlled. After adjustment, the Being-of-Light difference falls from +1.09 to +0.39 markers, and only two of seven markers remain elevated.
> 4. **Construct validity.** It was not checked against narrative length. Controlling for length halves the mean inter-marker correlation, and telepathy no longer correlates with the other markers.
> 5. **Cultural invariance.** It rested on a non-significant ANOVA (absence of evidence). An equivalence test now supports it for Christian vs atheist/agnostic experiencers.
> 6. **Prevalence hierarchy.** The predicted natural > spiritual > celestial ordering was never tested. It is not observed.
> 7. **Factual errors corrected.** The sample split was wrong: NDERF 5,659 and IANDS 1,092, not 6,135 and 618. The analysis notebook is `06_cognitive_mode_profile.ipynb`, not `05_…`. The factor method is minres, not principal axis. The telepathy denominators were wrong, and several religion SDs did not match the data.
> 8. **Strawman comparisons removed.** These were "the materialist null predicts no coherent structure" and "universal activation predicts a left-skewed distribution".
> 9. **Palaeolithic signs.** The link to the Palaeolithic geometric signs is now marked as speculative.
>
> N = 6,751 after removing two duplicate narratives.

## Abstract

**Background**: Near-death experiencers often report perceptual qualities unlike ordinary consciousness — heightened vividness, altered time, accelerated thought, telepathic communication, and a sense of "more real than real." Swedenborg's doctrine of discrete degrees proposes natural, spiritual and celestial levels of perception, normally constrained to the natural. Applied to NDEs, it predicts a coherent perceptual construct with a gradient of depth, a prevalence ordering from natural to celestial markers, internal structure reflecting the degrees, deeper perception in encounters with the Being of Light, and invariance across religious backgrounds.

**Methods**: We analysed 6,751 structured NDE records (NDERF n=5,659; IANDS n=1,092) extracted with GPT-5.2. Seven binary markers were assigned to degrees: natural (sensory vividness, memory persistence), spiritual (reality certainty, time perception, thought speed), celestial (comparative reality, telepathic communication). We assessed internal consistency (KR-20, KMO), factor structure (eigenvalues, parallel analysis, tetrachoric correlations, minres extraction), the score distribution against an independence baseline, and the influence of narrative length (partial correlations, length-adjusted regressions). Religious invariance was tested with ANOVA, Kruskal–Wallis and a two one-sided equivalence test (TOST).

**Results**: The markers form an internally consistent scale (KR-20 = 0.738; KMO = 0.817; 21/21 positive correlations). Narrative length explains 41% of score variance; controlling for it halves the mean inter-marker correlation (0.29 → 0.15), but the six non-telepathic markers still cohere (15/15 significant), while telepathy no longer correlates with them. Every retention criterion gives one factor; the predicted prevalence hierarchy is not observed (ρ = −0.47, p = 0.28). The right-skewed distribution is also produced by independent markers and is not diagnostic. Being-of-Light accounts score higher (d = 0.589), but after length adjustment the difference is +0.39 markers (95% CI 0.28–0.49), carried by comparative reality (OR 1.87) and telepathy (OR 3.90). Christian and atheist/agnostic experiencers score the same (difference −0.005; TOST within ±0.5, p = 0.005; length-adjusted +0.02).

**Conclusions**: NDE accounts contain one dominant dimension of enhanced perception that is not produced by narrative length alone and does not differ between Christian and non-religious experiencers — consistent with a universal perceptual state rather than religious priming. The predictions specific to *discrete* degrees — a prevalence hierarchy and degree-aligned factors — are not supported. The Being-of-Light association survives, attenuated, for the two markers assigned to the celestial degree.

**Keywords**: near-death experience, discrete degrees, perception, Swedenborg, correspondences, factor analysis, Being of Light, cultural invariance, equivalence testing

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF accounts (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS accounts (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis code | `06_cognitive_mode_profile.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/06_cognitive_mode_profile.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured data | `projects/nde/structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis) (6,753 files; 6,751 unique narratives) |
| Extraction model | GPT-5.2 via Azure OpenAI | Structured output with Pydantic schema |

---

## 1. Introduction

### 1.1 Background

Near-death experiencers frequently report perceptual qualities that differ from ordinary waking consciousness: heightened sensory vividness, accelerated thought, temporal distortion, telepathic communication, and an insistence that the experience was "more real than real life" (Moody, 1975; Ring, 1980; van Lommel, 2010). The *internal structure* of this perceptual shift — whether it forms a coherent construct, whether it varies in degree, and how it relates to other NDE features — has received less systematic attention.

### 1.2 Theoretical Framework

Swedenborg's doctrine of discrete degrees (1758, 1763) proposes three levels of perception:

| Degree | Mode of Perception | Key Property |
|--------|-------------------|--------------|
| **Natural** | Sensory-mediated, sequential, spatiotemporal | Filtered by biological constraints |
| **Spiritual** | Direct knowing through understanding; truth-mediated | Access to meaning without sensory intermediation |
| **Celestial** | Direct knowing through love; affection-mediated | Perception through union rather than understanding |

In embodied life, biological filtering constrains awareness to the natural degree; the higher degrees are present as capacities, and the ruling love determines which is developed. If filtering is suspended during an NDE, perception should reflect the degree already developed.

### 1.3 Hypotheses

| # | Hypothesis | What would distinguish discrete degrees from a single intensity dimension |
|---|---|---|
| H1 | Prevalence gradient: natural markers most common, celestial least | Yes |
| H2 | The markers form a coherent construct | No (any shared state predicts this) |
| H3 | Internal structure with 2+ factors aligned with the degrees | Yes |
| H4 | Being-of-Light encounter correlates with deeper perception | Partly (if the effect concentrates on higher-degree markers) |
| H5 | The profile is constant across religious backgrounds | No (constant state) |
| H6 | The score shows a gradient rather than all-or-none activation | Only if it differs from what independent or length-driven markers produce |

---

## 2. Methods

### 2.1 Data Sources

NDERF (5,659 accounts) and IANDS (1,092 accounts); two duplicate narratives counted once (N = 6,751). All records were processed through GPT-5.2 structured extraction using the Pydantic schema in `models/questionnaire.py`. Coding reliability was measured afterwards against a blind second coder (`08_extraction_reliability.ipynb`) for two of the seven markers. Telepathic communication agrees at Cohen's κ = 0.88. Comparative reality agrees at κ = 0.74, but GPT-5.2 codes it more often than the second coder (13 vs 8 in 100 accounts) and is unstable on it across duplicate submissions (test–retest κ = 0.58). The other five markers have not been recoded.

### 2.2 Perception Markers

| Marker | Source Field | Positive Values | Proposed Degree |
|--------|-------------|-----------------|-----------------|
| Sensory vividness | `sensory_vividness` | `incredibly_more_vivid`, `more_vivid` | Natural |
| Memory persistence | `memory_persistence` | `more_vivid_than_normal` | Natural |
| Reality certainty | `reality_assessment` | `definitely_real` | Spiritual |
| Time perception | `time_perception` | `everything_at_once`, `timeless` | Spiritual |
| Thought speed | `thought_speed` | `incredibly_fast`, `faster_than_normal` | Spiritual |
| Comparative reality | `comparative_reality` | `more_real_explicit`, `more_real_implied` | Celestial |
| Telepathic communication | `communication_modes` | list contains `telepathic` | Celestial |

Each marker is binary (1 = present; 0 = absent or not mentioned). The composite score (0–7) is the sum. Because "not mentioned" is scored 0, the score combines what was experienced with what was reported.

### 2.3 Statistical Analysis

- **Internal consistency**: phi correlations with Holm correction; KR-20; KMO; Bartlett's test
- **Factor structure**: eigenvalues of phi and tetrachoric matrices; parallel analysis (500 permutations, 95th percentile); minres extraction (`factor_analyzer`), 1- and 2-factor solutions
- **Narrative length**: word count of the source narrative; Spearman correlation and R² with the score; partial correlations after residualising each marker on log word count (linear and quadratic); length-adjusted OLS and logistic regressions
- **Distribution**: observed score distribution vs the Poisson-binomial distribution expected if the seven markers were independent with their observed prevalences
- **Being of Light**: t-test, Mann-Whitney U, Cohen's d; per-marker χ² and crude/length-adjusted odds ratios
- **Religion**: one-way ANOVA with η², Kruskal–Wallis, TOST equivalence (±0.5 markers) for Christian vs atheist/agnostic, per-marker χ² with Holm correction and expected-count checks

---

## 3. Results

### 3.1 Marker Prevalence and the Predicted Hierarchy (H1)

| Marker | Degree | % Mentioned | % Positive (All) | % Positive (Mentioned) | % Strongest Value |
|--------|--------|-------------|-------------------|------------------------|-------------------|
| Reality certainty | Spiritual | 61.7% | 58.2% | 94.3% | 58.2% |
| Sensory vividness | Natural | 38.5% | 32.5% | 84.3% | 18.0% |
| Memory persistence | Natural | 32.7% | 28.9% | 88.1% | 28.9% |
| Telepathic | Celestial | 56.2%* | 27.0% | 48.0%* | — |
| Time perception | Spiritual | 36.0% | 21.8% | 60.6% | 8.2% |
| Comparative reality | Celestial | 16.6% | 16.1% | 97.0% | 10.4% |
| Thought speed | Spiritual | 27.8% | 14.9% | 53.5% | 8.8% |

\* For telepathy, "mentioned" means any communication mode was reported (telepathic, nonverbal or speech). The earlier figures (27.0% mentioned, 36.0% of mentioned) used a denominator that included "no communication".

Rank correlation between assigned degree and prevalence: Spearman ρ = −0.47 (predicted sign), p = 0.28, n = 7.

**Finding (H1 — not supported).** The most prevalent marker (reality certainty, 58.2%) and the least prevalent (thought speed, 14.9%) are both assigned to the spiritual degree; the celestial telepathy marker (27.0%) is as common as the natural memory marker (28.9%). The spread within the spiritual degree is larger than the differences between degrees. When a feature is mentioned at all, positive responses dominate (48–97%), so prevalence depends largely on whether the narrative addresses the feature.

### 3.2 Construct Validity (H2)

**Raw data.** All 21 pairwise correlations are positive and significant after Holm correction (phi 0.11–0.43; e.g. sensory × comparative reality 0.434, sensory × thought speed 0.423, memory × reality 0.415, time × thought speed 0.391, comparative reality × telepathy 0.239, memory × telepathy 0.110).

| Test | Value |
|------|-------|
| KR-20 | 0.738 |
| Kaiser-Meyer-Olkin (KMO) | 0.817 |
| Bartlett's χ² (df = 21) | 8,480.5, p ≈ 0 |

**Controlling for narrative length.** Longer narratives mention more of everything, so part of the inter-marker correlation could be reporting completeness. After residualising each marker on log word count:

| Quantity | Raw | Length-controlled |
|---|---|---|
| Mean inter-marker correlation | 0.291 | 0.149 |
| Positive pairs | 21/21 | 20/21 |
| Significant after Holm | 21/21 | 18/21 |
| Six non-telepathic markers: mean r; significant | — | 0.194; 15/15 |
| Telepathy with the other six | 0.11–0.24 | −0.03 to 0.05; 0.13 with comparative reality |

KR-20 computed within narrative-length quintiles: 0.40, 0.42, 0.48, 0.58, 0.65 (shortest to longest).

**Finding (H2 — supported for six markers).** About half of the raw shared variance is narrative length, but six markers — vividness, memory, reality certainty, time, thought speed and comparative reality — remain positively and significantly inter-correlated after length control. A perceptual construct exists that is not reducible to "longer accounts mention more." Telepathic communication, by contrast, is related to the others almost entirely through length; its membership in the scale is not supported once length is controlled. The earlier reading of telepathy's weak correlations as a sign of its "higher-degree" status was a post-hoc interpretation rather than a test.

### 3.3 Factor Structure (H3)

| Matrix | Eigenvalues (first 3) | Retention |
|---|---|---|
| Phi (raw) | 2.798, 0.940, 0.858 | Kaiser: 1 factor; parallel analysis (95th pct 1.062, 1.040, 1.023): 1 factor |
| Tetrachoric (raw) | 4.114, 0.888, 0.684 | Kaiser: 1 factor |
| Phi (length-controlled) | 1.996, 1.066, 1.038 | Parallel analysis (1.061, 1.039, 1.022): 3 components, the 2nd and 3rd marginally |

**One-factor solution (raw, minres).** Loadings: sensory vividness 0.68, comparative reality 0.59, reality certainty 0.58, thought speed 0.55, memory 0.55, time 0.54, telepathy 0.30 (30.5% of variance). On the tetrachoric matrix: 0.40 (telepathy) to 0.83.

**The previously reported two-factor solution** (18.1% + 16.8% of variance) was imposed rather than found. Its second factor — thought speed (0.64) and time perception (0.51) — does not reproduce the degree assignment.

**Length-controlled structure.** The second component contrasts time perception, thought speed and telepathy (loadings 0.46, 0.33, 0.53) with memory and reality certainty (−0.49, −0.45); the third is dominated by telepathy (0.76). In a two-factor minres solution on the length-controlled matrix, thought speed, sensory vividness and time load on one factor (0.58, 0.44, 0.40), and memory, reality certainty and sensory vividness on the other (0.49, 0.49, 0.40); telepathy loads on neither.

**Finding (H3 — not supported).** On the raw data, every criterion retains one factor. After length control, weak additional dimensions appear, but they do not follow the proposed assignment: reality certainty (spiritual) groups with memory (natural), and the two celestial markers do not form a factor. The data describe one dominant dimension of perceptual intensity, with minor sub-structure that does not correspond to discrete degrees.

### 3.4 The Score Distribution (H6)

| Score | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| Observed % | 27.4 | 21.9 | 16.7 | 12.6 | 9.5 | 5.8 | 3.9 | 2.3 |
| If markers were independent % | 8.2 | 27.0 | 33.7 | 21.6 | 7.8 | 1.6 | 0.2 | 0.0 |

Mean 1.99, median 2. Skewness 0.82 observed vs 0.33 under independence. Tiers: 0 markers 1,848 (27.4%); 1–2 markers 2,603 (38.6%); 3–4 markers 1,492 (22.1%); 5–7 markers 808 (12.0%).

| Narrative length quintile | Median words | Mean score | % scoring 0 |
|---|---|---|---|
| Q1 (shortest) | 187 | 0.52 | 64.8% |
| Q2 | 376 | 1.10 | 36.7% |
| Q3 | 684 | 1.60 | 23.7% |
| Q4 | 1,277 | 2.79 | 8.5% |
| Q5 (longest) | 2,417 | 3.96 | 3.0% |

Score vs word count: Spearman ρ = 0.67; log word count alone explains R² = 0.41.

**Finding (H6 — observed, not diagnostic).** The earlier claim that the right skew is "exactly what discrete degree theory predicts," and that random markers would be "roughly normal," is incorrect: independent markers with these prevalences are also right-skewed. What distinguishes the observed distribution is the excess of zeros (27.4% vs 8.2%) and of scores 5–7 (12.0% vs 1.8%) — the signature of a common factor (§3.2). That factor is strongly tied to narrative length, so part of the "gradient" is a gradient of reporting detail. The distribution is consistent with the discrete-degrees prediction but equally with a reporting-completeness model, and does not discriminate between them.

Marker prevalence by tier (included for completeness; tiers are defined by the markers themselves, so rising rates are expected):

| Marker | Score 1–2 | Score 3–4 | Score 5–7 |
|--------|-----------|-----------|-----------|
| Reality certainty | 65.3% | 95.4% | 99.5% |
| Telepathic | 26.4% | 40.2% | 66.0% |
| Memory persistence | 17.9% | 54.9% | 81.9% |
| Sensory vividness | 16.9% | 65.5% | 95.9% |
| Time perception | 10.2% | 36.4% | 82.2% |
| Thought speed | 3.6% | 23.4% | 69.8% |
| Comparative reality | 2.9% | 27.2% | 75.2% |

### 3.5 Being of Light and Perceptual Depth (H4)

| Metric | With BoL (n=797) | Without BoL (n=5,954) |
|--------|-------------------|----------------------|
| Mean score | 2.95 | 1.86 |
| Median score | 3 | 1 |
| Std Dev | 2.03 | 1.82 |
| Median narrative length (words) | 1,238 | 626 |

t = 15.61, p = 5.5 × 10⁻⁵⁴; Mann-Whitney U = 3,122,058, p = 1.6 × 10⁻⁴⁹; Cohen's d = 0.589. Being-of-Light accounts are about twice as long. Adjusted for log word count, the difference is **+0.39 markers** (95% CI 0.28–0.49, p = 3 × 10⁻¹²), down from +1.09.

| Marker | Degree | With BoL | Without | χ² | Crude OR | Length-adjusted OR (95% CI) | Adjusted p |
|--------|---|----------|-------------|-----|---|---|---|
| Telepathic | Celestial | 59.8% | 22.6% | 494.0 | 5.11 | **3.90 (3.31–4.59)** | 7 × 10⁻⁶⁰ |
| Comparative reality | Celestial | 32.6% | 13.9% | 180.3 | 2.99 | **1.87 (1.56–2.25)** | 2 × 10⁻¹¹ |
| Reality certainty | Spiritual | 71.9% | 56.3% | 69.3 | 1.98 | 1.07 (0.88–1.29) | 0.50 |
| Sensory vividness | Natural | 44.3% | 30.9% | 56.8 | 1.78 | 1.02 (0.86–1.21) | 0.81 |
| Time perception | Spiritual | 31.7% | 20.5% | 51.5 | 1.80 | 0.95 (0.79–1.14) | 0.58 |
| Thought speed | Spiritual | 20.8% | 14.1% | 24.5 | 1.60 | 0.78 (0.63–0.96) | 0.019 |
| Memory persistence | Natural | 34.0% | 28.2% | 11.4 | 1.31 | 0.74 (0.62–0.88) | 0.0008 |

Communication of any kind: 88.8% of Being-of-Light accounts vs 51.8% of others. Among accounts reporting communication, telepathy: 67.4% vs 43.6%.

**Finding (H4 — partially supported).** Crude differences favour Being-of-Light accounts on every marker, but most of this follows narrative length. After adjustment, only the two markers assigned to the celestial degree remain elevated — comparative reality ("more real than real") and telepathy — while memory persistence and thought speed are *lower* in Being-of-Light accounts. The concentration of the surviving effect on the celestial markers is a framework-consistent pattern (**reasonable interpretation**). Two qualifications apply: it rests on two markers, and the telepathy effect is partly structural, since a being must be present for communication, although telepathy remains more common among communicators in Being-of-Light encounters.

### 3.6 Cultural Invariance (H5)

| Religious background | N | % of all |
|----------|---|---|
| Not mentioned | 5,122 | 75.9% |
| Christian | 1,282 | 19.0% |
| Other | 115 | 1.7% |
| Atheist/agnostic | 100 | 1.5% |
| Muslim | 43 | 0.6% |
| Jewish | 38 | 0.6% |
| Spiritual, not religious | 22 | 0.3% |
| Hindu | 15 | 0.2% |
| Buddhist | 14 | 0.2% |

Among the seven named backgrounds (n = 1,514; 84.7% Christian):

| Religion | N | Mean Score | Std Dev | Median |
|----------|---|-----------|---------|---|
| Christian | 1,282 | 3.48 | 1.90 | 3 |
| Atheist/agnostic | 100 | 3.48 | 1.82 | 3 |
| Muslim | 43 | 3.26 | 1.88 | 3 |
| Jewish | 38 | 3.82 | 1.63 | 4 |
| Spiritual, not religious | 22 | 3.59 | 1.56 | 3 |
| Hindu | 15 | 3.40 | 1.45 | 3 |
| Buddhist | 14 | 3.57 | 1.50 | 3 |

ANOVA F(6, 1507) = 0.331, p = 0.921, η² = 0.0013; Kruskal–Wallis H = 1.87, p = 0.931.

**Christian vs atheist/agnostic:** difference −0.005 markers (95% CI −0.38 to +0.37); **TOST equivalence within ±0.5 markers, p = 0.005**. The groups write accounts of similar length (median 1,703 vs 1,653 words); length-adjusted difference +0.02 (95% CI −0.30 to +0.35).

| Marker | χ² | df | p | Cells with expected < 5 | Holm p |
|--------|-----|---|---|---|---|
| Memory persistence | 13.5 | 6 | 0.036 | 0% | 0.25 |
| Telepathic | 9.3 | 6 | 0.155 | 7% | 0.93 |
| Reality certainty | 6.1 | 6 | 0.414 | 29% | 1.00 |
| Thought speed | 5.3 | 6 | 0.506 | 0% | 1.00 |
| Time perception | 3.3 | 6 | 0.775 | 0% | 1.00 |
| Sensory vividness | 2.8 | 6 | 0.836 | 0% | 1.00 |
| Comparative reality | 2.7 | 6 | 0.850 | 14% | 1.00 |

**Narrative-detail selection.** Accounts that state a religion score much higher than those that do not (3.48 vs 1.52; t = 40.04, d = 1.17) and are much longer (median 1,674 vs 488 words). All religion comparisons are therefore within a subgroup of long, detailed accounts.

**Finding (H5 — supported for Christian vs non-religious).** Christian and atheist/agnostic experiencers have the same perception profile, and the equivalence test shows that any difference is smaller than half a marker — positive evidence of invariance, not merely a failure to find a difference. Religion explains 0.1% of variance, and no marker differs after multiple-comparison correction. For other traditions (n = 14–43) the data are too sparse for equivalence claims.

---

## 4. Discussion

### 4.1 Summary

| Hypothesis | Result | Assessment |
|---|---|---|
| H1 Prevalence hierarchy | Most and least prevalent markers both "spiritual"; ρ = −0.47, p = 0.28 | **Not supported** |
| H2 Coherent construct | KR-20 0.74, KMO 0.82; six markers cohere after length control (15/15) | **Supported** (six markers); telepathy's membership is a length artefact |
| H3 Degree-aligned factors | One factor by every criterion; weak length-controlled sub-structure not degree-aligned | **Not supported** |
| H6 Gradient | Right-skewed with excess 0s and 5–7s; 41% of variance is narrative length | Observed, **not diagnostic** |
| H4 Being of Light ↔ deeper perception | d = 0.59 crude; +0.39 adjusted; celestial markers only (OR 1.87, 3.90) | **Partially supported** |
| H5 Religious invariance | Christian = atheist/agnostic (TOST p = 0.005; adjusted diff +0.02) | **Supported** for Christian vs non-religious |

### 4.2 Interpretation

**Statistically supported.**
- A perceptual construct of six markers exists in NDE accounts, beyond what narrative length produces.
- It does not differ between Christian and non-religious experiencers.
- Being-of-Light accounts show more "more real than real" and telepathic perception after length adjustment.

**Reasonable interpretation.** The religious invariance fits the framework's "constant state, variable form". The underlying state does not depend on the experiencer's religious repertoire. This result does not, on its own, discriminate between the framework and a universal neurophysiological account, which also predicts invariance. The framework does, however, predict this result, and religious-priming accounts predict the opposite; so with respect to priming it is a hit. The concentration of the Being-of-Light effect on the celestial markers is likewise the pattern the framework predicts.

**Not supported.** The data do not show *discrete* degrees: there is no prevalence hierarchy, and the factors are not degree-aligned. What they show is a single intensity dimension. Discrete degrees might still describe the experience. But these seven markers, as coded, cannot resolve them, or the degree assignments are wrong.

**Withdrawn.** The earlier version said the framework "outperforms the materialist null hypothesis (which predicts no coherent structure) and the universal activation hypothesis (which predicts a left-skewed distribution)". Neither alternative was specified or tested, and the claim is withdrawn.

### 4.3 Speculative Extension

The earlier version linked these findings to the 32 geometric signs found in European Palaeolithic caves, reading them as a possible "correspondential vocabulary" encoding directly perceived meaning. Nothing in this dataset bears on that hypothesis. It remains a **speculative** direction, not an implication of these results.

### 4.4 Limitations

1. **Narrative length**: explains 41% of score variance; adjustment for word count is a partial control, because length may itself partly reflect experiential depth.
2. **"Not mentioned" coded as absent**: scores mix experience with reporting completeness.
3. **AI-extracted data**: GPT-5.2 coding. Inter-coder agreement is high for telepathy (κ = 0.88) and acceptable for comparative reality (κ = 0.74, test–retest 0.58); the other five markers are untested.
4. **Sample composition**: one of the seven named religious backgrounds is stated in 22.4% of accounts (24.1% including "other"), 84.7% of them Christian; other traditions n = 14–43.
5. **Self-selected, predominantly Western archives.**
6. **Degree assignment is theoretical**: the mapping of markers to degrees is not empirically derived, and the data do not recover it.

### 4.5 Future Directions

1. Second coding of the five untested markers on a random subsample, as done for telepathy and comparative reality in `08_extraction_reliability.ipynb`
2. Confirmatory factor analysis comparing a one-factor model with a three-factor degree model, with narrative length as a covariate, ideally on graded rather than binary items
3. Non-Western samples with adequate size for equivalence tests in each tradition
4. Separating "not mentioned" from "absent" through structured follow-up questionnaires

---

## 5. Conclusion

Seven perception markers from 6,751 NDE accounts form an internally consistent scale (KR-20 = 0.74). Six of them still cohere after controlling for how much each account says, so the construct is not an artefact of narrative length. Telepathic communication is the exception. The construct is the same in Christian and non-religious experiencers (equivalence within ±0.5 markers), consistent with a universal perceptual state rather than religious priming.

Being-of-Light encounters are associated with more "more real than real" and telepathic perception, even after length adjustment. These are the two markers assigned to the celestial degree. The predictions specific to *discrete* degrees are not supported: no prevalence hierarchy, and a single dominant factor rather than degree-aligned strata. The right-skewed "gradient" is real but does not discriminate between models.

The framework's prediction of a constant underlying state is supported against religious priming. Its prediction of discrete perceptual degrees is not supported by these markers.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry*, 25(4), 269–276.

Horn, J. L. (1965). A rationale and test for the number of factors in factor analysis. *Psychometrika*, 30(2), 179–185.

Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Parnia, S., et al. (2014). AWARE—AWAreness during REsuscitation—A prospective study. *Resuscitation*, 85(12), 1799–1805.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Swedenborg, E. (1758). *Heaven and Hell* (§§ 38–39, 267–270). Swedenborg Foundation.

Swedenborg, E. (1763). *Divine Love and Wisdom* (§§ 173–281). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Variables | Statistic | df | p-value |
|------|-----------|-----------|-----|---------|
| KR-20 | 7 markers | 0.738 | — | — |
| KMO | 7 markers | 0.817 | — | — |
| Bartlett's sphericity | 7 markers | χ² = 8,480.5 | 21 | ≈ 0 |
| Spearman | Degree rank × prevalence (H1) | ρ = −0.47 | n = 7 | 0.28 |
| Spearman | Score × word count | ρ = 0.67 | — | ≈ 0 |
| Partial correlations | 6 non-telepathic markers, length-controlled | mean r = 0.194 | — | 15/15 Holm < 0.05 |
| Independent t-test | BoL × score | t = 15.61 | 6,749 | 5.5 × 10⁻⁵⁴ |
| Mann-Whitney U | BoL × score | U = 3,122,058 | — | 1.6 × 10⁻⁴⁹ |
| OLS (length-adjusted) | BoL × score | +0.39 (0.28–0.49) | — | 3 × 10⁻¹² |
| Logistic (length-adjusted) | Telepathic × BoL | OR = 3.90 | — | 7 × 10⁻⁶⁰ |
| Logistic (length-adjusted) | Comparative reality × BoL | OR = 1.87 | — | 2 × 10⁻¹¹ |
| One-way ANOVA | Religion × score | F = 0.331, η² = 0.0013 | 6, 1507 | 0.921 |
| Kruskal–Wallis | Religion × score | H = 1.87 | 6 | 0.931 |
| TOST (±0.5) | Christian vs atheist/agnostic | diff = −0.005 | — | 0.005 |

## Appendix B: Data Access

- **Repository**: [structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **Analysis notebook**: `projects/nde/notebooks/06_cognitive_mode_profile.ipynb`
- **Structured data**: `projects/nde/structured/*.json` (6,753 files; 6,751 unique narratives)
- **Extraction schema**: `projects/nde/models/questionnaire.py`
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
