"""Analyze PMC scrape results."""
import json
from pathlib import Path

cases = list(Path('data/pmc_cases/pmc').glob('*.json'))
print(f'Total cases: {len(cases)}')

# Check content lengths
lengths = []
for f in cases:
    with open(f, encoding='utf-8') as fp:
        case = json.load(fp)
    lengths.append(len(case.get('content', '')))

print(f'Content lengths:')
print(f'  Min: {min(lengths):,} chars')
print(f'  Max: {max(lengths):,} chars')  
print(f'  Avg: {sum(lengths)//len(lengths):,} chars')
print(f'  Total: {sum(lengths):,} chars')

# Count by content type  
with_pdf = 0
for f in cases:
    with open(f, encoding='utf-8') as fp:
        case = json.load(fp)
    if case.get('metadata', {}).get('pdf_path'):
        with_pdf += 1

print(f'\nWith PDF: {with_pdf}/{len(cases)}')

# Check PDFs on disk
pdf_dir = Path('data/pmc_cases/pmc/pdfs')
if pdf_dir.exists():
    pdfs = list(pdf_dir.glob('*.pdf'))
    total_pdf_size = sum(p.stat().st_size for p in pdfs)
    print(f'PDFs on disk: {len(pdfs)} files, {total_pdf_size/1024/1024:.1f} MB')

# Show sample
print('\nSample cases:')
for f in list(cases)[:5]:
    with open(f, encoding='utf-8') as fp:
        case = json.load(fp)
    content_len = len(case['content'])
    has_pdf = '✓' if case.get('metadata', {}).get('pdf_path') else '✗'
    title = case['title'][:55]
    print(f'  [{content_len:>6,} chars] [PDF:{has_pdf}] {title}...')
