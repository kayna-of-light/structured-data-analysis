"""Quick anomaly scan for downloaded NDERF JSON files."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

from nderf_scraper import canonicalize_url

MAX_EXAMPLES = 20
ISSUE_LABELS = {
    "invalid_json": "Invalid JSON files",
    "missing_id": "Missing id field",
    "missing_source": "Missing source_url field",
    "http_sources": "Files saved from http:// URLs",
    "missing_nde_code": "Missing nde_code",
    "empty_content": "Empty or whitespace-only content",
    "misparsed_content": "Content begins with 'Experience Description' (likely misparsed)",
}


def summarize_duplicates(counter: Counter[str], top_n: int) -> List[Tuple[str, int]]:
    items = [(key, value) for key, value in counter.items() if value > 1]
    items.sort(key=lambda pair: pair[1], reverse=True)
    return items[:top_n]


def track_issue(store: Dict[str, Dict[str, List[str] | int]], key: str, example: str | None = None) -> None:
    bucket = store.setdefault(key, {"count": 0, "examples": []})
    bucket["count"] += 1
    if example and len(bucket["examples"]) < MAX_EXAMPLES:
        bucket["examples"].append(example)


def record_issue_metadata(
    registry: Dict[str, List[Dict[str, str]]],
    key: str,
    *,
    path: str,
    entry_id: str,
    source_url: str,
) -> None:
    registry.setdefault(key, []).append(
        {
            "path": path,
            "id": entry_id,
            "source_url": source_url,
        }
    )


def export_issue_values(
    registry: Dict[str, List[Dict[str, str]]],
    issue: str,
    field: str,
    destination: Path | None,
) -> None:
    records = registry.get(issue, [])
    if not records:
        print(f"No records to export for issue '{issue}'")
        return
    valid_fields = {"source_url", "path", "id"}
    if field not in valid_fields:
        raise SystemExit(f"Invalid export field '{field}'; choose from {sorted(valid_fields)}")
    values: List[str] = []
    seen: set[str] = set()
    for entry in records:
        value = (entry.get(field) or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        values.append(value)
    if not values:
        print(f"No non-empty '{field}' values to export for issue '{issue}'")
        return
    payload = "\n".join(values) + "\n"
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(payload, encoding="utf-8")
        print(f"Exported {len(values)} values to {destination}")
    else:
        print("\n".join(values))


def main(
    output_dir: Path,
    top_n: int,
    export_issue: str | None,
    export_field: str,
    export_output: Path | None,
) -> None:
    if not output_dir.exists():
        raise SystemExit(f"Directory not found: {output_dir}")

    canon_counter: Counter[str] = Counter()
    id_counter: Counter[str] = Counter()
    canon_examples: Dict[str, List[str]] = defaultdict(list)

    stats = {"total_files": 0}
    issues: Dict[str, Dict[str, List[str] | int]] = {}
    issue_registry: Dict[str, List[Dict[str, str]]] = defaultdict(list)

    json_paths = sorted(output_dir.glob("*.json"))
    for path in json_paths:
        stats["total_files"] += 1
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except json.JSONDecodeError as exc:
            track_issue(issues, "invalid_json", f"{path.name}: {exc}")
            record_issue_metadata(
                issue_registry,
                "invalid_json",
                path=path.name,
                entry_id="",
                source_url="",
            )
            continue

        entry_id = str(data.get("id", "")).strip()
        source_url = (data.get("source_url") or "").strip()
        nde_code = (data.get("nde_code") or "").strip()
        content = (data.get("content") or "").strip()

        if not entry_id:
            track_issue(issues, "missing_id", path.name)
            record_issue_metadata(issue_registry, "missing_id", path=path.name, entry_id="", source_url=source_url)
        else:
            id_counter[entry_id] += 1

        if not source_url:
            track_issue(issues, "missing_source", path.name)
            record_issue_metadata(issue_registry, "missing_source", path=path.name, entry_id=entry_id, source_url="")
        else:
            if source_url.lower().startswith("http://"):
                track_issue(issues, "http_sources", path.name)
                record_issue_metadata(
                    issue_registry,
                    "http_sources",
                    path=path.name,
                    entry_id=entry_id,
                    source_url=source_url,
                )
            try:
                canon_url = canonicalize_url(source_url)
            except Exception:
                canon_url = source_url
            canon_counter[canon_url] += 1
            if len(canon_examples[canon_url]) < MAX_EXAMPLES:
                canon_examples[canon_url].append(path.name)

        if not nde_code:
            track_issue(issues, "missing_nde_code", path.name)
            record_issue_metadata(
                issue_registry,
                "missing_nde_code",
                path=path.name,
                entry_id=entry_id,
                source_url=source_url,
            )

        if not content:
            track_issue(issues, "empty_content", path.name)
            record_issue_metadata(
                issue_registry,
                "empty_content",
                path=path.name,
                entry_id=entry_id,
                source_url=source_url,
            )
        elif content.lstrip().lower().startswith("experience description"):
            preview = content[:120].replace("\n", " ")
            track_issue(issues, "misparsed_content", f"{path.name}: {preview}")
            record_issue_metadata(
                issue_registry,
                "misparsed_content",
                path=path.name,
                entry_id=entry_id,
                source_url=source_url,
            )

    print(f"Analyzed files: {stats['total_files']}")
    for key, label in ISSUE_LABELS.items():
        bucket = issues.get(key)
        if not bucket:
            continue
        print(f"{label}: {bucket['count']}")
        for example in bucket["examples"]:
            print("  ", example)

    dup_id_lines = summarize_duplicates(id_counter, top_n)
    if dup_id_lines:
        print("Duplicate IDs:")
        for key, count in dup_id_lines:
            print(f"  {key} -> {count} occurrences")

    dup_url_lines = summarize_duplicates(canon_counter, top_n)
    if dup_url_lines:
        print("Duplicate canonical source URLs:")
        for canon_url, count in dup_url_lines:
            print(f"  {canon_url} -> {count} occurrences")
            for sample in canon_examples[canon_url][:3]:
                print(f"     - {sample}")

    if export_issue:
        export_issue_values(issue_registry, export_issue, export_field, export_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Report possible anomalies in scraped NDERF data")
    parser.add_argument("--root", type=Path, default=Path("output/nderf"), help="Directory containing JSON files")
    parser.add_argument("--top", type=int, default=10, help="How many duplicate entries to list")
    parser.add_argument(
        "--export-issue",
        choices=sorted(ISSUE_LABELS.keys()),
        help="If provided, emit the requested field for every file matching the given issue",
    )
    parser.add_argument(
        "--export-field",
        choices=["source_url", "path", "id"],
        default="source_url",
        help="Which value to output when exporting issue data (default: %(default)s)",
    )
    parser.add_argument(
        "--export-output",
        type=Path,
        help="Optional path to save the exported values (defaults to stdout)",
    )
    args = parser.parse_args()
    main(args.root, args.top, args.export_issue, args.export_field, args.export_output)
