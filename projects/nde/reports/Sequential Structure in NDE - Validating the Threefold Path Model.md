# Sequential Structure in Near-Death Experience: Validating the Normative Path Model

## Abstract

Near-death experiences are often described as following a characteristic sequence—passage through darkness or tunnel, arrival in a realm of light, encounter with beings, life review, and return decision. Whether this sequence reflects a genuine structural pattern or post-hoc narrative reconstruction remains debated. The Swedenborgian framework proposes a specific normative path: most souls continue to permanent spiritual existence, with reincarnation representing an exceptional rather than universal pattern.

We analyzed 6,753 NDE records from NDERF (n=5,664) and IANDS (n=1,089) coded for return patterns, being encounters, life review characteristics, and transformation markers using GPT-5.2 structured extraction with a Pydantic schema containing 52 extracted features.

Among experiencers with willingness data, 49.4% were reluctant to return—suggesting the spiritual realm is genuinely preferable to earthly existence. Deceased relatives were encountered in 17.9% of cases, a finding with significant implications: if reincarnation were normative, these relatives would not be available for encounters. Reincarnation indicators proved rare across the corpus—past life memory 4.4%, intermission memory 1.0%, pre-incarnation covenant 1.3%—consistent with reincarnation as exception rather than rule. Life review occurred in 17.5% of cases with loving judgment vastly exceeding harsh judgment (15.9:1 ratio).

Four markers support the Normative Path Hypothesis: experiencer reluctance to leave the spiritual realm, deceased relatives present and recognizable, rare reincarnation indicators, and preserved identity throughout the experience. The data support a model in which continuation is normative and reincarnation is exceptional.

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,664) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,089) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `02_normative_path_validation.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb) |
| Structured Data | `analysis/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/analysis/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

Near-death experiences consistently feature recognizable elements: out-of-body experiences, tunnel passage, light encounters, meetings with deceased relatives, life reviews, and return decisions. Raymond Moody's pioneering research identified these core features (Moody, 1975), and subsequent studies by Kenneth Ring, Bruce Greyson, and others have confirmed their prevalence while documenting substantial individual variation (Ring, 1980; Greyson, 2003).

Ring's original work identified five stages: peace, body separation, entering darkness, seeing light, and entering light. This sequential structure raises fundamental questions about the nature of the experience. Is the structure inherent to the phenomenon—a genuine feature of post-mortem existence briefly glimpsed—or is it imposed through narrative reconstruction after the fact? Cultural expectations might shape how experiencers organize and report their memories; alternatively, the consistency of structure across cultures might indicate something objective about the territory traversed.

### 1.2 Theoretical Framework

Emanuel Swedenborg's eighteenth-century accounts of the spiritual world describe a post-mortem journey with distinctive stages (Swedenborg, 1758). According to Swedenborg, the newly deceased first enter a transitional realm he called the "World of Spirits"—an intermediate zone resembling earthly life where individuals undergo a process of self-revelation and instruction. This process unfolds in stages: first an external stage where the person appears much as they did in earthly life; then an internal stage where true character is progressively revealed; and finally an instruction stage preparing for permanent placement. The process culminates in individuals gravitating toward communities that match their "ruling love"—their fundamental orientation either toward self or toward the neighbor.

Critically, Swedenborg's framework proposes that continuation is normative. Most souls proceed to permanent spiritual existence rather than returning to physical embodiment. Reincarnation, when it occurs, represents an exception serving specific purposes—restorative healing from traumatic death, or volunteer mission requiring physical presence. This contrasts sharply with frameworks in which reincarnation is universal and cyclical.

This generates testable predictions about NDE phenomenology. If the spiritual realm is genuinely preferable to earthly existence, experiencers who glimpse it should be reluctant to leave. If continuation rather than reincarnation is the norm, deceased relatives should be available for encounters—they haven't reincarnated into new bodies and lost their recognizable identity. And explicit reincarnation indicators (past-life memories, pre-incarnation covenants) should be uncommon rather than widespread.

A clarification is essential here: NDE return—going back to one's current physical life—is entirely distinct from reincarnation—incarnating into a new life. The predictions above concern evidence about what happens to souls who complete their transition, not about the mechanism by which NDErs return to their bodies. The presence of deceased relatives, for instance, provides evidence about their post-mortem state (continuation), not about NDE return mechanics.

### 1.3 Aims

This analysis tests whether NDE phenomenology supports continuation as the normative path. Specifically, we examine return willingness (do experiencers want to stay?), deceased relative presence (are they available for encounters?), reincarnation indicator prevalence (how common are past-life memories and pre-birth covenants?), identity preservation (does personal identity persist?), and life review characteristics (what is the quality of any judgment experienced?).

---

## 2. Methods

### 2.1 Data Sources

Records were collected from two major NDE archives: the Near-Death Experience Research Foundation (NDERF), contributing 5,664 records, and the International Association for Near-Death Studies (IANDS), contributing 1,089 records. The combined corpus of 6,753 records enables robust statistical analysis while spanning diverse experiencer demographics and NDE contexts.

### 2.2 Return Pattern Extraction

The coding schema separates two dimensions of the return experience that are often conflated: return agency (who decided the return) and return willingness (how the experiencer felt about it). This distinction proves crucial because knowing that a being sent someone back tells us nothing about whether they wanted to return, and knowing someone was reluctant tells us nothing about who made the decision.

Return agency was coded as: self (experiencer chose), external_being (a being decided), involuntary (return happened without decision), mutual (negotiated), or not_mentioned. Return willingness was coded as: willing, reluctant, mixed, neutral, or not_mentioned. This separation enables analyses impossible with simpler coding schemes.

### 2.3 Key Field Definitions

Return pattern fields capture who decided return, how the experiencer felt about it, and stated reasons for return (family responsibility, not your time, earthly mission, unfinished business, or other). Continuation evidence fields capture whether deceased relatives were encountered and any indicators of prior incarnations: past life memory, intermission memory (between-lives awareness), pre-incarnation covenant, and incarnation choices (chose parents, mission, or life circumstances). Life review fields capture whether review occurred (and whether brief or extensive), the source of any judgment (self, being of light, guide, or none), and judgment intensity (loving/gentle through harsh/condemning).

### 2.4 Statistical Analysis

Analysis employed frequency calculations for categorical distributions, chi-square tests for independence between variables of interest, and cross-tabulation for multi-dimensional pattern analysis. The primary focus is descriptive—establishing what patterns exist in the data—with statistical tests used to assess whether observed associations exceed chance expectation.

---

## 3. Results

### 3.1 Return Agency

Among the 4,782 cases with return agency data, the distribution reveals that self-initiated return was uncommon. External being accounted for 28.6% (n=1,931), involuntary return for 21.1% (n=1,422), self-initiated for 16.6% (n=1,124), mutual for 4.5% (n=305), and not mentioned for 29.2% (n=1,971).

Combining external being and involuntary categories, 70.1% of experiencers did not return by their own choice. This finding describes the NDE return mechanism but does not directly test the continuation hypothesis—as noted, NDE return (resuming one's current life) is distinct from reincarnation (new incarnation). The finding does suggest that return to physical life is experienced as external imposition rather than personal preference, consistent with the spiritual realm being preferable.

### 3.2 Return Willingness

Among the 3,563 cases with willingness data, reluctance predominated. Reluctant experiencers constituted 26.0% (n=1,759) of the total sample and 49.4% of those with willingness data. Mixed feelings appeared in 14.0% (n=944), willing return in 11.3% (n=763), and neutral in 1.4% (n=97). The remaining 47.2% (n=3,190) did not mention willingness.

Nearly half of experiencers with relevant data preferred to remain in the spiritual state rather than return to physical life. This finding carries significant weight for the continuation hypothesis: if the NDE state represented mere hallucination or oxygen-deprivation artifact, we would not expect such consistent preference for remaining in it. The reluctance suggests experiencers perceive themselves as having encountered something genuinely preferable to ordinary waking consciousness—a glimpse of a realm they recognize as more real, more meaningful, or more aligned with their deepest nature than physical existence.

### 3.3 Agency and Willingness Cross-Tabulation

Cross-tabulating agency and willingness reveals that these dimensions, while correlated, capture distinct aspects of the experience (χ² = 4824.78, p < 0.0001). Among those sent back by external beings, 52.1% were reluctant and only 4.2% were willing—they did not want to return and were sent back anyway. Among those who chose to return themselves, 49.6% were willing and only 9.7% were reluctant—choosing to return generally aligned with wanting to return. Mutual decisions showed the most mixed pattern: 36.4% mixed feelings, 30.2% willing, and 28.5% reluctant.

The external-being/reluctant combination (sent back against one's preference) represents the modal NDE return pattern. This aligns with experiencer testimony: many report being told they must return despite their desire to stay, often for reasons related to unfinished earthly responsibilities or missions.

### 3.4 Return Reasons

Among cases with explicit return reasons, the distribution reveals that duty and obligation rather than preference drive return. "Not your time" was most common (1,459 mentions), followed by family responsibility (1,164), unfinished business (711), earthly mission (623), and other reasons (218). These reasons are not mutually exclusive; experiencers often report multiple reasons.

The prevalence of obligation-based reasons reinforces the willingness findings: experiencers return because they must, not because they want to. They are told their time hasn't come, reminded of family needing them, or commissioned with missions requiring physical presence. The rare experiencer who genuinely prefers to return stands out precisely because the pattern is so consistently otherwise.

### 3.5 Deceased Relatives: Evidence of Continuation

The presence of deceased relatives in NDEs carries particular significance for the continuation hypothesis. If reincarnation were normative—if most souls cycled rapidly through new incarnations—deceased relatives would rarely be available for encounters. They would have already reincarnated, losing their recognizable identity and relationship with the experiencer. The consistent presence of deceased relatives in NDEs suggests something different: that identity and relationships persist.

Among the 6,753 NDEs, 14.9% (n=1,007) reported named deceased relatives and an additional 2.9% (n=199) reported unnamed relatives—17.9% total. These relatives were recognized and identified; they had not lost their identity through dissolution or reincarnation. The theological implication is substantial: these individuals continued rather than reincarnated. Their presence supports the model in which continuation is normative.

### 3.6 Reincarnation Indicators

If continuation is normative and reincarnation exceptional, explicit reincarnation indicators should be rare in the general NDE population. The data strongly support this prediction.

Past life memory appeared in only 4.4% (n=297) of NDEs. Intermission memory (awareness of between-lives existence) appeared in only 1.0% (n=69). Pre-incarnation covenant (evidence of pre-birth life choice) appeared in 1.3% (n=86). More specific incarnation choices were rarer still: chose parents 0.1% (n=9), chose mission 1.4% (n=93), chose life circumstances 0.7% (n=47).

All reincarnation indicators fall below 5%, with most below 2%. This pattern is consistent with reincarnation representing an exception rather than the norm. The vast majority of experiencers show no evidence of prior incarnations or pre-birth planning. When such indicators do appear, they may represent the exception paths theorized in the Swedenborgian framework: restorative incarnation following traumatic death, or volunteer soul incarnation for specific missions.

### 3.7 Identity Preservation

The persistence of personal identity during NDEs provides additional evidence for the continuation model. Among the corpus, 64.8% (n=4,377) reported clear identity preserved—they remained themselves throughout the experience. Only 1.4% (n=92) reported identity altered or lost, and 0.6% (n=43) reported identity confusion. The remaining 33.2% (n=2,241) did not address identity.

Identity disruption is rare—only 2.0% report any form of it. Experiencers overwhelmingly maintain their sense of self: their memories, personality, relationships, and individual perspective persist through the transition out of physical embodiment. This argues against models in which death dissolves personal identity into cosmic consciousness or undifferentiated being. The continuation model predicts exactly this: individual identity persists beyond physical death.

### 3.8 Life Review

Life review occurred in 17.5% of NDEs: 10.6% (n=718) reported brief review and 6.9% (n=465) reported extensive review. When life review occurred, the source of any judgment varied: no judgment 22.5% (n=1,518), guide or entity 3.0% (n=205), Being of Light 2.3% (n=155), self 1.4% (n=95), deceased relative 0.1% (n=7). The majority (70.7%, n=4,773) did not mention judgment source.

The intensity of judgment proves most striking. Among those with intensity data, loving/gentle judgment appeared in 3.3% (n=223) while harsh/condemning judgment appeared in only 0.2% (n=14)—a ratio of 15.9:1 in favor of love. Neutral judgment appeared in 1.3% (n=89), uncomfortable in 1.9% (n=128). The overwhelming majority reported either no judgment or loving judgment.

This pattern aligns closely with Swedenborg's account of the World of Spirits: the intermediate state reveals rather than condemns. Individuals are shown their true character without external punishment. The life review functions as mirror rather than tribunal—enabling self-knowledge rather than imposing sentence. The near-total absence of harsh judgment challenges many religious expectations while confirming the non-judgmental character described by NDErs across traditions.

### 3.9 Empathetic Perspective

A distinctive feature of some life reviews is empathetic perspective-taking—experiencing one's actions from the viewpoint of those affected. Among the corpus, 2.9% (n=198) explicitly reported feeling others' emotions during life review, with an additional 0.9% (n=61) implying such experience. While not common, this empathetic dimension transforms life review from mere memory replay to moral education. Experiencers report feeling the joy they caused and the pain they inflicted, understanding the full impact of their choices in a way impossible during physical life.

---

## 4. Discussion

### 4.1 Evidence for the Normative Path

Four markers support the Normative Path Hypothesis, each representing a testable prediction from the theoretical framework.

First, experiencers are reluctant to leave the spiritual realm. Among those with willingness data, 49.4% were reluctant to return. If the NDE state were mere hallucination or physiological artifact, such consistent preference for remaining in it would be puzzling. The reluctance suggests experiencers recognize the spiritual realm as genuinely preferable—more real, more meaningful, more aligned with their deepest nature—than ordinary waking consciousness.

Second, deceased relatives are present and recognizable. In 17.9% of NDEs, experiencers encountered deceased family members who had maintained their identity and relationships. If reincarnation were normative, these relatives would have already moved to new incarnations, losing their recognizable form. Their consistent presence suggests continuation rather than reincarnation is the normal post-mortem path.

Third, reincarnation indicators are rare. Past life memory appears in only 4.4% of cases, pre-incarnation covenants in 1.3%. The vast majority of experiencers show no evidence of prior incarnations. This is consistent with reincarnation representing an exception rather than the rule—perhaps reserved for specific purposes like trauma healing or mission accomplishment.

Fourth, personal identity persists. In 64.8% of cases, experiencers report clear preservation of identity throughout the NDE. Identity disruption is rare (2.0%). This argues against models in which death dissolves personal identity, supporting instead a continuation model in which the individual self persists beyond physical embodiment.

### 4.2 The Threefold Path Framework

Integrating these findings with the theoretical framework suggests a threefold path structure.

The normative linear progression represents the default path. The vast majority—those with no past life memory (95.6%), no pre-incarnation covenant (98.7%), no reincarnation indicators of any kind—appear to be on their first and only earthly journey. They will continue to spiritual existence without returning to physical embodiment. This aligns with Swedenborg's primary account of post-mortem existence.

Restorative incarnation represents one exception path. The 4.4% with past life memory and 1.0% with intermission memory may represent souls who returned to physical life for healing purposes—often following traumatic or violent death that disrupted normal spiritual development. The DOPS research corpus (University of Virginia) provides independent evidence for this pattern: verified past-life memories cluster heavily around violent death in the previous incarnation.

Volunteer soul incarnation represents another exception path. The 1.3% reporting pre-incarnation covenants and 1.4% reporting mission choice may represent souls who accepted specific missions requiring physical presence. These are not compelled returns but chosen ones—volunteers accepting incarnation for service purposes.

### 4.3 The World of Spirits as Transition Zone

NDE phenomenology closely matches Swedenborg's description of the World of Spirits. Multiple points of correspondence emerge from the data.

The intermediate realm character appears in the encounter structure: experiencers meet beings, encounter deceased relatives, and exist in a transitional zone between physical and permanent spiritual existence. The self-revelation process appears in life review: 17.5% undergo review that reveals their character without external punishment, with judgment overwhelmingly loving (15.9:1 ratio). The instruction period appears in the communication and guidance commonly reported. Identity preservation matches Swedenborg's account that individuals maintain their personality and memory in the spiritual world. And the availability of deceased relatives for encounter suggests they have continued rather than reincarnated.

The non-judgmental character of life review deserves particular emphasis. Many religious traditions teach divine judgment of human sin; many experiencers might expect condemnation. Yet the data show love rather than judgment, revelation rather than punishment, education rather than sentence. This aligns precisely with Swedenborg's account: the World of Spirits shows rather than condemns, enabling self-knowledge rather than imposing external punishment.

### 4.4 Clinical Implications

If NDE structure reflects genuine spiritual geography rather than cultural construction, several clinical implications follow.

For preparation for death, education about NDEs may reduce death anxiety. The consistent finding that experiencers prefer the spiritual realm and encounter love rather than judgment suggests death may be less fearsome than commonly believed. Sharing this research with the dying and their families may provide comfort.

For post-NDE support, understanding the involuntary nature of return may help NDErs integrate their experience. Many experiencers struggle with having been "sent back"—feeling they glimpsed something wonderful and were forced to leave. Validating this experience as common and meaningful (rather than dismissing it as hallucination) supports healthy integration.

For palliative care, the consistent non-judgmental character of life reviews may comfort the dying. Those fearing divine judgment for past failures can be reassured that NDE research shows love vastly outweighing condemnation. The life review appears designed for education and growth, not punishment.

### 4.5 Limitations

Several limitations warrant acknowledgment. Self-selection bias affects the sample: profound experiences are more likely to be reported, potentially skewing the corpus toward more elaborate NDEs. The Western sample limits generalizability: non-Western NDE phenomenology may differ in ways not captured here. Retrospective reporting introduces potential distortion: narrative ordering may be imposed post-hoc rather than reflecting actual experience sequence. And GPT-5.2 extraction may have systematic biases in how it interprets and codes NDE accounts.

### 4.6 Future Directions

Cross-cultural analysis would test whether these patterns are universal or culture-specific. Prospective tracking would document transformation trajectories following NDEs, testing whether the experience produces lasting change. Longitudinal follow-up would assess whether "mission" returners show distinctive life trajectories—do they actually accomplish the missions they report being sent back for? And integration with DOPS past-life memory research would enable testing of the restorative incarnation hypothesis against independently verified cases.

---

## 5. Conclusion

Analysis of 6,753 near-death experiences provides convergent support for the Normative Path Hypothesis. Experiencers are reluctant to leave the spiritual realm—49.4% prefer to stay—suggesting they recognize it as genuinely preferable to physical existence. Deceased relatives are present and recognizable in 17.9% of cases, indicating they have continued rather than reincarnated. Reincarnation indicators are rare across the corpus, with past life memory appearing in only 4.4% and pre-incarnation covenants in only 1.3%. Personal identity persists throughout the experience in 64.8% of cases.

The data support a threefold path model: normative continuation (the vast majority), restorative incarnation for trauma healing (perhaps 4%), and volunteer incarnation for mission (perhaps 1%). The life review, appearing in 17.5% of cases, reveals rather than condemns—with a love-to-harsh ratio of 15.9:1.

The NDE appears to offer a glimpse into the first stage of post-mortem existence—what Swedenborg termed the World of Spirits, an intermediate realm where consciousness transitions from earthly to spiritual organization. The consistent phenomenology across experiencers—the reluctance to return, the presence of deceased relatives, the loving character of any judgment, the preservation of personal identity—suggests NDErs are not constructing hallucinations from cultural materials but encountering a genuine realm whose features they report with remarkable consistency.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry*, 25(4), 269-276.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value |
|------|-----------|----|---------| 
| Agency × Willingness | χ² = 4824.78 | — | < 0.0001 |
| Love:Harsh Ratio | 223:14 | — | 15.9:1 |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,664 |
| IANDS records | 1,089 |
| Return not by choice | 70.1% |
| Reluctant to return | 49.4% |
| Deceased relatives present | 17.9% |
| Past life memory | 4.4% |
| Pre-incarnation covenant | 1.3% |
| Life review occurred | 17.5% |
| Love:Harsh judgment ratio | 15.9:1 |
| Identity preserved | 64.8% |

## Appendix C: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [02_normative_path_validation.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb)
