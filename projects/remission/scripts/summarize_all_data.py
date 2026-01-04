"""Analyze all scraped data."""
import json
from pathlib import Path

def analyze_dataset(name, path_pattern):
    files = list(Path().glob(path_pattern))
    if not files:
        print(f"{name}: NO FILES FOUND at {path_pattern}")
        return 0
    
    lengths = []
    for f in files:
        with open(f, encoding='utf-8') as fp:
            case = json.load(fp)
        lengths.append(len(case.get('content', '')))
    
    print(f"{name}:")
    print(f"  Files: {len(files)}")
    print(f"  Content: {min(lengths):,} - {max(lengths):,} chars")
    print(f"  Average: {sum(lengths)//len(lengths):,} chars")
    print(f"  Total: {sum(lengths):,} chars")
    return len(files)

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

total = 0
total += analyze_dataset("PMC Case Reports", "../../data/pmc/pmc/*.json")
print()
total += analyze_dataset("Radical Remission", "../../data/radical_remission/radical_remission/*.json")

print()
print("=" * 60)
print(f"TOTAL CASES: {total}")
print("=" * 60)
