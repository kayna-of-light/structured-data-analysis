# NDE Questionnaire Schema Changes Report

**Date**: January 6, 2026  
**Purpose**: Document schema improvements for future analysis comparison

---

## Executive Summary

This report documents comprehensive schema improvements made to the NDE extraction questionnaire. The changes address **7 major categories** of issues:

1. **Temporal Conflation** — Fields that mixed "before" and "after" states
2. **Composite Fields** — Single fields capturing multiple independent concepts
3. **List vs. Scalar Conversion** — Fields that should allow multiple values
4. **Enum Refinement** — Improved categorization with clearer semantics
5. **New Granularity** — Additional detail capture (e.g., Christian denominations)
6. **Docstring Enhancement** — Clearer extraction guidance for the model
7. **Bias Correction** — Removed implicit value judgments from definitions

---

## Change Categories

### 1. Temporal Conflation Fixes (HIGH PRIORITY)

These changes split "change" indicators into explicit "before" and "after" measurements, enabling proper baseline analysis.

#### 1.1 Death Fear
| Before | After |
|--------|-------|
| `BeliefChange` enum (no_fear, some_fear, no_change) | `DeathFearLevel` enum with `death_fear_before` + `death_fear_after` fields |

**New Enum Values**: `none`, `minimal`, `moderate`, `significant`, `severe`, `not_mentioned`

**Rationale**: The old enum only captured change direction, not magnitude. We now capture actual fear levels at both timepoints.

#### 1.2 Spirituality
| Before | After |
|--------|-------|
| `SpiritualityShift` enum (more_spiritual, more_religious, etc.) | `SpiritualityLevel` enum with `spirituality_before` + `spirituality_after` fields |

**New Enum Values**: `none`, `low`, `moderate`, `high`, `central`, `not_mentioned`

**Rationale**: The old enum conflated spirituality and religiosity AND only captured direction. Now we can measure:
- Actual spirituality level at both timepoints
- Independent of religiosity

#### 1.3 Religiosity (NEW)
| Before | After |
|--------|-------|
| (conflated with spirituality) | `ReligiosityLevel` enum with `religiosity_before` + `religiosity_after` fields |

**New Enum Values**: `none`, `low`, `moderate`, `high`, `devout`, `not_mentioned`

**Rationale**: Spirituality (internal/personal) and religiosity (external/institutional) are orthogonal dimensions. A pastor may have high religiosity but decrease it while increasing spirituality after NDE.

#### 1.4 Age Fields
| Before | After |
|--------|-------|
| `age_reported: bool`, `age_years: Optional[int]` | `age_at_nde_reported: bool`, `age_at_nde: Optional[int]`, `years_since_nde: Optional[int]` |

**Rationale**: Clarifies that age refers to NDE timing, adds elapsed time since NDE for retrospective bias analysis.

#### 1.5 Religious Affiliation
| Before | After |
|--------|-------|
| `religious_affiliation: ReligiousAffiliation` | `religious_background` + `religious_belief_at_nde` (both ReligiousAffiliation) |

**Rationale**: Someone raised Catholic may be atheist at time of NDE. These are different analytical questions.

---

### 2. Composite Field Splits (HIGH PRIORITY)

Fields that captured multiple independent concepts now have separate fields.

#### 2.1 Judgment Analysis (Life Review)
| Before | After |
|--------|-------|
| `ReviewJudgment` (guide_or_light, self_judgment, harsh_punishing, none) | `JudgmentSource` + `JudgmentIntensity` + `ReviewEmotionalTone` |

**New Structure**:
- `JudgmentSource`: WHO judged (self, being_of_light, guide_or_entity, deceased_relative, none)
- `JudgmentIntensity`: HOW severe (loving_gentle, neutral, uncomfortable, harsh_condemning)
- `ReviewEmotionalTone`: EXPERIENCER'S feelings (love, neutral, shame_or_regret, mixed)

**Rationale**: The old field conflated source and intensity. Self-judgment can be loving or harsh. Being of Light judgment is usually loving. These are independent dimensions.

#### 2.2 Return Decision
| Before | After |
|--------|-------|
| `ReturnChoice` (chose_to_return, reluctant_return, told_to_return, involuntary) | `ReturnAgency` + `ReturnWillingness` |

**New Structure**:
- `ReturnAgency`: WHO decided (self, external_being, mutual, involuntary)
- `ReturnWillingness`: ATTITUDE toward returning (willing, reluctant, neutral, mixed)

**Rationale**: Agency and willingness are independent. Someone told to return (external agency) may be willing or reluctant. Someone who chose to return (self agency) may still be reluctant.

#### 2.3 Belief Consistency
| Before | After |
|--------|-------|
| `BeliefConsistency` (consistent, inconsistent, partially_consistent, no_prior_beliefs) | `DoctrineConsistency` + `PersonalExpectationConsistency` |

**New Structure**:
- `DoctrineConsistency`: Alignment with OFFICIAL religious teachings
- `PersonalExpectationConsistency`: Alignment with PERSONAL expectations (may differ from doctrine)

**Rationale**: A Catholic might personally expect universal acceptance even though doctrine teaches purgatory. These are different analytical questions for cultural influence analysis.

#### 2.4 Incarnation Choice
| Before | After |
|--------|-------|
| `IncarnationChoiceType` (chose_parents, chose_mission, chose_both) | `chose_parents`, `chose_mission`, `chose_life_circumstances` (all MentionResponse) |

**Rationale**: These are independent binary questions. Someone might mention choosing parents but not mission.

#### 2.5 Future Knowledge
| Before | After |
|--------|-------|
| `FutureKnowledgeType` (personal_future, global_future, both) | `personal_future_knowledge`, `global_future_knowledge` (both MentionResponse) |

**Rationale**: Same pattern — independent binary questions.

#### 2.6 Soul Age / Incarnation History
| Before | After |
|--------|-------|
| `SoulAgeType` (old_soul, new_soul, first_incarnation, many_lives) | `SoulAgeCharacterization` + `IncarnationHistory` |

**New Structure**:
- `SoulAgeCharacterization`: old_soul, new_soul, not_mentioned
- `IncarnationHistory`: first_incarnation, few_lives, many_lives, not_mentioned

**Rationale**: Soul age characterization (how described) vs incarnation count (how many lives) are independent.

---

### 3. List vs. Scalar Conversions (MEDIUM PRIORITY)

Fields where multiple values can co-occur now use List types.

| Field | Before | After |
|-------|--------|-------|
| `light_encounter` | `List[LightEncounter]` | `LightEncounter` (single with precedence rules) |
| `communication_mode` | `CommunicationMode` (scalar) | `List[CommunicationModeItem]` |
| `presentation` | `LifeReviewPresentation` (scalar) | `List[LifeReviewPresentationItem]` |
| `return_reason` | `ReturnReason` (scalar) | `List[ReturnReasonType]` |
| `home_identification` | `HomeIdentificationType` (scalar with "both") | `List[HomeIdentificationItem]` |
| `realm_type` | `RealmType` (scalar with "multiple_realms") | `List[RealmTypeItem]` |
| `veridical_perception` | `VeridicalPerception` (scalar) | `List[VeridicalClaimType]` + `VeridicalVerificationStatus` |
| `post_experience_gifts` | `PostExperienceGifts` (scalar with "multiple") | `List[PostExperienceGift]` |

**Pattern**: Removed "multiple", "both", "mixed" enum values in favor of List fields. This enables proper counting and co-occurrence analysis.

---

### 4. OBE Observation Split (HIGH PRIORITY)

| Before | After |
|--------|-------|
| `observation_accuracy: ObservationVerification` (verified, unverified, no) | `observations_made: OBEObservationsMade` + `observations_verified: OBEObservationsVerified` |

**Rationale**: Whether observations were MADE is independent from whether they were VERIFIED. The old field couldn't distinguish "no observations" from "observations not verified."

---

### 5. New Granularity Added

#### 5.1 Christian Denomination Enum (NEW)
```python
class ChristianDenomination(str, Enum):
    CATHOLIC = "catholic"  # Purgatory, saints, intercession
    ORTHODOX = "orthodox"  # Theosis tradition
    MAINLINE_PROTESTANT = "mainline_protestant"  # Methodist, Lutheran, Presbyterian
    EVANGELICAL_BAPTIST = "evangelical_baptist"  # Baptist, Pentecostal, non-denom
    MORMON_LDS = "mormon_lds"  # Three kingdoms, pre-existence
    JEHOVAHS_WITNESS = "jehovahs_witness"  # No immortal soul doctrine
    SEVENTH_DAY_ADVENTIST = "seventh_day_adventist"  # Soul sleep doctrine
    OTHER_CHRISTIAN = "other_christian"
    NOT_SPECIFIED = "not_specified"
```

**Fields Added**: `religious_background_denomination`, `religious_belief_at_nde_denomination`

**Rationale**: Christian denominations have significantly different afterlife theologies. A Catholic expecting purgatory vs an Evangelical expecting immediate heaven vs a JW expecting no afterlife are analytically distinct.

#### 5.2 Education Level Enum (NEW)
```python
class EducationLevel(str, Enum):
    NO_FORMAL = "no_formal"
    SOME_HIGH_SCHOOL = "some_high_school"
    HIGH_SCHOOL = "high_school"
    SOME_COLLEGE = "some_college"
    BACHELORS = "bachelors"
    MASTERS = "masters"
    DOCTORATE_PROFESSIONAL = "doctorate_professional"
    NOT_MENTIONED = "not_mentioned"
```

**Rationale**: Standardized categories enable demographic analysis. Free-text was inconsistent.

#### 5.3 Guidance Types (NEW)
```python
class GuidanceTypeItem(str, Enum):
    DIRECTIONAL = "directional"  # Told what to do, where to go
    INFORMATIONAL = "informational"  # Given knowledge or explanations
    LIFE_GUIDANCE = "life_guidance"  # Advice about how to live
    COMFORT = "comfort"  # Emotional support, reassurance
    TEACHING = "teaching"  # Spiritual lessons or instruction
    OTHER = "other"
```

**Rationale**: Old `GuidanceLevel` only captured presence/absence. New structure captures TYPE of guidance received.

#### 5.4 Return Reason: Unfinished Business (NEW)
Added `UNFINISHED_BUSINESS` to `ReturnReasonType` — common pattern distinct from mission/family.

#### 5.5 Post-Experience Gift: Enhanced Empathy (NEW)
Added `ENHANCED_EMPATHY` to `PostExperienceGift` — frequently reported, distinct from psychic abilities.

---

### 6. Docstring Enhancements

Several enums received detailed docstrings to guide extraction:

#### 6.1 LightEncounter Precedence
```python
class LightEncounter(str, Enum):
    """Type of light encounter. Select ONE value.
    
    Precedence: being_of_light > brilliant_light > presence_without_visual
    
    If the experiencer describes both a brilliant light AND a being of light,
    select being_of_light - the being inherently indicates presence of light.
    """
```

#### 6.2 JudgmentIntensity vs ReviewEmotionalTone
Both enums now have clear docstrings distinguishing:
- **JudgmentIntensity**: Character of the judgment ITSELF (how the source delivered it)
- **ReviewEmotionalTone**: EXPERIENCER'S emotional response (how they felt)

#### 6.3 Spirituality vs Religiosity Definitions
```python
class SpiritualityLevel(str, Enum):
    """Level of spirituality/spiritual engagement.
    
    Spirituality here means the INTERNAL/PERSONAL dimension of engagement with
    transcendent reality: prayer life, meditation, contemplation, sense of
    connection to the divine, personal religious experience. This dimension
    exists within ALL traditions - a devout Catholic with deep prayer life
    has high spirituality, as does a Buddhist practitioner or someone practicing
    private devotion outside any tradition.
    
    This is DISTINCT from religiosity (external/institutional engagement).
    """
```

---

### 7. Bias Correction

#### 7.1 SpiritualityLevel Definition
| Before (Implicit Bias) | After (Corrected) |
|------------------------|-------------------|
| "Includes SBNR, New Age, mystical traditions" | "This dimension exists within ALL traditions" |

**Issue**: Original wording implied SBNR/New Age were more "spiritual" than organized religion.

**Fix**: Clarified that spirituality (internal/personal dimension) exists equally in all traditions — Catholic prayer life, Buddhist meditation, and private devotion are all high spirituality.

---

### 8. Enum Value Cleanup

#### 8.1 Removed Redundant Values
- `BeingIdentification`: Removed `MULTIPLE_BEINGS`, `NONE`, `NOT_SPECIFIED` (use List + empty list pattern)
- `GreetingType`: Removed `NOT_MENTIONED` (use empty list pattern)
- `SpiritualBeingEncounter`: Removed `NO`, `NOT_MENTIONED` (use empty list pattern)
- `CommunicationModeItem`: Removed `MIXED` (use List pattern)
- `RealmTypeItem`: Removed `MULTIPLE_REALMS`, `NOT_MENTIONED` (use List pattern)
- `PostExperienceGift`: Removed `MULTIPLE`, `NONE` (use List pattern)
- `HomeIdentificationItem`: Removed `BOTH`, `NOT_MENTIONED` (use List pattern)

**Pattern**: Fields that can have multiple values use `List[EnumItem]` where empty list = not mentioned, multiple items = multiple values. No need for special "multiple" or "none" enum values.

---

## Migration Impact

### Breaking Changes
All field renames and enum changes will require re-extraction of existing data. The 6,753 JSON files in `projects/nde/structured/` use the old schema.

### Recommended Approach
1. Run new extraction on full dataset with updated schema
2. Compare old vs new extractions on test set to validate improvements
3. Document any systematic differences for analysis interpretation

---

## Validation Metrics

After re-extraction, compare these metrics to validate improvements:

| Metric | What to Check |
|--------|---------------|
| Death Fear Baseline | Do we now have before/after pairs where we previously only had "change"? |
| Spirituality/Religiosity Split | Do patterns emerge showing inverse relationships (↑ spirituality, ↓ religiosity)? |
| Judgment Analysis | Can we now separate "loving self-judgment" from "harsh external judgment"? |
| Denomination Distribution | Does Catholic vs Evangelical show different NDE phenomenology? |
| Return Agency vs Willingness | Do we see "told to return but willing" vs "chose to return but reluctant" patterns? |

---

## Files Changed

- `projects/nde/models/questionnaire.py` — Complete schema overhaul
- `projects/extraction-test/models/questionnaire.py` — Development version (source of changes)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Fields split (temporal) | 5 |
| Fields split (composite) | 6 |
| Scalar→List conversions | 8 |
| New enums added | 4 |
| New enum values added | ~25 |
| Enum values removed | ~15 |
| Docstrings enhanced | 10+ |
| Bias corrections | 1 |

**Total structural changes**: ~40 significant modifications

---

*Report generated from git diff between production and test questionnaire schemas.*
