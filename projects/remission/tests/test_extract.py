"""Unit tests for remission extraction module."""

import unittest
import sys
from pathlib import Path

# Add paths for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import build_user_prompt


class ExtractTests(unittest.TestCase):
    """Tests for remission extraction functionality."""

    def test_prompt_includes_metadata(self) -> None:
        """Prompt should include all metadata fields."""
        prompt = build_user_prompt(
            title="Test Case",
            date="Jan 1, 2024",
            dataset="radicalremission",
            source_url="https://example.test/case/123",
            content="Patient was diagnosed with stage IV cancer...",
            suffix=(
                "\nAnalyze this remission case according to the structured questionnaire. "
                "Extract medical details, identify which of Turner's 9 factors are present, "
                "note any anomalous experiences (NDE/STE), and assess the validation tier."
            ),
        )
        self.assertIn("Dataset: radicalremission", prompt)
        self.assertIn("Title: Test Case", prompt)
        self.assertIn("Reported date: Jan 1, 2024", prompt)
        self.assertIn("Source URL: https://example.test/case/123", prompt)
        self.assertIn("Patient was diagnosed with stage IV cancer...", prompt)
        self.assertIn("Turner's 9 factors", prompt)

    def test_prompt_without_optional_fields(self) -> None:
        """Prompt should work without optional fields."""
        prompt = build_user_prompt(
            title="",
            date=None,
            dataset="pubmed",
            source_url=None,
            content="Case narrative content.",
        )
        self.assertIn("Dataset: pubmed", prompt)
        self.assertIn("Title: Untitled", prompt)
        self.assertNotIn("Reported date:", prompt)
        self.assertNotIn("Source URL:", prompt)


if __name__ == "__main__":
    unittest.main()
