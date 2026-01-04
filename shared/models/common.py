"""
Common models and enums shared across NDE and Remission analysis.

These base classes and enums are used by both questionnaire schemas
to ensure consistency in how narratives are analyzed.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict


class QuestionnaireBaseModel(BaseModel):
    """
    Shared configuration for all questionnaire models.
    
    Features:
    - Forbids extra fields (strict schema)
    - Allows field aliasing for flexibility
    """
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class MentionResponse(str, Enum):
    """
    Standard mention detection response.
    
    Used throughout both NDE and Remission questionnaires to indicate
    whether a particular element was mentioned in the narrative.
    """
    YES_EXPLICIT = "yes_explicit"        # Clearly stated in narrative
    IMPLIED = "implied"                  # Reasonably inferred but not stated
    NO = "no"                            # Explicitly denied or contradicted
    NOT_MENTIONED = "not_mentioned"      # Simply not addressed in narrative


class DataSource(str, Enum):
    """
    Source of the case data.
    
    Used to track provenance of analyzed cases across both projects.
    """
    # NDE sources
    NDERF = "nderf"                      # Near Death Experience Research Foundation
    IANDS = "iands"                      # International Association for Near-Death Studies
    
    # Remission sources  
    PMC = "pmc"                          # PubMed Central case reports
    RADICAL_REMISSION = "radical_remission"  # RadicalRemission.com
    LOURDES = "lourdes"                  # Lourdes Medical Bureau
    IONS = "ions"                        # Institute of Noetic Sciences
    
    # Generic
    OTHER = "other"


def coerce_mention_response(v: Any) -> str:
    """
    Convert boolean/variant values to MentionResponse strings.
    
    LLMs sometimes return boolean or variant string values instead of
    the exact enum. This function normalizes them.
    
    Args:
        v: Input value (bool, str, or other)
        
    Returns:
        Normalized MentionResponse value string
    """
    if isinstance(v, bool):
        return "yes_explicit" if v else "not_mentioned"
    if isinstance(v, str):
        v_lower = v.lower().strip()
        # Handle common LLM variations
        if v_lower in ("true", "yes", "y", "1"):
            return "yes_explicit"
        if v_lower in ("false", "no", "n", "0", "none"):
            return "not_mentioned"
        if v_lower in ("unknown", "uncertain", "unclear", "n/a", "na"):
            return "not_mentioned"
    return v
