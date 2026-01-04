"""Unit tests for NDE extraction module."""

import unittest
import sys
from pathlib import Path

# Add paths for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT.parent.parent))

from shared.analysis import build_user_prompt


class ExtractTests(unittest.TestCase):
    """Tests for NDE extraction functionality."""

    def test_prompt_includes_metadata(self) -> None:
        """Prompt should include all metadata fields."""
        prompt = build_user_prompt(
            title="Test Title",
            date="Jan 1, 2020",
            dataset="nderf",
            source_url="https://example.test/entry",
            content="Line one.\nLine two.",
            suffix="\nProvide the most accurate structured questionnaire responses possible.",
        )
        self.assertIn("Dataset: nderf", prompt)
        self.assertIn("Title: Test Title", prompt)
        self.assertIn("Reported date: Jan 1, 2020", prompt)
        self.assertIn("Source URL: https://example.test/entry", prompt)
        self.assertIn("Line one.\nLine two.", prompt)
        self.assertTrue(
            prompt.strip().endswith(
                "Provide the most accurate structured questionnaire responses possible."
            )
        )

    def test_prompt_without_optional_fields(self) -> None:
        """Prompt should work without optional fields."""
        prompt = build_user_prompt(
            title="",
            date=None,
            dataset="iands",
            source_url=None,
            content="NDE narrative content.",
        )
        self.assertIn("Dataset: iands", prompt)
        self.assertIn("Title: Untitled", prompt)
        self.assertNotIn("Reported date:", prompt)
        self.assertNotIn("Source URL:", prompt)


if __name__ == "__main__":
    unittest.main()
