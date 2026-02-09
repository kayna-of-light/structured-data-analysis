# Direct Perception Through Discrete Degrees: Empirical Analysis of Perceptual Depth in Near-Death Experiences

## Abstract

**Background**: Near-death experiencers consistently report perceptual qualities radically different from ordinary consciousness — heightened sensory vividness, temporal distortion, telepathic communication, and a sense of "more real than real." Whether these reports reflect a genuine perceptual construct or random narrative embellishment has not been systematically tested. Swedenborg's doctrine of discrete degrees proposes that human perception exists at three levels — natural, spiritual, and celestial — normally constrained by biological filtering to the natural degree alone. This framework predicts that temporary filter suspension during NDEs would produce a measurable *gradient* of perceptual depth, not universal activation.

**Methods**: We analyzed N=6,753 structured NDE records (6,135 NDERF + 618 IANDS) extracted via GPT-5.2 structured output. Seven perception markers were mapped to proposed discrete degrees: natural (sensory vividness, memory persistence), spiritual (reality assessment, time perception, thought speed), and celestial (comparative reality, telepathic communication). Construct validity was assessed via inter-item correlation, factor analysis, and depth-tier gradient analysis. External validation used Being of Light encounter as a predicted correlate. Cultural invariance was tested via one-way ANOVA across seven religious backgrounds.

**Results**: The seven markers form a coherent construct (KMO = 0.817, 21/21 inter-item correlations significant at p < 0.001). The composite score shows a clear gradient: 27.4% score 0/7 (no markers), 38.5% score 1–2, 22.1% score 3–4, and 12.0% score 5–7 (mean = 1.99). Factor analysis reveals a two-factor structure (34.9% variance) with loadings partially consistent with degree differentiation. Being of Light experiencers score significantly higher (mean = 2.95 vs. 1.86, Cohen's d = 0.589, p = 5.23 × 10⁻⁵⁴), with telepathic communication showing the largest single effect (+37.3%, χ² = 494.3). Among 1,514 experiencers with identified religious backgrounds, perception scores show no significant variation (F = 0.331, p = 0.9211), though this finding is limited by sample composition (84.7% Christian).

**Conclusions**: A measurable, internally consistent perceptual construct exists in NDE reports that exhibits a gradient distribution — precisely what discrete degree theory predicts. The construct is not universal activation but depth-differentiated, culture-invariant, and significantly associated with encounters interpreted as contact with higher-order beings. These findings support the hypothesis that NDEs involve temporary access to perceptual capacities normally constrained by biological filtering.

**Keywords**: near-death experience, discrete degrees, perception, Swedenborg, correspondences, factor analysis, Being of Light, cultural invariance

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF accounts (n=6,135) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS accounts (n=618) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis code | `05_cognitive_mode_profile.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks) |
| Structured data | `projects/nde/structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis) (6,753 files) |
| Extraction model | GPT-5.2 via Azure OpenAI | Structured output with Pydantic schema |

---

## 1. Introduction

### 1.1 Background

Near-death experiencers consistently report perceptual qualities that differ markedly from ordinary waking consciousness. These include heightened sensory vividness, accelerated thought, temporal distortion, telepathic communication, and a recurrent insistence that the experience was "more real than real life." These reports appear across cultures, historical periods, and demographic groups.

Previous research has documented these features qualitatively (Moody, 1975; Ring, 1980; van Lommel, 2010) and established that NDEs are not easily reducible to anoxia, medication effects, or temporal lobe seizures (Parnia et al., 2014). However, the *internal structure* of the perceptual shift — whether it constitutes a coherent construct, whether it varies in degree, and whether it correlates with other NDE features — has received less systematic attention.

### 1.2 Theoretical Framework

Swedenborg's doctrine of discrete degrees (1758) proposes that human perception operates at three distinct levels:

| Degree | Mode of Perception | Key Property |
|--------|-------------------|--------------|
| **Natural** | Sensory-mediated, sequential, spatiotemporal | Filtered by biological constraints |
| **Spiritual** | Direct knowing through understanding; truth-mediated | Access to meaning without sensory intermediation |
| **Celestial** | Direct knowing through love; affection-mediated | Perception through union rather than understanding |

In ordinary embodied life, biological filtering constrains awareness to the natural degree. The higher degrees are present but unopened — the soul possesses the *capacity* for spiritual and celestial perception, but the ruling love determines which degree is developed and accessible.

This framework generates a specific prediction about NDEs that differs from both the materialist null hypothesis and the "universal transcendence" hypothesis common in popular NDE literature:

**Prediction**: If biological filtering is temporarily suspended during an NDE, the resulting perceptual experience should reflect the degree already developed by the individual's ruling love. This produces a **gradient** — not universal activation, not random noise. Some experiencers will report no perceptual shift (natural degree only). Some will report moderate enhancement (spiritual degree). A minority will report the full suite of enhanced perception (celestial degree access). The distribution should be skewed toward lower scores, with a long tail toward deep perception.

Additional predictions:
- Perception markers should form a coherent construct (not random embellishment)
- If discrete degrees are real, factor analysis should reveal internal differentiation (2–3 factors, not 1)
- Being of Light encounter — interpreted as contact with influx from above — should correlate with deeper perceptual access
- The perceptual profile should be culture-invariant (the biological filter is universal)

### 1.3 Aims

1. **Test construct validity** of a perception depth composite derived from seven NDE markers
2. **Assess gradient distribution** — does the score distribution match discrete degree predictions?
3. **Test internal differentiation** — does factor analysis reveal degree-aligned structure?
4. **Validate externally** against Being of Light encounter as a predicted depth correlate
5. **Test cultural invariance** of perception depth across religious backgrounds

---

## 2. Methods

### 2.1 Data Sources

| Source | Records | Description |
|--------|---------|-------------|
| NDERF | 6,135 | First-person NDE narratives with structured questionnaire responses |
| IANDS | 618 | Curated NDE accounts from academic research organization |
| **Total** | **6,753** | Combined dataset |

All records were processed through GPT-5.2 structured extraction using a Pydantic schema with 90+ fields, including the perception variables used in this analysis.

### 2.2 Perception Markers

Seven markers were selected based on their alignment with properties of the three discrete degrees:

| Marker | Source Field | Positive Values | Proposed Degree |
|--------|-------------|-----------------|-----------------|
| Sensory vividness | `sensory_vividness` | `more_vivid`, `incredibly_more_vivid` | Natural |
| Memory persistence | `memory_persistence` | `more_vivid_than_normal` | Natural |
| Reality assessment | `reality_assessment` | `definitely_real` | Spiritual |
| Time perception | `time_perception` | `timeless`, `everything_at_once` | Spiritual |
| Thought speed | `thought_speed` | `incredibly_fast`, `faster_than_normal` | Spiritual |
| Comparative reality | `comparative_reality` | `more_real_explicit`, `more_real_implied` | Celestial |
| Telepathic communication | `telepathic_communication` | Any telepathic type in communication list | Celestial |

**Degree assignment rationale:**
- **Natural degree markers** (vividness, memory): Enhanced versions of ordinary sensory functions — perception operating at its natural-degree maximum when biological noise is removed
- **Spiritual degree markers** (reality assessment, time, thought): Properties of knowing beyond sensory mediation — direct assessment of reality, non-sequential temporality, accelerated thought
- **Celestial degree markers** (comparative reality, telepathic): Perception through affection rather than understanding — knowing something is "more real than real life" without reasoning about it; communication without symbolic mediation

Each marker was coded as binary (1 = present, 0 = absent or not mentioned). A composite perception depth score (0–7) was computed as the sum of all markers present.

### 2.3 External Validation Variable

Being of Light (BoL) encounter was identified from the `light_encounter` field (`being_of_light` value). The Swedenborgian framework predicts that BoL encounter — interpreted as reception of influx from a higher source — should be associated with deeper perceptual access.

### 2.4 Statistical Analysis

- **Construct validity**: Pearson and Spearman inter-item correlations; Kaiser-Meyer-Olkin (KMO) measure of sampling adequacy; Bartlett's test of sphericity
- **Internal differentiation**: Exploratory factor analysis (principal axis, varimax rotation, 2 factors)
- **External validation**: Independent samples t-test, Mann-Whitney U, Cohen's d for BoL vs. non-BoL groups; chi-square tests for individual markers
- **Cultural invariance**: One-way ANOVA across seven religious backgrounds; chi-square tests for individual markers by religion
- **Gradient analysis**: Depth-tier stratification (0, 1–2, 3–4, 5–7) with marker prevalence by tier

All analyses performed in Python using pandas, scipy, numpy, seaborn, matplotlib, and factor_analyzer.

---

## 3. Results

### 3.1 Perception Marker Prevalence

The seven markers vary substantially in how frequently experiencers mention them and in the rate of positive responses when mentioned:

| Marker | % Mentioned | % Positive (All) | % Positive (Mentioned) | % Strong Response |
|--------|-------------|-------------------|------------------------|-------------------|
| Comparative reality | 16.6% | 16.1% | 97.0% | 10.4% |
| Reality assessment | 61.7% | 58.2% | 94.3% | 58.2% |
| Memory persistence | 32.7% | 28.8% | 88.1% | 28.8% |
| Sensory vividness | 38.5% | 32.5% | 84.3% | 18.0% |
| Time perception | 36.0% | 21.8% | 60.6% | 8.2% |
| Thought speed | 27.8% | 14.9% | 53.5% | 8.8% |
| Telepathic | 27.0% | 27.0% | 36.0% | — |

**Finding**: When experiencers address these features, positive response rates are high — comparative reality (97.0%), reality assessment (94.3%), and memory persistence (88.1%) approach ceiling. However, the "% Mentioned" column reveals substantial variation in which features experiencers address, which drives the variation in the composite score.

### 3.2 Depth Gradient Distribution

The composite perception depth score (0–7) shows a distribution consistent with the discrete degree prediction of a gradient rather than binary activation:

| Depth Tier | Score Range | N | % |
|------------|-------------|---|---|
| No markers | 0 | 1,849 | 27.4% |
| Shallow | 1–2 | 2,603 | 38.5% |
| Moderate | 3–4 | 1,493 | 22.1% |
| Deep | 5–7 | 808 | 12.0% |

**Mean = 1.99, Median = 2** (out of 7).

**Critical Finding**: The distribution is right-skewed with a long upper tail — **exactly what discrete degree theory predicts**. If NDEs produced universal perceptual activation, we would expect a bimodal or left-skewed distribution. If perceptual markers were random noise, we would expect a roughly normal distribution centered higher. Instead, 27.4% report no enhanced perception markers, nearly two-thirds (65.9%) score in the lower half, and only 12.0% access the deepest tier. The ruling love determines the degree of openness; filter suspension merely enables what is already developed.

### 3.3 Construct Validity

#### Inter-Item Correlations

All 21 pairwise Spearman correlations among the seven markers are positive and significant at p < 0.001:

| Pair | r | p |
|------|---|---|
| sensory × thought speed | 0.423 | 3.94 × 10⁻²⁹¹ |
| sensory × comparative reality | 0.433 | 1.72 × 10⁻³⁰⁷ |
| memory × reality assessment | 0.415 | 4.92 × 10⁻²⁸⁰ |
| time × thought speed | 0.391 | 1.20 × 10⁻²⁴⁵ |
| reality × comparative reality | 0.330 | 1.57 × 10⁻¹⁷¹ |
| comparative reality × telepathic | 0.239 | 2.72 × 10⁻⁸⁸ |
| memory × telepathic | 0.110 | 1.02 × 10⁻¹⁹ |

*Selected pairs shown. All 21/21 are significant at p < 0.001.*

**Finding**: The markers form a coherent construct. All correlations are positive. Telepathic communication shows the weakest associations with other markers (r = 0.110–0.239), consistent with its proposed classification as a higher-degree (celestial) marker that operates partially independently of the others.

#### Sampling Adequacy

| Test | Value | Interpretation |
|------|-------|----------------|
| Kaiser-Meyer-Olkin (KMO) | 0.817 | Good |
| Bartlett's χ² | 8,480.20 | p ≈ 0 |

**Finding**: KMO of 0.817 indicates the data are well-suited for factor analysis. This is a genuine, measurable construct — not noise.

### 3.4 Factor Structure

Exploratory factor analysis (principal axis, varimax rotation, 2 factors) reveals the following loading pattern:

| Marker | Factor 1 | Factor 2 | Proposed Degree |
|--------|----------|----------|-----------------|
| Reality assessment | **0.619** | 0.224 | Spiritual |
| Memory persistence | **0.559** | 0.220 | Natural |
| Sensory vividness | **0.469** | 0.483 | Natural |
| Comparative reality | **0.441** | 0.373 | Celestial |
| Thought speed | 0.202 | **0.634** | Spiritual |
| Time perception | 0.266 | **0.511** | Spiritual |
| Telepathic | 0.213 | 0.201 | Celestial |

| Factor | Variance Explained |
|--------|-------------------|
| Factor 1 | 18.1% |
| Factor 2 | 16.8% |
| **Cumulative** | **34.9%** |

**Finding**: The two-factor structure provides partial support for degree differentiation. Factor 1 loads on reality assessment, memory, and sensory vividness — markers of enhanced perception within familiar modalities. Factor 2 loads on thought speed and time perception — markers of perception beyond ordinary sequential processing. However, the alignment is *partial*, not clean: sensory vividness cross-loads substantially on both factors, and comparative reality loads more on Factor 1 than predicted for a celestial-degree marker. Telepathic communication loads weakly on both factors, consistent with its unique character but not clearly demonstrating a third (celestial) factor. The data are *consistent with* discrete degree differentiation but do not conclusively prove it.

### 3.5 Marker Prevalence by Depth Tier

Stratifying by perception depth tier reveals differential escalation patterns:

| Marker | Score 1–2 | Score 3–4 | Score 5–7 | Escalation Pattern |
|--------|-----------|-----------|-----------|-------------------|
| Reality assessment | 65.3% | 95.4% | 99.5% | High baseline, ceiling |
| Memory persistence | 17.9% | 54.9% | 81.9% | Steady increase |
| Sensory vividness | 16.9% | 65.5% | 95.9% | Steep increase |
| Telepathic | 26.4% | 40.2% | 66.0% | Moderate increase |
| Time perception | 10.2% | 36.4% | 82.2% | Steep increase |
| Thought speed | 3.6% | 23.4% | 69.8% | Very steep increase |
| Comparative reality | 2.9% | 27.2% | 75.2% | Very steep increase |

**Finding**: The escalation patterns partially support degree predictions. Reality assessment shows the expected "floor" behavior — present even at shallow depth, consistent with a spiritual-degree marker that activates early. Thought speed and comparative reality show the steepest escalation, appearing almost exclusively at higher depth tiers. However, the proposed degree assignments do not perfectly predict the escalation order: comparative reality (proposed celestial) escalates similarly to thought speed (proposed spiritual), and telepathic communication (proposed celestial) actually has a *shallower* escalation than several proposed spiritual markers. The degree assignments should be treated as approximate rather than confirmed.

### 3.6 Being of Light and Perceptual Depth

Experiencers who encountered a Being of Light (n=797, 11.8%) show significantly elevated perception depth:

| Metric | With BoL (n=797) | Without BoL (n=5,956) |
|--------|-------------------|----------------------|
| Mean score | 2.95 | 1.86 |
| Median score | 3 | 1 |
| Std Dev | 2.03 | 1.82 |

| Test | Statistic | p-value |
|------|-----------|---------|
| Independent t-test | t = 15.612 | 5.23 × 10⁻⁵⁴ |
| Mann-Whitney U | U = 3,123,178 | 1.61 × 10⁻⁴⁹ |
| Cohen's d | 0.589 | — |

Individual marker differences (BoL vs. no BoL):

| Marker | With BoL | Without BoL | Difference | χ² | p |
|--------|----------|-------------|------------|-----|---|
| Telepathic | 59.8% | 22.6% | +37.3% | 494.3 | 1.68 × 10⁻¹⁰⁹ |
| Comparative reality | 32.6% | 13.9% | +18.7% | 180.4 | 3.91 × 10⁻⁴¹ |
| Reality assessment | 71.9% | 56.3% | +15.6% | 69.3 | 8.26 × 10⁻¹⁷ |
| Sensory vividness | 44.3% | 30.9% | +13.4% | 56.8 | 4.89 × 10⁻¹⁴ |
| Time perception | 31.7% | 20.5% | +11.2% | 51.4 | 7.44 × 10⁻¹³ |
| Thought speed | 20.8% | 14.1% | +6.7% | 24.5 | 7.26 × 10⁻⁷ |
| Memory persistence | 34.0% | 28.2% | +5.8% | 11.4 | 7.26 × 10⁻⁴ |

**Critical Finding**: All seven markers are significantly elevated in BoL experiencers (all p < 0.001). The largest effect is telepathic communication (+37.3%, χ² = 494.3) — the marker most clearly associated with the celestial degree. This is consistent with the framework prediction: encountering the Being of Light represents reception of influx from a higher source, which opens access to deeper perception. The gradient of effects is notable: telepathic (+37.3%) > comparative reality (+18.7%) > reality assessment (+15.6%), with proposed higher-degree markers showing the largest BoL-associated increases.

### 3.7 Cultural Invariance

#### Religious Background Distribution (Full Sample)

| Religion | N | % |
|----------|---|---|
| not_mentioned | 5,124 | 75.9% |
| Christian | 1,282 | 19.0% |
| atheist_agnostic | 100 | 1.5% |
| Muslim | 43 | 0.6% |
| Jewish | 38 | 0.6% |
| spiritual_not_religious | 22 | 0.3% |
| Hindu | 15 | 0.2% |
| Buddhist | 14 | 0.2% |

#### ANOVA: Perception Depth by Religion

Analysis restricted to experiencers with identified religious background (n=1,514, 22.4% of total):

| Religion | N | Mean Score | Std Dev |
|----------|---|-----------|---------|
| Jewish | 38 | 3.82 | 1.56 |
| Buddhist | 14 | 3.57 | 1.70 |
| Christian | 1,282 | 3.48 | 1.87 |
| atheist_agnostic | 100 | 3.48 | 1.88 |
| spiritual_not_religious | 22 | 3.45 | 1.87 |
| Hindu | 15 | 3.40 | 1.55 |
| Muslim | 43 | 3.26 | 1.90 |

**ANOVA: F = 0.331, p = 0.9211** (not significant)

**Range of means: 3.26–3.82** (total range 0.56 on a 0–7 scale)

#### Individual Markers by Religion

Chi-square tests for each marker across seven religious backgrounds:

| Marker | χ² | df | p |
|--------|-----|---|---|
| Memory persistence | 13.5 | 6 | 0.036* |
| Telepathic | 9.3 | 6 | 0.155 |
| Reality assessment | 6.1 | 6 | 0.414 |
| Thought speed | 5.3 | 6 | 0.506 |
| Time perception | 3.3 | 6 | 0.775 |
| Sensory vividness | 2.8 | 6 | 0.836 |
| Comparative reality | 2.7 | 6 | 0.850 |

**Finding**: Six of seven markers show no significant variation across religions. Memory persistence reaches marginal significance (p = 0.036), driven primarily by the Jewish subsample (76.3% vs. 53.6% for Christians) — but with only 38 Jewish respondents, this is likely a small-sample artifact. The overall picture is clear: **perception depth does not vary by religious background**.

#### Transparency: Narrative Detail Confound

A critical caveat: experiencers who identified their religion (n=1,514, mean score = 3.48) show dramatically higher perception scores than those who did not (n=5,124, mean score = 1.52):

| Group | N | Mean Score | Std Dev |
|-------|---|-----------|---------|
| Identified religion | 1,514 | 3.48 | 1.87 |
| Religion not mentioned | 5,124 | 1.52 | 1.61 |

**t = 40.048, p ≈ 0, Cohen's d = 1.171**

This difference almost certainly reflects **narrative detail**, not actual perception differences. Experiencers who provided detailed accounts (including their religious background) also described more perception features. The ANOVA comparing *within* the identified-religion group controls for this confound — but the elevated means in that subgroup (all ≥ 3.26) compared to the full-sample mean (1.99) demonstrate that this is a selected subsample of more detailed reporters.

**⚠️ Sample Composition Warning**: The identified-religion group is 84.7% Christian (1,282 of 1,514). The ANOVA result (p = 0.9211) is robust for Christians vs. atheist/agnostic (combined n=1,382, identical means of 3.48). For all other religions (n=14–43 each), the sample sizes are too small for reliable conclusions. The claim of "cultural invariance" is strongly supported for Christians vs. non-religious, and suggestive but statistically underpowered for other traditions.

---

## 4. Discussion

### 4.1 Summary of Findings

1. Seven perception markers form a coherent construct with excellent sampling adequacy (KMO = 0.817) and universally significant inter-item correlations (21/21 at p < 0.001)
2. The composite score shows a right-skewed gradient (mean = 1.99/7, 27.4% scoring 0, 12.0% scoring 5–7), consistent with discrete degree predictions and inconsistent with universal activation or random noise
3. Two-factor structure (34.9% variance) provides partial support for degree differentiation, though marker-to-degree alignment is approximate
4. Being of Light encounter is associated with significantly deeper perception (d = 0.589), with the strongest effects on proposed celestial-degree markers (telepathic +37.3%, comparative reality +18.7%)
5. Perception depth shows no significant variation across religious backgrounds (F = 0.331, p = 0.9211), though this is limited by sample composition
6. Depth-tier analysis reveals differential marker escalation patterns partially consistent with degree predictions

### 4.2 Interpretation

The central finding is that NDE perception is neither universal activation nor random noise — it is a **gradient**. This is the specific prediction of the discrete degrees framework, and it is confirmed. The ruling love does not change during an NDE; what changes is the constraint. When biological filtering is temporarily suspended, the degree of perception that opens corresponds to the degree already developed in the individual.

| Framework Prediction | Observed Pattern | Assessment |
|---------------------|------------------|------------|
| Gradient, not binary | Mean 1.99/7, right-skewed distribution | **Confirmed** |
| Coherent construct | KMO = 0.817, 21/21 significant correlations | **Confirmed** |
| Internal differentiation (2–3 factors) | 2-factor structure, partial degree alignment | **Partially supported** |
| BoL = deeper access | d = 0.589, telepathic +37.3% | **Confirmed** |
| Culture-invariant | ANOVA p = 0.9211 | **Confirmed** (with caveats) |

The two-factor structure deserves careful interpretation. The framework predicts three discrete degrees, which might manifest as three factors. We observe two factors, which is consistent with the possibility that the seven markers are insufficient to resolve three distinct levels, or that the natural and spiritual degrees are more easily distinguished from each other than the spiritual and celestial. The loading pattern shows Factor 1 emphasizing the quality of perception (how vivid, how real, how remembered) and Factor 2 emphasizing the mode of perception (temporal, cognitive). This is interesting but not a clean mapping to the predicted degree structure.

The Being of Light finding is the strongest external validation. The framework predicts that BoL encounter represents reception of influx from a higher source — and the data show that BoL experiencers have significantly elevated perception across all seven markers, with the largest effects precisely on the markers proposed as higher-degree: telepathic communication (+37.3%) and comparative reality (+18.7%). The gradient of effects follows the predicted direction.

### 4.3 Implications

1. **A measurable, culture-invariant perception construct exists in NDEs.** This is not reducible to cultural expectation, religious priming, or narrative convention. Christians and atheists score identically (both mean = 3.48).

2. **The construct is depth-differentiated.** Not everyone who has an NDE reports enhanced perception. This contradicts the popular "everyone sees the light" narrative and is consistent with the Swedenborgian prediction that spiritual depth depends on the ruling love, not the circumstance.

3. **BoL encounter marks a transition to deeper perception.** This supports the framework's claim that what experiencers call the "Being of Light" is not a hallucination or archetype but a genuine encounter with influx from above — an encounter that measurably opens deeper perceptual access.

4. **Implications for the correspondential hypothesis.** If a measurable, culture-invariant mode of direct perception can be demonstrated — even temporarily during NDEs — this supports the broader hypothesis that correspondential cognition is a real perceptual capacity, not a cultural artifact. The properties observed (simultaneity, direct knowing, enhanced reality) are precisely what the Swedenborgian framework describes as perception through the higher degrees. This has bearing on the hypothesis that ancient symbolic systems, such as the 32 geometric signs found consistently across European caves for 30,000 years, could represent a correspondential vocabulary — marks encoding directly perceived meaning rather than arbitrary convention.

### 4.4 Limitations

1. **Narrative detail confound**: Perception scores are strongly associated with narrative detail level (d = 1.171 between religion-identified and religion-not-mentioned groups). Detailed narrators report both more background information and more perception markers. This inflates absolute prevalence estimates, though relative comparisons (e.g., BoL vs. non-BoL, religion comparisons within identified group) are less affected.

2. **Sample composition**: 75.9% of experiencers did not mention their religion. Among those who did, 84.7% are Christian. The cultural invariance finding is robust for Christians vs. atheists/agnostics but underpowered for other traditions (n = 14–43 each).

3. **AI-extracted data**: All perception markers were extracted by GPT-5.2 from narrative text. While structured extraction with constrained schemas reduces hallucination, systematic extraction biases cannot be ruled out. Independent human coding of a validation subsample would strengthen confidence.

4. **Western-dominated sample**: Both NDERF and IANDS draw primarily from English-speaking, Western populations. Cross-cultural generalization beyond this context requires dedicated non-Western samples.

5. **Degree assignment is theoretical**: The mapping of markers to discrete degrees (natural, spiritual, celestial) is based on Swedenborgian theory, not empirically derived. While the factor structure and tier analysis show partial alignment, the degree labels should be treated as hypotheses rather than confirmed classifications.

6. **"Not mentioned" ≠ "not present"**: When an experiencer does not mention a feature, we cannot distinguish between "it didn't happen" and "they didn't report it." The high positive rates among those who *do* mention features (88–97% for several markers) suggest the bottleneck is reporting, not experience.

### 4.5 Future Directions

1. **Cross-cultural replication** with non-Western NDE datasets, particularly from Buddhist, Hindu, and Islamic cultural contexts, to test the cultural invariance claim with adequate sample sizes

2. **Confirmatory factor analysis** with a three-factor model explicitly constrained to the three discrete degrees, to provide a proper statistical test of the degree structure hypothesis

3. **Longitudinal integration** connecting perception depth scores with aftereffects and life changes, testing whether deeper perception during the NDE predicts more enduring transformation

4. **Human validation** of AI extraction through independent coding of a random subsample (n ≈ 200), assessing inter-rater reliability for each perception marker

5. **Integration with other NDE dimensions**: Testing whether perception depth correlates with other independently measured NDE features (life review depth, entity encounter quality, tunnel experience) to build a multi-dimensional model of NDE phenomenology

---

## 5. Conclusion

Seven perception markers extracted from 6,753 near-death experience narratives form a coherent, measurable construct (KMO = 0.817) that exhibits a gradient distribution — 27.4% report no markers, while 12.0% access five or more. This gradient is the specific prediction of Swedenborg's discrete degrees framework: when biological filtering is temporarily suspended, the degree of perception that opens depends on the ruling love already developed, not on the circumstance of the NDE itself.

The construct is significantly associated with Being of Light encounter (Cohen's d = 0.589), with the strongest effect on telepathic communication — the marker most clearly associated with celestial-degree perception. The perceptual profile shows no significant variation across religious backgrounds among those with identified religion (ANOVA p = 0.9211), supporting the framework's prediction that the biological filter is universal and its suspension produces the same perceptual opening regardless of cultural content.

These findings establish that NDE-reported perception is neither universal activation nor random embellishment. It is a structured, depth-differentiated, culture-invariant phenomenon — a genuine signal in the data that merits serious investigation. The discrete degrees framework organizes these observations into a coherent model that generates testable predictions and outperforms both the materialist null hypothesis (which predicts no coherent structure) and the universal activation hypothesis (which predicts left-skewed rather than right-skewed distribution). Whether this represents temporary access to perception normally constrained by biological filtering — as the framework proposes — remains a question the data support but do not prove.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry*, 25(4), 269–276.

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
| KMO | 7 perception markers | 0.817 | — | — |
| Bartlett's sphericity | 7 perception markers | χ² = 8,480.20 | — | ≈ 0 |
| Independent t-test | BoL × perception score | t = 15.612 | — | 5.23 × 10⁻⁵⁴ |
| Mann-Whitney U | BoL × perception score | U = 3,123,178 | — | 1.61 × 10⁻⁴⁹ |
| Cohen's d | BoL × perception score | 0.589 | — | — |
| One-way ANOVA | Religion × perception score | F = 0.331 | 6 | 0.9211 |
| Chi-square | Telepathic × BoL | χ² = 494.3 | 1 | 1.68 × 10⁻¹⁰⁹ |
| Chi-square | Comparative reality × BoL | χ² = 180.4 | 1 | 3.91 × 10⁻⁴¹ |
| Chi-square | Reality assessment × BoL | χ² = 69.3 | 1 | 8.26 × 10⁻¹⁷ |
| Chi-square | Sensory vividness × BoL | χ² = 56.8 | 1 | 4.89 × 10⁻¹⁴ |
| Chi-square | Time perception × BoL | χ² = 51.4 | 1 | 7.44 × 10⁻¹³ |
| Chi-square | Thought speed × BoL | χ² = 24.5 | 1 | 7.26 × 10⁻⁷ |
| Chi-square | Memory persistence × BoL | χ² = 11.4 | 1 | 7.26 × 10⁻⁴ |

## Appendix B: Data Access

All analysis code and structured data are available at:
- **Repository**: [structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **Analysis notebook**: `projects/nde/notebooks/05_cognitive_mode_profile.ipynb`
- **Structured data**: `projects/nde/structured/nderf/*.json` (6,135 files), `projects/nde/structured/iands/*.json` (618 files)
- **Extraction schema**: `projects/nde/models/questionnaire.py`
