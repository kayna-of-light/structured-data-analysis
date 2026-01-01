"""Unit tests for analyze_cases module."""

import unittest

from analyze_cases import build_user_prompt


class AnalyzeCasesTests(unittest.TestCase):
    """Tests for analyze_cases functionality."""

    def test_prompt_includes_metadata(self) -> None:
        """Prompt should include all metadata fields."""
        prompt = build_user_prompt(
            title="Test Case",
            date="Jan 1, 2024",
            dataset="radicalremission",
            source_url="https://example.test/case/123",
            content="Patient was diagnosed with stage IV cancer...",
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
        self.assertIn("Untitled Case", prompt)
        self.assertNotIn("Reported date:", prompt)
        self.assertNotIn("Source URL:", prompt)


if __name__ == "__main__":
    unittest.main()
