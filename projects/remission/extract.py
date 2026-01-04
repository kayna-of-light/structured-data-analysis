#!/usr/bin/env python3
"""Structured extraction for spontaneous remission case narratives.

This script extracts structured data from remission case narratives using
Azure OpenAI and the RemissionAnalysisResponse questionnaire schema.

Usage:
    python extract.py --max-concurrency 4 --log-level INFO
    python extract.py --datasets radicalremission --limit 25 --dry-run
"""

from pathlib import Path
import sys

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import ExtractorConfig, StructuredExtractor
from models import RemissionAnalysisResponse

# Remission-specific configuration
SUPPORTED_DATASETS = (
    "radicalremission",
    "pubmed",
    "pmc",
    "nderf_healing",
    "healthtalk",
)

SYSTEM_PROMPT = """\
You are an expert researcher who analyzes spontaneous remission and radical healing 
case narratives according to the detailed questionnaire schema provided via structured output.

Your goal is to extract both medical 'ground truth' (diagnosis, treatment, outcome) and 
psycho-spiritual factors (Turner's 9 factors, existential shifts, anomalous experiences).

Ground every answer strictly in the supplied testimony. If the narrative omits a 
detail, mark the corresponding enum as not_mentioned or use empty lists. Only capture 
quotes or free-text details that are explicitly present.

Turner's 9 Factors to identify:
1. Radically changing diet
2. Taking control of health
3. Following intuition  
4. Using herbs and supplements
5. Releasing suppressed emotions
6. Increasing positive emotions
7. Embracing social support
8. Deepening spiritual connection
9. Having strong reasons for living

Also identify:
- Medical details (diagnosis, staging, treatment history)
- Remission outcome and verification level
- Existential shift markers (surrender, fear-to-love, authenticity)
- Any anomalous experiences (NDE, STE)
- Temporal ordering of transformation vs physical healing
"""


def main() -> None:
    """Run remission structured extraction."""
    config = ExtractorConfig(
        response_model=RemissionAnalysisResponse,
        system_prompt=SYSTEM_PROMPT,
        supported_datasets=SUPPORTED_DATASETS,
        data_root=PROJECT_ROOT.parent.parent / "data",
        output_root=PROJECT_ROOT / "structured",
        secrets_path=PROJECT_ROOT.parent.parent / "secrets" / "azure_openai.env",
        schema_name="RemissionAnalysisResponse",
        user_prompt_suffix=(
            "\nAnalyze this remission case according to the structured questionnaire. "
            "Extract medical details, identify which of Turner's 9 factors are present, "
            "note any anomalous experiences (NDE/STE), and assess the validation tier."
        ),
    )

    extractor = StructuredExtractor(config)
    extractor.run()


if __name__ == "__main__":
    main()
