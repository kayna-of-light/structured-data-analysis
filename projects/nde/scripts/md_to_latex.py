#!/usr/bin/env python3
"""Regenerate the LaTeX versions of a project's reports from their Markdown sources.

The Markdown reports in ``projects/<project>/reports/`` are the source of truth. This script
converts each one with pandoc and wraps it in the project's ``<project>-report-preamble`` layout
(title page, abstract with keywords, unnumbered provenance/reference sections, lettered
appendices). The project defaults to ``nde``.

Usage:
    python scripts/md_to_latex.py                     # all NDE reports that have a .tex version
    python scripts/md_to_latex.py "Being of Light - Statistical Analysis of NDE Phenomenology"
    python scripts/md_to_latex.py --project mallworld # all MallWorld reports that have a .tex version

Requires pandoc (``pip install pypandoc_binary`` provides one). Compile the output with any
LaTeX engine from ``reports/latex/``, e.g. ``tectonic "<name>.tex"`` or ``pdflatex "<name>.tex"``.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

PROJECTS_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT = "nde"
REPORTS_DIR = PROJECTS_DIR / PROJECT / "reports"
LATEX_DIR = REPORTS_DIR / "latex"


def set_project(project: str) -> None:
    """Point the converter at ``projects/<project>/reports``."""
    global PROJECT, REPORTS_DIR, LATEX_DIR
    PROJECT = project
    REPORTS_DIR = PROJECTS_DIR / project / "reports"
    LATEX_DIR = REPORTS_DIR / "latex"


PANDOC_FORMAT = "markdown+lists_without_preceding_blankline-subscript-superscript-implicit_figures"
UNNUMBERED = {"Data Provenance", "References"}

# Characters outside what pdflatex + T1 fonts render directly.
SUPERSCRIPTS = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-"))
SYMBOLS = {
    "χ": r"\ensuremath{\chi}",
    "κ": r"\ensuremath{\kappa}",
    "ρ": r"\ensuremath{\rho}",
    "η": r"\ensuremath{\eta}",
    "Δ": r"\ensuremath{\Delta}",
    "α": r"\ensuremath{\alpha}",
    "φ": r"\ensuremath{\phi}",
    "×": r"\ensuremath{\times}",
    "−": r"\ensuremath{-}",
    "≈": r"\ensuremath{\approx}",
    "≠": r"\ensuremath{\neq}",
    "≥": r"\ensuremath{\geq}",
    "≤": r"\ensuremath{\leq}",
    "±": r"\ensuremath{\pm}",
    "→": r"\ensuremath{\rightarrow}",
    "↔": r"\ensuremath{\leftrightarrow}",
    "↑": r"\ensuremath{\uparrow}",
    "↓": r"\ensuremath{\downarrow}",
    "§": r"\S{}",
    "…": r"\ldots{}",
    "–": "--",
    "—": "---",
    "é": r"\'{e}",
}


def pandoc(markdown: str, *extra: str) -> str:
    try:
        import pypandoc

        return pypandoc.convert_text(
            markdown, "latex", format=PANDOC_FORMAT, extra_args=["--wrap=preserve", *extra]
        )
    except ImportError:
        result = subprocess.run(
            ["pandoc", "-f", PANDOC_FORMAT, "-t", "latex", "--wrap=preserve", *extra],
            input=markdown,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout


def latex_safe(text: str) -> str:
    sup = "".join(SUPERSCRIPTS)
    text = re.sub(
        f"[{sup}]+",
        lambda m: r"\ensuremath{^{" + "".join(SUPERSCRIPTS[c] for c in m.group(0)) + "}}",
        text,
    )
    for char, repl in SYMBOLS.items():
        text = text.replace(char, repl)
    leftover = sorted({c for c in text if ord(c) > 127})
    if leftover:
        raise ValueError(f"unmapped non-ASCII characters: {leftover}")
    return text


def inline(markdown: str) -> str:
    out = pandoc(markdown).strip()
    return latex_safe(out)


def prepare_body(markdown: str) -> str:
    lines, seen_appendix = [], False
    for line in markdown.splitlines():
        if line.strip() == "---":
            continue  # section separators; LaTeX sections already separate content
        heading = re.match(r"^(#{2,4}) (.*)$", line)
        if heading:
            hashes, text = heading.groups()
            appendix = re.match(r"^Appendix [A-Z]: (.*)$", text)
            if hashes == "##" and appendix:
                if not seen_appendix:
                    lines += ["", r"\newpage", r"\appendix", ""]
                    seen_appendix = True
                text = appendix.group(1)
            text = re.sub(r"^\d+(\.\d+)*\.? ", "", text)  # LaTeX numbers sections itself
            if hashes == "##" and text in UNNUMBERED:
                text += " {-}"
            line = f"{hashes} {text}"
        lines.append(line)
    return "\n".join(lines)


def convert(md_path: Path) -> str:
    source = md_path.read_text(encoding="utf-8")
    title_line, rest = source.split("\n", 1)
    title = title_line.lstrip("# ").strip()
    main, _, subtitle = title.partition(": ")

    notice, _, rest = rest.partition("\n## Abstract\n")
    abstract, _, body = rest.partition("\n---\n")
    keywords = ""
    kw = re.search(r"^\*\*Keywords:?\*\*:?\s*(.+)$", abstract, flags=re.MULTILINE)
    if kw:
        keywords = kw.group(1).strip()
        abstract = abstract[: kw.start()] + abstract[kw.end() :]

    parts = [
        f"% Generated from ../{md_path.name} by scripts/md_to_latex.py.",
        "% Edit the Markdown report, then regenerate this file; do not edit it by hand.",
        rf"\input{{{PROJECT}-report-preamble}}",
        r"\usepackage{array}",
        r"\usepackage{calc}",
        r"\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}",
        r"\setlength{\emergencystretch}{3em}",
        r"\let\underscorechar\_",
        r"\renewcommand{\_}{\underscorechar\allowbreak}  % let long field names break after underscores",
        "",
        rf"\reporttitle{{{inline(main)}}}{{{inline(subtitle)}}}",
        r"\reportauthors",
        "",
        r"\begin{document}",
        "",
        r"\maketitle",
        "",
    ]
    if notice.strip():
        parts += [r"{\small", latex_safe(pandoc(notice.strip())), "}", ""]
    parts += [r"\begin{abstract}", latex_safe(pandoc(abstract.strip()))]
    if keywords:
        parts += [rf"\keywords{{{inline(keywords)}}}"]
    parts += [r"\end{abstract}", "", r"\newpage", ""]
    parts += [
        latex_safe(pandoc(prepare_body(body), "--shift-heading-level-by=-1")),
        "",
        r"\end{document}",
        "",
    ]
    return "\n".join(parts)


def main(names: list[str]) -> None:
    if not names:
        names = [
            p.stem
            for p in sorted(LATEX_DIR.glob("*.tex"))
            if not p.stem.endswith("-report-preamble")
        ]
    for name in names:
        md_path = REPORTS_DIR / f"{name}.md"
        out = LATEX_DIR / f"{name}.tex"
        out.write_text(convert(md_path), encoding="utf-8")
        print(f"wrote {out.relative_to(REPORTS_DIR.parent)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--project" in args:
        i = args.index("--project")
        set_project(args[i + 1])
        args = args[:i] + args[i + 2 :]
    main(args)
