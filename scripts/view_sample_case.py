"""View a sample PMC case report."""
import json
from pathlib import Path

# Find a good case with full text
for f in Path('data/test_output/pmc').glob('*.json'):
    with open(f) as fp:
        case = json.load(fp)
    if case['metadata'].get('content_type') == 'full_text_with_pdf':
        print(f"Title: {case['title']}")
        print(f"Journal: {case['metadata']['journal']}")
        authors = case['metadata']['authors'][:3]
        print(f"Authors: {', '.join(authors)}...")
        print(f"Content length: {len(case['content']):,} chars")
        print(f"PDF: {case['metadata'].get('pdf_path', 'N/A')}")
        print()
        print('=== CONTENT PREVIEW (first 3000 chars) ===')
        print(case['content'][:3000])
        break
