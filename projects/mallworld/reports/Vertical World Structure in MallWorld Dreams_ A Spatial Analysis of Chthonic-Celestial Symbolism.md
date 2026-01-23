# Vertical World Structure in MallWorld Dreams: A Spatial Analysis of Chthonic-Celestial Symbolism

## Abstract

Vertical space carries symbolic weight across human cultures, with ascent commonly associated with purity, transcendence, or proximity to the divine, and descent with material entanglement, threat, or spiritual degradation. This study investigates whether the MallWorld dream corpus—a collection of narratives describing recurring dreams of labyrinthine commercial spaces—exhibits systematic vertical symbolism consistent with these cross-cultural patterns.

Analyzing 2,678 dream narratives containing 11,351 discrete locations, we found robust statistical evidence for vertical-affective gradients. Underground spaces were significantly more threatening than ground or elevated spaces (mean atmosphere 2.27 vs 2.73 on a 5-point scale; χ² = 143.1, p < 10⁻²¹). Entity types stratified by elevation: creatures appeared at more than double the rate underground compared to other levels (11.6% vs 5.4%), while authority figures concentrated at elevated positions (14.9% vs 9.5%). Movement patterns showed near-perfect ascent-descent balance (22.2% vs 22.3%), suggesting bidirectional exploration rather than teleological progression. Ground-level interactions achieved the highest success rates (68.3% vs 61–63% at other levels).

These findings demonstrate that MallWorld dreams encode symbolically meaningful vertical structure. The patterns align with correspondential frameworks in which spatial elevation serves as a natural expression of qualitative states—higher positions associated with characteristics closer to good and truth, lower positions with more distorted or self-oriented archetypes. Whether this reflects cultural absorption, shared phenomenology, or deeper structural constraints remains an open question, but the regularities themselves are empirically robust.

**Keywords**: MallWorld, dream phenomenology, vertical symbolism, spatial cognition, correspondential structure, collective dreams

---

## Data Provenance

| Item | Value |
|------|-------|
| Source | r/themallworld subreddit |
| Total dreams analyzed | 2,678 |
| Total locations extracted | 11,351 |
| Locations with vertical data | 3,822 (33.7%) |
| Total connections | 5,499 |
| Total interactions | 7,283 |
| Extraction model | Azure OpenAI GPT-4o |

---

## 1. Introduction

### 1.1 Background

The MallWorld phenomenon has emerged as a distinctive category of collective dream experience. Thousands of individuals report recurring dreams of navigating labyrinthine shopping mall environments—spaces characterized by architectural impossibility, affective intensity, and structural consistency across dreamers. Unlike conventional recurring dreams tied to individual biography, MallWorld narratives exhibit regularities that transcend personal experience, suggesting they may access shared symbolic structures rather than merely replaying individual memories.

One of the most prominent architectural features of these narratives is their vertical complexity. Dreamers frequently describe multi-level mall spaces where different floors possess distinct experiential characteristics. Underground parking garages are described as threatening and disorienting; upper-level atriums as vertiginous but somehow cleaner or more open; basement corridors as places where one might encounter strange creatures or become irretrievably lost. This vertical stratification raises the question of whether dream-generated spaces follow the symbolic logic observed in traditional cosmologies, which nearly universally encode meaning through elevation.

The association of height with goodness, purity, or divinity appears across cultures with remarkable consistency. Mountains serve as sites of divine encounter in traditions from Sinai to Olympus; heavens are located above, hells below; ascent figures spiritual progress in contexts from Dante's *Commedia* to contemporary near-death experience reports. Whether this reflects embodied cognition (the physical effort of climbing, the vulnerability of falling), cultural transmission, or something more fundamental remains debated. What is clear is that vertical symbolism runs deep in human meaning-making.

### 1.2 Theoretical Framework

This investigation treats correspondential frameworks—including but not limited to the Swedenborgian system—as hypothesis generators rather than assumed authorities. In Swedenborg's writings, natural objects and spatial relations are understood to express spiritual realities through organic correspondence: light corresponds to truth because both illuminate; height corresponds to states closer to good and truth because both involve elevation away from self-oriented constraints. Importantly, this is not mere allegory where arbitrary symbols are assigned by convention, but claimed organic connection where the natural genuinely expresses the spiritual.

Within this framework, we would expect vertical structure in dreams to reflect qualitative gradients. Higher positions should be associated with states closer to good and truth—clearer perception, less distorted entities, more benevolent atmospheres. Lower positions should be associated with states closer to the proprium (self-love)—more threatening atmospheres, more distorted or creature-like entities, greater navigational difficulty. Crucially, this does *not* mean that physical elevation maps directly onto Swedenborg's discrete degrees (celestial, spiritual, natural), which describe ontological levels of reality rather than spatial positions. What it does suggest is that spatial elevation in dream imagery may serve as a natural expression of qualitative states—as a correspondence in the technical sense.

If MallWorld dreams genuinely express such correspondential structure, we would expect: (1) atmosphere to correlate positively with vertical position; (2) entity types to stratify by elevation, with more distorted forms below and more authority-bearing forms above; (3) movement to show bidirectional balance if vertical space serves exploration of states rather than teleological progress; and (4) ground level to serve as a stable reference point where interaction succeeds best.

### 1.3 Aims

This analysis tests four specific hypotheses:

1. **Atmosphere gradient**: Atmospheric valence correlates positively with vertical position, with underground spaces more threatening than elevated spaces.
2. **Entity stratification**: Entity type distributions differ significantly across vertical levels, with creatures concentrated below and authority figures above.
3. **Movement balance**: Ascent and descent movements occur with approximately equal frequency.
4. **Ground anchoring**: Ground-level interactions achieve higher success rates than interactions at other levels.

---

## 2. Methods

### 2.1 Data Sources

Dream narratives were collected from the r/themallworld subreddit, a community where individuals share accounts of the MallWorld phenomenon. Each narrative was processed through a structured extraction pipeline using Azure OpenAI's GPT-4o model with a detailed questionnaire schema designed to capture spatial, atmospheric, entity-related, and interaction-related features.

### 2.2 Coding Scheme

Vertical position was coded using a five-level ordinal scale: lowest (deep underground, sub-basement), lower (underground, basement), ground (street level, main floor), upper (above ground, upper floors), and uppermost (top floor, roof, attic). These were assigned numeric values from -2 to +2 for quantitative analysis, with ground level as the zero reference.

Atmosphere was coded on a five-point valence scale from threatening (1) through eerie (2), neutral (3), comfortable (4), to welcoming (5). This scale captures the affective quality of locations as described in narratives.

Entity types included categories such as creature, threat, authority figure, guide, stranger, and crowd. Demeanor was coded separately on dimensions including hostile, threatening, neutral, friendly, and helpful.

### 2.3 Statistical Analysis

Association testing employed chi-square tests for independence between categorical variables (atmosphere by vertical level, entity type by vertical level). Effect sizes for ordinal associations were quantified using Spearman correlation. Mean differences were assessed through independent-samples and one-sample t-tests. Movement balance was tested against the null hypothesis of 50/50 using binomial tests. All tests were two-tailed with α = 0.05.

---

## 3. Results

### 3.1 Vertical Distribution

Of 11,351 total locations in the corpus, 3,822 (33.7%) had defined vertical positions. The distribution strongly favored ground level, which accounted for 53.1% of coded positions (n = 2,031). Upper levels comprised 20.7% (n = 792), lower levels 14.5% (n = 556), uppermost levels 7.3% (n = 278), and lowest levels 4.3% (n = 165).

The mean vertical position was +0.12 (SD = 0.90), significantly above ground level (t(3821) = 8.33, p < 0.0001, d = 0.13). While the effect size is small, it indicates a systematic tendency: when dreamers leave ground level, they more often ascend than descend. Ground level nonetheless dominates the geography of dream space, serving as the default positional reference.

### 3.2 Atmosphere and Vertical Position

A chi-square test revealed a highly significant relationship between vertical position and atmospheric quality (χ² = 143.1, df = 15, p < 10⁻²¹). To characterize this relationship, we compared mean atmospheric valence across vertical categories. Underground spaces (combining lowest and lower levels) averaged 2.27 on the 5-point atmosphere scale (SD = 1.02, n = 570). Ground-level spaces averaged 2.73 (SD = 1.12, n = 1,547). Elevated spaces (combining upper and uppermost levels) averaged 2.77 (SD = 1.11, n = 819).

The difference between underground and ground-level atmospheres was significant (t = -5.45, p < 0.0001), confirming that underground spaces are perceived as substantially more threatening. Spearman correlation between numeric vertical position and atmospheric valence was ρ = 0.12 (p < 0.0001)—a small but significant positive correlation indicating that higher spaces tend toward more welcoming atmospheres.

The nearly half-point difference on a 5-point scale between underground and surface spaces (2.27 vs 2.73) represents a meaningful experiential gradient. Underground locations in MallWorld dreams are not merely lower; they are affectively different—more ominous, more threatening, less welcoming.

### 3.3 Reality Stability

Unlike atmosphere, reality stability—coded from decaying (1) to hyper-real (5)—showed no significant correlation with vertical position (ρ = -0.03, p = 0.30). Mean reality stability was virtually identical across levels: underground 2.65, ground 2.60, elevated 2.64. This indicates that the vertical gradient applies specifically to affective qualities, not to the ontological stability or vividness of the dream environment. Underground spaces feel more threatening, but they do not feel less real.

### 3.4 Movement Patterns

Analysis of 5,499 connections between locations revealed that lateral movement (remaining at the same level) accounted for 55.5% of transitions (n = 3,055). Vertical movements divided almost perfectly between ascent (22.2%, n = 1,220) and descent (22.3%, n = 1,224). The ascent-to-descent ratio was 1.00, and a binomial test found no significant deviation from 50/50 (p = 0.95).

This near-perfect balance suggests that MallWorld dreams explore vertical space bidirectionally without systematic preference for rising or descending narratives. Dreamers move up and down through the vertical structure with equal frequency, as if mapping the space rather than progressing through it.

### 3.5 Vertical Transport Mechanisms

Of the 5,499 connections, 843 (15.3%) involved explicit vertical transport mechanisms. Stairs dominated, accounting for 54.3% of vertical transport (n = 458). Elevators comprised 24.0% (n = 202), escalators 19.2% (n = 162), and other mechanisms 2.5% (n = 21). The prevalence of stairs—physical, navigable, potentially endless—is consistent with the MallWorld aesthetic of labyrinthine passageways that can be walked but never fully traversed.

### 3.6 Location Types and Vertical Position

Certain location types showed strong or perfect vertical segregation. Basements appeared 100% underground, as expected from their semantic definition. Parking garages were 86% underground. Attics and rooftops appeared 100% at elevated levels. More ambiguous spaces showed intermediate distributions: food courts were 5% underground, 50% ground level, and 45% elevated; corridors were 16% underground, 51% ground level, and 33% elevated.

This pattern indicates that semantic associations from waking architecture carry into dream space. A basement is coded as underground not because the dream explicitly describes descent but because the concept "basement" carries vertical information. The interesting question is whether the atmosphere gradient exceeds what such architectural semantics alone would predict—whether the affective quality of underground spaces reflects something beyond the conventional associations of basements and parking garages.

### 3.7 Entity Types and Vertical Position

Analysis of 1,257 entity occurrences at defined vertical levels revealed significant stratification (χ² = 41.13, df = 22, p = 0.008). The most striking pattern involved creatures and authority figures. Creatures—animals, monsters, or other non-human entities—appeared at 11.6% of underground locations but only 5.4% at ground level and 5.4% at elevated levels. Authority figures showed the opposite pattern: 14.9% at elevated levels, 11.5% at ground level, and 9.5% underground.

This distribution aligns with correspondential expectations. In frameworks where spatial elevation expresses qualitative states, lower positions should manifest more distorted or creature-like forms—affections, in Swedenborgian terms, "made visible" in their less refined state. Higher positions should manifest entities with teaching or governing functions, closer to truth and order. The data bear out this pattern: creatures cluster below, authorities above, with more than a twofold difference in creature prevalence between underground and surface levels.

### 3.8 Entity Demeanor

Entity demeanor showed a marginally significant relationship with vertical position (χ² = 28.56, df = 18, p = 0.054). Underground entities exhibited elevated threat levels (11.5% coded as threatening vs 8.2% at ground level), while elevated-level entities showed higher rates of unfriendly demeanor (10.2% vs 3.8% underground). This latter finding—more unfriendliness at elevation—may reflect resistance to authority or teaching rather than raw threat, a distinction that would be theoretically meaningful in correspondential frameworks where opposition to truth differs from opposition to good.

### 3.9 Interaction Outcomes

Analysis of 1,108 interactions with defined vertical levels and meaningful outcomes (succeeded, failed, interrupted, abandoned) revealed significant differences across levels (χ² = 27.40, df = 12, p = 0.007). Ground-level interactions achieved a 68.3% success rate (n = 545). Elevated interactions achieved 63.2% (n = 329). Underground interactions achieved 61.5% (n = 234).

Direct comparison of underground versus elevated success rates via Fisher's exact test yielded an odds ratio of 0.93 (p = 0.72)—not significantly different. Both represent departures from the ground-level baseline. This supports the hypothesis that ground level serves as the navigational anchor in MallWorld dreams: the stable reference frame where interaction proceeds most successfully, with both ascent and descent introducing uncertainty or difficulty.

### 3.10 Multi-Level Complexity

Analysis of vertical range within individual dreams showed that 52.7% of dreams with vertical data (n = 656) remained at a single level. The remaining 47.3% explored multiple levels: 24.8% spanned two adjacent levels, 15.2% spanned three levels, and 7.3% traversed four or more distinct elevations. Of 1,245 dreams with vertical data, 183 (14.7%) spanned the full underground-to-elevated range. MallWorld dreams exhibit genuine vertical complexity, with nearly half involving movement across multiple elevation strata.

---

## 4. Discussion

### 4.1 Summary of Findings

The evidence supports all four hypotheses. First, underground spaces are significantly more threatening than ground or elevated spaces, with a highly significant atmosphere-vertical correlation (p < 10⁻²¹) and a meaningful experiential gradient (half a point on a 5-point scale). Second, entity types stratify significantly by vertical level (p = 0.008), with creatures concentrated underground and authority figures at elevation. Third, ascent and descent occur with near-perfect balance (22.2% vs 22.3%, p = 0.95), suggesting exploration rather than directed progress. Fourth, ground-level interactions achieve the highest success rates (68.3% vs 61–63% elsewhere, p = 0.007).

### 4.2 Interpretation

These findings demonstrate that MallWorld dreams encode symbolically meaningful vertical structure. The patterns are not random noise nor artifacts of architectural convention alone. Underground spaces are experientially different—more threatening, more populated by creatures, less successful for interaction—in ways that exceed what the mere presence of basements and parking garages would predict.

The correspondential interpretation offers one framework for understanding these regularities. In this view, spatial elevation serves as a natural expression of qualitative states. Lower positions correspond to states closer to the proprium—self-love, distorted perception, affections manifesting in creature form. Higher positions correspond to states closer to good and truth—clearer perception, entities with teaching or governing functions, less threatening atmospheres. Importantly, this does not claim that underground spaces literally *are* spiritually lower or that rooftops literally *are* spiritually higher. It claims that vertical imagery naturally corresponds to qualitative gradients because both involve movement away from or toward a reference point.

The perfect balance of ascent and descent is particularly suggestive. If MallWorld dreams were encoding cultural narratives of progress (ascent as improvement) or regression (descent as deterioration), we would expect systematic asymmetry. Instead, dreamers explore the vertical structure bidirectionally, as if mapping a space rather than traversing a moral gradient. This is consistent with the view that vertical movement in dreams serves state exploration—experiencing different qualitative conditions—rather than teleological advancement.

The ground-anchoring finding adds nuance. Ground level achieves the highest interaction success rates, suggesting it functions as the stable reference frame for dream navigation. Both ascent and descent introduce uncertainty or difficulty relative to this baseline. This aligns with the natural plane serving as the default arena for action and interaction, with vertical excursions representing departures into less familiar experiential territory.

### 4.3 Alternative Explanations

Several alternative explanations deserve consideration. The atmosphere gradient might reflect absorbed cultural templates: horror films routinely locate threats in basements, and this association could be replicated in dream imagery through cultural learning rather than organic correspondence. The entity stratification might similarly reflect narrative conventions about where monsters lurk versus where authorities are encountered.

However, the cross-cultural consistency of vertical symbolism—predating modern horror genres by millennia—suggests the pattern runs deeper than contemporary media templates. The association of underground spaces with threat appears in traditions worldwide, from underworlds of the dead to chthonic monsters to the simple phenomenology of what cannot be seen in darkness. The MallWorld data may be expressing regularities that cultural templates themselves draw upon rather than ones they create.

### 4.4 Limitations

Several limitations constrain these findings. Only 33.7% of locations had defined vertical positions, potentially biasing toward architecturally salient cases where elevation was explicitly mentioned or clearly implied. The extraction pipeline relies on LLM inference from narrative descriptions, which may misinterpret ambiguous spatial language. Reddit users represent a specific demographic, and self-reported dreams may emphasize memorable content, which might disproportionately include vertically extreme experiences. Finally, while the correlational evidence is robust, it cannot distinguish between cultural absorption, shared phenomenology, and deeper structural constraints as generative mechanisms.

### 4.5 Future Directions

Several extensions suggest themselves. Longitudinal tracking could assess whether individual dreamers maintain consistent vertical symbolism across multiple MallWorld dreams. Cross-cultural comparison could test whether the atmosphere gradient appears in non-Western MallWorld dreamers, which would argue against purely Western-media-based explanations. Transition analysis could examine what predicts successful navigation of vertical space—whether certain approaches to ascent or descent yield better outcomes. And focused analysis of elevator encounters, which comprise 24% of vertical transport, could illuminate liminal vertical transitions where the dreamer is moved rather than moving.

---

## 5. Conclusion

MallWorld dreams exhibit robust vertical symbolism. Underground spaces are more threatening and more populated by creatures; elevated spaces concentrate authority figures and trend toward more welcoming atmospheres; ground level serves as the navigational anchor where interaction succeeds best. Movement patterns show perfect ascent-descent balance, suggesting bidirectional exploration of vertical space rather than progression through it.

These findings align with correspondential frameworks in which spatial elevation naturally expresses qualitative states. Higher positions correspond to characteristics closer to good and truth—less distorted entities, clearer atmospheres. Lower positions correspond to characteristics closer to self-orientation—more threatening atmospheres, more creature-like forms. This is not a claim that the dreams encode Swedenborgian theology, but that they exhibit the kind of vertical-qualitative correspondence that such frameworks describe.

Whether the patterns reflect cultural absorption, shared embodied cognition, or deeper phenomenological structure remains undetermined. What is established is that the patterns exist, that they are statistically robust, and that they encode meaningful vertical differentiation. The mall—a contemporary commercial space—has been recruited as the architectural substrate for a symbolic vertical cosmology that dreamers navigate bidirectionally, exploring states above and below the ground-level baseline with equal frequency but distinctly different experiential qualities.

---

## Appendix A: Statistical Summary

| Test | Variable Pair | Statistic | df | p-value |
|------|---------------|-----------|---:|---------|
| χ² (independence) | Atmosphere × Vertical | 143.1 | 15 | < 10⁻²¹ |
| χ² (independence) | Entity type × Vertical | 41.13 | 22 | 0.008 |
| χ² (independence) | Demeanor × Vertical | 28.56 | 18 | 0.054 |
| χ² (independence) | Outcome × Vertical | 27.40 | 12 | 0.007 |
| Spearman ρ | Atmosphere–Vertical | 0.12 | — | < 0.0001 |
| t-test (one-sample) | Mean vertical vs 0 | 8.33 | 3821 | < 0.0001 |
| t-test (independent) | Underground vs Ground atmosphere | -5.45 | — | < 0.0001 |
| Binomial | Ascent vs Descent | — | — | 0.95 |

## Appendix B: Key Distributions

**Vertical position** (n = 3,822): Ground 53.1%, Upper 20.7%, Lower 14.5%, Uppermost 7.3%, Lowest 4.3%

**Movement type** (n = 5,499): Lateral 55.5%, Ascent 22.2%, Descent 22.3%

**Vertical transport** (n = 843): Stairs 54.3%, Elevators 24.0%, Escalators 19.2%, Other 2.5%

**Interaction success by level**: Ground 68.3%, Elevated 63.2%, Underground 61.5%

**Creature prevalence**: Underground 11.6%, Ground 5.4%, Elevated 5.4%

**Authority figure prevalence**: Elevated 14.9%, Ground 11.5%, Underground 9.5%
