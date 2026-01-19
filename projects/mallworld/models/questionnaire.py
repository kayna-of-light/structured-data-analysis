"""Pydantic schema for Mall World phenomenological analysis.

This questionnaire extracts structured data from Mall World dream reports,
mapping phenomenological features to Swedenborgian correspondences.

Reference: "The Spiritual Topography of the Late Modern Soul" analysis document.
"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class QuestionnaireBaseModel(BaseModel):
    """Shared configuration for all questionnaire models."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# =============================================================================
# STANDARD RESPONSE ENUMS
# =============================================================================

class MentionResponse(str, Enum):
    """Standard response for presence/absence questions."""
    YES_EXPLICIT = "yes_explicit"
    IMPLIED = "implied"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


class IntensityLevel(str, Enum):
    """Intensity or prominence level."""
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# LOCATION ENUMS
# =============================================================================

class PrimaryLocation(str, Enum):
    """Primary location type in the Mall World."""
    MALL = "mall"
    AIRPORT = "airport"
    TRAIN_STATION = "train_station"
    HOTEL = "hotel"
    CASINO = "casino"
    SCHOOL_UNIVERSITY = "school_university"
    LIBRARY = "library"
    MUSEUM = "museum"
    BEACH_COAST = "beach_coast"
    AMUSEMENT_PARK = "amusement_park"
    PARKING_GARAGE = "parking_garage"
    BASEMENT_UNDERGROUND = "basement_underground"
    RESIDENTIAL = "residential"
    HOSPITAL = "hospital"
    OFFICE_BUILDING = "office_building"
    OTHER = "other"
    NOT_SPECIFIED = "not_specified"


class SubLocation(str, Enum):
    """Sub-locations within primary locations."""
    FOOD_COURT = "food_court"
    BATHROOM = "bathroom"
    ELEVATOR = "elevator"
    ESCALATOR = "escalator"
    STAIRS = "stairs"
    HALLWAY_CORRIDOR = "hallway_corridor"
    LOBBY = "lobby"
    STORE_SHOP = "store_shop"
    RESTAURANT = "restaurant"
    WAITING_AREA = "waiting_area"
    TUNNEL = "tunnel"
    PLATFORM = "platform"
    POOL_WATER_FEATURE = "pool_water_feature"
    ROOFTOP = "rooftop"
    ATRIUM = "atrium"
    OTHER = "other"


class ConnectivityMethod(str, Enum):
    """How locations connect to each other."""
    WALKING = "walking"
    TRAIN_SUBWAY = "train_subway"
    BUS = "bus"
    ELEVATOR = "elevator"
    ESCALATOR = "escalator"
    TUNNEL = "tunnel"
    SKYBRIDGE = "skybridge"
    TELEPORTATION_SHIFT = "teleportation_shift"
    UNCLEAR = "unclear"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# ARCHITECTURAL FEATURE ENUMS
# =============================================================================

class ArchitecturalQuality(str, Enum):
    """Architectural qualities of the space."""
    CIRCULAR = "circular"
    MULTI_LEVEL = "multi_level"
    INFINITE_ENDLESS = "infinite_endless"
    LABYRINTHINE = "labyrinthine"
    SHIFTING_CHANGING = "shifting_changing"
    FAMILIAR_REAL_PLACE = "familiar_real_place"
    UNFAMILIAR_ALIEN = "unfamiliar_alien"
    ABANDONED_EMPTY = "abandoned_empty"
    CROWDED = "crowded"
    CLAUSTROPHOBIC = "claustrophobic"
    VAST_OPEN = "vast_open"
    OTHER = "other"


class LightingQuality(str, Enum):
    """Lighting quality in the space."""
    BRIGHT_FLUORESCENT = "bright_fluorescent"
    DIM_DARK = "dim_dark"
    NATURAL_DAYLIGHT = "natural_daylight"
    NEON_COLORED = "neon_colored"
    WARM_GOLDEN = "warm_golden"
    HARSH_STARK = "harsh_stark"
    NO_VISIBLE_SOURCE = "no_visible_source"
    VARIABLE_CHANGING = "variable_changing"
    NOT_MENTIONED = "not_mentioned"


class ColorScheme(str, Enum):
    """Dominant color scheme mentioned."""
    RED_DOMINANT = "red_dominant"
    GOLD_OPULENT = "gold_opulent"
    GREY_NEUTRAL = "grey_neutral"
    WHITE_STERILE = "white_sterile"
    DARK_BLACK = "dark_black"
    COLORFUL_VIBRANT = "colorful_vibrant"
    MUTED_FADED = "muted_faded"
    NOT_MENTIONED = "not_mentioned"


class RealityQuality(str, Enum):
    """Quality of reality/solidity of the experience."""
    HYPER_REAL = "hyper_real"
    NORMAL_REALISTIC = "normal_realistic"
    DREAMLIKE_HAZY = "dreamlike_hazy"
    SOLID_PERSISTENT = "solid_persistent"
    SHIFTING_UNSTABLE = "shifting_unstable"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# VERTICAL MOVEMENT ENUMS
# =============================================================================

class ElevatorExperience(str, Enum):
    """Type of elevator experience."""
    NORMAL_FUNCTIONING = "normal_functioning"
    FALLING_CRASHING = "falling_crashing"
    ROCKETING_UPWARD = "rocketing_upward"
    MOVING_SIDEWAYS = "moving_sideways"
    STUCK_TRAPPED = "stuck_trapped"
    GLASS_TRANSPARENT = "glass_transparent"
    WRONG_FLOOR = "wrong_floor"
    FEAR_AVOIDANCE = "fear_avoidance"
    NOT_MENTIONED = "not_mentioned"


class EscalatorExperience(str, Enum):
    """Type of escalator experience."""
    NORMAL_FUNCTIONING = "normal_functioning"
    ENDLESS_INFINITE = "endless_infinite"
    STEEP_FRIGHTENING = "steep_frightening"
    FLATTENING_OUT = "flattening_out"
    GOING_WRONG_DIRECTION = "going_wrong_direction"
    FEAR_OF_FALLING = "fear_of_falling"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# EMOTIONAL/SPIRITUAL ENUMS
# =============================================================================

class EmotionalTone(str, Enum):
    """Dominant emotional tone of the experience."""
    ANXIETY_STRESS = "anxiety_stress"
    PEACE_CALM = "peace_calm"
    DREAD_FEAR = "dread_fear"
    CONFUSION_DISORIENTATION = "confusion_disorientation"
    FAMILIARITY_NOSTALGIA = "familiarity_nostalgia"
    WONDER_AWE = "wonder_awe"
    FRUSTRATION = "frustration"
    LONELINESS_ISOLATION = "loneliness_isolation"
    URGENCY_RUSHING = "urgency_rushing"
    NEUTRAL = "neutral"
    MIXED = "mixed"
    NOT_MENTIONED = "not_mentioned"


class TransactionOutcome(str, Enum):
    """Outcome of commerce/eating attempts."""
    SUCCESSFUL = "successful"
    FAILED_BLOCKED = "failed_blocked"
    INTERRUPTED = "interrupted"
    ITEM_UNAVAILABLE = "item_unavailable"
    CANNOT_PAY = "cannot_pay"
    FOOD_INEDIBLE = "food_inedible"
    WOKE_UP_BEFORE_COMPLETION = "woke_up_before_completion"
    NOT_ATTEMPTED = "not_attempted"
    NOT_MENTIONED = "not_mentioned"


class BeingType(str, Enum):
    """Types of beings encountered."""
    FAMILIAR_PEOPLE = "familiar_people"
    STRANGERS_CROWDS = "strangers_crowds"
    THREATENING_ENTITIES = "threatening_entities"
    GUIDES_HELPERS = "guides_helpers"
    DEMONS_EVIL_PRESENCE = "demons_evil_presence"
    EMPLOYEES_STAFF = "employees_staff"
    NO_PEOPLE = "no_people"
    OTHER = "other"


class BathroomCondition(str, Enum):
    """Condition of bathroom if mentioned."""
    CLEAN_NORMAL = "clean_normal"
    DIRTY_FILTHY = "dirty_filthy"
    OVERFLOWING = "overflowing"
    NO_PRIVACY_NO_DOORS = "no_privacy_no_doors"
    MAZE_LIKE = "maze_like"
    UNUSABLE = "unusable"
    NOT_MENTIONED = "not_mentioned"


class HotelCharacter(str, Enum):
    """Character/atmosphere of hotel if mentioned."""
    LUXURIOUS_OPULENT = "luxurious_opulent"
    RED_VELVET_GOLD = "red_velvet_gold"
    HAUNTED_CREEPY = "haunted_creepy"
    ABANDONED = "abandoned"
    NORMAL_NEUTRAL = "normal_neutral"
    CONVENTION_BUSINESS = "convention_business"
    NOT_MENTIONED = "not_mentioned"


class OceanExperience(str, Enum):
    """Type of ocean/water experience if mentioned."""
    CALM_PEACEFUL = "calm_peaceful"
    THREATENING_WAVES = "threatening_waves"
    TSUNAMI = "tsunami"
    ARTIFICIAL_POOL = "artificial_pool"
    CONCRETE_BEACH = "concrete_beach"
    DARK_OMINOUS = "dark_ominous"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# SWEDENBORGIAN CORRESPONDENCE CATEGORIES
# =============================================================================

class CorrespondenceCategory(str, Enum):
    """Swedenborgian correspondence category for the experience."""
    MARKETPLACE_COMMERCE = "marketplace_commerce"  # Mall - exchange of knowledges
    INTELLECTUAL_ASCENT = "intellectual_ascent"  # Airport - elevation of understanding
    BABYLON_SELF_LOVE = "babylon_self_love"  # Red Hotel - dominion, self-love
    EXCREMENTITIOUS_HELLS = "excrementitious_hells"  # Dirty bathrooms - exposure of evils
    GYMNASIUM_INSTRUCTION = "gymnasium_instruction"  # School - preparation for heaven
    ARCHIVES_MEMORY = "archives_memory"  # Library - interior memory
    BOUNDARY_INUNDATION = "boundary_inundation"  # Ocean/tsunami - ultimates, falsities
    LOWER_EARTH_VASTATION = "lower_earth_vastation"  # Basement - corporeal memory, purging
    DOCTRINE_TRANSPORT = "doctrine_transport"  # Train - collective movement in doctrine
    DEGREE_CHANGE = "degree_change"  # Elevator - change of spiritual level
    PHANTASY_DELIGHTS = "phantasy_delights"  # Amusement park - sensual pleasures
    NOT_APPLICABLE = "not_applicable"
    UNCLEAR = "unclear"


# =============================================================================
# COMPONENT MODELS
# =============================================================================

class LocationVisited(QuestionnaireBaseModel):
    """A location visited during the dream."""
    
    location_type: PrimaryLocation = Field(
        description="Type of primary location"
    )
    sub_locations: List[SubLocation] = Field(
        default_factory=list,
        description="Sub-locations within this primary location"
    )
    architectural_qualities: List[ArchitecturalQuality] = Field(
        default_factory=list,
        description="Architectural qualities mentioned for this location"
    )
    lighting: LightingQuality = Field(
        default=LightingQuality.NOT_MENTIONED,
        description="Lighting quality at this location"
    )
    color_scheme: ColorScheme = Field(
        default=ColorScheme.NOT_MENTIONED,
        description="Dominant color scheme if mentioned"
    )
    emotional_tone: EmotionalTone = Field(
        default=EmotionalTone.NOT_MENTIONED,
        description="Emotional tone at this location"
    )


class VerticalMovement(QuestionnaireBaseModel):
    """Vertical movement experience (elevator/escalator)."""
    
    elevator_experience: ElevatorExperience = Field(
        default=ElevatorExperience.NOT_MENTIONED,
        description="Type of elevator experience if any"
    )
    escalator_experience: EscalatorExperience = Field(
        default=EscalatorExperience.NOT_MENTIONED,
        description="Type of escalator experience if any"
    )
    direction_attempted: Optional[str] = Field(
        default=None,
        description="Direction attempted (up/down) if specified"
    )
    outcome_successful: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Was the vertical movement successful?"
    )


class TransactionAttempt(QuestionnaireBaseModel):
    """Attempt at commerce or eating."""
    
    type: str = Field(
        description="Type of transaction: 'buying', 'eating', 'finding', 'other'"
    )
    outcome: TransactionOutcome = Field(
        description="Outcome of the transaction attempt"
    )
    details: Optional[str] = Field(
        default=None,
        description="Brief details if provided (e.g., 'trying to buy clothes')"
    )


# =============================================================================
# MAIN RESPONSE MODEL
# =============================================================================

class MallworldResponse(QuestionnaireBaseModel):
    """
    Structured extraction schema for Mall World dream analysis.
    
    Maps phenomenological features to Swedenborgian correspondences.
    """
    
    # === LOCATION DATA ===
    primary_location: PrimaryLocation = Field(
        description="The main/primary location of the dream experience"
    )
    
    locations_visited: List[LocationVisited] = Field(
        default_factory=list,
        description="All locations visited with their features. Include at least the primary location."
    )
    
    connectivity_methods: List[ConnectivityMethod] = Field(
        default_factory=list,
        description="How the dreamer moved between locations"
    )
    
    # === PHENOMENOLOGICAL FEATURES ===
    reality_quality: RealityQuality = Field(
        default=RealityQuality.NOT_MENTIONED,
        description="Overall quality of reality/solidity of the experience"
    )
    
    hyper_reality_mentioned: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Did dreamer explicitly mention hyper-reality or 'more real than real'?"
    )
    
    recurring_dream: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Is this described as a recurring dream or familiar place?"
    )
    
    # === VERTICAL MOVEMENT ===
    vertical_movement: Optional[VerticalMovement] = Field(
        default=None,
        description="Vertical movement experience if any (elevator/escalator)"
    )
    
    # === TRANSACTIONS ===
    transaction_attempts: List[TransactionAttempt] = Field(
        default_factory=list,
        description="Any attempts at buying, eating, or finding things"
    )
    
    # === SPECIAL LOCATIONS ===
    bathroom_condition: BathroomCondition = Field(
        default=BathroomCondition.NOT_MENTIONED,
        description="Condition of bathroom if mentioned"
    )
    
    hotel_character: HotelCharacter = Field(
        default=HotelCharacter.NOT_MENTIONED,
        description="Character of hotel if mentioned"
    )
    
    ocean_experience: OceanExperience = Field(
        default=OceanExperience.NOT_MENTIONED,
        description="Ocean/water experience if mentioned"
    )
    
    # === BEINGS ENCOUNTERED ===
    beings_encountered: List[BeingType] = Field(
        default_factory=list,
        description="Types of beings encountered during the dream"
    )
    
    threatening_presence: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Was there a threatening or demonic presence?"
    )
    
    # === EMOTIONAL/SPIRITUAL ===
    dominant_emotion: EmotionalTone = Field(
        default=EmotionalTone.NOT_MENTIONED,
        description="The dominant emotional tone of the entire experience"
    )
    
    anxiety_triggers: List[str] = Field(
        default_factory=list,
        description="Specific anxiety triggers mentioned (e.g., 'missing flight', 'late for class')"
    )
    
    # === BOUNDARY/LIMIT EXPERIENCES ===
    boundary_experience: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Was there an experience of boundary/edge/limit of the world?"
    )
    
    # === SWEDENBORGIAN MAPPING ===
    primary_correspondence: CorrespondenceCategory = Field(
        description="""Primary Swedenborgian correspondence category. Select based on:
        - Mall/shopping → marketplace_commerce
        - Airport/flying → intellectual_ascent  
        - Red/opulent hotel → babylon_self_love
        - Dirty bathroom → excrementitious_hells
        - School/university → gymnasium_instruction
        - Library → archives_memory
        - Ocean/tsunami → boundary_inundation
        - Basement/underground → lower_earth_vastation
        - Train/subway → doctrine_transport
        - Elevator change → degree_change
        - Amusement park → phantasy_delights"""
    )
    
    secondary_correspondences: List[CorrespondenceCategory] = Field(
        default_factory=list,
        description="Additional correspondence categories if multiple apply"
    )
    
    vastation_indicators: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Are there indicators of spiritual vastation (purging, stripping, exposure)?"
    )
    
    # === METADATA ===
    notable_quotes: List[str] = Field(
        default_factory=list,
        description="Notable direct quotes that capture the phenomenology (max 3)"
    )
    
    analyst_notes: Optional[str] = Field(
        default=None,
        description="Any additional observations not captured by structured fields"
    )
