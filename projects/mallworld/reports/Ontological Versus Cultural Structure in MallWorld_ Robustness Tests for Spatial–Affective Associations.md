# Ontological Versus Cultural Structure in MallWorld: Robustness Tests for Spatial–Affective Associations

## Abstract

The MallWorld corpus—a collection of dream reports from the r/themallworld subreddit—exhibits striking regularities in the pairing of spatial motifs with affective atmospheres. Malls, transit corridors, and vertical transitions recur alongside descriptions of ominous, liminal, or celebratory moods. A central methodological question is whether these patterns reflect genuine cross-person structure or arise from more prosaic sources: author-specific stylistic habits, short-lived cultural fads, or imitation cascades within the community. This study addresses that question through a battery of robustness tests designed to challenge "cultural artifact" explanations directly.

Using structured extraction outputs from 1,926 dream reports contributed by 1,292 unique authors, we examined two core categorical associations: location type paired with atmosphere, and vertical position paired with atmosphere. Both associations proved highly significant in the full sample, with effect sizes in the small-to-medium range (Cramér's V = 0.21 and 0.14, respectively). More importantly, these effects survived four stringent robustness checks: time-split stability analysis revealed no meaningful drift between recent and earlier posts; author-holdout tests showed near-identical effect sizes across independent author subsets; removal of the most prolific contributors produced only gradual attenuation rather than collapse; and within-author permutation nulls—which preserve each author's base rates while destroying cross-author structure—yielded effect sizes less than half the observed values (p < 0.001 in both cases).

These findings disfavor narrow explanations attributing MallWorld's spatial–affective regularities to a small cadre of influential posters, to time-local memetic drift, or to author-specific stylistic priors. The results support the existence of genuine cross-person structure linking spatial descriptors to affective atmosphere, warranting deeper comparative modeling work and extension to additional phenomenological domains.

**Keywords**: MallWorld, collective dream phenomenology, categorical association, Cramér's V, robustness testing, author controls, permutation null, time stability

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| Raw MallWorld corpus | r/themallworld posts | Local repository (`data/mallworld/`) |
| Structured extractions | LLM-based extraction pipeline | Local repository (`projects/mallworld/structured/`) |
| Analysis notebook | Jupyter notebook | `11_ontological_vs_cultural_tests.ipynb` |
| Extraction schema | Pydantic models | `projects/mallworld/models/questionnaire.py` |

---

## 1. Introduction

### 1.1 Background

The analysis of collective dream corpora presents a distinctive methodological challenge. When hundreds or thousands of individuals report dreams featuring similar motifs—recurring malls, endless corridors, escalators that malfunction, underground passages suffused with unease—the analyst confronts an attribution problem. Do these regularities emerge from shared phenomenological structure, from cultural templates absorbed through media exposure, or from dynamics internal to the reporting community itself? The MallWorld subreddit, where users share dreams of visiting an uncanny, labyrinthine commercial space, offers an unusually rich test case for distinguishing among these possibilities.

Prior exploratory analyses of this corpus have documented the prevalence of certain spatial categories (malls, hotels, transit hubs, parking structures) and their frequent co-occurrence with specific affective atmospheres (ominous, liminal, neutral, occasionally celebratory). What remains unclear is whether these associations represent something more than statistical artifacts of how dream reports are written and shared online. If a handful of prolific contributors set the stylistic tone, or if atmospheric language drifts with subreddit fashions over time, the apparent regularities may tell us more about community dynamics than about dream phenomenology.

### 1.2 Theoretical Framework

This investigation adopts an empirical-first stance. The Swedenborgian correspondential framework—which posits systematic relationships between spatial symbolism and affective or spiritual states—serves here as a hypothesis generator rather than an assumed authority. Before adjudicating between correspondential interpretations and cultural-schema explanations, we must first establish whether the patterns in question are robust to strong falsification-style controls. A pattern that collapses when prolific authors are removed, or that reverses direction over time, or that disappears when author base rates are controlled, cannot bear the interpretive weight that either framework would place upon it.

### 1.3 Aims

This study pursues five interlocking aims. First, we test whether location type and atmosphere exhibit a statistically significant association at non-trivial effect sizes. Second, we perform the same test for vertical position and atmosphere, given the theoretical importance of verticality in correspondential frameworks. Third, we evaluate temporal stability by comparing effect sizes in recent versus earlier posts. Fourth, we assess generalizability across authors through holdout validation and sensitivity analyses that progressively remove the most prolific contributors. Fifth, and most stringently, we employ within-author permutation nulls that preserve each author's base rates while destroying any cross-author structure, asking whether the observed associations exceed what author-level confounding alone could produce.

---

## 2. Methods

### 2.1 Data Sources

The dataset comprises MallWorld posts stored locally with corresponding structured extraction outputs generated through an LLM-based pipeline. Each post was processed to extract spatial, atmospheric, and entity-level features according to a predefined schema. A dream-level metadata table was constructed by joining each structured record to its source JSON, enabling author-based analyses.

The resulting dataset included 1,926 dream reports from 1,292 unique authors. Author identification was available for the full corpus, though demographic metadata proved sparse: gender information was present for only 1.6% of dreamers, and age range for 8.6%. This sparsity precluded meaningful demographic stratification, focusing the robustness battery instead on author identity and temporal position.

### 2.2 Variables

Two primary categorical associations were examined:

The first paired **location type** with **atmosphere**. Location type refers to the categorical label assigned to each spatial setting within a dream (e.g., mall, hotel, hallway, parking structure, transit hub). Atmosphere captures the affective quality of that setting as described in the narrative (e.g., ominous, liminal, neutral, celebratory, surreal). Both variables were extracted at the location level, meaning that dreams featuring multiple locations contributed multiple observations.

The second association paired **vertical position** with **atmosphere**. Vertical position encodes the elevation of a location relative to ground level (underground, below ground, ground, above ground, elevated, high elevation). This variable carries theoretical weight in correspondential frameworks, where descent often signifies movement toward material or self-oriented states, and ascent toward more open or spiritual states.

Per project convention, observations coded as "not mentioned" were treated as missing and excluded from the corresponding analysis. This conservative approach ensures that associations reflect explicit narrative content rather than extraction defaults.

### 2.3 Statistical Analysis

Association testing employed chi-square tests of independence on contingency tables crossing each spatial variable with atmosphere. Effect sizes were quantified using Cramér's V, computed as $V = \sqrt{\chi^2 / (n(k-1))}$ where $k$ equals the smaller of the row and column counts. By convention, V values around 0.10 indicate small effects, 0.30 medium effects, and 0.50 large effects, though interpretation depends on context and dimensionality.

Four robustness tests were applied to challenge cultural-artifact explanations:

**Time-split stability** divided records into "recent" and "earlier" strata based on posting date and compared Cramér's V within each stratum. A permutation test assessed whether the observed between-stratum spread in V exceeded chance expectation.

**Author-holdout stability** repeatedly split the author set at random, computing V separately in the training and test halves. Over 300 such splits, the distribution of train-test V differences characterized how well the association generalizes to held-out authors.

**Prolific-author sensitivity** recomputed V after progressively removing the top-k contributors by post count (k = 1, 5, 10, 25, 50, 100). If the association depends critically on a small number of influential voices, V should collapse as those authors are removed.

**Within-author permutation nulls** represent the most stringent test. By shuffling the atmosphere labels within each author—thereby preserving each author's base rates and stylistic tendencies while destroying any cross-author structure—we generate a null distribution against which the observed V can be compared. If the association merely reflects author-level confounding (e.g., some authors always write ominous atmospheres regardless of location), the within-author null should approach the observed effect.

---

## 3. Results

### 3.1 Location Type and Atmosphere

In the full filtered sample of 4,306 location observations, location type and atmosphere were strongly non-independent (χ² = 1,737.99, df = 621, p = 2.13 × 10⁻¹⁰⁶). The association's magnitude, Cramér's V = 0.212, falls in the small-to-medium range for a contingency table of this dimensionality (70 location types × 10 atmosphere categories). This indicates that knowing a location's type provides meaningful, though not deterministic, information about its likely atmosphere.

Temporal stability analysis revealed no evidence of drift. Splitting the corpus into earlier and recent halves yielded V = 0.169 and V = 0.178, respectively—a spread of 0.009 that fell well within the permutation null distribution (p = 0.54). The association's strength has remained essentially constant across the subreddit's history.

Author-holdout validation confirmed generalizability. Across 300 random author splits, the mean V in training halves was 0.172 (SD = 0.010), and in test halves 0.171 (SD = 0.009). The median absolute difference between train and test was just 0.013, with 90% of splits showing differences below 0.029. The association replicates robustly in author subsets never seen during training.

Removing prolific contributors produced gradual attenuation rather than collapse. With no authors removed, V = 0.170; after removing the single most prolific author, V = 0.171; after removing the top 10, V = 0.164; after removing the top 100 (leaving 830 authors and 2,349 observations), V = 0.142. The association weakens by about 16% when the most active contributors are excluded—a noticeable but far from fatal reduction. The pattern clearly does not depend on a handful of dominant voices.

The within-author permutation null delivered the most decisive evidence. In 3,992 observations from 930 authors, the observed V was 0.170. The null distribution—generated by shuffling atmosphere labels within each author over 1,000 iterations—yielded a mean V of just 0.059, with a 90th percentile of 0.068 and a maximum of 0.081. The observed effect exceeds the null maximum; the permutation p-value is 0.001 (the minimum resolvable with 1,000 iterations). The association between location type and atmosphere cannot be explained by author-specific base rates alone.

### 3.2 Vertical Position and Atmosphere

The vertical position analysis drew on 1,955 observations where both vertical position and atmosphere were explicitly mentioned. The association was again highly significant (χ² = 203.50, df = 45, p = 4.97 × 10⁻²²), with Cramér's V = 0.144. Though smaller than the location-type effect, this magnitude remains noteworthy for a 6 × 10 contingency table.

Temporal stability held for vertical position as well. Earlier and recent strata showed V = 0.130 and V = 0.144, respectively—a spread of 0.014 that did not differ from the permutation null (p = 0.56). Whatever drives the vertical–affective coupling has been present throughout the corpus's temporal span.

Author-holdout validation again supported generalizability. Over 300 splits, the mean training V was 0.139 (SD = 0.014) and the mean test V was 0.136 (SD = 0.014). Median absolute train-test difference was 0.017, with 90% of splits differing by less than 0.046. The vertical–atmosphere association is not an artifact of fitting to a particular author subset.

Sensitivity to prolific authors showed modest but stable decline. With all 609 authors included, V = 0.136; after removing the top 10, V = 0.131; after removing the top 100 (leaving 509 authors and 1,068 observations), V = 0.121. The 11% reduction parallels the location-type pattern: prolific contributors amplify the signal but do not create it.

Within-author permutation nulls again showed the observed effect far exceeding what author-level confounding could produce. The observed V of 0.136 compared to a null mean of 0.060, a 90th percentile of 0.073, and a maximum of 0.093. The permutation p-value was 0.001. Vertical position's association with atmosphere is not reducible to author stylistic priors.

---

## 4. Discussion

### 4.1 Summary of Findings

The evidence supports three empirical conclusions. First, both location type and vertical position are meaningfully associated with atmosphere in MallWorld dream reports, with effect sizes in the small-to-medium range. Second, these associations are temporally stable: effect sizes in recent posts do not differ significantly from those in earlier posts. Third, the associations generalize across authors and survive stringent controls for author-level confounding: author-holdout validation shows near-identical effects in independent author subsets, removal of prolific contributors produces only gradual attenuation, and within-author permutation nulls fall far short of the observed effects.

### 4.2 Interpretation

These findings elevate the spatial–affective couplings from "statistically significant" to "robust under adversarial challenge." The robustness battery was specifically designed to give cultural-artifact explanations every opportunity to succeed. If the patterns reflected a few prolific posters imposing their style, dropping those posters should collapse the effect; it did not. If the patterns reflected time-local meme drift, earlier and recent strata should diverge; they did not. If the patterns reflected author-specific base rates—some authors invariably writing ominous atmospheres regardless of spatial content—within-author permutation nulls should approximate the observed effect; they fell to less than half.

What remains possible, and indeed likely, is that cultural schemas constrain expression in ways that extend across many authors and persist over time. Such schemas could reflect absorbed media templates, genre conventions of dream narration, or implicit subreddit norms about how MallWorld experiences "should" be described. Robustness to the present battery does not rule out cultural determination; it rules out the narrower claim that the patterns are driven by a small number of authors or a fleeting stylistic fad.

The theoretical question—whether these stable cross-person regularities reflect merely cultural constraint or something deeper, such as shared phenomenological structure or correspondential relationships—cannot be resolved by robustness testing alone. What robustness testing establishes is that the regularities are real enough, and stable enough, to warrant that deeper inquiry.

### 4.3 Implications

Methodologically, this analysis demonstrates the value of within-author permutation nulls for collective narrative corpora. Standard significance testing on large community datasets risks mistaking author-level confounding for genuine content-level structure. The within-author null directly controls for this threat and should become a routine check in phenomenological corpus analysis.

Substantively, the findings support the premise that MallWorld contains lawful structure worth modeling. The spatial–affective couplings documented here are not noise, not artifacts of a few dominant voices, and not ephemeral community fashions. They represent genuine regularities that any explanatory account—whether cultural, psychological, or correspondential—must accommodate.

### 4.4 Limitations

Several limitations warrant acknowledgment. First, the structured labels depend on LLM-based extraction, which may introduce misclassification or category drift. Second, some posts in the corpus may not represent genuine dream reports (e.g., AI-generated visualizations, meta-commentary); while filtering was applied, edge cases likely remain. Third, demographic metadata was too sparse to support meaningful stratification by gender or age, leaving open the question of whether associations differ across demographic subgroups. Fourth, tests were computed at the location level rather than the dream level, meaning that dreams featuring multiple locations contributed multiple observations; this inflates sample size but may also capture meaningful within-dream variation.

### 4.5 Future Directions

Several extensions suggest themselves. The robustness battery should be applied to entity variables (entity type × demeanor, authority nature × interaction outcome) to assess whether the patterns documented here generalize to the social dimension of MallWorld experience. Within-dream negative controls—shuffling atmosphere labels among locations within the same dream—could isolate within-dream narrative coherence effects from cross-dream structure. Finally, explicit generative modeling could pit cultural-schema baselines against structured-world hypotheses, using held-out predictive performance as the arbiter.

---

## 5. Conclusion

This study asked whether the spatial–affective regularities in MallWorld dream reports are robust to challenges designed to expose cultural artifacts. The answer is yes. Location type and vertical position both associate meaningfully with atmosphere, and these associations survive time-split, author-holdout, prolific-author sensitivity, and within-author permutation tests. The patterns are not ephemeral, not driven by a small number of influential contributors, and not reducible to author-specific stylistic priors.

What the patterns *are*—whether cultural schemas absorbed from shared media, constraints inherent to dream narration, or reflections of deeper phenomenological or correspondential structure—remains an open question. But it is now a question worth asking, grounded in regularities that have demonstrated their stability under stringent empirical scrutiny.

---

## Appendix A: Statistical Summary

| Variable Pair | n | χ² | df | p-value | Cramér's V |
|---------------|---:|---:|---:|---------|---:|
| Location type × Atmosphere | 4,306 | 1,737.99 | 621 | 2.13 × 10⁻¹⁰⁶ | 0.212 |
| Vertical position × Atmosphere | 1,955 | 203.50 | 45 | 4.97 × 10⁻²² | 0.144 |

## Appendix B: Robustness Summary

| Variable Pair | Test | Key Result |
|---------------|------|------------|
| Location type × Atmosphere | Time split | V = 0.169 vs 0.178; spread p = 0.54 |
| Location type × Atmosphere | Author holdout | Train V = 0.172 ± 0.010; Test V = 0.171 ± 0.009 |
| Location type × Atmosphere | Drop top-k | V declines 0.170 → 0.142 at k = 100 |
| Location type × Atmosphere | Within-author null | Observed V = 0.170; null mean = 0.059; p = 0.001 |
| Vertical position × Atmosphere | Time split | V = 0.130 vs 0.144; spread p = 0.56 |
| Vertical position × Atmosphere | Author holdout | Train V = 0.139 ± 0.014; Test V = 0.136 ± 0.014 |
| Vertical position × Atmosphere | Drop top-k | V declines 0.136 → 0.121 at k = 100 |
| Vertical position × Atmosphere | Within-author null | Observed V = 0.136; null mean = 0.060; p = 0.001 |
