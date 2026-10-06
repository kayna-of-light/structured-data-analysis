# Functional Differentiation of Beings in Near-Death Experiences: Testing Role Specialisation

## Abstract

**Background**: Near-death experiencers report meeting divine or religious figures, unidentified presences, angels and deceased relatives. The Swedenborgian framework predicts that such beings occupy differentiated functional roles rather than being interchangeable projections. A specific earlier claim was that divine figures give more guidance (70–73%) and relatives act as gatekeepers (29.5% "told to return"; χ² = 41.13, p = 0.008). That claim could not be reproduced from any notebook, and the field it rested on no longer exists in the schema.

**Methods**: The analysis covers 6,751 NDE narratives from NDERF (n=5,659) and IANDS (n=1,092), coded by GPT-5.2 structured extraction. Functions are recorded per account, not per being. A function is therefore attributed to a being type only in accounts with one kind of being. Five exclusive groups are compared: divine or religious figure (n=418), unknown presence (n=610), angels (n=112), deceased relatives (n=584) and other beings (n=910). The tests are χ² with Holm correction, logistic regression adjusted for narrative length, a cross-validated classifier, and archive and religion interaction tests. Coding reliability was measured separately with a blind second coder (κ 0.70–0.88 for the fields used here).

**Results**: Ten of eleven functions differ across being types after Holm correction (Cramér's V 0.07–0.18). The function profile separates divine from relative encounters better than narrative length alone (cross-validated AUC 0.673, 95% CI 0.640–0.707, vs 0.555). Divine figures do not give more guidance overall (73.2% vs 75.9%; adjusted OR 0.81, 0.61–1.09). They teach six times as often (23.0% vs 4.5%; OR 6.27, 3.94–9.98), communicate telepathically more (OR 1.83) and commission missions more (OR 1.62). Relatives give mostly directional guidance (67.3%) and comfort (43.8%), and rarely teach (5.9%). Sending the experiencer back is common to all being types (47.0–54.6%) and not specific to relatives (OR 1.11, 0.86–1.43, p = 0.42).

**Conclusions**: The beings are functionally differentiated, and the clearest specialisation is teaching by divine figures. That differentiation is a **hit** for the framework's prediction. The specific figures previously cited are not reproducible. The gatekeeping prediction is a **miss**: sending back is a shared function, not a relative-specific role. The unknown presence is functionally close to divine figures, but so are angels and other beings.

**Keywords**: near-death experience, entity encounters, functional differentiation, deceased relatives, Being of Light, teaching, Swedenborg, logistic regression

---

## Data Provenance

| Item | Source | Access |
|-----------------------|----------------------------|----------------------------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `07_entity_function_differentiation.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/07_entity_function_differentiation.ipynb) |
| Reliability Analysis | `08_extraction_reliability.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/08_extraction_reliability.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

Encounters with other beings are among the most frequently reported elements of near-death experiences (Moody, 1975; Greyson, 1983). Experiencers describe deceased relatives and friends, religious figures, angels, and luminous or unseen presences they cannot identify (Osis & Haraldsson, 1977; Kelly, 2001). Most research has counted *who* is met. Less attention has gone to *what* each kind of being does: whether a grandmother and a figure identified as Jesus perform the same role under different names, or different roles.

The question matters for interpretation. If the beings are culturally shaped projections of one underlying process, they should be functionally interchangeable: what they do should not depend on who they are. If they are distinct agents, or distinct appearances of distinct functions, their roles should differ systematically.

### 1.2 Theoretical Framework

Swedenborg's account of the transition after death (*Heaven and Hell*, 1758) assigns different beings different tasks. Friends and relatives receive and accompany the newly arrived. Angels instruct. The Lord is present as the source of wisdom and love. The framework therefore predicts **functional differentiation**: beings should differ in what they do, and teaching should concentrate in higher-order beings. Under the framework's principle of "constant state, variable form", a presence that the experiencer cannot name should behave like the divine figure it may represent.

`CLAUDE.md` recorded this prediction as confirmed, with three specific numbers: divine figures give "more significant guidance (70–73%)", relatives serve as gatekeepers ("29.5% told to return"), and χ² = 41.13 (p = 0.008). None of these numbers is produced by any notebook in the repository, current or archived. The 2026-10 audit flagged the claim as unverified, and this report tests it.

### 1.3 Aims

1. **Test** whether being types differ in function (H1), using exclusive groups so that functions can be attributed.
2. **Quantify** whether divine or religious figures give more guidance, and more teaching in particular, than deceased relatives (H2).
3. **Examine** whether relatives comfort rather than teach (H3) and act as gatekeepers (H4).
4. **Assess** whether functional signatures are consistent across archives and religious backgrounds (H5).
5. **Locate** the unknown presence on the divine–relatives axis.

---

## 2. Methods

### 2.1 Data Sources

| Source | Records | Description |
|---------|---------|----------------------------|
| NDERF | 5,659 | Near-Death Experience Research Foundation online archive |
| IANDS | 1,092 | International Association for Near-Death Studies archive |
| **Total** | **6,751** | After removing two exact duplicate narratives |

All records were coded by GPT-5.2 into the questionnaire schema (`models/questionnaire.py`) and loaded through the verified loader `scripts/nde_dataset.py`, which checks every enum value against the schema.

### 2.2 Being-Type Groups

Guidance, communication and return are recorded for the account as a whole. A function can be attributed to a kind of being only when that kind is the only one in the account. Accounts were assigned to one exclusive group:

| Group | Criterion | n | % |
|--------------------------|----------------------------|---------|---------|
| Divine or religious figure | God, Jesus, Buddha or a specified religious figure; no other kind | 418 | 6.2% |
| Unknown presence | `unknown_presence` only | 610 | 9.0% |
| Angels | `angels` only | 112 | 1.7% |
| Deceased relatives | `deceased_relative_guide` or deceased relatives (named/unnamed) only | 584 | 8.7% |
| Other beings | `other` only | 910 | 13.5% |
| Mixed (excluded) | more than one kind | 1,224 | 18.1% |
| No beings (excluded) | none | 2,893 | 42.9% |

### 2.3 Function Variables

**Guidance**: guidance received (`yes` vs other); guidance types (teaching, life guidance, informational, comfort, directional).
**Communication**: telepathic communication (`telepathic` in `communication_modes`).
**Return**: told it is not their time (`not_your_time` in `return_reasons`); return decided by a being (`return_agency = external_being`); verbal limit (`boundary_encounter = verbal_limit`).
**Commissioning**: mission commissioned (`yes_explicit` or `implied`).

### 2.4 Statistical Analysis

- χ² tests of each function across the five groups (df = 4), with Cramér's V and Holm correction across the 11 functions
- Five-fold cross-validated logistic classifier of divine vs relative accounts from the 11 functions plus log word count, compared with log word count alone (AUC with bootstrap CI)
- Pairwise logistic regressions (divine vs relatives, unknown vs relatives, divine vs unknown) adjusted for log word count, because longer accounts mention more of everything; Holm correction within each contrast
- McNemar tests for paired comparisons of guidance types within relative accounts
- Interaction tests of the divine–relatives contrast with archive (NDERF/IANDS) and with religious background (Christian vs other stated), with Holm correction
- Coding reliability from a blind second coding of 100 random accounts (`08_extraction_reliability.ipynb`)

---

## 3. Results

### 3.1 Functions Differ Across Being Types (H1)

Ten of the eleven functions differ significantly across the five groups after Holm correction (χ² tests, df = 4). Effects are small to moderate; the largest is teaching.

| Function | Divine | Unknown | Angels | Relatives | Other | χ² | Holm p | V |
|-------------------------|---------|---------|---------|---------|---------|---------|---------|---------|
| Guidance received | 73.2% | 77.5% | 72.3% | 75.9% | 68.6% | 17.9 | 0.006 | 0.08 |
| Teaching | 23.0% | 17.5% | 20.5% | 4.5% | 13.6% | 81.1 | <0.0001 | 0.18 |
| Life guidance | 37.1% | 23.8% | 33.0% | 27.7% | 22.5% | 36.4 | <0.0001 | 0.12 |
| Informational guidance | 29.9% | 31.5% | 29.5% | 22.8% | 31.5% | 15.7 | 0.010 | 0.08 |
| Comfort | 29.4% | 28.7% | 33.9% | 33.2% | 24.9% | 13.7 | 0.017 | 0.07 |
| Directional guidance | 36.1% | 47.9% | 41.1% | 51.0% | 42.6% | 26.5 | 0.0002 | 0.10 |
| Told it is not their time | 30.4% | 28.5% | 25.9% | 37.7% | 28.5% | 18.1 | 0.006 | 0.08 |
| Return decided by a being | 39.2% | 36.1% | 36.6% | 46.7% | 35.5% | 21.9 | 0.001 | 0.09 |
| Verbal limit | 29.4% | 30.0% | 26.8% | 26.5% | 24.6% | 6.7 | 0.154 | 0.05 |
| Telepathic communication | 44.0% | 42.5% | 36.6% | 28.6% | 33.3% | 39.4 | <0.0001 | 0.12 |
| Mission commissioned | 35.4% | 27.7% | 31.2% | 24.0% | 25.2% | 20.1 | 0.003 | 0.09 |

A classifier using the eleven functions separates divine-only from relatives-only accounts with a cross-validated AUC of **0.673** (95% CI 0.640–0.707). Narrative length alone gives 0.555.

**Finding**: Being types are **functionally differentiated**. The separation is modest, and the groups overlap, but it is not produced by narrative length. Under a projection account the beings would be interchangeable, and this pattern is the opposite.

### 3.2 Divine Figures Teach; They Do Not Guide More Overall (H2)

Length-adjusted contrasts between divine-only and relatives-only accounts:

| Function | Divine | Relatives | Adjusted OR (95% CI) | Holm p |
|------------------------|---------|---------|--------------------|---------|
| Guidance received | 73.2% | 75.9% | 0.81 (0.61–1.09) | 0.16 |
| **Teaching** | **23.0%** | **4.5%** | **6.27 (3.94–9.98)** | **< 0.0001** |
| Telepathic communication | 44.0% | 28.6% | 1.83 (1.39–2.41) | 0.0001 |
| Mission commissioned | 35.4% | 24.0% | 1.62 (1.22–2.15) | 0.007 |
| Life guidance | 37.1% | 27.7% | 1.43 (1.09–1.88) | 0.075 |
| Informational guidance | 29.9% | 22.8% | 1.39 (1.05–1.86) | 0.12 |
| Directional guidance | 36.1% | 51.0% | 0.54 (0.42–0.70) | < 0.0001 |
| Comfort | 29.4% | 33.2% | 0.76 (0.57–1.00) | 0.16 |

Among accounts that state whether guidance was received, the rate is 82.0–91.0% in every group. Guidance as such does not distinguish the beings.

**Critical Finding**: Divine figures are **six times as likely to teach** as deceased relatives (adjusted OR 6.27). They are also more likely to communicate telepathically and to commission a mission. The difference is in the **kind** of guidance, not its amount. "More significant guidance (70–73%)" is not reproducible. "More teaching" is, strongly.

### 3.3 Relatives Direct and Comfort; They Rarely Teach (H3)

Within the 443 relatives-only accounts that report any guidance type:

| Guidance type | n | % (95% CI) |
|---------------|---|------------|
| Directional | 298 | 67.3% (62.8–71.5) |
| Comfort | 194 | 43.8% (39.2–48.4) |
| Life guidance | 162 | 36.6% (32.2–41.2) |
| Informational | 133 | 30.0% (25.9–34.4) |
| Teaching | 26 | 5.9% (4.0–8.5) |

Comfort exceeds teaching within the same accounts (paired McNemar p < 10⁻⁴⁰), and comfort exceeds life guidance (p = 0.027). Relatives do not comfort significantly more than divine figures do (33.2% vs 29.4%; OR 0.76, Holm p = 0.16). They do give more directional guidance (51.0% vs 36.1%).

**Finding**: Deceased relatives **orient and reassure**: they say where to go, what to do, and that all is well. They rarely instruct. The prediction "comfort rather than teaching" holds. "More comfort than divine figures" does not reach significance.

### 3.4 Sending Back Is Shared, Not a Relative Role (H4)

| Sent back (not-your-time, being decides return, or verbal limit) | n | % (95% CI) |
|----------------------------|---------|-----------------|
| Deceased relatives only | 319/584 | 54.6% (50.6–58.6) |
| Divine or religious figure only | 216/418 | 51.7% (46.9–56.4) |
| Unknown presence only | 298/610 | 48.9% (44.9–52.8) |
| Angels only | 53/112 | 47.3% (38.3–56.5) |
| Other beings only | 428/910 | 47.0% (43.8–50.3) |

Relatives vs divine figures: adjusted OR 1.11 (0.86–1.43), p = 0.42. Taken separately, relatives are told "not your time" (37.7% vs 30.4%) and have the return decided by a being (46.7% vs 39.2%) somewhat more often, but neither survives Holm correction (Holm p = 0.11 and 0.12). Against unknown-presence accounts, both return codes do differ after correction (adjusted OR 0.67 and 0.65 for unknown vs relatives).

**Finding**: Gatekeeping is a **shared function** of all being types (47–55% of accounts). It is not a role specific to relatives. The "29.5% told to return" figure cannot be reproduced from any current field. The gatekeeping prediction is a **miss** as stated.

### 3.5 Where the Unknown Presence Sits

A "divine-likeness" score from the classifier (0 = relatives-like, 1 = divine-like) places each group on the divine–relatives axis:

| Group | Mean score (95% CI) | n |
|-------|---------------------|---|
| Divine or religious figure | 0.481 (0.463–0.500) | 418 |
| Angels | 0.458 (0.424–0.492) | 112 |
| Unknown presence | 0.454 (0.441–0.468) | 610 |
| Other beings | 0.436 (0.425–0.447) | 910 |
| Deceased relatives | 0.370 (0.359–0.382) | 584 |

Unknown-presence accounts match divine accounts on telepathy (42.5% vs 44.0%), teaching (Holm p = 0.33) and all return codes. They differ on life guidance (OR 1.89 for divine, Holm p < 0.0001) and directional guidance (OR 0.61, Holm p = 0.002).

**Finding**: The unknown presence behaves **like a divine figure, not like a relative**. This is what "constant state, variable form" predicts. Angels and other beings sit just as close to the divine end, however. The closeness is therefore a property of non-relative beings in general, not a signature that identifies the unknown presence with the divine.

### 3.6 Consistency Across Archives and Religious Backgrounds (H5)

| Function | Adjusted OR, NDERF | Adjusted OR, IANDS | Archive interaction p | Religion interaction p |
|------------------------|------------------|------------------|---------------------|----------------------|
| Teaching | 5.90 | 8.46 | 0.58 | 0.48 |
| Telepathic communication | 2.02 | 1.06 | 0.074 | 0.19 |
| Mission commissioned | 1.64 | 1.38 | 0.63 | 0.66 |
| Directional guidance | 0.57 | 0.42 | 0.35 | 0.87 |

The direction of the divine–relatives difference agrees between archives for 9 of 11 functions, including all four significant overall. No archive or religion interaction survives Holm correction. Power is limited: IANDS contributes 171 divine or relatives accounts, and only 241 accounts state a religion (203 Christian).

**Finding**: The functional signature is **consistent where it can be tested**. The test cannot speak to non-Christian traditions.

### 3.7 Measurement Reliability of the Variables Used

A blind second coder recoded 100 random accounts (`08_extraction_reliability.ipynb`). Agreement for the fields used here:

| Variable | Cohen's κ (95% CI) |
|----------|--------------------|
| Guidance received | 0.88 (0.78–0.96) |
| Telepathic communication | 0.88 (0.76–0.98) |
| Deceased relatives | 0.85 (0.72–0.97) |
| Return decided by a being | 0.83 (0.70–0.93) |
| God or Jesus | 0.82 (0.65–0.96) |
| Mission commissioned | 0.71 (0.49–0.88) |
| Teaching | 0.70 (0.45–0.88) |
| Unknown presence | 0.44 (0.20–0.66) |
| Boundary type (among boundaries) | 0.34 |

**Finding**: The variables behind the main results are measured with substantial to almost perfect agreement. Teaching, divine and relative identification, telepathy and return agency all reach κ ≥ 0.70. Random coding error of this size weakens differences rather than creating them. Two variables are weaker. The unknown-presence group depends on an undefined boundary between `unknown_presence` and `other`. The verbal-limit code depends on which boundary type a coder chooses when a barrier and a spoken limit co-occur.

---

## 4. Discussion

### 4.1 Summary of Findings

1. Ten of 11 functions differ across five exclusive being types (Holm-corrected; V 0.07–0.18).
2. Functions separate divine from relative encounters beyond narrative length (AUC 0.673 vs 0.555).
3. Divine figures teach six times as often as relatives (23.0% vs 4.5%; OR 6.27). They also communicate telepathically more (OR 1.83) and commission missions more (OR 1.62). They do not give more guidance overall (OR 0.81).
4. Relatives give directional guidance (67.3%) and comfort (43.8%) and rarely teach (5.9%).
5. Sending back is common to all being types (47.0–54.6%) and is not relative-specific (OR 1.11, p = 0.42).
6. The unknown presence is functionally closer to divine figures than to relatives, as are angels and other beings.
7. The direction of differences is consistent across archives (9 of 11 functions).

### 4.2 Interpretation

| Framework prediction | Observed pattern | Verdict |
|----------------------------|----------------------------|-------------------|
| Beings occupy differentiated roles | 10/11 functions differ; AUC 0.673 | **Hit** (modest effect) |
| Higher-order beings teach | Teaching OR 6.27 for divine vs relatives | **Hit** |
| Higher-order beings give more guidance overall | 73.2% vs 75.9%, OR 0.81 | **Miss** |
| Relatives receive and comfort rather than instruct | Directional 67.3%, comfort 43.8%, teaching 5.9% | **Hit** |
| Relatives act as gatekeepers | Sent back 54.6% vs 47.0–51.7% in other groups; not significant vs divine | **Miss** |
| Unknown presence = divine reality in variable form | Closer to divine than to relatives, but not distinguishable from angels or other beings | **Underdetermined** |
| Signatures stable across contexts | Same direction in both archives; no significant interaction | **Hit** where testable |

The pattern fits a division of labour in which teaching is concentrated in beings identified as divine and orientation is concentrated in relatives. The framework predicts this. A model of interchangeable projections does not: under it, who the being is should not predict what it does. Two parts of the earlier claim do not survive testing. Divine figures do not give *more* guidance, and gatekeeping is not a relatives' role. Swedenborg's own description has relatives receiving and accompanying the newly arrived, not deciding their return. The "gatekeeper" prediction may therefore have been an over-specification added later rather than a consequence of the framework.

These are associations between codes of the same narrative. They show that experiencers *report* beings of different kinds doing different things. Whether the reports reflect real agents (ontology) is a separate question that these data cannot settle.

### 4.3 Implications

1. The entity-function entry in `CLAUDE.md` should be replaced by these results: differentiation and teaching specialisation confirmed; guidance-amount and gatekeeping predictions not confirmed.
2. Future schema versions should record guidance, communication and return **per being**, so that the 1,224 mixed accounts can be used and attribution does not depend on single-type accounts.
3. The `unknown_presence` vs `other` boundary needs a definition before the unknown presence can be studied as a group.

### 4.4 Limitations

1. **Attribution by exclusion.** Functions are attributed only in single-type accounts (2,634 of 6,751). Mixed accounts may differ systematically.
2. **Model-coded data.** All variables are GPT-5.2 codes. Reliability is substantial for most fields but moderate for the unknown presence (κ 0.44).
3. **Small effects.** Cramér's V is at most 0.18, and the classifier separates the groups only modestly.
4. **Self-selected archives.** NDERF and IANDS accounts are volunteered and predominantly Western; religion is stated in a minority of accounts.
5. **Duplicates.** About 1.8% of records are near-duplicate submissions; removing them changes headline rates by less than 0.5 percentage points.

### 4.5 Future Directions

1. Re-extract with per-being function fields and re-test H1–H4 including mixed accounts.
2. Define the unknown-presence category and re-test its position on the divine–relatives axis.
3. Test differentiation within non-Christian accounts once adequate samples exist.
4. Examine whether teaching content differs by being type (what is taught, not only whether).

---

## 5. Conclusion

In 6,751 near-death experiences, the beings encountered are functionally differentiated. The sharpest difference is teaching: divine or religious figures teach in 23.0% of single-type accounts and deceased relatives in 4.5% (length-adjusted OR 6.27, 95% CI 3.94–9.98). Relatives orient and reassure. The framework predicted this differentiation, and it is a hit.

Two specific claims recorded earlier do not hold. Divine figures do not provide more guidance overall, and sending the experiencer back is a function shared by every kind of being rather than a role of relatives. The numbers once cited for this prediction (70–73%, 29.5%, χ² = 41.13) are not reproducible and should not be used.

---

## References

Greyson, B. (1983). The near-death experience scale: Construction, reliability, and validity. *Journal of Nervous and Mental Disease*, 171(6), 369–375.

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.

Kelly, E. W. (2001). Near-death experiences with reports of meeting deceased people. *Death Studies*, 25(3), 229–249.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Osis, K., & Haraldsson, E. (1977). *At the Hour of Death*. Avon Books.

Swedenborg, E. (1758). *Heaven and Hell* (De Caelo et Ejus Mirabilibus et de Inferno). London.

---

## Appendix A: Statistical Summary

| Test | Statistic | Result |
|----------------------------|----------------------------|---------------------------|
| Teaching × being type | χ² = 81.1, df = 4 | p < 0.0001, V = 0.18 |
| Telepathic communication × being type | χ² = 39.4, df = 4 | p < 0.0001, V = 0.12 |
| Life guidance × being type | χ² = 36.4, df = 4 | p < 0.0001, V = 0.12 |
| Verbal limit × being type | χ² = 6.7, df = 4 | p = 0.154 |
| Divine vs relatives classifier | AUC 0.673 (0.640–0.707) | Length only 0.555 |
| Teaching, divine vs relatives | Adjusted OR 6.27 (3.94–9.98) | Holm p < 0.0001 |
| Guidance received, divine vs relatives | Adjusted OR 0.81 (0.61–1.09) | Holm p = 0.16 |
| Sent back, relatives vs divine | Adjusted OR 1.11 (0.86–1.43) | p = 0.42 |
| Comfort vs teaching within relatives | McNemar | p < 10⁻⁴⁰ |
| Archive / religion interactions | 11 functions each | none significant after Holm |

## Appendix B: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **Analysis Notebook**: [07_entity_function_differentiation.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/07_entity_function_differentiation.ipynb)
- **Reliability Notebook**: [08_extraction_reliability.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/08_extraction_reliability.ipynb)
- **Figure**: `output/07_entity_functions.png` (generated by the notebook)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
