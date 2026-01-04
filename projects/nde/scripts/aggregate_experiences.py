from __future__ import annotations

import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Iterable, List, Mapping

from text_cleanup import dedupe_paragraphs

# Updated paths for new structure
ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(ROOT / "shared"))

from registry import load_registry

OUTPUT_DIR = ROOT / "output" / "compiled_experiences"
LEGACY_SINGLE_FILE = ROOT / "output" / "all_experiences.md"
MAX_CHUNK_BYTES = 18 * 1024 * 1024  # ~18 MB target to stay under 20 MB


def load_json(path: Path) -> Mapping[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=OrderedDict)


def gather_entries_from_registry(registry_path: Path, dataset_label: str) -> Iterable[dict]:
    """Gather entries using registry system."""
    if not registry_path.exists():
        print(f"Warning: Registry not found: {registry_path}")
        return
    
    registry = load_registry(registry_path)
    
    for dataset_name in registry.list_datasets():
        files = registry.get_files(dataset_name)
        for path in files:
            try:
                data = load_json(path)
            except json.JSONDecodeError:
                continue
            title = str(data.get("title") or path.stem).strip() or "Untitled Experience"
            date = (
                str(data.get("date") or data.get("data") or "").strip()
                or "Unknown"
            )
            content = str(data.get("content") or "").strip()
            content, _ = dedupe_paragraphs(content)
            source_url = str(data.get("source_url") or "").strip()
            elements = data.get("elements")
            if isinstance(elements, Mapping):
                qa_items = list(elements.items())
            else:
                qa_items = []
            yield {
                "dataset": dataset_label,
                "title": title,
                "date": date,
                "content": content,
                "source_url": source_url,
                "qa": qa_items,
                "path": path,
            }


def format_entry(entry: Mapping[str, object]) -> str:
    lines: List[str] = []
    title = str(entry["title"])
    lines.append(f"### {title}")
    meta_parts: List[str] = []
    date = str(entry.get("date") or "").strip()
    if date:
        meta_parts.append(f"**Date:** {date}")
    dataset = str(entry.get("dataset") or "").strip()
    if dataset:
        meta_parts.append(f"**Dataset:** {dataset}")
    source_url = str(entry.get("source_url") or "").strip()
    if source_url:
        meta_parts.append(f"**Source:** {source_url}")
    if meta_parts:
        lines.append(" ".join(meta_parts))
    content = str(entry.get("content") or "").strip()
    if content:
        lines.append("")
        lines.append(content)
    qa_items: Iterable = entry.get("qa") or []
    qa_rendered = []
    for question, answer in qa_items:
        q = str(question or "").strip()
        a = str(answer or "").strip()
        if not q and not a:
            continue
        qa_rendered.append(
            f"- **{q or 'Question'}**\n\n  {a or 'No answer provided.'}\n"
        )
    if qa_rendered:
        lines.append("")
        lines.append("#### Questions & Answers")
        lines.append("")
        lines.extend(qa_rendered)
    return "\n".join(lines).rstrip() + "\n"


def write_chunk(index: int, buffers: List[str]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / f"experiences_part-{index:03d}.md"
    payload = "".join(buffers)
    if not payload.endswith("\n"):
        payload += "\n"
    target.write_text(payload, encoding="utf-8")
    return target


def write_markdown_chunks(entries: List[Mapping[str, object]]) -> List[Path]:
    if OUTPUT_DIR.exists():
        for path in OUTPUT_DIR.glob("*.md"):
            if path.is_file():
                path.unlink()
    chunk_idx = 1
    current: List[str] = []
    current_size = 0
    written: List[Path] = []
    for idx, entry in enumerate(entries):
        separator = "---\n\n" if idx == 0 else "\n---\n\n"
        block = f"{separator}{format_entry(entry)}"
        block_bytes = len(block.encode("utf-8"))
        if current and current_size + block_bytes > MAX_CHUNK_BYTES:
            written.append(write_chunk(chunk_idx, current))
            chunk_idx += 1
            current = []
            current_size = 0
        current.append(block)
        current_size += block_bytes
    if current:
        written.append(write_chunk(chunk_idx, current))
    return written


def main() -> None:
    """Aggregate NDE experiences using registry system."""
    entries: List[dict] = []
    
    # Load from registry
    project_root = Path(__file__).parent.parent
    registry_path = project_root / "registries" / "nde_full.yaml"
    
    # Gather NDERF and IANDS entries from registry
    nderf_entries = list(gather_entries_from_registry(registry_path, "NDERF"))
    iands_entries = list(gather_entries_from_registry(registry_path, "IANDS"))
    
    # Filter by dataset name from the path
    entries.extend([e for e in nderf_entries if "nderf" in str(e["path"]).lower()])
    entries.extend([e for e in iands_entries if "iands" in str(e["path"]).lower()])
    
    dataset_rank = {"NDERF": 0, "IANDS": 1}
    entries.sort(key=lambda item: (dataset_rank.get(item["dataset"], 99), item["title"].lower()))
    
    if LEGACY_SINGLE_FILE.exists():
        LEGACY_SINGLE_FILE.unlink()
    
    chunk_paths = write_markdown_chunks(entries)
    print(
        f"Wrote {len(entries)} experiences across {len(chunk_paths)} files "
        f"in {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()
