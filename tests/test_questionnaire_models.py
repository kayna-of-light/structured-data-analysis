"""Unit tests for questionnaire models."""

import unittest

from pydantic import ValidationError

from models import RemissionAnalysisResponse


def _sample_payload() -> dict:
    """Return a minimal valid payload for testing."""
    return {
        "diagnosis": {
            "diagnosis_raw": "Stage IV breast cancer",
            "cancer_type": "breast cancer",
            "stage": "stage_iv",
            "metastasis_sites": ["liver", "bone"],
            "prognosis_given": "6 months",
            "biopsy_confirmed": "yes_explicit",
            "imaging_confirmed": "yes_explicit",
        },
        "treatment": {
            "conventional_status": "failed",
            "treatments_received": ["chemotherapy", "radiation"],
            "alternative_treatments": ["acupuncture", "meditation"],
            "supplement_list": ["vitamin C", "curcumin"],
        },
        "remission_outcome": {
            "remission_type": "complete_remission",
            "remission_speed": "rapid",
            "time_to_remission": "6 weeks",
            "verification_method": ["pet_scan", "blood_markers"],
            "current_status": "alive_ned",
            "survival_duration": "5 years",
        },
        "turner_factors": {
            "factor_diet_change": "yes_explicit",
            "dietary_protocol": "ketogenic",
            "factor_agency": "yes_explicit",
            "factor_intuition": "implied",
            "factor_supplements": "yes_explicit",
            "factor_emotional_release": "yes_explicit",
            "emotional_release_details": "Forgave estranged family member",
            "factor_positive_emotions": "yes_explicit",
            "positive_emotion_types": ["joy", "gratitude"],
            "factor_social_support": "yes_explicit",
            "social_support_level": "strong",
            "factor_spiritual_connection": "yes_explicit",
            "spiritual_practices": ["meditation", "prayer"],
            "factor_purpose": "yes_explicit",
            "purpose_details": "Wanted to see grandchildren grow up",
        },
        "anomalous_experience": {
            "has_experience": "yes_explicit",
            "experience_type": "nde",
            "greyson_score_estimate": 18,
            "veridical_perception": "implied",
            "experience_details": "Felt overwhelming love and was told to return",
        },
        "existential_shift": {
            "identity_shift": "yes_explicit",
            "authenticity_shift": "yes_explicit",
            "fear_to_love_shift": "yes_explicit",
            "surrender_event": "yes_explicit",
            "transformation_narrative": "Completely changed perspective on life",
        },
        "correspondential_markers": {
            "proprium_indicators": "implied",
            "self_attack_indicators": "no",
            "closed_will_indicators": "no",
            "resolution_type": "forgiveness",
            "transformation_preceded_healing": "yes_explicit",
        },
        "validation": {
            "verification_tier": "tier_2_clinical",
            "remission_category": "radical_post_failure",
            "medical_detail_density": "high",
            "lambertini_criteria_met": ["serious_disease", "suddenness"],
        },
        "case_summary": "Terminal breast cancer patient healed after profound spiritual transformation",
        "key_healing_factors": ["emotional_release", "spiritual_connection", "nde"],
    }


class QuestionnaireModelTests(unittest.TestCase):
    """Tests for RemissionAnalysisResponse model."""

    def test_valid_payload_parses(self) -> None:
        """Valid payload should parse without errors."""
        payload = _sample_payload()
        response = RemissionAnalysisResponse.model_validate(payload)
        self.assertEqual(response.diagnosis.cancer_type, "breast cancer")
        self.assertEqual(response.remission_outcome.remission_type.value, "complete_remission")
        self.assertEqual(response.turner_factors.factor_diet_change.value, "yes_explicit")

    def test_minimal_payload_parses(self) -> None:
        """Minimal payload with required fields should parse."""
        payload = {
            "diagnosis": {},
            "treatment": {},
            "remission_outcome": {},
            "turner_factors": {},
            "anomalous_experience": {},
            "existential_shift": {},
            "correspondential_markers": {},
            "validation": {},
        }
        response = RemissionAnalysisResponse.model_validate(payload)
        self.assertIsNotNone(response)

    def test_invalid_enum_rejected(self) -> None:
        """Invalid enum value should raise ValidationError."""
        payload = _sample_payload()
        payload["diagnosis"]["stage"] = "invalid_stage"
        with self.assertRaises(ValidationError):
            RemissionAnalysisResponse.model_validate(payload)

    def test_greyson_score_range(self) -> None:
        """Greyson score must be 0-32."""
        payload = _sample_payload()
        payload["anomalous_experience"]["greyson_score_estimate"] = 50
        with self.assertRaises(ValidationError):
            RemissionAnalysisResponse.model_validate(payload)

    def test_extra_fields_rejected(self) -> None:
        """Extra fields should be rejected (extra='forbid')."""
        payload = _sample_payload()
        payload["diagnosis"]["unexpected_field"] = "value"
        with self.assertRaises(ValidationError):
            RemissionAnalysisResponse.model_validate(payload)


if __name__ == "__main__":
    unittest.main()
