"""Tests for the verified NDE loader used by the analysis notebooks."""

import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import nde_dataset as nd  # noqa: E402


class SchemaGuardTests(unittest.TestCase):
    def test_columns_are_unambiguous(self):
        self.assertEqual(nd.COLUMN_PATHS["light_encounter"], "passage.arrival.light_encounter")
        self.assertEqual(nd.COLUMN_PATHS["sense_of_belonging"], "passage.arrival.sense_of_belonging")
        self.assertEqual(nd.COLUMN_PATHS["life_review_emotional_tone"], "life_review.emotional_tone")
        self.assertEqual(nd.COLUMN_PATHS["tunnel_emotional_tone"], "passage.tunnel.emotional_tone")

    def test_invalid_enum_values_raise(self):
        # Values used by earlier notebook versions that do not exist in the schema
        for column, bad in [("death_fear_before", ["extreme"]), ("mission_commissioned", ["yes"]),
                            ("judgment_source", ["self_judgment"]), ("occurrence", ["yes"])]:
            with self.assertRaises(ValueError):
                nd.check_values(column, bad)

    def test_ordinal_scales_cover_schema(self):
        self.assertEqual(set(nd.FEAR_SCALE) | {"not_mentioned"}, set(nd.allowed_values("death_fear_before")))
        self.assertEqual(set(nd.SPIRITUALITY_SCALE) | {"not_mentioned"}, set(nd.allowed_values("spirituality_after")))
        self.assertEqual(set(nd.RELIGIOSITY_SCALE) | {"not_mentioned"}, set(nd.allowed_values("religiosity_before")))

    def test_isin_handles_list_columns(self):
        frame = pd.DataFrame({"return_reasons": [["earthly_mission"], [], ["other", "not_your_time"]]})
        self.assertEqual(nd.has(frame, "return_reasons", "earthly_mission").tolist(), [True, False, False])

    def test_wilson_interval(self):
        lo, hi = nd.wilson_ci(50, 100)
        self.assertAlmostEqual(lo, 0.4038, places=3)
        self.assertAlmostEqual(hi, 0.5962, places=3)


@unittest.skipUnless(any(nd.STRUCTURED_DIR.glob("*.json")), "structured data not available")
class LoaderTests(unittest.TestCase):
    def test_load_frame_deduplicates(self):
        df = nd.load_frame(word_counts=False)
        self.assertEqual(len(df), len({c for c in df["file"]}))
        self.assertLess(len(df), len(list(nd.STRUCTURED_DIR.glob("*.json"))) + 1)
        self.assertTrue(df["dataset"].isin(["nderf", "iands"]).all())


if __name__ == "__main__":
    unittest.main()
