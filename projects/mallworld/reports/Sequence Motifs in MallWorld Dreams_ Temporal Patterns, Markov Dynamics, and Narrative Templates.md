# Sequence Motifs in MallWorld Dreams: Temporal Patterns, Markov Dynamics, and Narrative Templates

## Abstract

Dream narratives unfold through spatial transitions that may follow systematic patterns, yet the grammar of dream movement—which transitions occur, how sequences begin and end, and whether dreams trend toward resolution or deterioration—remains underexplored in phenomenological research. This study applies multiple complementary analytical frameworks to 6,781 location transitions extracted from 1,926 MallWorld dream reports, examining the temporal structure of dream sequences through n-gram frequency analysis, Markov chain modeling, loop and trap detection, narrative arc classification, and sequence clustering.

The analysis reveals that MallWorld dreams exhibit significant temporal asymmetry. Mall locations dominate dream entries (+8.4% versus exits) while "other" non-commercial locations dominate exits (+12.7% versus entries), indicating systematic flow from commercial to non-commercial spaces. Markov chain analysis identifies "other" as the dominant stationary state (31.7% of long-run probability mass), with the fastest escape path running from mall to other (3.1 steps mean first passage time). Loop analysis found that 30.2% of dreams contain location revisits, with "other" serving as the primary loop hub (58.7% of all loops). Narrative arc classification revealed that 35.1% of dreams show complex non-standard patterns, with oscillatory structures (rise-fall at 18.8% and descent-recovery at 17.3%) far more common than monotonic trajectories (pure descent 6.7%, pure ascent 5.9%). Atmospheric trajectories show systematic deterioration across sequences (p = 0.0010). Sequence clustering identified five major template families, dominated by mall-centric patterns (24.2%) and pure other exploration (14.9%).

These findings establish that MallWorld dreams follow a characteristic structure: entering through commercial spaces, experiencing atmospheric deterioration through exploration with frequent loops, and flowing toward non-commercial escape destinations that may themselves become traps. The Markov dynamics reveal mall as a gravitational center that dreamers orbit even while attempting escape, while the high loop rate and trap frequency suggest systematic entrapment experiences. Dream sequences are neither random walks nor fully deterministic scripts, but probabilistic narratives following learnable patterns amenable to formal analysis.

**Keywords**: dream sequences, Markov chains, transition grammar, narrative templates, loop detection, atmospheric dynamics, sequence clustering

---

## Data Provenance

| Item | Value |
|------|-------|
| Source | r/TheMallWorld subreddit |
| Total dreams | 1,926 |
| Total locations | 8,707 |
| Total transitions | 6,781 |
| Unique location types | 70 |
| Dreams with 4+ locations | 914 (47.5%) |
| Dreams with valid atmosphere arcs | 405 (21.0%) |
| Extraction model | GPT-5.2 via Azure OpenAI |

---

## 1. Introduction

### 1.1 Background

Most phenomenological research treats dreams as static snapshots—cataloguing content, themes, or emotional valence without attending to how dreams unfold in time. Yet dream experience is fundamentally sequential: the dreamer moves through spaces, encounters entities, and experiences atmospheric shifts in a temporal order that may carry its own significance. Questions of how dreams begin, evolve, and conclude—and whether these temporal patterns are systematic or random—remain largely unanswered.

The MallWorld phenomenon provides an ideal corpus for investigating dream temporality. These dream reports describe navigation through explicitly labeled locations with clear atmospheric ratings, creating natural sequences amenable to formal analysis. The consistency of the setting—liminal commercial spaces with distinctive architectural features—allows isolation of temporal dynamics from the confounding variation that plagues most dream corpora. If MallWorld dreams exhibit systematic sequential structure, this would suggest that dream phenomenology follows temporal grammar rather than unfolding through arbitrary succession.

### 1.2 Theoretical Framework

This investigation approaches dream sequences through five complementary analytical lenses. N-gram analysis treats location-to-location movements as tokens in a sequence language, identifying which two-step, three-step, and four-step patterns recur most frequently—the vocabulary and syntax of dream movement. Markov chain modeling treats dream navigation as a probabilistic state machine, computing transition probabilities between location types, the stationary distribution toward which sequences converge, and the mean number of steps required to reach particular destinations. Loop and trap detection identifies stuck patterns where dreamers revisit locations or cannot escape certain areas, analyzing what enables eventual escape. Narrative arc classification examines atmospheric trajectories across sequences to identify classic dramatic structures—rising action, climax, resolution—or their absence. Sequence clustering uses edit distance to identify recurring narrative templates and group similar dream sequences into families.

Together, these approaches characterize dream sequences at multiple levels of abstraction: local transitions, global convergence properties, stuck patterns, emotional trajectories, and recurring structural templates.

### 1.3 Research Questions

This analysis addresses five primary questions. First, what is the vocabulary and syntax of dream movement between location types—which transitions occur, and which are forbidden or rare? Second, what stationary distribution do dream sequences converge toward in the long run, and how quickly can dreamers reach escape destinations? Third, how common are stuck patterns where dreamers revisit the same locations, and what enables escape from these loops? Fourth, do dreams follow recognizable dramatic structures with climax and resolution, or do they show more irregular emotional trajectories? Fifth, can recurring story types be identified through sequence clustering, revealing narrative templates that organize dream experience?

---

## 2. Methods

### 2.1 N-gram Extraction

Location sequences were extracted from dream narratives using the locations array with visit order fields. N-grams of consecutive locations were computed at multiple scales: bigrams (two consecutive locations), trigrams (three consecutive locations), and quadgrams (four consecutive locations). Quadgram patterns were classified using symbolic notation where ABCD indicates four unique locations, AAAA indicates pure repetition at a single location, ABCA indicates return to the starting point after a journey, and so forth.

### 2.2 Markov Chain Construction

A transition probability matrix was constructed where each cell represents the probability of transitioning from one location type to another, estimated from observed transition frequencies across the corpus. The matrix was row-normalized to ensure valid probability distributions. The stationary distribution—representing where a random walker on the dream graph would spend time in the long run—was computed via eigenvalue decomposition, identifying the left eigenvector corresponding to eigenvalue one. Mean first passage times—the expected number of transitions required to reach a destination from a given source—were estimated via Monte Carlo simulation with 500 trials and a maximum of 100 steps per trial.

### 2.3 Loop and Trap Detection

Three levels of repetition were distinguished. A revisit occurs when any location type is visited more than once in a dream. A loop occurs when the dreamer returns to a previously visited location after intervening transitions (pattern A→...→A). A trap occurs when a location is visited three or more times in a single dream, suggesting systematic stuckness rather than incidental return. Loop escape analysis tracked the destination immediately following loop completion to identify which locations serve as exit points from stuck patterns.

### 2.4 Narrative Arc Classification

Dreams with three or more atmospheric ratings were segmented into thirds representing beginning, middle, and end. Mean atmospheric valence (on a scale from 1 for threatening to 5 for welcoming) was computed for each segment. Arc types were classified as follows: continuous descent when first exceeds middle exceeds last (linear worsening); continuous ascent when the reverse holds (linear improvement); rise-fall when the middle exceeds both first and last (inverted U representing temporary relief); descent-recovery when the middle is lower than both first and last (U-shape representing hitting bottom then recovering); stable when the absolute difference between first and last is less than 0.5; and complex for patterns not fitting these categories.

### 2.5 Sequence Clustering

To enable template analysis, locations were mapped to thirteen categorical symbols: M for mall-related spaces, S for stores and shops, P for parking, H for home and residential, U for university and school, C for city and street, F for food and restaurant, W for water-related, L for lodging and hotel, A for airport, T for theater, E for entertainment and amusement, and O for other. Levenshtein edit distance—the minimum number of insertions, deletions, and substitutions required to transform one sequence into another—was computed between the fifty most common motif strings. Sequences were clustered using a normalized distance threshold of 0.5.

---

## 3. Results

### 3.1 N-gram Analysis: The Vocabulary of Dream Movement

Analysis of 6,781 bigram transitions revealed a constrained transition vocabulary dominated by a small number of high-frequency patterns. The most common transition was other-to-other, accounting for 22.3% of all transitions (n = 1,513)—extensive exploration within non-commercial spaces. Mall self-loops (mall-to-mall) accounted for 8.6% (n = 582), and mall-to-other transitions accounted for 6.3% (n = 430), confirming the central role of mall as both attractor and escape source. The reverse transition, other-to-mall, occurred at only 4.0% (n = 272), indicating net flow away from commercial space.

Trigram analysis classified patterns as either linear (A→B→C, three distinct locations) or cyclic (A→B→A, return to origin). Linear progression dominated, accounting for 65.1% of trigrams (n = 3,133), while cyclic return accounted for 34.9% (n = 1,679). This strong preference for forward movement over immediate return suggests goal-directed navigation rather than repetitive wandering at the local scale.

Quadgram analysis of 3,955 four-location sequences across 914 dreams with sufficient length revealed that nearly half (49.6%, n = 1,960) showed pure progression through four unique locations (ABCD pattern). Mixed patterns accounted for 28.3% (n = 1,118). Return patterns—where the dreamer circles back to an earlier location—accounted for smaller proportions: ABCA (return after journey) at 4.3%, ABCB (return to middle) at 4.6%, ABAA (entry to repetition) at 4.4%. Pure repetition at a single location (AAAA) was rare, accounting for only 3.5% (n = 140). Oscillation patterns (ABAB) and palindromes (ABBA) were rarer still, at 0.8% and 0.6% respectively.

These n-gram distributions establish that MallWorld dreams show predominantly linear local structure—dreamers move forward through sequences of distinct locations rather than immediately returning or remaining stuck. The cyclic and repetitive patterns that do occur represent a meaningful minority (approximately one-third) but not the dominant mode of navigation.

### 3.2 Markov Chain Analysis: Probabilistic Dynamics

The transition probability matrix revealed that all location types have high probability of transitioning to "other"—ranging from 35% to 52% depending on the source location. This confirms "other" as a universal attractor state toward which dream sequences flow regardless of starting point. Among commercial spaces, mall showed the highest self-transition rate at 23.9%, indicating that dreamers who find themselves in mall tend to remain in mall for multiple consecutive locations.

The stationary distribution—representing the long-run equilibrium toward which dream sequences converge—showed "other" as the dominant state at 31.7% probability, substantially exceeding mall at 12.0%, mall stores at 8.0%, city streets at 5.6%, houses at 4.8%, and hotels at 3.4%. This represents where a random walker on the dream transition graph would spend most time: in the long run, dreams converge toward non-specific escape spaces rather than remaining in commercial environments.

Mean first passage time analysis revealed the expected number of transitions required to reach various destinations. The fastest escape path runs from mall to other, requiring only 3.1 steps on average. From city street the path to other requires 2.9 steps, and from house only 2.4 steps. These rapid escape times indicate that non-commercial space is highly accessible from anywhere in the dream geography. By contrast, parking lots proved difficult to reach from any source, requiring 29 to 35 steps—suggesting parking as an isolated state rarely visited deliberately.

The most striking finding concerns mall's reachability. From any location in the dream geography, mall can be reached in 10 to 14 steps. This moderate but consistent accessibility, combined with mall's self-transition persistence, establishes mall as a gravitational center: dreamers may escape relatively quickly (3.1 steps to other) but can also be pulled back toward commercial space from anywhere in the dream.

### 3.3 Loop and Trap Analysis: Stuck Patterns

Analysis of revisitation patterns revealed that 43.6% of dreams (n = 839) contained at least one location visited more than once. More specifically, 30.2% of dreams (n = 581) contained explicit loop patterns where the dreamer returned to a previously visited location after intervening transitions. Nearly one-fifth of dreams (19.5%, n = 375) qualified as traps with three or more visits to the same location—substantially higher than expected from random walks.

The locations serving as loop hubs showed strong concentration. "Other" dominated, serving as the hub for 58.7% of all loops (n = 341). Mall and mall stores together accounted for 17.2% of loop hubs. City streets (5.0%), houses (3.1%), hotels (3.1%), and schools (2.4%) served as hubs for smaller proportions of loops.

Trap analysis—locations visited three or more times—showed even stronger concentration. The vast majority of trap experiences (76.5%, n = 287) occurred in "other" locations, with mall stores a distant second at 14.1% (n = 53), mall proper at 5.9% (n = 22), and houses at 3.5% (n = 13). This reveals a paradox: while mall is experientially threatening, it is "other" spaces where dreamers become most stuck. Escape from mall may lead to a different form of entrapment in non-specific spaces.

Loop escape patterns showed characteristic destinations. From other-location loops, escape led primarily to city streets (n = 39), restaurants (n = 38), houses (n = 37), and pools (n = 36)—specific, identifiable spaces that may function as resolution points. From mall loops, escape led primarily to mall stores (n = 21) or other (n = 13), indicating difficulty escaping the commercial gravity well even when loops complete.

Loop length statistics showed a mean of 5.54 steps (median = 4.0 steps), with the most common length being 2 steps (n = 322 loops) and the maximum observed length being 29 steps. Dreams can spend substantial portions of their sequences cycling through repeated locations before achieving escape or resolution.

### 3.4 Narrative Arc Analysis: Emotional Trajectories

Analysis of 405 dreams with three or more valid atmospheric ratings revealed that the majority (35.1%, n = 142) showed complex patterns not fitting standard dramatic structures. Among recognizable arcs, rise-fall (temporary relief followed by return to difficulty) was most common at 18.8% (n = 76), followed by descent-recovery (hitting bottom then improving) at 17.3% (n = 70), stable trajectories at 16.3% (n = 66), continuous descent at 6.7% (n = 27), and continuous ascent at 5.9% (n = 24).

The rarity of monotonic trajectories is notable. Pure descent—the classic nightmare structure of progressive worsening—accounts for less than 7% of dreams. Pure ascent—progressive improvement—is even rarer at under 6%. The dominant patterns are oscillatory: temporary relief that doesn't last (rise-fall), or hitting bottom before partial recovery (descent-recovery). Dreams fluctuate rather than following linear emotional trajectories.

Mean atmospheric valence by arc segment illuminated these patterns. Continuous descent dreams began near neutral-comfortable (mean 3.85), deteriorated through the middle (2.63), and ended threatening (1.74)—a total drop of 2.10 points on the 5-point scale. Continuous ascent showed the mirror pattern: starting threatening (1.56), improving through the middle (2.45), and ending comfortable (3.62)—a gain of 2.06 points. Rise-fall dreams showed minimal net change (beginning 2.12, middle peak 3.49, ending 2.03), as did descent-recovery (beginning 3.22, middle trough 1.78, ending 3.05). The oscillatory patterns dominate precisely because they return to starting valence rather than progressing toward resolution.

Overall atmospheric trajectory analysis using binomial tests revealed systematic deterioration across sequences. Worsening transitions (529) significantly exceeded improving transitions (456), with p = 0.0010. Dreams trend toward negative atmospheres, even when the trajectory is not monotonically downward.

Climax location analysis—identifying where peak threatening moments occur—showed non-uniform distribution (χ² = 21.16, p < 0.05). Climaxes clustered in "other" (27.7%, n = 112) and mall (9.9%, n = 40) locations, with city streets (6.7%), houses (4.0%), mall stores (3.2%), hotels (3.2%), and schools (3.2%) contributing smaller proportions. Certain locations systematically serve as dramatic turning points in dream narratives.

### 3.5 Sequence Clustering: Narrative Templates

Motif analysis using the thirteen-symbol categorical mapping identified recurring narrative template families. Mall-centric dreams—those with 40% or more mall-related locations—accounted for 24.2% of the corpus (n = 466). Pure other dreams—sequences containing only non-specific locations—accounted for 14.9% (n = 287). Escape pattern dreams—beginning in mall and ending in other—accounted for 12.5% (n = 241). Loop pattern dreams—containing explicit A→...→A returns—accounted for 7.7% (n = 149). City wandering dreams with multiple city street locations accounted for 6.3% (n = 121). Smaller template families included water park dreams (2.6%), food journey dreams (1.7%), home-to-mall dreams (1.7%), airport dreams (1.6%), mall-to-home dreams (1.4%), and parking entry dreams (1.2%).

Subsequence frequency analysis revealed the most common two- to four-character patterns. The subsequence "OO" (extended other exploration) dominated at 1,513 occurrences—three times more common than "MM" (extended mall exploration) at 582. The escape pattern "MO" (mall to other) occurred 430 times, substantially exceeding the re-entry pattern "OM" (other to mall) at 272, confirming net flow away from commercial space. Longer subsequences showed the same asymmetry: "OOO" (659 occurrences) and "OOOO" (297 occurrences) far exceeded "MMM" (235 occurrences), indicating dreamers spend substantially more time in non-specific spaces.

Edit distance clustering of the fifty most common motifs identified five major clusters. The largest cluster centered on "OO" (other exploration) with 153 dreams. The second cluster centered on "MO" (mall escape) with 70 dreams. The third cluster centered on "MM" (mall entrapment) with 64 dreams. The fourth cluster centered on "OOOO" (extended wandering) with 59 dreams. The fifth cluster centered on "LL" (hotel/lodging sequences) with 13 dreams. The three dominant clusters represent other exploration, mall escape, and mall entrapment—the core narrative modes of MallWorld phenomenology.

---

## 4. Discussion

### 4.1 Summary of Findings

This comprehensive analysis of 6,781 transitions across 1,926 dreams establishes that MallWorld sequences follow systematic patterns at multiple levels of description. The transition grammar is constrained: only 43.3% of possible bigrams actually occur, with the vocabulary dominated by other-to-other (22.3%) and mall self-loops (8.6%). Markov dynamics show convergence toward "other" as the dominant stationary state (31.7%), with mall serving as a gravitational center reachable from anywhere in 10-14 steps. Loop prevalence is high: 30.2% of dreams contain explicit return patterns, with "other" serving as the primary hub (58.7%) and trap location (76.5%). Narrative arcs are predominantly oscillatory, with rise-fall (18.8%) and descent-recovery (17.3%) far exceeding pure descent (6.7%) or ascent (5.9%). Sequence templates cluster into recognizable families dominated by mall-centric (24.2%), pure other (14.9%), and escape pattern (12.5%) structures.

### 4.2 The Descent Narrative Structure

The combined evidence supports a characteristic dream structure that might be called the descent narrative. Dreams typically enter through commercial spaces—mall serving as the dominant entry point with +8.4% excess entry versus exit probability. Exploration proceeds through mall loops and self-transitions, with atmospheric deterioration accumulating across the sequence (worsening significantly exceeds improving, p = 0.0010). Escape attempts manifest as mall-to-other transitions, which occur frequently (430 instances) and quickly (3.1 steps mean passage time). Resolution—or further entrapment—occurs in "other" spaces, which serve as both escape destinations and the primary trap locations.

This is not random wandering but structured entrapment-escape simulation. The Markov dynamics reveal that escape is relatively easy (3.1 steps from mall to other) but return is common (30.2% loop rate), creating a recurring cycle of escape and re-entrapment that may never fully resolve.

### 4.3 Mall as Gravitational Center

Despite being associated with threatening atmospheres, mall exhibits paradoxical gravitational properties. It is reachable from any location in 10-14 steps, accessible from anywhere in the dream geography. It shows high self-transition persistence (23.9% probability of remaining in mall given current mall location). It serves as a hub for 17.2% of all loops. And re-entry transitions from other to mall occur 272 times despite escape pressure.

This paradox—threatening yet gravitationally central—suggests mall functions as a cognitive attractor that dreamers orbit even while experiencing distress. The commercial space is not merely a setting but a force that organizes dream trajectory.

### 4.4 The "Other" Absorber

The "other" location category emerges as the dominant structural feature of MallWorld sequences. It accounts for 31.7% of stationary probability (highest of all locations), 58.7% of all loop hubs, 76.5% of all trap experiences, and serves as the target of the fastest escape paths from all sources. Dreams flow toward non-specific spaces and tend to remain there.

The high trap rate in "other" locations (76.5% of all traps) reveals that escape from mall may lead to a different form of stuckness. The dreamer escapes the threatening commercial environment only to become trapped in non-specific space—perhaps a spatial correlate of the phenomenological experience of having escaped immediate threat without achieving genuine resolution.

### 4.5 Oscillatory Rather Than Linear Trajectories

The narrative arc analysis undermines any assumption that dreams follow simple dramatic structures. Pure descent (progressive worsening) accounts for less than 7% of dreams; pure ascent (progressive improvement) for less than 6%. The dominant patterns are oscillatory: rise-fall (temporary relief that doesn't last) and descent-recovery (hitting bottom before partial recovery). Combined with the "complex" category (35.1%), this means that nearly three-quarters of dreams show non-monotonic emotional trajectories.

This finding has implications for how we understand dream phenomenology. Dreams do not build toward climax and resolution in the manner of conventional narrative. They fluctuate, oscillate, improve and worsen without clear progression. The dreamer experiences relief that proves temporary, deterioration that partially reverses, complexity that resists narrative closure.

### 4.6 Limitations

Several limitations constrain interpretation. The "other" category may obscure meaningful distinctions that finer-grained coding would reveal. Short dreams with only two or three locations limit n-gram analysis and cannot support narrative arc classification. Retrospective reconstruction may introduce post-hoc rationalization that distorts actual dream sequences. Only 21% of dreams have sufficient atmospheric data for arc classification. The clustering threshold of 0.5 normalized distance is somewhat arbitrary.

### 4.7 Future Directions

Several extensions suggest themselves. Higher-order Markov models could test whether two-step or three-step history improves transition prediction beyond first-order chains. Hidden Markov models could infer latent narrative states not directly observable in location sequences. Joint modeling of location and atmosphere transitions could capture their covariation more precisely. Individual difference analysis could assess whether particular dreamers show consistent sequential patterns across multiple dreams. Predictive modeling could test whether dream endings can be predicted from openings, establishing how deterministic versus stochastic dream sequences actually are.

---

## 5. Conclusion

MallWorld dreams exhibit systematic temporal structure that can be characterized through multiple complementary analyses. The Markov chain perspective reveals "other" as the dominant stationary state with mall serving as a gravitational center. Loop analysis shows that nearly one-third of dreams contain revisit patterns, with escape primarily flowing from mall toward non-commercial spaces. Narrative arc classification finds oscillatory patterns more common than monotonic deterioration or improvement, suggesting dreams fluctuate rather than building toward resolution.

The characteristic pattern—commercial entry, progressive exploration with loops, atmospheric deterioration, escape toward non-specific space that may itself become a trap—represents a coherent narrative template instantiated across thousands of dream reports. The 24.2% mall-centric and 12.5% escape pattern families confirm this as a dominant structure, while the 30.2% loop rate and 19.5% trap rate establish entrapment as a pervasive feature of the phenomenology.

These findings establish that dream sequences are neither random walks nor fully deterministic scripts, but probabilistic narratives following learnable patterns. The Markov framework provides a principled approach to dream sequence modeling, while loop detection and narrative arc classification capture higher-level structure invisible to transition-level analysis alone. The gravitational pull of mall spaces—threatening yet repeatedly visited—and the absorbing nature of "other" spaces—escape destinations that become traps—reveal the paradoxical dynamics of MallWorld phenomenology: dreams that seek escape but remain bound to the geography of commercial space.

---

## Appendix A: Statistical Summary

| Test | Comparison | Statistic | p-value |
|------|------------|-----------|---------|
| Binomial | Improving vs worsening atmospheres | 456 vs 529 | 0.0010 |
| χ² | Climax location distribution | 21.16 | < 0.05 |
| Binomial | Mall entry vs exit | 329 vs 199 | < 0.001 |
| Binomial | Other entry vs exit | 284 vs 479 | < 0.001 |

## Appendix B: Key Distributions

**Top bigram transitions** (n = 6,781): other→other 22.3%, mall→mall 8.6%, mall→other 6.3%, other→mall 4.0%, mall→mall_store 3.5%

**Trigram structure**: Linear (A→B→C) 65.1%, Cyclic (A→B→A) 34.9%

**Quadgram patterns** (n = 3,955): Pure progression (ABCD) 49.6%, Mixed 28.3%, Return patterns 8.9%, Pure repetition (AAAA) 3.5%

**Stationary distribution**: other 31.7%, mall 12.0%, mall_store 8.0%, city_street 5.6%, house 4.8%

**Mean first passage times**: mall→other 3.1 steps, house→other 2.4 steps, city_street→other 2.9 steps

**Loop prevalence**: Dreams with loops 30.2%, Dreams with traps 19.5%, Mean loop length 5.54 steps

**Narrative arcs** (n = 405): Complex 35.1%, Rise-fall 18.8%, Descent-recovery 17.3%, Stable 16.3%, Continuous descent 6.7%, Continuous ascent 5.9%

**Template families**: Mall-centric 24.2%, Pure other 14.9%, Escape pattern 12.5%, Loop pattern 7.7%, City wandering 6.3%
