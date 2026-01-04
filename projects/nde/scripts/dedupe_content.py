from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from text_cleanup import dedupe_paragraphs


def iter_targets(paths: Iterable[Path]) -> Iterable[Path]:
    for path in paths:
        if path.is_file() and path.suffix == ".json":
            yield path
            continue
        if path.is_dir():
            yield from sorted(path.glob("*.json"))


def process_file(path: Path, apply: bool) -> tuple[int, int]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return (0, 0)
    original = str(data.get("content") or "")
    cleaned, removed = dedupe_paragraphs(original)
    if removed == 0:
        return (0, 0)
    if apply:
        data["content"] = cleaned
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return (1, removed)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove duplicate paragraphs from scraped JSON content"
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("../../../data/nderf"), Path("../../../data/iands")],
        help="Files or directories to sanitize",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the deduplicated text back to disk",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each file that would be updated",
    )
    args = parser.parse_args()

    total_files = 0
    total_removed = 0
    changed_files = 0

    targets = list(iter_targets(args.paths))
    for path in targets:
        total_files += 1
        changed, removed = process_file(path, args.apply)
        if changed:
            changed_files += 1
            total_removed += removed
            if args.verbose:
                action = "Updated" if args.apply else "Would update"
                print(f"{action} {path} (removed {removed} paragraphs)")

    if not targets:
        print("No JSON files matched the provided paths.")
        return

    if args.apply:
        print(
            f"Updated {changed_files} of {total_files} files; removed {total_removed} duplicate paragraphs"
        )
    else:
        print(
            f"Dry run: {changed_files} of {total_files} files contain duplicates; rerun with --apply to write changes"
        )


if __name__ == "__main__":
    main()
