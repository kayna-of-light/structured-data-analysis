"""Test targeted PMC search for actual case reports."""
import requests
import time
from xml.etree import ElementTree as ET

ESEARCH_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
EFETCH_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

# More targeted searches
searches = [
    ('Title has spontaneous regression', '"spontaneous regression"[Title]'),
    ('Title has spontaneous remission', '"spontaneous remission"[Title]'),
    ('Case Reports pub type', '("spontaneous remission" OR "spontaneous regression") AND cancer AND "Case Reports"[Publication Type]'),
]

print('Targeted PubMed Searches:')
print('=' * 70)

for name, query in searches:
    params = {'db': 'pubmed', 'term': query, 'retmax': 0, 'retmode': 'json'}
    resp = requests.get(ESEARCH_URL, params=params)
    count = resp.json().get('esearchresult', {}).get('count', 0)
    print(f'{count:>5} - {name}')
    time.sleep(0.34)

# Best query - title contains our terms
best_query = '("spontaneous regression"[Title] OR "spontaneous remission"[Title]) AND (cancer OR tumor OR carcinoma OR melanoma OR lymphoma)'
params = {'db': 'pubmed', 'term': best_query, 'retmax': 0, 'retmode': 'json'}
resp = requests.get(ESEARCH_URL, params=params)
count = resp.json().get('esearchresult', {}).get('count', 0)
print(f'\n{count:>5} - BEST: Title contains term + cancer-related')

# Fetch sample
print('\n\nSample articles (title contains "spontaneous regression/remission"):')
print('=' * 70)
params = {'db': 'pubmed', 'term': best_query, 'retmax': 25, 'retmode': 'json'}
resp = requests.get(ESEARCH_URL, params=params)
ids = resp.json().get('esearchresult', {}).get('idlist', [])

time.sleep(0.34)
params = {'db': 'pubmed', 'id': ','.join(ids), 'retmode': 'xml'}
resp = requests.get(EFETCH_URL, params=params)
root = ET.fromstring(resp.content)

for i, article in enumerate(root.findall('.//PubmedArticle'), 1):
    title = article.findtext('.//ArticleTitle') or 'No title'
    year = article.findtext('.//PubDate/Year') or article.findtext('.//PubDate/MedlineDate') or '?'
    pmid = article.findtext('.//PMID') or '?'
    # Check for PMC ID
    pmc = article.findtext('.//ArticleId[@IdType="pmc"]') or ''
    pmc_marker = ' [PMC]' if pmc else ''
    print(f'{i:2}. [{year}] {title[:70]}{pmc_marker}')
