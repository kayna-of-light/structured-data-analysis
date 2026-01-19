#!/usr/bin/env python3
"""Structured extraction for Mall World dream narratives.

This script extracts structured phenomenological data from Mall World dream
reports using Azure OpenAI and the MallworldResponse questionnaire schema.

The analysis maps dream topography to Swedenborgian correspondences,
treating the Mall World as perception of the World of Spirits.

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
You are an expert researcher analyzing Mall World dream narratives for 
phenomenological patterns and spiritual correspondences.

Ground every answer strictly in the supplied dream report. If the narrative 
omits a detail, mark the corresponding enum as not_mentioned or use empty 
lists. Only capture quotes or details that are explicitly present.

Focus on extracting:
- Primary and secondary locations visited (mall, airport, hotel, school, etc.)
- Architectural features (levels, elevators, escalators, tunnels, bathrooms)
- Sensory qualities (lighting, colors, textures, sense of reality)
- Emotional tone and atmosphere (anxiety, peace, dread, familiarity)
- Movement patterns (vertical via elevator/escalator, horizontal via transit)
- Transaction attempts (buying, eating) and their success/failure
- Beings or entities encountered
- Any boundary or limit experiences (ocean, edge, walls)
- Signs of "shifting" or "changing" environments

Map observations to Swedenborgian correspondence categories where applicable:
- Commerce/Mall → exchange of affections and knowledges
- Vertical movement → change of spiritual degree
- Red/opulent hotel → Babylon/self-love
- Dirty bathrooms → exposure of internal evils
- Educational spaces → instruction/gymnasium
- Ocean/tsunami → boundary/inundation
- Basement/underground → Lower Earth/vastation
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
        user_prompt_suffix="\nProvide the most accurate structured questionnaire responses possible.",
        registries_dir=PROJECT_ROOT / "registries",
        use_registries=True,
    )

    extractor = StructuredExtractor(config)
    extractor.run()


if __name__ == "__main__":
    main()
