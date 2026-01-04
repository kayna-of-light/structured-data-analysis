from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Mapping
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

from aggregate_experiences import (
    IANDS_DIR,
    NDERF_DIR,
    ROOT,
    format_entry,
    gather_entries,
)

OUTPUT_PDF_DIR = ROOT / "output" / "compiled_experiences_pdf"
MAX_PDF_BYTES = 5 * 1024 * 1024
PDF_CHUNK_ESTIMATE_BYTES = 4 * 1024 * 1024

_styles = getSampleStyleSheet()
TITLE_STYLE = ParagraphStyle(
    "EntryTitle",
    parent=_styles["Heading2"],
    fontSize=16,
    leading=20,
    spaceAfter=6,
)
META_STYLE = ParagraphStyle(
    "Meta",
    parent=_styles["BodyText"],
    textColor=colors.HexColor("#444444"),
    spaceAfter=6,
)
BODY_STYLE = ParagraphStyle(
    "Body",
    parent=_styles["BodyText"],
    leading=14,
    spaceAfter=6,
)
SECTION_STYLE = ParagraphStyle(
    "SectionHeading",
    parent=_styles["Heading3"],
    spaceBefore=6,
    spaceAfter=6,
)
QA_STYLE = ParagraphStyle(
    "QA",
    parent=_styles["BodyText"],
    leftIndent=12,
    leading=14,
    spaceAfter=4,
)


def sanitize(text: str) -> str:
    return escape(text or "").replace("\n", "<br/>")


def entry_flowables(entry: Mapping[str, object]) -> List:
    flow: List = []
    flow.append(Paragraph(sanitize(str(entry.get("title") or "Untitled Experience")), TITLE_STYLE))

    meta_parts: List[str] = []
    date = str(entry.get("date") or "").strip()
    if date:
        meta_parts.append(f"<b>Date:</b> {sanitize(date)}")
    dataset = str(entry.get("dataset") or "").strip()
    if dataset:
        meta_parts.append(f"<b>Dataset:</b> {sanitize(dataset)}")
    source_url = str(entry.get("source_url") or "").strip()
    if source_url:
        meta_parts.append(f"<b>Source:</b> {sanitize(source_url)}")
    if meta_parts:
        flow.append(Paragraph(" &nbsp;&nbsp;".join(meta_parts), META_STYLE))

    content = str(entry.get("content") or "").strip()
    if content:
        for paragraph in content.split("\n\n"):
            cleaned = paragraph.strip()
            if not cleaned:
                continue
            flow.append(Paragraph(sanitize(cleaned), BODY_STYLE))
        flow.append(Spacer(1, 6))

    qa_items: Iterable = entry.get("qa") or []
    qa_items = list(qa_items)
    if qa_items:
        flow.append(Paragraph("Questions & Answers", SECTION_STYLE))
        for question, answer in qa_items:
            q = sanitize(str(question or "Question"))
            a = sanitize(str(answer or "No answer provided."))
            flow.append(Paragraph(f"<b>{q}:</b> {a}", QA_STYLE))
        flow.append(Spacer(1, 6))

    return flow


def build_chunks(entries: List[Mapping[str, object]]) -> List[List[Mapping[str, object]]]:
    chunks: List[List[Mapping[str, object]]] = []
    current: List[Mapping[str, object]] = []
    current_size = 0
    for idx, entry in enumerate(entries):
        separator = "---\n\n" if idx == 0 else "\n---\n\n"
        block_bytes = len((separator + format_entry(entry)).encode("utf-8"))
        if current and current_size + block_bytes > PDF_CHUNK_ESTIMATE_BYTES:
            chunks.append(current)
            current = []
            current_size = 0
        current.append(entry)
        current_size += block_bytes
    if current:
        chunks.append(current)
    return chunks


def write_pdf(chunk_index: int, chunk_entries: List[Mapping[str, object]]) -> tuple[Path, int]:
    OUTPUT_PDF_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_PDF_DIR / f"experiences_part-{chunk_index:03d}.pdf"
    doc = SimpleDocTemplate(
        str(target),
        pagesize=LETTER,
        title=f"Near-Death Experiences Part {chunk_index:03d}",
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    story = []
    for entry in chunk_entries:
        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=colors.HexColor("#777777"),
                spaceBefore=12,
                spaceAfter=12,
            )
        )
        story.extend(entry_flowables(entry))
    doc.build(story)
    size = target.stat().st_size
    return target, size


def write_chunk_with_limit(
    chunk_entries: List[Mapping[str, object]],
    chunk_index: int,
    written: List[Path],
) -> int:
    path, size = write_pdf(chunk_index, chunk_entries)
    if size > MAX_PDF_BYTES and len(chunk_entries) > 1:
        path.unlink(missing_ok=True)
        mid = max(1, len(chunk_entries) // 2)
        next_index = write_chunk_with_limit(chunk_entries[:mid], chunk_index, written)
        return write_chunk_with_limit(chunk_entries[mid:], next_index, written)

    if size > MAX_PDF_BYTES:
        print(
            f"Warning: {path.name} is {size / (1024 * 1024):.2f} MB and cannot be reduced further (single entry)."
        )
    written.append(path)
    return chunk_index + 1


def collect_entries() -> List[Mapping[str, object]]:
    entries: List[Mapping[str, object]] = []
    entries.extend(list(gather_entries(NDERF_DIR, "NDERF") or []))
    entries.extend(list(gather_entries(IANDS_DIR, "IANDS") or []))
    dataset_rank = {"NDERF": 0, "IANDS": 1}
    entries.sort(key=lambda item: (dataset_rank.get(item.get("dataset"), 99), str(item.get("title")).lower()))
    return entries


def remove_existing_pdfs() -> None:
    if not OUTPUT_PDF_DIR.exists():
        return
    for path in OUTPUT_PDF_DIR.glob("*.pdf"):
        if path.is_file():
            path.unlink()


def main() -> None:
    entries = collect_entries()
    if not entries:
        print("No experiences found to export.")
        return
    remove_existing_pdfs()
    chunks = build_chunks(entries)
    written: List[Path] = []
    next_index = 1
    for chunk_entries in chunks:
        next_index = write_chunk_with_limit(chunk_entries, next_index, written)
    print(
        f"Wrote {len(entries)} experiences into {len(written)} PDF files in {OUTPUT_PDF_DIR}"
    )


if __name__ == "__main__":
    main()
