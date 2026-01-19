"""
Mall World Dream Phenomenology Extraction Schema.

This schema extracts raw phenomenological data from r/TheMallWorld dream reports
for statistical analysis. The goal is to capture spatial, temporal, and qualitative
data WITHOUT interpretation—interpretation happens in the analysis phase.

DESIGN PRINCIPLES:
1. Data is captured at the appropriate hierarchical level:
   - Dream-level: overall qualities, map coherence, recurrence
   - Location-level: each place with its specific qualities
   - Connection-level: paths between locations with traversal qualities
   - Interaction-level: events at specific locations

2. NO INTERPRETATION during extraction:
   - Capture "disgusting bathroom" not "excrementitious hell correspondence"
   - Capture "elevator going down" not "descent into lower states"
   - The analysis phase maps raw data to correspondences

3. Spatial relationships are first-class data:
   - Relative positions (above, below, adjacent)
   - Cardinal directions if mentioned
   - Center vs periphery
   - Map coherence across dreams

4. Temporal qualities matter:
   - Time of day / lighting (distinct concepts)
   - Sense of time flow
   - Sequence of visits
   - Recurrence patterns
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class QuestionnaireBaseModel(BaseModel):
    """Shared configuration for all questionnaire models."""
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# =============================================================================
# ENUMS - Raw phenomenological categories (NOT interpretive)
# =============================================================================

class MentionResponse(str, Enum):
    """Standard response for presence/absence."""
    YES_EXPLICIT = "yes_explicit"
    IMPLIED = "implied"
    NO = "no"
    NOT_MENTIONED = "not_mentioned"


# --- Location Types (what the place IS, not what it means) ---

class LocationType(str, Enum):
    """Primary location type - what kind of place."""
    MALL = "mall"
    MALL_FOOD_COURT = "mall_food_court"
    MALL_STORE = "mall_store"
    MALL_ARCADE = "mall_arcade"
    MALL_THEATER = "mall_theater"
    
    SCHOOL = "school"
    SCHOOL_CLASSROOM = "school_classroom"
    SCHOOL_GYM = "school_gym"
    SCHOOL_CAFETERIA = "school_cafeteria"
    SCHOOL_LIBRARY = "school_library"
    
    HOTEL = "hotel"
    HOTEL_LOBBY = "hotel_lobby"
    HOTEL_ROOM = "hotel_room"
    HOTEL_POOL = "hotel_pool"
    HOTEL_BALLROOM = "hotel_ballroom"
    
    AIRPORT = "airport"
    AIRPORT_TERMINAL = "airport_terminal"
    AIRPORT_GATE = "airport_gate"
    AIRPORT_SECURITY = "airport_security"
    
    TRAIN_STATION = "train_station"
    BUS_STATION = "bus_station"
    SUBWAY = "subway"
    
    HOSPITAL = "hospital"
    HOSPITAL_ROOM = "hospital_room"
    HOSPITAL_WAITING = "hospital_waiting"
    
    RESTAURANT = "restaurant"
    RESTAURANT_FAST_FOOD = "restaurant_fast_food"
    RESTAURANT_BUFFET = "restaurant_buffet"
    
    BATHROOM = "bathroom"
    BATHROOM_PUBLIC = "bathroom_public"
    BATHROOM_LOCKER_ROOM = "bathroom_locker_room"
    
    PARKING_STRUCTURE = "parking_structure"
    PARKING_LOT = "parking_lot"
    
    WATERPARK = "waterpark"
    POOL = "pool"
    BEACH = "beach"
    AQUARIUM = "aquarium"
    
    AMUSEMENT_PARK = "amusement_park"
    CARNIVAL = "carnival"
    CASINO = "casino"
    
    CHURCH = "church"
    THEATER = "theater"
    MUSEUM = "museum"
    LIBRARY = "library"
    
    HOUSE = "house"
    APARTMENT = "apartment"
    MANSION = "mansion"
    DORM = "dorm"
    
    OFFICE = "office"
    WAREHOUSE = "warehouse"
    FACTORY = "factory"
    
    FOREST = "forest"
    MOUNTAIN = "mountain"
    CAVE = "cave"
    RUINS = "ruins"
    ISLAND = "island"
    
    CITY_STREET = "city_street"
    NEIGHBORHOOD = "neighborhood"
    DOWNTOWN = "downtown"
    SUBURB = "suburb"
    
    BASEMENT = "basement"
    ATTIC = "attic"
    ROOF = "roof"
    UNDERGROUND = "underground"
    
    CRUISE_SHIP = "cruise_ship"
    AIRPLANE = "airplane"
    TRAIN = "train"
    BUS = "bus"
    
    OTHER = "other"
    UNSPECIFIED = "unspecified"


# --- Spatial Position (where in the structure) ---

class VerticalPosition(str, Enum):
    """Vertical position relative to other areas."""
    UPPERMOST = "uppermost"           # Top floor, highest level
    UPPER = "upper"                   # Above ground, upper floors
    GROUND = "ground"                 # Ground level
    LOWER = "lower"                   # Below ground, lower floors
    LOWEST = "lowest"                 # Basement, deepest level
    VARIES = "varies"                 # Position changes
    NOT_MENTIONED = "not_mentioned"


class HorizontalPosition(str, Enum):
    """Horizontal position in the space."""
    CENTER = "center"
    EDGE = "edge"
    CORNER = "corner"
    ENTRANCE = "entrance"
    EXIT = "exit"
    BACK = "back"
    FRONT = "front"
    NOT_MENTIONED = "not_mentioned"


class CardinalDirection(str, Enum):
    """Cardinal direction if mentioned."""
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    NORTHEAST = "northeast"
    NORTHWEST = "northwest"
    SOUTHEAST = "southeast"
    SOUTHWEST = "southwest"
    NOT_MENTIONED = "not_mentioned"


# --- Raw Qualities (phenomenological, not interpretive) ---

class LightQuality(str, Enum):
    """Quality of light at location."""
    BRIGHT_NATURAL = "bright_natural"       # Sunlight, daylight
    BRIGHT_ARTIFICIAL = "bright_artificial" # Fluorescent, harsh
    DIM = "dim"                             # Low light, shadowy
    DARK = "dark"                           # No/minimal light
    FLICKERING = "flickering"               # Unstable light
    COLORED = "colored"                     # Unusual color
    ABSENT = "absent"                       # Complete darkness
    MIXED = "mixed"                         # Multiple types
    NOT_MENTIONED = "not_mentioned"


class TimeOfDay(str, Enum):
    """Time of day at location (distinct from light quality)."""
    MORNING = "morning"
    DAYTIME = "daytime"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    NIGHT = "night"
    TIMELESS = "timeless"             # No sense of time
    INCONSISTENT = "inconsistent"      # Time doesn't make sense
    NOT_MENTIONED = "not_mentioned"


class StateOfPlace(str, Enum):
    """Physical state/condition of the location."""
    NEW = "new"                        # Fresh, newly built
    MAINTAINED = "maintained"          # Good condition
    WORN = "worn"                      # Showing age/use
    DECAYING = "decaying"              # Falling apart
    ABANDONED = "abandoned"            # Left empty, neglected
    DESTROYED = "destroyed"            # Ruined, wrecked
    UNDER_CONSTRUCTION = "under_construction"
    RENOVATING = "renovating"
    MIXED = "mixed"                    # Different areas different states
    NOT_MENTIONED = "not_mentioned"


class Atmosphere(str, Enum):
    """General atmosphere/feeling of place."""
    WELCOMING = "welcoming"
    NEUTRAL = "neutral"
    UNCOMFORTABLE = "uncomfortable"
    OPPRESSIVE = "oppressive"
    THREATENING = "threatening"
    PEACEFUL = "peaceful"
    CHAOTIC = "chaotic"
    EERIE = "eerie"
    NOSTALGIC = "nostalgic"
    WRONG = "wrong"                    # Something off/uncanny
    NOT_MENTIONED = "not_mentioned"


class Crowding(str, Enum):
    """How crowded the location is."""
    EMPTY = "empty"
    SPARSE = "sparse"
    MODERATE = "moderate"
    CROWDED = "crowded"
    PACKED = "packed"
    VARIES = "varies"
    NOT_MENTIONED = "not_mentioned"


class Cleanliness(str, Enum):
    """Cleanliness state of location."""
    STERILE = "sterile"               # Unnaturally clean
    CLEAN = "clean"
    NORMAL = "normal"
    DIRTY = "dirty"
    FILTHY = "filthy"
    DISGUSTING = "disgusting"         # Excrement, rot, etc.
    NOT_MENTIONED = "not_mentioned"


class WaterPresence(str, Enum):
    """Presence and state of water."""
    NONE = "none"
    POOL_CLEAN = "pool_clean"
    POOL_DIRTY = "pool_dirty"
    FOUNTAIN = "fountain"
    FLOOD = "flood"
    LEAK = "leak"
    OCEAN_CALM = "ocean_calm"
    OCEAN_TURBULENT = "ocean_turbulent"
    RIVER = "river"
    RAIN = "rain"
    TSUNAMI = "tsunami"
    SUBMERGED = "submerged"           # Underwater area
    NOT_MENTIONED = "not_mentioned"


# --- Connection/Path Types ---

class ConnectionType(str, Enum):
    """How locations connect to each other."""
    ELEVATOR = "elevator"
    ESCALATOR = "escalator"
    STAIRS = "stairs"
    HALLWAY = "hallway"
    DOOR = "door"
    TUNNEL = "tunnel"
    BRIDGE = "bridge"
    RAMP = "ramp"
    LADDER = "ladder"
    CRAWLSPACE = "crawlspace"
    PORTAL = "portal"                 # Instant transition
    TELEPORT = "teleport"             # Location shift
    OUTSIDE_PATH = "outside_path"
    VEHICLE = "vehicle"
    FLYING = "flying"
    FALLING = "falling"
    SWIMMING = "swimming"
    OTHER = "other"
    UNSPECIFIED = "unspecified"


class MovementDirection(str, Enum):
    """Direction of movement through connection."""
    UP = "up"
    DOWN = "down"
    HORIZONTAL = "horizontal"
    DIAGONAL_UP = "diagonal_up"
    DIAGONAL_DOWN = "diagonal_down"
    UNKNOWN = "unknown"
    NOT_APPLICABLE = "not_applicable"


class TraversalDifficulty(str, Enum):
    """How difficult to traverse the connection."""
    EASY = "easy"
    NORMAL = "normal"
    DIFFICULT = "difficult"
    BLOCKED = "blocked"
    IMPOSSIBLE = "impossible"
    VARIES = "varies"
    NOT_MENTIONED = "not_mentioned"


class MechanismFunction(str, Enum):
    """For mechanical connections (elevator, escalator), how it functions."""
    WORKING_NORMAL = "working_normal"
    WORKING_SLOW = "working_slow"
    WORKING_FAST = "working_fast"
    MALFUNCTIONING = "malfunctioning"
    BROKEN = "broken"
    UNPREDICTABLE = "unpredictable"    # Random behavior
    DANGEROUS = "dangerous"
    NOT_APPLICABLE = "not_applicable"
    NOT_MENTIONED = "not_mentioned"


class TraversalOutcome(str, Enum):
    """Did they successfully traverse?"""
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    PARTIAL = "partial"               # Got somewhere unexpected
    INTERRUPTED = "interrupted"
    STILL_IN_PROGRESS = "still_in_progress"
    NOT_ATTEMPTED = "not_attempted"
    NOT_MENTIONED = "not_mentioned"


# --- Interaction Types ---

class InteractionType(str, Enum):
    """Type of interaction/event."""
    TRANSACTION = "transaction"        # Buying, paying
    NAVIGATION = "navigation"          # Finding way
    SOCIAL = "social"                  # Talking to entities
    TASK = "task"                      # Given task/mission
    ESCAPE = "escape"                  # Fleeing, avoiding
    SEARCH = "search"                  # Looking for something
    OBSERVATION = "observation"        # Just watching
    CONFLICT = "conflict"              # Fighting, confrontation
    OTHER = "other"


class InteractionOutcome(str, Enum):
    """Result of the interaction."""
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    PREVENTED = "prevented"            # Blocked from attempting
    INTERRUPTED = "interrupted"
    ABANDONED = "abandoned"            # Gave up
    ONGOING = "ongoing"                # Still happening
    NOT_MENTIONED = "not_mentioned"


class EntityType(str, Enum):
    """Type of entity encountered."""
    KNOWN_PERSON = "known_person"      # Real person dreamer knows
    STRANGER = "stranger"              # Unknown human
    CROWD = "crowd"                    # Faceless masses
    AUTHORITY = "authority"            # Police, guards, staff
    GUIDE = "guide"                    # Someone helpful
    THREAT = "threat"                  # Hostile entity
    DECEASED = "deceased"              # Dead person dreamer knew
    CREATURE = "creature"              # Non-human
    SHADOW = "shadow"                  # Shadowy figure
    WATCHER = "watcher"                # Observer entity
    CHILD = "child"                    # Child entity
    FAMILY_MEMBER = "family_member"    # Family (alive)
    FRIEND = "friend"                  # Friend (alive)
    COWORKER = "coworker"              # Work colleague
    FACELESS = "faceless"              # Entity without face
    MANNEQUIN = "mannequin"            # Mannequin-like entity
    OTHER = "other"
    NONE = "none"


class EntityDemeanor(str, Enum):
    """How the entity behaves toward the dreamer."""
    HELPFUL = "helpful"                # Actively helping
    FRIENDLY = "friendly"              # Pleasant, welcoming
    NEUTRAL = "neutral"                # Neither positive nor negative
    INDIFFERENT = "indifferent"        # Ignoring the dreamer
    UNFRIENDLY = "unfriendly"          # Cold, unwelcoming
    HOSTILE = "hostile"                # Actively antagonistic
    THREATENING = "threatening"        # Menacing
    WATCHING = "watching"              # Just observing
    CONFUSING = "confusing"            # Behavior doesn't make sense
    NOT_MENTIONED = "not_mentioned"


class EntityRole(str, Enum):
    """What role the entity plays in the dream."""
    CASHIER = "cashier"                # Working register
    SECURITY = "security"              # Security guard
    STAFF = "staff"                    # Generic employee
    TEACHER = "teacher"                # Teacher/instructor
    STUDENT = "student"                # Fellow student
    CUSTOMER = "customer"              # Fellow customer
    GUIDE = "guide"                    # Showing the way
    BLOCKER = "blocker"                # Preventing access
    CHASER = "chaser"                  # Pursuing dreamer
    COMPANION = "companion"            # Traveling with dreamer
    BYSTANDER = "bystander"            # Just present
    AUTHORITY = "authority"            # Position of power
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class DreamerIdentity(str, Enum):
    """Who is the dreamer in this dream?"""
    CURRENT_SELF = "current_self"            # Themselves at current age
    YOUNGER_SELF = "younger_self"            # Themselves but younger
    CHILD_SELF = "child_self"                # Themselves as a child
    OLDER_SELF = "older_self"                # Themselves but older
    DIFFERENT_PERSON = "different_person"    # Someone else entirely
    OBSERVER_ONLY = "observer_only"          # Just watching, no body
    MULTIPLE = "multiple"                    # Shifts between identities
    UNCLEAR = "unclear"                      # Identity is ambiguous
    NOT_MENTIONED = "not_mentioned"


class DreamerRole(str, Enum):
    """What role/function does the dreamer have at a location?"""
    CUSTOMER = "customer"                    # Shopping, browsing
    EMPLOYEE = "employee"                    # Working there
    STUDENT = "student"                      # Attending school
    TEACHER = "teacher"                      # Teaching
    RESIDENT = "resident"                    # Living there
    GUEST = "guest"                          # Hotel guest, visitor
    PATIENT = "patient"                      # In hospital/medical
    TRAVELER = "traveler"                    # Passing through, in transit
    LOST = "lost"                            # Lost, trying to find way
    ESCAPEE = "escapee"                      # Trying to escape/leave
    EXPLORER = "explorer"                    # Deliberately exploring
    OWNER = "owner"                          # Owns the place
    MANAGER = "manager"                      # Runs/manages things
    SECURITY = "security"                    # Security role
    PERFORMER = "performer"                  # Performing, on stage
    AUDIENCE = "audience"                    # Watching performance
    HOMELESS = "homeless"                    # Living rough in the space
    TRESPASSER = "trespasser"                # Not supposed to be there
    PRISONER = "prisoner"                    # Trapped, held against will
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# COMPONENT MODELS - Nested at appropriate levels
# =============================================================================

class LocationQualities(QuestionnaireBaseModel):
    """Raw phenomenological qualities of a specific location."""
    
    light: LightQuality = Field(
        default=LightQuality.NOT_MENTIONED,
        description="Quality of light at this specific location"
    )
    time_of_day: TimeOfDay = Field(
        default=TimeOfDay.NOT_MENTIONED,
        description="Perceived time of day at this location"
    )
    state: StateOfPlace = Field(
        default=StateOfPlace.NOT_MENTIONED,
        description="Physical condition/state of this location"
    )
    atmosphere: Atmosphere = Field(
        default=Atmosphere.NOT_MENTIONED,
        description="Emotional atmosphere at this location"
    )
    crowding: Crowding = Field(
        default=Crowding.NOT_MENTIONED,
        description="How crowded this location is"
    )
    cleanliness: Cleanliness = Field(
        default=Cleanliness.NOT_MENTIONED,
        description="Cleanliness state - especially note disgusting conditions"
    )
    water_presence: WaterPresence = Field(
        default=WaterPresence.NOT_MENTIONED,
        description="Any water features and their state"
    )
    
    raw_description: Optional[str] = Field(
        default=None,
        description="Key descriptive phrases from the text about this location (verbatim or close paraphrase)"
    )


class SpatialPosition(QuestionnaireBaseModel):
    """Position of a location in the overall spatial structure."""
    
    vertical: VerticalPosition = Field(
        default=VerticalPosition.NOT_MENTIONED,
        description="Vertical position (upper floors, ground, basement, etc.)"
    )
    horizontal: HorizontalPosition = Field(
        default=HorizontalPosition.NOT_MENTIONED,
        description="Horizontal position (center, edge, entrance, etc.)"
    )
    cardinal: CardinalDirection = Field(
        default=CardinalDirection.NOT_MENTIONED,
        description="Cardinal direction if mentioned (north, south, etc.)"
    )
    
    relative_to: Optional[str] = Field(
        default=None,
        description="What this position is relative to (e.g., 'above the food court', 'behind the school')"
    )
    relative_to_id: Optional[str] = Field(
        default=None,
        description="If relative_to refers to another location in this dream, its location_id"
    )


class LocationVisit(QuestionnaireBaseModel):
    """A single location visited during the dream."""
    
    location_id: str = Field(
        description="Unique identifier for this location in this dream (e.g., 'loc_1', 'loc_2')"
    )
    location_type: LocationType = Field(
        description="What type of place this is"
    )
    location_name: Optional[str] = Field(
        default=None,
        description="Specific name if given (e.g., 'Spencer's', 'the blue bathroom')"
    )
    
    position: SpatialPosition = Field(
        default_factory=SpatialPosition,
        description="Where this location sits in the spatial structure"
    )
    qualities: LocationQualities = Field(
        default_factory=LocationQualities,
        description="Raw phenomenological qualities of this location"
    )
    
    is_familiar: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Does the dreamer recognize this as a recurring location?"
    )
    is_accessible: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Can the dreamer access/enter this location?"
    )
    
    dreamer_role: DreamerRole = Field(
        default=DreamerRole.NOT_MENTIONED,
        description="What role does the dreamer have at this location (customer, employee, student, etc.)"
    )
    
    visit_order: Optional[int] = Field(
        default=None,
        description="Order in which this location was visited (1 = first, 2 = second, etc.)"
    )


class Connection(QuestionnaireBaseModel):
    """A path or connection between two locations."""
    
    from_location_id: str = Field(
        description="ID of the source location"
    )
    to_location_id: str = Field(
        description="ID of the destination location"
    )
    
    connection_type: ConnectionType = Field(
        description="How these locations connect"
    )
    direction: MovementDirection = Field(
        default=MovementDirection.UNKNOWN,
        description="Direction of travel through this connection"
    )
    
    difficulty: TraversalDifficulty = Field(
        default=TraversalDifficulty.NOT_MENTIONED,
        description="How difficult to traverse"
    )
    mechanism_function: MechanismFunction = Field(
        default=MechanismFunction.NOT_APPLICABLE,
        description="For elevators/escalators, how the mechanism behaves"
    )
    outcome: TraversalOutcome = Field(
        default=TraversalOutcome.NOT_MENTIONED,
        description="Did they successfully traverse this connection?"
    )
    
    qualities: Optional[str] = Field(
        default=None,
        description="Notable qualities of the connection itself (e.g., 'narrow and dark', 'endless hallway')"
    )


class Entity(QuestionnaireBaseModel):
    """An entity encountered during the dream."""
    
    entity_type: EntityType = Field(
        description="What type of entity this is"
    )
    demeanor: EntityDemeanor = Field(
        default=EntityDemeanor.NOT_MENTIONED,
        description="How the entity behaves toward the dreamer"
    )
    role: EntityRole = Field(
        default=EntityRole.NOT_MENTIONED,
        description="What role this entity plays in the dream"
    )
    
    is_known: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Does the dreamer know this entity from waking life?"
    )
    is_recurring: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Has this entity appeared in previous dreams?"
    )
    
    description: Optional[str] = Field(
        default=None,
        description="Brief description if given (e.g., 'old woman in red', 'faceless man in suit')"
    )
    name_or_relation: Optional[str] = Field(
        default=None,
        description="Name or relation if mentioned (e.g., 'my grandmother', 'John')"
    )


class Interaction(QuestionnaireBaseModel):
    """An interaction or event at a specific location."""
    
    location_id: str = Field(
        description="ID of the location where this happened"
    )
    
    interaction_type: InteractionType = Field(
        description="Type of interaction"
    )
    description: str = Field(
        description="Brief description of what happened"
    )
    
    outcome: InteractionOutcome = Field(
        default=InteractionOutcome.NOT_MENTIONED,
        description="Result of the interaction"
    )
    
    entities_involved: List[Entity] = Field(
        default_factory=list,
        description="Entities involved in this interaction"
    )
    
    # Transaction-specific
    transaction_item: Optional[str] = Field(
        default=None,
        description="For transactions: what was being bought/sold"
    )
    transaction_blocker: Optional[str] = Field(
        default=None,
        description="For failed transactions: what prevented it"
    )


# ============================================================================
# BOUNDARY AND DEMOGRAPHIC ENUMS
# These must be defined before the models that use them
# ============================================================================

class Gender(str, Enum):
    """Author's gender if mentioned."""
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class AgeRange(str, Enum):
    """Author's age range if mentioned or inferrable."""
    CHILD = "child"                      # Under 13
    TEEN = "teen"                        # 13-19
    YOUNG_ADULT = "young_adult"          # 20-29
    ADULT = "adult"                      # 30-49
    MIDDLE_AGED = "middle_aged"          # 50-64
    SENIOR = "senior"                    # 65+
    NOT_MENTIONED = "not_mentioned"


class BoundaryType(str, Enum):
    """Type of boundary/edge encountered."""
    OCEAN = "ocean"                      # Water boundary
    WALL = "wall"                        # Physical wall/barrier
    CLIFF = "cliff"                      # Drop-off, edge
    FENCE = "fence"                      # Permeable barrier
    VOID = "void"                        # Nothingness beyond
    FOG = "fog"                          # Visibility boundary
    DARKNESS = "darkness"                # Light boundary
    INVISIBLE = "invisible"              # Can't go further, no visible reason
    LOCKED = "locked"                    # Locked door/gate
    GUARDED = "guarded"                  # Entity preventing passage
    END_OF_ROAD = "end_of_road"          # Path simply ends
    EDGE_OF_MAP = "edge_of_map"          # Explicit edge of the world
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class BeyondBoundary(str, Enum):
    """What is perceived beyond the boundary?"""
    VISIBLE_LOCATION = "visible_location"  # Can see another place
    OCEAN_WATER = "ocean_water"            # Water extends
    VOID_NOTHING = "void_nothing"          # Empty/nothing
    DARKNESS = "darkness"                  # Can't see
    FOG_OBSCURED = "fog_obscured"          # Blocked by fog
    UNKNOWN = "unknown"                    # Just can't tell
    THREATENING = "threatening"            # Something bad
    BEAUTIFUL = "beautiful"                # Something appealing
    HOME = "home"                          # Real world/waking
    NOT_MENTIONED = "not_mentioned"


# ============================================================================
# POST CLASSIFICATION ENUMS
# ============================================================================

class PostType(str, Enum):
    """Primary classification of what kind of post this is."""
    DREAM_REPORT = "dream_report"              # Actual dream experience (PRIMARY USE)
    DREAM_REPORT_WITH_MAP = "dream_report_with_map"  # Dream + drawn map image
    MAP_ONLY = "map_only"                      # Just a map/drawing, no narrative
    AI_VISUALIZATION = "ai_visualization"      # AI-generated images of dreams
    QUESTION = "question"                      # Asking if others experience X
    THEORY = "theory"                          # Proposing explanation/theory
    META_DISCUSSION = "meta_discussion"        # About the subreddit/phenomenon
    SURVEY_RESEARCH = "survey_research"        # Surveys, data collection
    INTRODUCTION = "introduction"              # "Just found this sub" posts
    MEDIA_REFERENCE = "media_reference"        # Song/movie/game reminds of MW
    LUCID_TECHNIQUE = "lucid_technique"        # Tips for lucid dreaming in MW
    SHARED_DREAM_CLAIM = "shared_dream_claim"  # Claims of shared dreams
    OFF_TOPIC = "off_topic"                    # Unrelated to Mall World dreams
    SPAM_TROLL = "spam_troll"                  # Spam, trolling, nonsense
    OTHER = "other"


class PostContentFlag(str, Enum):
    """Flags for content characteristics (can have multiple)."""
    HAS_IMAGE = "has_image"                    # Post contains image(s)
    HAS_MAP_DRAWING = "has_map_drawing"        # Contains hand-drawn map
    HAS_AI_IMAGE = "has_ai_image"              # Contains AI-generated image
    HAS_SURVEY_LINK = "has_survey_link"        # Contains survey/form link
    HAS_EXTERNAL_LINK = "has_external_link"    # Links to other content
    MULTIPLE_DREAMS = "multiple_dreams"        # Describes more than one dream
    CHILDHOOD_DREAM = "childhood_dream"        # Dream from childhood
    RECENT_DREAM = "recent_dream"              # Dream from last few days
    RECURRING_DREAM = "recurring_dream"        # Mentions recurrence
    LUCID_DREAM = "lucid_dream"                # Achieved lucidity
    NIGHTMARE = "nightmare"                    # Explicitly described as nightmare
    MENTIONS_OTHER_DREAMERS = "mentions_other_dreamers"  # References shared experience


class DetailLevel(str, Enum):
    """How much detail/information the post contains."""
    MINIMAL = "minimal"          # Brief mention, no specific details
    LOW = "low"                  # Basic description, few details
    MODERATE = "moderate"        # Reasonable detail, some specifics
    HIGH = "high"                # Rich detail, many specifics
    EXTENSIVE = "extensive"      # Very detailed, comprehensive narrative


# ============================================================================
# BOUNDARY AND DEMOGRAPHIC MODELS
# ============================================================================

class Boundary(QuestionnaireBaseModel):
    """A boundary or edge of the map/world."""
    
    location_id: Optional[str] = Field(
        default=None,
        description="ID of the location where boundary is encountered (if at a specific place)"
    )
    
    boundary_type: BoundaryType = Field(
        description="What type of boundary this is"
    )
    direction: CardinalDirection = Field(
        default=CardinalDirection.NOT_MENTIONED,
        description="Which direction the boundary blocks (if mentioned)"
    )
    
    beyond: BeyondBoundary = Field(
        default=BeyondBoundary.NOT_MENTIONED,
        description="What is perceived beyond the boundary"
    )
    can_see_beyond: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Can the dreamer see past the boundary?"
    )
    
    crossing_attempted: MentionResponse = Field(
        default=MentionResponse.NOT_MENTIONED,
        description="Did the dreamer try to cross the boundary?"
    )
    crossing_outcome: TraversalOutcome = Field(
        default=TraversalOutcome.NOT_MENTIONED,
        description="If attempted, what happened?"
    )
    
    description: Optional[str] = Field(
        default=None,
        description="Raw description of the boundary"
    )


class AuthorDemographics(QuestionnaireBaseModel):
    """Demographic information about the author if mentioned."""
    
    gender: Gender = Field(
        default=Gender.NOT_MENTIONED,
        description="Author's gender if mentioned"
    )
    age_range: AgeRange = Field(
        default=AgeRange.NOT_MENTIONED,
        description="Author's current age range if mentioned or inferrable"
    )
    age_explicit: Optional[int] = Field(
        default=None,
        description="Exact age if explicitly stated"
    )
    
    dreams_since_age: Optional[int] = Field(
        default=None,
        description="Age when Mall World dreams started (if mentioned)"
    )
    dreams_duration_years: Optional[int] = Field(
        default=None,
        description="How many years they've had these dreams (if mentioned)"
    )


class PostClassification(QuestionnaireBaseModel):
    """Classification of the post type for filtering and analysis routing."""
    
    post_type: PostType = Field(
        description="Primary classification of this post"
    )
    content_flags: List[PostContentFlag] = Field(
        default_factory=list,
        description="Content characteristics flags"
    )
    
    detail_level: DetailLevel = Field(
        default=DetailLevel.MODERATE,
        description="How much detail/information this post contains"
    )
    
    # Usefulness for our analysis
    has_extractable_dream: bool = Field(
        default=False,
        description="Does this post contain a dream that can be extracted?"
    )
    has_spatial_information: bool = Field(
        default=False,
        description="Does the post contain useful spatial/map information?"
    )
    has_map_image: bool = Field(
        default=False,
        description="Does this post include a map drawing that should be manually reviewed?"
    )
    
    # For non-dream posts that are still useful
    theory_summary: Optional[str] = Field(
        default=None,
        description="If theory post: brief summary of the theory proposed"
    )
    question_topic: Optional[str] = Field(
        default=None,
        description="If question post: what are they asking about?"
    )
    
    # Skip flag
    should_skip_extraction: bool = Field(
        default=False,
        description="Should dream extraction be skipped for this post?"
    )
    skip_reason: Optional[str] = Field(
        default=None,
        description="Why extraction should be skipped"
    )


# =============================================================================
# DREAM-LEVEL DATA
# =============================================================================

class MapCoherence(str, Enum):
    """Does the author describe a consistent spatial structure?"""
    HIGHLY_COHERENT = "highly_coherent"      # Clear, consistent map
    MOSTLY_COHERENT = "mostly_coherent"      # Generally consistent
    PARTIALLY_COHERENT = "partially_coherent" # Some consistency
    INCOHERENT = "incoherent"                # Contradictory/shifting
    SINGLE_LOCATION = "single_location"      # Only one place, n/a
    NOT_ENOUGH_INFO = "not_enough_info"


class RecurrencePattern(str, Enum):
    """Is this a recurring dream location?"""
    FIRST_VISIT = "first_visit"
    RECURRING = "recurring"
    VARIATION = "variation"              # Similar but different
    LONG_TERM_RECURRING = "long_term_recurring"  # Years of visits
    NOT_MENTIONED = "not_mentioned"


class TimeFlow(str, Enum):
    """How does time flow in the dream?"""
    NORMAL = "normal"
    SLOW = "slow"
    FAST = "fast"
    FROZEN = "frozen"
    LOOPING = "looping"
    COMPRESSED = "compressed"            # Much time passes quickly
    INCONSISTENT = "inconsistent"
    NOT_MENTIONED = "not_mentioned"


class DreamMeta(QuestionnaireBaseModel):
    """Dream-level metadata and overall qualities."""
    
    map_coherence: MapCoherence = Field(
        default=MapCoherence.NOT_ENOUGH_INFO,
        description="Does the author describe a spatially consistent world?"
    )
    recurrence: RecurrencePattern = Field(
        default=RecurrencePattern.NOT_MENTIONED,
        description="Is this a recurring dream/location?"
    )
    time_flow: TimeFlow = Field(
        default=TimeFlow.NOT_MENTIONED,
        description="How does time seem to flow in the dream?"
    )
    
    # Author demographics
    author: AuthorDemographics = Field(
        default_factory=AuthorDemographics,
        description="Demographic information about the author if mentioned"
    )
    
    # Dreamer identity in the dream
    dreamer_identity: DreamerIdentity = Field(
        default=DreamerIdentity.NOT_MENTIONED,
        description="Who is the dreamer in this dream (current self, younger self, different person)?"
    )
    occupation_in_dream: Optional[str] = Field(
        default=None,
        description="If the dreamer has a specific job/occupation in the dream (raw text)"
    )
    
    # Overall emotional arc
    initial_emotion: Optional[str] = Field(
        default=None,
        description="Emotional state at start of dream"
    )
    final_emotion: Optional[str] = Field(
        default=None,
        description="Emotional state at end/upon waking"
    )
    
    # Author meta-commentary
    author_theory: Optional[str] = Field(
        default=None,
        description="Does the author propose a theory about what mall world is?"
    )
    is_asking_if_shared: bool = Field(
        default=False,
        description="Is the author asking if others share this experience?"
    )


# =============================================================================
# MAIN RESPONSE MODEL
# =============================================================================

class MallworldResponse(QuestionnaireBaseModel):
    """
    Complete extraction from a Mall World dream report.
    
    Captures raw phenomenological data at appropriate hierarchical levels:
    - Dream-level: overall qualities, recurrence, map coherence, demographics
    - Location-level: each place with its specific qualities and position
    - Connection-level: paths between locations with traversal qualities
    - Boundary-level: edges, walls, limits of the world
    - Interaction-level: events at specific locations
    
    NO INTERPRETATION: This captures what is described, not what it means.
    Correspondence mapping happens in the analysis phase.
    """
    
    # Post classification (ALWAYS extracted first)
    classification: PostClassification = Field(
        default_factory=PostClassification,
        description="Classification of the post type - determines extraction routing"
    )
    
    # Dream-level metadata
    meta: DreamMeta = Field(
        default_factory=DreamMeta,
        description="Dream-level metadata and overall qualities"
    )
    
    # Locations visited (with their qualities)
    locations: List[LocationVisit] = Field(
        default_factory=list,
        description="All locations mentioned in the dream, with their qualities and positions"
    )
    
    # Connections between locations
    connections: List[Connection] = Field(
        default_factory=list,
        description="Paths and connections between locations"
    )
    
    # Boundaries/edges of the world
    boundaries: List[Boundary] = Field(
        default_factory=list,
        description="Boundaries, edges, or limits of the map/world encountered"
    )
    
    # Interactions at locations
    interactions: List[Interaction] = Field(
        default_factory=list,
        description="Events and interactions that occurred at specific locations"
    )
    
    # Extraction quality
    has_spatial_data: bool = Field(
        default=False,
        description="Does this report contain meaningful spatial/positional information?"
    )
    has_temporal_data: bool = Field(
        default=False,
        description="Does this report contain meaningful temporal information?"
    )
    extraction_confidence: Optional[str] = Field(
        default=None,
        description="How confident is the extraction? (high/medium/low/minimal)"
    )
    extraction_notes: Optional[str] = Field(
        default=None,
        description="Any notes about extraction difficulties or ambiguities"
    )
