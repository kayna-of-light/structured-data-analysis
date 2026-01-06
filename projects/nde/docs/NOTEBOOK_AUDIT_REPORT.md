# NDE Analysis Notebooks - Field Mapping Audit Report

**Date:** January 5, 2026  
**Purpose:** Verify that analysis notebooks are using correct schema fields and measuring what they claim to measure

---

## Executive Summary

After reviewing the analysis notebooks against the questionnaire schema and spot-checking extracted data, I identified several issues of varying severity:

| Category | Status | Impact |
|----------|--------|--------|
| **Life Review Judgment Source** | ✅ CORRECT | Core 84.8% stat is valid |
| **Life Review Emotional Tone** | ⚠️ MISINTERPRETED | Conflates feeling with judgment source |
| **Field Name Mappings** | ✅ CORRECT | Notebooks use correct paths |
| **Love:Shame Ratio (3.4:1)** | ⚠️ MISLEADING | Measures emotional response, not judgment source |

---

## Issue #1: Love:Shame Ratio Conflates Two Distinct Questions

### The Problem

The framework makes two distinct claims:
1. **84.8% experience no external condemnation** ← Measures WHO judges (judgment source)
2. **3.4:1 love:shame ratio** ← Measures HOW experiencer FEELS (emotional tone)

These are **different questions** being conflated:

| Question | Schema Field | What It Measures |
|----------|--------------|------------------|
| Who judges? | `life_review.judgment` | Source of judgment (self/guide/none) |
| How do they feel? | `life_review.emotional_tone` | Experiencer's emotional response |

### Evidence from Spot-Check

From our 10-case extraction test:

| Case | Judgment Source | Emotional Tone | Interpretation |
|------|-----------------|----------------|----------------|
| Elsa (00660) | `guide_or_light` | `shame_or_regret` | Being showed → she felt shame |
| John (00615) | `self_judgment` | `shame_or_regret` | He judged himself → felt shame |
| Carolle (00449) | `none` | `love` | No judgment → felt love |
| Hiker | `none` | `love` | No judgment → felt love |

**Key insight:** When there's NO judgment, tone is LOVE. When there IS judgment (self OR external), tone is SHAME.

### The Research Question Conflation

The framework document asks: "Do people experience judgment FROM the Being of Light or do they judge THEMSELVES?"

- **84.8% statistic** answers this correctly ✅
- **3.4:1 ratio** answers a different question (emotional response) ❌

### Impact

The 3.4:1 ratio is valid data but **doesn't measure what the research question asks**. It measures whether people FEEL love vs shame, not WHETHER the Being judges them.

### Recommendation

1. Keep the 84.8% stat as the primary answer to "external vs self judgment"
2. Reframe 3.4:1 ratio as "emotional experience during life review"
3. Add cross-tabulation: judgment source × emotional tone to show the CORRELATION
4. The pattern "no judgment → love, self-judgment → shame" is the real finding

---

## Issue #2: Statistical Definitions Need Clarification

### The 84.8% Calculation

The report says: **84.8% = none (57.0%) + self-judgment (26.3%)**

But looking at the actual enum values in `questionnaire.py`:

```python
class ReviewJudgment(str, Enum):
    GUIDE_OR_LIGHT = "guide_or_light"  # Being judges
    SELF = "self_judgment"              # Person judges themselves
    NONE = "none"                       # No judgment at all
    NOT_MENTIONED = "not_mentioned"     # Unclear
```

The calculation should exclude `not_mentioned` from the denominator:
- If 5.9% are `not_mentioned`, the base is 94.1% of reviews
- 84.8% / 94.1% = **90.1%** of *classifiable* cases have no external condemnation

### Recommendation

Be explicit: "Of life reviews where judgment source could be determined (n=X), Y% had no external condemnation"

---

## Issue #3: Emotional Tone Categories May Be Under-Discriminating

### The Schema

```python
class ReviewEmotionalTone(str, Enum):
    LOVE = "love"
    NEUTRAL = "neutral"
    SHAME_OR_REGRET = "shame_or_regret"
    MIXED = "mixed"
    NOT_SPECIFIED = "not_specified"
```

### Problem: "Mixed" is Ambiguous

From the 6,739 case analysis:
- Mixed: **45.0%** (564 cases) - the largest category!

"Mixed" could mean:
- Both love AND shame (complex experience)
- Neither strongly (moderate experience)
- Varies throughout review (temporal mixing)

### Impact on 3.4:1 Ratio

If 45% are "mixed," the love:shame ratio only represents ~30% of cases. The ratio is:
- Love: 26.8% (336)
- Shame: 7.8% (98)
- Mixed: 45.0% (564) ← What is this?

### Recommendation

1. Re-examine "mixed" cases to understand what they represent
2. Consider whether "mixed" should contribute to both love and shame counts
3. Report ratios with and without mixed category

---

## Issue #4: Field Path Verification ✅ CORRECT

The notebooks correctly access fields:

| Notebook Access | Schema Path | Status |
|-----------------|-------------|--------|
| `review.get('occurrence')` | `life_review.occurrence` | ✅ |
| `review.get('judgment')` | `life_review.judgment` | ✅ |
| `review.get('emotional_tone')` | `life_review.emotional_tone` | ✅ |
| `review.get('perspective_of_others')` | `life_review.perspective_of_others` | ✅ |

Previous versions had `life_review_occurred` which was incorrect, but this was fixed.

---

## Issue #5: Volunteer Discriminant Analysis - Appropriate Fields

The `volunteer_discriminant_analysis.ipynb` uses:

| Field | Purpose | Appropriate? |
|-------|---------|--------------|
| `return_reason` | Discriminate volunteer vs restorative | ✅ Yes |
| `mission_commissioned` | Identify commissioning moments | ✅ Yes |
| `volunteer_language` | Direct volunteer mentions | ✅ Yes |
| `death_memory` | Restorative indicator | ✅ Yes |
| `past_life_memory` | Restorative indicator | ✅ Yes |

**Assessment:** This notebook appears correctly designed.

---

## Issue #6: Being of Light vs Other Beings Distinction

The `light_being_analysis.ipynb` correctly distinguishes:

```python
light_being_ids = {'god', 'jesus', 'religious_figure_specified', 'buddha', 'muhammad', 'unknown_presence'}
other_being_ids = {'deceased_relative_guide', 'angels', 'multiple_beings', 'other'}
```

**Assessment:** This distinction is well-designed and implemented.

---

## Recommended Actions

### Immediate

1. **Re-run analysis with cross-tabulation** of judgment source × emotional tone
2. **Update framework documents** to clarify what each metric measures
3. **Add caveat** to 3.4:1 ratio about what it does/doesn't measure

### Medium-term

1. **Investigate "mixed" emotional tone** cases to improve categorization
2. **Add confidence intervals** to key statistics
3. **Consider adding field** for "intensity" of judgment/emotional experience

### Documentation

1. Add methodology notes explaining the distinction between:
   - Judgment SOURCE (who judges)
   - Judgment OUTCOME (what they find)
   - Emotional RESPONSE (how they feel)

---

## Appendix: Key Schema Reference

### LifeReviewSection Fields

```python
class LifeReviewSection(QuestionnaireBaseModel):
    occurrence: LifeReviewOccurrence    # extensive/brief/no/not_mentioned
    presentation: LifeReviewPresentation # panoramic/sequential/reexperience/mixed
    perspective_of_others: MentionResponse # yes_explicit/implied/no/not_mentioned
    judgment: ReviewJudgment            # guide_or_light/self_judgment/none/not_mentioned
    emotional_tone: ReviewEmotionalTone # love/neutral/shame_or_regret/mixed/not_specified
```

### Critical Distinction

| Metric | Field | Research Question |
|--------|-------|-------------------|
| 84.8% no external condemnation | `judgment` | Does the Being judge? |
| 3.4:1 love:shame ratio | `emotional_tone` | How does the person FEEL? |

These answer **different questions**. Both are valid, but should not be conflated.
