#!/usr/bin/env python3
"""
Extraction Test - Model Comparison Script
==========================================
This script is designed to iteratively test and optimize structured data extraction
for NDE narratives. It allows comparison between different Azure OpenAI models.

Usage:
    python extract.py                    # Use default model from secrets (gpt-5.2)
    python extract.py --model gpt-5.1    # Override to use gpt-5.1
    python extract.py --overwrite        # Re-extract existing files
    python extract.py --dry-run          # Preview what would be extracted
"""

from pathlib import Path
import sys

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import NDEAnalysisResponse

# === SYSTEM PROMPT VERSIONS ===
# These can be modified to test different prompting strategies

SYSTEM_PROMPT_V1 = """\
You are an expert researcher who classifies near-death experience (NDE) narratives 
according to the detailed questionnaire schema provided via structured output.

Ground every answer strictly in the supplied testimony. If the narrative omits a 
detail, mark the corresponding enum as not_mentioned or use empty lists rather than 
inferring or guessing.

Focus on identifying:
- NDE phenomenology (OBE, tunnel, light, beings, life review, etc.)
- Greyson scale elements and estimated score
- Aftereffects and life changes
- Any veridical perception claims
- Spiritual or transformative elements
"""

SYSTEM_PROMPT_V2 = """\
You are an expert researcher classifying near-death experience (NDE) narratives.

Ground all answers strictly in the supplied testimony. If the narrative omits a 
detail, use not_mentioned or empty lists rather than inferring.

LIFE REVIEW CLASSIFICATION GUIDANCE:

For the life_review.emotional_tone field, classify based on the ACTUAL emotional 
content described in the account:

1. LOVE - The review focuses on positive emotions and experiences:
   - "mostly good memories" 
   - Feelings of acceptance, warmth, or being loved
   - Memories of joyful events (celebrations, kindness given/received)
   
2. SHAME_OR_REGRET - The review focuses on negative self-judgment:
   - "ashamed", "asked for forgiveness"
   - Shown wrongdoings, times they hurt others
   - Guilt, regret, self-criticism
   
3. MIXED - The review explicitly contains BOTH positive AND negative:
   - "people I had done wrong things to...people I had done good things to"
   - Shows both loving moments AND shameful ones
   - Describes experiencing both gratitude and regret
   
4. NEUTRAL - Factual review without strong emotional coloring

5. NOT_SPECIFIED - Life review occurred but emotional tone not described

The threshold for MIXED requires EXPLICIT evidence of BOTH positive and negative elements.
If the account only mentions one valence, classify as LOVE or SHAME_OR_REGRET accordingly.
"""

# Default to V2 (more detailed guidance for emotional_tone)
SYSTEM_PROMPT = SYSTEM_PROMPT_V2

# Datasets - using registry files
SUPPORTED_DATASETS = ("nderf", "iands")


def main() -> None:
    """Run extraction test pipeline."""
    config = ExtractorConfig(
        response_model=NDEAnalysisResponse,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        schema_name="NDEAnalysisResponse",
        user_prompt_suffix="\nProvide the most accurate structured questionnaire responses possible.",
        registries_dir=PROJECT_ROOT / "registries",
        use_registries=True,
    )

    extractor = StructuredExtractor(config)
    extractor.run()


if __name__ == "__main__":
    main()
