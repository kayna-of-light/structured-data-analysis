"""Find open access articles for testing."""
import requests
from urllib.parse import urlencode

# Simpler search
search_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
params = {
    'db': 'pmc',
    'term': '(spontaneous regression OR spontaneous remission) cancer',
    'retmax': '10',
    'retmode': 'json',
    'sort': 'relevance'
}
resp = requests.get(f'{search_url}?{urlencode(params)}', timeout=30)
import json
data = resp.json()
ids = data.get('esearchresult', {}).get('idlist', [])
print('Found PMC IDs:', ids[:5])

# Check which are OA
for pmc_id in ids[:5]:
    pmcid = f'PMC{pmc_id}'
    oa_url = f'https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmcid}'
    oa_resp = requests.get(oa_url, timeout=30)
    has_pdf = 'format="pdf"' in oa_resp.text
    print(f'{pmcid}: OA PDF available = {has_pdf}')
