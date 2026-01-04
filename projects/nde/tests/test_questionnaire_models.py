import unittest

from pydantic import ValidationError

from models import NDEAnalysisResponse


def _sample_payload() -> dict:
    return {
        "passage": {
            "out_of_body": {
                "separation": "yes_explicit",
                "vantage_points": ["above_body"],
                "observation_accuracy": "unverified",
                "heightened_perception": "yes_explicit",
                "identity_continuity": "clear_identity",
                "separation_sensations": ["peace"],
            },
            "tunnel": {
                "passage_type": "tunnel",
                "movement_sensations": ["rapid"],
                "light_visibility": "bright",
                "emotional_tone": "peaceful",
            },
            "arrival": {
                "environment_description": "detailed",
                "light_encounter": ["brilliant_light"],
                "being_identifications": ["angels"],
                "greeting_types": ["spiritual_beings"],
                "sense_of_belonging": "explicit",
            },
        },
        "world_of_spirits": {
            "environment": {
                "environment_description": "detailed",
                "environment_features": ["landscape", "light"],
                "comparative_reality": "more_real_explicit",
                "thought_responsiveness": "yes_explicit",
            },
            "encounters": {
                "deceased_relatives": "named",
                "spiritual_beings": ["guides_or_angels"],
                "communication_mode": "telepathic",
                "guidance_level": "significant_guidance",
                "other_souls_presence": "many",
            },
            "self_perception": {
                "self_form": "current_self",
                "physical_limitations": "none",
            },
        },
        "life_review": {
            "occurrence": "extensive",
            "presentation": "panoramic",
            "perspective_of_others": "yes_explicit",
            "judgment": "guide_or_light",
            "emotional_tone": "love",
        },
        "boundary_and_return": {
            "boundary_encounter": "physical_barrier",
            "return_choice": "chose_to_return",
            "return_reason": "earthly_mission",
            "return_description": "detailed",
            "return_method": "rapid",
            "return_feeling": "unpleasant",
        },
        "transformative_effects": {
            "readjustment": "significant",
            "post_ability_changes": ["psychic"],
            "belief_change": "no_fear",
            "value_shift": "major",
            "spirituality_shift": "more_spiritual",
        },
        "context": {
            "nde_cause": "cardiac_arrest",
            "clinical_status": "verified",
            "experience_duration": "seconds_to_minutes",
            "age_reported": True,
            "age_years": 35,
            "cultural_background_reported": True,
            "cultural_or_religious_background": "Christian",
            "prior_nde_knowledge": "aware",
        },
        "stage_sequence": {
            "present_elements": ["obe", "tunnel"],
            "canonical_sequence": "mostly",
            "repeated_stages": "no",
            "simultaneous_stages": "no",
        },
        "unique_elements": {
            "nonstandard_elements": None,
            "notable_quotes": None,
        },
    }


class QuestionnaireModelTests(unittest.TestCase):
    def test_model_instantiation_succeeds(self) -> None:
        payload = _sample_payload()
        response = NDEAnalysisResponse.model_validate(payload)
        self.assertEqual(response.context.age_years, 35)
        self.assertEqual(
            response.passage.out_of_body.separation.value,
            "yes_explicit",
        )

    def test_age_required_when_flagged(self) -> None:
        payload = _sample_payload()
        payload["context"]["age_years"] = None
        with self.assertRaises(ValidationError):
            NDEAnalysisResponse.model_validate(payload)


if __name__ == "__main__":
    unittest.main()