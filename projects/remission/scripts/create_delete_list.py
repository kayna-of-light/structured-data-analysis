"""Create final list of PMC files to delete (confirmed non-human or non-case-study)."""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PMC_DIR = ROOT / "data" / "pmc_cases" / "pmc"

# CONFIRMED ANIMAL/LAB STUDIES (not human case reports)
ANIMAL_STUDIES = [
    "pmc11035550.json",  # minipig melanomas
    "pmc12123822.json",  # mouse neuroblastoma model (despite having human-like terms)
    "pmc2071283.json",   # mammary tumours in RATS
    "pmc2131164.json",   # tuberculosis in RABBITS
    "pmc2180720.json",   # murine leukemia virus
    "pmc3290113.json",   # MURINE ovarian cancer cells / nude mice
    "pmc4402496.json",   # Apc-knockout MOUSE models
    "pmc7646068.json",   # MDA-MB-231HM human breast cancer cells (lab study)
]

# DOG/CAT case studies - NOT HUMAN but may be interesting for comparison
# Keeping separately tagged
DOG_CAT_STUDIES = [
    "pmc6612484.json",   # DOG with canine papillomavirus
    "pmc6833175.json",   # DOG with extradural intraspinal cysts
    "pmc9643767.json",   # CAT with minimal change disease
]

# NON-CASE STUDIES (reviews, trials, meta-analyses, multi-patient studies)
NON_CASE_STUDIES = [
    "pmc11135932.json",  # Systematic review using immunohistochemistry
    "pmc11303966.json",  # 31 patients observational
    "pmc3523032.json",   # HPV study cohort
    "pmc5467065.json",   # Mini-review
    "pmc8439357.json",   # 5-year retrospective China
    "pmc8990007.json",   # Systematic review and pooled analysis
    "pmc8271173.json",   # Review article - therapeutic significance
    "pmc7409640.json",   # Review of literature (is actually a case report - keep)
]

# Actually "pmc7409640.json" IS a case report with review - KEEP IT
NON_CASE_STUDIES.remove("pmc7409640.json")

# Files that were flagged but are VALID human case studies - DO NOT DELETE
VALID_HUMAN_CASES = [
    "pmc10828767.json",  # SAMD9L syndrome in children
    "pmc12306882.json",  # cutaneous epithelioid after biopsy - 27yo female
    "pmc2010094.json",   # human AML xenografts (talks about human cells)
    "pmc2703639.json",   # alveolar soft part sarcoma - adult male patient
    "pmc2760877.json",   # neuroblastoma clinical outcomes
    "pmc2974747.json",   # congenital epulis - newborn child
    "pmc3618050.json",   # Cronkhite-Canada syndrome patient
    "pmc4641483.json",   # three cases AML M5 - human patients
    "pmc4890101.json",   # Merkel cell carcinoma - 58yo man
    "pmc6082924.json",   # Paroxysmal Nocturnal Hemoglobinuria - human
    "pmc6954166.json",   # B-cell lymphoma patients
    "pmc6963339.json",   # Pancreatic tumor - 82yo female
    "pmc7409640.json",   # ALK fusion NSCLC - 76 year old (VALID case report)
]

# Multi-patient that might still have value - review individually
BORDERLINE = [
    "pmc11900398.json",  # Cervical lesions Thai population study
    "pmc12686737.json",  # Cervical lesions Dijon study
    "pmc4082862.json",   # Prediction cervical neoplasia
    "pmc5640371.json",   # Lymphangiomas single center 34 years
    "pmc9578209.json",   # Cervical neoplasia biopsy interval
]

# FINAL DELETE LIST
DELETE_FILES = ANIMAL_STUDIES + DOG_CAT_STUDIES + NON_CASE_STUDIES

print("="*60)
print("FINAL DELETE LIST")
print("="*60)
print(f"Animal/Lab studies: {len(ANIMAL_STUDIES)}")
print(f"Dog/Cat studies: {len(DOG_CAT_STUDIES)}")
print(f"Non-case studies: {len(NON_CASE_STUDIES)}")
print(f"TOTAL TO DELETE: {len(DELETE_FILES)}")
print()

for f in DELETE_FILES:
    path = PMC_DIR / f
    if path.exists():
        data = json.load(open(path, encoding='utf-8'))
        print(f"  {f}")
        print(f"    → {data.get('title', 'NO TITLE')[:80]}")
    else:
        print(f"  {f} - NOT FOUND")

# Write the delete list
output = ROOT / "output" / "pmc_delete_final.txt"
output.parent.mkdir(exist_ok=True)
output.write_text("\n".join(DELETE_FILES))
print()
print(f"Delete list written to: {output}")
