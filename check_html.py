import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles3.html'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'lxml')

# Get all paragraphs
paragraphs = soup.find_all('p')
print(f'Total paragraphs: {len(paragraphs)}')

# Find ones with Virginie or Marie or BOREL (case insensitive)
for i, p in enumerate(paragraphs):
    text = p.get_text(strip=True).lower()
    if 'virginie' in text or 'borel' in text or 'haudebourg' in text:
        orig = p.get_text(strip=True)
        print(f'=== P{i} ===')
        print(f'Length: {len(orig)}')
        print(f'Text: {orig[:400]}')
        print()
