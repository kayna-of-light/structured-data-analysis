"""Check Lourdes case content."""
import json
from pathlib import Path

files = sorted(Path('data/lourdes_cases/lourdes').glob('*.json'))

# Find shortest cases
cases = []
for f in files:
    with open(f, encoding='utf-8') as fp:
        case = json.load(fp)
    cases.append((len(case.get('content', '')), f.name, case))

cases.sort(key=lambda x: x[0])

print('SHORTEST LOURDES CASES:')
for length, name, case in cases[:5]:
    print(f'\n[{length} chars] {name}')
    print(f"Title: {case['title']}")
    content = case['content']
    print(f"Content: {content[:200]}..." if len(content) > 200 else f"Content: {content}")

print('\n' + '='*60)
print('LONGEST LOURDES CASES:')
for length, name, case in cases[-3:]:
    print(f'\n[{length} chars] {name}')
    print(f"Title: {case['title']}")
    print(f"Content preview: {case['content'][:400]}...")
