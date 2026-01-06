"""Pydantic schema that mirrors the NDE analysis questionnaire."""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


class QuestionnaireBaseModel(BaseModel):
    """Shared configuration for all questionnaire models."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class MentionResponse(str, Enum):
    YES_EXPLICIT = "yes_explicit"
    IMPLIED = "implied"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class ObservationVerification(str, Enum):
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class IdentityContinuity(str, Enum):
    CLEAR = "clear_identity"
    CONFUSED = "identity_confusion"
    ALTERED_OR_LOST = "identity_altered_or_lost"
    NOT_MENTIONED = "not_mentioned"


class OBEVantage(str, Enum):
    ABOVE_BODY = "above_body"
    ROOM_CORNER = "room_corner"
    CEILING = "ceiling"
    MOVING_THROUGH_SPACES = "moving_through_spaces"
    MULTIPLE_LOCATIONS = "multiple_locations"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class SeparationSensation(str, Enum):
    PEACE = "peace"
    JOY = "joy"
    FREEDOM = "freedom"
    RELIEF = "relief"
    FEAR = "fear"
    VIBRATION = "vibration"
    PULLING = "pulling"
    POPPING = "popping"
    WEIGHTLESSNESS = "weightlessness"
    NONE_SPECIFIED = "none_specified"
    OTHER = "other"


class PassageType(str, Enum):
    TUNNEL = "tunnel"
    VOID = "void"
    OTHER = "other"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class TunnelMovementSensation(str, Enum):
    RAPID = "rapid"
    FLOATING = "floating"
    PULLED = "pulled"
    WITH_SOUND = "with_sound"
    NONE_SPECIFIED = "none_specified"
    OTHER = "other"


class LightVisibility(str, Enum):
    BRIGHT = "bright"
    PRESENT_NOT_BRIGHT = "present_not_bright"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class PassageEmotionalTone(str, Enum):
    FRIGHTENING = "frightening"
    PEACEFUL = "peaceful"
    NEUTRAL = "neutral"
    MIXED = "mixed"
    NOT_MENTIONED = "not_mentioned"


class ArrivalDescription(str, Enum):
    DETAILED = "detailed"
    MINIMAL = "minimal"
    REMAINED_TRANSITIONAL = "remained_transitional"
    NOT_MENTIONED = "not_mentioned"


class LightEncounter(str, Enum):
    BRILLIANT_LIGHT = "brilliant_light"
    BEING_OF_LIGHT = "being_of_light"
    PRESENCE_WITHOUT_VISUAL = "presence_without_visual"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class BeingIdentification(str, Enum):
    JESUS = "jesus"
    GOD = "god"
    ANGELS = "angels"
    BUDDHA = "buddha"
    RELIGIOUS_FIGURE_SPECIFIED = "religious_figure_specified"
    DECEASED_RELATIVE_GUIDE = "deceased_relative_guide"
    UNKNOWN_PRESENCE = "unknown_presence"
    MULTIPLE_BEINGS = "multiple_beings"
    OTHER = "other"
    NONE = "no_being_encountered"
    NOT_SPECIFIED = "not_specified"


class GreetingType(str, Enum):
    DECEASED_LOVED_ONES = "deceased_loved_ones"
    SPIRITUAL_BEINGS = "spiritual_beings"
    UNIDENTIFIED_PRESENCE = "unidentified_presence"
    SOLITARY = "solitary_arrival"
    NOT_MENTIONED = "not_mentioned"


class BelongingSense(str, Enum):
    EXPLICIT = "explicit"
    IMPLIED = "implied"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class EnvironmentDescription(str, Enum):
    DETAILED = "detailed"
    BRIEF = "brief"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class EnvironmentFeature(str, Enum):
    LANDSCAPE = "landscape"
    BUILDINGS = "buildings"
    LIGHT = "light"
    COLORS = "colors"
    WATER = "water"
    SKY = "sky"
    OTHER = "other"


class ComparativeReality(str, Enum):
    MORE_REAL_EXPLICIT = "more_real_explicit"
    MORE_REAL_IMPLIED = "more_real_implied"
    COMPARABLE = "comparable"
    NOT_MENTIONED = "not_mentioned"


class EncounteredRelatives(str, Enum):
    NAMED = "named"
    UNNAMED = "unnamed"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class SpiritualBeingEncounter(str, Enum):
    GUIDES_OR_ANGELS = "guides_or_angels"
    RELIGIOUS_FIGURES = "religious_figures"
    UNIDENTIFIED_BENEVOLENT = "unidentified_benevolent"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class CommunicationMode(str, Enum):
    TELEPATHIC = "telepathic"
    NONVERBAL = "nonverbal"
    NORMAL_SPEECH = "normal_speech"
    MIXED = "mixed"
    NOT_SPECIFIED = "not_specified"
    NONE = "no_communication"


class GuidanceLevel(str, Enum):
    SIGNIFICANT_GUIDANCE = "significant_guidance"
    COMFORT_OR_REASSURANCE = "comfort_or_reassurance"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class OtherSoulsPresence(str, Enum):
    MANY = "many"
    FEW = "few"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class SelfForm(str, Enum):
    CURRENT_SELF = "current_self"
    YOUNGER_OR_HEALTHIER = "younger_or_healthier"
    LIGHT_OR_ENERGY = "light_or_energy"
    NO_PHYSICAL_FORM = "no_physical_form"
    NO_DESCRIPTION = "no_description"
    NOT_MENTIONED = "not_mentioned"


class PhysicalLimitationStatus(str, Enum):
    NONE = "none"
    PRESENT = "present"
    NOT_MENTIONED = "not_mentioned"


class LifeReviewOccurrence(str, Enum):
    EXTENSIVE = "extensive"
    BRIEF = "brief"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class LifeReviewPresentation(str, Enum):
    PANORAMIC = "panoramic"
    SEQUENTIAL = "sequential"
    REEXPERIENCE = "reexperience"
    MIXED = "mixed"
    NOT_SPECIFIED = "not_specified"


class JudgmentSource(str, Enum):
    """Who passed judgment during the life review?"""
    SELF = "self"  # Experiencer judged themselves
    BEING_OF_LIGHT = "being_of_light"  # Being of Light evaluated
    GUIDE_OR_ENTITY = "guide_or_entity"  # Other spiritual guide or entity
    DECEASED_RELATIVE = "deceased_relative"  # Family member or friend who passed
    NONE = "none"  # Explicitly stated no judgment occurred
    NOT_MENTIONED = "not_mentioned"  # Account doesn't address judgment


class JudgmentIntensity(str, Enum):
    """How intense/severe was the judgment?"""
    LOVING_GENTLE = "loving_gentle"  # Supportive, educational, compassionate
    NEUTRAL = "neutral"  # Matter-of-fact observation without emotional weight
    UNCOMFORTABLE = "uncomfortable"  # Caused shame/regret but not condemning
    HARSH_CONDEMNING = "harsh_condemning"  # Punitive, hellish, fear-inducing
    NOT_APPLICABLE = "not_applicable"  # No judgment occurred (source=none)
    NOT_SPECIFIED = "not_specified"  # Judgment happened but intensity unclear


class ReviewEmotionalTone(str, Enum):
    LOVE = "love"
    NEUTRAL = "neutral"
    SHAME_OR_REGRET = "shame_or_regret"
    MIXED = "mixed"
    NOT_SPECIFIED = "not_specified"


class BoundaryEncounter(str, Enum):
    PHYSICAL_BARRIER = "physical_barrier"
    THRESHOLD = "threshold"
    VERBAL_LIMIT = "verbal_limit"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class ReturnChoice(str, Enum):
    CHOSE_TO_RETURN = "chose_to_return"
    RELUCTANT_RETURN = "reluctant_return"
    TOLD_TO_RETURN = "told_to_return"
    INVOLUNTARY = "involuntary"
    NOT_MENTIONED = "not_mentioned"


class ReturnReason(str, Enum):
    EARTHLY_MISSION = "earthly_mission"
    FAMILY_RESPONSIBILITY = "family_responsibility"
    NOT_YOUR_TIME = "not_your_time"
    NO_REASON_GIVEN = "no_reason_given"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class ReturnDescriptionDetail(str, Enum):
    DETAILED = "detailed"
    BRIEF = "brief"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class ReturnMethod(str, Enum):
    RAPID = "rapid"
    GRADUAL = "gradual"
    INSTANT = "instant"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class ReturnFeeling(str, Enum):
    UNPLEASANT = "unpleasant"
    NEUTRAL = "neutral"
    PLEASANT = "pleasant"
    NOT_MENTIONED = "not_mentioned"


class ReadjustmentDifficulty(str, Enum):
    SIGNIFICANT = "significant"
    BRIEF = "brief"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class PostAbilityChange(str, Enum):
    PSYCHIC = "psychic"
    EMPATHY = "empathy"
    ELECTRICAL = "electrical"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class BeliefChange(str, Enum):
    NO_FEAR = "no_fear"
    SOME_FEAR = "some_fear"
    NO_CHANGE = "no_change"
    NOT_MENTIONED = "not_mentioned"


class ValueShift(str, Enum):
    MAJOR = "major"
    SUBTLE = "subtle"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class SpiritualityShift(str, Enum):
    MORE_SPIRITUAL = "more_spiritual"
    MORE_RELIGIOUS = "more_religious"
    NO_CHANGE = "no_change"
    LESS_RELIGIOUS_MORE_SPIRITUAL = "less_religious_more_spiritual"
    NOT_MENTIONED = "not_mentioned"


# === Cosmic Knowledge & Pre-Existence Enums ===


class IncarnationChoiceType(str, Enum):
    """Whether the experiencer described choosing to incarnate."""
    CHOSE_PARENTS = "chose_parents"
    CHOSE_MISSION = "chose_mission"
    CHOSE_BOTH = "chose_both"
    NO_CHOICE = "no_choice"
    NOT_MENTIONED = "not_mentioned"


class FutureKnowledgeType(str, Enum):
    """Type of future knowledge received."""
    PERSONAL_FUTURE = "personal_future"
    GLOBAL_FUTURE = "global_future"
    BOTH = "both"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class DeathMemoryType(str, Enum):
    """Memory of a previous death (for reincarnation discrimination)."""
    VIOLENT = "violent"
    NATURAL = "natural"
    UNSPECIFIED = "unspecified"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class SoulAgeType(str, Enum):
    """Indication of soul age or incarnation history."""
    OLD_SOUL = "old_soul"
    NEW_SOUL = "new_soul"
    FIRST_INCARNATION = "first_incarnation"
    MANY_LIVES = "many_lives"
    NOT_MENTIONED = "not_mentioned"


class HomeIdentificationType(str, Enum):
    """Where the experiencer identified as 'home'."""
    SPIRITUAL_REALM = "spiritual_realm"
    EARTH = "earth"
    BOTH = "both"
    NEITHER = "neither"
    NOT_MENTIONED = "not_mentioned"


class MissionType(str, Enum):
    """Types of missions commissioned during the NDE."""
    HEALING = "healing"
    TEACHING = "teaching"
    WITNESSING = "witnessing"
    SERVICE = "service"
    CREATIVE = "creative"
    RAISING_CHILDREN = "raising_children"
    OTHER = "other"


# === Experience Quality & Phenomenological Markers ===


class TimePerception(str, Enum):
    """How time was perceived during the experience."""
    TIMELESS = "timeless"
    EVERYTHING_AT_ONCE = "everything_at_once"
    SPEEDED_UP = "speeded_up"
    SLOWED_DOWN = "slowed_down"
    NORMAL = "normal"
    NOT_MENTIONED = "not_mentioned"


class ThoughtSpeed(str, Enum):
    """Speed of cognitive processing during the experience."""
    INCREDIBLY_FAST = "incredibly_fast"
    FASTER_THAN_NORMAL = "faster_than_normal"
    NORMAL = "normal"
    SLOWER = "slower"
    NOT_MENTIONED = "not_mentioned"


class SensoryVividness(str, Enum):
    """Vividness of sensory perception compared to normal."""
    INCREDIBLY_MORE_VIVID = "incredibly_more_vivid"
    MORE_VIVID = "more_vivid"
    SAME = "same"
    LESS_VIVID = "less_vivid"
    NOT_MENTIONED = "not_mentioned"


class MemoryPersistence(str, Enum):
    """How the memory compares to normal life memories."""
    MORE_VIVID_THAN_NORMAL = "more_vivid_than_normal"
    SAME_AS_NORMAL = "same_as_normal"
    LESS_VIVID = "less_vivid"
    FADING = "fading"
    NOT_MENTIONED = "not_mentioned"


class RealityAssessment(str, Enum):
    """Experiencer's assessment of whether the experience was 'real'."""
    DEFINITELY_REAL = "definitely_real"
    PROBABLY_REAL = "probably_real"
    UNCERTAIN = "uncertain"
    PROBABLY_NOT_REAL = "probably_not_real"
    NOT_MENTIONED = "not_mentioned"


class RealmType(str, Enum):
    """Type of realm or environment experienced."""
    CLEARLY_UNEARTHLY = "clearly_unearthly"
    VAGUELY_UNEARTHLY = "vaguely_unearthly"
    FAMILIAR_EARTHLIKE = "familiar_earthlike"
    HEAVENLY = "heavenly"
    HELLISH = "hellish"
    VOID_DARKNESS = "void_darkness"
    MULTIPLE_REALMS = "multiple_realms"
    NOT_MENTIONED = "not_mentioned"


class ExperienceValence(str, Enum):
    """Overall emotional valence of the experience."""
    INCREDIBLY_PLEASANT = "incredibly_pleasant"
    PLEASANT = "pleasant"
    NEUTRAL = "neutral"
    DISTRESSING = "distressing"
    TERRIFYING = "terrifying"
    MIXED = "mixed"
    NOT_MENTIONED = "not_mentioned"


class VeridicalPerception(str, Enum):
    """Whether experiencer reported verifiable out-of-body perceptions."""
    VERIFIED_ACCURATE = "verified_accurate"  # Confirmed accurate OBE observations
    CLAIMED_UNVERIFIED = "claimed_unverified"  # Claims remote perception but unverified
    ESP_CLAIMED = "esp_claimed"  # General ESP/remote viewing claimed
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class BeliefConsistency(str, Enum):
    """Whether experience was consistent with prior beliefs."""
    CONSISTENT = "consistent"  # Matched prior religious/spiritual expectations
    INCONSISTENT = "inconsistent"  # Contradicted prior beliefs
    PARTIALLY_CONSISTENT = "partially_consistent"  # Some elements matched, others didn't
    NO_PRIOR_BELIEFS = "no_prior_beliefs"  # Had no strong beliefs before
    NOT_MENTIONED = "not_mentioned"


class PostExperienceGifts(str, Enum):
    """Psychic or unusual abilities reported after the NDE."""
    PSYCHIC_ABILITIES = "psychic_abilities"  # General psychic gifts
    HEALING_ABILITIES = "healing_abilities"  # Healing touch/energy
    PRECOGNITION = "precognition"  # Seeing future events
    MEDIUMSHIP = "mediumship"  # Communication with deceased
    INCREASED_INTUITION = "increased_intuition"  # Enhanced intuition
    ELECTRICAL_SENSITIVITY = "electrical_sensitivity"  # Affects electronics
    MULTIPLE = "multiple"  # Multiple gifts reported
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class NDECause(str, Enum):
    CARDIAC_ARREST = "cardiac_arrest"
    ACCIDENT = "accident"
    SURGERY = "surgery"
    ILLNESS = "illness"
    CHILDBIRTH = "childbirth"
    SUICIDE_ATTEMPT = "suicide_attempt"
    COMBAT_OR_VIOLENCE = "combat_or_violence"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class ClinicalDeathStatus(str, Enum):
    VERIFIED = "verified"
    IMPLIED = "implied"
    NO = "no"
    UNKNOWN = "unknown"


class ExperienceDuration(str, Enum):
    SECONDS_TO_MINUTES = "seconds_to_minutes"
    MINUTES_TO_HOURS = "minutes_to_hours"
    TIMELESS = "timeless"
    NOT_SPECIFIED = "not_specified"


class PriorKnowledgeStatus(str, Enum):
    AWARE = "aware"
    UNAWARE = "unaware"
    NOT_MENTIONED = "not_mentioned"


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    NOT_MENTIONED = "not_mentioned"


class MaritalStatus(str, Enum):
    MARRIED = "married"
    SINGLE = "single"
    DIVORCED_SEPARATED = "divorced_separated"
    WIDOWED = "widowed"
    NOT_MENTIONED = "not_mentioned"


class ReligiousAffiliation(str, Enum):
    CHRISTIAN = "christian"
    JEWISH = "jewish"
    MUSLIM = "muslim"
    HINDU = "hindu"
    BUDDHIST = "buddhist"
    ATHEIST_AGNOSTIC = "atheist_agnostic"
    SPIRITUAL_NOT_RELIGIOUS = "spiritual_not_religious"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class CanonicalSequenceAdherence(str, Enum):
    STRICT = "strict"
    MOSTLY = "mostly"
    PARTIAL = "partial"
    RADICAL = "radical"
    INDETERMINATE = "indeterminate"
    NOT_APPLICABLE = "not_applicable"


class StageElement(str, Enum):
    OBE = "obe"
    TUNNEL = "tunnel"
    LIGHT_ENCOUNTER = "light_encounter"
    LOVED_ONES = "loved_ones"
    LIFE_REVIEW = "life_review"
    BOUNDARY = "boundary"
    RETURN_CHOICE = "return_choice"
    ENVIRONMENT = "environment"
    COMMUNICATION = "communication"
    OTHER = "other"


class StageRepetitionStatus(str, Enum):
    YES = "yes"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class StageSimultaneityStatus(str, Enum):
    YES = "yes"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class OutOfBodyExperience(QuestionnaireBaseModel):
    separation: MentionResponse = Field(
        ...,
        description="Q1.1.1 — Did the experiencer report separating from their physical body?",
    )
    vantage_points: List[OBEVantage] = Field(
        default_factory=list,
        description="Q1.1.2 — Locations described during the OBE.",
    )
    vantage_other_detail: Optional[str] = Field(
        None, description="Detail when 'other' vantage is selected."
    )
    observation_accuracy: ObservationVerification = Field(
        ...,
        description="Q1.1.3 — Did they report observing events and were they verified?",
    )
    heightened_perception: MentionResponse = Field(
        ...,
        description="Q1.1.4 — Sense of enhanced clarity or heightened perception.",
    )
    identity_continuity: IdentityContinuity = Field(
        ...,
        description="Q1.1.5 — Continuity of identity and self-awareness during the OBE.",
    )
    separation_sensations: List[SeparationSensation] = Field(
        default_factory=list,
        description="Q1.1.6 — Sensations accompanying separation from the body.",
    )
    separation_sensations_other: Optional[str] = Field(
        None, description="Detail for other separation sensations."
    )


class TunnelExperience(QuestionnaireBaseModel):
    passage_type: PassageType = Field(
        ...,
        description="Q1.2.1 — Reported movement through tunnel, void, or other space.",
    )
    passage_other_detail: Optional[str] = Field(
        None, description="Detail for other type of passage."
    )
    movement_sensations: List[TunnelMovementSensation] = Field(
        default_factory=list,
        description="Q1.2.2 — Sensations accompanying tunnel movement.",
    )
    movement_other_detail: Optional[str] = Field(
        None, description="Detail for other movement sensations."
    )
    light_visibility: LightVisibility = Field(
        ...,
        description="Q1.2.3 — Presence of light at the end of the passage.",
    )
    emotional_tone: PassageEmotionalTone = Field(
        ...,
        description="Q1.2.4 — Emotional tone of the tunnel/transitional phase.",
    )


class ArrivalExperience(QuestionnaireBaseModel):
    environment_description: ArrivalDescription = Field(
        ...,
        description="Q1.3.1 — Emergence into a new environment or realm.",
    )
    light_encounter: List[LightEncounter] = Field(
        default_factory=list,
        description="Q1.3.2 — Encounter with light, being of light, or presence of love.",
    )
    being_identifications: List[BeingIdentification] = Field(
        default_factory=list,
        description="Q1.3.3 — Identified beings encountered upon arrival.",
    )
    religious_figure_detail: Optional[str] = Field(
        None, description="Detail when a specific religious figure is mentioned."
    )
    other_being_detail: Optional[str] = Field(
        None, description="Detail for other types of beings encountered."
    )
    greeting_types: List[GreetingType] = Field(
        default_factory=list,
        description="Q1.3.4 — How the experiencer was greeted or welcomed.",
    )
    sense_of_belonging: BelongingSense = Field(
        ...,
        description="Q1.3.4 (duplicate number) — Sense of coming home or belonging.",
    )


class PassageSection(QuestionnaireBaseModel):
    out_of_body: OutOfBodyExperience
    tunnel: TunnelExperience
    arrival: ArrivalExperience


class EnvironmentDescriptionSection(QuestionnaireBaseModel):
    environment_description: EnvironmentDescription = Field(
        ...,
        description="Q2.1.1 — Description of the environment entered.",
    )
    environment_features: List[EnvironmentFeature] = Field(
        default_factory=list,
        description="Q2.1.2 — Physical features of the environment.",
    )
    environment_other_detail: Optional[str] = Field(
        None, description="Detail for other environment features."
    )
    comparative_reality: ComparativeReality = Field(
        ...,
        description="Q2.1.3 — Whether the environment felt more real than earthly reality.",
    )
    thought_responsiveness: MentionResponse = Field(
        ...,
        description="Q2.1.4 — Whether the environment was responsive to thought or intention.",
    )


class EncountersSection(QuestionnaireBaseModel):
    deceased_relatives: EncounteredRelatives = Field(
        ...,
        description="Q2.2.1 — Encounters with deceased relatives or friends.",
    )
    spiritual_beings: List[SpiritualBeingEncounter] = Field(
        default_factory=list,
        description="Q2.2.2 — Encounters with guides, angels, or religious figures.",
    )
    communication_mode: CommunicationMode = Field(
        ...,
        description="Q2.2.3 — Mode of communication with beings.",
    )
    guidance_level: GuidanceLevel = Field(
        ...,
        description="Q2.2.4 — Whether beings provided guidance or comfort.",
    )
    other_souls_presence: OtherSoulsPresence = Field(
        ...,
        description="Q2.2.5 — Presence of other souls not personally known.",
    )


class SelfPerceptionSection(QuestionnaireBaseModel):
    self_form: SelfForm = Field(
        ...,
        description="Q2.3.1 — How the experiencer described their own form.",
    )
    physical_limitations: PhysicalLimitationStatus = Field(
        ...,
        description="Q2.3.2 — Whether physical limitations were present.",
    )


class WorldOfSpiritsSection(QuestionnaireBaseModel):
    environment: EnvironmentDescriptionSection
    encounters: EncountersSection
    self_perception: SelfPerceptionSection


class LifeReviewSection(QuestionnaireBaseModel):
    occurrence: LifeReviewOccurrence = Field(
        ...,
        description="Q3.1.1 — Whether a life review occurred.",
    )
    presentation: LifeReviewPresentation = Field(
        ...,
        description="Q3.1.2 — How the life review was presented.",
    )
    perspective_of_others: MentionResponse = Field(
        ...,
        description="Q3.1.3 — Experiencing emotions/perspectives of others.",
    )
    judgment_source: JudgmentSource = Field(
        ...,
        description="Q3.1.4 — Who passed judgment during the life review?",
    )
    judgment_intensity: JudgmentIntensity = Field(
        ...,
        description="Q3.1.5 — How intense or severe was the judgment?",
    )
    emotional_tone: ReviewEmotionalTone = Field(
        ...,
        description="Q3.1.6 — Emotional tone of the life review.",
    )


class CosmicKnowledgeSection(QuestionnaireBaseModel):
    """Section capturing pre-existence, cosmic knowledge, and soul trajectory markers.
    
    These fields are critical for discriminating between:
    - Restorative incarnations (trauma-driven returns with past-life memories)
    - Volunteer/Normative souls (non-cyclic origins, mission-oriented)
    
    Based on NDERF questionnaire fields and Selection Artifact research.
    """
    
    # Pre-Existence / Premortal Knowledge
    premortal_existence_info: MentionResponse = Field(
        ...,
        description="Q3.2.1 — Did they gain information about existence before birth?",
    )
    pre_birth_realm_description: MentionResponse = Field(
        ...,
        description="Q3.2.2 — Did they describe a pre-birth spiritual realm?",
    )
    incarnation_choice: IncarnationChoiceType = Field(
        ...,
        description="Q3.2.3 — Did they describe choosing to incarnate (parents/mission/both)?",
    )
    life_preview: MentionResponse = Field(
        ...,
        description="Q3.2.4 — Were they shown a preview of this life before birth?",
    )
    pre_incarnation_covenant: MentionResponse = Field(
        ...,
        description="Q3.2.5 — Memory of a contract/agreement made before birth?",
    )
    
    # Cosmic/Universal Knowledge
    universal_knowledge: MentionResponse = Field(
        ...,
        description="Q3.3.1 — Access to all knowledge or cosmic understanding?",
    )
    cosmic_understanding: MentionResponse = Field(
        ...,
        description="Q3.3.2 — Understanding of how the universe works?",
    )
    future_knowledge: FutureKnowledgeType = Field(
        ...,
        description="Q3.3.3 — Information about future events (personal/global/both)?",
    )
    purpose_of_existence: MentionResponse = Field(
        ...,
        description="Q3.3.4 — Understanding of why existence/creation exists?",
    )
    
    # Reincarnation Markers (for Restorative vs. Volunteer discrimination)
    past_life_memory: MentionResponse = Field(
        ...,
        description="Q3.4.1 — Memory of previous earthly lives?",
    )
    death_memory: DeathMemoryType = Field(
        ...,
        description="Q3.4.2 — Memory of a previous death (violent/natural/none)?",
    )
    intermission_memory: MentionResponse = Field(
        ...,
        description="Q3.4.3 — Memory of time between lives (intermission)?",
    )
    soul_age_indication: SoulAgeType = Field(
        ...,
        description="Q3.4.4 — Any indication of soul age or incarnation history?",
    )
    
    # Ontological Markers (soul type indicators)
    home_identification: HomeIdentificationType = Field(
        ...,
        description="Q3.5.1 — Where did they identify as 'home' (spiritual realm/earth/both)?",
    )
    earth_alienation: MentionResponse = Field(
        ...,
        description="Q3.5.2 — Sense of not belonging on Earth or being a 'stranger'?",
    )
    identity_pre_body: MentionResponse = Field(
        ...,
        description="Q3.5.3 — Identity existed before current body?",
    )


class BoundarySection(QuestionnaireBaseModel):
    boundary_encounter: BoundaryEncounter = Field(
        ...,
        description="Q4.1.1 — Encountering a boundary or point of no return.",
    )
    return_choice: ReturnChoice = Field(
        ...,
        description="Q4.1.2 — Whether there was a choice involved in returning.",
    )
    return_reason: ReturnReason = Field(
        ...,
        description="Q4.1.3 — Reason provided for the return.",
    )
    return_reason_other_detail: Optional[str] = Field(
        None, description="Detail for other reasons to return."
    )
    return_description: ReturnDescriptionDetail = Field(
        ...,
        description="Q4.2.1 — Description of the return to the body.",
    )
    return_method: ReturnMethod = Field(
        ...,
        description="Q4.2.2 — Method of returning to the body.",
    )
    return_method_other_detail: Optional[str] = Field(
        None, description="Detail for other return methods."
    )
    return_feeling: ReturnFeeling = Field(
        ...,
        description="Q4.2.3 — Emotional tone of the return experience.",
    )
    
    # Mission/Purpose Commissioning
    mission_commissioned: MentionResponse = Field(
        ...,
        description="Q4.3.1 — Were they given a specific task/mission to accomplish?",
    )
    mission_types: List[MissionType] = Field(
        default_factory=list,
        description="Q4.3.2 — Types of mission (healing/teaching/witnessing/service/creative/other).",
    )
    mission_detail: Optional[str] = Field(
        None, description="Q4.3.3 — Description of the mission if specified."
    )
    volunteer_language: MentionResponse = Field(
        ...,
        description="Q4.3.4 — Used 'volunteer' or similar language about incarnating?",
    )


class AftereffectsSection(QuestionnaireBaseModel):
    readjustment: ReadjustmentDifficulty = Field(
        ...,
        description="Q5.1.1 — Difficulty readjusting to physical reality.",
    )
    post_ability_changes: List[PostAbilityChange] = Field(
        default_factory=list,
        description="Q5.1.2 — Reported abilities or sensitivities after the NDE.",
    )
    belief_change: BeliefChange = Field(
        ...,
        description="Q5.2.1 — Change in beliefs about death.",
    )
    value_shift: ValueShift = Field(
        ...,
        description="Q5.2.2 — Changes in values, priorities, or life purpose.",
    )
    spirituality_shift: SpiritualityShift = Field(
        ...,
        description="Q5.2.3 — Changes in spirituality or religious involvement.",
    )


class ExperienceQualitySection(QuestionnaireBaseModel):
    """Phenomenological quality markers for NDE authenticity and character assessment.
    
    These fields capture the experiential quality dimensions that distinguish
    NDEs from dreams, hallucinations, and other altered states. They also
    enable analysis of the "hyper-real" nature frequently reported.
    """
    
    # Time & Consciousness Perception
    time_perception: TimePerception = Field(
        ...,
        description="Q5.3.1 — How was time perceived during the experience?",
    )
    thought_speed: ThoughtSpeed = Field(
        ...,
        description="Q5.3.2 — Speed of cognitive processing during the experience.",
    )
    
    # Sensory Quality
    sensory_vividness: SensoryVividness = Field(
        ...,
        description="Q5.3.3 — Vividness of sensory perception compared to normal.",
    )
    
    # Authenticity Markers (critical for discriminant analysis)
    ineffability: MentionResponse = Field(
        ...,
        description="Q5.3.4 — Did they state the experience was impossible to describe in words?",
    )
    memory_persistence: MemoryPersistence = Field(
        ...,
        description="Q5.3.5 — How does the memory compare to normal life memories?",
    )
    reality_assessment: RealityAssessment = Field(
        ...,
        description="Q5.3.6 — Experiencer's assessment of whether the experience was 'real'.",
    )
    
    # Unity/Oneness (key spiritual marker)
    unity_experience: MentionResponse = Field(
        ...,
        description="Q5.3.7 — Did they feel unity or oneness with the universe?",
    )
    
    # Realm Classification
    realm_type: RealmType = Field(
        ...,
        description="Q5.3.8 — Type of realm or environment experienced.",
    )
    
    # Overall Valence
    overall_valence: ExperienceValence = Field(
        ...,
        description="Q5.3.9 — Overall emotional valence of the experience.",
    )
    
    # Veridical/Paranormal Markers
    veridical_perception: VeridicalPerception = Field(
        ...,
        description="Q5.3.10 — Did they report verifiable OBE observations or ESP?",
    )
    
    # Belief-Experience Alignment (cultural influence analysis)
    belief_consistency: BeliefConsistency = Field(
        ...,
        description="Q5.3.11 — Was the experience consistent with prior religious/spiritual beliefs?",
    )
    
    # Post-Experience Paranormal Gifts
    post_experience_gifts: PostExperienceGifts = Field(
        ...,
        description="Q5.3.12 — Any psychic or unusual abilities reported after the NDE?",
    )
    
    # Multiple NDE Flag
    multiple_ndes: MentionResponse = Field(
        ...,
        description="Q5.3.13 — Has the experiencer had more than one NDE?",
    )


class NDEContextSection(QuestionnaireBaseModel):
    nde_cause: NDECause = Field(
        ...,
        description="Q6.1.1 — Cause of the near-death event.",
    )
    nde_cause_other_detail: Optional[str] = Field(
        None, description="Detail for other causes of the NDE."
    )
    clinical_status: ClinicalDeathStatus = Field(
        ...,
        description="Q6.1.2 — Whether the individual was clinically dead.",
    )
    experience_duration: ExperienceDuration = Field(
        ...,
        description="Q6.1.3 — Subjective duration of the NDE.",
    )


class PersonDemographicsSection(QuestionnaireBaseModel):
    age_reported: bool = Field(
        ...,
        description="Q6.2.1 — Whether age was mentioned.",
    )
    age_years: Optional[int] = Field(
        None, ge=0, description="Age in years when reported."
    )
    gender: Gender = Field(
        ...,
        description="Q6.2.2 — Gender of the experiencer.",
    )
    location_country: Optional[str] = Field(
        None, description="Q6.2.3 — Country if mentioned."
    )
    location_state_province: Optional[str] = Field(
        None, description="Q6.2.3 — State/province if mentioned."
    )
    location_city: Optional[str] = Field(
        None, description="Q6.2.3 — City if mentioned."
    )
    nationality_ethnicity: Optional[str] = Field(
        None, description="Q6.2.4 — Nationality or ethnicity if mentioned."
    )
    religious_affiliation: ReligiousAffiliation = Field(
        ...,
        description="Q6.2.5 — Religious affiliation or spiritual background.",
    )
    religious_affiliation_detail: Optional[str] = Field(
        None, description="Detail for Christian denomination or other religious affiliation."
    )
    occupation: Optional[str] = Field(
        None, description="Q6.2.6 — Occupation or professional background."
    )
    education_level: Optional[str] = Field(
        None, description="Q6.2.7 — Highest educational level mentioned."
    )
    marital_status: MaritalStatus = Field(
        ...,
        description="Q6.2.8 — Marital status if mentioned.",
    )
    has_children: Optional[bool] = Field(
        None, description="Q6.2.8 — Whether the experiencer has children."
    )
    number_of_children: Optional[int] = Field(
        None, ge=0, description="Q6.2.8 — Number of children if specified."
    )
    prior_nde_knowledge: PriorKnowledgeStatus = Field(
        ...,
        description="Q6.2.9 — Prior knowledge or belief in NDEs.",
    )

    @model_validator(mode="after")
    def validate_demographics(self):
        # Allow age_reported=True with age_years=None when age is mentioned but not extractable
        # (e.g., "in my early 20s", "as a child", "middle-aged")
        # Previously this raised ValueError, but vague age references are common in narratives
        if not self.age_reported:
            self.age_years = None

        if self.number_of_children is not None and self.number_of_children < 0:
            raise ValueError("Number of children cannot be negative.")
        if not self.has_children:
            self.number_of_children = None

        return self


class StageSequenceSection(QuestionnaireBaseModel):
    present_elements: List[StageElement] = Field(
        default_factory=list,
        description="Q7.1.1 — Stages present in the experience.",
    )
    elements_other_detail: Optional[str] = Field(
        None, description="Detail for other significant elements."
    )
    canonical_sequence: CanonicalSequenceAdherence = Field(
        ...,
        description="Q7.1.2 — Degree of adherence to canonical stage order.",
    )
    sequence_variation_description: Optional[str] = Field(
        None, description="Q7.1.3 — Description of actual order when it varies."
    )
    repeated_stages: StageRepetitionStatus = Field(
        ...,
        description="Q7.1.4 — Whether stages were repeated.",
    )
    repeated_stage_detail: Optional[str] = Field(
        None, description="Details about which stages repeated."
    )
    simultaneous_stages: StageSimultaneityStatus = Field(
        ...,
        description="Q7.1.5 — Whether stages occurred simultaneously.",
    )
    simultaneous_stage_detail: Optional[str] = Field(
        None, description="Details about simultaneous stages."
    )


class UniqueElementsSection(QuestionnaireBaseModel):
    nonstandard_elements: Optional[str] = Field(
        None,
        description="Q8.1 — Elements that do not fit the standard model.",
    )
    notable_quotes: Optional[str] = Field(
        None,
        description="Q8.2 — Notable quotes or vivid descriptions to extract.",
    )


class NDEAnalysisResponse(QuestionnaireBaseModel):
    """Complete structured response for the NDE questionnaire."""

    passage: PassageSection
    world_of_spirits: WorldOfSpiritsSection
    life_review: LifeReviewSection
    cosmic_knowledge: CosmicKnowledgeSection
    boundary_and_return: BoundarySection
    transformative_effects: AftereffectsSection
    experience_quality: ExperienceQualitySection
    context: NDEContextSection
    person_demographics: PersonDemographicsSection
    stage_sequence: StageSequenceSection
    unique_elements: UniqueElementsSection
