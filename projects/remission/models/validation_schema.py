"""
Quick validation schema for identifying true physical remission cases.
Uses minimal fields for fast LLM classification.
"""

from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class RemissionType(str, Enum):
    """Type of remission described in the narrative."""
    CANCER = "cancer"
    CHRONIC_DISEASE = "chronic_disease"
    ACUTE_CONDITION = "acute_condition"
    INJURY = "injury"
    NONE = "none"


class ValidationResult(str, Enum):
    """Final classification of the case."""
    CONFIRMED_REMISSION = "confirmed_remission"  # Clear physical healing/remission described
    PROBABLE_REMISSION = "probable_remission"    # Likely remission but details unclear
    SPIRITUAL_ONLY = "spiritual_only"            # Only spiritual/emotional healing mentioned
    THIRD_PARTY = "third_party"                  # Describes someone else's healing, not experiencer
    NO_HEALING = "no_healing"                    # No healing content found
    INSUFFICIENT_DATA = "insufficient_data"      # Cannot determine from narrative


class QuickValidation(BaseModel):
    """
    Rapid validation questionnaire to classify NDE cases for physical remission content.
    
    Focus: Does this narrative describe the experiencer undergoing physical healing/remission
    of a medical condition as a result of or connected to their NDE/spiritual experience?
    """
    
    # Q1: Is there ANY mention of physical healing in this narrative?
    mentions_physical_healing: bool = Field(
        description="Does the narrative mention any form of physical healing, cure, or remission of a medical condition?"
    )
    
    # Q2: Who experienced the healing?
    healing_subject_is_experiencer: bool = Field(
        description="Is the person who experienced the healing the same person who had the NDE/spiritual experience (not a third party, family member, or someone they healed)?"
    )
    
    # Q3: What type of condition was healed?
    remission_type: RemissionType = Field(
        description="What type of medical condition was healed/cured? Use 'none' if no physical healing occurred."
    )
    
    # Q4: Brief description of the condition
    condition_description: Optional[str] = Field(
        default=None,
        description="Brief description of the medical condition that was healed (e.g., 'stage 4 lung cancer', 'paralysis from spinal injury', 'chronic asthma'). Leave empty if no physical healing."
    )
    
    # Q5: Was the healing medically verified or documented?
    medically_verified: bool = Field(
        description="Does the narrative indicate the healing was confirmed by doctors, medical tests, or hospital records?"
    )
    
    # Q6: Connection to NDE/spiritual experience
    healing_connected_to_experience: bool = Field(
        description="Is the physical healing described as occurring during, immediately after, or as a direct result of the NDE/spiritual experience?"
    )
    
    # Final classification
    validation_result: ValidationResult = Field(
        description="Final classification: confirmed_remission (clear physical healing of experiencer), probable_remission (likely but unclear), spiritual_only (emotional/psychological healing only), third_party (someone else's healing), no_healing (no healing content), insufficient_data (cannot determine)"
    )
    
    # Confidence score
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="Confidence in this classification (0.0-1.0)"
    )
    
    # Brief rationale
    rationale: str = Field(
        description="One sentence explaining the classification decision."
    )


# For structured output with OpenAI
VALIDATION_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "quick_validation",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "mentions_physical_healing": {
                    "type": "boolean",
                    "description": "Does the narrative mention any form of physical healing, cure, or remission of a medical condition?"
                },
                "healing_subject_is_experiencer": {
                    "type": "boolean",
                    "description": "Is the person who experienced the healing the same person who had the NDE?"
                },
                "remission_type": {
                    "type": "string",
                    "enum": ["cancer", "chronic_disease", "acute_condition", "injury", "none"],
                    "description": "Type of medical condition healed"
                },
                "condition_description": {
                    "type": ["string", "null"],
                    "description": "Brief description of medical condition healed"
                },
                "medically_verified": {
                    "type": "boolean",
                    "description": "Was healing confirmed by doctors or medical tests?"
                },
                "healing_connected_to_experience": {
                    "type": "boolean",
                    "description": "Is healing connected to the NDE/spiritual experience?"
                },
                "validation_result": {
                    "type": "string",
                    "enum": ["confirmed_remission", "probable_remission", "spiritual_only", "third_party", "no_healing", "insufficient_data"],
                    "description": "Final classification"
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence score 0.0-1.0"
                },
                "rationale": {
                    "type": "string",
                    "description": "One sentence explanation"
                }
            },
            "required": [
                "mentions_physical_healing",
                "healing_subject_is_experiencer",
                "remission_type",
                "condition_description",
                "medically_verified",
                "healing_connected_to_experience",
                "validation_result",
                "confidence",
                "rationale"
            ],
            "additionalProperties": False
        }
    }
}
