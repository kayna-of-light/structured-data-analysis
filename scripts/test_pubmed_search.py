"""Test PubMed search to debug IONS scraper."""
import requests
from urllib.parse import urlencode

# Try several search strategies
searches = [
    # Strategy 1: Full title (current - failing)
    '"The spontaneous regression of cancer. A review of cases from 1900 to 1987"[Title]',
    # Strategy 2: Simpler title match without period
    'spontaneous regression cancer review[Title] AND Challis[Author]',
    # Strategy 3: Author + year + keywords
    'Challis[Author] AND spontaneous regression[Title] AND 1990[pdat]',
    # Strategy 4: Just keywords and author
    'spontaneous regression cancer[Title] AND Challis[Author]',
]

for query in searches:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": "5",
        "rettype": "xml",
    }
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{urlencode(params)}"
    
    resp = requests.get(url)
    
    # Check for IDs
    import re
    ids = re.findall(r"<Id>(\d+)</Id>", resp.text)
    print(f"Found PMIDs: {ids}")

