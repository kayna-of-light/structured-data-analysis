"""Verified loader for the MallWorld structured extractions (schema ``MallworldResponse``).

Every MallWorld analysis notebook should load data through this module. It exists because
the 2026-10 audit (``projects/mallworld/docs/STATISTICAL_AUDIT_2026-10.md``) found that the
earlier notebooks:

* used different analysis populations without saying so (2,678 "dreams" included questions,
  AI-generated visualisations and map-only posts; other notebooks used 1,926 dream reports);
* filtered on keys that do not exist (``ext.get('post_type')``, ``ext.get('is_not_dream_report')``),
  so the filter silently did nothing;
* treated locations, entities and interactions nested in the same dream as independent;
* never attached narrative length, the main confound for "more of X with Y" comparisons.

The module therefore provides:

* one row per post (:func:`load_posts`) with the post type, author, date, text length, image
  count and the analysis population it belongs to;
* long tables for locations, connections, interactions, entities and boundaries, each keyed by
  ``post_id`` (the dream) and ``author`` so analyses can cluster on them;
* the allowed enum values of every categorical column, taken from the Pydantic schema itself,
  and :func:`isin`, which raises if asked to match a value the schema cannot produce.

Populations
-----------
``"primary"``      dream reports (``dream_report`` or ``dream_report_with_map``) with at least one
                   extracted location, excluding exact duplicate submissions (the later copy of
                   identical text). This is the analysis population for all audited work.
``"extractable"``  every post the extractor flagged ``has_extractable_dream`` (the population of
                   the old notebook 09 and its thesis); kept only to reproduce old figures.
``"all"``          every structured post.
"""

from __future__ import annotations

import ast
import hashlib
import json
import sys
from collections.abc import Iterable
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

MW_ROOT = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = MW_ROOT / "structured"
RAW_DIR = MW_ROOT.parent.parent / "data" / "mallworld"

if str(MW_ROOT) not in sys.path:
    sys.path.insert(0, str(MW_ROOT))

from models import questionnaire as q  # noqa: E402

DREAM_POST_TYPES = ("dream_report", "dream_report_with_map")

# ---------------------------------------------------------------------------
# Column -> schema enum. Column names are unique across all tables.
# ---------------------------------------------------------------------------
COLUMN_ENUMS: dict[str, type[Enum]] = {
    # posts
    "post_type": q.PostType,
    "content_flags": q.PostContentFlag,
    "detail_level": q.DetailLevel,
    "map_coherence": q.MapCoherence,
    "recurrence": q.RecurrencePattern,
    "time_flow": q.TimeFlow,
    "dreamer_identity": q.DreamerIdentity,
    "author_gender": q.Gender,
    "author_age_range": q.AgeRange,
    # locations
    "location_type": q.LocationType,
    "vertical": q.VerticalPosition,
    "horizontal": q.HorizontalPosition,
    "cardinal": q.CardinalDirection,
    "light": q.LightQuality,
    "light_temperature": q.LightTemperature,
    "time_of_day": q.TimeOfDay,
    "state": q.StateOfPlace,
    "atmosphere": q.Atmosphere,
    "reality_stability": q.RealityStability,
    "crowding": q.Crowding,
    "crowd_behavior": q.CrowdBehavior,
    "intellectual_focus": q.IntellectualFocus,
    "cleanliness": q.Cleanliness,
    "privacy_status": q.PrivacyStatus,
    "water_presence": q.WaterPresence,
    "affective_response": q.AffectiveResponse,
    "somatic_response": q.SomaticResponse,
    "is_familiar": q.MentionResponse,
    "is_accessible": q.MentionResponse,
    "dreamer_role": q.DreamerRole,
    # connections
    "connection_type": q.ConnectionType,
    "transit_mode": q.TransitMode,
    "direction": q.MovementDirection,
    "difficulty": q.TraversalDifficulty,
    "mechanism_function": q.MechanismFunction,
    "traversal_outcome": q.TraversalOutcome,
    # interactions
    "interaction_type": q.InteractionType,
    "interaction_outcome": q.InteractionOutcome,
    "failure_type": q.FailureType,
    # entities
    "entity_type": q.EntityType,
    "demeanor": q.EntityDemeanor,
    "entity_role": q.EntityRole,
    "authority_nature": q.AuthorityNature,
    "is_known": q.MentionResponse,
    "is_recurring": q.MentionResponse,
    # boundaries
    "boundary_type": q.BoundaryType,
    "boundary_direction": q.CardinalDirection,
    "beyond": q.BeyondBoundary,
    "can_see_beyond": q.MentionResponse,
    "crossing_attempted": q.MentionResponse,
    "crossing_outcome": q.TraversalOutcome,
}
LIST_COLUMNS = {"content_flags"}

# ---------------------------------------------------------------------------
# Analyst-defined codings (documented so every notebook uses the same ones)
# ---------------------------------------------------------------------------
#: Vertical position as a signed level (ground = 0). ``varies``/``not_mentioned`` -> NaN.
VERTICAL_LEVEL = {"lowest": -2, "lower": -1, "ground": 0, "upper": 1, "uppermost": 2}
#: Three-way valence of the location atmosphere. ``nostalgic`` is ambiguous and kept apart.
ATMOSPHERE_VALENCE = {
    "welcoming": 1,
    "peaceful": 1,
    "neutral": 0,
    "threatening": -1,
    "oppressive": -1,
    "uncomfortable": -1,
    "wrong": -1,
    "eerie": -1,
    "chaotic": -1,
}
#: The 5-point ordinal used by the archived notebooks (kept only to reproduce old figures).
ATMOSPHERE_OLD_5PT = {
    "threatening": 1,
    "oppressive": 2,
    "uncomfortable": 2,
    "wrong": 2,
    "eerie": 2,
    "chaotic": 2,
    "neutral": 3,
    "nostalgic": 4,
    "peaceful": 4,
    "welcoming": 5,
}
#: Location types whose name itself implies a vertical position. The extraction prompt told the
#: model to infer vertical position and movement direction from these types ("Implied
#: verticality"), so vertical effects must be checked with these types excluded.
INTRINSICALLY_VERTICAL_TYPES = (
    "basement",
    "underground",
    "cave",
    "subway",
    "parking_structure",
    "attic",
    "roof",
    "mountain",
)


# ---------------------------------------------------------------------------
# Schema checks
# ---------------------------------------------------------------------------
def allowed_values(column: str) -> tuple[str, ...]:
    """Enum values the schema allows for ``column``."""
    if column not in COLUMN_ENUMS:
        raise KeyError(f"{column} is not a schema enum column")
    return tuple(m.value for m in COLUMN_ENUMS[column])


def check_values(column: str, values: Iterable[str]) -> tuple[str, ...]:
    """Raise ``ValueError`` if any of ``values`` cannot occur in ``column``."""
    values = tuple(values)
    allowed = allowed_values(column)
    bad = [v for v in values if v not in allowed]
    if bad:
        raise ValueError(f"{column}: values {bad} are not in the schema; allowed = {allowed}")
    return values


def isin(df: pd.DataFrame, column: str, values: Iterable[str]) -> pd.Series:
    """Schema-checked ``isin`` for scalar and list columns."""
    values = check_values(column, values)
    if column in LIST_COLUMNS:
        vs = set(values)
        return df[column].apply(lambda xs: bool(vs.intersection(xs)))
    return df[column].isin(values)


def has(df: pd.DataFrame, column: str, value: str) -> pd.Series:
    """Schema-checked test for a single value."""
    return isin(df, column, [value])


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------
def _parse_metadata(meta: Any) -> dict[str, Any]:
    if isinstance(meta, dict):
        return meta
    if isinstance(meta, str) and meta.strip():
        try:
            return ast.literal_eval(meta)
        except (ValueError, SyntaxError):
            return {}
    return {}


@lru_cache(maxsize=1)
def _raw_index() -> dict[str, dict[str, Any]]:
    index = {}
    for path in RAW_DIR.glob("*.json"):
        raw = json.loads(path.read_text(encoding="utf-8"))
        raw["metadata"] = _parse_metadata(raw.get("metadata"))
        index[str(raw["source_id"])] = raw
    return index


@lru_cache(maxsize=1)
def load_records() -> tuple[dict[str, Any], ...]:
    """All structured records, sorted by post id, each with ``_post_id`` and ``_raw`` attached."""
    raw_index = _raw_index()
    records = []
    for path in sorted(STRUCTURED_DIR.glob("mallworld-*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        post_id = path.stem[len("mallworld-") :]
        record["_post_id"] = post_id
        record["_raw"] = raw_index.get(post_id, {})
        records.append(record)
    return tuple(records)


def _images(raw: dict[str, Any]) -> list[str]:
    urls = raw.get("metadata", {}).get("image_urls") or []
    return list(urls) if isinstance(urls, (list, tuple)) else []


def _author(raw: dict[str, Any], post_id: str) -> str:
    author = raw.get("metadata", {}).get("author")
    if not author or author in ("[deleted]", "None"):
        return f"unknown:{post_id}"  # each unknown author treated as a distinct person
    return str(author)


@lru_cache(maxsize=1)
def load_posts() -> pd.DataFrame:
    """One row per structured post with population flags and covariates."""
    rows = []
    for record in load_records():
        ext = record["extraction"]
        raw = record["_raw"]
        cls, meta = ext["classification"], ext["meta"]
        text = (raw.get("content") or "").strip()
        words = len(text.split())
        title_words = len((raw.get("title") or "").split())
        n_entities = sum(len(i.get("entities_involved", [])) for i in ext["interactions"])
        rows.append(
            {
                "post_id": record["_post_id"],
                "author": _author(raw, record["_post_id"]),
                "date": pd.to_datetime(raw.get("date_published"), utc=True, errors="coerce"),
                "title": raw.get("title"),
                "words": words,
                "title_words": title_words,
                "has_text": words > 0,
                "n_images": len(_images(raw)),
                "post_type": cls["post_type"],
                "content_flags": list(cls.get("content_flags") or []),
                "detail_level": cls.get("detail_level"),
                "has_extractable_dream": bool(cls.get("has_extractable_dream")),
                "map_coherence": meta.get("map_coherence"),
                "recurrence": meta.get("recurrence"),
                "time_flow": meta.get("time_flow"),
                "dreamer_identity": meta.get("dreamer_identity"),
                "author_gender": (meta.get("author") or {}).get("gender"),
                "author_age_range": (meta.get("author") or {}).get("age_range"),
                "n_locations": len(ext["locations"]),
                "n_connections": len(ext["connections"]),
                "n_interactions": len(ext["interactions"]),
                "n_entities": n_entities,
                "n_boundaries": len(ext["boundaries"]),
                "text_checksum": (
                    hashlib.sha1(" ".join(text.lower().split()).encode()).hexdigest()
                    if words
                    else None
                ),
            }
        )
    df = pd.DataFrame(rows).sort_values(["date", "post_id"]).reset_index(drop=True)
    df["log_words"] = np.log1p(df["words"])
    # Accidental double submissions (identical text, seconds apart): keep the earliest copy.
    df["is_duplicate"] = df["text_checksum"].notna() & df["text_checksum"].duplicated(keep="first")
    df["is_dream_report"] = df["post_type"].isin(DREAM_POST_TYPES)
    df["primary"] = df["is_dream_report"] & (df["n_locations"] > 0) & ~df["is_duplicate"]
    df["year"] = df["date"].dt.year
    return df


def _population_ids(population: str) -> set[str]:
    posts = load_posts()
    if population == "primary":
        return set(posts.loc[posts["primary"], "post_id"])
    if population == "extractable":
        return set(posts.loc[posts["has_extractable_dream"], "post_id"])
    if population == "all":
        return set(posts["post_id"])
    raise ValueError(f"unknown population {population!r}")


def _post_covariates() -> pd.DataFrame:
    return load_posts()[["post_id", "author", "words", "log_words", "n_locations", "year"]]


def _finish(rows: list[dict[str, Any]], population: str) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df = df[df["post_id"].isin(_population_ids(population))]
    return df.merge(_post_covariates(), on="post_id", how="left").reset_index(drop=True)


def load_locations(population: str = "primary") -> pd.DataFrame:
    """One row per extracted location, with derived ``vertical_level`` and ``valence``."""
    rows = []
    for record in load_records():
        for k, loc in enumerate(record["extraction"]["locations"]):
            pos, qual = loc.get("position") or {}, loc.get("qualities") or {}
            rows.append(
                {
                    "post_id": record["_post_id"],
                    "location_id": loc["location_id"],
                    "list_index": k,
                    "visit_order": loc.get("visit_order"),
                    "location_type": loc["location_type"],
                    "location_name": loc.get("location_name"),
                    "vertical": pos.get("vertical", "not_mentioned"),
                    "horizontal": pos.get("horizontal", "not_mentioned"),
                    "cardinal": pos.get("cardinal", "not_mentioned"),
                    "relative_to": pos.get("relative_to"),
                    "light": qual.get("light", "not_mentioned"),
                    "light_temperature": qual.get("light_temperature", "not_mentioned"),
                    "time_of_day": qual.get("time_of_day", "not_mentioned"),
                    "state": qual.get("state", "not_mentioned"),
                    "atmosphere": qual.get("atmosphere", "not_mentioned"),
                    "reality_stability": qual.get("reality_stability", "not_mentioned"),
                    "crowding": qual.get("crowding", "not_mentioned"),
                    "crowd_behavior": qual.get("crowd_behavior", "not_mentioned"),
                    "intellectual_focus": qual.get("intellectual_focus", "not_mentioned"),
                    "cleanliness": qual.get("cleanliness", "not_mentioned"),
                    "privacy_status": qual.get("privacy_status", "not_mentioned"),
                    "water_presence": qual.get("water_presence", "not_mentioned"),
                    "water_clarity": qual.get("water_clarity"),
                    "raw_description": qual.get("raw_description"),
                    "affective_response": loc.get("affective_response", "not_mentioned"),
                    "somatic_response": loc.get("somatic_response", "none"),
                    "is_familiar": loc.get("is_familiar", "not_mentioned"),
                    "is_accessible": loc.get("is_accessible", "not_mentioned"),
                    "dreamer_role": loc.get("dreamer_role", "not_mentioned"),
                }
            )
    df = _finish(rows, population)
    df["vertical_level"] = df["vertical"].map(VERTICAL_LEVEL)
    df["valence"] = df["atmosphere"].map(ATMOSPHERE_VALENCE)
    df["intrinsically_vertical"] = df["location_type"].isin(INTRINSICALLY_VERTICAL_TYPES)
    return df


def load_connections(population: str = "primary") -> pd.DataFrame:
    rows = []
    for record in load_records():
        for k, c in enumerate(record["extraction"]["connections"]):
            rows.append(
                {
                    "post_id": record["_post_id"],
                    "list_index": k,
                    "from_location_id": c["from_location_id"],
                    "to_location_id": c["to_location_id"],
                    "connection_type": c["connection_type"],
                    "transit_mode": c.get("transit_mode", "not_mentioned"),
                    "direction": c.get("direction", "unknown"),
                    "difficulty": c.get("difficulty", "not_mentioned"),
                    "mechanism_function": c.get("mechanism_function", "not_applicable"),
                    "traversal_outcome": c.get("outcome", "not_mentioned"),
                    "connection_qualities": c.get("qualities"),
                }
            )
    return _finish(rows, population)


def load_interactions(population: str = "primary") -> pd.DataFrame:
    rows = []
    for record in load_records():
        for k, i in enumerate(record["extraction"]["interactions"]):
            rows.append(
                {
                    "post_id": record["_post_id"],
                    "interaction_index": k,
                    "location_id": i["location_id"],
                    "interaction_type": i["interaction_type"],
                    "interaction_description": i.get("description"),
                    "interaction_outcome": i.get("outcome", "not_mentioned"),
                    "failure_type": i.get("failure_type", "not_applicable"),
                    "n_entities_involved": len(i.get("entities_involved", [])),
                }
            )
    return _finish(rows, population)


def load_entities(population: str = "primary") -> pd.DataFrame:
    """One row per entity *involvement* (entities are recorded inside interactions)."""
    rows = []
    for record in load_records():
        for k, i in enumerate(record["extraction"]["interactions"]):
            for ent in i.get("entities_involved", []):
                rows.append(
                    {
                        "post_id": record["_post_id"],
                        "interaction_index": k,
                        "location_id": i["location_id"],
                        "interaction_type": i["interaction_type"],
                        "interaction_outcome": i.get("outcome", "not_mentioned"),
                        "entity_type": ent["entity_type"],
                        "demeanor": ent.get("demeanor", "not_mentioned"),
                        "entity_role": ent.get("role", "not_mentioned"),
                        "authority_nature": ent.get("authority_nature", "not_mentioned"),
                        "is_known": ent.get("is_known", "not_mentioned"),
                        "is_recurring": ent.get("is_recurring", "not_mentioned"),
                        "entity_description": ent.get("description"),
                        "name_or_relation": ent.get("name_or_relation"),
                    }
                )
    return _finish(rows, population)


def load_boundaries(population: str = "primary") -> pd.DataFrame:
    rows = []
    for record in load_records():
        for b in record["extraction"]["boundaries"]:
            rows.append(
                {
                    "post_id": record["_post_id"],
                    "location_id": b.get("location_id"),
                    "boundary_type": b["boundary_type"],
                    "boundary_direction": b.get("direction", "not_mentioned"),
                    "beyond": b.get("beyond", "not_mentioned"),
                    "can_see_beyond": b.get("can_see_beyond", "not_mentioned"),
                    "crossing_attempted": b.get("crossing_attempted", "not_mentioned"),
                    "crossing_outcome": b.get("crossing_outcome", "not_mentioned"),
                    "boundary_description": b.get("description"),
                }
            )
    return _finish(rows, population)


def raw_text(post_id: str) -> str:
    """Title + body text of a post, as the extractor received it (images not included)."""
    raw = _raw_index().get(post_id, {})
    return f"{raw.get('title') or ''}\n\n{raw.get('content') or ''}".strip()


# ---------------------------------------------------------------------------
# Statistics helpers (dream-clustered inference)
# ---------------------------------------------------------------------------
def wilson_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    from scipy.stats import norm

    if n == 0:
        return (float("nan"), float("nan"))
    z = norm.ppf(1 - alpha / 2)
    p = k / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (centre - half, centre + half)


def fmt_pct(k: int, n: int) -> str:
    lo, hi = wilson_ci(k, n)
    return f"{k}/{n} = {100 * k / n:.1f}% [95% CI {100 * lo:.1f}–{100 * hi:.1f}]"


def cramers_v(table: pd.DataFrame | np.ndarray) -> float:
    from scipy.stats import chi2_contingency

    table = np.asarray(table)
    chi2 = chi2_contingency(table, correction=False)[0]
    k = min(table.shape) - 1
    return float(np.sqrt(chi2 / (table.sum() * k))) if k > 0 else float("nan")


def expected_count_report(table: pd.DataFrame | np.ndarray) -> str:
    from scipy.stats import chi2_contingency

    expected = chi2_contingency(np.asarray(table))[3]
    return (
        f"min expected = {expected.min():.2f}; "
        f"cells with expected < 5: {(expected < 5).mean() * 100:.0f}%"
    )


def cluster_bootstrap(
    df: pd.DataFrame,
    stat,
    cluster: str = "post_id",
    n_boot: int = 2000,
    seed: int = 0,
) -> tuple[float, tuple[float, float], np.ndarray]:
    """Point estimate and percentile CI of ``stat(df)``, resampling whole clusters."""
    groups = {k: g for k, g in df.groupby(cluster, sort=False)}
    keys = np.array(list(groups))
    rng = np.random.default_rng(seed)
    point = stat(df)
    draws = []
    for _ in range(n_boot):
        sample = rng.choice(keys, size=len(keys), replace=True)
        boot = pd.concat([groups[k] for k in sample], ignore_index=True)
        value = stat(boot)
        if np.isfinite(value):
            draws.append(value)
    draws = np.asarray(draws)
    return (
        float(point),
        (float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))),
        draws,
    )


def clustered_logit(df: pd.DataFrame, formula: str, cluster: str = "post_id", maxiter: int = 35):
    """Logistic regression with standard errors clustered on ``cluster`` (default: the dream).

    ``maxiter`` is passed to the Newton optimiser (statsmodels' default is 35).
    """
    import statsmodels.formula.api as smf

    data = df.dropna(subset=[cluster]).copy()
    model = smf.logit(formula, data=data)
    groups = pd.factorize(data.loc[model.data.row_labels, cluster])[0]
    return model.fit(disp=0, maxiter=maxiter, cov_type="cluster", cov_kwds={"groups": groups})


def odds_ratio_table(result, terms: Iterable[str] | None = None) -> pd.DataFrame:
    """OR, 95% CI and p for the terms of a fitted (clustered) logit."""
    params, ci, p = result.params, result.conf_int(), result.pvalues
    terms = list(terms) if terms is not None else [t for t in params.index if t != "Intercept"]
    return pd.DataFrame(
        {
            "OR": np.exp(params[terms]),
            "lo": np.exp(ci.loc[terms, 0]),
            "hi": np.exp(ci.loc[terms, 1]),
            "p": p[terms],
        }
    )
