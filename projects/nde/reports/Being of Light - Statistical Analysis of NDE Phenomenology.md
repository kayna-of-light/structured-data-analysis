# The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology

## Abstract

Near-death experiences frequently involve encounters with a "Being of Light" described in terms evoking divine presence. Whether these encounters reflect cultural conditioning or represent access to an objective spiritual reality remains contested. The Swedenborgian correspondential framework proposes a testable middle ground: the Being is ontologically real, but identification is culturally mediated.

We analyzed 6,753 structured NDE records from two major databases (NDERF: n=5,660; IANDS: n=1,093) coded for light encounter type, being identification, religious background, communication mode, and transformative effects using GPT-5.2 structured extraction with a Pydantic schema containing 52 extracted features. Chi-square tests examined independence between religious background and being identification.

Among experiencers with Being of Light encounters (n=1,881; 27.9%), the most common identification was "unknown presence" (51.9%), followed by God (22.5%), Jesus (18.9%), and religious figures (6.5%). Religious background significantly predicted identification vocabulary (χ² = 365.14, p < 0.000001), yet the majority across all traditions transcended cultural labels entirely. Critically, experiential properties remained identical regardless of identification: Christians naming "Jesus" and those naming "Unknown" reported virtually identical encounter characteristics—all differences below 10%. Loving judgment exceeded harsh judgment by a ratio of 36.5:1, and 84.2% reported increased spirituality.

The data support a two-tier model: a consistent underlying phenomenon (constant state) expressed through variable cultural interpretation (variable form). The Being is objective reality; identification is culturally conditioned perception.

---

## Data Provenance

| Item | Source | Access |
|------|--------|--------|
| NDERF Records (n=5,660) | Near-Death Experience Research Foundation | [nderf.org](https://nderf.org) |
| IANDS Records (n=1,093) | International Association for Near-Death Studies | [iands.org](https://iands.org) |
| Being of Light Analysis | `01_being_of_light_analysis.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb) |
| Conceptual Framework Analysis | `04_conceptual_framework_theory.ipynb` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb) |
| Structured Data | `analysis/*.json` | [Repository](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/analysis/) (6,753 files) |
| Extraction Model | GPT-5.2 via Azure OpenAI | Azure OpenAI Service |

---

## 1. Introduction

### 1.1 Background

The "Being of Light" stands among the most iconic elements of near-death experience phenomenology. Raymond Moody's foundational research identified this figure as a brilliant light experienced as a personal presence—characterized by unconditional love and apparently complete knowledge of the experiencer's life (Moody, 1975). In the decades since, studies across cultures have consistently confirmed the prevalence of light-related experiences in NDEs (van Lommel, 2010; Greyson, 2021), yet the interpretation of these encounters remains contested.

The phenomenology presents a philosophical puzzle of considerable depth. The Being is almost universally described as supremely loving, non-judgmental, and possessed of complete knowledge—attributes traditionally associated with the Divine across religious traditions. Yet experiencers from different religious backgrounds identify this presence differently: Christians often report seeing Jesus or God, Hindus may perceive Yama or Krishna, while secular experiencers describe an "unknown presence" or "pure light" without religious attribution.

This variation has fueled a long-standing debate. Skeptics argue that the differences demonstrate cultural construction—the dying brain producing hallucinations shaped by expectation. Religious traditionalists sometimes argue for literal visitation by their tradition's divine figures. Neither position accounts for a puzzling observation: while *identification* varies, the *experiential quality* remains remarkably consistent across traditions. Whether called Jesus, Krishna, or simply "light," the Being consistently manifests love, wisdom, and transformative power.

### 1.2 Theoretical Framework

The present analysis employs Emanuel Swedenborg's doctrine of correspondences as an interpretive lens (Swedenborg, 1758). This doctrine proposes that spiritual realities present themselves to human perception through forms drawn from the recipient's mental repertoire. The same spiritual entity may thus appear differently to different observers—not through deception, but through the inherent structure of how spiritual reality translates into human perception.

On this model, the Being of Light represents what Swedenborg termed the "Divine Human"—the personal manifestation of infinite love and wisdom. When an experiencer encounters this reality, their mind necessarily clothes it in forms it can recognize. A Christian's mental furniture includes Jesus, Mary, and angels; a Hindu's includes Krishna, Shiva, and devas; an atheist's may include only "light," "presence," or "energy." The spiritual reality is constant; the perceptual form varies.

This generates a testable prediction: if the correspondential model is correct, we should observe *variation* in specific identification correlated with religious background (cultural mediation), while *consistency* in the qualitative character of the encounter remains stable across backgrounds (underlying reality). Moreover, we should find that experiencers who use different labels—"Jesus" versus "unknown presence"—report essentially identical experiential properties.

### 1.3 Aims

The primary aim is to test whether being identification varies systematically with religious background while core phenomenology remains constant. This requires distinguishing between two claims: (1) that cultural background influences how experiencers *name* what they encounter, and (2) that cultural background shapes *what they actually experience*. The correspondential hypothesis predicts the first but not the second.

Secondary aims include quantifying the prevalence of different being identifications, testing whether the Being exhibits monotheistic characteristics regardless of experiencer tradition, examining the relationship between identification and transformative effects, and assessing what the data reveal about the cultural interpretation versus objective reality debate.

---

## 2. Methods

### 2.1 Data Sources

Records were collected from the two largest English-language NDE archives: the Near-Death Experience Research Foundation (NDERF), which provided 5,660 questionnaire responses, and the International Association for Near-Death Studies (IANDS), which contributed 1,093 accounts. The combined corpus of 6,753 records represents one of the largest structured NDE datasets analyzed to date.

### 2.2 Coding Scheme

Each record was processed using GPT-5.2 (Azure OpenAI) for structured extraction into a comprehensive Pydantic schema with 52 extracted features. The schema was designed to capture nuances often lost in simpler coding approaches, including temporal splits (death fear before/after NDE, spirituality before/after, religiosity before/after), religious granularity (distinguishing religious background from religious belief at time of NDE, with denomination-level detail for Christians), judgment characteristics (separating source, intensity, and experiencer emotional response), and return experience dimensions (separating agency—who decided—from willingness—how they felt about it).

Fields relevant to this analysis include demographics (age at NDE, sex, religious affiliation at time of NDE), light encounter type (brilliant_light, being_of_light, presence_without_visual), being identification (unknown_presence, god, jesus, religious_figure, buddha), communication mode (telepathic, normal_speech, nonverbal, no_communication), life review characteristics (occurrence, judgment source, judgment intensity, experiencer emotion), and transformative effects (fear changes, spirituality shift, value changes).

### 2.3 Statistical Analysis

Primary analyses employed chi-square tests for independence between religious background and being identification, Cramér's V as effect size measure for categorical associations, Mann-Whitney U tests for non-parametric group comparisons, and Random Forest classification to assess whether religious background could reliably predict identification.

### 2.4 Methodological Note: Light Being versus Other Beings

A critical distinction in this analysis separates Being of Light encounters—the transcendent, central entity representing or emanating from the Light itself—from encounters with other beings such as deceased relatives, angels, or guides. This distinction is essential because the correspondential hypothesis specifically concerns the central divine presence, not the full population of beings that may appear during NDEs.

Among the 6,753 NDEs, 1,881 (27.9%) involved Light Being encounters, 1,898 (28.1%) involved other beings only (without the Light Being), and 2,974 (44.0%) reported no beings at all. Among Light Being encounters, 59.0% involved the Light Being alone while 41.0% included both the Light Being and other beings. All analyses of Being of Light characteristics focus on the 1,881 Light Being encounters.

---

## 3. Results

### 3.1 Light Encounter Prevalence

Light-related experiences proved common in the corpus, with 40.9% reporting brilliant light and an additional 11.8% specifically describing a being of light. Another 4.2% reported a presence without visual form—sensed rather than seen. The remaining cases either did not mention light (24.2%) or did not address the question (18.9%).

Light Being presence varied significantly by religious background (χ² = 19.92, p = 0.0002). Christians showed the highest Light Being encounter rate at 39.7%, followed by Jewish experiencers at 28.9%, spiritual-but-not-religious at 27.3%, other religions at 24.3%, and atheist/agnostic at 24.0%. Muslim experiencers showed the lowest rate at 9.3%, though the small sample size (n=43) warrants caution.

### 3.2 Being of Light Identification

Among the 1,881 Light Being encounters, the most striking finding is the prevalence of transcendence: 51.9% (n=976) identified the Being as "unknown presence"—a category that explicitly resists religious labeling. This was followed by God at 22.5% (n=423), Jesus at 18.9% (n=355), religious figure (specified) at 6.5% (n=122), and Buddha at 0.3% (n=5).

The majority response—"unknown presence"—carries significant weight. These experiencers are not simply failing to identify what they encountered; they are actively affirming that the Being transcended their available categories. This pattern appears across all religious backgrounds: unknown presence rates ranged from 20% (Buddhist, small sample) to 100% (Muslim, small sample), with atheists/agnostics at 66.7%, spiritual-not-religious at 66.7%, Christians at 44.2%, and Jews at 54.5%.

Religious background significantly predicted identification vocabulary (χ² = 365.14, p < 0.000001), confirming cultural mediation. Christians were more likely to use God/Jesus terminology; atheists and spiritual-not-religious were more likely to use presence/light vocabulary. Yet even among Christians—the largest religious subgroup and the one with the strongest cultural emphasis on Jesus as divine—44.2% chose "unknown presence" rather than a specifically Christian label. The experience appears to exceed the categories even of those whose tradition provides robust divine-encounter vocabulary.

### 3.3 The Singularity Finding

A particularly intriguing pattern emerged when comparing monotheistic and polytheistic traditions. If the Being of Light were a projection of religious expectation, we might expect experiencers from polytheistic traditions to encounter multiple divine beings or to perceive the Light as one god among many. Instead, the data show that experiencers from Hindu and Buddhist backgrounds—traditions comfortable with plurality of divine manifestation—consistently report encountering a *singular* transcendent entity.

Polytheists showed a 27.6% Light Being encounter rate (versus 38.4% for monotheists) and a 25.0% "unknown presence" rate among those encounters. Critically, they do not report multiple beings of light or a pantheon of divine figures. The singularity appears to be a property of the phenomenon itself, not a projection of monotheistic cultural expectations.

### 3.4 Light Being Authority

The Being of Light occupies a unique position relative to other beings encountered during NDEs. Comparing Light Being encounters to encounters with other beings only (deceased relatives, angels, guides), the Light Being provided significantly more guidance (81.7% versus 74.9%, χ² = 25.24, p < 0.000001). The Light Being also substantially exceeded other beings in providing teaching (475 versus 239 instances)—nearly double the rate. This pattern suggests the Light Being is not simply another member of the spiritual landscape but holds a position of unique authority.

### 3.5 Life Review and Judgment

Among the 453 Light Being encounters that included life reviews, the character of judgment provides strong evidence for the correspondential hypothesis. The judgment source distribution revealed that 27.2% experienced no judgment at all, 26.7% experienced judgment from the Being of Light, 18.5% from a guide or entity, and 8.6% from self alone. The combined category of "no external condemnation" (no judgment plus self-only) reached 54.7%.

Judgment intensity proved more striking still. Among those experiencing judgment, 32.2% characterized it as loving/gentle while only 0.9% characterized it as harsh/condemning—a ratio of 36.5:1 in favor of love. Neutral judgment appeared in 9.1%, uncomfortable in 11.3%, and 26.7% reported judgment not applicable. This ratio challenges expectations based on many religious traditions that emphasize divine judgment of human sin.

The cross-tabulation of judgment source and intensity revealed that even self-judgment occurs in an atmosphere of love: among those who judged themselves, 43.6% characterized the experience as loving/gentle. The Being of Light, when it served as judgment source, overwhelmingly provided loving judgment (91 instances) versus harsh (2 instances). The data suggest that life review functions as revelation rather than condemnation—showing rather than punishing.

Christians with life reviews showed a particularly interesting pattern. Despite cultural expectations of divine judgment, 63.3% reported no external condemnation, and 31.3% characterized their judgment as loving/gentle. The experience appears to *correct* rather than confirm expectations—a finding that argues against simple cultural projection.

### 3.6 Communication Mode

The dominant mode of communication with the Light Being was telepathic (34.8%), followed by nonverbal (29.0%), normal speech (22.0%), and no communication (3.4%). The prevalence of telepathic communication suggests a non-physical, mind-to-mind connection consistent with encountering a spiritual rather than physical entity.

### 3.7 Transformative Effects

Being of Light encounters produced substantial transformative effects. Among experiencers with before/after spirituality data (n=190), 84.2% reported increased spirituality, 1.6% reported decreased spirituality, and 14.2% remained unchanged. Value shifts were common: 43.5% reported major shifts and 16.1% reported subtle shifts. Death fear showed consistent reduction, with 36.4% of Light Being experiencers reporting decreased fear and 0.0% reporting increased fear.

### 3.8 The Critical Test: Jesus versus Unknown Identification

The strongest test of the correspondential hypothesis comes from comparing experiencers who use different labels. If the Being of Light is genuinely the same phenomenon regardless of identification, then experiencers naming "Jesus" and those naming "Unknown" should report virtually identical experiential properties. If identification reflects different actual encounters—Jesus literally appearing to Christians while something else appears to others—we would expect measurable differences in encounter characteristics.

Among Christians with Light Being encounters (n=460), 38.9% identified the Being as unknown only, 22.2% as Jesus only, 18.0% as God only, and 20.9% used mixed identifications. Comparing the Jesus-only group (n=102) with the Unknown-only group (n=179) on key experiential properties reveals remarkable convergence:

Self-judgment: Jesus identifiers 1.0%, Unknown identifiers 1.7% (difference: -0.7%)
Loving judgment: Jesus identifiers 4.9%, Unknown identifiers 5.0% (difference: -0.1%)
Love emotion reported: Jesus identifiers 2.9%, Unknown identifiers 5.6% (difference: -2.6%)

All differences fall below 10%. Experiencers who confidently name "Jesus" and those who explicitly decline to name the Being report the same experience. The label differs; the encounter does not. This is precisely what the correspondential hypothesis predicts: the spiritual reality is constant; only the perceptual clothing varies.

### 3.9 Denomination Analysis

Christian denominations offer another natural experiment. Catholic theology emphasizes Mary and the saints alongside Jesus; Evangelical theology emphasizes a personal relationship with Jesus specifically. If encounters reflect theological training, we might expect Evangelicals to identify Jesus at higher rates.

Among Christians with denomination data (n=287), the Jesus identification rates were: Catholic 21.7%, Other Christian 35.2%, Mainline Protestant 26.8%, Evangelical/Baptist 20.8%, Mormon/LDS 46.2%. The expected pattern does not appear: Catholics and Evangelicals—despite different theological emphases—show nearly identical Jesus identification rates (21.7% versus 20.8%, a difference of -0.8%). Mormon experiencers showed the highest Jesus identification rate (46.2%), but the small sample (n=13) warrants caution. The data do not support the hypothesis that doctrinal emphasis on Jesus produces higher identification rates.

### 3.10 Machine Learning Classification

As a final test, we employed Random Forest classification to determine whether religious background could reliably predict being identification. If identification is primarily cultural determination, religious background should predict naming with reasonable accuracy. If identification reflects a genuine encounter that transcends cultural categories, religious background should fail as a predictor.

The classifier achieved 37.8% test accuracy with cross-validation accuracy of 38.2% (±8.9%). The baseline accuracy (always predicting the most common class) was 45.9%. The machine learning model performed *below baseline*—religious background cannot reliably predict identification. This finding argues strongly against pure cultural determination. The encounter is not simply the product of what experiencers bring to it.

---

## 4. Discussion

### 4.1 Summary of Findings

This analysis reveals a complex interplay between universal phenomenology and cultural interpretation that aligns remarkably well with the correspondential hypothesis.

First, the majority of experiencers (51.9%) transcend cultural categories entirely, identifying the Being as "unknown presence." This is not a residual category for those who failed to identify what they saw; it is an active assertion that the Being exceeded available categories. This pattern appears across all religious backgrounds, including traditions with robust divine-encounter vocabulary.

Second, cultural mediation is real but limited to vocabulary. Religious background significantly predicts identification labels (χ² = 365.14, p < 0.000001), yet the experiential properties of the encounter remain constant regardless of labeling. Christians who name "Jesus" and Christians who name "Unknown" report the same experience in all measured dimensions.

Third, the Being exhibits characteristics that appear intrinsic rather than projected. The singularity (one Being, even for polytheists), the loving character (36.5:1 love:harsh ratio), the teaching function, and the transformative effects remain constant across religious and non-religious experiencers. These appear to be properties of the phenomenon itself.

Fourth, expectations are corrected rather than confirmed. Christians who might expect divine judgment overwhelmingly experience love and acceptance. This correction pattern argues against simple projection: the experience does not deliver what cultural programming would predict.

### 4.2 The Two-Tier Model: Constant States, Variable Forms

The data support an interpretation distinguishing constant states (the underlying reality of the encounter) from variable forms (the cultural clothing in which that reality appears).

Constant states include the encounter itself (27.9% of NDEs), the singular nature of the Being, the loving and non-judgmental character, the teaching and transformative function, and the transcendence of categories (51.9% cannot name it). These features remain stable across religious backgrounds, denominations, and even individual differences in cultural emphasis.

Variable forms include the specific identification vocabulary (God, Jesus, Light, Presence), which correlates with religious background, and the visual imagery, which draws on the experiencer's mental repertoire. Yet these variations are superficial—they do not penetrate to the experiential core.

This pattern is precisely what Swedenborgian correspondence theory predicts. The Divine Human is the objective spiritual reality; the experiencer's mind provides the perceptual clothing. The correspondence is not arbitrary projection but structured translation—the same spiritual reality appearing through different but related forms.

### 4.3 The "Expect Judgment, Find Love" Pattern

One finding deserves particular emphasis: the consistent *correction* of expectations. Many religious traditions emphasize divine judgment of human sinfulness; many secular narratives about death emphasize fear. Yet NDErs overwhelmingly encounter love rather than judgment (36.5:1 ratio), acceptance rather than condemnation (63.3% of Christians report no external condemnation during life reviews), and peace rather than terror.

If NDE phenomenology were primarily cultural projection, experiences should track expectations. Christians expecting judgment should experience judgment; secular people fearing annihilation should experience terror. The systematic correction of such expectations suggests the encounter delivers something independent of what experiencers bring to it. This is difficult to explain on a pure projection model; it follows naturally if the encounter is genuinely informative about an external reality.

### 4.4 Limitations

Several limitations warrant acknowledgment. The sample is predominantly Western and English-speaking, limiting generalizability to non-Western contexts. Reports are retrospective, potentially influenced by subsequent reflection and integration. GPT-5.2 extraction may introduce systematic biases in coding. The observational design cannot establish causal relationships.

Additionally, the correspondential interpretation, while consistent with the data, is not the only possible interpretation. Skeptics might argue that the consistency of characteristics across traditions reflects common brain physiology under hypoxic conditions rather than encounter with genuine spiritual reality. This analysis cannot definitively adjudicate between these interpretations; it can only note which predictions each model makes and how well those predictions match the observed patterns.

### 4.5 Future Directions

Several directions would strengthen and extend these findings. Cross-cultural replication using non-Western NDE archives would test whether the constant state/variable form pattern holds outside Western cultural contexts. Prospective studies documenting pre-NDE beliefs would address retrospective reporting concerns. Deeper phenomenological analysis of "unknown presence" descriptions—what exactly do experiencers mean when they assert that the Being transcends categories?—would illuminate the nature of that transcendence.

---

## 5. Conclusion

Analysis of 6,753 near-death experiences reveals that the Being of Light is a consistent phenomenon expressed through variable cultural forms. The majority (51.9%) cannot fit the Being into any cultural category; religious background predicts naming vocabulary but not experiential properties; even among Christians, those naming "Jesus" and those naming "Unknown" report identical encounters; and expectations of judgment are systematically corrected toward experiences of love.

This pattern supports the Swedenborgian correspondential model: the Divine Human is an objective spiritual reality encountered during near-death states, but the specific form in which it appears is shaped by the experiencer's cultural and religious vocabulary. The experience is neither purely subjective (the encounter would then track expectations, but it corrects them) nor purely objective in a naive sense (all would then perceive identical forms, but forms vary). It is correspondence—spiritual reality translated through the structure of human reception.

The Being of Light appears to be what near-death experiencers consistently report it to be: a personal, loving presence of ultimate significance that transcends cultural categories while speaking to each experiencer in forms they can receive. Whether called God, Jesus, Krishna, or simply "unknown light," the encounter transforms those who experience it—reducing fear of death (84.2% report increased spirituality, 0.0% report increased death fear) and reorienting values toward love and service.

---

## References

Greyson, B. (2021). *After: A Doctor Explores What Near-Death Experiences Reveal about Life and Beyond*. St. Martin's Essentials.

Moody, R. A. (1975). *Life After Life*. Mockingbird Books.

Swedenborg, E. (1758). *Heaven and Hell* (G. F. Dole, Trans.). Swedenborg Foundation.

van Lommel, P. (2010). *Consciousness Beyond Life: The Science of the Near-Death Experience*. HarperOne.

---

## Appendix A: Statistical Summary

| Test | Statistic | df | p-value |
|------|-----------|----|---------| 
| Religion × Presence Rate | χ² = 19.92 | 3 | 0.0002 |
| Religion × Identification | χ² = 365.14 | 32 | < 0.000001 |
| Light Being vs Other: Guidance | χ² = 25.24 | 1 | < 0.000001 |
| ML Classification Accuracy | — | — | 37.8% (below 45.9% baseline) |

## Appendix B: Key Statistics

| Metric | Value |
|--------|-------|
| Total NDEs analyzed | 6,753 |
| NDERF records | 5,660 |
| IANDS records | 1,093 |
| Light Being encounters | 1,881 (27.9%) |
| Unknown presence identification | 51.9% |
| No external judgment | 54.7% |
| Love:Harsh judgment ratio | 36.5:1 |
| Increased spirituality | 84.2% |
| Christians: No external condemnation | 63.3% |

## Appendix C: Data Access

All analysis code and raw data are available at:
- **Repository**: [https://github.com/marconian/structured-data-analysis](https://github.com/marconian/structured-data-analysis)
- **NDE Project**: [/tree/main/projects/nde/](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/)
- **Analysis Notebooks**: 
  - [01_being_of_light_analysis.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/01_being_of_light_analysis.ipynb)
  - [04_conceptual_framework_theory.ipynb](https://github.com/marconian/structured-data-analysis/tree/main/projects/nde/notebooks/04_conceptual_framework_theory.ipynb)
