"""Utility to collapse suffixed duplicate JSON files in data/nderf."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List

SUFFIX_PATTERN = re.compile(r"^(?P<base>.+?)-(\d{3})\.json$")


@dataclass
class VariantGroup:
    base: str
    base_path: Path
    variants: List[Path]

    @property
    def canonical_path(self) -> Path:
        return self.base_path


def collect_variants(root: Path) -> Dict[str, VariantGroup]:
    mapping: Dict[str, VariantGroup] = {}
    for path in sorted(root.glob("*.json")):
        match = SUFFIX_PATTERN.match(path.name)
        if not match:
            continue
        base = match.group("base")
        group = mapping.get(base)
        if group is None:
            group = VariantGroup(base=base, base_path=root / f"{base}.json", variants=[])
            mapping[base] = group
        group.variants.append(path)
    return mapping


def resolve_group(group: VariantGroup, *, apply: bool) -> dict:
    candidates = list(group.variants)
    if group.base_path.exists():
        candidates.append(group.base_path)
    if not candidates:
        return {"kept": None, "deleted": [], "created": False}

    newest = max(candidates, key=lambda path: path.stat().st_mtime)
    kept_path = group.base_path
    kept_existed = kept_path.exists()
    created = False
    deleted: List[tuple[Path, int]] = []

    if newest != kept_path:
        data = newest.read_bytes()
        kept_path.write_bytes(data)
        created = not kept_existed

    seen = set()
    for path in candidates:
        if path == kept_path:
            continue
        if path in seen:
            continue
        seen.add(path)
        if not apply:
            continue
        try:
            size = path.stat().st_size
        except FileNotFoundError:
            size = 0
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        else:
            deleted.append((path, size))

    if apply:
        return {"kept": kept_path, "deleted": deleted, "created": created}

    return {"kept": kept_path, "deleted": [], "created": created}


def cleanup(root: Path, *, apply: bool) -> None:
    groups = collect_variants(root)
    if not groups:
        print("No suffixed duplicates detected.")
        return

    print(f"Detected {len(groups)} base names with suffixed variants")
    total_suffixes = sum(len(group.variants) for group in groups.values())
    print(f"Total suffixed files: {total_suffixes}")

    deleted_files = 0
    deleted_bytes = 0

    for group in groups.values():
        result = resolve_group(group, apply=apply)
        kept = result["kept"]
        if not apply:
            variant_names = ", ".join(path.name for path in group.variants)
            print(f"{kept.name if kept else group.base + '.json'} -> variants: {variant_names}")
            continue
        for path, size in result["deleted"]:
            deleted_files += 1
            deleted_bytes += size

    if apply:
        print(f"Removed {deleted_files} files (freed ~{deleted_bytes/1024:.1f} KiB)")
    else:
        print("Run again with --apply to delete the duplicates")


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove suffixed *-###.json duplicates")
    parser.add_argument("--root", type=Path, default=Path("../../data/nderf"), help="Directory to scan")
    parser.add_argument("--apply", action="store_true", help="Actually delete the duplicates")
    args = parser.parse_args()
    cleanup(args.root, apply=args.apply)


if __name__ == "__main__":
    main()
