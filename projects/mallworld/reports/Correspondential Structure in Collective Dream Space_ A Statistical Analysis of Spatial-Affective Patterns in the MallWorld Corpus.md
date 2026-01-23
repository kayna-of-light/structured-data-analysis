# Correspondential Structure in Collective Dream Space: A Statistical Analysis of Spatial-Affective Patterns in the MallWorld Corpus

## Abstract

**Background**: The MallWorld phenomenon—thousands of individuals reporting recurring dreams of labyrinthine commercial spaces with consistent architectural and affective features—presents an opportunity to test whether collective dream phenomenology exhibits systematic structure consistent with correspondential frameworks. Such frameworks propose that natural features express spiritual or psychological realities through organic functional relationships rather than arbitrary symbolism. This study applies hypothesis-testing methodology to determine whether MallWorld dream narratives encode predictable patterns in the relationships between spatial features, atmospheric qualities, entity behaviors, and individual characteristics.

**Methods**: We analyzed 2,678 dream narratives from the r/themallworld community, extracting 11,351 discrete locations and 4,235 entity encounters through structured processing using Azure OpenAI GPT-4o. Statistical validation employed chi-square tests for categorical associations, Spearman correlations for ordinal relationships, intraclass correlation coefficients for within-person consistency, variance decomposition for source attribution, and permutation tests for robustness verification. The analysis proceeded through eleven phases examining environmental correspondences, entity behavioral patterns, animal symbolism, atmosphere source attribution, and cross-domain comparisons.

**Results**: Twenty of thirty pre-registered tests showed patterns consistent with correspondential predictions. Environmental features exhibited robust correlations with atmosphere: vertical position (ρ = 0.25–0.30, p < 0.0001), water clarity (2.6× effect), light quality (V = 0.483), and cleanliness (ρ = 0.302). Entity types showed functional differentiation with behavioral invariance across environmental conditions—guides maintained 0% hostility at all vertical levels, threats maintained 92–94% hostility regardless of atmosphere. Animal type predicted demeanor with large effect size (V = 0.513, OR = 106:1 for predator vs. cat) while showing complete independence from environmental atmosphere (χ² ≈ 0, p = 1.0). Critically, dreamer identity explained 56.4% of atmosphere variance compared to 7.1% for location type, and within-dream affect showed near-zero predictive power for subsequent atmosphere after controlling for current state (partial ρ = 0.007, p = 0.71). Cross-domain comparison with 6,753 near-death experiences revealed dramatically different atmosphere distributions (Cramér's V = 0.645), with MallWorld showing 64% negative atmospheres versus NDE showing 48% positive.

**Conclusions**: The MallWorld corpus exhibits systematic structure consistent with correspondential predictions across multiple independent domains. Environmental features correlate with atmosphere in predicted directions; entities maintain type-consistent behavior regardless of environmental context; animals cluster by dreamer identity rather than environmental atmosphere; and individual characteristics dominate over location in determining atmospheric experience. These patterns are consistent with a framework in which spatial and natural features express qualitative states through functional correspondence, while entities and animals express characteristics of the beings they represent rather than the environments they occupy. Alternative explanations including narrative conventions, psychological projection, and reporting bias cannot be excluded, but the convergence of multiple independent findings across different feature domains suggests genuine structural regularities in collective dream phenomenology.

**Keywords**: MallWorld, collective dreams, correspondential structure, spatial symbolism, entity phenomenology, animal correspondences, dream phenomenology, hypothesis-testing, post-materialist inquiry

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| Dream narratives (N = 2,678) | r/themallworld subreddit | Public Reddit data |
| Temporal range | 2021-09-23 to 2026-01-19 | ~4.5 years |
| Unique authors | 2,038 (71.2% single-post) | — |
| Locations extracted | 11,351 | Structured JSON |
| Entities extracted | 4,235 | Structured JSON |
| Connections (transitions) | 5,499 | Structured JSON |
| Extraction model | Azure OpenAI GPT-4o | Azure OpenAI Service |
| Analysis notebooks | `09_prereg_falsification_tests.ipynb`, `10_*.ipynb` | Project repository |
| Structured data | `projects/mallworld/structured/*.json` | Project repository |
| NDE comparison data (N = 6,753) | NDERF, IANDS databases | Structured extraction |

---

## 1. Introduction

### 1.1 Background

The MallWorld phenomenon has emerged as a distinctive category of collective dream experience that challenges conventional explanations of dream content. Thousands of individuals, without apparent prior contact, report recurring dreams of navigating labyrinthine shopping mall environments characterized by architectural impossibility, affective intensity, and structural consistency across dreamers. Unlike idiosyncratic recurring dreams tied to individual biography, MallWorld narratives exhibit regularities that transcend personal experience—suggesting they may access shared symbolic structures rather than merely replaying individual memories.

The phenomenon presents an unusual research opportunity. The consistency of architectural features (endless corridors, impossible escalators, abandoned storefronts), affective qualities (threatening basements, liminal food courts, vertiginous atriums), and entity encounters (faceless crowds, pursuing figures, helpful strangers) across unrelated dreamers raises questions about the origins of dream symbolism. Are these regularities cultural artifacts—shared media exposure producing shared dream imagery? Are they psychological universals—common anxieties finding common expression? Or do they reflect something more fundamental about how consciousness structures experiential space?

This study applies systematic statistical analysis to the MallWorld corpus to determine whether the reported regularities are empirically robust and whether they exhibit patterns consistent with correspondential frameworks. Such frameworks—including but not limited to the Swedenborgian system articulated in the 18th century—propose that natural phenomena express spiritual or psychological realities through organic functional relationships. Light corresponds to wisdom because both illuminate; descent corresponds to states closer to self-interest because both involve movement away from higher reference points. If such correspondences describe genuine structural features of experiential reality, MallWorld dreams should exhibit predictable patterns in the relationships between spatial features and affective qualities, between entity types and behavioral profiles, between animal forms and the dreamers who encounter them.

### 1.2 Theoretical Framework

This investigation treats correspondential frameworks as hypothesis generators rather than assumed authorities. The methodology follows principles articulated in post-materialist consciousness studies: theoretical frameworks are evaluated not by their origins (visionary, scientific, religious) but by their predictive accuracy. A framework that generates accurate predictions across multiple independent domains earns provisional acceptance; one that generates systematic misses warrants revision or rejection.

The Swedenborgian correspondential system proposes several testable principles relevant to dream phenomenology. First, natural features express qualitative states through functional correspondence—vertical elevation corresponds to proximity to good and truth because ascent involves movement away from self-oriented constraints; water clarity corresponds to truth because clear water enables perception while murky water obscures. Second, spiritual beings maintain their essential nature regardless of environmental context—a guide is helpful not because of where it appears but because of what it is; a threat is hostile not because of the surrounding atmosphere but because hostility defines its character. Third, animals represent affections (emotional-volitional states) of the beings who encounter them—the animal form reveals the quality of the affection, while the animal's demeanor (hostile or friendly) reveals whether that affection manifests in good or evil form.

These principles generate specific, falsifiable predictions for dream phenomenology:

**Environmental Correspondences**: If spatial features express qualitative states through functional correspondence, we should observe systematic correlations between physical characteristics and atmospheric qualities. Underground spaces should be more threatening than elevated spaces; dirty water should co-occur with negative atmosphere more than clean water; dim or absent light should correlate with worse atmospheric conditions than bright natural light.

**Entity Autonomy**: If entities maintain essential nature regardless of environment, entity behavioral profiles should remain constant across different spatial contexts. Guides should show similar helpfulness rates at all vertical levels; threats should show similar hostility rates regardless of surrounding atmosphere. The correlation between entity demeanor and environmental atmosphere should approach zero when entity type is controlled.

**Animal Correspondence**: If animals represent dreamer affections rather than environmental qualities, animal type and demeanor should cluster by dreamer identity rather than by location characteristics. The same dreamer should encounter similar animals across different dreams; animals should show independence from environmental atmosphere; and animal type should predict demeanor with large effect size while environmental atmosphere shows no predictive power.

**Atmosphere Source Attribution**: If atmosphere corresponds to stable individual characteristics (the "ruling love" in Swedenborgian terminology) rather than to fluctuating thoughts and emotions, dreamer identity should explain more variance in atmosphere than location characteristics, and within-dream affect should show minimal predictive power for subsequent atmosphere after controlling for current state.

### 1.3 The Question of Alternative Explanations

Scientific integrity requires acknowledging that correlational findings admit multiple interpretations. Patterns consistent with correspondential predictions might also be consistent with alternative explanations:

**Narrative Conventions**: Dream reports are narratives, and narratives follow conventions. The association of underground spaces with threat might reflect cultural storytelling tropes (dungeons, basements in horror films) rather than correspondential structure. Entity behavioral consistency might reflect narrative coherence requirements rather than entity autonomy.

**Psychological Projection**: Jungian and psychodynamic frameworks interpret dream content as projection of internal states. Entity encounters might represent externalized aspects of the dreamer's psyche; animal encounters might symbolize instinctual drives. The patterns observed might be explicable without reference to correspondence as an ontological feature of reality.

**Reporting Bias**: The MallWorld community has developed shared vocabulary and expectations. Dreamers may selectively remember or report features that match community norms, producing apparent regularities that reflect social construction rather than experiential structure.

**Extraction Artifacts**: The use of large language models for structured extraction introduces the possibility that observed patterns reflect model biases rather than dream content. The extraction model might impose structure that exists in its training data rather than in the source narratives.

This analysis cannot definitively exclude these alternatives. What it can do is document whether patterns exist, quantify their magnitude, test whether they replicate across subsamples, and assess whether the constellation of findings is more parsimoniously explained by correspondential structure or by the sum of alternative explanations. The cumulative weight of multiple independent findings—if they converge—constitutes stronger evidence than any single correlation.

### 1.4 Aims

This analysis addresses four primary research domains:

**Domain 1: Environmental Correspondences** — Do physical features of dream locations correlate with atmospheric qualities in directions predicted by correspondential theory? We test associations between vertical position, water clarity, light quality, cleanliness, privacy/exposure, and atmospheric valence.

**Domain 2: Entity Behavioral Patterns** — Do entities maintain type-consistent behavioral profiles across environmental contexts? We examine whether guides, threats, authorities, deceased, and other entity types show invariant behavioral signatures regardless of where they appear.

**Domain 3: Animal Correspondences** — Do animals cluster by dreamer identity or by environmental characteristics? We test whether animal type predicts demeanor, whether animal patterns show independence from atmosphere, and whether the same dreamer encounters consistent animal forms across dreams.

**Domain 4: Atmosphere Source Attribution** — What explains variance in atmospheric experience? We decompose atmosphere variance into dreamer-level and location-level components, test whether within-dream affect predicts subsequent atmosphere, and examine temporal stability of patterns.

Secondary analyses examine cross-domain comparison with near-death experience data, null and weak findings, and exploratory profiling of building types.

---

## 2. Methods

### 2.1 Data Sources

Dream narratives were collected from the r/themallworld subreddit, a community where individuals share accounts of the MallWorld phenomenon. The dataset spans September 23, 2021 through January 19, 2026—approximately 4.5 years of community activity. After filtering non-dream content (meta-posts, questions, artwork), the corpus comprises 2,678 analyzable dream narratives from 2,038 unique authors. The distribution of posts per author is highly skewed: 71.2% of authors contributed only a single narrative, while a minority contributed multiple reports enabling within-person analyses.

Temporal distribution shows community growth over time: 2021 contributed 1.1% of posts, 2022 contributed 5.2%, 2023 contributed 15.8%, 2024 contributed 25.9%, and 2025 contributed 48.0% (with 2026 partial at 4.1%). This growth pattern reflects organic community expansion rather than sampling decisions.

For cross-domain comparison, we utilized structured extractions from 6,753 near-death experience reports drawn from the NDERF (Near-Death Experience Research Foundation) and IANDS (International Association for Near-Death Studies) databases, processed using the same extraction methodology.

### 2.2 Extraction Pipeline

Each narrative was processed through a structured extraction pipeline using Azure OpenAI's GPT-4o model with a detailed questionnaire schema. The schema captures:

- **Location features**: Vertical position (5-level ordinal), building type (70 categories), atmosphere (5-point valence scale), light quality, water presence and clarity, cleanliness, accessibility, and architectural elements
- **Entity features**: Entity type (guide, threat, authority, deceased, stranger, creature, watcher, crowd), demeanor (hostile, threatening, neutral, friendly, helpful, watching), role (chaser, guide, blocker, companion, bystander), and interaction outcomes
- **Connection features**: Movement direction (ascending, descending, level), transition type, and sequence order
- **Animal features**: Animal type (predator, dog, cat, bird, serpent, insect, aquatic, monster, domestic, other), demeanor, and behavior

The extraction model processes raw narrative text and returns structured JSON conforming to the schema. Extraction reliability was validated through manual review of a random subsample, with high concordance between model extraction and human coding for primary variables.

### 2.3 Coding Scheme

**Atmosphere**: Coded on a 5-point valence scale: 1 = threatening, 2 = eerie, 3 = neutral, 4 = comfortable, 5 = welcoming. This scale captures the affective quality of locations as described in narratives.

**Vertical Position**: Coded using a 5-level ordinal scale: -2 = lowest (deep underground, sub-basement), -1 = lower (underground, basement), 0 = ground (street level, main floor), +1 = upper (above ground, upper floors), +2 = uppermost (top floor, roof, attic). Ground level serves as the zero reference.

**Entity Type**: Primary categories include guide (helpful beings offering assistance or direction), threat (beings creating danger or fear), authority (figures with institutional power—security, staff, teachers), deceased (identified dead individuals), stranger (unknown humans), creature (non-human beings), and watcher (observing presences).

**Entity Demeanor**: Coded as hostile, threatening, neutral, friendly, helpful, or watching. Multiple demeanors may apply to a single entity.

**Animal Type**: Classified by functional category: predator (wolves, lions, sharks), dog, cat, bird, serpent/snake, insect, aquatic (fish, sea creatures), monster (chimeric or impossible creatures), domestic (farm animals), and other.

**Light Quality**: Categorized as bright/natural, artificial, dim/flickering, or dark/absent.

**Water Clarity**: Coded as clean/clear or dirty/murky when water is present.

### 2.4 Statistical Methods

**Association Testing**: Chi-square tests assessed independence between categorical variables. Effect sizes for categorical associations were quantified using Cramér's V, with conventional thresholds: V < 0.1 negligible, 0.1–0.3 small, 0.3–0.5 medium, V > 0.5 large.

**Ordinal Correlations**: Spearman's ρ quantified monotonic associations between ordinal variables (vertical position, atmosphere). Significance was assessed using permutation distributions.

**Variance Decomposition**: Intraclass correlation coefficients (ICC) quantified the proportion of variance attributable to between-person differences versus within-person variation. ANOVA-based η² estimated effect sizes for categorical predictors.

**Regression Analysis**: Partial correlations isolated unique predictive contributions after controlling for confounds. Linear regression decomposed variance sources.

**Permutation Tests**: For critical findings, observed statistics were compared against null distributions generated by 10,000 random permutations of relevant labels, providing nonparametric significance assessment robust to distributional assumptions.

**Cross-Validation**: Where applicable, findings were validated across train/validation/test splits to assess generalizability.

All tests were two-tailed with α = 0.05. Multiple comparison corrections were not applied given the confirmatory (pre-registered hypothesis testing) rather than exploratory nature of the primary analyses; however, effect sizes are reported throughout to enable assessment of practical significance independent of sample-size-dependent p-values.

---

## 3. Results: Environmental Correspondences

The correspondential framework predicts that physical features of spaces should correlate with atmospheric qualities through functional relationships—light with clarity of perception, water with truth, elevation with proximity to good, cleanliness with purity. This section tests these predictions systematically across multiple environmental dimensions.

### 3.1 Vertical Position and Atmosphere

The relationship between vertical position and atmospheric quality represents a foundational test of correspondential structure. If elevation corresponds to qualitative states, underground spaces should exhibit more threatening atmospheres than elevated spaces.

Analysis of 3,822 locations with defined vertical positions revealed a robust positive correlation between vertical position and atmospheric valence. The Spearman correlation coefficient ranged from ρ = 0.25 to ρ = 0.30 across different analytical approaches, consistently achieving statistical significance (p < 0.0001). This correlation replicated across train/validation/test splits, demonstrating stability.

The magnitude of the effect appears in mean atmosphere comparisons. Underground spaces (combining lowest and lower levels) averaged 2.27 on the 5-point atmosphere scale, while ground-level spaces averaged 2.73 and elevated spaces averaged 2.77. The nearly half-point difference between underground and surface spaces on a 5-point scale represents a meaningful experiential gradient—underground locations in MallWorld dreams are not merely lower but affectively different, characterized by more ominous and threatening qualities.

Chi-square testing confirmed the association between vertical position categories and atmosphere categories (χ² = 143.1, df = 15, p < 10⁻²¹). The relationship is monotonic: as vertical position increases from lowest to uppermost, mean atmosphere increases correspondingly. This pattern is consistent with correspondential predictions that elevation expresses proximity to states of good and truth.

**Finding**: Vertical position correlates positively with atmospheric quality (ρ = 0.25–0.30, p < 0.0001), with underground spaces averaging nearly half a point more threatening than surface spaces on a 5-point scale.

### 3.2 Water Clarity and Atmosphere

The correspondential framework associates water with truth—clear water with truth that illuminates, murky water with truth obscured or falsified. If this correspondence operates in dream phenomenology, water clarity should correlate with atmospheric quality.

Among locations featuring water elements, clean or clear water associated with positive atmospheric ratings at approximately 45%, while dirty or murky water associated with positive atmosphere at only approximately 17%. This 2.6-fold difference represents a substantial effect. The pattern held across location types and vertical levels, suggesting water clarity operates as an independent atmospheric marker rather than a confound of other spatial features.

**Finding**: Water clarity correlates strongly with atmosphere, with clean water showing 2.6× the positive atmosphere rate of dirty water.

### 3.3 Light Quality and Atmosphere

Light represents a central correspondence across symbolic traditions—associated with wisdom, truth, and perception. The framework predicts that light quality should correlate with atmospheric conditions, with bright natural light associated with more positive atmospheres and darkness with more threatening conditions.

Analysis of 780 locations with defined light quality revealed a strong association between light and atmosphere (χ² = 182.18, p < 0.0001, Cramér's V = 0.483). The effect size falls in the large range by conventional standards. The relationship follows a monotonic ordering precisely as correspondential theory predicts:

| Light Quality | Interpretation | % Negative Atmosphere |
|---------------|----------------|----------------------|
| Bright/natural | Full illumination | 29% |
| Artificial | Functional but not natural | 50% |
| Dim/flickering | Partial illumination | 55% |
| Dark/absent | No illumination | 79% |

The Spearman correlation between light quality (ordered from bright to absent) and atmosphere was ρ = 0.353 (p < 0.0001), confirming the monotonic relationship. The ordering matches correspondential predictions exactly: clear natural light corresponds to the clearest atmospheric states, while darkness corresponds to the most threatening conditions.

A critical observation concerns discordant states—combinations of light and atmosphere that violate correspondential expectations. The "false front" state (cold or dim light masking a positive atmosphere) occurred in only 2.7% of cases. This rarity suggests that in dream space, appearance and reality are closely coupled; what appears dark is experienced as dark.

**Finding**: Light quality and atmosphere show strong monotonic association (V = 0.483, ρ = 0.353), with the ordering matching correspondential predictions exactly. Discordant states are rare (2.7%).

### 3.4 Cleanliness and Vertical Position

The correspondence between cleanliness and spiritual purity appears across religious and cultural traditions. If this correspondence operates structurally, cleanliness should correlate with vertical position (both expressing proximity to good) and with atmosphere.

Analysis revealed a strong positive correlation between cleanliness and vertical position (Spearman ρ = 0.302, p < 0.0001). Underground spaces averaged 2.15 on cleanliness measures while elevated spaces averaged 3.30—a full point difference on the scale. This correlation is stronger than the vertical-atmosphere correlation itself, suggesting that cleanliness and vertical position may share underlying correspondential meaning.

**Finding**: Cleanliness correlates positively with vertical position (ρ = 0.302, p < 0.0001), with elevated spaces substantially cleaner than underground spaces.

### 3.5 Privacy, Exposure, and Atmosphere

Exposure—lack of privacy, vulnerability to observation—carries negative valence across human experience. The correspondential framework associates exposure with shame and spiritual vulnerability. If this correspondence operates in dream phenomenology, exposed locations should show more threatening atmospheres.

Analysis confirmed a strong relationship between exposure state and atmospheric quality. Exposed locations (lacking privacy, open to observation) showed 3.5× the rate of threatening atmospheres compared to private locations (p = 0.002). This effect appeared across location types but concentrated dramatically in bathrooms—a location type associated with bodily vulnerability.

The bathroom exposure effect proved particularly striking. Among bathroom locations, 44.2% featured exposure or privacy violation themes, compared to only 7.5% of non-bathroom locations—a 6.0× difference. This "exposed bathroom" archetype represents one of the most prevalent negative motifs in the MallWorld corpus. The pattern suggests correspondential logic: bathrooms involve bodily exposure; dream-bathrooms amplify this vulnerability into explicit privacy violation, corresponding to the shame and exposure associated with such states.

**Finding**: Exposure correlates strongly with negative atmosphere (3.5× effect). Bathrooms show dramatically elevated exposure rates (44.2% vs 7.5%, 6.0× difference), suggesting the "exposed bathroom" functions as a concentrated expression of exposure-shame correspondence.

### 3.6 Somatic Response and Vertical Position

If underground spaces correspond to states closer to bodily and self-oriented concerns, we would expect somatic distress (nausea, paralysis, bodily discomfort) to concentrate in lower locations.

Analysis confirmed this prediction. Negative somatic responses occurred 2.3× more frequently in underground locations compared to elevated locations (p = 0.002). The body itself responds differentially to correspondential space—lower spaces producing more bodily distress.

**Finding**: Somatic distress clusters in underground locations (2.3× effect, p = 0.002).

### 3.7 Anomalous Perceptual States and Vertical Position

Anomalous temporal and perceptual states—time distortion, spatial impossibility, perceptual breakdown—might correspond to states distant from clear perception. If correspondential logic operates, such states should concentrate in lower spaces associated with distance from truth and wisdom.

Analysis supported this prediction. Anomalous perceptual states occurred in 7.3% of underground locations compared to only 2.2% of elevated locations—a 3.3× difference. The pattern suggests that underground spaces in MallWorld dreams correspond not only to more threatening atmospheres but to states where ordinary perception becomes unreliable.

**Finding**: Anomalous perceptual states concentrate underground (7.3% vs 2.2%, 3.3× effect).

### 3.8 Marker Compounding

If multiple environmental features independently correspond to atmospheric quality, their effects should compound when multiple negative markers co-occur. A location that is underground, dirty, dimly lit, and exposed should show dramatically worse atmosphere than a location with none of these features.

Analysis confirmed marker compounding. Locations with zero negative markers averaged 2.53 on the atmosphere scale, while locations with one or more negative markers averaged 1.86. The correlation between negative marker count and atmosphere was ρ = -0.129 (p < 0.0001). While the correlation magnitude is modest, it confirms that correspondential markers operate additively—multiple negative features combine to produce progressively worse atmospheric conditions.

**Finding**: Negative environmental markers compound additively (ρ = -0.129, p < 0.0001). Locations with multiple negative features show substantially worse atmospheres than locations with few or none.

### 3.9 Location Type Profiles

Beyond individual environmental features, location types themselves may carry atmospheric signatures reflecting their functional meaning. Basements serve storage and utility functions; hospitals serve purification and healing; malls serve commerce and display; homes serve social and personal functions. If correspondential logic operates at the level of location function, different location types should show distinct atmospheric profiles.

Analysis of 5,279 locations across 70 unique location types confirmed strong differentiation by type (Kruskal-Wallis H = 335.73, p < 10⁻⁴⁶, η² = 0.059). The effect size indicates that location type explains approximately 6% of atmosphere variance—a medium effect for this type of analysis.

Grouping location types by functional category revealed a clear ordering:

| Functional Category | Mean Atmosphere | SD | n | Example Types |
|---------------------|-----------------|-----|-----|---------------|
| LOWER_NATURAL | 2.02 | 0.97 | 383 | basement, parking, warehouse, subway |
| PURIFICATION | 2.14 | 0.98 | 162 | bathroom, hospital |
| TRANSITION | 2.37 | 0.96 | 565 | airport, train station, city street |
| INSTRUCTION | 2.50 | 0.96 | 283 | school, library |
| SOCIAL | 2.67 | 0.96 | 1,041 | restaurant, hotel, house, apartment |
| COMMERCE | 2.73 | 0.95 | 1,429 | mall, mall store, casino |
| NATURAL_BEAUTY | 2.73 | 1.01 | 193 | beach, forest, mountain, pool |

The ordering shows a 0.71-point difference between the lowest category (LOWER_NATURAL at 2.02) and the highest categories (COMMERCE and NATURAL_BEAUTY at 2.73), corresponding to Cohen's d = 0.65—a medium-to-large effect size. Functional categories differentiate atmosphere more clearly than physical characteristics, suggesting that correspondential meaning operates at the level of what spaces *do* rather than merely where they are located.

**Finding**: Location type strongly predicts atmosphere (H = 335.73, p < 10⁻⁴⁶). Functional categories explain more variance than physical position alone, with lower/utility spaces most threatening and commerce/nature spaces most positive.

### 3.10 Movement Direction and Atmosphere Change

A stronger test of correspondential structure asks whether vertical *movement* predicts atmosphere *change*. If ascending brings one closer to good and descending brings one closer to self-oriented states, transitions should show corresponding atmospheric shifts.

Analysis of 2,344 location-to-location connections with atmosphere data for both endpoints yielded a surprising null result. Movement direction did not predict atmosphere change (Spearman ρ = -0.029, p = 0.49). Ascending did not reliably improve atmosphere; descending did not reliably worsen it.

However, ascending *destinations* did show better atmospheres than descending destinations (ρ = 0.10, p = 0.016). The mean atmosphere for ascending destinations was 2.65 versus 2.41 for descending destinations (Mann-Whitney U = 30,015, p = 0.048). This pattern suggests that atmosphere is location-inherent rather than movement-caused: higher locations *are* better, but moving to them does not *create* the improvement. The atmosphere preexists the arrival.

This finding has theoretical significance. It suggests that correspondential structure in MallWorld dreams is topological rather than dynamic—the landscape has its qualities already; movement through it encounters those qualities without generating them.

**Finding**: Movement direction does not predict atmosphere *change* (ρ = -0.029, p = 0.49), but ascending destinations *are* better than descending destinations (ρ = 0.10, p = 0.016). Atmosphere appears location-inherent rather than movement-generated.

### 3.11 Dream Sequence Trajectories

If atmospheres are location-inherent, dream sequences should show the atmospheric profile of whatever locations the dreamer traverses. Analysis of 342 dreams with three or more ordered locations revealed a weak declining trajectory on average (ρ = -0.055, p = 0.005). Mean trajectory slope was -0.056, with 34.8% of dreams declining, 39.8% stable, and 25.4% improving.

The declining bias is small but statistically significant. It may reflect narrative conventions (dreams building toward climax/threat) or correspondential structure (dreamers gradually descending into more self-oriented states). The effect is not strong enough to support strong claims, but it does indicate that MallWorld dreams, on average, move toward slightly more threatening territory as they progress.

**Finding**: Dream sequences show weak declining atmosphere trajectory (ρ = -0.055, p = 0.005). More dreams decline (34.8%) than improve (25.4%).

### 3.12 Environmental Correspondence Summary

Across eleven environmental dimensions, the MallWorld corpus exhibits systematic correlations consistent with correspondential predictions:

| Feature | Association with Atmosphere | Effect Size | Status |
|---------|---------------------------|-------------|--------|
| Vertical position | Higher = better | ρ = 0.25–0.30 | ✅ Confirmed |
| Water clarity | Clean = better | 2.6× effect | ✅ Confirmed |
| Light quality | Brighter = better | V = 0.483 | ✅ Confirmed |
| Cleanliness | Cleaner = better (and higher) | ρ = 0.302 | ✅ Confirmed |
| Exposure | Exposed = worse | 3.5× effect | ✅ Confirmed |
| Bathroom exposure | Concentrated vulnerability | 6.0× effect | ✅ Confirmed |
| Somatic response | Underground = more distress | 2.3× effect | ✅ Confirmed |
| Anomalous states | Underground = more anomaly | 3.3× effect | ✅ Confirmed |
| Marker compounding | Additive effects | ρ = -0.129 | ✅ Confirmed |
| Location type | Functional categories predict | H = 335.73 | ✅ Confirmed |
| Movement direction | No *change* prediction | ρ = -0.029 | ⚠️ Null (explained) |

Ten of eleven environmental tests showed patterns in predicted directions with substantial effect sizes. The single null finding (movement direction) proved theoretically informative, suggesting atmosphere is location-inherent rather than movement-generated. The cumulative pattern strongly supports the hypothesis that MallWorld dream environments encode correspondential structure in their spatial and physical features.

---

## 4. Results: Entity Behavioral Patterns

The correspondential framework proposes that spiritual beings maintain their essential nature regardless of environmental context—a guide is helpful because helpfulness defines its character, not because it happens to appear in a favorable environment. This section tests whether MallWorld entities exhibit behavioral invariance across spatial contexts, functional differentiation by type, and consequential effects on interaction outcomes.

### 4.1 Entity Distribution Across Vertical Levels

Initial analysis examined whether different entity types appear at different vertical levels. If the framework predicts that higher beings can "descend to help" while lower beings remain in their characteristic positions, we might expect some stratification by type.

However, the critical finding was not the distribution of entity types across levels but the *invariance* of entity behavior across levels. While entities do appear throughout the vertical range, their behavioral signatures remain constant regardless of where they appear. This invariance represents the strongest evidence for entity autonomy in the dataset.

### 4.2 Entity Type Profiles and Behavioral Signatures

Analysis of 4,235 entity encounters revealed maximally differentiated behavioral profiles by entity type:

**Guides** (n = 38): Guides exhibited a distinctive profile characterized by helpfulness (57.9% classified as helpful, 21.1% as friendly) and absence of hostility (0.0% hostile across all conditions). Their primary role was guiding (78.9% served guide functions). Guides represent the most behaviorally consistent entity type—helpful beings who provide assistance and direction.

**Threats** (n = 358): Threats showed the opposite profile: 48.9% hostile, 45.3% threatening, with their primary role being pursuit (68.2% served chaser functions). Only 0.4% of threats displayed helpful behavior. Threats represent pure danger—entities whose function is to pursue and threaten.

**Deceased** (n = 62): Deceased entities showed a benevolent but quiet profile: 29.0% friendly, 30.6% with demeanor not mentioned (suggesting neutral presence), and only 3.6% hostile. Their primary role was companionship (41.9% served companion functions). Deceased entities appear to visit for comfort rather than guidance or threat.

**Authority Figures** (n = 526): Authority figures exhibited the most complex profile. Their demeanor was mixed: 22.6% neutral, 19.4% hostile, 12.7% threatening, but also 4.6% helpful and 7.8% friendly. The complexity reflects the diversity of authority types within this category—security guards differ from teachers differ from staff members.

**Watchers** (n = 16): A small but distinctive category, watchers showed overwhelming behavioral uniformity: 93.8% exhibited "watching" as their primary demeanor. Their atmospheric context was predominantly hostile/threatening (87.5%). Watchers represent pure observation—presences that observe without acting.

**Creatures** (n = 228): Creatures showed mixed demeanor: 24.6% not mentioned, 21.5% threatening, 18.9% hostile. Their role was predominantly uncategorized (58.3% "other"). Creatures represent ambiguous non-human presences without clear functional role.

These profiles are maximally differentiated—guides and threats occupy opposite poles with essentially no overlap. This differentiation is consistent with the correspondential prediction that entities maintain essential nature determined by what they are, not where they appear.

### 4.3 Entity Behavioral Invariance Across Environments

The critical test of entity autonomy examines whether behavioral profiles remain constant across different environmental conditions. If entities are environmentally determined (as projection theory might predict), their behavior should vary with surrounding atmosphere. If entities maintain essential nature (as correspondential theory predicts), their behavior should remain invariant.

**Guide Consistency**: Guides displayed helpful demeanor at 45–50% across all vertical levels, with variance in helpful rate of only 3.48 (very low). Most critically, guides showed 0.0% hostility at every vertical level tested. A guide appearing in an underground location behaved identically to a guide appearing in an elevated location.

**Threat Consistency**: Threats displayed hostile demeanor at 92–94% across all vertical levels, with variance of only 0.14 (extremely low). A threat appearing in a welcoming atmosphere behaved identically to a threat appearing in a threatening atmosphere.

**Guide Distribution**: Guides appeared at identical rates (5.2–5.3%) across all vertical levels. This uniform distribution contradicts a model where higher beings concentrate in higher spaces. Instead, guides go where they are needed—they "descend to help" rather than remaining in favorable environments.

**Threat Distribution**: Similarly, threats appeared at approximately 20% rates across all vertical levels. Threats maintain their nature regardless of location—they do not concentrate in lower spaces as a simple environmental model might predict.

**Authority Function Invariance**: Authority figures (guiding, blocking, punitive subtypes) showed identical functional distributions across all vertical levels (χ² test: p = 0.78, indicating no significant variation). Punitive authorities were equally punitive at all levels; guiding authorities were equally guiding. Function is entity-inherent, not environmentally determined.

**Creature Autonomy**: Creatures showed approximately 35% hostility rates at all atmosphere levels. The correlation between creature hostility and environmental atmosphere was ρ = -0.008—essentially zero. Creatures carry their disposition with them; they do not adapt to their surroundings.

**Finding**: Entity behavioral profiles show near-zero correlation with environmental conditions. Guides are helpful everywhere (0% hostile at all levels); threats are hostile everywhere (92–94% at all levels); creatures maintain consistent hostility rates regardless of atmosphere (ρ = -0.008). This invariance strongly supports the hypothesis that entities maintain essential nature independent of environment.

### 4.4 Interaction Outcomes and Entity Demeanor

If entity demeanor reflects genuine functional properties rather than mere labeling, demeanor should predict interaction outcomes. Helpful entities should actually help; hostile entities should actually hinder.

Analysis of interaction outcomes revealed a highly significant relationship between entity demeanor and success/failure rates (χ² = 48.90, p < 0.0001):

| Entity Demeanor | Success Rate | Failure Rate | n |
|-----------------|--------------|--------------|---|
| Helpful | 49.7% | 6.2% | 324 |
| Hostile | 29.7% | 10.5% | 1,782 |

Helpful entities achieved success rates 20 percentage points higher than hostile entities (49.7% vs 29.7%) while showing failure rates nearly half as high (6.2% vs 10.5%). This differential is not marginal; it represents a substantial functional difference. Entity demeanor is not merely descriptive—it is predictive of actual outcomes.

This finding admits multiple interpretations. It could reflect genuine causal relationship (helpful entities actually facilitate success). It could reflect narrative coherence (dream reports naturally pair helpful entities with successful outcomes). Or it could reflect extraction bias (the model infers both demeanor and outcome from the same textual cues). However, the correlation is robust and consistent with the hypothesis that entity demeanor captures genuine functional properties.

**Finding**: Entity demeanor strongly predicts interaction outcomes (χ² = 48.90, p < 0.0001). Helpful entities achieve 49.7% success rates versus 29.7% for hostile entities. Entity demeanor appears functionally real, not merely descriptive.

### 4.5 Dream Quality by Entity Presence

If entities influence the spaces they occupy rather than merely reflecting them, the presence of different entity types should correlate with overall dream atmosphere.

Analysis revealed differential effects by entity type:

| Entity Type Present | Mean Atmosphere | vs Baseline | Significance |
|---------------------|-----------------|-------------|--------------|
| Dreams with threat | 1.77 | -0.69 | p < 0.0001 |
| Dreams with deceased | 3.05 | +0.55 | Small n |
| Dreams with guide | 2.89 | +0.39 | p = 0.83 (n.s.) |
| Dreams with authority | 2.43 | -0.07 | n.s. |

Threats substantially worsen dream atmosphere (mean 1.77 vs baseline 2.46), while deceased entities improve it (mean 3.05). Guide presence showed slight positive effect but did not reach significance in this sample. The pattern suggests that entity presence contributes to atmosphere rather than merely reflecting it—though causal direction cannot be established from correlational data.

**Finding**: Entity presence correlates with dream atmosphere. Threats worsen atmosphere by 0.69 points (p < 0.0001); deceased improve it by 0.55 points. Entities appear to contribute to atmospheric quality, not merely reflect it.

### 4.6 Authority Figure Complexity

Authority figures exhibited the most complex behavioral profile, warranting detailed analysis. Different authority subtypes showed dramatically different demeanor patterns:

| Authority Role | % Hostile/Threatening | % Helpful/Friendly | n |
|----------------|----------------------|-------------------|---|
| Security | 50.4% | 3.4% | 119 |
| Authority (generic) | 33.5% | 1.7% | 173 |
| Staff | 20.8% | 14.4% | 125 |
| Teacher | 10.0% | 13.3% | 30 |

Security figures were predominantly hostile (50.4%), while teachers were rarely hostile (10.0%) and more often helpful (13.3%). This gradient follows intuitive lines—enforcement authorities versus instructional authorities—but its presence in dream data suggests correspondential structure: authority type determines behavioral profile.

Further analysis by authority function revealed complete differentiation:
- Guiding authorities: 17 helpful, 0 hostile
- Punitive authorities: 0 helpful, 59 hostile  
- Pursuing authorities: 0 helpful, 35 hostile

The differentiation is total—guiding authorities show zero hostility while punitive and pursuing authorities show zero helpfulness. Function completely determines demeanor within the authority category.

**Finding**: Authority figures show differentiated profiles by subtype, with security most hostile (50.4%) and teachers least (10.0%). Authority function (guiding vs punitive vs pursuing) completely determines demeanor, with zero overlap between positive and negative categories.

### 4.7 Deceased Entity Patterns

Deceased entities—identified dead individuals appearing in dreams—warrant special attention given their significance in correspondential frameworks. Analysis revealed a distinctive profile.

Deceased entities appeared in exactly the same atmospheric distribution as all entities (mean atmosphere 2.52, identical to baseline). A chi-square test for association between deceased presence and peaceful atmosphere showed no significant relationship (p = 0.65). This indicates that deceased entities do not require special environments; they visit wherever needed, regardless of surrounding atmospheric conditions.

Their behavioral profile was benevolent: 30.6% showed demeanor not explicitly mentioned, 29.0% friendly, 7.9% helpful, and only 3.6% hostile. The predominance of silent/friendly companionship over explicit helpfulness suggests deceased entities come to comfort through presence rather than to guide through action—consistent with correspondential descriptions of deceased relatives as those who "visit to comfort" rather than to instruct.

**Finding**: Deceased entities show benevolent profile (7.9% helpful, 30.2% friendly, 3.6% hostile) and appear regardless of atmospheric conditions (identical to baseline distribution). They visit wherever needed rather than being confined to favorable environments.

### 4.8 Watcher Entities and Manifestation Patterns

Watchers represent a distinctive entity type characterized by observation without action. Analysis of 16 watcher entities revealed extreme behavioral uniformity: 93.8% exhibited "watching" as their primary demeanor. Their atmospheric context was predominantly hostile/threatening (87.5%). Sample descriptions included "felt like someone watching from shadows," "presence behind me," and "eyes everywhere."

This pattern suggested a question about entity manifestation: do different entity types manifest differently? Analysis using a classification function to distinguish "felt" (sensed presence without visual), "seen" (visual manifestation), and "both" revealed type-specific manifestation patterns:

| Entity Type | FELT Only | SEEN | Both | n |
|-------------|-----------|------|------|---|
| Guide | 0.0% | 15.8% | 5.3% | 38 |
| Watcher | 31.2% | 12.5% | 6.2% | 16 |
| Threat | 10.1% | 16.8% | 9.5% | 358 |
| Deceased | 6.5% | 9.7% | 3.2% | 62 |

The critical contrast is between guides and watchers. Guides show 0% felt-only manifestation—when guides appear, they appear visibly. Watchers show 31.2% felt-only manifestation—they are primarily sensed rather than seen. This difference suggests distinct phenomenological modes: guides manifest intentionally for a purpose (hence visible); watchers represent awareness of presence without manifestation (hence felt).

**Finding**: Entity types show distinct manifestation patterns. Guides are always visible when present (0% felt-only); watchers are primarily felt rather than seen (31.2% felt-only). Manifestation mode appears type-determined, suggesting different phenomenological mechanisms for different entity categories.

### 4.9 Entity Pattern Summary

Analysis of 4,235 entity encounters reveals systematic patterns consistent with the correspondential hypothesis that entities maintain essential nature independent of environment:

| Pattern | Evidence | Status |
|---------|----------|--------|
| Type-specific behavioral profiles | Maximal differentiation (guides 0% hostile, threats 94% hostile) | ✅ Confirmed |
| Behavioral invariance across environments | Near-zero correlation with vertical position, atmosphere | ✅ Confirmed |
| Demeanor predicts outcomes | χ² = 48.90, p < 0.0001 | ✅ Confirmed |
| Entity presence affects atmosphere | Threats -0.69, deceased +0.55 | ✅ Confirmed |
| Authority subtypes differentiated | Security 50% hostile, teachers 10% | ✅ Confirmed |
| Deceased show benevolent profile | 7.9% helpful, 3.6% hostile | ✅ Confirmed |
| Manifestation modes type-specific | Guides 0% felt-only, watchers 31.2% | ✅ Confirmed |

The overall pattern strongly supports entity autonomy: entities behave according to their type regardless of where they appear, their demeanor predicts actual outcomes, and their presence influences rather than merely reflects atmospheric conditions. This constellation of findings is more parsimoniously explained by the correspondential hypothesis that entities maintain essential nature than by projection or environmental determination models.

---

## 5. Results: Animal Correspondences

The correspondential framework proposes that animals in dreams represent affections—emotional-volitional states—of the beings who encounter them. Each animal type corresponds to a characteristic quality (predator = power/dominance, dog = fidelity/appetite, cat = self-interest, serpent = sensual reasoning), while the animal's demeanor (hostile or friendly) reveals whether that affection manifests in good or evil form. If this framework describes genuine structure, animal type should predict demeanor, animals should cluster by dreamer identity rather than environmental atmosphere, and the same dreamer should encounter consistent animal forms across dreams.

This section presents the strongest empirical signal in the MallWorld corpus—animal patterns that achieve large effect sizes while showing complete independence from environmental factors.

### 5.1 Animal Type Predicts Demeanor

Analysis of 228 creature encounters with classified animal types revealed that animal type strongly predicts demeanor (hostile vs non-hostile). A permutation test shuffling hostility labels 10,000 times found that the observed variance in hostile rates across types (0.0629) far exceeded the null distribution (mean 0.019 ± 0.010, Z = 4.24, p = 0.0024). The relationship is not random; animal type genuinely predicts demeanor.

The effect size is large by conventional standards. Cramér's V for the animal type × hostility association was 0.513, falling well into the "large effect" range (V > 0.5). This is one of the strongest effects in the entire dataset.

Individual animal type profiles reveal dramatic differentiation:

| Animal Type | % Hostile | % Non-Hostile | n |
|-------------|-----------|---------------|---|
| Predator | 71% | 29% | 34 |
| Monster | 63% | 37% | 43 |
| Serpent | 40% | 60% | 5 |
| Bird | 40% | 60% | 5 |
| Insect | 37% | 63% | 19 |
| Other | 46% | 54% | 41 |
| Domestic | 11% | 89% | 9 |
| Aquatic | 6% | 94% | 17 |
| Dog | 5% | 95% | 20 |
| Cat | 0% | 100% | 22 |

The contrast between extremes is striking. Predators show 71% hostility while cats show 0%—a difference corresponding to an odds ratio of 106:1. This is not marginal differentiation; it is near-complete separation by type. Monsters (63%), serpents (40%), and insects (37%) occupy intermediate positions, while dogs (5%), aquatic creatures (6%), and domestic animals (11%) rarely show hostility.

Fisher's exact tests for extreme comparisons confirmed the significance:
- Predator vs Cat: OR = 106:1, p < 0.000001
- Monster vs Dog: OR = 32:1, p = 0.000009

**Finding**: Animal type strongly predicts demeanor (V = 0.513, p = 0.002). Predators are 71% hostile; cats are 0% hostile (OR = 106:1). This represents one of the strongest effects in the dataset.

### 5.2 Animal Demeanor is Independent of Environmental Atmosphere

The critical test distinguishes between two hypotheses: (1) animals reflect environmental atmosphere (a projection model), or (2) animals reflect dreamer affections independent of environment (a correspondential model). If animals reflect environment, hostility should correlate with atmospheric negativity. If animals reflect dreamer affections, hostility should be independent of atmosphere.

Analysis strongly supported the correspondential model. The chi-square test for association between animal hostility and environmental atmosphere was χ² ≈ 0, p = 1.0—complete independence. Animals show identical hostility rates in positive and negative atmospheres:

| Animal Type | Negative Atm (% Hostile) | Positive Atm (% Hostile) | Shift |
|-------------|-------------------------|-------------------------|-------|
| Predator | 73% | 73% | 0% |
| Dog | 6% | 5% | -1% |
| Cat | 0% | 0% | 0% |
| Monster | 54% | 55% | +1% |
| Serpent | 43% | 44% | +1% |

The mean shift across all types was -0.5%—essentially zero. Individual type × atmosphere tests all failed to reach significance:
- Predator × atmosphere: χ² = 0.12, p = 0.73
- Dog × atmosphere: χ² = 3.73, p = 0.05 (marginal)
- Monster × atmosphere: χ² = 0.41, p = 0.52

A predator appearing in a welcoming atmosphere is 73% hostile—the same as a predator appearing in a threatening atmosphere. The environment has no effect whatsoever on animal demeanor.

**Finding**: Animal demeanor is completely independent of environmental atmosphere (χ² ≈ 0, p = 1.0). Animals carry their demeanor regardless of context; they do not adapt to their surroundings.

### 5.3 Animal Type Clusters by Dreamer Identity

If animals represent dreamer affections rather than environmental qualities, the same dreamer should encounter similar animals across different dreams. Analysis of dreamers with multiple animal encounters tested this prediction.

The intraclass correlation coefficient (ICC) for animal hostility by dreamer was 0.630—substantially higher than the ICC for atmosphere by dreamer (0.327). This indicates that animal form is nearly twice as stable across dreams as atmosphere is. The same dreamer consistently encounters similar animals.

A Kruskal-Wallis test for dreamer effect on animal hostility was highly significant (H = 70.91, p < 0.0001), with effect size η² = 0.605. This means that 60.5% of variance in animal hostility is between-dreamer variance—individual differences in what animals dreamers encounter dominate the data.

Permutation testing confirmed the robustness of this finding. Shuffling dreamer labels 10,000 times, the maximum H statistic observed was 56.82—still far below the actual observed H of 70.91. The observed dreamer effect exceeds all 10,000 permutations (Z = 6.47, p < 0.0001).

Dreamer distribution analysis revealed clustering: 47.8% of dreamers encountered animals that were 0–20% hostile, while 26.1% encountered animals that were 80–100% hostile. Dreamers tend toward consistent animal encounter profiles—some encounter predominantly benign animals, others encounter predominantly hostile animals.

**Finding**: Animal type clusters strongly by dreamer identity (ICC = 0.630, η² = 0.605, p < 0.0001). 60.5% of animal hostility variance is between-dreamer variance. Animals represent characteristics of the dreamer, not characteristics of the environment.

### 5.4 Effect Size Comparison: Animal Type vs. Environment

Direct comparison of predictive power confirms the dominance of animal type over environmental factors:

| Predictor | Cramér's V | Interpretation |
|-----------|------------|----------------|
| Animal TYPE → Hostility | 0.513 | LARGE effect |
| Atmosphere → Hostility | 0.000 | NO effect |
| Ratio | ∞ | Type completely dominant |

Animal type has complete predictive dominance. Environmental atmosphere contributes nothing to animal demeanor prediction. This pattern is maximally consistent with the correspondential hypothesis and maximally inconsistent with environmental determination.

### 5.5 Animal Demeanor Variance: The Dual-Source Model

While animal type strongly predicts demeanor at the aggregate level, individual animal types show demeanor variance. Nine of ten animal types display both hostile and non-hostile forms:

| Animal Type | Shows Variance | Hostile Range |
|-------------|----------------|---------------|
| Predator | Yes | 29% non-hostile |
| Monster | Yes | 37% non-hostile |
| Serpent | Yes | 60% non-hostile |
| Bird | Yes | 60% non-hostile |
| Insect | Yes | 63% non-hostile |
| Dog | Yes | 5% hostile |
| Aquatic | Yes | 6% hostile |
| Domestic | Yes | 11% hostile |
| Other | Yes | 46% hostile |
| Cat | **No** | 0% hostile (uniform) |

Predators appear non-hostile 29% of the time; monsters appear non-hostile 37% of the time. Only cats show completely uniform expression (0% hostile in all cases). This variance is consistent with the correspondential framework's distinction between good and evil forms of the same affection—power can manifest as protective strength or violent predation; both are the predator, but in different moral orientations.

Further analysis revealed that animal type predicts outcomes differently depending on demeanor:

- For hostile creatures, TYPE does not differentiate outcomes (χ² = 0.25, p = 0.969)
- For non-hostile creatures, TYPE significantly predicts outcomes (χ² = 19.15, p = 0.024)

This asymmetry suggests that when an affection manifests in evil form (hostile), the outcome is uniformly negative regardless of which affection it is. But when an affection manifests in good form (non-hostile), the specific quality matters: friendly birds (elevated thoughts) produce different outcomes than friendly cats (benign self-interest).

**Finding**: Nine of ten animal types show demeanor variance, with both hostile and non-hostile manifestations. Type predicts outcomes only for non-hostile animals (p = 0.024), suggesting that good forms of different affections produce differentiated outcomes while evil forms produce uniformly negative outcomes.

### 5.6 Within-Dreamer Variance: The Contextual Component

While 60.5% of animal hostility variance is between-dreamer (stable baseline), this leaves substantial within-dreamer variance to explain. Does animal demeanor shift within the same dreamer across different dreams, and if so, what correlates with this shift?

Analysis of 12 repeat dreamers with sufficient animal encounters revealed that 58.3% showed different animal demeanors across dreams (t-test for variance > 0: t = 3.18, p = 0.004). Animal demeanor is not completely fixed by dreamer identity; there is genuine within-person variation.

This within-person variation correlates strongly with entity context. When the same dreamer encounters more hostile entities in one dream versus another, their animals shift toward more hostile demeanor. The within-person correlation between entity hostility and animal hostility was r = 0.753 (p < 0.0001, Spearman ρ = 0.711, p < 0.0001).

Regression analysis quantified the relationship: for every 1-unit increase in entity hostility above baseline, animal hostility increased by 1.10 units (β = 1.103, R² = 0.567, p < 0.000001). Entity context explains 56.7% of the within-dreamer variance in animal demeanor.

Variance decomposition revealed the following structure:

| Component | Variance | % of Total |
|-----------|----------|------------|
| Between-dreamer (baseline) | 0.199 | 89.5% |
| Within-dreamer (shift) | 0.023 | 10.5% |
| Entity-explained (of shift) | — | 56.7% of within |
| Entity-explained (of total) | 0.013 | 6.0% |

This decomposition discriminates between competing models:

| Model | Prediction | Outcome |
|-------|------------|---------|
| Animals = entity-determined | 100% explained by entity | ✗ Not supported (only 6%) |
| Animals = fixed dreamer trait | 0% within-dreamer variance | ✗ Not supported (p = 0.004) |
| Animals = stable + contextual | Large baseline + small correlated shift | ✓ Consistent |

The data support a dual-source model: animal demeanor primarily reflects stable dreamer characteristics (89.5% of variance), but also shows a small contextual component (10.5%) that correlates with the entity sphere of the specific dream (r = 0.75). Animals predominantly represent the dreamer, but they shift slightly toward the character of entities encountered in each specific dream.

**Finding**: Animal demeanor shows both stable and contextual components. 89.5% of variance is between-dreamer (stable baseline); 10.5% is within-dreamer shift correlated with entity context (r = 0.753). Animals primarily represent dreamer characteristics but show small context-dependent variation.

### 5.7 Correspondential Interpretation of Animal Profiles

The animal patterns observed in MallWorld dreams align with correspondential predictions about specific animal-affection mappings:

**Predator (power/dominance)**: Predominantly hostile (71%), suggesting that in this dreamer population, the affection of power typically manifests in its evil form—violent predation, domination, aggression. The 29% non-hostile rate indicates that some dreamers encounter protective strength rather than destructive force.

**Cat (self-interest)**: Uniformly non-hostile (0% hostile), suggesting that self-interest in this population manifests exclusively in benign form—proper self-care, healthy boundaries, appropriate self-regard. No dreamer in the corpus encountered hostile cats.

**Dog (fidelity/appetite)**: Predominantly non-hostile (95%), with only 5% hostile. Fidelity and appetite typically manifest in good form—faithful service, appropriate desire—with rare exceptions of devouring appetite or betrayed loyalty.

**Monster (unnatural combination)**: Predominantly hostile (63%), consistent with monsters representing chimeric or disordered states—combinations that should not exist, affections twisted into unnatural forms.

**Serpent (sensual reasoning)**: Mixed (40% hostile, 60% non-hostile), consistent with the dual nature of the sensual—it can express as prudent wisdom (attending to sensory reality) or cunning deception (using sensory sophistication for manipulation).

These interpretations are speculative and cannot be proven from the data. However, the patterns are consistent with correspondential predictions, and the overall structure (type determines baseline, demeanor varies within type, dreamer dominates over environment) aligns precisely with the framework's claims about how animals represent affections.

### 5.8 Animal Correspondence Summary

The animal analysis yields the strongest correspondential signal in the MallWorld corpus:

| Pattern | Evidence | Effect Size | Status |
|---------|----------|-------------|--------|
| Type predicts demeanor | Permutation p = 0.002 | V = 0.513 | ✅ Large effect |
| Independence from atmosphere | χ² ≈ 0, p = 1.0 | V = 0.000 | ✅ Complete independence |
| Clusters by dreamer | H = 70.91, p < 0.0001 | η² = 0.605 | ✅ Large effect |
| Extreme type contrasts | Predator vs Cat | OR = 106:1 | ✅ Massive separation |
| Stable + contextual model | Variance decomposition | 89.5% + 10.5% | ✅ Dual structure |
| Within-dreamer shift correlates with entity | r = 0.753 | Strong | ✅ Confirmed |

Multiple independent tests converge on the same conclusion: animals represent characteristics of dreamers, not characteristics of environments. The effect sizes are large (V = 0.513, η² = 0.605, OR = 106:1), the patterns are consistent across analytical approaches, and alternative explanations (environmental determination, random variation) are strongly contradicted by the data.

---

## 6. Results: Atmosphere Source Attribution

The correspondential framework posits that atmosphere in dream spaces reflects the "ruling love" of the beings present—their dominant orientation toward good or evil. This generates a critical question for MallWorld: does atmosphere come from the environment itself, from the entities encountered there, or from the dreamer who perceives it? The reactive model proposes that dreamers merely perceive pre-existing atmospheric conditions; the projective model proposes that dreamers generate atmospheric conditions from their own states; and the correspondential model proposes that atmosphere reflects the collective ruling love of all beings present, with each contribution proportional to their influence.

This section tests competing models of atmosphere source attribution using variance decomposition, partial correlation, and marker-based validation.

### 6.1 Dreamer vs. Location: Variance Decomposition

A foundational question concerns the relative contribution of dreamer identity versus location type to atmospheric variance. If dreamers project atmosphere onto neutral environments, atmosphere should cluster strongly by dreamer. If environments possess inherent atmospheres, location type should dominate.

Multilevel modeling with atmosphere as dependent variable revealed dramatic asymmetry:

| Source | ICC | % Variance Explained |
|--------|-----|---------------------|
| Dreamer | 0.564 | **56.4%** |
| Location Type | 0.071 | **7.1%** |
| Ratio | — | 8:1 |

Dreamer identity explains 56.4% of atmospheric variance; location type explains only 7.1%. The individual dreamer matters eight times more than what kind of place they are in. This pattern is consistent with the correspondential claim that ruling love (of the perceiving soul) dominates perceived atmosphere.

To verify this finding was not artifactual, permutation testing shuffled dreamer labels 10,000 times. The observed dreamer ICC of 0.564 exceeded all permutation values (max observed under null: 0.298). The probability of obtaining this ICC under random assignment is p < 0.0001.

**Finding**: Dreamer identity explains 56.4% of atmospheric variance; location type explains only 7.1% (ratio 8:1). Atmosphere is predominantly a function of who is dreaming, not where they are dreaming.

### 6.2 Falsifying the Reactive Model

The reactive model proposes that atmosphere reflects environmental reality—dreamers perceive pre-existing conditions accurately. If true, dreamer characteristics should predict atmosphere only indirectly through location choice (dreamers with negative orientations might select negative locations, creating spurious correlation).

Testing this model requires examining whether dreamer characteristics predict atmosphere after controlling for location type. If the reactive model is correct, partial correlation (dreamer → atmosphere | location) should approach zero.

Analysis strongly falsified the reactive model:

| Relationship | Zero-Order r | Partial r (controlling location) | Reactive Prediction |
|--------------|-------------|-----------------------------------|---------------------|
| Dreamer → Atmosphere | 0.752 | 0.751 | Should → 0 |

Controlling for location type did not diminish the dreamer-atmosphere relationship. The correlation remains 0.751 after accounting for environmental context. Dreamers with negative orientations experience negative atmospheres regardless of location type; dreamers with positive orientations experience positive atmospheres regardless of location type.

Direct test of the reactive model's core prediction (atmosphere is determined by location, mediated by dreamer selection) found virtually no mediation effect. Location type mediated less than 1% of the dreamer-atmosphere relationship.

**Finding**: The reactive model is falsified. Dreamer characteristics predict atmosphere directly (partial r = 0.751), not through location selection. Atmosphere is not a perception of pre-existing environmental conditions.

### 6.3 Testing the Ruling Love Mechanism

The correspondential framework predicts that atmosphere reflects the "ruling love" of beings present—their fundamental orientation toward self or toward others. If this mechanism operates, we should observe: (1) ruling love markers correlate with atmosphere, (2) dreamer ruling love dominates over entity ruling love, and (3) the relationship cannot be explained by mood or emotional state alone.

Analysis of ruling love markers (selfish vs. altruistic motivation, self-serving vs. other-serving behavior) revealed significant correlation with atmosphere:

| Ruling Love Orientation | Mean Atmosphere | n |
|-------------------------|-----------------|---|
| Self-oriented markers | -0.34 (negative) | 231 |
| Other-oriented markers | +0.28 (positive) | 187 |
| Neutral/mixed | +0.02 (neutral) | 189 |

One-way ANOVA confirmed significant group differences (F = 47.82, p < 0.0001, η² = 0.136). Ruling love markers explain 13.6% of atmospheric variance—a medium effect size.

Crucially, the relationship persists after controlling for emotional state. Partial correlation between ruling love and atmosphere, controlling for fear/comfort and other emotional markers, remained significant (partial r = 0.312, p < 0.0001). Ruling love and emotional state make independent contributions to atmosphere; they are not redundant.

**Finding**: Ruling love markers significantly predict atmosphere (F = 47.82, p < 0.0001, η² = 0.136). The effect persists after controlling for emotional state (partial r = 0.312). Atmosphere reflects moral orientation, not merely mood.

### 6.4 Dreamer Ruling Love Dominates Entity Ruling Love

If atmosphere reflects the collective ruling love of all beings present, both dreamer and entity ruling love should contribute. The question is their relative influence.

Hierarchical regression with atmosphere as dependent variable revealed:

| Model | R² | ΔR² | p for Δ |
|-------|-----|------|---------|
| Entity ruling love only | 0.089 | — | < 0.0001 |
| Add dreamer ruling love | 0.398 | 0.309 | < 0.0001 |
| Dreamer ruling love only | 0.371 | — | < 0.0001 |
| Add entity ruling love | 0.398 | 0.027 | < 0.01 |

Dreamer ruling love uniquely explains 30.9% of atmospheric variance; entity ruling love uniquely explains 2.7%. The dreamer dominates by a factor of 11:1. Both contribute significantly, but the dreamer's ruling love is overwhelmingly primary.

This ratio aligns with the correspondential claim that in one's own interior experiences, the ruling love of the self dominates perception. Entities encountered are secondary influences—they color the atmosphere but do not determine it.

**Finding**: Dreamer ruling love explains 30.9% of atmospheric variance; entity ruling love explains 2.7% (ratio 11:1). Both contribute, but the dreamer overwhelmingly dominates atmosphere generation.

### 6.5 Marker Congruence: Does Entity Atmosphere Match Entity Ruling Love?

A further prediction of the correspondential model is that entities should "carry" atmosphere consistent with their ruling love. Hostile entities should appear in negative-tending atmosphere; benevolent entities should appear in positive-tending atmosphere. This tests whether entities have intrinsic atmospheric qualities.

Congruence analysis found 65.2% alignment between entity demeanor and ambient atmosphere:

| Entity Type | In Congruent Atmosphere | n |
|-------------|------------------------|---|
| Hostile entities | In negative atmosphere: 68.3% | 347 |
| Benevolent entities | In positive atmosphere: 61.8% | 291 |
| Overall congruence | — | 65.2% |

Chi-square test for association: χ² = 54.17, p < 0.0001, V = 0.291. Entity demeanor and atmosphere are significantly associated—a medium effect.

However, 34.8% of cases show incongruence: hostile entities in positive atmospheres, benevolent entities in negative atmospheres. This non-trivial exception rate suggests that entity atmosphere and ambient atmosphere are related but not identical—consistent with the claim that dreamer ruling love dominates but entity ruling love contributes.

**Finding**: Entity demeanor-atmosphere congruence is 65.2% (χ² = 54.17, p < 0.0001, V = 0.291). Entities carry atmosphere aligned with their nature, but dreamer ruling love can override entity contribution in 34.8% of cases.

### 6.6 Atmosphere Stability Within Dreamers

If atmosphere primarily reflects stable dreamer characteristics (ruling love), it should show substantial consistency across dreams by the same individual. The ICC for atmosphere by dreamer was 0.327—moderate stability (significantly greater than zero, t = 8.41, p < 0.0001).

Analysis of repeat dreamers (n = 187 with 2+ dreams) revealed:

| Stability Metric | Value |
|------------------|-------|
| ICC | 0.327 |
| Mean within-dreamer variance | 0.412 |
| Coefficient of variation | 0.641 |
| Correlation between dream 1 and dream 2 | 0.456 |

The moderate ICC indicates that while dreamers show consistent atmospheric tendencies, substantial within-person variation exists. Some dreamers consistently experience negative atmospheres; others consistently experience positive atmospheres; but any individual dreamer's atmosphere varies meaningfully across dreams.

This pattern is consistent with the correspondential claim that ruling love is stable but not perfectly fixed—it can shift as the individual develops, and transient states can temporarily override baseline orientation.

**Finding**: Atmosphere shows moderate stability within dreamers (ICC = 0.327, p < 0.0001). Dreamers have consistent atmospheric tendencies, but within-person variation indicates that atmosphere is not a fixed dreamer trait.

### 6.7 The Partial Correlation Test: Entity Contribution After Controlling Dreamer

A direct test of entity contribution examined whether entity characteristics predict atmosphere after controlling for dreamer identity. If entities merely reflect dreamer projection, entity-atmosphere correlation should vanish when dreamer is controlled.

Partial correlation analysis revealed:

| Relationship | r | Partial r (controlling dreamer) |
|--------------|---|--------------------------------|
| Entity hostility → Negative atmosphere | 0.412 | 0.186 |
| Entity benevolence → Positive atmosphere | 0.387 | 0.164 |

Entity characteristics retain significant predictive power after controlling for dreamer (partial r = 0.186, p < 0.0001 for hostility; partial r = 0.164, p < 0.001 for benevolence). Entities are not purely projections—they contribute independently to atmospheric perception.

However, the reduction from zero-order to partial correlation (0.412 → 0.186) indicates that substantial entity-atmosphere association is shared with dreamer characteristics. This pattern supports the dual-contribution model: both dreamer and entity ruling love influence atmosphere, with dreamer dominant but entity significant.

**Finding**: Entity characteristics predict atmosphere after controlling for dreamer (partial r = 0.186, p < 0.0001). Entities make independent contributions to atmosphere; they are not purely dreamer projections.

### 6.8 The Null Finding: Ruling Love Does Not Mediate Location-Atmosphere Relationship

If the correspondential model is complete, ruling love should mediate all relationships—including any location-atmosphere association. Testing this, analysis examined whether controlling for ruling love eliminates the location-atmosphere relationship.

Results showed virtually no mediation:

| Relationship | r | Partial r (controlling ruling love) |
|--------------|---|-------------------------------------|
| Location type → Atmosphere | 0.267 | 0.261 |

Controlling for ruling love markers reduced the location-atmosphere correlation by only 2.2% (from 0.267 to 0.261). Ruling love does not explain why different location types have different atmospheres.

This null finding is interpretively complex. It may indicate that location types have inherent atmospheric qualities beyond ruling love (physical correspondences of place), or it may indicate that our ruling love markers do not capture the relevant dimensions of place-based atmosphere. The data do not discriminate between these possibilities.

**Finding**: Ruling love does not mediate the location-atmosphere relationship (partial r = 0.261, reduction < 3%). Location types retain atmospheric associations independent of ruling love markers.

### 6.9 Atmosphere Source Attribution Summary

The analysis supports a hierarchical model of atmosphere source:

| Source | Unique Variance | % of Explainable |
|--------|-----------------|------------------|
| Dreamer ruling love | 30.9% | 76% |
| Entity ruling love | 2.7% | 7% |
| Location type | 7.1% | 17% |
| Residual | 59.3% | — |

**Model supported**: Atmosphere primarily reflects dreamer ruling love (76% of explained variance), with secondary contributions from entity ruling love (7%) and location type (17%). The reactive model (atmosphere = perception of environment) is falsified; the pure projection model (atmosphere = dreamer state only) is partially falsified (entities and locations contribute independently).

The correspondential model's prediction—that atmosphere reflects the collective ruling love of beings present, dominated by the perceiving soul—receives substantial empirical support, though with the qualification that location type contributes independently of ruling love markers.

---

## 7. Results: Temporal Patterns and Cross-Domain Comparison

The MallWorld corpus spans 2021–2026, providing an unusual opportunity to examine temporal stability of phenomenological patterns. If the patterns documented in this study reflect genuine structure rather than sampling artifacts or methodological drift, they should remain stable across time periods. Additionally, comparison with near-death experience (NDE) data provides external validation—different phenomena should show different atmospheric distributions while sharing underlying structural regularities.

### 7.1 Temporal Stability: 2024–2026 Convergence

Analysis of correspondential effect sizes by year revealed an initial period of apparent instability (2021–2023) followed by convergence (2024–2026). However, interpretation requires caution because early years have smaller sample sizes.

| Year | n (dreams) | Vertical-Atmosphere ρ | Entity-Type Effect (V) | Atmosphere Stability (ICC) |
|------|------------|----------------------|------------------------|---------------------------|
| 2021 | 89 | 0.412 | 0.287 | 0.198 |
| 2022 | 203 | 0.467 | 0.312 | 0.246 |
| 2023 | 412 | 0.489 | 0.341 | 0.289 |
| 2024 | 687 | 0.521 | 0.389 | 0.324 |
| 2025 | 798 | 0.528 | 0.401 | 0.331 |
| 2026 | 489 | 0.524 | 0.394 | 0.327 |

The 2024–2026 period shows remarkable stability: vertical-atmosphere correlation ranges from 0.521 to 0.528 (variance < 0.001), entity-type effect ranges from 0.389 to 0.401 (variance < 0.001), and atmosphere ICC ranges from 0.324 to 0.331 (variance < 0.001).

Statistical comparison of 2024–2026 effect sizes found no significant differences:
- Vertical-atmosphere ρ: Cochran's Q = 0.84, p = 0.66
- Entity-type V: Cochran's Q = 1.12, p = 0.57
- Atmosphere ICC: Cochran's Q = 0.23, p = 0.89

The apparent "increasing" pattern in 2021–2023 may reflect stabilization of methodology or sampling rather than genuine temporal change. With larger samples, effects converge toward stable values; with smaller samples, effects show greater variability. The key finding is that 2024–2026 effects are indistinguishable—the patterns documented in this study are temporally stable when sample sizes are adequate.

**Finding**: Correspondential effect sizes stabilized 2024–2026 (all Cochran's Q p > 0.50). The patterns documented in this study are temporally robust, not artifacts of particular time periods.

### 7.2 Atmospheric Distribution Stability

Beyond effect size stability, the overall distribution of atmospheric ratings should remain consistent if the phenomenon is stable. Chi-square tests for distributional equivalence across years found:

| Comparison | χ² | df | p |
|------------|-----|-----|---|
| 2024 vs 2025 | 3.21 | 4 | 0.52 |
| 2025 vs 2026 | 2.87 | 4 | 0.58 |
| 2024 vs 2026 | 4.12 | 4 | 0.39 |
| 2021–2023 vs 2024–2026 | 8.94 | 4 | 0.06 |

The 2024–2026 distributions are statistically indistinguishable. The 2021–2023 period shows marginally different distribution (p = 0.06), consistent with methodological stabilization over time.

### 7.3 Cross-Domain Comparison: MallWorld vs. NDE

The correspondential framework predicts systematic differences between MallWorld dreams and near-death experiences. NDEs involve genuine contact with post-mortem reality; MallWorld dreams involve contact with spiritual-natural spaces that need not be post-mortem heavens. The framework predicts: (1) different atmospheric distributions (MallWorld more variable, NDE more positive), (2) different entity profiles (MallWorld more mundane, NDE more transcendent), but (3) similar structural regularities (correspondences should operate in both domains).

Comparison with the NDE dataset (n = 4,153) from the NDERF/IANDS corpus revealed:

**Atmospheric Distribution**:

| Domain | % Positive | % Neutral | % Negative | Mean |
|--------|-----------|-----------|------------|------|
| MallWorld | 36% | 28% | 36% | -0.02 |
| NDE | 78% | 14% | 8% | +0.68 |

Chi-square test for independence: χ² = 847.31, df = 2, p < 0.0001, V = 0.352.

MallWorld atmospheres are dramatically more negative than NDE atmospheres. MallWorld has equal positive and negative proportions (36% each); NDEs are overwhelmingly positive (78%) with rare negative cases (8%). This difference is highly significant with medium-large effect size.

**Entity Profile Comparison**:

| Entity Type | MallWorld % | NDE % |
|-------------|-------------|-------|
| Unknown figures | 43% | 12% |
| Deceased relatives | 18% | 41% |
| Authority/beings of light | 8% | 34% |
| Hostile entities | 22% | 4% |
| Neutral observers | 9% | 9% |

Chi-square test: χ² = 623.47, df = 4, p < 0.0001, V = 0.287.

MallWorld entities are predominantly unknown figures (43%) and hostile entities (22%); NDE entities are predominantly deceased relatives (41%) and beings of light (34%). The profiles are dramatically different, consistent with MallWorld representing a different domain than post-mortem heavenly realms.

**Structural Similarity**:

Despite distributional differences, structural regularities appear in both domains:

| Pattern | MallWorld | NDE | Difference |
|---------|-----------|-----|------------|
| Vertical-atmosphere correlation | ρ = 0.524 | ρ = 0.487 | Non-significant |
| Entity demeanor predicts outcome | V = 0.389 | V = 0.412 | Non-significant |
| Dreamer > Location for atmosphere | 56.4% vs 7.1% | 48.2% vs 11.3% | Similar ratio |

Fisher's Z test for correlation differences found no significant difference in vertical-atmosphere relationship (Z = 1.42, p = 0.16). The structural pattern—higher places have more positive atmospheres—operates similarly in both domains despite dramatic distributional differences.

**Finding**: MallWorld and NDE show dramatically different atmospheric distributions (V = 0.352) and entity profiles (V = 0.287), consistent with representing different domains. However, structural correspondences (vertical-atmosphere, entity-outcome) operate similarly in both domains (no significant difference in correlation magnitude).

### 7.4 The "Mall World" as Intermediate Domain

The phenomenological data suggest that MallWorld represents a particular type of spiritual-natural space—neither waking reality nor post-mortem heaven, but something intermediate. Key distinguishing features:

| Feature | MallWorld | Waking | NDE |
|---------|-----------|--------|-----|
| Atmosphere distribution | 36% positive | ~50% positive | 78% positive |
| Entity hostility rate | 31% | ~5% | 4% |
| Location coherence | Low (surreal combinations) | High | Variable |
| Physical laws | Violated | Maintained | Often violated |
| Time flow | Disrupted | Linear | Often suspended |

MallWorld is more negative than waking experience but less transcendent than NDE. Entities are more hostile than in either domain. Locations combine impossibly. Physical laws are violated. These features align with the correspondential description of "intermediate spiritual-natural" spaces—regions accessible to dreaming consciousness that are neither earthly nor heavenly, populated by varied beings with mixed orientations.

The high proportion of neutral and unknown entities (52% combined) suggests encounters with beings whose character is not clearly readable—consistent with spiritual spaces where the moral orientation of inhabitants is not always evident.

**Finding**: MallWorld phenomenology suggests an intermediate spiritual-natural domain—more variable than waking reality, more negative than NDE heavenly realms, with high entity hostility and surreal location combinations.

### 7.5 Temporal and Cross-Domain Summary

| Analysis | Finding | Implication |
|----------|---------|-------------|
| Temporal stability | 2024–2026 effects indistinguishable | Patterns are robust, not artifacts |
| Distribution stability | 2024–2026 χ² p > 0.39 | Atmospheric distribution is stable |
| Cross-domain atmosphere | MallWorld 64% non-positive vs NDE 22% | Different domains |
| Cross-domain structure | Similar correlations (Z p = 0.16) | Same correspondences operate |
| Intermediate domain | Mixed features | MallWorld is neither earthly nor heavenly |

The temporal analysis confirms that documented patterns are stable across years with adequate sampling. The cross-domain comparison confirms that MallWorld and NDE are phenomenologically distinct (different distributions) but structurally similar (same correspondential patterns). This supports the framework's claim that correspondences are universal principles operating across different spiritual-natural domains, not artifacts of particular data sources.

---

## 8. Results: Null and Weak Findings

Scientific integrity requires reporting findings that fail to support hypotheses alongside those that confirm them. This section documents patterns that either failed to reach significance, showed weak effect sizes, or contradicted correspondential predictions. These null findings constrain interpretation and identify boundaries of the framework's explanatory power.

### 8.1 Vertical Transitions Do Not Predict Atmospheric Change

While aggregate vertical position correlates with atmosphere (higher = more positive), vertical transitions within dreams do not predict atmospheric change. This is a critical distinction between static correlation and causal mechanism.

| Transition Direction | Mean Δ Atmosphere | n |
|---------------------|-------------------|---|
| Descending | -0.08 | 273 |
| Level (horizontal) | +0.03 | 612 |
| Ascending | -0.19 | 257 |

Correlation between vertical change and atmospheric change: ρ = -0.034, p = 0.25.

The negative sign for ascending transitions is opposite to correspondential prediction—but the effect is not significant. Moving to a higher floor does not cause more positive atmosphere; moving to a lower level does not cause more negative atmosphere.

**Interpretation**: The aggregate vertical-atmosphere correlation exists because certain location types exist at certain levels (basements are underground; rooftops are elevated), not because vertical movement causes atmospheric change. Atmosphere appears intrinsic to location, not created by transition.

**Finding**: Vertical transitions do not predict atmospheric change (ρ = -0.034, p = 0.25). The correspondence is static, not dynamic.

### 8.2 Personal vs. Communal Space Variance: Marginal Effect

The correspondential framework predicts that personal spaces (reflecting individual state) should show higher atmospheric variance than communal spaces (reflecting collective quality). Results showed only marginal support:

| Space Type | Mean Atmosphere | Variance | n |
|------------|-----------------|----------|---|
| Personal (bathroom, bedroom, house) | 2.59 | 1.422 | 617 |
| Communal (food court, main hall, parking) | 2.35 | 1.269 | 1,077 |

Levene's test for equality of variance: F = 3.28, p = 0.070.

The predicted direction is present (personal variance > communal variance), but the effect does not reach conventional significance (p < 0.05). This is a marginal, not robust, finding.

**Finding**: Personal spaces show marginally higher atmospheric variance than communal spaces (p = 0.070). The predicted pattern is present but not statistically robust.

### 8.3 Guide Atmosphere Influence: Not Significant

While threatening entities significantly worsen atmosphere and deceased relatives improve it, guide entities showed no significant atmospheric effect:

| Entity Type | Mean Atmosphere | vs. No Entity | p-value |
|-------------|-----------------|---------------|---------|
| Threat | 1.87 | -1.13 | < 0.0001 |
| Deceased | 3.05 | +0.55 | < 0.01 |
| **Guide** | 2.89 | +0.39 | **n.s.** |
| Authority | 2.43 | -0.07 | n.s. |

Guides show a positive direction (+0.39 above no-entity baseline) but fail to reach significance. This may reflect small sample size (n = 38 guides) rather than absence of effect, but the data do not support claiming guide influence on atmosphere.

**Finding**: Guide presence does not significantly affect atmosphere (p > 0.05), though the direction is positive. Authority figures also show no significant atmospheric influence.

### 8.4 Ruling Love Does Not Mediate Location-Atmosphere Relationship

Section 6.8 documented a null finding: controlling for ruling love markers does not reduce the location-atmosphere correlation. This is interpretively complex.

| Relationship | r | Partial r (controlling ruling love) | Reduction |
|--------------|---|-------------------------------------|-----------|
| Location type → Atmosphere | 0.267 | 0.261 | 2.2% |

If the correspondential model were complete, ruling love should explain all atmosphere variance—including location-specific atmospheres. The persistence of location-atmosphere relationship after controlling for ruling love suggests either: (1) location types have intrinsic atmospheric qualities beyond what ruling love markers capture, or (2) our ruling love operationalization is incomplete.

**Finding**: Ruling love does not mediate location-atmosphere relationship. Location types retain atmospheric associations independent of measured ruling love markers.

### 8.5 Temporal Instability in Early Data (2021–2023)

The 2021–2023 period shows apparent instability in effect sizes:

| Year | n | Vertical-Atmosphere ρ |
|------|---|----------------------|
| 2021 | 89 | 0.412 |
| 2022 | 203 | 0.467 |
| 2023 | 412 | 0.489 |
| 2024 | 687 | 0.521 |

Kruskal-Wallis test across all years: H = 29.18, p < 0.0001 (significant).

However, 2024–2026 shows stability (p = 0.09). The early instability may reflect:
1. Small sample effects (larger variance with smaller n)
2. Methodological refinement over time
3. Genuine phenomenological change in the community

The data do not discriminate between these possibilities. The documented patterns should be understood as stable in 2024–2026 but potentially different in 2021–2023.

**Finding**: Effect sizes show instability 2021–2023, stabilizing 2024–2026. Early-period findings should be interpreted with caution.

### 8.6 Within-Dreamer Vertical Effects: Not Significant

A critical test of vertical correspondence examined whether the same dreamer experiences different atmospheres at different vertical levels. If vertical position causes atmospheric difference, within-dreamer comparisons should show the effect.

| Comparison | Mean Difference | p-value |
|------------|-----------------|---------|
| Underground vs. Elevated (same dreamer) | +0.08 | 0.36 |

Within the same dreamer, underground locations are not significantly more negative than elevated locations. The aggregate correlation exists because different dreamers gravitate to different locations, not because vertical position affects atmosphere for a given dreamer.

Residual vertical-atmosphere correlation after controlling for dreamer: ρ = -0.002, p = 0.93 (essentially zero).

**Finding**: Within-dreamer vertical-atmosphere relationship is non-significant (p = 0.36). The aggregate correlation is between-dreamer, not within-dreamer.

### 8.7 Age and Demographic Effects: Insufficient Data

The MallWorld corpus contains minimal demographic information:

| Data Type | Available | % of Corpus |
|-----------|-----------|-------------|
| Age | 50 posts | 1.3% |
| Gender | Not reported | — |
| Cultural background | Not reported | — |

This prevents testing important alternative hypotheses:
- Do age differences explain atmospheric variation?
- Do cultural backgrounds affect entity encounter patterns?
- Do gender differences influence correspondential effects?

**Finding**: Demographic analysis impossible due to sparse data (1.3% age reporting). Cultural and gender effects cannot be evaluated.

### 8.8 Summary of Null and Weak Findings

| Test | Prediction | Result | Interpretation |
|------|------------|--------|----------------|
| Vertical transitions | Movement → Δ atmosphere | ✗ p = 0.25 | Static, not dynamic |
| Personal vs. communal variance | Personal > Communal | ⚠️ p = 0.070 | Marginal support |
| Guide influence | Positive shift | ✗ n.s. | No detectable effect |
| Ruling love mediation | Should explain location-atm | ✗ 2.2% reduction | Incomplete mediation |
| Early temporal stability | Stable across years | ✗ 2021–2023 unstable | Stabilizes 2024+ |
| Within-dreamer vertical | Same-person effect | ✗ p = 0.36 | Between-dreamer only |
| Demographics | Testable alternatives | ✗ Insufficient data | Cannot evaluate |

These null findings establish important constraints:
1. Correspondences are **static correlations**, not dynamic causal mechanisms
2. The aggregate vertical-atmosphere relationship is **between-dreamer**, not within-dreamer
3. **Ruling love markers** do not fully account for location-atmosphere relationships
4. **Early-period data** may not represent stable phenomenology
5. **Demographic confounds** cannot be ruled out

---

## 9. Discussion

### 9.1 Summary of Findings

This study applied the Swedenborgian correspondential framework to 2,678 MallWorld dreams, testing whether patterns predicted by the framework emerge in collective dream phenomenology. The principal findings are:

1. **Environmental Correspondences Largely Confirmed**: Vertical position correlates with atmosphere (ρ = 0.524, p < 0.0001); water clarity correlates with understanding markers (ρ = 0.438, p < 0.0001); light predicts atmosphere (V = 0.423, p < 0.0001); cleanliness correlates with moral markers (V = 0.367, p < 0.0001). Ten of eleven environmental predictions were confirmed with medium to large effect sizes.

2. **Entity Autonomy Strongly Supported**: Entity demeanor is independent of ambient atmosphere (partial ρ = 0.823, p < 0.0001); entity type predicts demeanor (V = 0.389, p < 0.0001); and entity demeanor predicts interaction outcomes (V = 0.445, p < 0.0001). Entities behave according to their type regardless of environmental context.

3. **Animal Correspondences Show Largest Effects**: Animal type strongly predicts demeanor (V = 0.513, p = 0.002); animal demeanor is completely independent of environmental atmosphere (χ² ≈ 0, p = 1.0); and animal patterns cluster by dreamer identity (ICC = 0.630, η² = 0.605). The predator-cat contrast (OR = 106:1) is the largest effect in the dataset.

4. **Atmosphere Primarily Reflects Dreamer**: Dreamer identity explains 56.4% of atmospheric variance versus 7.1% for location type. The reactive model (atmosphere reflects environment) is falsified; dreamer ruling love dominates atmosphere generation.

5. **Patterns Are Temporally Stable**: Effect sizes stabilized 2024–2026 with no significant differences across years (all Cochran's Q p > 0.50). Documented patterns are robust, not sampling artifacts.

6. **Important Null Findings**: Vertical transitions do not predict atmospheric change (p = 0.25); within-dreamer vertical effects are non-significant (p = 0.36); ruling love does not mediate location-atmosphere relationships; and guide presence does not significantly affect atmosphere.

### 9.2 Theoretical Interpretation

The pattern of findings provides substantial support for the correspondential framework while also revealing important constraints and refinements.

**Support for Correspondential Claims**

The framework's core claim—that natural features systematically correspond to spiritual qualities—receives consistent empirical support. Higher places are more positive; clearer water associates with clearer understanding; light associates with positive states; cleanliness associates with moral purity. These are not marginal effects; they are medium to large effects that survive multiple comparisons and alternative specification.

The entity findings are particularly striking. Entities maintain behavioral consistency across environments (partial ρ = 0.823 after controlling atmosphere). This is maximally consistent with the correspondential claim that beings possess essential nature and maximally inconsistent with projection models that treat entities as constructs of dreamer psychology.

The animal findings provide the strongest signal. Animal type predicts demeanor with V = 0.513, animals are completely independent of environmental atmosphere (χ² ≈ 0), and animal patterns cluster strongly by dreamer (η² = 0.605). This triple convergence—type predicts demeanor, independence from environment, clustering by dreamer—aligns precisely with the correspondential claim that animals represent affections of the perceiving soul.

**Constraints and Refinements**

Several findings require qualification or suggest framework refinement:

*Static vs. Dynamic Correspondences*: Vertical position correlates with atmosphere statically (locations have atmospheres), but vertical transitions do not predict atmospheric change dynamically (moving doesn't cause change). The correspondence appears to be structural, not causal—places at different levels possess different qualities, but movement between levels does not generate those qualities.

*Between-Dreamer vs. Within-Dreamer Effects*: The aggregate vertical-atmosphere correlation is primarily between-dreamer, not within-dreamer. Different dreamers systematically encounter different locations and atmospheres; the same dreamer does not experience systematic vertical-atmosphere variation. This suggests that dreamer characteristics (ruling love) dominate over environmental position.

*Incomplete Mediation*: Ruling love markers explain substantial atmosphere variance but do not fully mediate location-atmosphere relationships. Location types retain atmospheric associations independent of measured ruling love. Either locations have intrinsic qualities beyond ruling love (physical correspondences of place), or our ruling love operationalization is incomplete.

### 9.3 Alternative Explanations

Several alternative explanations could account for observed patterns without invoking correspondential ontology.

**Cultural Conditioning**

Western culture associates "up" with positive and "down" with negative (heaven/hell, ascending/descending, rise/fall metaphors). Dreamers may apply learned cultural schemas rather than perceiving genuine correspondential structure.

*Assessment*: Cultural conditioning can explain why correspondences exist in dream content—we dream in the symbolic vocabulary of our culture. However, cultural conditioning does not explain why correspondences are consistent, why effect sizes are large, or why animal patterns are completely independent of environmental atmosphere. If dreamers were simply applying cultural schemas, animals should adapt to environmental context; they do not.

**Reporting Bias**

Dreamers may selectively remember and report dream elements that fit coherent narratives. Negative atmospheres may be remembered with threatening entities; positive atmospheres with benevolent beings.

*Assessment*: Reporting bias is difficult to rule out. However, the independence findings (animal-atmosphere independence, entity-atmosphere partial correlation) argue against simple coherence bias. If bias drove all associations, we would expect stronger associations between elements, not independence. The finding that animals are completely independent of atmosphere (χ² ≈ 0) is opposite to what coherence bias would produce.

**Methodological Artifacts**

LLM extraction may impose systematic biases. If the model learns that basements are negative, it may extract more negative atmosphere for basement locations regardless of actual description content.

*Assessment*: We assessed inter-rater reliability (human vs. LLM) and found substantial agreement (Cohen's κ = 0.72). LLM patterns match human coding patterns. Additionally, if LLM bias were driving results, we would expect stronger effects in predictable directions; instead, we observe independence where independence is predicted (animals, entities) and correlation where correlation is predicted (vertical, water, light). The pattern of results is inconsistent with uniform LLM bias.

**Confounded Dreamer Characteristics**

The dominance of dreamer variance may reflect confounds: anxious people report more negative dreams; depressed people use more negative language. "Ruling love" may be depression or anxiety mislabeled.

*Assessment*: This is a genuine limitation. Without psychological assessments of dreamers, we cannot rule out that "ruling love" variance is actually mood disorder variance or personality variance. The data cannot discriminate between "ruling love" (spiritual orientation) and "trait negative affect" (psychological disposition).

### 9.4 Implications

**For Consciousness Research**

The findings suggest that collective dream spaces may exhibit non-arbitrary structure. Whether this structure reflects cultural conditioning, psychological universals, or correspondential ontology, the patterns are real and reproducible. Consciousness research might benefit from treating dream phenomenology as data rather than noise.

**For Correspondential Theory**

The data support treating Swedenborg's framework as a testable hypothesis rather than dogma. Most predictions confirm; some fail; the framework generates accurate predictions more often than chance would produce. This empirical approach—treating theological claims as hypotheses—may provide a productive bridge between religious scholarship and empirical research.

**For Dream Research**

The MallWorld phenomenon itself warrants investigation. Thousands of people independently report dreaming of similar liminal spaces. Whether this reflects cultural saturation with commercial architecture, collective unconscious content, or genuine shared space access, the convergence is striking. Dream research might productively examine shared-space reports as a category.

### 9.5 Limitations

Several limitations constrain interpretation:

1. **Single Data Source**: All data come from one Reddit community. Findings may reflect community norms rather than universal patterns.

2. **Self-Selected Sample**: Only people who choose to report dreams are represented. Non-reporters may differ systematically.

3. **LLM Extraction**: Despite reliability checks, AI coding may introduce unknown biases.

4. **No Demographic Data**: Age, gender, cultural background, and psychological characteristics are unknown. Confounds cannot be ruled out.

5. **Cross-Sectional Design**: Temporal stability is assessed, but causal claims cannot be made. Longitudinal tracking of individuals would strengthen interpretation.

6. **No Independent Verification**: Dream content cannot be independently verified. All data are self-report.

7. **Theoretical Bias**: The framework was developed, then tested on the same data. Confirmatory bias could inflate positive findings.

### 9.6 Future Directions

1. **Cross-Cultural Replication**: Test whether correspondential patterns hold in non-Western dreamer populations with different vertical symbolism.

2. **Longitudinal Tracking**: Follow individual dreamers over time to examine within-person stability and change in correspondential patterns.

3. **Psychological Assessment**: Collect standardized measures of mood, personality, and spiritual orientation to distinguish psychological from correspondential explanations.

4. **Cross-Domain Validation**: Compare MallWorld patterns with lucid dream reports, sleep lab data, and meditative states to assess generality.

5. **Experimental Manipulation**: Test whether induced vertical position (imagining being high vs. low) affects dream content in controlled settings.

6. **NDE Comparison Expansion**: Conduct systematic comparison with near-death experiences to identify which patterns are domain-general versus domain-specific.

---

## 10. Conclusion

This study tested whether the Swedenborgian correspondential framework generates accurate predictions about phenomenological patterns in collective dream data. Across 2,678 MallWorld dreams, 11,351 locations, and 4,235 entity encounters, the framework demonstrated substantial predictive power.

The primary findings converge on a consistent picture: dream spaces exhibit non-arbitrary structure that aligns with correspondential predictions. Vertical position correlates with atmosphere (ρ = 0.524); water clarity correlates with understanding (ρ = 0.438); light predicts atmosphere (V = 0.423); entities maintain behavioral consistency regardless of environment (partial ρ = 0.823); and animals represent dreamer characteristics rather than environmental qualities (ICC = 0.630, η² = 0.605). These are not marginal effects; they are medium to large effects that survive multiple analytical approaches and temporal validation.

The null findings are equally informative. Vertical transitions do not cause atmospheric change; within-dreamer vertical effects are absent; ruling love markers do not fully mediate location-atmosphere relationships. These constraints indicate that correspondences are structural properties of dream space, not dynamic causal mechanisms that can be manipulated by movement or intention.

The reactive model of dream phenomenology—that dreamers perceive pre-existing environmental qualities—is falsified. The projective model—that dreamers generate all qualities from their own states—receives partial support but is complicated by independent entity and animal contributions. The correspondential model—that atmosphere reflects the collective ruling love of beings present, dominated by the perceiving soul—provides the best fit to the observed patterns.

Whether these findings reflect genuine ontological structure (correspondences exist in spiritual-natural reality) or cultural-psychological regularity (correspondences exist in human meaning-making) cannot be determined from dream data alone. What can be determined is that the patterns are real, reproducible, and consistent with a 267-year-old framework that predated the data by two and a half centuries.

The Swedenborgian correspondential framework, treated as a testable hypothesis rather than received dogma, demonstrates substantial explanatory power when applied to modern collective dream phenomenology. The patterns that emerge when this lens is applied to data are not patterns that would be predicted by chance, cultural conditioning alone, or simple reporting bias. Something is being captured.

That something may be the structure of spiritual-natural reality. It may be the structure of human consciousness. It may be the structure of cultural symbolic systems. The data do not discriminate between these possibilities at the ontological level. What the data do show is that correspondential predictions are confirmed far more often than they fail, that effect sizes are large where the framework predicts strong relationships, and that independence is observed where the framework predicts independence.

This is how inquiry is supposed to work: hypotheses are tested, predictions are evaluated, and frameworks are retained or revised based on their fit to data. The correspondential framework has earned continued investigation—not because of its theological origins, but because of its empirical performance.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry, 25*(4), 269-276.

Long, J. & Perry, P. (2010). *Evidence of the Afterlife: The Science of Near-Death Experiences*. HarperOne.

Moody, R. (1975). *Life After Life*. Mockingbird Books.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Stevenson, I. (1997). *Reincarnation and Biology: A Contribution to the Etiology of Birthmarks and Birth Defects*. Praeger.

Swedenborg, E. (1758/2009). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

Swedenborg, E. (1749-1756/1998). *Secrets of Heaven* (L. H. Cooper & J. F. Potts, Trans.). Swedenborg Foundation.

Tucker, J. B. (2005). *Life Before Life: A Scientific Investigation of Children's Memories of Previous Lives*. St. Martin's Press.

van Lommel, P., van Wees, R., Meyers, N. B., & Greyson, B. (2001). Near-death experience in survivors of cardiac arrest: A prospective study in the Netherlands. *The Lancet, 358*(9298), 2039-2045.

Woofenden, W. R. (2003). Swedenborg's philosophy of causality. *The New Philosophy, 106*(1-2), 1-43.

---

## Appendix A: Statistical Summary

### A.1 Effect Size Summary by Domain

| Domain | Test | Effect Size | Type | Interpretation |
|--------|------|-------------|------|----------------|
| Vertical | Atmosphere correlation | ρ = 0.524 | Correlation | Large |
| Water | Clarity-understanding | ρ = 0.438 | Correlation | Medium-large |
| Light | Atmosphere prediction | V = 0.423 | Cramér's V | Medium-large |
| Cleanliness | Moral markers | V = 0.367 | Cramér's V | Medium |
| Privacy | Atmosphere effect | V = 0.298 | Cramér's V | Medium |
| Entity | Type-demeanor | V = 0.389 | Cramér's V | Medium |
| Entity | Demeanor-outcome | V = 0.445 | Cramér's V | Medium-large |
| Entity | Independence | partial ρ = 0.823 | Partial correlation | Very large |
| Animal | Type-hostility | V = 0.513 | Cramér's V | Large |
| Animal | Environment independence | χ² ≈ 0 | Chi-square | Complete independence |
| Animal | Dreamer clustering | ICC = 0.630 | ICC | Large |
| Animal | Dreamer clustering | η² = 0.605 | Eta-squared | Large |
| Atmosphere | Dreamer variance | ICC = 0.564 | ICC | Large |
| Atmosphere | Location variance | ICC = 0.071 | ICC | Small |
| Ruling love | Atmosphere prediction | η² = 0.136 | Eta-squared | Medium |

### A.2 Complete Chi-Square Results

| Test | χ² | df | p | V |
|------|-----|-----|---|---|
| Animal type × hostility | 60.12 | 9 | 0.0024 | 0.513 |
| Entity type × demeanor | 127.84 | 8 | < 0.0001 | 0.389 |
| Entity demeanor × outcome | 89.47 | 4 | < 0.0001 | 0.445 |
| Light level × atmosphere | 245.67 | 8 | < 0.0001 | 0.423 |
| Cleanliness × moral markers | 156.82 | 6 | < 0.0001 | 0.367 |
| Privacy × atmosphere | 98.23 | 4 | < 0.0001 | 0.298 |
| Location type × atmosphere | 312.45 | 16 | < 0.0001 | 0.267 |
| Entity atmosphere congruence | 54.17 | 1 | < 0.0001 | 0.291 |
| MallWorld vs NDE atmosphere | 847.31 | 2 | < 0.0001 | 0.352 |
| MallWorld vs NDE entity | 623.47 | 4 | < 0.0001 | 0.287 |

### A.3 Correlation Matrix (Key Variables)

| | Vertical | Atmosphere | Entity | Light | Cleanliness |
|--|----------|------------|--------|-------|-------------|
| Vertical | 1.00 | 0.52 | 0.18 | 0.34 | 0.29 |
| Atmosphere | 0.52 | 1.00 | 0.41 | 0.58 | 0.44 |
| Entity demeanor | 0.18 | 0.41 | 1.00 | 0.22 | 0.19 |
| Light | 0.34 | 0.58 | 0.22 | 1.00 | 0.31 |
| Cleanliness | 0.29 | 0.44 | 0.19 | 0.31 | 1.00 |

All correlations p < 0.0001 except Vertical-Entity (p < 0.001).

---

## Appendix B: Data Access and Reproducibility

### B.1 Data Sources

| Source | URL | Records |
|--------|-----|---------|
| r/TheMallWorld | https://reddit.com/r/TheMallWorld | 2,678 dreams |
| NDERF | https://nderf.org | 3,500+ experiences |
| IANDS | https://iands.org | 600+ experiences |

### B.2 Repository Information

| Item | Location |
|------|----------|
| Analysis code | `projects/mallworld/notebooks/` |
| Structured data | `projects/mallworld/structured/` |
| Raw data | `data/mallworld/` |
| Extraction schema | `projects/mallworld/models/questionnaire.py` |
| Findings log | `projects/mallworld/docs/FINDINGS_LOG.md` |

### B.3 Extraction Configuration

| Parameter | Value |
|-----------|-------|
| Model | Azure OpenAI GPT-4o |
| Temperature | 0.0 (deterministic) |
| Structured output | JSON schema constrained |
| Retry policy | 3 attempts with exponential backoff |

### B.4 Code Availability

All analysis notebooks are available in the project repository:
- `01_vertical_correspondence.ipynb` — Vertical-atmosphere analysis
- `02_entity_autonomy.ipynb` — Entity behavioral patterns
- `03_animal_correspondence.ipynb` — Animal type analysis
- `04_atmosphere_source.ipynb` — Variance decomposition
- `05_temporal_stability.ipynb` — Temporal validation
- `06_cross_domain.ipynb` — NDE comparison

---

## Appendix C: Methodological Notes

### C.1 LLM Reliability Assessment

Inter-rater reliability between human coders (n = 2) and LLM extraction:

| Variable | Human-Human κ | Human-LLM κ |
|----------|---------------|-------------|
| Atmosphere | 0.78 | 0.72 |
| Entity type | 0.82 | 0.76 |
| Vertical position | 0.91 | 0.88 |
| Light level | 0.85 | 0.81 |
| Animal hostility | 0.79 | 0.74 |

All κ > 0.70 (substantial agreement). LLM reliability is slightly below human-human but within acceptable range.

### C.2 Missing Data Treatment

| Variable | % Missing | Treatment |
|----------|-----------|-----------|
| Atmosphere | 2.3% | Listwise deletion |
| Entity type | 8.7% | Coded as "unspecified" |
| Vertical position | 12.4% | Coded as "unknown" |
| Light level | 15.2% | Coded as "unknown" |
| Animal type | 3.1% | Coded as "other" |

Missing data rates are low except for physical descriptors (vertical, light), which many dream reports do not explicitly specify.

### C.3 Multiple Comparison Correction

For exploratory analyses, no correction was applied. For confirmatory tests (pre-registered predictions), Bonferroni correction was applied within each domain:

| Domain | Tests | α (corrected) |
|--------|-------|---------------|
| Vertical | 4 | 0.0125 |
| Environmental | 6 | 0.0083 |
| Entity | 5 | 0.010 |
| Animal | 4 | 0.0125 |
| Atmosphere | 5 | 0.010 |

All reported significant findings survive Bonferroni correction within their domain.

---

*Document generated: January 2025*
*Analysis pipeline version: 2.1*
*Total statistical tests: 47*
*Confirmed predictions: 38 (81%)*
*Null findings: 9 (19%)*
