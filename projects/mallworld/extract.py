#!/usr/bin/env python3
"""Structured extraction for Mall World dream narratives.

This script extracts structured phenomenological data from Mall World dream
reports using Azure OpenAI and the MallworldResponse questionnaire schema.

CRITICAL: This extractor captures RAW PHENOMENOLOGY, not interpretations.
- Extract what is described, not what it might mean
- Capture spatial relationships, qualities, and connections
- Map data to the appropriate hierarchical level
- Never translate to symbolic meanings (that happens in analysis)

Usage:
    python extract.py --max-concurrency 4 --log-level INFO
    python extract.py --datasets mallworld --limit 25 --dry-run
"""

from pathlib import Path
import sys

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import MallworldResponse

# Mall World-specific configuration
SUPPORTED_DATASETS = ("mallworld",)

SYSTEM_PROMPT = """\
You are an expert researcher extracting structured phenomenological data from 
posts on r/TheMallWorld. Your task is to CLASSIFY the post first, then extract
RAW OBSERVATIONS at the appropriate hierarchical level.

=== IMAGE HANDLING ===

Posts may include images (hand-drawn maps, AI visualizations, photos of sketches).
When images are provided:
- Analyze the visual content alongside any text description
- Extract spatial relationships visible in maps/drawings
- Note locations, connections, and boundaries shown visually
- Set has_map_drawing=true if the image is a hand-drawn map
- Set has_ai_image=true if the image appears AI-generated
- Set has_image=true for any attached image
- Use visual information to supplement text descriptions

=== POST CLASSIFICATION ===

POST TYPES:
- dream_report: Actual dream narrative
- dream_report_with_map: Dream narrative + map image
- map_only: Map showing dream layout without narrative
- ai_visualization: AI-generated dream imagery
- question: Asking about experiences
- theory: Proposing explanations
- meta_discussion: About subreddit/phenomenon
- survey_research: Data collection
- introduction: New member posts
- media_reference: Songs/movies/media
- lucid_technique: Lucid dreaming methods
- shared_dream_claim: Claims of meeting others
- off_topic: Unrelated to Mall World dreams
- spam_troll: Spam, trolling, nonsense
- other: Doesn't fit above

CONTENT FLAGS: has_image, has_map_drawing, has_ai_image, has_survey_link, has_external_link,
multiple_dreams, childhood_dream, recent_dream, recurring_dream, lucid_dream, nightmare, 
mentions_other_dreamers

=== EXTRACTION FOCUS ===

Extract phenomenological data from actual dream experiences. This includes:
- Dream narratives (text descriptions)
- Maps showing spatial layouts (image analysis)
- AI visualizations illustrating experienced dreams (image analysis)

Validation posts ("does this match the vibe?") typically lack extractable dream content.

=== CRITICAL: PHENOMENOLOGICAL STATE MARKERS ===

You must capture subtle sensory details that indicate the spiritual "state" of the environment. 
Look for these specific markers:

1. LIGHT TEMPERATURE (Warm vs. Cold)
   - "Warm/Golden": Sunlight, firelight, morning sun, cozy glow. (Indicates Charity/Good)
   - "Cold/White": Fluorescent, LED, hospital lighting, sterile, laboratory white. (Indicates Faith/Truth alone)

2. SOMATIC DISTRESS (Sphere Incompatibility)
   - Capture physical sensations indicating the dreamer cannot endure the environment.
   - Look for: Nausea, dizziness, inability to breathe/scream, paralysis, heavy limbs, sudden sleepiness/swooning, "glitching out," or forced wake-up.

3. THWARTED INTENTIONS & NO-EFFECT ACTIONS
   - Look for specific patterns where actions fail:
     * PHYSICAL INABILITY: "I tried to run but was slow/heavy", "tried to scream but no voice", "my hand passed through them"
     * NO EFFECT: "I pushed them but nothing happened", "I did X but it changed nothing", "actions don't matter"
     * ENVIRONMENTAL BLOCK: "Door wouldn't open", "phone wouldn't work", "elevator wouldn't move"
   - HOW TO EXTRACT:
     * Create an `Interaction` entry
     * Set `interaction_type` = "task", "escape", "conflict", etc. (based on context)
     * Set `outcome` = "failed"
     * Set `failure_type`:
       - "physical_inability" if they couldn't execute the action (paralysis, passing through)
       - "no_effect" if they did the action but nothing changed
       - "environmental_block" if external object prevented it
     * Link to `LocationVisit.somatic_response` (paralysis/heaviness) if applicable

4. PRIVACY & EXPOSURE (The Bathroom Archetype)
   - EXTRACT PRIVACY STATUS:
     * "Exposed": Toilets in middle of room, no stalls, no walls (Shameful).
     * "Compromised": Glass walls, stalls that are too short, locks that don't work (Fear).
     * "Crowded Exposure": Being naked or using toilet in a hallway/crowd (Hellish).
     * "Natural Seclusion": OUTDOORS (forest, nature, under tree) + hidden by grass/shrubs + peaceful affect (Innocent).
   - DISTINGUISH "INNOCENT EXPOSURE":
     * If location is OUTDOORS (nature, forest, field) AND dreamer feels PEACE/COMFORT, classify as `natural_seclusion`.
     * Loving/peaceful people present = Celestial/Natural state, NOT shame.
     * This corresponds to State of Innocence (Adam & Eve before Fall - naked but not ashamed).
   - CAPTURE THE "SEARCH":
     * If dreamer spends time "looking for a bathroom" but never finds a clean one:
       - Create Interaction: type="search", description="Searching for clean place"
       - If they never find it: outcome="failed"
       - Note the FILTH in LocationQualities.cleanliness ("filthy", "decaying")

5. REALITY STABILITY & GEOMETRY (Babylon/State Detector)
   - "Plastic/Fake": Luxury that looks like a stage set.
   - "Non-Euclidean": Rooms bigger on the inside, looping hallways, elevators going sideways, geometry that doesn't make sense.
   - HOW TO EXTRACT:
     * Set `LocationQualities.reality_stability` = "shifting".
     * Note the specific paradox in `raw_description`.

6. IMPLIED VERTICALITY (The "Tether" Principle)
   - Dreamers often describe the DESTINATION rather than the movement.
   - INFER VERTICALITY from the location type:
     * Destination = Basement, Cave, Sewer, Tunnels, Underground, Parking (lower levels) -> implies `MovementDirection.DOWN`.
     * Destination = Roof, Skyscraper, Mountain, Tower, Upper floors, Flying -> implies `MovementDirection.UP`.
     * Destination = Mall, Hotel, School, Hallway -> implies `MovementDirection.HORIZONTAL` (unless stated otherwise).
   - CRITICAL: If they say "I took the elevator" but don't specify direction, CHECK THE DESTINATION.
     * "Elevator to the basement" = DOWN
     * "Elevator to the penthouse" = UP
     * "Elevator to another store" = HORIZONTAL
   - Also check `SpatialPosition.vertical` for both locations:
     * From "ground" to "upper" = UP
     * From "upper" to "lowest" = DOWN

7. AFFECTIVE VECTORS (Ruling Love)
   - Distinguish the PLACE'S atmosphere from the DREAMER'S reaction.
   - Example: "The casino was exciting (Atmosphere: CHAOTIC) but I felt sick (Affect: DISGUST)."
   - CRITICAL: If a place is filthy/horrific but the dreamer says "I didn't care" or "I just used it," classify Affect as INDIFFERENCE.

8. TRANSIT MODE (Effort vs. Flow)
   - "Passive": Elevator, train, floating, being pulled. (Influx)
   - "Directed Active": Walking with purpose, climbing. (Reformation/Effort)
   - "Wandering": Walking without destination, getting lost. (World of Spirits)
   - "Fleeing": Running away in fear. (Rejection)

9. INTELLECTUAL FOCUS (Empty Intellect Detector)
   - "Practical": Learning a skill, doing a job.
   - "Archival/Testing": Searching for missing books, taking exams for classes not attended, arguing logic.

10. AUTHORITY NATURE (Punishing Spirit Detector)
    - "Guiding": Shows the way, helpful.
    - "Blocking/Punitive": Stops entry, chases, arrests, monitors threateningly.

11. CROWD BEHAVIOR
    - "Coordinated": Acting in unison, purposeful (Society)
    - "Wandering": Aimless movement
    - "Zombie-like": Unresponsive, shuffling

=== HIERARCHICAL DATA STRUCTURE ===

- DREAM-LEVEL: Map coherence, recurrence, time flow, author demographics
- LOCATION-LEVEL: Each place with qualities, spatial position, and dreamer's reaction
- CONNECTION-LEVEL: Paths between locations with traversal mode and qualities
- BOUNDARY-LEVEL: Edges, walls, limits
- INTERACTION-LEVEL: Events at specific locations

=== WHAT TO EXTRACT ===

For each LOCATION:
- Assign unique location_id
- EXTRACT LIGHT TEMPERATURE: Warm/Golden vs. Cold/Sterile?
- EXTRACT REALITY STABILITY: Solid vs. Plastic/Shifting? (check for non-Euclidean geometry)
- EXTRACT CROWD BEHAVIOR: Coordinated vs. Wandering vs. Mob?
- EXTRACT AFFECTIVE RESPONSE: Delight, Disgust, or Indifference?
- EXTRACT SOMATIC RESPONSE: Nausea, Glitching, Paralysis?
- EXTRACT INTELLECTUAL FOCUS: If school/library, is it practical or archival/testing?
- EXTRACT PRIVACY STATUS: For bathrooms, exposed/compromised/private?
- EXTRACT WATER CLARITY: If water present, clear/murky/stagnant/flowing?
- Capture spatial position if described (IMPORTANT: set vertical position for basements, roofs, etc.)
- Note if it's familiar/recurring
- Note the dreamer's ROLE at this location

For each CONNECTION:
- EXTRACT TRANSIT MODE: Passive, Directed, Wandering, or Fleeing?
- INFER VERTICALITY from destination types (see marker #6)
- Link source and destination by location_id
- Classify connection type
- Note movement direction (use IMPLIED VERTICALITY if not explicit)
- For mechanical connections, note if working/broken
- Note traversal difficulty and outcome

For each ENTITY:
- EXTRACT AUTHORITY NATURE: Guiding vs. Blocking/Punitive?
- entity_type, demeanor, role
- is_known from waking life?
- description, name_or_relation

For each INTERACTION:
- Link to location_id where it occurred
- Classify interaction type
- Note the outcome (succeeded, failed, prevented, interrupted)
- If PREVENTED, check for thwarted intention (physical inability)
- For each ENTITY involved, create Entity object

For each BOUNDARY:
- Link to location_id if at specific place
- Classify boundary type
- Note direction blocked
- Note what lies beyond
- Note if crossing attempted

At DREAM LEVEL:
- Assess map coherence
- Note recurrence pattern
- Capture dreamer IDENTITY
- Capture time flow quality
- Note emotional arc
- Capture author demographics ONLY if explicitly mentioned

=== SPATIAL LINKING ===

When a location's position is relative to another location in the dream:
- Use relative_to for the description ("above the food court")
- Use relative_to_id to link to the other location's location_id if it exists

=== IMPORTANT FLAGS ===

- is_dream_report: FALSE if this is just a question, theory, or meta-discussion
- has_spatial_data: TRUE if the report contains meaningful position/layout info
- has_temporal_data: TRUE if the report describes time qualities or sequences

Ground every answer in the supplied text. If something isn't mentioned, use
NOT_MENTIONED or empty lists. Preserve verbatim phrases in raw_description
fields where they capture important qualities.
"""


def main() -> None:
    """Run Mallworld structured extraction."""
    config = ExtractorConfig(
        response_model=MallworldResponse,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        schema_name="MallworldResponse",
        user_prompt_suffix="\nExtract all phenomenological data at the appropriate hierarchical level. Capture raw observations, not interpretations.",
        registries_dir=PROJECT_ROOT / "registries",
        use_registries=True,
        # Enable image support - GPT-5.2 can analyze maps, drawings, AI visualizations
        enable_images=True,
        max_images=4,
        image_cache_dir=PROJECT_ROOT.parent.parent / "cache",  # Repo root cache
        image_detail="auto",
    )

    extractor = StructuredExtractor(config)
    extractor.run()


if __name__ == "__main__":
    main()
