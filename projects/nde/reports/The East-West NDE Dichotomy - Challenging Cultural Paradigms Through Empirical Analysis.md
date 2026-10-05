# The East-West NDE Dichotomy: Challenging Cultural Paradigms Through Empirical Analysis

> **Correction notice (2026-10-05).** This report was revised after a statistical audit (`docs/STATISTICAL_AUDIT_2026-10.md`). Changes: (1) **the statement that inter-rater reliability was assessed (κ = 0.84 on 200 records) has been removed** — no such validation exists in the repository, and the companion perception report lists human validation as future work; (2) "deceased relatives (17.9%) nearly twice religious figures (9.9%)" omitted God and Jesus from the religious-figure count — corrected counts are 13.8–19.9% depending on definition, and the "inversion" does not hold under the report's own category label; (3) "brilliant light" was relabelled "impersonal light", but more than half of those accounts identify beings and report communication; (4) the nature-vs-urban test used an invalid goodness-of-fit χ² on overlapping counts (now McNemar); (5) several appendix χ² values did not match their p-values; (6) associations are now adjusted for narrative length; (7) the boundary-type × agency association is partly built into the category definitions; (8) the sample was described as "Western NDEs" although country is unknown for 88% and 27% of known countries are outside the West; (9) N = 6,751 after removing two duplicate narratives. The LaTeX and PDF versions were regenerated from this corrected text.

## Abstract

**Background**: Cross-cultural NDE literature has contrasted a "Western" profile — personified Being of Light (claimed 70–80%), Cities of Light, frequent life reviews (25–30%), tunnel (34–50%) — with a "Japanese" profile of impersonal light, flower gardens, ancestors and absent life reviews. Both profiles rest on small or selected samples.

**Methods**: We analysed 6,751 structured NDE records from two predominantly Western, English-language archives (NDERF n=5,659; IANDS n=1,092), coded with GPT-5.2 structured extraction. We compared observed prevalences with the claimed Western rates (exact binomial tests), compared paired features with McNemar tests, and estimated associations with odds ratios adjusted for narrative length.

**Results**: The light was coded as a *being* of light in 11.8% of all accounts (20.7% of accounts reporting any light or presence), far below the claimed 70–80%. Brilliant light without a being *of* light (40.9%) was more common, but this is not "impersonal": 57.0% of brilliant-light accounts identified beings and 56.9% reported communication. Landscape features exceeded buildings (17.0% vs 11.4%; McNemar p < 10⁻²⁴). Life reviews (17.5%) and tunnels (23.7%) were less frequent than claimed. Deceased relatives (17.9%) exceeded named religious figures (13.8%) but not religious figures including angels (17.1–19.9%), so the "ancestor inversion" is definition-dependent. Being-of-Light encounters co-occurred with earthly-mission returns (OR 4.38; 3.26 after length adjustment) and life reviews (OR 2.55; 1.89 adjusted). Boundary reporters described more of nearly every other element, robust to length adjustment; boundary type was associated with return agency (Cramér's V = 0.35), partly by category definition.

**Conclusions**: The claimed Western prevalence figures do not describe these archives. Whether the Japanese profile is equally distorted cannot be tested without Japanese data. Personal interaction with the Light is associated with purposive elements of the narrative; reading this as "purposive economy" is a framework interpretation.

**Keywords**: near-death experience, cross-cultural, Being of Light, life review, cultural paradigm, purposive economy, Japanese NDE, correspondences, boundary

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Notebook | `05_cultural_paradigm_challenge.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files; 6,751 unique narratives) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 The Paradigm and Its Origins

Following Moody (1975), researchers asked whether NDE features hold across cultures. A dichotomy emerged: Western NDEs with a personified Being of Light, urban heavenly realms and morally evaluative life reviews; Japanese NDEs with ambient light, natural settings such as flower gardens and rivers, ancestral guides and absent life reviews. If NDEs vary this way by culture, the dying brain might construct experiences from cultural templates. Both profiles, however, rest on small or curated samples (e.g. Ohkado & Greyson, 2014, with 22 interviews), and neither may represent the phenomenon's baseline.

### 1.2 The Problem of Prevalence Claims

The 70–80% Being-of-Light figure appears repeatedly but its provenance and denominator are unclear; it may describe selected "classic" cases or core NDEs rather than all accounts. The same scrutiny applies to the Japanese profile. The figures quoted as "claimed" in this report are taken from the source document in `docs/`; because their denominators are not documented, comparisons with them are indicative.

### 1.3 Theoretical Framework: Correspondences and Purposive Economy

The Swedenborgian framework proposes that spiritual realities are constant while their perceived forms vary with the observer's repertoire. **Purposive economy** extends this: the Light engages personally when the encounter's purpose requires it (commissioning, review, teaching) and remains as presence otherwise. Predictions: personal interaction should correlate with purpose; nature and urban imagery should not be culture-specific; boundaries should function as expressions of the return decision rather than fixed locations.

### 1.4 Aims

1. Test the claimed prevalences of "Western" features against these archives
2. Examine whether personal interaction with the Light correlates with purposive elements
3. Examine what boundary reports correlate with
4. State what can and cannot be concluded about the East-West dichotomy from Western-archive data

---

## 2. Methods

### 2.1 Data Sources

NDERF (5,659 accounts; online questionnaire) and IANDS (1,092 narrative accounts); two duplicate narratives counted once (N = 6,751). Both archives consist of self-selected submissions. Country is stated in 829 accounts (12.3%); of these, 72.7% are from North America, Western Europe or Australasia and 27.3% from elsewhere (e.g. India, Mexico, Brazil, Iran). "Western NDEs" in this report means *accounts in two predominantly Western, English-language archives*.

### 2.2 Structured Extraction

Each record was processed with GPT-5.2 (Azure OpenAI) into the Pydantic schema in `models/questionnaire.py`. Key fields: `light_encounter` (brilliant_light, being_of_light, presence_without_visual, no, not_mentioned); `being_identifications` (multi-select); `environment_features` (light, landscape, buildings, sky, colors, water, other); life review occurrence; `boundary_encounter` (none, physical_barrier, verbal_limit, threshold, not_mentioned); return reasons; return agency (self, external_being, involuntary, mutual, not_mentioned).

**No human validation of the extraction has been performed.** (An earlier version of this report stated that human coders achieved κ = 0.84 on 200 records; no record of such a study exists, and the statement has been removed.)

### 2.3 Statistical Analysis

Wilson 95% CIs; exact binomial tests against claimed rates; McNemar tests for paired features within the same accounts; χ² with Yates correction for 2×2 tables and Cramér's V; Fisher exact tests; logistic regression odds ratios adjusted for log narrative word count (accounts with more elements are longer, so crude co-occurrence overstates association).

---

## 3. Results

### 3.1 The Being of Light: Testing the Central Claim

| Light Encounter Type | N | % of all |
|---------------------|---|---|
| Brilliant light (no being *of* light) | 2,759 | 40.9% |
| No light | 1,636 | 24.2% |
| Not mentioned | 1,274 | 18.9% |
| Being of light | 797 | **11.8%** |
| Presence without visual | 285 | 4.2% |

The light itself was coded as a being in 11.8% of all accounts (95% CI 11.1–12.6), 14.6% of accounts addressing light, and 20.7% of accounts reporting any light or presence. All are far below 70–80% (binomial p ≈ 0).

**What "brilliant light" contains.** The category means "light without an identified being *of* light", not "no personal interaction". Of 2,759 brilliant-light accounts, 57.0% identified beings, 56.9% reported communication with beings and 25.6% telepathic communication; 7.3% identified God or Jesus. Being-of-light accounts identified God or Jesus in 46.4% and reported communication in 88.8%.

**Finding.** The *form* of the light is far more often a brilliant light than a luminous being — this is robust. The earlier "impersonal : personified = 3.8 : 1" equated the form of the light with the presence of personal interaction, which these data contradict; it has been withdrawn.

### 3.2 Beings and Settings

**Beings.**

| Category | % of NDEs | McNemar vs deceased relatives |
|---|---|---|
| Deceased relatives encountered | 17.9% | — |
| Named religious figure (God/Jesus/Buddha/specified) | 13.8% | χ² = 43.8, p < 10⁻¹⁰ |
| Named religious figure or angels | 17.1% | χ² = 1.2, p = 0.26 |
| … or spiritual-being codes (religious figures, guides/angels) | 19.9% | χ² = 9.7, p = 0.002 |

The earlier count of 9.9% for "religious figures (God/Jesus/angels/specified)" omitted God and Jesus because of a field error.

**Finding.** Deceased relatives are more common than *named* religious figures (ratio 1.3, not 1.8), but under the report's own category — God, Jesus, angels and specified figures — religious figures are as common as deceased relatives. The claim that Western NDEs follow the "ancestor model" is **not supported**; both kinds of being are common.

**Settings.**

| Environment Feature | N | % of all NDEs |
|--------------------|---|---------------|
| Light | 3,394 | 50.3% |
| Colors | 1,906 | 28.2% |
| Landscape | 1,151 | **17.0%** |
| Sky | 871 | 12.9% |
| Buildings | 772 | **11.4%** |
| Water | 414 | 6.1% |

Landscape exceeded buildings (296 accounts had both; McNemar χ² = 107.4, p < 10⁻²⁴); among accounts describing any environment, 23.0% vs 15.4%. The schema has no "garden" or "city" category, so these are approximations. (The previous χ² = 74.7 compared overlapping counts with a goodness-of-fit test, which is invalid.)

**Finding (statistically supported):** natural features are more common than built ones in these archives.

### 3.3 Life Review and Tunnel

| Feature | Claimed Western rate | Observed | 95% CI | Binomial p (vs lower bound) |
|---|---|---|---|---|
| Being of light (all accounts) | 70–80% | 11.8% | 11.1–12.6 | ≈ 0 |
| Being of light (accounts with any light) | 70–80% | 20.7% | 19.5–22.1 | ≈ 0 |
| Life review | 25–30% | 17.5% | 16.6–18.4 | < 10⁻⁴⁸ |
| Tunnel | 34–50% | 23.7% | 22.7–24.8 | < 10⁻⁷⁴ |

Life reviews with a judgment element (any evaluator, including self) occur in 6.4% of all NDEs; with an external evaluator in 5.0%.

**Finding:** the claimed Western rates do not describe these archives. Because the claims' denominators are undocumented and the archives are self-selected, this shows the claims are not representative of these data; it does not by itself explain how the claims arose.

### 3.4 Personal Interaction and Purpose

| Element | BoL rate with / without | Co-occur / expected | χ² (Yates) | OR | Length-adjusted OR (95% CI) |
|---|---|---|---|---|---|
| Earthly mission (reason) | 32.1% / 9.7% | 200 / 73.5 | 269.4 | 4.38 | 3.26 (2.68–3.97) |
| Mission commissioned | 25.3% / 8.0% | 375 / 175 | 332 | 3.90 | 2.88 (2.45–3.39) |
| Life review | 21.6% / 9.7% | 255 / 140 | 129.8 | 2.55 | 1.89 (1.59–2.25) |
| Not your time (reason) | 20.4% / 9.4% | 297 / 172 | 129.7 | 2.45 | 2.30 (1.96–2.70) |
| Family responsibility (reason) | 17.4% / 10.6% | 203 / 137 | 42.2 | 1.78 | 1.50 (1.25–1.79) |

Fisher exact test, earthly mission × Being of Light: OR 4.38, p ≈ 10⁻⁴⁶. Among the three light types, life-review rates were 32.0% (being of light), 19.1% (brilliant light) and 17.5% (presence without visual); χ² = 64.0, df = 2, p < 10⁻¹³.

**Finding (statistically supported):** Being-of-Light encounters co-occur with life reviews, mission returns and other return reasons more than chance predicts, and these associations survive adjustment for narrative length (attenuated by about a quarter).

**Interpretation.** Purposive economy reads this as the Light becoming personal when purpose requires it. Two alternative readings fit the same association: a single narrative passage in which a luminous being gives instructions will be coded both as `being_of_light` and as a mission; and experiencers who meet a personified being may be more likely to frame their return as purposeful. The association is real in the data; its direction is interpretation. The hypothesis that Japanese samples show fewer personified encounters *because* they contain fewer mission returns is not tested here (no Japanese data).

### 3.5 Boundaries

Any boundary was reported in 41.9% of accounts (verbal limit 18.3%, physical barrier 12.9%, threshold 10.8%).

**Tunnel and boundary are associated:** boundary in 58.6% of tunnel accounts vs 36.8% of others (χ² = 236.9, OR 2.43, φ = 0.19; length-adjusted OR 2.24, 95% CI 1.99–2.51). Most tunnel accounts are nevertheless not boundary accounts; they are distinct but correlated elements.

**Content with and without a boundary:**

| Content | With boundary | Without | Crude OR | Length-adjusted OR (95% CI) |
|---|---|---|---|---|
| Heavenly realm | 43.5% | 18.7% | 3.35 | 2.92 (2.61–3.28) |
| Deceased relatives | 27.9% | 10.6% | 3.27 | 3.07 (2.69–3.51) |
| Being of light | 18.8% | 6.7% | 3.21 | 2.73 (2.33–3.21) |
| Named religious figure | 19.4% | 9.7% | 2.24 | 1.97 (1.71–2.28) |
| Buildings | 16.0% | 8.1% | 2.16 | 1.90 (1.63–2.22) |
| Life review | 21.3% | 14.8% | 1.55 | 1.28 (1.13–1.46) |

Of 772 accounts with buildings, 55.3% report no physical or verbal boundary; of 1,962 with heavenly realms, 53.3%. A depth score (0–8) is higher with a boundary (3.95 vs 2.58; +1.12 after length adjustment).

**Finding (statistically supported):** boundary reporters describe *more* of the other elements, so boundaries do not mark a point before which experiences stop.

**Boundary type and return agency** (boundary reported and agency stated, n = 2,733): external being decided in 70.5% of verbal limits and 58.4% of physical barriers; self in 48.8% of thresholds (χ² = 683.8, df = 6, Cramér's V = 0.35; the earlier χ² = 3,724.7 with df = 16 — 3,728.7 on the deduplicated data — included the "none" and "not mentioned" categories).

**Finding with caveat.** The association is partly built into the categories: a verbal limit is by definition a being telling the experiencer to go back, and a threshold is typically the experiencer's own sense of a limit. It is therefore expected from the coding and cannot by itself show that the boundary *is* the return decision. That reading is a framework interpretation. Physical barriers co-occur with water in 11.3% of cases.

Two earlier arguments were removed as invalid: that unequal frequencies of boundary types show they are "not consistent representations of the same phenomenon" (frequency says nothing about consistency), and that 58% returning without a boundary shows boundaries are not points of no return (everyone in the dataset returned; the earlier version itself noted this is untestable).

### 3.6 Summary

| Feature | Claimed Western | Observed in these archives | Assessment |
|---------|-----------------|------------------|----------------|
| Being of light | 70–80% | 11.8% (20.7% of light accounts) | Claim not observed |
| Brilliant light = impersonal | — | 57% identify beings, 57% communicate | Relabelling withdrawn |
| Life review | 25–30% | 17.5% | Lower than claimed |
| Tunnel | 34–50% | 23.7% | Lower than claimed |
| Nature > urban | No | Landscape 17.0% vs buildings 11.4% | Western claim not observed |
| Deceased > religious figures | No | 17.9% vs 13.8–19.9% | Definition-dependent |
| Purpose ↔ personal interaction | — | Mission OR 3.3 (adjusted) | Association supported; causation interpretive |
| Boundary as hard limit | — | Boundary reporters report more | Not supported |

---

## 4. Discussion

### 4.1 What the Data Show About the Western Profile

In two large Western archives, the light is usually experienced as brilliant light rather than a luminous being, life reviews and tunnels are less frequent than often claimed, and natural features are more common than buildings. The claimed Western figures do not describe these archives. Plausible contributors include selection of dramatic cases in early research, differences in denominators (all accounts vs core NDEs), and the self-selection of these archives; the data do not identify which.

### 4.2 What the Data Cannot Show About the Japanese Profile

No Japanese accounts are analysed. Whether the Japanese profile is also a distortion, and whether purpose-distribution explains East-West differences, remain hypotheses. The earlier conclusion that "the dichotomy was never real" went beyond what Western data can show.

### 4.3 The Correspondential Model

The data fit a model in which the Light appears in variable forms — usually brilliant, sometimes a personal figure — and in which the personal form co-occurs with purposive narrative elements. They also fit a model in which richer, more purposeful narratives produce more codes of every kind; length adjustment reduces but does not remove this concern. The correspondential reading of boundaries as expressions of the return decision is coherent but rests on an association partly built into the coding.

### 4.4 Implications for Cross-Cultural Research

Cross-cultural comparisons need common, documented denominators; large, systematically coded samples from each culture; paired tests for features reported in the same accounts; control for narrative length; and validated coding. Applying this extraction to Japanese and other non-Western archives is the necessary next step.

### 4.5 Limitations

Self-selected archives; no human validation of LLM extraction; "not mentioned" treated as absence for prevalence figures; country unknown for 88%; no non-Western comparison sample; claimed rates of uncertain provenance.

---

## 5. Conclusion

In 6,751 NDE accounts from two predominantly Western archives, the light was a luminous *being* in about one account in eight (one in five among those reporting light), far below the 70–80% often attributed to Western NDEs; life reviews and tunnels were also less frequent than claimed, and natural features exceeded built ones. These findings challenge the Western half of the East-West dichotomy as a description of these archives. They do not test the Japanese half. Corrected counts do not support the claim that deceased relatives dominate over religious figures, and "brilliant light" is not impersonal. Personal encounters with the Light co-occur with purposive narrative elements even after length adjustment — consistent with the purposive-economy interpretation, which remains an interpretation rather than a demonstrated mechanism.

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
| McNemar | Landscape vs buildings | χ² = 107.4 | 1 | < 10⁻²⁴ |
| McNemar | Deceased vs named religious figures | χ² = 43.8 | 1 | < 10⁻¹⁰ |
| McNemar | Deceased vs religious figures incl. angels | χ² = 1.2 | 1 | 0.26 |
| Binomial | Being of light vs 70% | 11.8% observed | — | ≈ 0 |
| Binomial | Life review vs 25% | 17.5% observed | — | < 10⁻⁴⁸ |
| Binomial | Tunnel vs 34% | 23.7% observed | — | < 10⁻⁷⁴ |
| χ² | Light type (3 types) × life review | χ² = 64.0 | 2 | < 10⁻¹³ |
| χ² (Yates) | Life review × Being of light | χ² = 129.8 | 1 | < 10⁻²⁹ |
| χ² (Yates) | Earthly mission × Being of light | χ² = 269.4 | 1 | < 10⁻⁵⁹ |
| Fisher | Earthly mission × Being of light | OR = 4.38 (adjusted 3.26) | — | ≈ 10⁻⁴⁶ |
| χ² | Tunnel × boundary | χ² = 236.9, OR 2.43 | 1 | < 10⁻⁵² |
| χ² | Boundary type × return agency (both stated) | χ² = 683.8, V = 0.35 | 6 | < 10⁻¹⁴³ |
| Mann-Whitney | Depth score by boundary | 3.95 vs 2.58 | — | < 10⁻²³⁸ |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,751 |
| Being of light | 797 (11.8%) |
| Brilliant light | 2,759 (40.9%) |
| … of which identify beings / report communication | 57.0% / 56.9% |
| Landscape / buildings | 17.0% / 11.4% |
| Deceased relatives | 17.9% |
| Named religious figures / incl. angels | 13.8% / 17.1% |
| Life reviews | 17.5% |
| Tunnel | 23.7% |
| Any boundary | 41.9% |
| Earthly mission → Being of light, OR (adjusted) | 4.38 (3.26) |

## Appendix C: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **Analysis Notebook**: [05_cultural_paradigm_challenge.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/05_cultural_paradigm_challenge.ipynb)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
