"""Analyze all scraped data using registry system."""
import json
import sys
from pathlib import Path

# Add shared to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT.parent.parent / "shared"))

from registry import load_registry


def analyze_dataset_from_registry(registry_name):
    """Analyze dataset using registry file."""
    registry_path = PROJECT_ROOT / "registries" / f"{registry_name}.yaml"
    
    if not registry_path.exists():
        print(f"Registry not found: {registry_path}")
        return 0
    
    registry = load_registry(registry_path)
    
    total_files = 0
    for dataset_name in registry.list_datasets():
        files = registry.get_files(dataset_name)
        
        if not files:
            print(f"{dataset_name} ({registry_name}): NO FILES FOUND")
            continue
        
        lengths = []
        for f in files:
            try:
                with open(f, encoding='utf-8') as fp:
                    case = json.load(fp)
                lengths.append(len(case.get('content', '')))
            except Exception as e:
                print(f"  Error reading {f.name}: {e}")
        
        if lengths:
            print(f"{dataset_name} ({registry_name}):")
            print(f"  Files: {len(files)}")
            print(f"  Content: {min(lengths):,} - {max(lengths):,} chars")
            print(f"  Average: {sum(lengths)//len(lengths):,} chars")
            print(f"  Total: {sum(lengths):,} chars")
            total_files += len(files)
    
    return total_files


print("=" * 60)
print("DATASET SUMMARY (Registry-based)")
print("=" * 60)

total = 0
total += analyze_dataset_from_registry("pmc")
print()
total += analyze_dataset_from_registry("radical_remission")
print()
# Note: NDERF and IANDS healing subsets can be added when needed
# total += analyze_dataset_from_registry("nderf")
# total += analyze_dataset_from_registry("iands")

print()
print("=" * 60)
print(f"TOTAL CASES: {total}")
print("=" * 60)
