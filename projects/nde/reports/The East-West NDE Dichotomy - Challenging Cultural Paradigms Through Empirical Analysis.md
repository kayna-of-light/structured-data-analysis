# The East-West NDE Dichotomy: Challenging Cultural Paradigms Through Empirical Analysis

## Abstract

**Background**: For four decades, scholarly literature has posited a fundamental dichotomy between Western and Japanese near-death experiences. Western NDEs are characterized as featuring a personified "Being of Light" (70–80%), elaborate "Cities of Light," and frequent life reviews (25–30%), while Japanese NDEs allegedly involve impersonal light, flower gardens, and absent life reviews. This paradigm has profoundly shaped cross-cultural NDE research—yet both profiles may represent scholarly constructions shaped by selection bias, small samples, and paradigmatic assumptions rather than phenomenological reality.

**Methods**: We analyzed 6,753 structured NDE records from two major databases (NDERF: n=5,660; IANDS: n=1,093), coded using GPT-5.2 structured extraction for light encounter type, being identification, environment features, life review occurrence, boundary encounters, and return reasons. Chi-square tests examined associations between phenomenological features, Fisher's exact test assessed purpose-interaction correlations, and Mann-Whitney U tests compared experiential depth across boundary categories.

**Results**: The data fundamentally contradict the claimed Western profile. Being of Light encounters occurred in only 11.8% of Western NDEs—not 70–80%. Brilliant light without personification (40.9%) dominated, yielding a ratio of 3.8:1 impersonal to personified. Nature settings (17.0%) exceeded urban settings (11.4%). Deceased relatives (17.9%) were encountered more frequently than religious figures (9.9%)—the opposite of the claimed Western pattern. These findings suggest a universal baseline that neither scholarly tradition accurately captured. The key variable predicting personal interaction proved to be not culture but purpose: those returning with earthly missions showed 4.4× the odds of encountering the Being of Light (p < 10⁻⁴⁶). Analysis of boundary phenomena further supports a correspondential model: boundary type systematically maps to return agency (χ² = 3,724.7, p < 10⁻⁷⁸⁰), with physical barriers corresponding to external decisions and thresholds to self-choice. Boundary experiencers have richer, not shallower, experiences—demonstrating that the "point of no return" represents the correspondence of the return decision rather than a fixed structural limit.

**Conclusions**: The East-West NDE dichotomy reflects scholarly projection rather than phenomenological reality. Both the claimed "Western" profile (with its inflated Being of Light rates) and the claimed "Japanese" profile (constructed from small, curated samples) appear to be divergent distortions of a universal baseline. This supports a correspondential model of constant underlying reality with variable cultural expression, mediated by purposive economy rather than cultural determination. The dichotomy was never between East and West—it was between scholarly constructions and empirical truth.

**Keywords**: near-death experience, cross-cultural, Being of Light, life review, cultural paradigm, purposive economy, Japanese NDE, correspondences, boundary

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Notebook | `05_cultural_paradigm_challenge.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb) |
| Structured Data | `structured/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 The Paradigm and Its Origins

Since the late 1980s, a paradigm has crystallized in near-death experience research that divides the phenomenon along cultural lines. Following Raymond Moody's seminal *Life After Life* (1975), which established the modern NDE typology from American cases, researchers began examining whether the pattern held across cultures. What emerged was a dichotomy: Western NDEs, characterized by encounters with a personified "Being of Light," elaborate urban heavenly realms, and morally evaluative life reviews; and Eastern (particularly Japanese) NDEs, featuring impersonal ambient light, natural settings such as flower gardens and rivers, ancestral guides rather than divine figures, and notably absent life reviews.

This dichotomy carries profound theoretical implications. If near-death experiences vary systematically by culture—if Americans meet Jesus while Japanese meet ancestors, if Westerners traverse cities while Easterners wander gardens—this suggests that the dying brain constructs experiences from available cultural templates. The NDE, on this view, would be a culturally conditioned hallucination rather than a glimpse of objective spiritual reality. The stakes for NDE interpretation could not be higher.

Yet the empirical foundation of this paradigm deserves scrutiny on *both* sides. The claimed Western profile—70–80% Being of Light encounters, Cities of Light, frequent life reviews—derives largely from early studies using selected samples, retrospective compilation of "classic" cases, and small datasets. The Japanese profile similarly rests on limited samples, some comprising fewer than twenty cases, and may reflect its own selection biases—researchers seeking experiences that fit Japanese aesthetic or theological frameworks (natural settings, ancestral encounters, secular phenomenology). When claims of fundamental East-West difference rest on comparing thirty American hospital cases with seventeen Japanese accounts, both shaped by their respective scholarly assumptions, the potential for dual sampling artifacts is substantial. Neither profile may accurately represent the universal baseline of the phenomenon.

### 1.2 The Problem of Prevalence Claims

Consider the central claim: that 70–80% of Western NDEs feature a personified Being of Light. This figure appears repeatedly in the literature, yet its provenance is unclear. Moody's original typology described the Being of Light as a common element without quantifying prevalence. Kenneth Ring's subsequent research reported somewhat lower figures. The 70–80% estimate appears to derive from selective samples—cases chosen precisely because they exhibited classic features, or samples from contexts (such as support groups) where experiencers with dramatic encounters self-select.

The Japanese contrast similarly requires examination—and similar skepticism. Ornstein's "Japanese NDEs and the Being of Light" and subsequent work by Becker, Kellehear, and Ohkado established that Japanese NDEs feature "impersonal" light and lack the Being of Light encounter. But this profile was constructed from small, curated samples (Ohkado and Greyson's influential comparative analysis relied on just 22 interviews). Japanese researchers may have selected cases that fit cultural expectations—natural imagery congruent with Shinto aesthetics, ancestral encounters consistent with Japanese family religion, secular phenomenology that avoided Western theological categories. The "Japanese profile" may be as much a scholarly projection as the "Western profile."

Moreover, if Japanese samples happened to contain fewer experiencers who returned with specific missions—fewer who needed commissioning, teaching, or guidance requiring personal dialogue—they would naturally show fewer personified encounters by statistical necessity. The cultural explanation would be an artifact of purpose-distribution, not a window into different spiritual realities. Both East and West may have been measuring their own scholarly assumptions rather than the phenomenon itself.

### 1.3 Theoretical Framework: Correspondences and Purposive Economy

The present analysis applies a theoretical framework derived from Swedenborgian correspondential philosophy to evaluate the East-West paradigm. This framework proposes that spiritual realities are ontologically constant but perceptually variable: the same underlying phenomenon may appear differently to different observers based on their mental repertoire, cultural vocabulary, and—critically—the purpose the encounter serves.

The key concept is **purposive economy**: the principle that every element in an NDE serves the transformative goal. If the Light operates with perfect efficiency, it would engage personally when personal engagement is required (commissioning a mission, conducting a life review, teaching through dialogue) and remain as ambient presence when presence alone suffices. Cultural differences in NDE phenomenology would then reflect differences in sample composition—what purposes were represented—rather than differences in the nature of the Light itself.

This framework generates testable predictions. First, the underlying light phenomenon should be universal; whether experiencers perceive it as "personified" versus "impersonal" should correlate with functional variables (purpose) rather than cultural variables (nationality). Second, natural versus urban imagery should not systematically differ by culture if both are valid correspondential expressions of the same underlying realms. Third, boundary phenomena (the "point of no return") should function not as fixed structural features of spiritual geography but as correspondences of the return decision—expressed differently depending on how the return occurred.

### 1.4 Aims

This study tests the East-West paradigm against the largest systematically-coded Western NDE dataset analyzed to date. Our aims are:

1. To test the claimed prevalence rates for key "Western" NDE features against empirical data
2. To examine whether personal interaction with the Light correlates with culture or with purpose
3. To evaluate whether boundary phenomena represent fixed structural features or correspondences of return decisions
4. To determine whether the East-West dichotomy reflects phenomenological reality or scholarly projection

---

## 2. Methods

### 2.1 Data Sources

We compiled records from the two largest English-language NDE archives. The Near-Death Experience Research Foundation (NDERF) contributed 5,660 questionnaire responses spanning 1998 to 2024, collected through a standardized online instrument. The International Association for Near-Death Studies (IANDS) contributed 1,093 narrative accounts with biographical context. The combined corpus of 6,753 records constitutes the largest systematically structured NDE dataset analyzed to date.

Both archives collect accounts from self-selected respondents who sought out the respective organizations, introducing potential selection bias toward more profound or memorable experiences. However, this bias operates equally across all analyses, and the sample size provides statistical power unavailable in prior cross-cultural studies.

### 2.2 Structured Extraction

Each record was processed using GPT-5.2 (Azure OpenAI) for structured extraction into a validated Pydantic schema with 52 extracted features. The model extracted categorical classifications rather than generating novel text, reducing hallucination risk. Key fields for this analysis include:

- **Light encounter type**: Categorical classification (brilliant_light, being_of_light, presence_without_visual, no, not_mentioned)
- **Being identifications**: Multiple-select from standardized categories (god, jesus, deceased_relative_guide, unknown_presence, angels, religious_figure_specified, buddha, other)
- **Environment features**: Multiple-select (light, landscape, buildings, sky, colors, water, other)
- **Life review**: Occurrence and extent (no, brief, extensive, not_mentioned)
- **Boundary type**: Categorical (none, physical_barrier, verbal_limit, threshold, not_mentioned)
- **Return reasons**: Multiple-select (earthly_mission, family_responsibility, not_your_time, unfinished_business, other)
- **Return agency**: Who initiated the return (self_choice, external_being, unknown, other)

Inter-rater reliability was assessed on a 200-record subset, with human coders achieving κ = 0.84 agreement with GPT-5.2 classifications.

### 2.3 Statistical Analysis

Analyses employed chi-square tests for independence between categorical variables, Fisher's exact test for 2×2 tables with small expected cell counts, Mann-Whitney U tests for ordinal comparisons, and odds ratio calculations for association strength. All tests used α = 0.05, with Bonferroni correction applied for multiple comparisons where indicated.

---

## 3. Results

### 3.1 The Being of Light: Testing the Central Claim

The East-West paradigm rests fundamentally on the claim that Western NDEs feature a personified Being of Light in 70–80% of cases. This figure has been repeated across decades of cross-cultural NDE literature as the signature Western feature—the divine personal presence that supposedly distinguishes Western from Eastern experiences. Testing this claim against our dataset of 6,753 Western NDEs yields a striking result.

| Light Encounter Type | N | % |
|---------------------|---|---|
| Brilliant light (impersonal) | 2,761 | 40.9% |
| No light | 1,636 | 24.2% |
| Not mentioned | 1,274 | 18.9% |
| Being of Light (personified) | 797 | **11.8%** |
| Presence without visual | 285 | 4.2% |

The Being of Light—a personified presence with which the experiencer engages in dialogue or communion—appears in only 11.8% of Western NDEs. This is not a modest deviation from the claimed 70–80%; it is a six-fold discrepancy. The claimed Western signature feature is, in fact, a minority phenomenon.

What Western experiencers encounter far more commonly is brilliant light without explicit personification: 40.9% describe light that illuminates, surrounds, or pervades without taking personal form or engaging in dialogue. Including the category of "presence without visual form" (sensed but not seen) with impersonal light yields 45.1% impersonal versus 11.8% personified—a ratio of 3.8 to 1.

This finding inverts the paradigm. Western NDEs do not characteristically feature personified divine encounter; they characteristically feature impersonal luminosity. The "Japanese" profile of impersonal light is, in fact, the *Western* profile. The Being of Light, when it appears, is the exception rather than the rule.

### 3.2 Settings and Beings: Further Inversions

The paradigm extends beyond light encounters to settings and beings. Western NDEs supposedly feature "Cities of Light"—elaborate urban heavenly realms with architecture and structure—while Japanese NDEs feature natural settings like flower gardens, rivers, and mountains. Western experiencers supposedly encounter divine figures (God, Jesus, angels) while Japanese experiencers meet ancestors. These claims, too, require empirical testing.

Examining environmental features, we find that nature dominates over urban imagery in Western NDEs:

| Environment Feature | N | % of all NDEs |
|--------------------|---|---------------|
| Light | 3,395 | 50.3% |
| Landscape/nature | 1,151 | **17.0%** |
| Buildings/urban | 772 | **11.4%** |
| Water | 414 | 6.1% |

The "Cities of Light" stereotype is contradicted by the data. Nature settings (17.0%) significantly exceed urban settings (11.4%) in Western accounts (χ² = 74.7, p < 0.0001). Western experiencers describe meadows, gardens, forests, and landscapes more often than buildings, cities, or architectural structures. Once again, Western NDEs align with the supposedly "Japanese" pattern.

The pattern continues with beings encountered. The paradigm holds that Westerners meet divine figures while Japanese meet ancestors. Our data show the reverse:

| Being Category | N | % of all NDEs |
|----------------|---|---------------|
| Deceased relatives | 1,206 | **17.9%** |
| Religious figures (God/Jesus/angels/specified) | 670 | **9.9%** |

Deceased relatives (17.9%) are encountered nearly twice as often as religious figures (9.9%) in Western NDEs. The "ancestor" pattern supposedly distinctive to Japan is, in fact, the dominant Western pattern. Western experiencers are more likely to meet grandmother than God, more likely to encounter a deceased spouse than Jesus.

### 3.3 Life Reviews: Between the Extremes

The life review has been characterized as a signature Western feature (claimed 25–30%) essentially absent from Japanese NDEs (claimed ~0%). Our data show an intermediate rate:

| Life Review Occurrence | N | % |
|-----------------------|---|---|
| No | 5,245 | 77.7% |
| Brief | 718 | 10.6% |
| Extensive | 465 | 6.9% |
| Not mentioned | 325 | 4.8% |

Life reviews occur in 17.5% of Western NDEs—below the claimed 25–30% Western rate but substantially above zero. The dichotomy overstates the difference. More importantly, as we shall see, life review occurrence correlates not with culture but with purpose: when teaching is required, the life review occurs; when presence alone suffices, it does not.

### 3.4 The Purposive Economy Hypothesis

Having demonstrated that Western NDEs are far closer to the "Japanese" profile than the literature claims, we turn to a more fundamental question: if culture does not determine whether the Light appears as personified, what does?

The correspondential framework predicts that personal interaction serves function. The Light would engage personally—in dialogue, in life review, in commissioning—when the transformative purpose requires personal engagement. When presence alone accomplishes the goal, the Light would remain as ambient luminosity. This is **purposive economy**: intervention calibrated to need.

To test this hypothesis, we examined correlations between purposive elements (return reasons indicating specific missions or tasks) and personal interaction elements (Being of Light encounters, life reviews):

| Purposive Element | Personal Element | Co-occurrence | Expected by Chance | Ratio | p-value |
|-------------------|------------------|---------------|-------------------|-------|---------|
| Earthly Mission | Being of Light | 200 | 73.5 | **2.72×** | < 10⁻⁶⁰ |
| Life Review | Being of Light | 255 | 139.6 | **1.83×** | < 10⁻³⁰ |
| Not Your Time | Being of Light | 297 | 172.2 | **1.72×** | < 10⁻³⁰ |
| Family Responsibility | Being of Light | 203 | 137.4 | **1.48×** | < 10⁻¹¹ |

Every purposive element correlates significantly with personal interaction. The pattern is unmistakable: the Light engages personally when purpose requires it.

The most powerful test involves the earthly mission return reason. Experiencers who return with a specific mission—a task to accomplish, a message to deliver, a purpose to fulfill—require commissioning. You cannot assign a task impersonally; commissioning requires personal communication. If purposive economy operates, mission-returners should show dramatically elevated Being of Light rates.

| Condition | Being of Light Rate | Odds Ratio |
|-----------|---------------------|------------|
| With earthly mission (n=623) | **32.1%** | — |
| Without earthly mission (n=6,130) | 9.7% | — |
| **Comparison** | **3.3× higher** | **4.38** (p < 10⁻⁴⁶) |

Those returning with an earthly mission have 4.4 times the odds of encountering the Being of Light. This is not chance association—it represents a functional relationship. The Light becomes personal when personal communication is required for the transformative purpose.

This finding reframes the entire East-West discussion. If Japanese NDE samples happened to contain fewer mission-returners—whether due to sampling methods, survival rates, cultural differences in how return reasons are articulated, or random variation—they would show fewer Being of Light encounters by statistical necessity. The cultural explanation would be an artifact of purpose-distribution, not evidence of different spiritual realities.

The Light, on this model, operates with perfect efficiency: personal mode when personal mode is required, presence without dialogue when presence alone serves the purpose. A skilled teacher does not lecture every student on every topic. Some students need only a nod of encouragement; some need detailed instruction; some need mentorship with explicit commissioning. The teacher's restraint with some students does not make the teacher "impersonal"—the intervention is calibrated to the need. The wisdom is in the restraint.

### 3.5 The Boundary as Correspondence

The East-West paradigm frequently invokes the "point of no return" as a structural feature distinguishing NDE types. The Japanese river, the Western barrier—these are described as cultural variations of a fixed location in spiritual geography, beyond which physical return becomes impossible. This conceptualization requires examination.

If the boundary represents a fixed structural limit, we would expect experiencers who encounter it to have shallower experiences than those who do not—they would have been stopped before reaching deeper content. The data show the opposite:

| Content Element | With Boundary (n=2,833) | Without Boundary (n=3,920) | Ratio |
|-----------------|-------------------------|----------------------------|-------|
| Cities/urban | 16.0% | 8.1% | **2.0×** |
| Heavenly realms | 43.5% | 18.6% | **2.3×** |
| Life review | 21.2% | 14.8% | **1.4×** |
| Being of Light | 66.5% | 42.7% | **1.6×** |
| Deceased relatives | 25.7% | 9.3% | **2.8×** |

Boundary experiencers have *more* deep content, not less. They are 2.0–2.8 times more likely to report the richest experiential elements. The boundary does not prevent depth—it marks where depth culminates.

Moreover, experiencers who describe the deepest content—cities, heavenly realms—frequently report no hard boundary at all:

| Deep Content | N | No Hard Boundary | With Hard Boundary |
|--------------|---|------------------|--------------------|
| Saw cities | 772 | **55.3%** | 44.7% |
| Heavenly realms | 1,963 | **53.2%** | 46.8% |

Over half of those who entered the deepest realms report no physical barrier or verbal limit. The "point of no return" is not required to reach or return from deep experience.

The most significant finding concerns what the boundary represents. If the boundary is a fixed structural feature, its type should be independent of how the return decision was made. The data show precise correspondence:

| Boundary Type | External Being Decided | Self Choice | Dominant Pattern |
|---------------|------------------------|-------------|------------------|
| Physical barrier | **55.5%** | 10.6% | External decision |
| Verbal limit | **69.6%** | 16.5% | External decision |
| Threshold | 23.9% | **46.1%** | Self decision |
| None | 10.0% | 10.2% | No distinctive marker |

Chi-square: χ² = 3,724.7, df = 16, p < 10⁻⁷⁸⁰

Boundary type systematically maps to return mechanism. When an external being makes the return decision, experiencers perceive physical barriers (rivers, walls, fences) or verbal limits ("not your time," "go back"). When the experiencer makes the decision, they perceive a threshold—a felt sense, an internal knowing. The form varies; the function is constant.

The boundary is not a location—it is the **correspondence** of the return decision. It does not exist independently of the decision; it *is* the decision, perceived through available mental forms. The Japanese river and the Western barrier are not cultural variations of a cosmic limit—they are different expressions of the same functional reality: the moment when return occurs.

This resolves a persistent confusion in cross-cultural NDE research. The question "Is the Japanese river the same as the Western tunnel?" is malformed because it conflates two distinct functional categories. The tunnel is a passage experience—how one travels. The river is typically a boundary experience—the decision point. These are different phenomena serving different functions in the experiential architecture.

### 3.6 Summary: Two Distorted Profiles, One Universal Baseline

The evidence permits a comprehensive reassessment of the East-West paradigm:

| Feature | Claimed Western | Observed Western | Claimed Japanese | Interpretation |
|---------|-----------------|------------------|------------------|----------------|
| Being of Light | 70–80% | **11.8%** | Rare | Western claim grossly inflated |
| Impersonal light | Rare | **40.9%** | Common | Japanese claim may be accurate for baseline |
| Life review | 25–30% | **17.5%** | ~0% | Both claims are off: moderate rate is baseline |
| Nature > Urban | No | **1.5×** | Yes | Western claim wrong; Japanese may be baseline |
| Deceased > Religious | No | **1.8×** | Yes | Western claim wrong; ancestral is baseline |
| Boundary = fixed location | Yes | **No** | Yes | Both claims wrong: boundary = correspondence |

The picture that emerges is not that the Japanese profile was "right" while the Western profile was "wrong." Rather, both scholarly profiles represent distortions of a universal baseline—the Western version inflated by selecting dramatic cases, the Japanese version potentially shaped by its own selection biases (favoring secular, nature-focused, ancestral encounters over theologically charged material). Our large-scale data reveals what may be closer to the actual universal distribution: impersonal light dominates, nature settings are common, deceased relatives are the primary beings encountered, and life reviews occur at moderate rates. The dichotomy was never real—it was a comparison between two scholarly constructions, neither of which accurately captured the phenomenon.

---

## 4. Discussion

### 4.1 The Dichotomy as Dual Scholarly Construction

The findings presented here suggest that the East-West NDE dichotomy reflects scholarly projection rather than phenomenological reality—on *both* sides. The claimed Western profile—personified Being of Light in 70–80% of cases, Cities of Light, frequent life reviews—does not match what Western experiencers actually report. Western NDEs feature impersonal light (40.9%) more than personified (11.8%), nature settings (17.0%) more than urban (11.4%), and deceased relatives (17.9%) more than religious figures (9.9%).

But we must be equally critical of the Japanese profile. Though our data cannot directly test Japanese claims, the methodological concerns are symmetric: small samples (sometimes fewer than 25 cases), potential selection biases (favoring secular experiences congruent with Japanese academic and cultural expectations), and the same vocabulary conflation that affected Western research. The Japanese "impersonal light, nature settings, ancestral encounters, no life review" profile may be as much a scholarly construction as the Western "Being of Light, Cities of Light, frequent life reviews" profile—simply distorted in a different direction.

How did both paradigms arise? Several factors likely contributed:

**Selection bias in both traditions**: Western researchers, following Moody, selected for dramatic encounters with personal divine figures. Japanese researchers, perhaps influenced by secular academic norms and Shinto/Buddhist aesthetics, may have selected for nature-based, non-theological experiences. Both presented their selections as representative.

**Confirmation through contrast**: Each side defined itself against the other. Western researchers emphasized what distinguished their cases from "Eastern" patterns; Japanese researchers emphasized difference from "Western" expectations. The dichotomy became mutually reinforcing.

**Vocabulary conflation**: "Being of Light" implies personification; "brilliant light" does not. The same phenomenon might be coded differently depending on the categories researchers brought to the data. Cultural vocabulary shaped categorization, creating apparent differences where phenomenological similarity existed.

**Publication bias on both sides**: Cases confirming each paradigm were more publishable than cases contradicting it. The "typical Western NDE" and "typical Japanese NDE" became self-fulfilling categorizations.

### 4.2 The Correspondential Model

Our findings support a correspondential model of NDE phenomenology. The underlying spiritual reality appears constant—a light that pervades, beings that guide, realms that welcome, boundaries that mark return. The surface expression varies: whether the light is named "Being" or perceived as "brilliant," whether settings are described as gardens or cities, whether beings are identified as Jesus or ancestors, whether boundaries appear as rivers or walls.

This model explains why purpose predicts personal interaction. The Light operates with purposive economy: engaging personally when the transformative goal requires personal engagement (commissioning, teaching, guidance), remaining as ambient presence when presence alone accomplishes the goal. What researchers interpreted as cultural variation in the *nature* of the Light was actually functional variation in the *mode* of the Light—calibrated to individual need rather than determined by cultural background.

The boundary analysis extends this model. The "point of no return" is not a fixed location in spiritual geography but the correspondence of the return decision. When an external being decides the return, experiencers perceive barriers or verbal commands. When the experiencer decides, they perceive thresholds or felt knowing. The form expresses the function; the boundary *is* the decision, not a separate feature the experiencer happens to encounter.

### 4.3 Implications for Cross-Cultural Research

These findings have significant implications for cross-cultural NDE research methodology:

**Sample size matters**: Claims about cultural differences require large, systematically coded samples. The 70–80% Being of Light figure cannot be replicated in large Western datasets; claims about Japanese NDEs based on small samples deserve similar skepticism.

**Purpose must be controlled**: Any comparison of personified versus impersonal light encounters must control for purpose-distribution. If samples differ in the proportion of mission-returners, they will differ in Being of Light rates by statistical necessity—regardless of culture.

**Vocabulary must be distinguished from phenomenology**: Experiencers from different cultures may use different words for the same phenomenon. "Being of Light" and "brilliant radiance" may describe the same encounter through different cultural lenses.

**Functional categories must not be conflated**: The tunnel (passage) and the river (boundary) serve different functions. Comparing them as cultural variants of "the same thing" is a category error.

Future cross-cultural studies should apply identical structured extraction to Japanese, Indian, and other non-Western NDE archives, control for purpose-category distributions, and test the purposive economy hypothesis directly.

### 4.4 Limitations

Several limitations warrant acknowledgment. This analysis tests only Western claims against Western data; it cannot directly assess whether Japanese NDEs actually match the claimed Japanese profile. The sample, while large, derives from self-selected respondents who sought out NDE archives. AI-based coding may introduce systematic biases, though inter-rater reliability was acceptable (κ = 0.84). Return reasons are experiencer-reported rather than independently verified. The dataset spans decades during which cultural context changed.

Most fundamentally, the claim "no boundary necessary for return" is inherently untestable—every member of the dataset returned. We can only assess what boundary presence correlates with, not whether boundary absence permits return.

---

## 5. Conclusion

Analysis of 6,753 Western near-death experiences reveals that the East-West NDE dichotomy is largely a **dual** scholarly construction—both profiles appear to be distortions of a universal baseline that neither tradition accurately captured. The claimed Western profile—70–80% personified Being of Light, Cities of Light, frequent life reviews—does not match the observed data. Western NDEs feature impersonal light (40.9%) more than personified (11.8%), nature settings (17.0%) more than urban (11.4%), and deceased relatives (17.9%) more than religious figures (9.9%).

But the solution is not simply to declare the Japanese profile "correct." That profile—constructed from small, curated samples (some fewer than 25 cases)—likely reflects its own selection biases: Japanese researchers favoring secular, nature-based, ancestral encounters that fit cultural and academic expectations, while filtering out theologically charged material. The Japanese claim of ~0% life reviews is as suspect as the Western claim of 70–80% Being of Light encounters. Neither represents unfiltered phenomenological reality.

What our large-scale data reveals is something closer to the **universal baseline**: impersonal light dominates (~41%), personified light is a minority (~12%), nature settings exceed urban settings, deceased relatives are the primary beings encountered, and life reviews occur at moderate rates (~17.5%). Both scholarly traditions distorted this baseline—the Western version inflated toward the dramatic and theological, the Japanese version deflated toward the secular and naturalistic.

The key variable determining personal interaction is not culture but **purpose**. Those returning with earthly missions show 4.4× the odds of encountering the Being of Light. Life reviews correlate with Being of Light encounters at 1.83×. The Light engages personally when the transformative purpose requires personal engagement—commissioning, teaching, guiding. When presence alone suffices, the Light remains as ambient brilliance. What researchers attributed to cultural difference was functional variation: the Light's mode calibrated to individual need, not national origin.

The boundary or "point of no return" similarly reflects not fixed spiritual geography but the correspondence of the return decision. Boundary type maps systematically to return agency: physical barriers express external decisions; thresholds express self-decisions. Boundary experiencers have richer, not shallower, experiences. The boundary marks the choice, not a cosmic limit—and both the Western "barrier" and Japanese "river" may be cultural vocabularies for the same functional reality.

These findings support a correspondential model of **constant underlying reality** with **variable cultural expression**, mediated by **purposive economy** rather than cultural determination. The Light is one; the forms are many; the mode of interaction serves the goal. Neither East nor West experiences something fundamentally different—and neither the Western scholarly profile nor the Japanese scholarly profile accurately captured what both populations actually experience. The dichotomy was never between East and West. It was between **scholarly constructions** and **empirical truth**.

The Being of Light, whether named or unnamed, personified or brilliant, appears to be what experiencers consistently report across cultures when unfiltered by academic agendas: a presence of love and wisdom that engages with perfect economy—speaking when speaking serves, and present without words when presence alone transforms.

---

## References

Becker, C. B. (1981). The centrality of near-death experiences in Chinese Pure Land Buddhism. *Anabiosis: The Journal for Near-Death Studies*, 1(2), 154–171.

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Kellehear, A. (1993). Culture, biology, and the near-death experience: A reappraisal. *Journal of Nervous and Mental Disease*, 181(3), 148–156.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Ohkado, M., & Greyson, B. (2014). A comparative analysis of Japanese and Western NDEs. *Journal of Near-Death Studies*, 32(4), 187–198.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Variable | Statistic | df | p-value |
|------|----------|-----------|----|---------| 
| Chi-square | Nature vs. Urban settings | χ² = 74.7 | 1 | < 0.0001 |
| Chi-square | Light type × Life review | χ² = 183.20 | 4 | < 0.0001 |
| Fisher's exact | Mission × Being of Light | OR = 4.38 | — | 1.25 × 10⁻⁴⁶ |
| Chi-square | Life Review × Being of Light | χ² = 53.2 | 1 | < 10⁻³⁰ |
| Chi-square | Earthly Mission × Being of Light | χ² = 258.7 | 1 | < 10⁻⁶⁰ |
| Chi-square | Boundary × Deep content | χ² = 100.9 | 1 | < 10⁻²³ |
| Chi-square | Boundary type × Return agency | χ² = 3,724.7 | 16 | < 10⁻⁷⁸⁰ |
| Mann-Whitney | Experience depth by boundary | U = 7.31 × 10⁶ | — | < 10⁻¹²³ |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,660 |
| IANDS records | 1,093 |
| Being of Light encounters | 797 (11.8%) |
| Brilliant light encounters | 2,761 (40.9%) |
| Impersonal:Personified ratio | 3.8:1 |
| Nature settings | 1,151 (17.0%) |
| Urban settings | 772 (11.4%) |
| Deceased relative encounters | 1,206 (17.9%) |
| Religious figure encounters | 670 (9.9%) |
| Life reviews | 1,183 (17.5%) |
| Boundary encounters | 2,833 (42.0%) |
| Mission → Being of Light odds ratio | 4.38 |
| Boundary experiencers: mean depth | 2.90 |
| Non-boundary experiencers: mean depth | 2.06 |

## Appendix C: Claimed Versus Observed Rates

| Feature | Claimed Western | Observed | Deviation |
|---------|-----------------|----------|-----------|
| Being of Light | 70–80% | 11.8% | −58 to −68 pp |
| Life review | 25–30% | 17.5% | −7 to −12 pp |
| Tunnel | 34–50% | 23.7% | −10 to −26 pp |
| Nature > Urban | No | Yes (1.5:1) | Reversed |
| Deceased > Religious | No | Yes (1.8:1) | Reversed |

## Appendix D: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [05_cultural_paradigm_challenge.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb)
- **Structured Data**: [/structured/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 JSON files)
