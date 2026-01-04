"""Check PMC availability for spontaneous remission case reports."""
import requests

ESEARCH_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

# Search PMC directly (full text available)
query = '("spontaneous regression"[Title] OR "spontaneous remission"[Title]) AND (cancer OR tumor OR carcinoma OR melanoma OR lymphoma OR leukemia)'

params = {'db': 'pmc', 'term': query, 'retmax': 0, 'retmode': 'json'}
resp = requests.get(ESEARCH_URL, params=params)
count = resp.json().get('esearchresult', {}).get('count', 0)
print(f'PMC (full text available): {count} articles')

# More specific - case reports only
query2 = query + ' AND "case report"'
params = {'db': 'pmc', 'term': query2, 'retmax': 0, 'retmode': 'json'}
resp = requests.get(ESEARCH_URL, params=params)
count2 = resp.json().get('esearchresult', {}).get('count', 0)
print(f'PMC case reports only: {count2} articles')

# Open access specifically
query3 = query + ' AND open access[filter]'
params = {'db': 'pmc', 'term': query3, 'retmax': 0, 'retmode': 'json'}
resp = requests.get(ESEARCH_URL, params=params)
count3 = resp.json().get('esearchresult', {}).get('count', 0)
print(f'PMC open access: {count3} articles')
