# Academic Research Report Structure

A comprehensive template for writing professional research reports based on empirical analysis.

---

## Document Architecture

```
TITLE
│
├── ABSTRACT
│   ├── Background (2-3 sentences)
│   ├── Methods (2-3 sentences)
│   ├── Results (3-5 sentences with key statistics)
│   ├── Conclusions (2-3 sentences)
│   └── Keywords (5-8 terms)
│
├── DATA PROVENANCE TABLE
│
├── 1. INTRODUCTION
│   ├── 1.1 Background
│   ├── 1.2 Theoretical Framework
│   └── 1.3 Aims
│
├── 2. METHODS
│   ├── 2.1 Data Sources
│   ├── 2.2 Coding Scheme / Variables
│   ├── 2.3 Classification Criteria (if applicable)
│   └── 2.4 Statistical Analysis
│
├── 3. RESULTS
│   ├── 3.1-3.N Organized by research question or theme
│   └── Each section: narrative + table + finding statement
│
├── 4. DISCUSSION
│   ├── 4.1 Summary of Findings
│   ├── 4.2 Interpretation
│   ├── 4.3 Implications
│   ├── 4.4 Limitations
│   └── 4.5 Future Directions
│
├── 5. CONCLUSION (1-3 paragraphs)
│
├── REFERENCES
│
└── APPENDICES
    ├── Appendix A: Statistical Summary
    └── Appendix B: Data Access
```

---

## 1. Title

### Format
```markdown
# [Descriptive Phrase]: [Subtitle Indicating Methodology or Scope]
```

### Characteristics
- **Descriptive lead phrase** — Names the phenomenon or subject
- **Colon separator** — Divides topic from approach
- **Methodological subtitle** — Indicates analysis type (Statistical Analysis, Discriminant Analysis, Validating X Model)
- **No abbreviations** — Spell out acronyms in title

### Examples
| Good | Why |
|------|-----|
| "The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology" | Clear subject + method |
| "Sequential Structure in Near-Death Experience: Validating the Threefold Path Model" | Phenomenon + theoretical test |
| "Mission-Based Returns: A Discriminant Analysis of Volunteer Soul Phenomenology" | Specific category + methodology |

---

## 2. Abstract

### Structure (5 labeled sections)

```markdown
## Abstract

**Background**: [Context and gap in knowledge. 2-3 sentences.]

**Methods**: [Data source, sample size, coding approach, analysis type. 2-3 sentences.]

**Results**: [Key findings with specific statistics. 3-5 sentences. Include χ², p-values, percentages.]

**Conclusions**: [Interpretation and significance. 2-3 sentences.]

**Keywords**: [term1, term2, term3, term4, term5]
```

### Rules
1. **Background** — State what is known and what question remains
2. **Methods** — Include N, source names, coding method (e.g., "GPT-5.1 structured extraction"), analysis types
3. **Results** — Lead with the primary finding; include 2-4 key statistics with exact values
4. **Conclusions** — State what the data support; avoid hedging
5. **Keywords** — 5-8 terms; include methodology terms and theoretical framework terms

### Example Statistics in Results
- "94.6% of mission-returners had explicit or implied mission commissioning versus 5.8-29.5% in other return categories (χ² = 2845.61, p < 0.0001)"
- "Christians were 2.6× more likely to identify Jesus than non-Christians (14.9% vs. 5.7%)"

---

## 3. Data Provenance Table

### Format
```markdown
## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| [Dataset 1] (n=X) | [Organization name] | [URL](url) |
| [Dataset 2] (n=Y) | [Organization name] | [URL](url) |
| Analysis Code | `[notebook_name].ipynb` | [Repository](url) |
| Structured Data | `[path]/*.json` | [Repository](url) (N files) |
| Extraction Model | [Model name] via [Service] | [Service name] |
```

### Purpose
- **Reproducibility** — Others can access the same data
- **Transparency** — Methods are verifiable
- **Citation** — Proper attribution to data sources

---

## 4. Introduction

### 4.1 Background
- **Opening paragraph**: Establish the phenomenon and its significance
- **Second paragraph**: Review prior research (cite 2-4 key works)
- **Third paragraph**: Identify the gap or contested question

### 4.2 Theoretical Framework
- **Name the framework** — "The Swedenborgian correspondential framework proposes..."
- **Explain the mechanism** — How does the theory work?
- **Generate predictions** — "This framework suggests testable predictions..."
- **List predictions** as numbered items or bullet points

### 4.3 Aims
- **Numbered list** of 3-5 specific research aims
- Begin each with an action verb: "Test," "Quantify," "Validate," "Examine," "Assess"
- Be specific about what will be measured

### Example Aims
```markdown
### 1.3 Aims

1. Test the discriminant validity of mission-based return as a phenomenological category
2. Develop a multi-pathway classification of soul origins
3. Quantify pre-birth indicator profiles by pathway
4. Validate the Volunteer Soul hypothesis through empirical analysis
```

---

## 5. Methods

### 5.1 Data Sources
- **Table format** with Source, Records, Description columns
- Include total N at bottom
- Name specific databases/archives

### 5.2 Coding Scheme / Variables
- **Group variables by category** using bold subheadings
- List each variable with its possible values
- For enums, show the options: "(none, brief, extensive)"

### Example
```markdown
**Return Characteristics**:
- Return reason (earthly_mission, family_responsibility, not_your_time, no_reason_given, other)
- Return choice type (chose_to_return, told_to_return, involuntary, reluctant_return)
- Mission commissioned (yes_explicit, implied, no, not_mentioned)
```

### 5.3 Classification Criteria (if applicable)
- **Table format** with Path/Category and Criteria columns
- Be explicit about inclusion rules

### 5.4 Statistical Analysis
- **Bullet list** of tests used
- Name the test, what it measures, and any corrections applied
- Example: "Chi-square tests for independence between religious background and being identification"

---

## 6. Results

### Organization Principles
1. **One major finding per subsection** (3.1, 3.2, etc.)
2. **Lead with the most important finding**
3. **Each section follows**: Narrative → Table → Finding Statement

### Table Formatting

**Distribution Tables**:
```markdown
| Category | N | % |
|----------|---|---|
| Item A | 1,234 | 45.6% |
| Item B | 567 | 21.0% |
```

**Cross-tabulation Tables**:
```markdown
| Variable | Group A | Group B | Difference | χ² | p |
|----------|---------|---------|------------|-----|---|
| Feature 1 | 45.6% | 23.4% | +22.2% | 123.45 | < 0.0001 |
```

**Comparison Tables**:
```markdown
| Metric | Path A | Path B | Path C |
|--------|--------|--------|--------|
| Feature 1 | 92.6% | 38.1% | 21.4% |
```

### Finding Statements
After each major table, include a bolded interpretive statement:

```markdown
**Critical Finding**: The "earthly mission" return reason achieves **94.6% discriminant accuracy** for mission commissioning. This is not chance association—it represents a coherent phenomenological category.
```

### Statistical Reporting
- Always include: test statistic, df (if applicable), p-value
- Format: "(χ² = 2845.61, df = 15, p < 0.0001)"
- For ratios: "Love:Shame ratio: 137:101 = **1.36:1**"
- For comparisons: "Christians were 2.6× more likely..."

### Highlighting
- **Bold** for critical findings and key statistics
- **Bold** column headers in tables for emphasis
- Use "**Finding:**" or "**Critical Finding:**" prefixes

---

## 7. Discussion

### 4.1 Summary of Findings
- **Numbered or bulleted list** recapping key results
- Include the main statistics
- 5-10 bullet points maximum

### 4.2 Interpretation
- What do the findings mean?
- How do they relate to the theoretical framework?
- Use interpretation tables to align theory with observation:

```markdown
| Theoretical Concept | Observed Pattern |
|--------------------|------------------|
| Concept A | Finding that supports it |
| Concept B | Finding that supports it |
```

### 4.3 Implications
- Practical implications (clinical, educational, etc.)
- Theoretical implications (what this changes about understanding)
- Numbered list format works well

### 4.4 Limitations
- **Numbered list** of 4-6 limitations
- Be specific: "Western sample," "Retrospective reporting," "AI coding"
- Don't over-qualify—state the limitation directly

### 4.5 Future Directions
- **Numbered list** of 3-5 future research directions
- Be specific and actionable
- Examples: "Cross-cultural analysis," "Longitudinal tracking," "Integration with X dataset"

---

## 8. Conclusion

### Format
- **1-3 paragraphs** (typically 150-300 words)
- **First paragraph**: Restate main finding with key statistic
- **Second paragraph**: Broader interpretation/significance
- **Third paragraph** (optional): Practical implication or call to action

### Tone
- Confident but not overreaching
- Ground claims in data: "The data support..." not "This proves..."
- End with significance statement

---

## 9. References

### Format
```markdown
## References

Author, A. B. (Year). *Title of book*. Publisher.

Author, A. B. (Year). Title of article. *Journal Name*, Volume(Issue), pages.
```

### Guidelines
- Alphabetical by first author surname
- Include 5-15 references typical for empirical reports
- Cite foundational works in the field
- Cite theoretical framework sources

---

## 10. Appendices

### Appendix A: Statistical Summary
```markdown
## Appendix A: Statistical Summary

| Test | Variable | χ² | df | p-value |
|------|----------|-----|----|---------| 
| Independence | Var A × Var B | 2845.61 | 15 | < 0.0001 |
```

### Appendix B: Data Access
```markdown
## Appendix B: Data Access

All analysis code and raw data are available at:
- **Repository**: [URL](url)
- **Project Path**: [/path/](url)
- **Analysis Notebook**: [notebook.ipynb](url)
```

### Optional Appendices
- **Appendix C**: Classification exports / data files
- **Appendix D**: Extended methodology
- **Appendix E**: Supplementary figures

---

## Formatting Conventions

### Numbers
- Spell out numbers under 10 in prose: "three stages"
- Use numerals for statistics: "56.5%", "n=443"
- Use commas for thousands: "6,753 records"
- Percentages always with one decimal: "73.4%"

### Statistical Notation
- Chi-square: χ²
- p-values: p < 0.0001 (not p = 0.0000)
- Correlation: r = 0.055
- Effect size: Cramér's V = 0.220
- Sample: n=443 (lowercase for subset), N=6,753 (uppercase for total)

### Tables
- Left-align text columns
- Right-align numeric columns
- Bold column headers
- Include totals where appropriate
- Always include N and %

### Emphasis
- **Bold** for key findings, important terms, emphasis
- *Italics* for book titles, foreign terms, defining terms
- `code` for variable names, file names, paths

### Section Dividers
- Use `---` between major sections (after Abstract, before References, between Appendices)
- Don't overuse—reserve for major structural breaks

---

## Quality Checklist

### Structure
- [ ] Title has descriptive phrase + methodological subtitle
- [ ] Abstract has all 5 labeled sections (Background, Methods, Results, Conclusions, Keywords)
- [ ] Data Provenance table included
- [ ] Introduction has Background, Theoretical Framework, Aims
- [ ] Methods has Data Sources, Coding Scheme, Statistical Analysis
- [ ] Results organized by research question
- [ ] Discussion has Summary, Interpretation, Implications, Limitations, Future Directions
- [ ] Conclusion is 1-3 paragraphs
- [ ] References present
- [ ] At least Statistical Summary appendix included

### Content
- [ ] Abstract Results include 2-4 specific statistics with values
- [ ] Aims are numbered and begin with action verbs
- [ ] Each Results subsection has table + finding statement
- [ ] Statistical tests include test statistic, df, p-value
- [ ] Limitations are specific, not vague
- [ ] Conclusion restates key finding with statistic

### Formatting
- [ ] Tables have consistent structure
- [ ] Numbers formatted correctly (commas, decimals)
- [ ] Bold used for emphasis, not underlining
- [ ] References in consistent format
- [ ] Appendix letters used (A, B, C)
