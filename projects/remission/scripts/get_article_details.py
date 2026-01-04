"""Get details of an OA article."""
import requests
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

def get_element_text(elem):
    """Get all text from element including children."""
    if elem is None:
        return "N/A"
    text_parts = []
    if elem.text:
        text_parts.append(elem.text)
    for child in elem:
        text_parts.append(get_element_text(child))
        if child.tail:
            text_parts.append(child.tail)
    return "".join(text_parts).strip()

for pmcid in ['6221684', '8271173']:
    print(f"\n=== PMC{pmcid} ===")
    efetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    params = {
        'db': 'pmc',
        'id': pmcid,
        'rettype': 'xml',
    }
    resp = requests.get(f'{efetch_url}?{urlencode(params)}', timeout=30)

    root = ET.fromstring(resp.content)

    title = root.find('.//article-title')
    print('Title:', get_element_text(title))

    authors = root.findall('.//contrib[@contrib-type="author"]//surname')
    print('Authors:', [a.text for a in authors[:3]])

    journal = root.find('.//journal-title')
    print('Journal:', get_element_text(journal))

    year = root.find('.//pub-date/year')
    print('Year:', year.text if year is not None else 'N/A')

    pmid_elem = root.find('.//article-id[@pub-id-type="pmid"]')
    print('PMID:', pmid_elem.text if pmid_elem is not None else 'N/A')
