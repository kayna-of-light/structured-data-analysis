# Sequential Structure in Near-Death Experience: Evaluating the Normative Path Model

> **Correction notice (2026-10-05).** This report was revised after a statistical audit (`docs/STATISTICAL_AUDIT_2026-10.md`). Changes: (1) the sequence data the title refers to had never been analysed; they are now reported, and a fixed canonical order is essentially absent; (2) the life-review "15.9:1 loving:harsh" mixed life reviews with judgments recorded outside life reviews and used all 6,753 records as denominator — within life reviews the ratio is 36.2:1 but loving:critical is 1.7:1; (3) several percentages were computed on the wrong denominator (e.g. judgment sources as % of all NDEs); (4) the "four markers support" conclusion relied on criteria that could not fail; markers are now classified by what they can and cannot test; (5) agency × willingness χ² was inflated by co-missing data (4,824.8 → 1,389.0 without "not mentioned"); (6) N is 6,751 after removing two duplicate narratives, and four IANDS records previously mislabelled as NDERF are corrected. The LaTeX and PDF versions were regenerated from this corrected text.

## Abstract

Near-death experiences are often described as following a characteristic sequence — passage, arrival in light, encounters, life review, return. The Swedenborgian framework proposes a normative path in which most souls continue in the spiritual world, with reincarnation an exception. We analysed 6,751 NDE records from NDERF (n=5,659) and IANDS (n=1,092), coded with GPT-5.2 structured extraction, for return patterns, encounters with deceased relatives, identity, life review, reincarnation indicators, transformation, and adherence to a canonical stage order.

Among accounts stating who decided the return, 70.1% did not return by their own choice (95% CI 68.8–71.4); among those stating their attitude, 49.4% were reluctant. Deceased relatives appeared in 17.9% of NDEs; identity was described as clear in 97.0% of accounts addressing it. Reincarnation content was rare: past-life memory 4.4%, intermission memory 1.0%, pre-incarnation covenant 1.3%. Life reviews occurred in 17.5%; within them, harsh evaluation was rare (1.4% of rated reviews) but uncomfortable evaluation common (28.0%). Strict adherence to the canonical stage order occurred in 3 of 6,249 assessable accounts (0.05%); 37.7% followed it mostly and 54.3% partially.

The data are consistent with several descriptive expectations of a continuation model — a valued state, encounters with the dead, preserved identity, rare reincarnation content, non-condemning review — but most of these markers do not discriminate between continuation and competing accounts. The one structural prediction that could fail, a characteristic sequence, is only weakly present.

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,659) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,092) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Analysis Code | `02_normative_path_validation.ipynb` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb) |
| Data loader | `scripts/nde_dataset.py` | Repository |
| Structured Data | `structured/*.json` | [Repository](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured/) (6,753 files; 6,751 unique narratives) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

Near-death experiences feature recognizable elements: out-of-body experiences, tunnel passage, light encounters, meetings with deceased relatives, life reviews and return decisions (Moody, 1975; Ring, 1980; Greyson, 2003). Ring's original work described a five-stage progression. Whether such structure is inherent to the experience or imposed in retrospective narration remains debated.

### 1.2 Theoretical Framework

Swedenborg (1758) described a post-mortem journey through a "World of Spirits" in stages — an external stage, an internal stage of self-revelation, and instruction — culminating in a community matching the person's ruling love. Continuation is normative; reincarnation, where it occurs, is an exception (restorative healing after traumatic death, or a volunteered mission). NDE return to one's current body is distinct from reincarnation.

Predictions examined: experiencers who glimpse the spiritual state should value it (reluctance to return); deceased relatives should be encountered; reincarnation content should be uncommon; identity should persist; the life review should reveal rather than condemn; and the experience should show a characteristic sequence.

### 1.3 Aims and What Can Be Tested

Every member of the dataset returned and all data are retrospective self-reports. The analyses therefore describe return, encounter, identity and review phenomenology and assess whether each is consistent with the framework — and whether a competing model would predict something different. A marker that any model predicts equally is reported as *consistent, not a test*.

---

## 2. Methods

### 2.1 Data Sources

NDERF (5,659 records) and IANDS (1,092 records); two duplicate narratives counted once (N = 6,751). Source is taken from the records' `dataset` field.

### 2.2 Fields

Return agency (self, external_being, involuntary, mutual) and willingness (willing, reluctant, mixed, neutral); return reasons (multi-select: earthly mission, family responsibility, not your time, unfinished business, other); deceased relatives; identity continuity; reincarnation and pre-birth indicators (explicit or implied); life review occurrence, judgment source, judgment intensity and experiencer emotional tone; before/after death fear, spirituality and religiosity; and stage-sequence fields (`canonical_sequence`: strict / mostly / partial / radical; repeated and simultaneous stages).

### 2.3 Statistical Analysis

Proportions with Wilson 95% CIs and stated denominators ("not mentioned" excluded where indicated). χ² tests with expected-count checks and Cramér's V; Wilcoxon signed-rank tests for before/after changes on 5-level scales; exact binomial CIs for ratios.

---

## 3. Results

### 3.1 Return Agency and Willingness

| Return agency | n | % of stated (n = 4,781) |
|---|---|---|
| External being | 1,930 | 40.4% |
| Involuntary | 1,422 | 29.7% |
| Self | 1,124 | 23.5% |
| Mutual | 305 | 6.4% |
| Not mentioned | 1,970 | — |

70.1% (95% CI 68.8–71.4) of stated returns were not self-chosen. Of 3,563 accounts stating an attitude, 49.4% were reluctant, 26.5% mixed, 21.4% willing and 2.7% neutral.

Agency and willingness are strongly associated among accounts stating both (n = 3,330; χ² = 1,389.0, df = 9, p < 10⁻²⁹⁰, Cramér's V = 0.37). Of those sent back by a being, 73.3% were reluctant and 6.0% willing; of those who chose to return, 53.2% were willing and 10.4% reluctant. (The previously reported χ² = 4,824.8 included "not mentioned" categories; 1,737 records lack both.)

**Finding:** most stated returns were not self-chosen, and reluctance is common. *Interpretation:* reluctance shows the NDE state was valued; it is consistent with the framework but would also follow from any intensely pleasant altered state, so it does not discriminate between models. "Return as exception" is untestable because everyone in the dataset returned.

### 3.2 Return Reasons

Not your time 21.6%, family responsibility 17.2%, unfinished business 10.5%, earthly mission 9.2%, other 3.2% (of all NDEs; 44.3% gave at least one reason). The schema has no "personal preference" category, so the earlier statement that "duty and obligation rather than preference drive return" cannot be tested from this field; 557 experiencers both chose to return and were willing.

### 3.3 Deceased Relatives

Deceased relatives were encountered in 1,206 NDEs: 17.9% of all (95% CI 17.0–18.8) and 22.6% of accounts that address the question (named 1,007, unnamed 199).

**Finding:** consistent with continuation, **not a test.** The data contain no measure of how long relatives had been dead, and several reincarnation doctrines also allow encounters with the recently dead in an intermediate state, so no competing quantitative prediction is available.

### 3.4 Identity

Identity was described as clear in 4,376 of 4,511 accounts addressing it (97.0%, 95% CI 96.5–97.5); altered or lost in 92 and confused in 43.

**Finding:** strongly consistent with persistence of identity, but preserved selfhood is also predicted by non-survival accounts of NDE phenomenology; it does not discriminate between them.

### 3.5 Reincarnation Indicators

| Indicator (explicit or implied) | n | % of all | 95% CI | % of accounts addressing it |
|---|---|---|---|---|
| Premortal existence information | 478 | 7.1% | 6.5–7.7 | 9.5% |
| Past-life memory | 297 | 4.4% | 3.9–4.9 | 6.2% |
| Chose mission | 140 | 2.1% | 1.8–2.4 | 3.0% |
| Pre-birth realm description | 120 | 1.8% | 1.5–2.1 | 2.6% |
| Pre-incarnation covenant | 86 | 1.3% | 1.0–1.6 | 1.9% |
| Chose life circumstances | 82 | 1.2% | 1.0–1.5 | 1.8% |
| Intermission memory | 69 | 1.0% | 0.8–1.3 | 1.6% |
| Chose parents | 29 | 0.4% | 0.3–0.6 | 0.6% |

(Earlier figures of 1.4% for chose mission and 0.1% for chose parents counted only "implied" responses.) Memory of a prior death appears in 36 accounts (19 violent).

**Finding:** reincarnation content is **rarely reported** in NDEs. This is consistent with reincarnation as an exception but **not a test** of it: absence of a report during a brief NDE is not evidence of absence of prior lives, and no competing model predicts a specific higher rate. The earlier rule "supported if below 10%" could not fail.

### 3.6 Life Review

Life reviews occurred in 1,183 NDEs (17.5%, 95% CI 16.6–18.4; brief 718, extensive 465).

**Evaluator** (928 reviews with stated source): none 53.1%, guide or entity 19.9%, Being of Light 15.9%, self 10.2%, deceased relative 0.8%. About a third (36.6%) involved an external evaluator. (The earlier report gave these as percentages of all 6,753 records, including records without a life review.)

**Character** (428 rated reviews): loving/gentle 50.7% (95% CI 46.0–55.4), neutral 19.9%, uncomfortable 28.0% (24.0–32.5), harsh/condemning 1.4% (0.6–3.0). Loving : harsh = 36.2 : 1 (95% CI 16.3–99.6); loving : (uncomfortable + harsh) = 1.72 : 1. Judgment fields are also filled for 26 records without a life review (8 of them harsh); the earlier 15.9 : 1 (223 : 14) mixed both groups.

**Empathetic perspective** (feeling others' emotions): 18.0% of life reviews (previously reported as 2.9% of all NDEs). **Experiencer tone:** mixed is most common; love (163) and shame/regret (169) are about equally frequent.

**Finding:** the life review is predominantly **non-condemning** (harsh ≈ 1%), in line with Swedenborg's description of self-revelation rather than punishment. It is not uniformly loving: more than a quarter of rated evaluations are uncomfortable, and experiencers feel regret as often as love.

### 3.7 Transformation

Where both levels are stated: death fear fell in 84.7% and rose in 4.0% (n = 327; mean 2.43 → 0.31 on 0–4; Wilcoxon p < 10⁻⁴⁵); spirituality rose in 83.7% and fell in 1.7% (n = 723; p < 10⁻¹⁰⁰); religiosity rose in 20.2% and fell in 19.9% (n = 1,168; p = 0.58). Death fear "after" is stated in 1,402 accounts but "before" in only 569, so the pairs are selected toward people whose fear changed.

### 3.8 Sequential Structure

| Canonical stage order | n | % of assessable (n = 6,249) |
|---|---|---|
| Strict | 3 | 0.05% |
| Mostly | 2,356 | 37.7% |
| Partial | 3,396 | 54.3% |
| Radical departure | 494 | 7.9% |

Stages were repeated in 23.1% and simultaneous in 43.8% of accounts addressing these questions. Stage elements present: return decision 83.5%, OBE 65.6%, environment 56.8%, light 55.8%, communication 54.9%, boundary 40.6%, tunnel 32.9%, loved ones 21.4%, life review 15.2%.

**Finding:** NDE elements recur as a recognisable *set*, but not in a fixed *sequence*. A strict temporal ordering is **not supported**. Whether this counts against the 4-stage model depends on whether the stages are read as a strict temporal order (miss) or as functional phases that may overlap (underdetermined).

---

## 4. Discussion

### 4.1 Evidence Assessment

| Marker | Corrected value | What it can show | Assessment |
|---|---|---|---|
| Return not self-chosen | 70.1% of stated | Everyone returned; "exception" untestable | Consistent, not a test |
| Reluctance to return | 49.4% of stated | State was valued; not model-discriminating | Consistent, not a test |
| Deceased relatives | 17.9% | No competing quantitative prediction | Consistent, not a test |
| Identity preserved | 97.0% of stated | Predicted by most models | Consistent |
| Reincarnation content rare | 1–4% | Absence of report ≠ absence of prior life | Consistent, not a test |
| Life review non-condemning | Harsh 1.4%, uncomfortable 28.0% | Framework predicts revelation over condemnation | **Supported** (harsh rare); "loving" overstated |
| Canonical sequence | Strict 0.05%, mostly 37.7% | Could have failed | **Not supported** as a strict order |

### 4.2 The Threefold Path Framework

The data are compatible with a normative path of continuation with rare exceptions, in the sense that reincarnation and pre-birth content are uncommon (1–7%). They cannot establish the relative frequencies of the three paths: NDE reports describe what is experienced during a brief episode, not soul histories. The 4.4% reporting past-life memory and the 1–2% reporting pre-incarnation choices are rates of *reported content*, not estimates of how many experiencers are on restorative or volunteer paths.

### 4.3 The World of Spirits as Transition Zone

NDE phenomenology shares several features with Swedenborg's account of the World of Spirits: encounters with the dead, preserved identity, a self-revealing review that is rarely condemning, and instruction or guidance. These parallels are real in the data. Two cautions: the parallels are mostly with features that many afterlife models share, and the canonical ordering that would mark a structured passage through stages is weak.

### 4.4 Clinical Implications

The low rate of harsh evaluation in life reviews (≈1%) may be reassuring to people who fear judgment at death. Clinicians should also know that uncomfortable evaluation and feelings of regret are common parts of the life review, and that experiencers who were sent back against their wishes frequently report reluctance — validating both aspects supports integration.

### 4.5 Limitations

Self-selected online archives; LLM extraction without human validation; retrospective reports; many fields "not mentioned"; before/after pairs selected toward change; predominantly Western sample (country stated for 12%).

### 4.6 Future Directions

Pre-registered, discriminating predictions (e.g. what a reincarnation-normative model would predict about deceased-relative encounters as a function of time since death); human-validated coding of stage order; and comparison with prospective clinical NDE samples.

---

## 5. Conclusion

Across 6,751 near-death experiences, return is usually not self-chosen and often reluctant, deceased relatives appear in about one in six accounts, identity is preserved, reincarnation content is rare, and the life review is predominantly non-condemning though often uncomfortable. These findings are consistent with a continuation model of the post-mortem path, but most do not discriminate it from alternatives. The characteristic sequence implied by a staged journey is weak: strict canonical order is essentially absent. The earlier conclusion of "convergent support" from "four markers" overstated what these data can show.

---

## References

Greyson, B. (2003). Incidence and correlates of near-death experiences in a cardiac care unit. *General Hospital Psychiatry*, 25(4), 269–276.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Ring, K. (1980). *Life at Death: A Scientific Investigation of the Near-Death Experience*. Coward, McCann & Geoghegan.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value |
|------|-----------|----|---------|
| Agency × willingness (both stated) | χ² = 1,389.0, V = 0.37 | 9 | < 10⁻²⁹⁰ |
| Death fear before vs after | Wilcoxon W = 1,148 (n = 327) | — | < 10⁻⁴⁵ |
| Spirituality before vs after | Wilcoxon W = 2,198 (n = 723) | — | < 10⁻¹⁰⁰ |
| Religiosity before vs after | Wilcoxon W = 53,538 (n = 1,168) | — | 0.58 |
| Life review loving : harsh | 217 : 6 = 36.2 : 1 (95% CI 16.3–99.6) | — | — |
| Life review loving : critical | 217 : 126 = 1.72 : 1 | — | — |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,751 |
| Return not self-chosen (of stated) | 70.1% |
| Reluctant to return (of stated) | 49.4% |
| Deceased relatives present | 17.9% |
| Identity clear (of stated) | 97.0% |
| Past-life memory | 4.4% |
| Pre-incarnation covenant | 1.3% |
| Life review occurred | 17.5% |
| Harsh / uncomfortable evaluation (rated reviews) | 1.4% / 28.0% |
| Strict / mostly canonical sequence | 0.05% / 37.7% |

## Appendix C: Data Access

- **Repository**: [https://github.com/kayna-of-light/structured-data-analysis](https://github.com/kayna-of-light/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebook**: [02_normative_path_validation.ipynb](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/02_normative_path_validation.ipynb)
- **Audit**: `projects/nde/docs/STATISTICAL_AUDIT_2026-10.md`
