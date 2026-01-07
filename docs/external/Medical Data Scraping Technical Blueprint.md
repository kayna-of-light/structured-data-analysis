# **Technical Architecture and Implementation Specification for the Programmatic Extraction of Spontaneous Remission Data: Biomedical, Clinical, and Forensic Sources**

## **1\. Executive Technical Overview**

The objective of this technical report is to define the architectural specifications, scraping logic, and data extraction methodologies required to aggregate disjointed medical datasets concerning Spontaneous Remission (SR). This document addresses the requirements of a software developer and data scientist tasked with building the ingestion layer of a Spontaneous Remission Database (SRD). The scope is strictly limited to medical and clinical datasets—specifically PubMed Central (PMC), the Radical Remission Project (RRP), the Lourdes Medical Bureau, and the Institute of Noetic Sciences (IONS) Bibliography—while explicitly excluding phenomenological datasets such as NDERF (Near-Death Experience Research Foundation) and DOPS (Division of Perceptual Studies).

The engineering challenge lies in the extreme heterogeneity of the source targets. The data pipeline must orchestrate the ingestion of highly structured biomedical data via standardized APIs (PMC/OAI-PMH), semi-structured dynamic content from single-page applications (RRP), static historical records stored in HTML tables (Lourdes/Miracle Hunter), and unstructured legacy archives (IONS). This report provides the granular technical details necessary to implement the scraping code, including endpoint specifications, DOM traversal strategies, XML schema parsing logic, and necessary request headers, without delving into downstream medical analysis or theological interpretation.

## **2\. The Biomedical Tier: PubMed Central (PMC) and the Open Access Subset**

The "hard" medical baseline for any SR database is derived from peer-reviewed case reports. PubMed Central (PMC) is the primary target due to its provision of full-text XML for its Open Access (OA) subset. Unlike scraping HTML web pages, which is brittle and prone to breakage, extracting data from PMC relies on the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH). This protocol allows for the systematic, incremental harvesting of records in a machine-readable format.

### **2.1 OAI-PMH Protocol Implementation Details**

The PMC OAI-PMH service acts as the primary ingress point. It is a RESTful API that serves metadata and full-text content wrapped in XML envelopes. To set up the scraping code, the developer must implement a harvester that strictly adheres to the OAI-PMH version 2.0 standard.

Endpoint Configuration:  
The base URL for all requests is:  
https://pmc.ncbi.nlm.nih.gov/api/oai/v1/mh/.1  
Set Selection logic:  
To ensure the retrieval of full-text data (required for extracting case narratives) rather than just abstracts, the scraper must specify the set parameter. The target set for this pipeline is pmc-open. This subset includes millions of articles under Creative Commons licenses that legally permit text mining and reuse.1

* **Parameter:** set=pmc-open  
* **Implication:** This filters the harvest to exclude "author manuscripts" or subscription-only content that would return 403 errors or incomplete metadata during full-text fetch attempts.2

Metadata Format Selection:  
Standard Dublin Core (oai\_dc) is insufficient for this application because it lacks the granular tagging required to identify "remission" versus "treatment." The scraper must request the NISO JATS (Journal Article Tag Suite) format.

* **Parameter:** metadataPrefix=pmc.1  
* **Technical Justification:** The pmc prefix returns the full-text XML, including the \<body\> element where the case presentation resides. The pmc\_fm prefix only returns front-matter (abstract/authors), which is inadequate for confirming spontaneous remission details.1

Request Cycle and Pagination:  
The initial request structure for the harvester code should be:

HTTP

GET https://pmc.ncbi.nlm.nih.gov/api/oai/v1/mh/?verb=ListRecords\&set=pmc-open\&metadataPrefix=pmc

The API does not return the entire dataset in a single response. It utilizes flow control via resumption tokens. The response will contain a \<resumptionToken\> element at the end of the XML list. The scraper code must parse this token and issue a subsequent GET request:

HTTP

GET https://pmc.ncbi.nlm.nih.gov/api/oai/v1/mh/?verb=ListRecords\&resumptionToken=

This loop continues until the API returns an empty resumption token, signaling the end of the dataset.

### **2.2 NISO JATS XML Structure and Parsing Logic**

Once the XML is retrieved, the core task is parsing the NISO JATS structure to identify relevant case reports. The JATS schema is highly nested and requires a robust XML parser (such as Python's lxml or the dedicated pubmed\_parser library) to navigate.

Article Type Identification:  
The first filter in the scraping logic is to determine if a record is a "Case Report." This is defined in the root \<article\> element attributes.

* **XPath Target:** /article/@article-type  
* **Target Value:** case-report.5  
* **Secondary Values:** While case-report is the primary target, valuable data may occasionally appear in research-article or letter. However, for the initial setup, restricting the scraper to article-type="case-report" yields the highest signal-to-noise ratio.

Section-Level Extraction (The Case Presentation):  
Within a valid case report, the narrative of the spontaneous remission is typically contained within a specific section. The JATS standard includes a @sec-type attribute to semantically classify sections.

* **Primary XPath:** //body/sec\[@sec-type='case-presentation'\].7  
* **Fallback XPath:** If the specific attribute is missing (as implementation varies by publisher), the scraper must inspect the \<title\> child of the section: //body/sec or //body/sec\[contains(title, 'Case')\].

Diagnostic Verification Logic:  
The scraper must programmatically verify the diagnosis to ensure the case involves malignancy. This involves extracting data from the \<kwd-group\> or the abstract text.

* **Keywords:** The code should extract text from //front/article-meta/kwd-group and run a regex check for oncology-related terms (e.g., "carcinoma," "sarcoma," "metastatic").  
* **Biopsy Confirmation:** A critical technical requirement is validating that the remission was genuine. The scraper should parse the text within the \<case-presentation\> section for specific strings indicating histological verification: "biopsy," "histopathology," "immunohistochemistry," or "pathological examination".8

Outcome and Intervention Extraction:  
To differentiate "spontaneous" remission from standard therapeutic response, the scraper must extract treatment data.

* **Intervention Tags:** While specific tags for "intervention" are rare, the scraper can target drug names using Named Entity Recognition (NER) on the text within //body/sec\[@sec-type='case-presentation'\].  
* **Outcome Markers:** The code must scan for negation patterns in proximity to treatment terms (e.g., "declined chemotherapy," "no treatment administered") to flag Type I remissions (no treatment).

### **2.3 Handling Images and Supplementary Material**

Medical case reports frequently rely on visual evidence (CT/PET scans) to prove remission. The JATS XML references these files, which must be scraped separately if the database intends to store evidence.

* **Graphic Elements:** Images are defined in \<graphic\> tags. The scraper must extract the @xlink:href attribute, which contains the filename.9  
* **Media Mapping:** These filenames correspond to assets stored in the PMC FTP service or cloud buckets. The scraper code needs to construct the full URL by appending the base image path for the specific PMCID.  
* **Caption Text:** The \<caption\> element associated with each graphic is a high-priority scrape target. Captions often contain quantitative data (e.g., "Figure 1: 5cm tumor... Figure 2: Complete resolution"). Extracting //fig/caption/p allows the system to capture this regression data textually.9

## **3\. The Clinical Narrative Tier: The Radical Remission Project (RRP)**

The Radical Remission Project (RRP) provides a dataset of "clinically supported narratives." Unlike PMC's structured XML, this source is a dynamic web application containing user-submitted profiles. The scraping approach here shifts from API harvesting to browser automation and DOM traversal.

### **3.1 Target Site Architecture and Scraping Strategy**

The website (radicalremission.com) utilizes modern web technologies that likely render content dynamically via JavaScript. A simple requests.get() in Python will fail to retrieve the survivor data because the HTML is generated client-side.

* **Required Tooling:** The scraping environment must utilize a headless browser driver such as **Selenium** or **Playwright**. These tools allow the script to execute the page's JavaScript, rendering the full DOM before extraction attempts.8  
* **Target URL Pattern:** The scraper should target the survivor stories index, typically located at /survivor-stories/ or /blog/category/survivor-stories/. Individual profiles often follow a permalink structure like /profile/\[survivor-name\] or /story/\[id\].8  
* **Pagination Logic:** The index page will likely use infinite scroll or numbered pagination. The scraper code must detect the "Next" button or the scroll event trigger to iteratively load all profiles.

### **3.2 DOM Structure and Data Selectors**

Once the page is rendered, the scraper must target specific HTML elements to extract the "9 Key Factors" and diagnostic metadata. While the CSS classes may change, the semantic structure typically remains stable.

A. Profile Metadata Extraction:  
The top section of a survivor profile usually contains the "hard" data regarding their condition.

* **Diagnosis Field:** Look for elements containing the text "Diagnosis:" or "Cancer Type:". The data is often in a sibling \<span\> or \<div\>.  
  * *Selector Strategy:* //div/following-sibling::div or .profile-diagnosis.  
* **Prognosis/Stage:** Similarly, look for "Stage" or "Prognosis" labels.  
  * *Selector Strategy:* //div/following-sibling::div.  
* **Date of Diagnosis:** This is critical for calculating survival duration.  
  * *Selector Strategy:* //div/following-sibling::div.

B. The "9 Key Factors" Extraction:  
The RRP dataset is unique because it tags cases with specific healing factors (e.g., "Radically changing your diet," "Following your intuition"). These are often displayed as a list of tags or checkboxes within the profile.8

* **List Iteration:** The scraper should identify the container element for these factors (e.g., ul.healing-factors or div.tags).  
* **Mapping Logic:** The code must iterate through the \<li\> or \<span\> children of this container. For each item found, the scraper should update a boolean array in the database schema (e.g., factor\_diet \= True, factor\_intuition \= True). The specific text strings to match against are:  
  1. Radically changing your diet  
  2. Taking control of your health  
  3. Following your intuition  
  4. Using herbs and supplements  
  5. Releasing suppressed emotions  
  6. Increasing positive emotions  
  7. Embracing social support  
  8. Deepening your spiritual connection  
  9. Having strong reasons for living.8

C. Narrative Text Extraction:  
The unstructured "My Story" section provides the context for the factors.

* **Content Block:** The scraper must locate the main article body, usually contained in \<div class="entry-content"\> or \<article\>.  
* **Cleaning:** The extraction code should strip out social media sharing buttons, "Related Posts" widgets, and comments, focusing solely on the \<p\> tags within the main content wrapper.

### **3.3 Access Control and Ethics**

The RRP data involves user-submitted health data. While public, it requires careful handling.

* **Rate Limiting:** To prevent IP blocking and server strain, the scraper must implement a sleep() function between requests (e.g., 2-5 seconds).  
* **Robots.txt:** The code should check https://radicalremission.com/robots.txt to identify any disallowed paths or sitemap locations (Sitemap:.../sitemap.xml) which can make the discovery phase significantly more efficient.8

## **4\. The Forensic Tier: Lourdes Medical Bureau and Miracle Hunter**

The Lourdes dataset represents the "Forensic" tier—cases validated by the International Medical Committee of Lourdes (CMIL). This data exists in two primary formats: static HTML tables on aggregation sites (Miracle Hunter) and PDF dossiers/official lists on the sanctuary's site.

### **4.1 Scraping Miracle Hunter (Static HTML Tables)**

The website miraclehunter.com maintains a comprehensive, static list of the verified cures. This data is highly structured in HTML tables or list definitions.

Target URLs:  
The primary list is split across multiple pages. The scraper must iterate through these known endpoints:

* http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles1.html (Miracles 1-20)  
* http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles2.html (Miracles 21-40)  
* http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles3.html (Miracles 41-60)  
* http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles4.html (Miracles 61-70).12

HTML Parsing Logic:  
The pages use a repetitive layout where each case is separated by horizontal rules (\<hr\>) or distinct table rows (\<tr\>).

* **Name Extraction:** The scraper should target bold tags \<b\> or \<strong\> at the start of a block to capture the patient's name (e.g., "**Mrs Catherine LATAPIE**").12  
* **Data Parsing (Regex):** Much of the metadata is embedded in text strings. The scraper needs Regex patterns to extract fields:  
  * *Birth Year:* r"Born in (\\d{4})"  
  * *Cure Date:* r"Cured (?:on )?(\\d{1,2}(?:st|nd|rd|th)?\\.? \\w+ \\d{4})"  
  * *Recognition Date:* r"Miracle on (\\d{1,2}(?:st|nd|rd|th)?\\.? \\w+ \\d{4})".12  
* **Narrative Extraction:** The text following the headers describes the medical condition. The scraper must capture this text block to parse for keywords like "Tuberculosis," "Paralysis," or "Blindness." Since these terms are often archaic (e.g., "Pott's disease"), the scraper's post-processing pipeline should include a mapping dictionary to modernize these terms to ICD-10 codes.8

### **4.2 Scraping Official PDF Dossiers (Lourdes-France.org)**

The official sanctuary website (lourdes-france.org) often hosts the official list and detailed dossiers in PDF format.

* **Target Asset:** The scraper should look for the "List of recognized miracles" PDF.14  
* **PDF Extraction Tooling:** Python libraries like pdfplumber or PyPDF2 are required here. Unlike HTML, PDFs lack a DOM. The strategy is to extract text based on spatial layout or text streams.  
* **Key Fields in PDF:** The scraper should look for tabular data within the PDF text stream. Columns typically include "Name," "Diocese," "Date of Cure," and "Nature of Illness."  
* **Validation Marker:** The scraper should verify the presence of the string "Bureau des Constatations Médicales" or "International Medical Committee" in the header/footer to confirm the document's authenticity.8

## **5\. The Legacy Tier: IONS Bibliography**

The Institute of Noetic Sciences (IONS) produced the seminal "Spontaneous Remission: An Annotated Bibliography" in 1993\. This dataset is a legacy artifact, often available only as digitized PDFs or static web archives, rather than a queryable database.

### **5.1 Scraping Strategy for Static Archives**

The scraping code for IONS data must function primarily as a "Re-hydration" engine. The goal is to extract citation strings from the static/PDF text and use them to query modern databases (like PubMed) to retrieve the full, structured metadata.

**Extraction Pipeline:**

1. **Download:** The scraper fetches the chapter-based PDFs from the IONS library page.15  
2. **OCR/Text Extraction:** Using pytesseract (if images) or pdfplumber (if text-based), the scraper converts the PDF content into a raw text stream.  
3. **Citation Parsing:** The code must identify citation blocks. These typically follow a pattern: \[Author List\].. \[Journal\].;\[Volume\]:\[Pages\].  
4. **Re-hydration (The "Modernization" Step):** Once a citation string is extracted (e.g., "Everson & Cole, 1966"), the scraper sends this string to the **PubMed ID Converter API** or the **Crossref API**.  
   * *API Endpoint:* https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/.17  
   * *Goal:* To retrieve a valid PMID (PubMed ID) or DOI (Digital Object Identifier).  
5. **Integration:** Once a PMID is obtained, the record essentially moves to the "Biomedical Tier" (Section 2), where the OAI-PMH scraper can be used to fetch the full JATS XML, effectively upgrading the legacy text into a modern, structured case report.

## **6\. Implementation Strategy and Code Structure**

To operationalize this specification, the scraping infrastructure should be modular, separating the crawling logic from the parsing and storage logic.

**Technology Stack:**

* **Language:** Python 3.9+ (Standard for data science/scraping).  
* **Core Libraries:**  
  * requests: For OAI-PMH and static HTML fetching.  
  * lxml: For high-performance JATS XML parsing.  
  * selenium / playwright: For RRP dynamic content.  
  * beautifulsoup4: For cleaning messy HTML from Miracle Hunter.  
  * pdfplumber: For extracting text from Lourdes/IONS PDFs.  
* **Data Storage:** PostgreSQL with a JSONB column is recommended. The JSONB column allows for the flexible storage of heterogeneous metadata (e.g., distinct fields for "Miracle Date" vs. "Biopsy Date") while maintaining a relational structure for core fields (Patient ID, Diagnosis Code).

**Orchestration Logic:**

1. **Harvester Module:** Runs chronologically. For PMC, it stores the last\_harvest\_date and only requests records from from=\[last\_date\] to minimize load.  
2. **Parser Module:** Contains specific classes for each source (JATSParser, RRPParser, LourdesParser). Each class implements a normalize() method to map source-specific fields to the common SRD schema.  
3. **Validation Module:** Runs post-scrape. It checks for the presence of "Verification Markers" (e.g., biopsy confirmation) and assigns a Validation\_Tier (1-4) to the record before committing it to the database.8

This architecture provides a scalable, resilient foundation for aggregating spontaneous remission data. By treating medical case reports, patient narratives, and forensic records as distinct but compatible data streams, the system can build a dataset that is both clinically rigorous and rich in the qualitative factors associated with anomalous healing.

#### **Works cited**

1. PMC OAI-PMH API \- PubMed Central, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/tools/oai/](https://pmc.ncbi.nlm.nih.gov/tools/oai/)  
2. PMC Open Access Subset \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/tools/openftlist/](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/)  
3. PMC Copyright Notice \- PubMed Central \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/about/copyright/](https://pmc.ncbi.nlm.nih.gov/about/copyright/)  
4. List of Approved Lourdes Miracles, accessed on January 1, 2026, [https://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles3.html](https://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles3.html)  
5. Attribute: Type of Article \- Journal Article Tag Suite, accessed on January 1, 2026, [https://jats.nlm.nih.gov/archiving/tag-library/1.1/attribute/article-type.html](https://jats.nlm.nih.gov/archiving/tag-library/1.1/attribute/article-type.html)  
6. Attribute: Type of Article \- Journal Article Tag Suite, accessed on January 1, 2026, [https://jats.nlm.nih.gov/archiving/tag-library/1.3/attribute/article-type.html](https://jats.nlm.nih.gov/archiving/tag-library/1.3/attribute/article-type.html)  
7. Sections | JATS Guide, accessed on January 1, 2026, [https://jats.taylorandfrancis.com/jats-guide/topics/sections/](https://jats.taylorandfrancis.com/jats-guide/topics/sections/)  
8. Architectural Blueprint for the Comprehensive Spontaneous Remission Database: Ontological Framework, Data Acquisition Strategies, and Computational Schema Design  
9. NIHMS JATS 1.2 Tagging Guidelines \[article\] \- NCBI, accessed on January 1, 2026, [https://www.ncbi.nlm.nih.gov/pmc/pmcdoc/tagging-guidelines/manuscript/tags.html](https://www.ncbi.nlm.nih.gov/pmc/pmcdoc/tagging-guidelines/manuscript/tags.html)  
10. How To Scrape GitHub: A Practical Tutorial 2025 \- Decodo, accessed on January 1, 2026, [https://decodo.com/blog/how-to-scrape-github](https://decodo.com/blog/how-to-scrape-github)  
11. The Transformative Power of the Radical Remission: 10 Healing Factors \- Yes to Life Charity, accessed on January 1, 2026, [https://yestolife.org.uk/the-transformative-power-of-the-radical-remission/](https://yestolife.org.uk/the-transformative-power-of-the-radical-remission/)  
12. Lourdes \- List of Approved Miracles \- Miracle Hunter, accessed on January 1, 2026, [http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles1.html](http://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles1.html)  
13. Miraculous healings \- Lourdes, accessed on January 1, 2026, [https://www.lourdes-france.org/en/miraculous-healings/](https://www.lourdes-france.org/en/miraculous-healings/)  
14. The Lourdes Medical Cures Revisited \- PMC \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3854941/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3854941/)  
15. Spontaneous Remission Bibliography \- Institute of Noetic Sciences (IONS), accessed on January 1, 2026, [https://noetic.org/science/spontaneous-remission-bibliography/](https://noetic.org/science/spontaneous-remission-bibliography/)  
16. Spontaneous Remission Bibliography Project \- Institute of Noetic Sciences (IONS), accessed on January 1, 2026, [https://noetic.org/research/spontaneous-remission-bibliography-project/](https://noetic.org/research/spontaneous-remission-bibliography-project/)  
17. For Developers \- PMC \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/tools/developers/](https://pmc.ncbi.nlm.nih.gov/tools/developers/)