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
RAW OBSERVATIONS at the appropriate hierarchical level—NOT interpret their meaning.

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

=== RAW PHENOMENOLOGY EXTRACTION ===

=== RAW PHENOMENOLOGY EXTRACTION ===

Capture what is described, not interpretations:
- Extract "disgusting bathroom with no privacy" NOT "excrementitious correspondence"
- Extract "elevator going down to basement" NOT "descent to lower states"
- Extract "couldn't pay, card didn't work" NOT "frustrated worldly attachment"

HIERARCHICAL DATA STRUCTURE:
- DREAM-LEVEL: Map coherence, recurrence, time flow, author demographics
- LOCATION-LEVEL: Each place with qualities and spatial position
- CONNECTION-LEVEL: Paths between locations with traversal qualities
- BOUNDARY-LEVEL: Edges, walls, limits
- INTERACTION-LEVEL: Events at specific locations

SPATIAL RELATIONSHIPS:
- Vertical: upper floors, ground level, basement, underground
- Horizontal: center, edge, entrance, back
- Relative: "school is above the mall", "bathroom behind food court"
- Cardinal: north/south/east/west (when mentioned)

CONNECTIONS AS DATA:
- Type: elevator, stairs, hallway, door, tunnel, teleport
- Direction: up, down, horizontal
- Function: working, broken, unpredictable, dangerous
   - Did traversal succeed? (reached destination, got lost, got stuck)

5. BOUNDARIES AND EDGES ARE CRITICAL
   - Note any edges of the world: oceans, walls, cliffs, barriers, void
   - What direction is blocked? (north, south, edge of map)
   - What lies beyond? (void, unknown, visible but unreachable, described otherwhere)
   - Was crossing attempted? What happened?

6. DREAMER IDENTITY AND ROLES
   - WHO is the dreamer? (current self, younger self, child self, different person, observer)
   - What ROLE do they have at each location? (customer, employee, student, lost, escapee)
   - Roles can VARY by location (student at school, customer at mall)
   - If they mention a specific job/occupation in the dream, capture it

7. CAPTURE RAW QUALITIES
   - Light: bright/dim/dark, natural/artificial, flickering
   - State: new/maintained/worn/decaying/abandoned/destroyed
   - Atmosphere: welcoming/neutral/oppressive/eerie/wrong
   - Cleanliness: sterile/clean/dirty/filthy/disgusting
   - Crowding: empty/sparse/moderate/crowded/packed
   - Water: none/clean pool/dirty pool/flood/leak/ocean/tsunami

7. AUTHOR DEMOGRAPHICS (if mentioned)
   - Gender: only if author explicitly states
   - Age range: if author mentions their age
   - Don't infer—only capture what is explicitly stated

=== WHAT TO EXTRACT ===

For each LOCATION mentioned:
- Assign a unique location_id (loc_1, loc_2, etc.)
- Classify the location type (mall, school, hotel, bathroom, etc.)
- Capture its spatial position if described
- Capture its phenomenological qualities (light, state, atmosphere, etc.)
- Note if it's familiar/recurring to the dreamer
- Note the dreamer's ROLE at this location (customer, employee, student, lost, etc.)
- Note visit order if determinable

For each CONNECTION between locations:
- Link source and destination by location_id
- Classify connection type (elevator, stairs, hallway, etc.)
- Note movement direction (up, down, horizontal)
- For mechanical connections, note if working/broken/malfunctioning
- Note traversal difficulty and outcome

For each BOUNDARY encountered:
- Link to location_id if the boundary is at a specific place
- Classify boundary type (ocean, wall, cliff, edge_of_world, barrier, void)
- Note the direction that is blocked
- Note what lies beyond (void, unreachable_visible, unknown, threatening)
- Note if crossing was attempted and the outcome

For each INTERACTION at a location:
- Link to location_id where it occurred
- Classify interaction type (transaction, navigation, social, escape, etc.)
- Note the outcome (succeeded, failed, prevented, interrupted)
- For transactions, note what was being bought and what blocked it
- For each ENTITY involved, create an Entity object with:
  * entity_type: what kind (stranger, authority, deceased, creature, etc.)
  * demeanor: how they behave (helpful, hostile, indifferent, watching)
  * role: their function (cashier, security, guide, blocker, companion)
  * is_known: does dreamer know them from waking life?
  * description: brief appearance if given ("old woman in red")
  * name_or_relation: if mentioned ("my grandmother", "John")

At DREAM LEVEL:
- Assess map coherence (does the space make consistent sense?)
- Note recurrence pattern (first visit, recurring, long-term recurring)
- Capture dreamer IDENTITY (current self, younger self, different person, observer)
- If dreamer has a specific occupation/job in the dream, capture it
- Capture time flow quality (normal, slow, frozen, looping)
- Note emotional arc (initial and final emotional states)
- Flag if author proposes theories or asks if experience is shared
- Capture author demographics ONLY if explicitly mentioned (gender, age)

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
