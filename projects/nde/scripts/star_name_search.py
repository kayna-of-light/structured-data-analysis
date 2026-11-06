#!/usr/bin/env python3
"""Full-text search of the raw NDE narratives for the star names of the contact literature.

Purpose
-------
The literary-compilation document *From Planets to Constellations* asks whether unforced
experiences (NDEs) carry the astronomical addresses that the contactee and channelled
literature gives its beings (the Pleiades, Sirius, Arcturus, Lyra, Vega, Andromeda,
Orion, Zeta Reticuli, "starseed"). This script lists every raw narrative that names one
of them, with context, so that each hit can be read and classified by hand.

Prediction (stated before the search): if the stellar address belongs to the literature
rather than to the experience, named stars will be rare in spontaneous accounts, and
where a being or the experiencer's origin is tied to a star, the label will tend to
arrive after the experience from an outside source. A miss would be a substantial number
of accounts in which the experience itself supplies a named star as a being's home.

This is a keyword search of the raw text, not a coded variable: it has no reliability
statistic, and every hit must be read. Searching raw files (not ``nd.load_frame()``)
is deliberate, because the structured schema has no field for star names.

Usage::

    python projects/nde/scripts/star_name_search.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCES = [ROOT / "data" / "nderf", ROOT / "data" / "iands"]

STAR_TERMS = re.compile(
    r"\b(pleiad\w*|pl[eé]iades|arctur\w*|sirius|sirian\w*|lyra|lyran\w*|vega|"
    r"andromed\w*|orion\w*|zeta reticuli|reticulan\w*|starseed\w*)\b",
    re.IGNORECASE,
)

# Hits read and found not to be about the experience (checked by hand, 2026-11-02).
NOT_ABOUT_EXPERIENCE = {
    "01575_lindsey-s-nde-3532.json": "Orion is the narrator's son",
    "04708_arnulfo-g-nde-8900.json": "NASA's Orion spacecraft programme",
    "10002_cougar-nde-62.json": "an e-mail address",
    "confirmation-of-eternity.json": "a Chevrolet Vega",
    "10030_christianne-ndes-18-nde-18.json": "a Chevrolet Vega",
}


def main() -> None:
    files = sorted(p for src in SOURCES for p in src.glob("*.json"))
    hits: dict[str, list[str]] = {}
    for path in files:
        text = json.loads(path.read_text(encoding="utf-8")).get("content") or ""
        for m in STAR_TERMS.finditer(text):
            ctx = re.sub(r"\s+", " ", text[max(0, m.start() - 200) : m.end() + 200])
            hits.setdefault(f"{path.parent.name}/{path.name}", []).append(ctx)

    print(f"raw files searched: {len(files)}")
    print(f"files with a star term: {len(hits)}")
    relevant = {k: v for k, v in hits.items() if k.split("/")[1] not in NOT_ABOUT_EXPERIENCE}
    print(f"excluded (not about the experience): {len(hits) - len(relevant)}")
    print(f"accounts naming a star in connection with the experience: {len(relevant)}\n")
    for name, ctxs in relevant.items():
        print(f"## {name}")
        for c in dict.fromkeys(ctxs):
            print(f"   ...{c}...")
        print()


if __name__ == "__main__":
    main()
