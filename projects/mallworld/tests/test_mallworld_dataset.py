"""Checks for the verified MallWorld loader."""

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import mallworld_dataset as mw  # noqa: E402


def test_populations():
    posts = mw.load_posts()
    assert len(posts) == 3732
    assert posts["has_extractable_dream"].sum() == 2678
    primary = posts[posts["primary"]]
    assert primary["post_type"].isin(mw.DREAM_POST_TYPES).all()
    assert (primary["n_locations"] > 0).all()
    assert not primary["is_duplicate"].any()
    assert primary["post_id"].is_unique


def test_observed_values_are_in_schema():
    tables = [
        mw.load_posts(),
        mw.load_locations("all"),
        mw.load_connections("all"),
        mw.load_interactions("all"),
        mw.load_entities("all"),
        mw.load_boundaries("all"),
    ]
    for column in mw.COLUMN_ENUMS:
        for table in tables:
            if column not in table:
                continue
            if column in mw.LIST_COLUMNS:
                values = set(itertools.chain.from_iterable(table[column]))
            else:
                values = set(table[column].dropna())
            assert values <= set(mw.allowed_values(column)), column


def test_isin_rejects_impossible_values():
    locations = mw.load_locations()
    with pytest.raises(ValueError):
        mw.isin(locations, "atmosphere", ["scary"])
    with pytest.raises(ValueError):
        mw.isin(locations, "vertical", ["underground"])  # not a schema value
    assert mw.isin(locations, "vertical", ["lowest", "lower"]).sum() > 0


def test_codings_cover_schema():
    assert set(mw.ATMOSPHERE_VALENCE) | {"nostalgic", "not_mentioned"} == set(
        mw.allowed_values("atmosphere")
    )
    assert set(mw.VERTICAL_LEVEL) | {"varies", "not_mentioned"} == set(
        mw.allowed_values("vertical")
    )
    assert set(mw.INTRINSICALLY_VERTICAL_TYPES) <= set(mw.allowed_values("location_type"))


def test_long_tables_carry_cluster_keys():
    for loader in (mw.load_locations, mw.load_connections, mw.load_interactions, mw.load_entities):
        df = loader()
        assert df["post_id"].notna().all() and df["author"].notna().all()
        assert set(df["post_id"]) <= set(mw.load_posts().query("primary")["post_id"])


def test_cluster_bootstrap_runs():
    df = pd.DataFrame({"post_id": np.repeat(np.arange(50), 3), "y": np.tile([0, 1, 1], 50)})
    point, (lo, hi), draws = mw.cluster_bootstrap(df, lambda d: d["y"].mean(), n_boot=200)
    assert lo <= point <= hi and len(draws) == 200
