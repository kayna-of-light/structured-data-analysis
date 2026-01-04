from __future__ import annotations

from typing import Iterable, Tuple


def _normalize_paragraphs(text: str) -> Iterable[str]:
    normalized = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    # Split on double newlines to approximate paragraphs while keeping order.
    for chunk in normalized.split("\n\n"):
        cleaned = chunk.strip()
        if cleaned:
            yield cleaned


def dedupe_paragraphs(text: str) -> Tuple[str, int]:
    """Remove repeated paragraphs while preserving the first occurrence.

    Paragraph boundaries are inferred by blank-line separation. Two paragraphs are
    considered duplicates only when their trimmed text matches exactly. The
    function returns the cleaned text plus the number of paragraphs removed.
    """

    paragraphs = list(_normalize_paragraphs(text))
    if not paragraphs:
        return "", 0

    seen: set[str] = set()
    cleaned: list[str] = []
    removed = 0
    for paragraph in paragraphs:
        if paragraph in seen:
            removed += 1
            continue
        seen.add(paragraph)
        cleaned.append(paragraph)
    return "\n\n".join(cleaned), removed
