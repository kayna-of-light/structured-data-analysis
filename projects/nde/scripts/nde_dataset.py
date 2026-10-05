"""Verified loader for the NDE structured extractions (schema 2026-01-06).

Every analysis notebook should load data through this module. It exists because
an audit (docs/STATISTICAL_AUDIT_2026-10.md) found that most errors in the
notebooks came from ad-hoc field access: wrong nesting paths, legacy (v1) field
names, and comparisons against enum values that do not exist in the schema
(e.g. ``'yes'`` instead of ``'yes_explicit'``, ``'EXTREME'`` instead of
``'severe'``). Such comparisons silently evaluate to ``False`` and produce 0%.

The module therefore:

* flattens every leaf field of ``NDEAnalysisResponse`` into one column, with a
  deterministic, unambiguous name (see :data:`COLUMN_PATHS`);
* exposes the allowed enum values of every column, taken from the Pydantic
  schema itself (:func:`allowed_values`);
* provides :func:`isin`, which raises if asked to match a value the schema
  cannot produce;
* drops exact duplicate narratives (identical ``content_checksum``);
* attaches the word count of the raw source narrative, the main covariate for
  the narrative-detail confound (longer accounts mention more of everything).
"""

from __future__ import annotations

import json
import sys
import typing
from collections.abc import Iterable
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

NDE_ROOT = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = NDE_ROOT / "structured"
DATA_ROOT = NDE_ROOT.parent.parent / "data"

if str(NDE_ROOT) not in sys.path:
    sys.path.insert(0, str(NDE_ROOT))

from models.questionnaire import NDEAnalysisResponse

# ---------------------------------------------------------------------------
# Value groups used throughout the analyses (all verified against the schema)
# ---------------------------------------------------------------------------
YES = ("yes_explicit", "implied")
LIFE_REVIEW_YES = ("brief", "extensive")
BOUNDARY_YES = ("physical_barrier", "threshold", "verbal_limit")
DECEASED_YES = ("named", "unnamed")

#: Being identifications treated as "Light Being" candidates in notebooks 01/04.
LIGHT_BEING_IDS = ("god", "jesus", "religious_figure_specified", "buddha", "unknown_presence")
#: Remaining being identifications.
OTHER_BEING_IDS = ("deceased_relative_guide", "angels", "other")
#: Named religious figures (any tradition), used for "religious figure" counts.
RELIGIOUS_FIGURE_IDS = ("god", "jesus", "religious_figure_specified", "buddha")

#: Ordinal codings. Ranks start at 0 = absent.
FEAR_SCALE = {"none": 0, "minimal": 1, "moderate": 2, "significant": 3, "severe": 4}
SPIRITUALITY_SCALE = {"none": 0, "low": 1, "moderate": 2, "high": 3, "central": 4}
RELIGIOSITY_SCALE = {"none": 0, "low": 1, "moderate": 2, "high": 3, "devout": 4}


# ---------------------------------------------------------------------------
# Schema introspection
# ---------------------------------------------------------------------------
def _unwrap(annotation: Any) -> tuple[Any, bool]:
    """Return (inner type, is_list) for Optional/List annotations."""
    is_list = False
    origin = typing.get_origin(annotation)
    while origin is not None:
        args = [a for a in typing.get_args(annotation) if a is not type(None)]
        if origin in (list, list):
            is_list = True
        annotation = args[0]
        origin = typing.get_origin(annotation)
    return annotation, is_list


def _walk(model: type, prefix: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], Any, bool]]:
    hints = typing.get_type_hints(model)
    for name in model.model_fields:
        inner, is_list = _unwrap(hints[name])
        path = prefix + (name,)
        if isinstance(inner, type) and hasattr(inner, "model_fields"):
            yield from _walk(inner, path)
        else:
            yield path, inner, is_list


@lru_cache(maxsize=1)
def _schema_leaves() -> dict[str, tuple[tuple[str, ...], Any, bool]]:
    leaves = list(_walk(NDEAnalysisResponse))
    counts: dict[str, int] = {}
    for path, _, _ in leaves:
        counts[path[-1]] = counts.get(path[-1], 0) + 1
    columns: dict[str, tuple[tuple[str, ...], Any, bool]] = {}
    for path, inner, is_list in leaves:
        name = path[-1] if counts[path[-1]] == 1 else f"{path[-2]}_{path[-1]}"
        if name in columns:
            raise RuntimeError(f"Ambiguous column name {name}")
        columns[name] = (path, inner, is_list)
    return columns


#: column name -> dotted path inside ``extraction``
COLUMN_PATHS: dict[str, str] = {k: ".".join(v[0]) for k, v in _schema_leaves().items()}


def allowed_values(column: str) -> tuple[str, ...] | None:
    """Enum values the schema allows for ``column`` (None for free/bool/int fields)."""
    _, inner, _ = _schema_leaves()[column]
    if isinstance(inner, type) and issubclass(inner, Enum):
        return tuple(m.value for m in inner)
    return None


def check_values(column: str, values: Iterable[str]) -> tuple[str, ...]:
    """Raise ``ValueError`` if any of ``values`` cannot occur in ``column``."""
    values = tuple(values)
    allowed = allowed_values(column)
    if allowed is None:
        raise ValueError(f"{column} is not an enum column")
    bad = [v for v in values if v not in allowed]
    if bad:
        raise ValueError(f"{column}: values {bad} are not in the schema; allowed = {allowed}")
    return values


def isin(df: pd.DataFrame, column: str, values: Iterable[str]) -> pd.Series:
    """Schema-checked ``isin``. Works for scalar and list (multi-select) columns."""
    values = check_values(column, values)
    _, _, is_list = _schema_leaves()[column]
    if is_list:
        vs = set(values)
        return df[column].apply(lambda xs: bool(vs.intersection(xs)))
    return df[column].isin(values)


def has(df: pd.DataFrame, column: str, value: str) -> pd.Series:
    """Schema-checked membership test for a single value."""
    return isin(df, column, [value])


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------
def _get(d: dict[str, Any], path: tuple[str, ...]) -> Any:
    for key in path:
        if not isinstance(d, dict):
            return None
        d = d.get(key)
    return d


def _raw_path(record: dict[str, Any]) -> Path:
    rel = record["source_file"].replace("\\", "/").split("/data/")[-1]
    return DATA_ROOT / rel


def raw_word_count(record: dict[str, Any]) -> float:
    """Word count of the raw scraped narrative (NaN if the file is missing)."""
    path = _raw_path(record)
    if not path.exists():
        return float("nan")
    raw = json.loads(path.read_text(encoding="utf-8"))
    return float(len((raw.get("content") or "").split()))


def load_records(dedupe: bool = True) -> list[dict[str, Any]]:
    """Load structured JSON records, sorted by file name.

    With ``dedupe=True`` records whose ``content_checksum`` repeats an earlier
    record are dropped (2 exact duplicate pairs exist in the 2026-01-06 run).
    """
    records, seen = [], set()
    for path in sorted(STRUCTURED_DIR.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        checksum = record.get("content_checksum")
        if dedupe and checksum in seen:
            continue
        seen.add(checksum)
        record["_file"] = path.name
        records.append(record)
    return records


def load_frame(dedupe: bool = True, word_counts: bool = True) -> pd.DataFrame:
    """One row per NDE, one column per schema leaf, plus derived helper columns.

    Derived columns
    ---------------
    ``dataset``           'nderf' or 'iands' (from the record, not the file name)
    ``file``              structured file name
    ``word_count``        words in the raw narrative (if ``word_counts``)
    ``log_words``         log(1 + word_count)
    ``has_light_being``   any of :data:`LIGHT_BEING_IDS` in being_identifications
    ``has_other_being``   any of :data:`OTHER_BEING_IDS` in being_identifications
    ``bol_encounter``     light_encounter == 'being_of_light'
    ``life_review``       occurrence in brief/extensive
    ``any_boundary``      boundary_encounter in physical_barrier/threshold/verbal_limit
    """
    leaves = _schema_leaves()
    rows = []
    for record in load_records(dedupe=dedupe):
        ext = record.get("extraction") or {}
        row: dict[str, Any] = {
            "file": record["_file"],
            "dataset": record.get("dataset"),
            "title": record.get("title"),
        }
        for name, (path, _, is_list) in leaves.items():
            value = _get(ext, path)
            if is_list:
                value = list(value) if isinstance(value, list) else []
            row[name] = value
        if word_counts:
            row["word_count"] = raw_word_count(record)
        rows.append(row)
    df = pd.DataFrame(rows)
    if word_counts:
        df["log_words"] = np.log1p(df["word_count"])
    df["has_light_being"] = isin(df, "being_identifications", LIGHT_BEING_IDS)
    df["has_other_being"] = isin(df, "being_identifications", OTHER_BEING_IDS)
    df["bol_encounter"] = has(df, "light_encounter", "being_of_light")
    df["life_review"] = isin(df, "occurrence", LIFE_REVIEW_YES)
    df["any_boundary"] = isin(df, "boundary_encounter", BOUNDARY_YES)
    return df


# ---------------------------------------------------------------------------
# Small statistics helpers shared by the notebooks
# ---------------------------------------------------------------------------
def wilson_ci(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Wilson score interval for a proportion k/n."""
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
    """'k/n = p% [95% CI lo–hi]' using the Wilson interval."""
    lo, hi = wilson_ci(k, n)
    return f"{k}/{n} = {100 * k / n:.1f}% [95% CI {100 * lo:.1f}–{100 * hi:.1f}]"


def cramers_v(table: pd.DataFrame | np.ndarray) -> float:
    from scipy.stats import chi2_contingency

    table = np.asarray(table)
    chi2 = chi2_contingency(table, correction=False)[0]
    n = table.sum()
    k = min(table.shape) - 1
    return float(np.sqrt(chi2 / (n * k))) if k > 0 else float("nan")


def expected_count_report(table: pd.DataFrame | np.ndarray) -> str:
    """Summarise the chi-square expected-count assumption (Cochran's rule)."""
    from scipy.stats import chi2_contingency

    expected = chi2_contingency(np.asarray(table))[3]
    lt5 = (expected < 5).mean() * 100
    return f"min expected = {expected.min():.2f}; cells with expected < 5: {lt5:.0f}%"


def adjusted_odds_ratio(
    df: pd.DataFrame, outcome: str, exposure: str, covariates: Iterable[str] = ("log_words",)
):
    """Logistic regression OR for a binary exposure, adjusted for covariates.

    Returns a dict with crude and adjusted OR, 95% CI and p-value.
    """
    import statsmodels.api as sm

    covariates = list(covariates)
    data = df[[outcome, exposure] + covariates].dropna().astype(float)
    y = data[outcome]
    crude = sm.Logit(y, sm.add_constant(data[[exposure]])).fit(disp=0)
    adj = sm.Logit(y, sm.add_constant(data[[exposure] + covariates])).fit(disp=0)
    ci = np.exp(adj.conf_int().loc[exposure])
    return {
        "n": len(data),
        "crude_or": float(np.exp(crude.params[exposure])),
        "adj_or": float(np.exp(adj.params[exposure])),
        "adj_ci": (float(ci[0]), float(ci[1])),
        "adj_p": float(adj.pvalues[exposure]),
    }
