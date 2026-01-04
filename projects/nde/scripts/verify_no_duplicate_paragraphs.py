from __future__ import annotations

import json
from pathlib import Path


def count_duplicates(root: Path) -> tuple[int, int]:
    total = 0
    dupes = 0
    for path in root.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        content = data.get("content") or ""
        normalized = content.replace("\r\n", "\n").replace("\r", "\n")
        paragraphs = [p.strip() for p in normalized.split("\n\n") if p.strip()]
        total += 1
        if len(paragraphs) != len(set(paragraphs)):
            dupes += 1
    return total, dupes


def main() -> None:
    n_total, n_dupes = count_duplicates(Path("output/nderf"))
    i_total, i_dupes = count_duplicates(Path("output/iands"))
    print(f"NDERF duplicates remaining: {n_dupes} / {n_total}")
    print(f"IANDS duplicates remaining: {i_dupes} / {i_total}")


if __name__ == "__main__":
    main()
