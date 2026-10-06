# Mission-Based Returns: Volunteer Soul Detection Analysis

> **Correction notice (2026-10-05).** This report was revised after a statistical audit (`docs/STATISTICAL_AUDIT_2026-10.md`). Changes: (1) the headline "94.2% discriminant accuracy" is a **positive predictive value**; the full diagnostic picture is sensitivity 39.7%, accuracy 86.2% against a 78.1% baseline, and Cohen's κ = 0.49; (2) the χ² values for mission commissioning (3,018) and volunteer language (599) tested variables that *define* the volunteer group and are circular; (3) "sense of belonging shows no association (χ² = 0.0)" and "life transformation shows no association" were produced by a wrong field path and a non-existent field — belonging is in fact associated (χ² = 252); (4) the volunteer-detection rule described in Methods did not match the rule used; (5) associations are now adjusted for narrative length; (6) N = 6,751 (two duplicate narratives removed; four IANDS records previously mislabelled NDERF). The LaTeX and PDF versions were regenerated from this corrected text.

> **Reliability addendum (2026-10-06).** Coding reliability was measured with a blind second coder; see *Reliability of Near-Death Experience Narrative Coding* (`08_extraction_reliability.ipynb`). Mission commissioning agrees at Cohen's κ = 0.71 and the earthly-mission return reason at 0.75. GPT-5.2's "implied" commissioning codes are liberal. The second coder confirmed all 7 explicit codes but only 5 of 13 implied ones; the rest were general life lessons rather than a specific task. Calibrated to the second coder, commissioning prevalence is about 14.8% (95% CI 12.2–18.4) rather than 21.9%. The association between an earthly-mission return reason and commissioning holds under both coders (6/6 and 6/7 in the sample).

## Abstract

Some near-death experiencers report returning for an "earthly mission". The Swedenborgian framework proposes that mission-based returns form a distinct category associated with souls who incarnate for specific purposes. We analysed 6,751 NDE records from NDERF (n=5,659) and IANDS (n=1,092), coded by GPT-5.2 for return reasons, mission commissioning, volunteer language, pre-birth indicators and related features. We use binary "volunteer detection" rather than soul-path classification.

An earthly-mission return reason appeared in 9.2% of NDEs. Of these, 94.2% (95% CI 92.1–95.8) were also coded as having received a mission (positive predictive value), compared with 29.8–60.1% for other return reasons and 9.1% when no reason was given. The reverse does not hold: 60.3% of commissioned experiencers did not cite an earthly mission (sensitivity 39.7%); agreement between the two codes is moderate (κ = 0.49). Volunteer markers were detected in 695 accounts (10.3%). In the 53 accounts using volunteer language, pre-birth indicators were 10–36 times more frequent, an overlap that is largely definitional. Volunteer-detected accounts also differed on independent features — spiritual "home" identification, explicit belonging, hyper-reality, major value shift and Being-of-Light encounters — with associations that remain after adjustment for narrative length (adjusted ORs 2.0–3.3).

Mission-return narratives form an internally coherent and distinctive cluster. Because all variables are model-coded features of the same retrospective narrative, the data establish that mission commissioning is consistently *reported*, not that it occurred.

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `03_volunteer_soul_profile.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/03_volunteer_soul_profile.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

A subset of near-death experiencers report returning not because of family obligation or timing but because they were given, or accepted, an earthly mission (Ring, 1998; Atwater, 2007). Whether this is a distinct phenomenological category or a retrospective framing of an unwanted return has not been systematically examined.

### 1.2 Theoretical Framework

The Swedenborgian framework distinguishes normative incarnation from incarnation undertaken for specific service. The "volunteer soul" hypothesis (cf. Newton, 1994) proposes that some individuals retain awareness of choosing their life for a purpose. Predictions: mission-returners should report commissioning during the NDE, elevated pre-birth awareness, and a coherent profile of related features.

### 1.3 Methodological Approach: Detection, Not Classification

We measure whether volunteer-type markers are *reported*. We cannot measure soul paths, first versus returning incarnation, or Ohkado-type "reverse cases" (children with spontaneous pre-birth memory — a different population and method). Pre-birth awareness during an NDE may occur in any experiencer.

**Same-source caveat.** Every variable is coded by the same language model from the same narrative. When two codes describe overlapping content ("returned for a mission" and "was given a mission"), their association partly reflects the same passage coded twice. Such associations show that narratives are internally coherent; they cannot by themselves show that the reported events occurred.

### 1.4 Aims

To describe how mission returns relate to commissioning, volunteer language and pre-birth indicators; to characterise volunteer-detected accounts on features that do not define the group; and to state what these data can and cannot establish.

---

## 2. Methods

### 2.1 Data Sources

NDERF (5,659) and IANDS (1,092); N = 6,751 after removing two duplicate narratives.

### 2.2 Coding Scheme

Return reasons (multi-select), return agency and willingness, mission commissioned (`yes_explicit`/`implied`/`no`/`not_mentioned`), volunteer language, premortal existence information, pre-birth realm description, chose mission / parents / life circumstances, identity pre-body, home identification, past-life and prior-death memory, and features not used in detection (belonging, comparative reality, value shift, light encounter).

### 2.3 Volunteer Detection Rule

A case is flagged if **any** of: volunteer language (explicit or implied); earthly mission among return reasons; or mission commissioned (explicit or implied) **and** chose mission (explicit or implied). (The previous version of this section described the third criterion as "mission commissioned = yes_explicit", a rule that would flag 898 cases instead of 695.)

### 2.4 Statistical Analysis

Confusion-matrix diagnostics (PPV, sensitivity, specificity, accuracy, Cohen's κ); Fisher exact tests; χ² with Cramér's V; Wilson CIs. Volunteer-detected accounts are twice as long as others (median 1,353 vs 635 words), so associations are also reported as odds ratios adjusted for log narrative word count. Tests involving a variable that defines the volunteer group are labelled circular.

---

## 3. Results

### 3.1 Return Reasons

Not your time 21.6%, family responsibility 17.2%, unfinished business 10.5%, earthly mission 9.2% (n = 623), other 3.2%; 44.3% gave at least one reason and 1,034 gave more than one.

### 3.2 Earthly Mission and Mission Commissioning

| Return reason | Mission commissioned (explicit or implied) |
|---|---|
| Earthly mission (n=623) | 94.2% (92.1–95.8) |
| Unfinished business (n=711) | 60.1% (56.4–63.6) |
| Not your time (n=1,459) | 36.7% (34.2–39.2) |
| Family responsibility (n=1,164) | 31.3% (28.7–34.0) |
| Other (n=218) | 29.8% (24.1–36.2) |
| No reason given (n=3,763) | 9.1% (8.2–10.1) |

| Diagnostic: earthly mission → commissioned | Value |
|---|---|
| Positive predictive value | 94.2% (587/623) |
| Sensitivity | 39.7% (587/1,480) |
| Specificity | 99.3% (5,235/5,271) |
| Accuracy | 86.2% (majority-class baseline 78.1%) |
| Cohen's κ | 0.49 |
| Odds ratio (length-adjusted) | 88.9 (95% CI 62.6–126.3) |

**Finding (corrected).** Experiencers who give an earthly mission as their reason for returning are almost always also coded as having received a mission (PPV 94.2%), but most commissioned experiencers give other reasons, so the overall agreement is moderate (κ = 0.49). "94.2% discriminant accuracy" was a mislabelled positive predictive value.

**Interpretation.** The association is strong and coherent. Because the two codes describe overlapping content in the same narrative, it cannot distinguish "commissioning occurred during the NDE" from "the return was later framed as a mission". The earlier statement that the result "cannot be explained by post-hoc rationalization" is withdrawn.

### 3.3 Volunteer Detection

Volunteer markers were detected in 695 accounts (10.3%, 95% CI 9.6–11.0): 623 via an earthly-mission reason, 53 via volunteer language, and 42 only via commissioning plus chosen mission.

### 3.4 Volunteer Language and Pre-Birth Indicators

Volunteer language was explicit in 22 accounts and implied in 31 (0.8% together); 4,596 explicitly lacked it and 2,102 did not address it. These 53 accounts are long (median 2,314 vs 676 words).

| Indicator | Volunteer language (n=53) | Others (n=6,698) | Rate ratio | Fisher OR | Length-adjusted OR (95% CI) |
|---|---|---|---|---|---|
| Incarnation choice (any) | 71.7% | 2.0% | 36 | 124 | 73 (37–144) |
| Pre-birth realm description | 34.0% | 1.5% | 22 | 33 | 14 (7.5–28) |
| Premortal existence information | 69.8% | 6.6% | 11 | 33 | 18 (9.0–35) |
| Home = spiritual realm | 58.5% | 16.8% | 3.5 | 7.0 | 3.6 (2.0–6.4) |
| Identity pre-body | 79.2% | 34.6% | 2.3 | 7.2 | 3.9 (2.0–7.9) |

**Finding.** Pre-birth indicators are strongly elevated in volunteer-language accounts, beyond what narrative length explains. However, "volunteering to incarnate" *semantically entails* pre-birth existence and a choice to incarnate, so co-occurrence of these codes is largely definitional. With 53 accounts, intervals are wide.

### 3.5 Profile of Volunteer-Detected Accounts

| Characteristic | Volunteer-detected (n=695) | Not detected (n=6,056) | Length-adjusted OR (95% CI) | Status |
|---|---|---|---|---|
| Mission commissioned | 92.7% | 13.8% | — | Defines the group |
| Volunteer language | 7.6% | 0% | — | Defines the group |
| Pre-birth awareness | 29.4% | 5.1% | 4.7 (3.8–5.9) | Partly definitional |
| Continuation memory | 14.0% | 3.3% | 2.8 (2.1–3.6) | Independent |
| Home = spiritual realm | 41.4% | 14.4% | 3.0 (2.5–3.5) | Independent |
| Sense of belonging (explicit) | 25.0% | 9.1% | 2.2 (1.8–2.8) | Independent |
| More real than earthly reality | 36% | 14% | 2.0 (1.7–2.4) | Independent |
| Major value shift | 58% | 26% | 2.6 (2.2–3.1) | Independent |
| Being of Light (light_encounter) | 32% | 9.5% | 3.3 (2.7–4.0) | Independent |

**Finding (statistically supported).** Volunteer-detected accounts differ on several features that play no part in the detection rule, and these associations remain after adjustment for narrative length. The earlier statement that "sense of belonging … χ² = 0.0 … the profile is specific, not global" was an artifact of reading the field from the wrong section; belonging is associated with volunteer detection (χ² = 252.1, df = 3, p < 10⁻⁵³, V = 0.19).

### 3.6 Continuation Memory

Past-life memory appears in 4.4% of NDEs, intermission memory in 1.0%, and memory of a prior death in 0.5% (36 accounts, 19 violent; previously reported as 0 because the wrong values were matched). Past-life memory co-occurs *positively* with volunteer language (4.4% vs 0.6%; OR 7.3), mission commissioning (52.9% vs 20.5%; OR 4.3) and earthly-mission returns (25.3% vs 8.5%; OR 3.6). This is compatible with "past-life memory" in NDE narratives often reflecting remembered pre-existence rather than prior earth lives, but the data cannot distinguish the two.

### 3.7 Pre-Birth Indicator Count

Zero indicators 92.4%, one 4.9%, two 2.0%, three 0.7% (n = 47). Of the 47 accounts with all three, 41 (87.2%) are volunteer-detected — partly by construction, since "chose mission" contributes both to the count and to the detection rule.

### 3.8 Statistical Tests

| Variable × volunteer detection | χ² | df | V | Status |
|---|---|---|---|---|
| Mission commissioned | 3,017.0 | 3 | 0.67 | **Circular** |
| Volunteer language | 599.2 | 3 | 0.30 | **Circular** |
| Pre-birth awareness | 515.5 | 1 | 0.28 | Partly circular |
| Return agency | 696.5 | 4 | 0.32 | Independent |
| Return willingness | 284.8 | 4 | 0.21 | Independent |
| Sense of belonging | 252.1 | 3 | 0.19 | Independent |
| Comparative reality | 223.3 | 3 | 0.18 | Independent |
| Continuation memory | 164.7 | 1 | 0.16 | Independent |

All p < 10⁻³⁷. Circular tests are not evidence for the category.

---

## 4. Discussion

### 4.1 Summary of Corrected Findings

Mission-return narratives are coherent: an earthly-mission reason almost always comes with a reported commissioning, volunteer language almost always with pre-birth content, and volunteer-detected accounts differ on several independent features (spiritual home, belonging, hyper-reality, value change, Being of Light) even after accounting for how much the narrative says.

### 4.2 What the Data Support

- A recognisable cluster of mission-related reports exists in about one in ten NDE accounts.
- The cluster is associated with features outside its definition, so it is not merely a by-product of the detection rule.
- The framework's prediction that mission-returners report commissioning and pre-birth awareness is **consistent with** the data.

### 4.3 What the Data Cannot Support

- That commissioning *occurred*: all evidence is the same retrospective narrative coded twice.
- That mission returns are not retrospective meaning-making: the data contain no measure that would distinguish the two.
- Soul-path classification, first versus returning incarnation, or Ohkado-type reverse cases.
- That non-detection means non-volunteer.

### 4.4 Implications

Clinically, mission-return accounts are coherent and warrant respectful engagement; their coherence does not, however, establish their accuracy, and clinicians need not adjudicate it. For research, longitudinal follow-up (do mission-returners report pursuing the stated mission?) and independent corroboration would test what the narrative data cannot.

### 4.5 Limitations

LLM extraction (inter-coder κ 0.71 for commissioning, with liberal "implied" codes that overstate prevalence by about a third); self-selected archives; mission and volunteer language may be culturally available framings; volunteer-language n = 53; detection is rule-dependent (695 vs 898 under the alternative rule).

### 4.6 Future Directions

Human coding of mission content; prospective and longitudinal designs; cross-cultural samples; schema fields that separate *when* in the narrative the mission was given from *how* the return was explained.

---

## 5. Conclusion

In 6,751 near-death experiences, about 10% contain volunteer or mission markers. Mission returns and reported commissioning go together (PPV 94.2%, κ = 0.49), volunteer language goes with pre-birth content, and mission-oriented accounts differ from others on several independent features after narrative length is controlled. These results show a coherent, distinctive pattern of *reports*. They do not show that commissioning took place, and the earlier claims of "94.2% discriminant accuracy" and validation by χ² tests on defining variables have been withdrawn.

---

## References

Atwater, P. M. H. (2007). *The Big Book of Near-Death Experiences*. Hampton Roads Publishing.

Newton, M. (1994). *Journey of Souls: Case Studies of Life Between Lives*. Llewellyn Publications.

Ohkado, M. (2017). Children with life-between-life memories. *Journal of Scientific Exploration*, 31(2), 217–228.

Ring, K. (1998). *Lessons from the Light: What We Can Learn from the Near-Death Experience*. Perseus Books.

---

## Appendix A: Statistical Summary

| Test | Value |
|------|-------|
| Earthly mission → commissioned: PPV / sensitivity / specificity | 94.2% / 39.7% / 99.3% |
| Accuracy vs baseline | 86.2% vs 78.1% |
| Cohen's κ | 0.49 |
| Volunteer × belonging (independent) | χ² = 252.1, df = 3, V = 0.19 |
| Volunteer × return agency (independent) | χ² = 696.5, df = 4, V = 0.32 |
| Volunteer × mission commissioned | χ² = 3,017.0 (circular) |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,751 |
| Earthly-mission return reason | 623 (9.2%) |
| Volunteer markers detected | 695 (10.3%) |
| Volunteer language | 53 (0.8%) |
| Pre-birth awareness | 515 (7.6%) |
| Continuation memory | 298 (4.4%) |
| Home is spiritual (volunteer / not) | 41.4% / 14.4% |

## Appendix C: Methodological Notes

Volunteer detection measures the presence of reported mission markers. It does not measure soul path, first versus returning incarnation, Ohkado-type pre-birth memory, or restorative path (which requires DOPS-type verified data).

## Appendix D: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **Analysis Notebook**: [03_volunteer_soul_profile.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/03_volunteer_soul_profile.ipynb)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
