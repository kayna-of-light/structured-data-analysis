"""Review animal-flagged files to see which are actually human case studies."""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PMC_DIR = ROOT / "data" / "pmc_cases" / "pmc"

# Files flagged as animal studies - manually review content
flagged = [
    "pmc10828767.json",  # SAMD9L young children
    "pmc11035550.json",  # minipig melanomas
    "pmc12123822.json",  # neuroblastoma differentiation 
    "pmc12306882.json",  # cutaneous epithelioid - biopsy
    "pmc2010094.json",   # leukaemia xenografts
    "pmc2071283.json",   # mammary tumours in rats
    "pmc2131164.json",   # tuberculosis in rabbits
    "pmc2180720.json",   # murine leukemia
    "pmc2703639.json",   # alveolar soft part sarcoma - case report
    "pmc2760877.json",   # MYCN/c-MYC neuroblastoma
    "pmc2974747.json",   # congenital epulis - case report  
    "pmc3290113.json",   # ovarian tumors carbonyl reductase
    "pmc3618050.json",   # polyposis abdominal colectomy
    "pmc4402496.json",   # microadenomas tracing
    "pmc4641483.json",   # three cases AML M5
    "pmc4890101.json",   # Merkel cell carcinoma lifestyle
    "pmc6082924.json",   # Paroxysmal Nocturnal Hemoglobinuria
    "pmc6612484.json",   # canine papillomavirus - DOG
    "pmc6833175.json",   # extradural cysts - DOG
    "pmc6954166.json",   # B-cell lymphoma mechanisms
    "pmc6963339.json",   # pancreatic inflammatory
    "pmc7409640.json",   # ALK fusion lung carcinoma
    "pmc7646068.json",   # micro-metastases excision
    "pmc8271173.json",   # cancer insights therapeutic
    "pmc9643767.json",   # minimal change disease - CAT
]

for fname in flagged:
    f = PMC_DIR / fname
    if not f.exists():
        print(f"NOT FOUND: {fname}")
        continue
    
    data = json.load(open(f, encoding='utf-8'))
    title = data.get('title', '')
    content = data.get('content', '')[:800]
    
    # Check for definitive animal keywords
    content_lower = (title + content).lower()
    is_animal = any(x in content_lower for x in ['dog', 'cat', 'rabbit', 'rat', 'mice', 'mouse', 'minipig', 'canine', 'feline', 'xenograft'])
    human_indicators = any(x in content_lower for x in ['patient', 'year-old', 'she was', 'he was', 'woman', 'man', 'child'])
    
    status = "ANIMAL" if is_animal and not human_indicators else "HUMAN" if human_indicators else "UNCLEAR"
    
    print(f"\n{'='*60}")
    print(f"FILE: {fname}")
    print(f"STATUS: {status}")
    print(f"TITLE: {title}")
    print(f"SNIPPET: {content[:400]}...")
