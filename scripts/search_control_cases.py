"""Search for potential comparison/control case reports."""
import requests
import time

ESEARCH_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

searches = [
    # Progression / failure cases
    ('"rapid progression" cancer "case report"', 'Rapid progression'),
    ('"treatment failure" cancer "case report"', 'Treatment failure'),
    ('"disease progression" cancer "case report"', 'Disease progression'),
    ('"tumor progression"[Title]', 'Tumor progression in title'),
    ('"cancer progression"[Title]', 'Cancer progression in title'),
    
    # Fatal outcomes
    ('"fatal outcome" cancer "case report"', 'Fatal outcome'),
    ('"terminal cancer" "case report"', 'Terminal cancer'),
    
    # Refractory (doesn't respond to treatment)
    ('"refractory" cancer "case report"', 'Refractory cancer'),
    
    # Recurrence after treatment
    ('"cancer recurrence"[Title] "case report"', 'Recurrence in title'),
    
    # Unexpected death
    ('"unexpected death" cancer', 'Unexpected death'),
]

print('Searching for comparison/control case types:')
print('=' * 70)

for query, name in searches:
    params = {'db': 'pmc', 'term': query, 'retmax': 0, 'retmode': 'json'}
    resp = requests.get(ESEARCH_URL, params=params)
    count = resp.json().get('esearchresult', {}).get('count', 0)
    print(f'{count:>6} - {name}')
    time.sleep(0.34)

# The issue: "didn't remit" isn't newsworthy - it's the default
print('\n' + '=' * 70)
print('NOTE: The challenge is that "normal progression" is not case-report-worthy.')
print('Case reports document UNUSUAL outcomes, and dying from cancer is sadly typical.')
print('\nPossible alternatives:')
print('1. Case series that include responders AND non-responders')
print('2. Clinical trial data with both outcomes')
print('3. Registry data (SEER, etc.)')
