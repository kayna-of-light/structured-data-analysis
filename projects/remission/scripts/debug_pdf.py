"""Debug PDF download from PMC using OA API."""
import requests
import xml.etree.ElementTree as ET

pmcid = 'PMC3192512'

# OA API endpoint
oa_url = f'https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmcid}'
print(f'OA API URL: {oa_url}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

resp = requests.get(oa_url, timeout=30, headers=headers)
print(f'Status: {resp.status_code}')
print(f'\nFull Response:\n{resp.text}\n')

# Parse XML to find PDF link
root = ET.fromstring(resp.content)
for record in root.findall('.//record'):
    print(f'\nRecord:')
    for link in record.findall('.//link'):
        format_type = link.get('format', '')
        href = link.get('href', '')
        print(f'  Format: {format_type}')
        print(f'  URL: {href}')
        
        if format_type == 'pdf':
            # Convert FTP URL to HTTPS
            if href.startswith('ftp://ftp.ncbi.nlm.nih.gov/'):
                href = href.replace('ftp://ftp.ncbi.nlm.nih.gov/', 'https://ftp.ncbi.nlm.nih.gov/')
            print(f'  HTTP URL: {href}')
            
            print(f'\n  Trying PDF download...')
            pdf_resp = requests.get(href, timeout=60, headers=headers)
            print(f'  PDF Status: {pdf_resp.status_code}')
            is_pdf = pdf_resp.content[:4] == b'%PDF'
            print(f'  Is PDF: {is_pdf}')
            print(f'  Size: {len(pdf_resp.content)} bytes')
            if is_pdf:
                print('  SUCCESS!')
