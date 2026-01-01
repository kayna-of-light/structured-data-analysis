# **Architectural Blueprint for the Comprehensive Spontaneous Remission Database: Ontological Framework, Data Acquisition Strategies, and Computational Schema Design**

## **1\. Introduction: The Epistemological Necessity of Anomalous Data Aggregation**

The contemporary landscape of oncological informatics is dominated by registries designed to track the efficacy of standard-of-care interventions. Databases such as the Surveillance, Epidemiology, and End Results (SEER) program or the National Cancer Database (NCDB) are optimized to quantify the outcomes of chemotherapy, radiation, and surgical resection. However, these systems inherently marginalize the statistical outlier: the patient who recovers in the absence of conventional treatment, or whose recovery defies the probabilistic prognosis of their pathology. This phenomenon, historically termed "Spontaneous Remission" (SR) and more recently reframed as "Radical Remission," remains one of the most provocative yet under-utilized frontiers in medical science. The challenge in studying SR is not a lack of occurrence—research suggests the phenomenon is significantly underreported rather than non-existent—but a lack of structured, aggregated data.1

To transition the study of spontaneous remission from the realm of anecdote to the rigor of statistical science, a new architectural baseline is required. This report outlines the design and implementation of a centralized **Spontaneous Remission Database (SRD)**. This system is not merely a repository of text but a structured engine designed to scrape, parse, normalize, and analyze disparate data sources ranging from peer-reviewed medical case reports to verified patient narratives. The objective is to map the "long tail" of survivorship by integrating biological "ground truth" with the bio-behavioral and psycho-spiritual variables that frequently accompany inexplicable recoveries.

The design of this database requires a fundamental shift in medical ontology. Where traditional databases ask, "What drug did the patient receive?", the SRD must be engineered to ask, "What profound existential shift, lifestyle modification, or anomalous experience preceded the regression of the disease?" This necessitates a complex schema capable of handling data from four distinct epistemological domains: the rigorous clinical definitions of the **Institute of Noetic Sciences (IONS)**, the qualitative lifestyle factors identified by **Dr. Kelly Turner (Radical Remission)**, the phenomenological accounts of **Near-Death Experiences (NDERF)**, and the strict forensic verification protocols of the **Lourdes Medical Bureau**. By synthesizing these domains, we establish a baseline for a scraper that can distinguish between a "miracle," a misdiagnosis, and a delayed therapeutic effect, ultimately providing the data density required for multivariate statistical analysis.3

## **2\. Ontological Framework: Defining the Signal in the Noise**

Before any code is written or any data is scraped, the precise definition of the target variable—remission—must be established. The "signal" in this domain is often obscured by the "noise" of palliative treatments, slow-growing pathologies, and misdiagnoses. Therefore, the scraper must be mapped upon a rigorous ontological framework that differentiates between various types of regression and recovery.

### **2.1 The Taxonomy of Remission and Regression**

The foundational definition for this database is derived from the seminal work of Everson and Cole (1966), later refined by O'Regan and Hirshberg in the IONS bibliography. For the purposes of the scraper's inclusion logic, Spontaneous Remission is defined as the partial or complete disappearance of a malignant tumor in the absence of all treatment, or in the presence of therapy which is considered inadequate to exert a significant influence on neoplastic disease.2

To support granular analysis, the database must implement a tiered classification system that sorts scraped cases into specific ontological buckets. The scraper must be programmed to detect contextual clues that categorize the remission event:

* **Type I (Pure Remission):** This category includes cases where the patient received absolutely no allopathic intervention. An example would be a patient diagnosed with biopsy-confirmed osteosarcoma who refuses amputation and chemotherapy, yet is disease-free five years later. The scraper must prioritize keywords such as "refused treatment," "no intervention," or "hospice care only" to identify these high-value cases.1  
* **Type II (Inadequate Treatment):** This category captures cases where treatment was administered but is medically insufficient to explain the cure. For instance, a patient with metastatic renal cell carcinoma who receives palliative radiation to a single bone lesion but subsequently experiences the clearance of systemic lung metastases. The scraper logic here is complex, requiring a lookup of "Standard of Care" vs. "Received Treatment" to calculate a Therapeutic\_Adequacy\_Score.7  
* **Type III (Psychogenic/Anomalous Mediation):** This classification is critical for the user's specific interest in "experiences." It involves remissions temporally linked to a specific event, such as a Near-Death Experience (NDE), a profound spiritual conversion (e.g., Lourdes), or a radical lifestyle overhaul. These cases often overlap with Types I and II but are distinguished by the presence of a distinct "trigger" event.

Furthermore, the database must enforce a distinction between **Regression** (a measurable reduction in tumor burden) and **Remission** (the absence of clinical disease activity). Many "miracle" stories on the internet conflate the two; a tumor shrinking by 10% is regression, but it is not a cure. The scraper's Natural Language Processing (NLP) pipeline must extract quantitative metrics (e.g., "tumor shrank from 5cm to 2cm") to validate these classifications.2

### **2.2 The Psycho-Spiritual Correlate: Extending the Medical Schema**

A purely materialist database would fail to capture the variables most relevant to the user's query regarding "experiences." Research from the Division of Perceptual Studies (DOPS) and the Radical Remission Project suggests that physiological changes are often downstream effects of shifts in consciousness or "influx".3 Consequently, the data schema must extend beyond standard medical coding systems like ICD-10 or SNOMED-CT.

The database requires a **Bio-Behavioral Ontology**. This involves creating structured fields for concepts that standard medicine treats as unstructured text. For example, Dr. Kelly Turner’s research identifies "Releasing Suppressed Emotions" and "Deepening Spiritual Connection" as key factors.4 The scraper must map narrative phrases such as "I finally forgave my father" or "I let go of my resentment" to a boolean or scalar variable Emotional\_Release\_Event. Similarly, the "Swedenborgian" view presented in the research suggests a bidirectional link between trauma and somatic manifestation; just as past-life trauma might print birthmarks onto a fetus, the resolution of spiritual trauma (fear/guilt) might erase physical pathology.3 The scraper must therefore look for keywords indicating a "reversal" of trauma or a "rewrite" of the patient's identity narrative.

## **3\. Structural Baseline: Analyzing Source-Specific Data Models**

To build a universal scraper, we must deconstruct the data structures of the primary existing repositories. The proposed SRD will be a superset of these models, ingesting data from each while normalizing it into a unified schema.

### **3.1 The IONS Spontaneous Remission Bibliography Model**

The Institute of Noetic Sciences (IONS) produced the gold standard bibliography for this field, cataloging over 3,500 references from 800 journals.1 The IONS model provides the "hard" medical baseline for the database.

The IONS entries are structured around **Histological Verification**. The single most critical data point in this model is the confirmation of diagnosis. Without a biopsy, a "remission" is statistically worthless because the original diagnosis could have been an error (e.g., a benign cyst misdiagnosed as cancer).

* **Data Requirement:** The scraper must parse the "Methods" or "Case Presentation" sections of medical texts to find strings like "biopsy confirmed," "histopathology revealed," or "specimen analysis."  
* **Documentation Level:** The database should assign a Confidence\_Score based on the IONS hierarchy:  
  1. **Histologic Confirmation:** The tissue was examined under a microscope (Highest Confidence).  
  2. **Radiographic Evidence:** The tumor was seen on X-ray/CT/MRI but not biopsied (Medium Confidence).  
  3. **Clinical Diagnosis:** Diagnosis based on physical exam/symptoms (Low Confidence).

The IONS model also emphasizes the **Duration of Remission**. A "cure" is a function of time. The scraper must extract temporal data points: Date\_of\_Diagnosis, Date\_of\_Treatment\_Cessation, and Date\_of\_Last\_Followup. The calculated delta between these dates determines whether a case qualifies as a "durable remission" or merely a temporary fluctuation.2

### **3.2 The Radical Remission (Kelly Turner) Model**

Dr. Kelly Turner's research introduces the "human" variable. While IONS focuses on the biology of the tumor, the Radical Remission model focuses on the agency of the patient. Turner analyzed over 1,500 cases and identified 9 key healing factors, only two of which (diet and supplements) are physical.4 The remaining seven are psycho-spiritual.

Scraping Targets for the Turner Model:  
The scraper must be trained to recognize the 9 factors within unstructured patient testimonials (found on sites like RadicalRemission.com or The Patient Story):

1. **Dietary Change:** Keywords: "Keto," "Vegan," "Juicing," "No Sugar," "Organic."  
2. **Taking Control:** Keywords: "Did my own research," "Defied doctor's timeline," "Advocate."  
3. **Intuition:** Keywords: "Gut feeling," "Voice told me," "Just knew."  
4. **Supplements:** Keywords: "Mistletoe," "Vitamin C," "Curcumin," "CBD."  
5. **Releasing Emotions:** Keywords: "Forgiveness," "Therapy," "Letting go," "Crying," "Anger."  
6. **Positive Emotions:** Keywords: "Joy," "Laughter," "Comedy," "Hope."  
7. **Social Support:** Keywords: "Community," "Family," "Friends," "Prayer circle."  
8. **Spiritual Connection:** Keywords: "Meditation," "God," "Universe," "Nature," "Source."  
9. **Reasons for Living:** Keywords: "Grandchildren," "Unfinished business," "Purpose."

**Database Implication:** The Intervention table in the database must include boolean flags for each of these factors (e.g., factor\_diet\_change: TRUE), as well as text fields to capture the specific qualitative details (e.g., diet\_details: "Strict ketogenic diet with intermittent fasting"). This allows for statistical correlation: do patients who combine Factor 1 (Diet) and Factor 5 (Emotion) see faster remission times than those who only use Diet?

### **3.3 The NDERF & DOPS Anomalous Experience Model**

A significant subset of spontaneous remissions occurs in conjunction with Near-Death Experiences (NDEs). The case of Anita Moorjani is the archetype: end-stage lymphoma resolving within days following an NDE.3 To capture this, the database must incorporate the data standards of NDE research, specifically the **Greyson NDE Scale** and the NDERF questionnaire structure.

The Greyson Scale Integration:  
The Greyson Scale is a validated instrument for quantifying the depth of an NDE.13 The scraper should attempt to calculate a proxy Greyson score based on the narrative features present in the text.

* **Cognitive Features:** Time distortion, thought acceleration, life review.  
* **Affective Features:** Feelings of peace, joy, cosmic unity, light.  
* **Paranormal Features:** Out-of-body experience (OBE), vivid senses, ESP.  
* **Transcendental Features:** Unearthly realms, encounters with deceased/religious figures, borders/points of no return.

Veridical Perception:  
A critical data point for validation is "veridical perception"—situations where the patient, while comatose or clinically dead, observes events (e.g., a conversation in the hallway) that are later verified by medical staff.15 The scraper should tag cases with Veridical\_Evidence: TRUE if the narrative contains phrases like "doctor confirmed," "nurse was shocked I knew," or "verified by staff." This connects to the DOPS research on consciousness surviving bodily death, suggesting a non-local mechanism for the healing "download".9

### **3.4 The Lourdes Medical Bureau Verification Model**

For cases labeled as "miraculous," the Lourdes Medical Bureau provides the strictest verification model in existence. Their process, based on the **Lambertini Criteria** (established by Pope Benedict XIV in the 1700s), is a forensic audit that eliminates almost all claims.6

**The 7 Lambertini Criteria (Scraping Validation Logic):**

1. **Diagnosis:** The disease must be serious and impossible to cure or difficult to treat.  
2. **Prognosis:** The disease must not be in a stage where natural regression is possible.  
3. **Treatment:** No medication could have been the cause.  
4. **Suddenness:** The cure must be instantaneous or nearly so.  
5. **Completeness:** The cure must be perfect, not just an improvement.  
6. **Permanence:** The cure must be lasting (no relapse).  
7. **Crisis:** The cure must follow a distinct "crisis" or invocation.

When scraping data from religious or spiritual healing archives, the system must look for official "Medical Bureau" stamps or attestations. A case from Lourdes that has passed the *Bureau des Constatations Médicales* is of a higher data quality tier than a self-reported story on a forum. The database must reflect this hierarchy of evidence. The Lourdes archives also introduce the concept of the "Dossier," a complete medical file containing pre- and post-cure imaging. While the scraper cannot access physical dossiers, it can identify digital references to them (e.g., "Case 54, Vittorio Micheli, osteosarcoma of the pelvis, bone regrew"). The specific mention of **structural regeneration** (e.g., bone regrowth) is a key differentiator from simple symptom remission.17

## **4\. Comprehensive Data Schema Specification**

Based on the synthesis of the four domains above, the following schema is proposed for the Spontaneous Remission Database. This schema utilizes a relational database structure (e.g., PostgreSQL) to maintain data integrity while allowing for the flexibility of JSONB columns to store unstructured narrative data.

### **4.1 Table: CASE\_registry (The Core Index)**

This table serves as the primary ledger for the database. Every scraped entity, whether a PDF from PubMed or a blog post from NDERF, becomes a row here.

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| case\_id | UUID | Primary Key | System Generated |
| source\_url | String | Origin URL of the data point | url |
| original\_source\_id | String | ID from the source (e.g., PMID, NDERF Case \#) | pmid, case\_number |
| data\_confidence\_score | Float | Calculated (0.0-1.0) based on biopsy/imaging presence | Algorithm |
| validation\_tier | Enum | Tier1\_Institutional\_Verification (Lourdes/Published), Tier2\_Medically\_Supported, Tier3\_Patient\_Reported | 2 |
| remission\_category | Enum | Spontaneous, Radical, Inadequate\_Tx, Unexpected\_Response | Everson & Cole |
| publication\_date | Date | Date the report was published | Metadata |
| last\_scraped | Timestamp | Date of extraction | System |

**Insight:** The validation\_tier is the most critical metadata field. It allows researchers to filter the dataset. For a study on "biological mechanisms," one might query only Tier1 cases. For a study on "psychological correlates," Tier3 cases are permissible.

### **4.2 Table: PATIENT\_demographics**

Standardizing the subject of the case while adhering to privacy standards (HIPAA/GDPR).

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| case\_id | UUID | Foreign Key |  |
| year\_of\_birth | Integer | YYYY (Avoid full DOB for anonymization) | CARE Guidelines 19 |
| sex | Enum | Male, Female, Intersex | Demographics |
| ethnicity | String | Standardized Census Categories | Demographics |
| geographic\_region | String | ISO Country Code / State | Location Data |
| occupation | String | Relevant for environmental exposure analysis | Patient History |
| pre\_morbid\_personality | Text | Qualitative description (e.g., "Type A", "Depressive") | Psychosocial 2 |

### **4.3 Table: MEDICAL\_diagnosis (The "Ground Truth")**

This table captures the biological reality prior to the remission event. It is the "Before" snapshot.

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| primary\_diagnosis\_raw | String | The exact text from the source (e.g., "Stage 4 Lung Ca") | Raw Text |
| icd\_10\_code | String | Normalized diagnosis code (e.g., C34.9) | ICD Ontology |
| histology\_type | String | Cell type (e.g., "Adenocarcinoma", "Osteosarcoma") | Pathology |
| stage\_at\_diagnosis | String | TNM Staging (I, II, III, IV) | AJCC Staging |
| grade | Integer | Tumor Grade (1-4) | Pathology |
| metastasis\_sites | JSONB | List of sites (e.g., \`\`) | Clinical Data |
| biopsy\_confirmed | Boolean | TRUE if histology report is cited | IONS Criteria 2 |
| imaging\_confirmed | Boolean | TRUE if CT/MRI/PET is cited | IONS Criteria |
| prognosis\_given | Text | Expected survival (e.g., "6 months") | Narrative |
| karnofsky\_score | Integer | Performance status (0-100) at diagnosis | Clinical Metrics |

**Insight:** The biopsy\_confirmed field is the primary filter for scientific validity. If this is FALSE, the case is likely anecdotal. The metastasis\_sites field is crucial for distinguishing between local regression (which can happen spontaneously in some tumors) and systemic remission (which implies a holistic organismal shift).

### **4.4 Table: INTERVENTION\_history (The "Cause" Analysis)**

Tracking the "independent variables"—what was done to the patient, both conventionally and alternatively.

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| conventional\_tx | JSONB | List: \`\` | Standard Care |
| tx\_outcome | Enum | Failed, Refused, Incomplete, Abandoned | Narrative |
| alternative\_tx | JSONB | List: \`\` | Radical Remission 11 |
| dietary\_protocol | Enum | None, Keto, Vegan, Raw, Fasting, Macrobiotic | Turner Factor 1 |
| supplement\_list | Text | Extracted entities (e.g., "Mistletoe, Vit C") | Turner Factor 4 |
| emotional\_work | Boolean | TRUE if therapy/release work mentioned | Turner Factor 5 |
| spiritual\_practice | Boolean | TRUE if prayer/meditation mentioned | Turner Factor 8 |
| social\_support | Enum | Strong, Moderate, Isolated | Turner Factor 7 |

### **4.5 Table: ANOMALOUS\_experience (The "Trigger" Event)**

This table captures the specific data points related to the user's interest in "experiences." It is derived from the NDERF and DOPS methodologies.

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| has\_experience | Boolean | TRUE if NDE/STE/OBE reported | NDERF |
| experience\_type | Enum | NDE, OBE, STE, Shared\_Death, Dream | NDERF Classifications |
| greyson\_score | Integer | Estimated score (0-32) based on narrative features | Greyson Scale 13 |
| phenomena\_tags | JSONB | \`\` | NDE Features |
| veridical\_check | Boolean | TRUE if out-of-body perceptions were verified | Verification 15 |
| transformational\_shift | Text | Description of psychological reset (e.g., "No fear of death") | Narrative Analysis |
| intuitive\_insight | Text | Specific "download" received (e.g., "Eat only grapes") | Intuition Factor |

**Insight:** This table allows for the correlation of *subjective intensity* with *objective outcome*. Does a higher Greyson score correlate with a faster rate of tumor regression? This is a question only this database could answer.

### **4.6 Table: REMISSION\_outcome (The "Effect")**

The measurable result of the case.

| Field Name | Data Type | Description | Source Mapping |
| :---- | :---- | :---- | :---- |
| date\_of\_remission | Date | Date "No Evidence of Disease" (NED) declared | Timeline |
| remission\_type | Enum | Complete, Partial, Stable, Spontaneous\_Regression | RECIST Criteria |
| time\_to\_remission | Integer | Days from trigger/intervention to remission | Timeline |
| duration\_survived | Integer | Months of verified survival post-remission | Survival Stats |
| current\_status | Enum | Alive, Deceased\_Cancer, Deceased\_Other, Lost | Follow-up |
| verification\_method | String | "CT Scan", "PET Scan", "Autopsy" | Lourdes 6 |
| structural\_change | Boolean | TRUE if tissue regenerated (e.g., bone regrowth) | Lourdes/Biology 16 |

## **5\. Strategic Scraping Implementation & Logic**

To populate this schema, the scraper must be an intelligent extraction agent. Simple HTML parsing is insufficient; the system requires a multi-modal approach combining API access, HTML scraping, and OCR text extraction.

### **5.1 Target Source Prioritization and Methods**

#### **5.1.1 High-Confidence Medical Literature (PubMed Central)**

The **PubMed Open Access (OA) Subset** is the primary target for verified biological data.

* **Access Method:** Use the PubMed Central OAI-PMH service or the FTP service for bulk retrieval of XML files.20  
* **Search Query:** Using boolean logic to isolate relevant cases: ("spontaneous regression" OR "spontaneous remission" OR "palliative care survivor") AND ("cancer" OR "neoplasm") NOT ("placebo" OR "clinical trial").  
* **Extraction Logic:** Use the pubmed\_parser Python library to parse the XML structure.  
  * Map \<article-title\> to Case Title.  
  * Map \<abstract\> to Case Summary.  
  * Parse the \<body-content\> specifically looking for the "Case Presentation" header to extract patient history.  
  * Extract citations to cross-reference with the IONS bibliography.

#### **5.1.2 Narrative & Experience Registries (NDERF, Radical Remission)**

These sources provide the psycho-spiritual data that medical journals often omit.

* **NDERF.org:** This site has a consistent URL structure (e.g., /Experiences/1anita\_m\_nde.html).  
  * **Scraper Logic:** Iterate through the "Exceptional NDEs" and "Nude Stories" (likely a typo in source, meant "NDE Stories") indexes.  
  * **Field Mapping:** Map the specific NDERF questionnaire fields (e.g., "Did you feel separated from your body?") directly to the ANOMALOUS\_experience table. Extract the narrative text block into case\_narrative for NLP processing.  
  * **Key Validation:** Check for the "Verified" tag or "Medical records provided" note in the header.15  
* **Radical Remission Project:**  
  * **Method:** Scrape user profiles and "Survivor Stories." These pages often contain structured fields like "Diagnosis," "Prognosis," and "Healing Factors Used."  
  * **Constraint:** These pages may be behind a login or dynamically loaded. Use **Selenium** or **Playwright** to render the JavaScript before extraction.23

#### **5.1.3 The "Gold Standard" Archives (Lourdes/Miracle Hunter)**

These sources provide the highest level of verification but are low volume.

* **Method:** These records are often static HTML tables or PDFs.  
* **Lourdes:** Scrape the list of 70 recognized miracles. For each, extract the "Bishop's Recognition Date" and "Medical Bureau Findings."  
* **MiracleHunter:** Parse the tables of "Cured" vs. "Miracle" to distinguish between medically inexplicable and religiously canonized events.24

### **5.2 Natural Language Processing (NLP) Pipeline**

Raw text from these sources must be converted into structured data. The scraping pipeline should integrate a Named Entity Recognition (NER) model, such as **spaCy** with the en\_core\_sci\_lg (biomedical) model.

**NLP Tasks:**

1. **Entity Extraction:**  
   * Identify **Diseases** and map them to ICD-10 codes (e.g., "Lung Ca" \-\> C34.9).  
   * Identify **Treatments** (e.g., "Cisplatin," "Reiki").  
2. **Temporal Resolution:**  
   * Extract timelines: "Diagnosed in 2012," "Clear scan in 2014." Calculate time\_to\_remission.  
3. **Negation Detection:**  
   * Crucial for defining Type I remission. If the text says "Patient *refused* chemotherapy," the NLP must detect the negation to flag conventional\_tx as None or Refused.  
4. **Sentiment/Theme Classification:**  
   * Analyze the narrative for Turner's 9 factors. A sentence like "I decided to stop fighting myself and start loving my body" should trigger the Emotional\_Release flag.

### **5.3 Technical Stack Recommendations**

* **Language:** Python (industry standard for data science).  
* **Scraping:** Scrapy for high-volume static sites (NDERF), Selenium for dynamic sites (Radical Remission), BeautifulSoup for parsing HTML structures.  
* **Parsing:** pubmed\_parser for XML, PyPDF2 or Tesseract (OCR) for reading older case reports in PDF format.20  
* **Storage:** PostgreSQL with a JSONB schema is ideal. It offers the rigidity of SQL for the demographic/medical tables and the flexibility of NoSQL (JSON) for storing the variable questionnaire responses and unstructured narratives.

## **6\. Legal and Ethical Framework: The Compliance Layer**

The aggregation of patient data, even when publicly posted, carries significant ethical and legal responsibilities. The database must be designed with "Privacy by Design" principles.

### **6.1 De-identification and HIPAA/GDPR Compliance**

While case reports published in journals are arguably public domain, data scraped from patient forums or social registries (like NDERF) requires careful handling.

* **Safe Harbor Method:** The database should automatically strip 18 specific identifiers defined by HIPAA.  
* **Date Generalization:** Do not store exact birth dates. Store Year\_of\_Birth only.  
* **Name Hashing:** If a name is present (e.g., "Anita M."), hash it to create a unique patient\_id but do not store the plaintext name unless explicitly authorized or part of a public book citation.  
* **Case Reports Exemption:** Under US federal regulations (45 CFR 46), case reports of 3 or fewer individuals generally do not constitute "human subjects research" requiring IRB approval. However, creating a *database* of thousands moves this into the realm of research. If the user intends to publish, IRB consultation is strongly advised, and the scraper should prioritize **De-identified Data**.25

### **6.2 Validity Scoring and Data Quality**

The central risk of this database is "Garbage In, Garbage Out." A user claiming to have cured cancer with baking soda on a forum is not equivalent to a biopsy-confirmed regression in a peer-reviewed journal.

* **Confidence Scoring Algorithm:**  
  * **\+3 Points:** Biopsy/Pathology report cited or uploaded.  
  * **\+2 Points:** Medical Imaging (CT/MRI) verification cited.  
  * **\+2 Points:** Case appears in a peer-reviewed journal (PubMed).  
  * **\+1 Point:** Case reviewed by an institutional board (Lourdes/IONS).  
  * **\-1 Point:** Self-reported diagnosis without doctor/hospital naming.  
  * **\-2 Points:** Diagnosis by non-medical practitioner (e.g., "My herbalist said I had cancer").  
* **Filtering:** The database front-end should allow users to toggle "Show only Medically Verified Cases" (Score \> 3).

## **7\. Analytical Implications: From Database to Insight**

Constructing this database opens the door to "Second-Order" and "Third-Order" insights that are currently impossible to generate.

### **7.1 The "Placebo" vs. "Influx" Distinction**

Current medical models often dismiss anomalous healing as the "placebo effect." However, the Swedenborgian and IONS frameworks suggest placebo is merely a "threshold" phenomenon—a weak echo of a more potent force (Influx).3 By capturing both the biological *magnitude* of the healing (e.g., bone regrowth, which placebo rarely achieves) and the *intensity* of the subjective experience (Greyson score), this database allows researchers to test the **Dose-Response Relationship of Consciousness**. Does a deeper NDE (higher Greyson score) correlate with a more rapid or structural biological repair?

### **7.2 The Bidirectional Trauma Model**

Research from DOPS indicates that spiritual trauma can "print" onto the body (e.g., birthmarks corresponding to past-life wounds).9 The SRD allows for the investigation of the inverse: does the *release* of spiritual trauma "clear" the body? By linking the Emotional\_Release fields from the Turner model with the Tumor\_Regression timelines, the database can statistically validate the "Body as Soul in Ultimates" theory proposed in the ontological framework.

### **7.3 Pattern Recognition in "Incurable" Cases**

Standard registries like SEER do not track "what else" the patient did. They track chemo and radiation. If a patient survives pancreatic cancer for 20 years, they are a statistical anomaly in SEER. In the SRD, they become a data point. By aggregating thousands of these "anomalies," the database may reveal hidden clusters—e.g., a statistically significant correlation between "Radical Diet Change" and "Spontaneous Remission of Renal Cell Carcinoma" that is invisible in datasets that only track chemotherapy.

## **8\. Conclusion**

The construction of a Spontaneous Remission Database is not merely a technical task of web scraping; it is an act of scientific reclamation. It involves gathering the "discarded data" of modern oncology—the anomalies, the miracles, the unexplained recoveries—and subjecting them to the same rigorous data structuring as clinical trials.

By adopting the **Everson/Cole definition** for inclusion, utilizing the **CARE guidelines** for clinical structure, and integrating the **Turner/Greyson scales** for qualitative variables, this project will generate a dataset capable of bridging the gap between materialist medicine and the phenomenology of healing. The blueprint provided here—spanning ontology, schema, scraping strategy, and ethics—ensures that when the "inexplicable" occurs, it is no longer lost to anecdote, but captured, codified, and made available for the advancement of human knowledge.

## ---

**9\. Appendix: Baseline Data Dictionary & Variable Map**

### **A. Core Identification Variables**

* **Source\_ID**: Unique ID from the source (e.g., PMID, NDERF Case \#).  
* **Data\_Source**: PubMed, NDERF, RadicalRemission, Lourdes\_Archives.  
* **URL**: Direct link to the source material.  
* **Verification\_Level**:  
  * *Level 1:* Self-reported, no medical records cited.  
  * *Level 2:* Self-reported, medical records/doctor cited by name.  
  * *Level 3:* Published Case Report (Peer-reviewed).  
  * *Level 4:* Institutional Validation (Lourdes Bureau, Ivy League Case Series).

### **B. Clinical Variables (The "Hard" Data)**

* **Diagnosis\_ICD10**: Mapped ICD-10 code.  
* **Tumor\_Site**: Primary organ.  
* **Tumor\_Histology**: Cell type.  
* **Stage\_TNM**: Tumor, Node, Metastasis classification.  
* **Treatment\_Status**: None, Incomplete, Palliative, Refused.  
* **Survival\_Months**: Time from diagnosis to last contact.  
* **Remission\_Status**: NED (No Evidence of Disease), Partial, Stable.

### **C. Experiential Variables (The "Soft" Data)**

* **RR\_Factors**: Binary flags for Turner's 9 factors (Diet, Intuition, etc.).  
* **NDE\_Present**: Boolean.  
* **NDE\_Score**: Integer (Greyson Scale).  
* **Trauma\_Release**: Boolean (Did the patient explicitly mention releasing a past trauma?).  
* **Spiritual\_Shift**: Boolean (Did the patient report a fundamental change in worldview?).

### **D. Scraper Configuration Parameters**

* **Rate\_Limit**: 1 request per 2 seconds (to avoid IP bans).  
* **User\_Agent**: Rotate user agents to mimic browser traffic.  
* **Robots\_Txt**: Adhere to robots.txt for each domain (scrape only allowed paths).  
* **Data\_Retention**: Store raw HTML/PDF locally; extract to SQL.

#### **Works cited**

1. Spontaneous Remission Bibliography \- Institute of Noetic Sciences (IONS), accessed on January 1, 2026, [https://noetic.org/science/spontaneous-remission-bibliography/](https://noetic.org/science/spontaneous-remission-bibliography/)  
2. Introduction \- Spontaneous Remission: An Annotated Bibliography \- Institute of Noetic Sciences (IONS), accessed on January 1, 2026, [https://noetic.org/wp-content/uploads/2020/10/SRB-intro.pdf](https://noetic.org/wp-content/uploads/2020/10/SRB-intro.pdf)  
3. Spiritual Transformation and Healing  
4. The Transformative Power of the Radical Remission: 10 Healing Factors \- Yes to Life Charity, accessed on January 1, 2026, [https://yestolife.org.uk/the-transformative-power-of-the-radical-remission/](https://yestolife.org.uk/the-transformative-power-of-the-radical-remission/)  
5. Near-Death Experiences Evidence for Their Reality \- PMC \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6172100/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6172100/)  
6. Lourdes Medical Bureau \- Wikipedia, accessed on January 1, 2026, [https://en.wikipedia.org/wiki/Lourdes\_Medical\_Bureau](https://en.wikipedia.org/wiki/Lourdes_Medical_Bureau)  
7. Metachronous Primary Lung Cancer Occurring during the Spontaneous Regression of Locally Advanced Lung Cancer: A Rare Case Report \- Semantic Scholar, accessed on January 1, 2026, [https://pdfs.semanticscholar.org/df95/aa44bc1ff612c2430baa6c41f3ca8c73c1db.pdf](https://pdfs.semanticscholar.org/df95/aa44bc1ff612c2430baa6c41f3ca8c73c1db.pdf)  
8. Radical remission : surviving cancer against all odds : Turner, Kelly A., author : Free Download, Borrow, and Streaming \- Internet Archive, accessed on January 1, 2026, [https://archive.org/details/radicalremission0000turn](https://archive.org/details/radicalremission0000turn)  
9. Cases of the Reincarnation Type with Memories from the Intermission Between Lives \- University of Virginia School of Medicine, accessed on January 1, 2026, [https://med.virginia.edu/perceptual-studies/wp-content/uploads/sites/360/2015/11/REI31.pdf](https://med.virginia.edu/perceptual-studies/wp-content/uploads/sites/360/2015/11/REI31.pdf)  
10. Spontaneous Remission: An Annotated Bibliography \- Institute of Noetic Sciences (IONS), accessed on January 1, 2026, [https://noetic.org/publication/spontaneous-remission-annotated-bibliography/](https://noetic.org/publication/spontaneous-remission-annotated-bibliography/)  
11. Effect of the Radical Remission Multimodal Intervention on Quality of Life of People with Cancer \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11528749/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11528749/)  
12. WWW Nderf Org Experiences 1anita M Nde HTML PDF \- Scribd, accessed on January 1, 2026, [https://www.scribd.com/document/459829095/www-nderf-org-Experiences-1anita-m-nde-html-pdf](https://www.scribd.com/document/459829095/www-nderf-org-Experiences-1anita-m-nde-html-pdf)  
13. Near-Death Encounters With and Without Near-Death Experiences: Comparative NDE Scale Profiles \- UNT Digital Library, accessed on January 1, 2026, [https://digital.library.unt.edu/ark:/67531/metadc799124/m2/1/high\_res\_d/vol8-no3-151.pdf](https://digital.library.unt.edu/ark:/67531/metadc799124/m2/1/high_res_d/vol8-no3-151.pdf)  
14. The Near-Death Experience Scale: Construction, reliability, and validity \- University of Virginia School of Medicine, accessed on January 1, 2026, [https://med.virginia.edu/perceptual-studies/wp-content/uploads/sites/360/2017/01/NDE8.pdf](https://med.virginia.edu/perceptual-studies/wp-content/uploads/sites/360/2017/01/NDE8.pdf)  
15. Anita M NDE 2766/11068 \- NDERF, accessed on January 1, 2026, [https://www.nderf.org/Experiences/1anita\_m\_nde.html](https://www.nderf.org/Experiences/1anita_m_nde.html)  
16. The Lourdes Medical Cures Revisited \- PMC \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3854941/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3854941/)  
17. List of Approved Lourdes Miracles, accessed on January 1, 2026, [https://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles3.html](https://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles3.html)  
18. news | northkerry \- WordPress.com, accessed on January 1, 2026, [https://northkerry.wordpress.com/tag/news/](https://northkerry.wordpress.com/tag/news/)  
19. How to Write a Case Report \- CARE guidelines, accessed on January 1, 2026, [https://www.care-statement.org/writing-a-case-report](https://www.care-statement.org/writing-a-case-report)  
20. titipata/pubmed\_parser: :clipboard: A Python Parser for PubMed Open-Access XML Subset and MEDLINE XML Dataset \- GitHub, accessed on January 1, 2026, [https://github.com/titipata/pubmed\_parser](https://github.com/titipata/pubmed_parser)  
21. PMC Open Access Subset \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/tools/openftlist/](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/)  
22. OA Web Service API \- PMC \- PubMed Central \- NIH, accessed on January 1, 2026, [https://pmc.ncbi.nlm.nih.gov/tools/oa-service/](https://pmc.ncbi.nlm.nih.gov/tools/oa-service/)  
23. web-scraper · GitHub Topics, accessed on January 1, 2026, [https://github.com/topics/web-scraper](https://github.com/topics/web-scraper)  
24. Lourdes \- List of Approved Miracles \- Miracle Hunter, accessed on January 1, 2026, [http://www.miraclehunter.com/marian\_apparitions/approved\_apparitions/lourdes/miracles1.html](http://www.miraclehunter.com/marian_apparitions/approved_apparitions/lourdes/miracles1.html)  
25. Case Reports \- Human Research Protection Program \- University of Wisconsin–Madison, accessed on January 1, 2026, [https://irb.wisc.edu/manual/investigator-manual/irb-review-requirements-and-application-types/irb-review-requirements-and-application-types/case-reports/](https://irb.wisc.edu/manual/investigator-manual/irb-review-requirements-and-application-types/irb-review-requirements-and-application-types/case-reports/)  
26. Case Report Publication Guidance: IRB Review and HIPAA Compliance, accessed on January 1, 2026, [https://www.hopkinsmedicine.org/institutional-review-board/guidelines-policies/guidelines/case-report](https://www.hopkinsmedicine.org/institutional-review-board/guidelines-policies/guidelines/case-report)  
27. Spontaneous remission : an annotated bibliography \- Frostburg State University, accessed on January 1, 2026, [https://usmai-fsu.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma9910756558208236\&context=L\&vid=01USMAI\_FSU:FSU\_ORT\&lang=en\&search\_scope=DN\_and\_CI\&adaptor=Local%20Search%20Engine\&tab=Everything\&query=sub%2Cexact%2C%20Cancer%20regression%20%2CAND\&mode=advanced\&offset=0](https://usmai-fsu.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma9910756558208236&context=L&vid=01USMAI_FSU:FSU_ORT&lang=en&search_scope=DN_and_CI&adaptor=Local+Search+Engine&tab=Everything&query=sub,exact,+Cancer+regression+,AND&mode=advanced&offset=0)