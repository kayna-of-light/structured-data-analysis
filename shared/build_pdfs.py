#!/usr/bin/env python3
"""
Build PDFs from markdown reports.

Prefers LaTeX (pdflatex) if available for professional output with:
- Clickable hyperlinks
- Proper Greek letters and math symbols
- Professional typography

Falls back to fpdf2 if LaTeX not installed.

Usage:
    python build_pdfs.py <reports_dir>
    python build_pdfs.py ../projects/nde/reports
"""

import subprocess
import shutil
import sys
from pathlib import Path
import re
import argparse

# Check if pdflatex is available
def find_pdflatex():
    """Find pdflatex executable, checking common locations."""
    # First check PATH
    pdflatex = shutil.which('pdflatex')
    if pdflatex:
        return pdflatex
    
    # Check common MiKTeX locations on Windows
    if sys.platform == 'win32':
        common_paths = [
            Path.home() / 'AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex.exe',
            Path('C:/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe'),
            Path('C:/Program Files (x86)/MiKTeX/miktex/bin/x64/pdflatex.exe'),
        ]
        for path in common_paths:
            if path.exists():
                return str(path)
    
    return None

PDFLATEX = find_pdflatex()


def sanitize_text(text: str) -> str:
    """Replace Unicode characters with ASCII equivalents."""
    replacements = {
        'χ': 'X',  # chi
        '²': '2',  # superscript 2
        '³': '3',  # superscript 3
        '—': '-',  # em dash
        '–': '-',  # en dash
        '"': '"',  # curly quotes
        '"': '"',
        ''': "'",
        ''': "'",
        '…': '...',
        '×': 'x',  # multiplication
        '→': '->',  # arrow
        '←': '<-',
        '≈': '~',
        '≤': '<=',
        '≥': '>=',
        '±': '+/-',
        '°': ' deg',
        '•': '*',
        '\u2013': '-',  # en dash
        '\u2014': '-',  # em dash
        '\u2018': "'",  # left single quote
        '\u2019': "'",  # right single quote
        '\u201c': '"',  # left double quote  
        '\u201d': '"',  # right double quote
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    # Remove any remaining non-ASCII
    text = text.encode('ascii', 'replace').decode('ascii')
    return text


def clean_markdown_links(text: str, keep_urls: bool = False) -> str:
    """Convert markdown links to display text, optionally keeping URL info."""
    if keep_urls:
        # Return tuple-friendly format for link extraction
        return text
    # [display text](url) -> display text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Also handle bare URLs
    text = re.sub(r'https?://\S+', lambda m: truncate_url(m.group(0)), text)
    return text


def extract_links(text: str) -> list:
    """Extract markdown links as (display_text, url) tuples."""
    links = []
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
        links.append((match.group(1), match.group(2)))
    return links


def truncate_url(url: str, max_len: int = 40) -> str:
    """Truncate long URLs for display."""
    if len(url) <= max_len:
        return url
    return url[:max_len-3] + '...'


def clean_cell_text(text: str) -> str:
    """Clean table cell text - remove links, truncate if needed."""
    # Remove markdown links, keep display text
    text = clean_markdown_links(text)
    # Remove backticks
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Sanitize unicode
    text = sanitize_text(text)
    # Truncate very long cells
    if len(text) > 50:
        text = text[:47] + '...'
    return text


def compile_latex(tex_file: Path, output_dir: Path) -> Path:
    """Compile a LaTeX file to PDF using pdflatex."""
    if not PDFLATEX:
        raise RuntimeError("pdflatex not found")
    
    # Run pdflatex twice (for references)
    for _ in range(2):
        result = subprocess.run(
            [PDFLATEX, '-interaction=nonstopmode', '-output-directory', str(output_dir), str(tex_file)],
            cwd=tex_file.parent,
            capture_output=True,
            text=True
        )
    
    pdf_path = output_dir / tex_file.with_suffix('.pdf').name
    if not pdf_path.exists():
        raise RuntimeError(f"PDF not created. pdflatex output:\n{result.stdout}\n{result.stderr}")
    
    # Clean up auxiliary files
    for ext in ['.aux', '.log', '.out', '.toc']:
        aux_file = output_dir / tex_file.with_suffix(ext).name
        if aux_file.exists():
            aux_file.unlink()
    
    return pdf_path


def markdown_to_pdf_fpdf(md_file: Path, output_dir: Path) -> Path:
    """Convert markdown to PDF using fpdf2."""
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
    
    class AcademicPDF(FPDF):
        def __init__(self):
            super().__init__()
            self.set_margins(20, 20, 20)
            self.set_auto_page_break(auto=True, margin=20)
            
        def header(self):
            if self.page_no() > 1:
                self.set_font('Helvetica', 'I', 9)
                self.set_text_color(128)
                self.cell(0, 10, 'NDE Statistical Analysis', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
                self.ln(5)
                
        def footer(self):
            self.set_y(-15)
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(128)
            self.cell(0, 10, f'Page {self.page_no()}', align='C')
            
        def chapter_title(self, title: str, level: int = 1):
            sizes = {1: 16, 2: 14, 3: 12}
            self.set_font('Helvetica', 'B', sizes.get(level, 12))
            self.set_text_color(0)
            self.ln(8 if level == 1 else 5)
            self.multi_cell(0, 8, sanitize_text(clean_markdown_links(title)))
            self.ln(4)
            
        def body_text(self, text: str):
            self.set_font('Times', '', 11)
            self.set_text_color(0)
            self.multi_cell(0, 6, sanitize_text(clean_markdown_links(text)))
            self.ln(2)
            
        def critical_finding(self, text: str):
            self.set_fill_color(255, 250, 230)
            self.set_font('Times', 'B', 11)
            self.set_text_color(0)
            self.multi_cell(0, 6, f"CRITICAL FINDING: {sanitize_text(clean_markdown_links(text))}", fill=True)
            self.ln(4)
            
        def add_table(self, headers: list, rows: list):
            """Add a table with automatic column width calculation."""
            self.set_font('Helvetica', 'B', 8)
            
            # Calculate column widths based on content
            num_cols = len(headers)
            available_width = self.w - 50  # margins + padding
            
            # Get max content width per column
            col_max_lens = []
            for i in range(num_cols):
                max_len = len(clean_cell_text(headers[i]))
                for row in rows:
                    if i < len(row):
                        max_len = max(max_len, len(clean_cell_text(row[i])))
                col_max_lens.append(max_len)
            
            total_chars = sum(col_max_lens) or 1
            col_widths = [(l / total_chars) * available_width for l in col_max_lens]
            
            # Ensure minimum width
            min_width = 15
            col_widths = [max(w, min_width) for w in col_widths]
            
            # Scale down if too wide
            total_width = sum(col_widths)
            if total_width > available_width:
                scale = available_width / total_width
                col_widths = [w * scale for w in col_widths]
            
            # Header row
            self.set_fill_color(240, 240, 240)
            for i, header in enumerate(headers):
                self.cell(col_widths[i], 8, clean_cell_text(header), border=1, fill=True, align='C')
            self.ln()
            
            # Data rows
            self.set_font('Times', '', 8)
            for row in rows:
                for i, cell in enumerate(row):
                    if i < len(col_widths):
                        self.cell(col_widths[i], 7, clean_cell_text(cell), border=1, align='C')
                self.ln()
            self.ln(4)
    
    # Read markdown
    content = md_file.read_text(encoding='utf-8')
    
    # Parse and convert
    pdf = AcademicPDF()
    pdf.add_page()
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        pdf.set_font('Helvetica', 'B', 18)
        title_text = sanitize_text(clean_markdown_links(title_match.group(1)))
        pdf.multi_cell(0, 10, title_text, align='C')
        pdf.ln(8)
    
    # Process content
    lines = content.split('\n')
    in_table = False
    table_headers = []
    table_rows = []
    in_code_block = False
    
    for line in lines:
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            if in_table and table_headers:
                pdf.add_table(table_headers, table_rows)
                table_headers = []
                table_rows = []
                in_table = False
            continue
            
        # Code blocks
        if line_stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        # Headers
        if line_stripped.startswith('# ') and not title_match:
            pdf.chapter_title(line_stripped[2:], 1)
        elif line_stripped.startswith('## '):
            pdf.chapter_title(line_stripped[3:], 1)
        elif line_stripped.startswith('### '):
            pdf.chapter_title(line_stripped[4:], 2)
        elif line_stripped.startswith('#### '):
            pdf.chapter_title(line_stripped[5:], 3)
            
        # Critical findings
        elif '**Critical Finding**' in line_stripped or '**CRITICAL FINDING**' in line_stripped:
            text = re.sub(r'\*\*Critical Finding[:\s]*\*\*', '', line_stripped, flags=re.IGNORECASE)
            text = re.sub(r'\*\*', '', text)
            pdf.critical_finding(text.strip())
            
        # Tables
        elif '|' in line_stripped:
            cells = [c.strip() for c in line_stripped.split('|')[1:-1]]
            if cells:
                if all(set(c) <= {'-', ':', ' '} for c in cells):
                    continue  # Skip separator line
                elif not table_headers:
                    table_headers = cells
                    in_table = True
                else:
                    table_rows.append(cells)
                    
        # Bold text (findings)
        elif line_stripped.startswith('**') and line_stripped.endswith('**'):
            pdf.set_font('Times', 'B', 11)
            pdf.multi_cell(0, 6, sanitize_text(clean_markdown_links(line_stripped.strip('*'))))
            pdf.ln(2)
            
        # Bullet points
        elif line_stripped.startswith('- ') or line_stripped.startswith('* '):
            text = line_stripped[2:]
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # Bold
            text = re.sub(r'\*(.+?)\*', r'\1', text)  # Italic
            text = clean_markdown_links(text)
            text = re.sub(r'`([^`]+)`', r'\1', text)  # Code
            pdf.set_font('Times', '', 11)
            pdf.multi_cell(0, 6, f"   * {sanitize_text(text)}")
            pdf.ln(1)
            
        # Numbered lists
        elif re.match(r'^\d+\.\s', line_stripped):
            num_match = re.match(r'^(\d+)\.\s*', line_stripped)
            num = num_match.group(1) if num_match else ''
            text = re.sub(r'^\d+\.\s*', '', line_stripped)
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = clean_markdown_links(text)
            pdf.set_font('Times', '', 11)
            pdf.multi_cell(0, 6, f"   {num}. {sanitize_text(text)}")
            pdf.ln(1)
            
        # Regular paragraphs
        elif not line_stripped.startswith('---'):
            # Clean up markdown formatting
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', line_stripped)  # Bold
            text = re.sub(r'\*(.+?)\*', r'\1', text)  # Italic
            text = clean_markdown_links(text)
            text = re.sub(r'`([^`]+)`', r'\1', text)  # Code
            if text:
                pdf.body_text(text)
    
    # Final table if pending
    if table_headers:
        pdf.add_table(table_headers, table_rows)
    
    # Output
    output_file = output_dir / f"{md_file.stem}.pdf"
    pdf.output(str(output_file))
    return output_file


def main():
    """Build PDFs from markdown reports in a directory."""
    parser = argparse.ArgumentParser(description='Convert markdown reports to PDF')
    parser.add_argument('reports_dir', nargs='?', default='../projects/nde/reports',
                        help='Directory containing markdown reports')
    parser.add_argument('--force-fpdf', action='store_true',
                        help='Force use of fpdf2 even if pdflatex is available')
    args = parser.parse_args()
    
    # Resolve paths
    script_dir = Path(__file__).parent
    reports_dir = Path(args.reports_dir)
    if not reports_dir.is_absolute():
        reports_dir = (script_dir / reports_dir).resolve()
    
    if not reports_dir.exists():
        print(f"Error: Reports directory not found: {reports_dir}")
        sys.exit(1)
    
    # Output PDFs to same directory as markdown files
    output_dir = reports_dir
    
    # Check for LaTeX source files
    latex_dir = reports_dir / 'latex'
    tex_files = list(latex_dir.glob('*.tex')) if latex_dir.exists() else []
    tex_files = [f for f in tex_files if not f.name.startswith('nde-report-preamble')]
    
    # Find markdown reports (exclude README, etc.)
    md_files = [f for f in reports_dir.glob('*.md') 
                if not f.name.lower().startswith('readme')]
    
    print(f"Found {len(md_files)} markdown reports in {reports_dir}")
    if tex_files:
        print(f"Found {len(tex_files)} LaTeX source files in {latex_dir}")
    
    # Use pdflatex if available and LaTeX files exist
    if PDFLATEX and tex_files and not args.force_fpdf:
        print(f"Using pdflatex: {PDFLATEX}")
        print("  (Professional output with clickable links and proper typography)")
        
        for tex_file in tex_files:
            print(f"Compiling {tex_file.name}...")
            try:
                output = compile_latex(tex_file, output_dir)
                print(f"  -> {output.name}")
            except Exception as e:
                print(f"  X Failed: {e}")
    else:
        # Fall back to fpdf2
        if not md_files:
            print("No markdown files found.")
            sys.exit(0)
            
        if PDFLATEX and not tex_files:
            print("pdflatex available but no LaTeX source files found.")
            print("Using fpdf2 to convert markdown directly.")
        elif args.force_fpdf:
            print("Using fpdf2 (--force-fpdf specified)")
        else:
            print("pdflatex not found, using fpdf2")
        
        # Ensure fpdf2 is installed
        try:
            from fpdf import FPDF
        except ImportError:
            print("Installing fpdf2...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'fpdf2'], check=True)
        
        # Convert each file
        for md_file in md_files:
            print(f"Converting {md_file.name}...")
            try:
                output = markdown_to_pdf_fpdf(md_file, output_dir)
                print(f"  -> {output.name}")
            except Exception as e:
                print(f"  X Failed: {e}")
                import traceback
                traceback.print_exc()


if __name__ == '__main__':
    main()
