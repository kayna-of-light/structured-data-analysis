#!/usr/bin/env python3
"""Structured extraction for Near-Death Experience (NDE) narratives.

This script extracts structured data from NDE narratives using Azure OpenAI
and the NDEAnalysisResponse questionnaire schema.

Usage:
    python extract.py --max-concurrency 4 --log-level INFO
    python extract.py --datasets nderf --limit 25 --dry-run
"""

from pathlib import Path
import sys

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import NDEAnalysisResponse

# NDE-specific configuration
SUPPORTED_DATASETS = ("nderf", "iands")

SYSTEM_PROMPT = """\
You are an expert researcher who classifies near-death experience (NDE) narratives 
according to the detailed questionnaire schema provided via structured output.

Ground every answer strictly in the supplied testimony. If the narrative omits a 
detail, mark the corresponding enum as not_mentioned or use empty lists. Only capture 
quotes or free-text details that are explicitly present.

Focus on identifying:
- NDE phenomenology (OBE, tunnel, light, beings, life review, etc.)
- Greyson scale elements and estimated score
- Aftereffects and life changes
- Any veridical perception claims
- Spiritual or transformative elements
"""


def main() -> None:
    """Run NDE structured extraction."""
    config = ExtractorConfig(
        response_model=NDEAnalysisResponse,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        schema_name="NDEAnalysisResponse",
        user_prompt_suffix="\nProvide the most accurate structured questionnaire responses possible.",
    )

    extractor = StructuredExtractor(config)
    extractor.run()


if __name__ == "__main__":
    main()
