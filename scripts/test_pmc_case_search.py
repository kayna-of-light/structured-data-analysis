"""Test PMC search for case reports on spontaneous remission."""
import requests
import time

ESEARCH_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

searches = [
    '"spontaneous remission" cancer "case report"',
    '"spontaneous regression" cancer "case report"',
    '"spontaneous remission" tumor "case report"',
    '"spontaneous regression" tumor "case report"',
    '"spontaneous remission"[Title] cancer',
    '"spontaneous regression"[Title] cancer',
]

print('PMC Case Report Search Results:')
print('=' * 60)

for query in searches:
    params = {
        'db': 'pmc',
        'term': query,
        'retmax': 0,
        'retmode': 'json'
    }
    resp = requests.get(ESEARCH_URL, params=params)
    data = resp.json()
    count = data.get('esearchresult', {}).get('count', 0)
    print(f'{count:>5} results: {query}')
    time.sleep(0.34)

# Try a combined search
combined = '("spontaneous remission" OR "spontaneous regression") AND (cancer OR tumor OR tumour OR carcinoma OR melanoma OR lymphoma OR leukemia) AND "case report"'
params = {
    'db': 'pmc',
    'term': combined,
    'retmax': 0,
    'retmode': 'json'
}
resp = requests.get(ESEARCH_URL, params=params)
data = resp.json()
count = data.get('esearchresult', {}).get('count', 0)
print(f'\n{count:>5} results: COMBINED search')

# Also try PubMed (larger database)
print('\n\nPubMed Search Results:')
print('=' * 60)

for query in searches[:2]:  # Just test a couple
    params = {
        'db': 'pubmed',
        'term': query,
        'retmax': 0,
        'retmode': 'json'
    }
    resp = requests.get(ESEARCH_URL, params=params)
    data = resp.json()
    count = data.get('esearchresult', {}).get('count', 0)
    print(f'{count:>5} results: {query}')
    time.sleep(0.34)

# PubMed combined
params = {
    'db': 'pubmed',
    'term': combined,
    'retmax': 0,
    'retmode': 'json'
}
resp = requests.get(ESEARCH_URL, params=params)
data = resp.json()
count = data.get('esearchresult', {}).get('count', 0)
print(f'\n{count:>5} results: COMBINED search (PubMed)')

# Let's also check what types of articles we'd get
print('\n\nSample titles from combined PMC search:')
print('=' * 60)
params = {
    'db': 'pmc',
    'term': combined,
    'retmax': 20,
    'retmode': 'json'
}
resp = requests.get(ESEARCH_URL, params=params)
data = resp.json()
ids = data.get('esearchresult', {}).get('idlist', [])

if ids:
    # Fetch details
    from xml.etree import ElementTree as ET
    efetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    params = {
        'db': 'pmc',
        'id': ','.join(ids[:10]),
        'retmode': 'xml'
    }
    time.sleep(0.34)
    resp = requests.get(efetch_url, params=params)
    root = ET.fromstring(resp.content)
    
    for i, article in enumerate(root.findall('.//article'), 1):
        title_el = article.find('.//article-title')
        title = ''.join(title_el.itertext()) if title_el is not None else 'No title'
        print(f'{i:2}. {title[:80]}...' if len(title) > 80 else f'{i:2}. {title}')
