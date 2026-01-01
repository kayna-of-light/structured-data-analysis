import re

texts = [
    'Joachime DEHANTBorn in 1849 in Velaine/s/SambreLived in Gesves',
    'Elisa SEISSONBorn in1855Cured on 29.8.1882',
    'Pierre de RUDDERBorn on 7/2/1822 in Jabbeke',
    'Mrs Catherine LATAPIEBorn in 1820Lived in Loubajac',
]

# Current full_match pattern from the scraper
full_pattern = r"^(?:Mrs?\.?\s+|Sister\s+)?([A-Z][a-zA-Z\-\'\s]+?)(?:nee\s+[A-Z]+,?\s*)?(?:,?\s*[Bb]orn|,?\s*[Ll]ived|,?\s*[Cc]ured)"

print("Testing full_match pattern:")
for text in texts:
    m = re.match(full_pattern, text)
    if m:
        print(f"  MATCH: {text[:50]}... -> name={repr(m.group(1))}")
    else:
        print(f"  NO MATCH: {text[:50]}...")
