"""Scan data files to identify animal studies and non-case-study content."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_ROOT = ROOT / "data"

# Animal indicators in title or content
ANIMAL_PATTERNS = [
    r'\brabbits?\b', r'\bmice\b', r'\bmouse\b', r'\brats?\b', r'\bmurine\b',
    r'\bcanine\b', r'\bdogs?\b', r'\bfeline\b', r'\bcats?\b', r'\bporcine\b',
    r'\bpigs?\b', r'\bovine\b', r'\bcattle\b', r'\bsheep\b', r'\bgoats?\b',
    r'\bmonkeys?\b', r'\bprimates?\b', r'\bhamsters?\b', r'\bguinea pigs?\b',
    r'\bxenograft\b', r'\btumor model\b', r'\banimal model\b', 
    r'\bexperimental model\b', r'\binoculation\b', r'\binoculated\b',
]
ANIMAL_REGEX = re.compile('|'.join(ANIMAL_PATTERNS), re.IGNORECASE)

# In vitro / lab study indicators (check TITLE only - content will have these in valid cases)
LAB_PATTERNS = [
    r'\bin vitro\b', r'\bcell line[s]?\b', r'\bcell culture\b', 
    r'\bcultured cells\b', r'\bHeLa\b', r'\bMCF-7\b', r'\bA549\b',
]
LAB_REGEX = re.compile('|'.join(LAB_PATTERNS), re.IGNORECASE)

# Non-case-study indicators (check title ONLY - these indicate the paper itself is not a case study)
# Note: "case report and literature review" is a VALID case study pattern - exclude it
NON_CASE_TITLE_PATTERNS = [
    r'^(?!.*case report).*systematic review',  # "systematic review" without "case report"
    r'^(?!.*case report).*meta-analysis',  # "meta-analysis" without "case report"
    r'\brandomized\b',
    r'\bclinical trial\b',
    r'\bcohort study\b',
    r'\bretrospective analysis\b',  
    r'\bprospective study\b',
    r'^(?!.*case report).*retrospective',  # "retrospective" without "case report"  
    r'\bpooled analysis\b',
    r'\bmini-review\b',
    r'\b\d+ patients\b',  # "X patients" where X is a number
    r'\b\d+ cases\b',  # "X cases" where X is a number
]
NON_CASE_TITLE_REGEX = re.compile('|'.join(NON_CASE_TITLE_PATTERNS), re.IGNORECASE)

# Multi-patient study indicators in content
MULTI_PATIENT_PATTERNS = [
    r'\bpatients were enrolled\b', r'\b(\d{2,}) patients\b', 
    r'\bseries of \d+\b', r'\bwe enrolled\b', r'\bparticipants\b',
    r'\bsubjects were\b', r'\bcases were reviewed\b',
]
MULTI_PATIENT_REGEX = re.compile('|'.join(MULTI_PATIENT_PATTERNS), re.IGNORECASE)


def scan_pmc_data():
    """Scan PMC data for quality issues."""
    pmc_dir = DATA_ROOT / "pmc_cases" / "pmc"
    if not pmc_dir.exists():
        print("PMC directory not found")
        return
    
    animal_files = []
    lab_files = []
    non_case_files = []
    multi_patient_files = []
    valid_cases = []
    
    all_files = list(pmc_dir.glob("*.json"))
    
    for f in all_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            title = data.get("title", "")
            content = data.get("content", "")[:5000]  # Check first 5000 chars
            
            # Check for animal studies (title + content)
            if ANIMAL_REGEX.search(title) or ANIMAL_REGEX.search(content):
                animal_files.append((f.name, title[:100]))
                continue
            
            # Check for in vitro / lab studies (TITLE ONLY - not content)
            if LAB_REGEX.search(title):
                lab_files.append((f.name, title[:100]))
                continue
            
            # Check for reviews/trials in title
            if NON_CASE_TITLE_REGEX.search(title):
                non_case_files.append((f.name, title[:100]))
                continue
            
            # Check for multi-patient studies
            if MULTI_PATIENT_REGEX.search(content):
                multi_patient_files.append((f.name, title[:100]))
                continue
            
            valid_cases.append((f.name, title[:100]))
            
        except Exception as e:
            print(f"Error reading {f.name}: {e}")
    
    print("=" * 70)
    print("PMC DATA QUALITY SCAN")
    print("=" * 70)
    print(f"Total PMC files: {len(all_files)}")
    print(f"Animal studies: {len(animal_files)}")
    print(f"In vitro / lab studies: {len(lab_files)}")
    print(f"Non-case studies (reviews/trials): {len(non_case_files)}")
    print(f"Multi-patient studies: {len(multi_patient_files)}")
    print(f"Potentially valid single-case studies: {len(valid_cases)}")
    print()
    
    to_delete = animal_files + lab_files + non_case_files + multi_patient_files
    print(f"TOTAL TO DELETE: {len(to_delete)}")
    print()
    
    print("=" * 70)
    print(f"ANIMAL STUDIES ({len(animal_files)})")
    print("=" * 70)
    for name, title in animal_files:
        print(f"  {name}")
        print(f"    {title}")
    print()
    
    print("=" * 70)
    print(f"IN VITRO / LAB STUDIES ({len(lab_files)})")
    print("=" * 70)
    for name, title in lab_files:
        print(f"  {name}")
        print(f"    {title}")
    print()
    
    print("=" * 70)
    print(f"NON-CASE STUDIES ({len(non_case_files)})")
    print("=" * 70)
    for name, title in non_case_files:
        print(f"  {name}")
        print(f"    {title}")
    print()
    
    print("=" * 70)
    print(f"MULTI-PATIENT STUDIES ({len(multi_patient_files)})")
    print("=" * 70)
    for name, title in multi_patient_files[:30]:
        print(f"  {name}")
        print(f"    {title}")
    if len(multi_patient_files) > 30:
        print(f"  ... and {len(multi_patient_files) - 30} more")
    print()
    
    print("=" * 70)
    print(f"VALID CASES SAMPLE ({len(valid_cases)} total)")
    print("=" * 70)
    for name, title in valid_cases[:20]:
        print(f"  {name}")
        print(f"    {title}")
    
    # Return files to delete
    return [name for name, _ in to_delete]


def scan_other_datasets():
    """Scan RRP, NDERF, IANDS - these should all be human cases."""
    for dataset in ["rrp_cases/radical_remission", "nderf", "iands"]:
        ds_path = DATA_ROOT / dataset
        if not ds_path.exists():
            continue
        
        files = list(ds_path.glob("*.json"))
        animal_count = 0
        
        for f in files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                title = data.get("title", "")
                content = data.get("content", "")[:3000]
                
                if ANIMAL_REGEX.search(title) or ANIMAL_REGEX.search(content):
                    animal_count += 1
                    print(f"WARNING: Possible animal content in {dataset}/{f.name}")
                    print(f"  Title: {title[:80]}")
            except Exception as e:
                pass
        
        print(f"{dataset}: {len(files)} files, {animal_count} possible animal studies")


if __name__ == "__main__":
    to_delete = scan_pmc_data()
    print()
    print("=" * 70)
    print("OTHER DATASETS CHECK")
    print("=" * 70)
    scan_other_datasets()
    
    # Write delete list to file
    if to_delete:
        delete_file = ROOT / "output" / "pmc_files_to_delete.txt"
        delete_file.parent.mkdir(parents=True, exist_ok=True)
        delete_file.write_text("\n".join(to_delete))
        print()
        print(f"Delete list written to: {delete_file}")
