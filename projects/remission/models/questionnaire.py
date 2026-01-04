"""Pydantic schema for structured spontaneous remission case analysis.

This questionnaire is designed to extract both medical "ground truth" and
psycho-spiritual factors from remission case narratives, enabling statistical
analysis of the relationship between spiritual transformation and physical healing.

Based on:
- Kelly Turner's 9 Radical Remission Factors (1,500+ cases)
- Everson & Cole Spontaneous Regression criteria (1966)
- IONS Spontaneous Remission Project
- Lourdes Medical Bureau Lambertini Criteria (7 criteria)
- NCI Best Case Series standards
- mCODE (Minimal Common Oncology Data Elements)
- Schilder et al. Existential Reorganization research
- Swedenborgian correspondential ontology (disease-spirit correspondence)
- Psychoneuroimmunology literature

Data Sources Mapped:
- PMC case reports (medical literature)
- Radical Remission Project survivor stories
- NDERF/IANDS healing-associated cases
- Lourdes Medical Bureau archives

Statistical Analysis Goals:
1. Test causal sequence: Spiritual Transformation → Physical Remission
2. Identify strongest predictors of complete vs partial remission
3. Correlate disease type with psychological/spiritual patterns
4. Validate Turner's 9 Factors across diverse data sources
5. Test correspondential hypothesis (specific disease ↔ specific spiritual state)
"""

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


def _coerce_mention_response(v: Any) -> str:
    """Convert boolean/variant values to MentionResponse strings."""
    if isinstance(v, bool):
        return "yes_explicit" if v else "not_mentioned"
    if isinstance(v, str):
        v_lower = v.lower().strip()
        # Handle common LLM variations
        if v_lower in ("true", "yes", "y", "1"):
            return "yes_explicit"
        if v_lower in ("false", "no", "n", "0", "none"):
            return "not_mentioned"
        if v_lower in ("unknown", "uncertain", "unclear", "n/a", "na"):
            return "not_mentioned"
    return v


class QuestionnaireBaseModel(BaseModel):
    """Shared configuration for all questionnaire models."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# =============================================================================
# SECTION 1: ENUMERATION TYPES
# =============================================================================


class DataSource(str, Enum):
    """Source of the case data."""
    PMC = "pmc"                          # PubMed Central case reports
    RADICAL_REMISSION = "radical_remission"  # RadicalRemission.com
    NDERF = "nderf"                      # Near Death Experience Research Foundation
    IANDS = "iands"                      # International Association for Near-Death Studies
    LOURDES = "lourdes"                  # Lourdes Medical Bureau
    IONS = "ions"                        # Institute of Noetic Sciences
    OTHER = "other"


class MentionResponse(str, Enum):
    """Standard mention detection response."""
    YES_EXPLICIT = "yes_explicit"        # Clearly stated in narrative
    IMPLIED = "implied"                  # Reasonably inferred
    NO = "no"                            # Explicitly absent/denied
    NOT_MENTIONED = "not_mentioned"      # No information either way


class ConfidenceLevel(str, Enum):
    """Confidence in extracted information."""
    HIGH = "high"                        # Direct quote or explicit statement
    MEDIUM = "medium"                    # Strong inference from context
    LOW = "low"                          # Weak inference
    UNCERTAIN = "uncertain"              # Conflicting signals


class VerificationTier(str, Enum):
    """Validation tier based on evidence quality (per ontology doc)."""
    TIER_1_INSTITUTIONAL = "tier_1_institutional"  # Published case report, biopsy+scans, Lourdes verified
    TIER_2_CLINICAL = "tier_2_clinical"            # Detailed medical terminology, doctor names, dates
    TIER_3_DETAILED = "tier_3_detailed"            # Self-reported with specifics (stage, treatment names)
    TIER_4_ANECDOTAL = "tier_4_anecdotal"          # Vague, hearsay, minimal detail


class RemissionCategory(str, Enum):
    """Type of remission per Everson & Cole (1966) + Turner extensions."""
    PURE_SPONTANEOUS = "pure_spontaneous"          # No treatment at all
    INADEQUATE_TREATMENT = "inadequate_treatment"  # Treatment insufficient to explain outcome
    RADICAL_POST_FAILURE = "radical_post_failure"  # After conventional treatment failed
    ANOMALOUS_RESPONSE = "anomalous_response"      # Response statistically exceeds prognosis
    DELAYED_TREATMENT_EFFECT = "delayed_treatment_effect"  # Could be late treatment response
    NOT_DETERMINABLE = "not_determinable"


class DiseaseCategory(str, Enum):
    """Primary disease category for stratification."""
    CANCER = "cancer"
    AUTOIMMUNE = "autoimmune"              # MS, lupus, RA, Crohn's, etc.
    INFECTIOUS = "infectious"              # HIV, hepatitis, TB, etc.
    CARDIOVASCULAR = "cardiovascular"      # Heart disease, stroke sequelae
    NEUROLOGICAL = "neurological"          # Paralysis, epilepsy, neuropathy
    MUSCULOSKELETAL = "musculoskeletal"    # Arthritis, bone disorders
    RESPIRATORY = "respiratory"            # COPD, asthma, pulmonary fibrosis
    ENDOCRINE = "endocrine"                # Diabetes, thyroid disorders
    GASTROINTESTINAL = "gastrointestinal"  # IBD, liver disease (non-cancer)
    RENAL = "renal"                        # Kidney disease (non-cancer)
    DERMATOLOGICAL = "dermatological"      # Psoriasis, eczema, vitiligo
    HEMATOLOGICAL = "hematological"        # Non-cancer blood disorders
    PSYCHIATRIC = "psychiatric"            # Severe mental illness
    CONGENITAL = "congenital"              # Birth defects
    DEGENERATIVE = "degenerative"          # ALS, Parkinson's, Alzheimer's
    CHRONIC_PAIN = "chronic_pain"          # Fibromyalgia, chronic fatigue
    OTHER = "other"
    UNKNOWN = "unknown"


class CancerType(str, Enum):
    """Cancer subtypes (only applicable when disease_category=CANCER)."""
    BREAST = "breast"
    LUNG = "lung"
    COLORECTAL = "colorectal"
    PROSTATE = "prostate"
    PANCREATIC = "pancreatic"
    LIVER_HEPATOCELLULAR = "liver_hepatocellular"
    MELANOMA = "melanoma"
    LYMPHOMA = "lymphoma"
    LEUKEMIA = "leukemia"
    BRAIN_CNS = "brain_cns"
    KIDNEY_RENAL = "kidney_renal"
    OVARIAN = "ovarian"
    CERVICAL = "cervical"
    THYROID = "thyroid"
    BLADDER = "bladder"
    STOMACH_GASTRIC = "stomach_gastric"
    ESOPHAGEAL = "esophageal"
    SARCOMA = "sarcoma"
    NEUROBLASTOMA = "neuroblastoma"
    MESOTHELIOMA = "mesothelioma"
    MULTIPLE_MYELOMA = "multiple_myeloma"
    OTHER_CANCER = "other_cancer"
    NOT_APPLICABLE = "not_applicable"      # Non-cancer cases
    UNKNOWN = "unknown"


class AutoimmuneType(str, Enum):
    """Autoimmune disease subtypes."""
    MULTIPLE_SCLEROSIS = "multiple_sclerosis"
    RHEUMATOID_ARTHRITIS = "rheumatoid_arthritis"
    LUPUS_SLE = "lupus_sle"
    CROHNS_DISEASE = "crohns_disease"
    ULCERATIVE_COLITIS = "ulcerative_colitis"
    PSORIASIS = "psoriasis"
    TYPE_1_DIABETES = "type_1_diabetes"
    HASHIMOTOS = "hashimotos"
    GRAVES_DISEASE = "graves_disease"
    CELIAC = "celiac"
    SJOGRENS = "sjogrens"
    ANKYLOSING_SPONDYLITIS = "ankylosing_spondylitis"
    MYASTHENIA_GRAVIS = "myasthenia_gravis"
    GUILLAIN_BARRE = "guillain_barre"
    OTHER_AUTOIMMUNE = "other_autoimmune"
    NOT_APPLICABLE = "not_applicable"
    UNKNOWN = "unknown"


class InfectiousType(str, Enum):
    """Infectious disease subtypes."""
    HIV_AIDS = "hiv_aids"
    HEPATITIS_B = "hepatitis_b"
    HEPATITIS_C = "hepatitis_c"
    TUBERCULOSIS = "tuberculosis"
    LYME_DISEASE = "lyme_disease"
    SEPSIS = "sepsis"
    MENINGITIS = "meningitis"
    OTHER_VIRAL = "other_viral"
    OTHER_BACTERIAL = "other_bacterial"
    OTHER_PARASITIC = "other_parasitic"
    NOT_APPLICABLE = "not_applicable"
    UNKNOWN = "unknown"


class CancerStage(str, Enum):
    """TNM/AJCC staging."""
    STAGE_0 = "stage_0"                  # Carcinoma in situ
    STAGE_I = "stage_i"                  # Localized
    STAGE_II = "stage_ii"                # Regional spread
    STAGE_III = "stage_iii"              # Extensive regional
    STAGE_IV = "stage_iv"                # Distant metastasis
    RECURRENT = "recurrent"              # Returned after treatment
    METASTATIC = "metastatic"            # Spread to distant sites
    LOCALLY_ADVANCED = "locally_advanced"
    UNKNOWN = "unknown"


class HistologicalGrade(str, Enum):
    """Tumor differentiation grade."""
    GRADE_1_WELL = "grade_1_well"        # Well differentiated (low grade)
    GRADE_2_MODERATE = "grade_2_moderate"  # Moderately differentiated
    GRADE_3_POOR = "grade_3_poor"        # Poorly differentiated (high grade)
    GRADE_4_UNDIFF = "grade_4_undiff"    # Undifferentiated/anaplastic
    NOT_GRADED = "not_graded"
    UNKNOWN = "unknown"


class TreatmentStatus(str, Enum):
    """Conventional treatment relationship to remission."""
    NONE = "none"                        # Never received any treatment
    REFUSED = "refused"                  # Offered but declined
    FAILED = "failed"                    # Completed but cancer progressed
    ABANDONED = "abandoned"              # Started but stopped (side effects, futility)
    INCOMPLETE = "incomplete"            # Did not finish prescribed course
    CONCURRENT = "concurrent"            # Ongoing during remission
    COMPLETED_PRIOR = "completed_prior"  # Finished before remission
    PALLIATIVE_ONLY = "palliative_only"  # Only comfort care received
    NOT_MENTIONED = "not_mentioned"


class TreatmentType(str, Enum):
    """Types of conventional treatment."""
    SURGERY = "surgery"
    CHEMOTHERAPY = "chemotherapy"
    RADIATION = "radiation"
    IMMUNOTHERAPY = "immunotherapy"
    TARGETED_THERAPY = "targeted_therapy"
    HORMONE_THERAPY = "hormone_therapy"
    BONE_MARROW_TRANSPLANT = "bone_marrow_transplant"
    RADIOFREQUENCY_ABLATION = "radiofrequency_ablation"
    CRYOTHERAPY = "cryotherapy"
    TACE = "tace"                        # Transcatheter arterial chemoembolization
    PHOTODYNAMIC = "photodynamic"
    OTHER = "other"


class RemissionType(str, Enum):
    """RECIST-style outcome classification."""
    COMPLETE_REMISSION = "complete_remission"      # NED (No Evidence of Disease)
    PARTIAL_REMISSION = "partial_remission"        # >50% tumor reduction
    STABLE_DISEASE = "stable_disease"              # No progression
    SPONTANEOUS_REGRESSION = "spontaneous_regression"  # Any measurable reduction
    CURE = "cure"                                  # Long-term NED (5+ years)
    NOT_SPECIFIED = "not_specified"


class RemissionSpeed(str, Enum):
    """Speed of the remission event (per Lambertini criteria)."""
    INSTANTANEOUS = "instantaneous"      # <7 days (miraculous/Lourdes criterion)
    RAPID = "rapid"                      # 1-8 weeks
    MODERATE = "moderate"                # 2-6 months
    GRADUAL = "gradual"                  # 6-12 months
    SLOW = "slow"                        # >12 months
    NOT_SPECIFIED = "not_specified"


class RemissionDurability(str, Enum):
    """Long-term outcome of remission."""
    PERMANENT = "permanent"              # No recurrence (5+ years)
    DURABLE = "durable"                  # No recurrence (2-5 years)
    SUSTAINED = "sustained"              # No recurrence (1-2 years)
    TEMPORARY = "temporary"              # Recurrence within 1 year
    RELAPSED = "relapsed"                # Cancer returned
    UNKNOWN = "unknown"                  # Follow-up not available


class VerificationMethod(str, Enum):
    """How remission was confirmed."""
    BIOPSY = "biopsy"
    PET_SCAN = "pet_scan"
    CT_SCAN = "ct_scan"
    MRI = "mri"
    ULTRASOUND = "ultrasound"
    X_RAY = "x_ray"
    BLOOD_MARKERS = "blood_markers"      # PSA, CEA, AFP, CA-125, etc.
    PHYSICAL_EXAM = "physical_exam"
    ENDOSCOPY = "endoscopy"
    SELF_REPORTED = "self_reported"
    PHYSICIAN_STATEMENT = "physician_statement"
    MEDICAL_RECORDS = "medical_records"
    NOT_SPECIFIED = "not_specified"


class DietaryProtocol(str, Enum):
    """Dietary change type (Turner Factor 1)."""
    NONE = "none"
    KETOGENIC = "ketogenic"
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"
    RAW_FOOD = "raw_food"
    JUICING = "juicing"
    FASTING_INTERMITTENT = "fasting_intermittent"
    FASTING_EXTENDED = "fasting_extended"
    MACROBIOTIC = "macrobiotic"
    ANTI_INFLAMMATORY = "anti_inflammatory"
    ORGANIC = "organic"
    SUGAR_FREE = "sugar_free"
    GERSON_THERAPY = "gerson_therapy"
    BUDWIG_PROTOCOL = "budwig_protocol"
    MEDITERRANEAN = "mediterranean"
    ALKALINE = "alkaline"
    ELIMINATION = "elimination"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class SupplementType(str, Enum):
    """Supplement categories (Turner Factor 4)."""
    VITAMIN_C_HIGH_DOSE = "vitamin_c_high_dose"
    VITAMIN_D = "vitamin_d"
    VITAMIN_E = "vitamin_e"
    SELENIUM = "selenium"
    ZINC = "zinc"
    FISH_OIL_OMEGA3 = "fish_oil_omega3"
    CURCUMIN_TURMERIC = "curcumin_turmeric"
    MUSHROOM_EXTRACTS = "mushroom_extracts"  # Reishi, Turkey Tail, etc.
    GREEN_TEA_EGCG = "green_tea_egcg"
    PROBIOTICS = "probiotics"
    DIGESTIVE_ENZYMES = "digestive_enzymes"
    MISTLETOE = "mistletoe"              # Iscador
    ESSIAC_TEA = "essiac_tea"
    CBD_CANNABIS = "cbd_cannabis"
    ARTEMISININ = "artemisinin"
    HERBAL_CHINESE = "herbal_chinese"
    HERBAL_AYURVEDIC = "herbal_ayurvedic"
    HERBAL_OTHER = "herbal_other"
    ANTIOXIDANTS_GENERAL = "antioxidants_general"
    IV_THERAPIES = "iv_therapies"
    OTHER = "other"


class AlternativeTherapyType(str, Enum):
    """Alternative/complementary therapy categories."""
    ACUPUNCTURE = "acupuncture"
    ENERGY_HEALING = "energy_healing"    # Reiki, therapeutic touch, etc.
    MEDITATION = "meditation"
    YOGA = "yoga"
    QIGONG = "qigong"
    HYPNOTHERAPY = "hypnotherapy"
    VISUALIZATION = "visualization"
    PRAYER_THERAPY = "prayer_therapy"
    BIOFEEDBACK = "biofeedback"
    CHIROPRACTIC = "chiropractic"
    NATUROPATHY = "naturopathy"
    HOMEOPATHY = "homeopathy"
    AYURVEDA = "ayurveda"
    TRADITIONAL_CHINESE = "traditional_chinese"
    MASSAGE_THERAPY = "massage_therapy"
    SAUNA_HYPERTHERMIA = "sauna_hyperthermia"
    OZONE_THERAPY = "ozone_therapy"
    COFFEE_ENEMAS = "coffee_enemas"
    DETOX_PROTOCOLS = "detox_protocols"
    LAETRILE = "laetrile"
    OTHER = "other"


class SocialSupportLevel(str, Enum):
    """Level of social support (Turner Factor 7)."""
    STRONG = "strong"                    # Active support network, community
    MODERATE = "moderate"                # Some support
    WEAK = "weak"                        # Minimal support
    ISOLATED = "isolated"                # No apparent support
    DETERIORATED = "deteriorated"        # Support decreased (divorce, conflict)
    IMPROVED = "improved"                # Support increased during illness
    NOT_MENTIONED = "not_mentioned"


class SpiritualPracticeType(str, Enum):
    """Spiritual practice categories (Turner Factor 8)."""
    PRAYER = "prayer"
    MEDITATION_MINDFULNESS = "meditation_mindfulness"
    CHURCH_ATTENDANCE = "church_attendance"
    SCRIPTURE_STUDY = "scripture_study"
    NATURE_CONNECTION = "nature_connection"
    GRATITUDE_PRACTICE = "gratitude_practice"
    FORGIVENESS_PRACTICE = "forgiveness_practice"
    PILGRIMAGE = "pilgrimage"            # Lourdes, etc.
    RETREAT = "retreat"
    SPIRITUAL_COUNSELING = "spiritual_counseling"
    TWELVE_STEP = "twelve_step"
    INDIGENOUS_CEREMONY = "indigenous_ceremony"
    YOGA_SPIRITUAL = "yoga_spiritual"
    BUDDHIST_PRACTICE = "buddhist_practice"
    CONTEMPLATIVE = "contemplative"
    NONE = "none"
    OTHER = "other"


class EmotionalReleaseType(str, Enum):
    """Type of emotional release (Turner Factor 5)."""
    FORGIVENESS = "forgiveness"          # Of self or others
    GRIEF_PROCESSING = "grief_processing"
    ANGER_RELEASE = "anger_release"
    FEAR_CONFRONTATION = "fear_confrontation"
    TRAUMA_HEALING = "trauma_healing"
    RESENTMENT_RELEASE = "resentment_release"
    GUILT_RELEASE = "guilt_release"
    SHAME_RELEASE = "shame_release"
    RECONCILIATION = "reconciliation"
    THERAPY_COUNSELING = "therapy_counseling"
    SUPPORT_GROUP = "support_group"
    JOURNALING = "journaling"
    CRYING_CATHARSIS = "crying_catharsis"
    OTHER = "other"
    NONE = "none"


class PositiveEmotionType(str, Enum):
    """Positive emotions cultivated (Turner Factor 6)."""
    JOY = "joy"
    LOVE = "love"
    GRATITUDE = "gratitude"
    PEACE = "peace"
    HOPE = "hope"
    HUMOR_LAUGHTER = "humor_laughter"
    AWE_WONDER = "awe_wonder"
    COMPASSION = "compassion"
    CONTENTMENT = "contentment"
    ENTHUSIASM = "enthusiasm"


class AnomalousExperienceType(str, Enum):
    """Type of anomalous/transcendent experience linked to remission."""
    NDE = "nde"                          # Near-death experience
    OBE = "obe"                          # Out-of-body experience
    STE = "ste"                          # Spiritually transformative experience
    MYSTICAL_EXPERIENCE = "mystical_experience"
    RELIGIOUS_CONVERSION = "religious_conversion"
    PROFOUND_DREAM = "profound_dream"
    VISION = "vision"
    VOICE_HEARING = "voice_hearing"
    HEALING_SERVICE = "healing_service"  # Church/faith healer event
    SYNCHRONICITY = "synchronicity"
    PRECOGNITION = "precognition"
    ENCOUNTER_DECEASED = "encounter_deceased"
    NONE = "none"
    NOT_MENTIONED = "not_mentioned"


class CurrentStatus(str, Enum):
    """Current patient status at time of report."""
    ALIVE_NED = "alive_ned"              # No Evidence of Disease
    ALIVE_WITH_DISEASE = "alive_with_disease"
    ALIVE_UNKNOWN = "alive_unknown"      # Alive but disease status unknown
    DECEASED_CANCER = "deceased_cancer"
    DECEASED_OTHER = "deceased_other"
    DECEASED_UNKNOWN_CAUSE = "deceased_unknown_cause"
    LOST_TO_FOLLOWUP = "lost_to_followup"
    NOT_SPECIFIED = "not_specified"


class PreIllnessLifePattern(str, Enum):
    """Life patterns before illness onset (for causal analysis)."""
    HIGH_STRESS = "high_stress"
    WORKAHOLIC = "workaholic"
    CAREGIVER_BURNOUT = "caregiver_burnout"
    RELATIONSHIP_CONFLICT = "relationship_conflict"
    SUPPRESSED_EMOTIONS = "suppressed_emotions"
    PEOPLE_PLEASING = "people_pleasing"
    PERFECTIONISM = "perfectionism"
    LOSS_GRIEF = "loss_grief"
    TRAUMA_UNRESOLVED = "trauma_unresolved"
    ISOLATION = "isolation"
    DEPRESSION = "depression"
    ANXIETY = "anxiety"
    ANGER_CHRONIC = "anger_chronic"
    GUILT_CHRONIC = "guilt_chronic"
    LACK_OF_PURPOSE = "lack_of_purpose"
    SPIRITUAL_CRISIS = "spiritual_crisis"
    NONE_IDENTIFIED = "none_identified"
    NOT_MENTIONED = "not_mentioned"


class OrganSystem(str, Enum):
    """Organ systems for correspondential analysis."""
    CARDIOVASCULAR = "cardiovascular"    # Heart ↔ Will/Love
    RESPIRATORY = "respiratory"          # Lungs ↔ Understanding/Truth reception
    DIGESTIVE = "digestive"              # Processing/assimilation
    HEPATIC = "hepatic"                  # Liver ↔ Purification of good
    LYMPHATIC = "lymphatic"              # Immune/defense ↔ Conscience
    NEUROLOGICAL = "neurological"        # Brain ↔ Wisdom/Understanding
    REPRODUCTIVE = "reproductive"        # Generativity
    MUSCULOSKELETAL = "musculoskeletal"  # Bone ↔ Foundation/structural truth
    INTEGUMENTARY = "integumentary"      # Skin ↔ External/boundary
    ENDOCRINE = "endocrine"              # Hormonal balance
    URINARY = "urinary"                  # Elimination
    BLOOD = "blood"                      # Life force
    MULTIPLE = "multiple"
    OTHER = "other"


class BiologicalSex(str, Enum):
    """Biological sex for demographic stratification."""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


class ReligiousBackground(str, Enum):
    """Religious/spiritual background categories."""
    CHRISTIAN_CATHOLIC = "christian_catholic"
    CHRISTIAN_PROTESTANT = "christian_protestant"
    CHRISTIAN_ORTHODOX = "christian_orthodox"
    CHRISTIAN_OTHER = "christian_other"
    JEWISH = "jewish"
    MUSLIM = "muslim"
    HINDU = "hindu"
    BUDDHIST = "buddhist"
    SIKH = "sikh"
    SPIRITUAL_NOT_RELIGIOUS = "spiritual_not_religious"
    AGNOSTIC = "agnostic"
    ATHEIST = "atheist"
    NONE = "none"
    OTHER = "other"
    NOT_MENTIONED = "not_mentioned"


# =============================================================================
# SECTION 2: NESTED MODELS - PATIENT DEMOGRAPHICS
# =============================================================================


class DemographicsSection(QuestionnaireBaseModel):
    """Patient demographic information."""
    
    age_at_diagnosis: Optional[int] = Field(
        None,
        ge=0,
        le=120,
        description="Patient age at initial diagnosis."
    )
    age_at_remission: Optional[int] = Field(
        None,
        ge=0,
        le=120,
        description="Patient age when remission was confirmed."
    )
    sex: BiologicalSex = Field(
        BiologicalSex.NOT_MENTIONED,
        description="Biological sex of the patient."
    )
    geographic_region: Optional[str] = Field(
        None,
        description="Country or region (for cultural stratification)."
    )
    occupation: Optional[str] = Field(
        None,
        description="Occupation if mentioned."
    )
    religious_background: ReligiousBackground = Field(
        ReligiousBackground.NOT_MENTIONED,
        description="Religious/spiritual background."
    )
    religious_background_detail: Optional[str] = Field(
        None,
        description="Specific denomination or detail if mentioned."
    )
    socioeconomic_indicators: Optional[str] = Field(
        None,
        description="Any indicators of socioeconomic status."
    )


# =============================================================================
# SECTION 4: NESTED MODELS - MEDICAL DIAGNOSIS
# =============================================================================


class DiagnosisSection(QuestionnaireBaseModel):
    """Medical diagnosis information (the medical 'ground truth').
    
    Designed to capture diagnoses across all disease categories, with
    disease-specific fields that are optional based on category.
    """
    
    # Primary diagnosis (universal)
    diagnosis_raw: Optional[str] = Field(
        None,
        description="Original diagnosis text as stated in the narrative."
    )
    disease_category: DiseaseCategory = Field(
        DiseaseCategory.UNKNOWN,
        description="Primary disease category (cancer, autoimmune, infectious, etc.)."
    )
    disease_name: Optional[str] = Field(
        None,
        description="Specific disease name as stated (e.g., 'Stage IV melanoma', 'multiple sclerosis', 'HIV')."
    )
    organ_system: OrganSystem = Field(
        OrganSystem.OTHER,
        description="Primary organ system affected (for correspondential analysis)."
    )
    
    # Disease severity (universal)
    severity_description: Optional[str] = Field(
        None,
        description="Description of disease severity (e.g., 'terminal', 'advanced', 'severe', 'relapsing-remitting')."
    )
    considered_terminal: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was the condition considered terminal/incurable?"
    )
    considered_incurable: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was the condition considered incurable by conventional medicine?"
    )
    
    # Prognosis (universal)
    prognosis_given: Optional[str] = Field(
        None,
        description="Prognosis given by doctors (e.g., '6 months to live', 'progressive decline')."
    )
    prognosis_months: Optional[int] = Field(
        None,
        description="Predicted survival/timeline in months if extractable."
    )
    quality_of_life_impact: Optional[str] = Field(
        None,
        description="Impact on quality of life (e.g., 'bedridden', 'wheelchair-bound', 'unable to work')."
    )
    
    # Verification (universal)
    medically_documented: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was the diagnosis medically documented?"
    )
    specialist_diagnosed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was diagnosis made by a specialist?"
    )
    multiple_opinions: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were multiple medical opinions obtained?"
    )
    
    # Lab/diagnostic results (universal)
    lab_tests_mentioned: List[str] = Field(
        default_factory=list,
        description="Lab tests mentioned (e.g., ['blood work', 'MRI', 'biopsy', 'viral load'])."
    )
    lab_values: Optional[str] = Field(
        None,
        description="Specific lab values if mentioned."
    )
    
    # Dates (universal)
    diagnosis_date: Optional[str] = Field(
        None,
        description="Date of diagnosis if mentioned (YYYY-MM or YYYY)."
    )
    diagnosis_year: Optional[int] = Field(
        None,
        description="Year of diagnosis."
    )
    symptom_onset_date: Optional[str] = Field(
        None,
        description="When symptoms first appeared."
    )
    disease_duration_before_healing: Optional[str] = Field(
        None,
        description="How long they had the disease before healing."
    )
    
    # ===========================================
    # CANCER-SPECIFIC FIELDS (when disease_category=CANCER)
    # ===========================================
    cancer_type: CancerType = Field(
        CancerType.NOT_APPLICABLE,
        description="Cancer type (only if disease_category=CANCER)."
    )
    cancer_subtype: Optional[str] = Field(
        None,
        description="Specific cancer subtype (e.g., 'ductal carcinoma', 'small cell')."
    )
    histology: Optional[str] = Field(
        None,
        description="Histological type (e.g., 'adenocarcinoma', 'squamous cell')."
    )
    histological_grade: HistologicalGrade = Field(
        HistologicalGrade.NOT_GRADED,
        description="Tumor differentiation grade."
    )
    cancer_stage: CancerStage = Field(
        CancerStage.UNKNOWN,
        description="Cancer stage at diagnosis (TNM/AJCC)."
    )
    stage_raw: Optional[str] = Field(
        None,
        description="Original staging text (e.g., 'T3N1M0', 'Stage IIIB')."
    )
    primary_site: Optional[str] = Field(
        None,
        description="Primary tumor location."
    )
    metastasis_present: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was metastatic disease present?"
    )
    metastasis_sites: List[str] = Field(
        default_factory=list,
        description="Sites of metastasis."
    )
    tumor_size_cm: Optional[float] = Field(
        None,
        description="Tumor size in centimeters."
    )
    tumor_count: Optional[int] = Field(
        None,
        description="Number of tumors."
    )
    lymph_node_involvement: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was lymph node involvement mentioned?"
    )
    biopsy_confirmed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was cancer biopsy-confirmed?"
    )
    tumor_markers: List[str] = Field(
        default_factory=list,
        description="Tumor markers (e.g., ['PSA', 'CEA', 'CA-125', 'AFP'])."
    )
    tumor_marker_values: Optional[str] = Field(
        None,
        description="Specific tumor marker values."
    )
    
    # ===========================================
    # AUTOIMMUNE-SPECIFIC FIELDS
    # ===========================================
    autoimmune_type: AutoimmuneType = Field(
        AutoimmuneType.NOT_APPLICABLE,
        description="Autoimmune disease type (only if disease_category=AUTOIMMUNE)."
    )
    autoimmune_antibodies: List[str] = Field(
        default_factory=list,
        description="Autoantibodies mentioned (e.g., ['ANA', 'anti-dsDNA', 'RF'])."
    )
    flare_pattern: Optional[str] = Field(
        None,
        description="Pattern of flares/remissions before healing."
    )
    
    # ===========================================
    # INFECTIOUS-SPECIFIC FIELDS  
    # ===========================================
    infectious_type: InfectiousType = Field(
        InfectiousType.NOT_APPLICABLE,
        description="Infectious disease type (only if disease_category=INFECTIOUS)."
    )
    pathogen: Optional[str] = Field(
        None,
        description="Specific pathogen if mentioned."
    )
    viral_load: Optional[str] = Field(
        None,
        description="Viral load if mentioned."
    )
    
    # ===========================================
    # NEUROLOGICAL-SPECIFIC FIELDS
    # ===========================================
    neurological_deficits: List[str] = Field(
        default_factory=list,
        description="Specific neurological deficits (e.g., ['paralysis', 'blindness', 'seizures'])."
    )
    mobility_status: Optional[str] = Field(
        None,
        description="Mobility status before healing (e.g., 'wheelchair-bound', 'bedridden')."
    )
    
    # ===========================================
    # CARDIOVASCULAR-SPECIFIC FIELDS
    # ===========================================
    cardiac_function: Optional[str] = Field(
        None,
        description="Cardiac function measures (e.g., 'ejection fraction 20%')."
    )
    vascular_condition: Optional[str] = Field(
        None,
        description="Vascular condition details."
    )


# =============================================================================
# SECTION 5: NESTED MODELS - TREATMENT HISTORY
# =============================================================================


class TreatmentSection(QuestionnaireBaseModel):
    """Treatment history (to establish 'spontaneous' nature of remission)."""
    
    # Overall treatment status
    conventional_status: TreatmentStatus = Field(
        TreatmentStatus.NOT_MENTIONED,
        description="Status of conventional treatment relative to remission."
    )
    
    # Treatment details
    treatments_received: List[TreatmentType] = Field(
        default_factory=list,
        description="List of conventional treatments received."
    )
    treatments_raw: Optional[str] = Field(
        None,
        description="Raw treatment description from narrative."
    )
    
    # Specific treatments
    surgery_performed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was surgery performed?"
    )
    surgery_type: Optional[str] = Field(
        None,
        description="Type of surgery (e.g., 'mastectomy', 'prostatectomy', 'resection')."
    )
    surgery_outcome: Optional[str] = Field(
        None,
        description="Outcome of surgery (complete removal, partial, margins positive, etc.)."
    )
    
    chemotherapy_received: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was chemotherapy received?"
    )
    chemotherapy_drugs: List[str] = Field(
        default_factory=list,
        description="Specific chemotherapy drugs if mentioned."
    )
    chemotherapy_cycles: Optional[int] = Field(
        None,
        description="Number of chemotherapy cycles if mentioned."
    )
    chemotherapy_response: Optional[str] = Field(
        None,
        description="Response to chemotherapy (worked/failed/partial/side effects)."
    )
    
    radiation_received: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was radiation therapy received?"
    )
    radiation_site: Optional[str] = Field(
        None,
        description="Site of radiation treatment."
    )
    
    immunotherapy_received: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was immunotherapy received?"
    )
    
    hormone_therapy_received: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was hormone therapy received?"
    )
    
    # Treatment timing relative to remission
    treatment_to_remission_months: Optional[int] = Field(
        None,
        description="Months between last treatment and remission observation."
    )
    treatment_stopped_reason: Optional[str] = Field(
        None,
        description="Why treatment was stopped (completed, failed, side effects, refused)."
    )
    
    # Alternative treatments
    alternative_treatments: List[AlternativeTherapyType] = Field(
        default_factory=list,
        description="Alternative/complementary therapies used."
    )
    alternative_treatments_raw: Optional[str] = Field(
        None,
        description="Raw description of alternative treatments."
    )
    
    # Supplements (Turner Factor 4)
    supplements_used: List[SupplementType] = Field(
        default_factory=list,
        description="Supplements mentioned (Turner Factor 4)."
    )
    supplements_raw: Optional[str] = Field(
        None,
        description="Raw supplement list from narrative."
    )


# =============================================================================
# SECTION 6: NESTED MODELS - REMISSION OUTCOME
# =============================================================================


class RemissionOutcomeSection(QuestionnaireBaseModel):
    """The remission event itself - the core outcome variable."""
    
    # Remission classification
    remission_type: RemissionType = Field(
        RemissionType.NOT_SPECIFIED,
        description="Type of remission achieved (RECIST-style)."
    )
    remission_category: RemissionCategory = Field(
        RemissionCategory.NOT_DETERMINABLE,
        description="Category per Everson & Cole / Turner definitions."
    )
    
    # Temporal characteristics
    remission_speed: RemissionSpeed = Field(
        RemissionSpeed.NOT_SPECIFIED,
        description="How quickly remission occurred."
    )
    time_to_remission_raw: Optional[str] = Field(
        None,
        description="Time from intervention/trigger to remission as stated."
    )
    time_to_remission_days: Optional[int] = Field(
        None,
        description="Days from trigger to confirmed remission."
    )
    remission_date: Optional[str] = Field(
        None,
        description="Date remission was confirmed (YYYY-MM or YYYY)."
    )
    remission_year: Optional[int] = Field(
        None,
        description="Year of remission."
    )
    
    # Verification
    verification_methods: List[VerificationMethod] = Field(
        default_factory=list,
        description="How remission was verified."
    )
    verification_detail: Optional[str] = Field(
        None,
        description="Details of verification (specific scans, doctor quotes, etc.)."
    )
    before_after_imaging: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were before AND after imaging studies mentioned?"
    )
    before_after_biomarkers: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were before AND after biomarker values mentioned?"
    )
    physician_confirmed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did a physician explicitly confirm the remission?"
    )
    physician_quote: Optional[str] = Field(
        None,
        description="Direct quote from physician about the remission."
    )
    
    # Biological specificity
    tumor_response: Optional[str] = Field(
        None,
        description="Specific tumor response (e.g., '70% shrinkage', 'disappeared', 'necrotic')."
    )
    tumor_size_change: Optional[str] = Field(
        None,
        description="Change in tumor size (e.g., '5cm to undetectable')."
    )
    biomarker_normalization: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did biomarkers return to normal?"
    )
    biomarker_trajectory: Optional[str] = Field(
        None,
        description="Biomarker trajectory (e.g., 'PSA 33 → 0.1')."
    )
    tissue_regeneration: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was tissue regeneration mentioned (bone regrowth, organ repair)?"
    )
    tissue_regeneration_detail: Optional[str] = Field(
        None,
        description="Details of tissue regeneration if mentioned."
    )
    
    # Durability
    durability: RemissionDurability = Field(
        RemissionDurability.UNKNOWN,
        description="Long-term durability of remission."
    )
    follow_up_duration_months: Optional[int] = Field(
        None,
        description="Months of follow-up documented."
    )
    follow_up_duration_raw: Optional[str] = Field(
        None,
        description="Follow-up duration as stated (e.g., '27 years later')."
    )
    recurrence_occurred: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did recurrence occur?"
    )
    recurrence_timing: Optional[str] = Field(
        None,
        description="When recurrence occurred if applicable."
    )
    
    # Current status
    current_status: CurrentStatus = Field(
        CurrentStatus.NOT_SPECIFIED,
        description="Patient status at time of report/update."
    )
    years_since_diagnosis: Optional[int] = Field(
        None,
        description="Years survived since diagnosis."
    )
    years_since_remission: Optional[int] = Field(
        None,
        description="Years since remission was confirmed."
    )


# =============================================================================
# SECTION 7: NESTED MODELS - TURNER'S 9 RADICAL REMISSION FACTORS
# =============================================================================


class TurnerFactorsSection(QuestionnaireBaseModel):
    """Kelly Turner's 9 Radical Remission Factors - the core psycho-spiritual variables.
    
    Based on Turner's analysis of 1,500+ radical remission cases, these 9 factors
    were present in virtually all cases. 7 of 9 are psycho-spiritual (77%).
    """
    
    # FACTOR 1: Radically changing diet
    factor_diet_change: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 1: Did they make significant dietary changes?"
    )
    dietary_protocols: List[DietaryProtocol] = Field(
        default_factory=list,
        description="Specific dietary protocols adopted."
    )
    diet_details: Optional[str] = Field(
        None,
        description="Specific dietary details mentioned."
    )
    diet_timing: Optional[str] = Field(
        None,
        description="When diet change was implemented relative to diagnosis/treatment."
    )
    
    # FACTOR 2: Taking control of your health
    factor_agency: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 2: Did they take control of their health decisions?"
    )
    agency_examples: List[str] = Field(
        default_factory=list,
        description="Examples of taking control (research, second opinions, refusing treatment)."
    )
    agency_details: Optional[str] = Field(
        None,
        description="How they took control."
    )
    refused_recommended_treatment: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they refuse a recommended treatment?"
    )
    sought_alternatives: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they actively seek alternative approaches?"
    )
    
    # FACTOR 3: Following intuition
    factor_intuition: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 3: Did they follow inner guidance/intuition?"
    )
    intuition_examples: List[str] = Field(
        default_factory=list,
        description="Examples of intuitive guidance followed."
    )
    intuition_details: Optional[str] = Field(
        None,
        description="Specific intuitive guidance mentioned."
    )
    intuition_about_healing: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they have intuitive sense they would heal?"
    )
    
    # FACTOR 4: Using herbs and supplements
    factor_supplements: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 4: Did they use herbs/supplements?"
    )
    # (supplement details captured in TreatmentSection)
    
    # FACTOR 5: Releasing suppressed emotions
    factor_emotional_release: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 5: Did they release suppressed emotions?"
    )
    emotional_release_types: List[EmotionalReleaseType] = Field(
        default_factory=list,
        description="Types of emotional release (forgiveness, grief, anger, etc.)."
    )
    emotional_release_details: Optional[str] = Field(
        None,
        description="Description of emotional release process."
    )
    forgiveness_self: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was self-forgiveness mentioned?"
    )
    forgiveness_others: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was forgiving others mentioned?"
    )
    specific_person_forgiven: Optional[str] = Field(
        None,
        description="Specific relationship forgiven (parent, spouse, etc.)."
    )
    trauma_addressed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was past trauma specifically addressed?"
    )
    
    # FACTOR 6: Increasing positive emotions
    factor_positive_emotions: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 6: Did they increase positive emotions?"
    )
    positive_emotion_types: List[PositiveEmotionType] = Field(
        default_factory=list,
        description="Types of positive emotions cultivated (joy, love, gratitude, etc.)."
    )
    positive_emotion_practices: List[str] = Field(
        default_factory=list,
        description="Practices used to cultivate positive emotions."
    )
    gratitude_practice: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was gratitude practice specifically mentioned?"
    )
    humor_laughter: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was humor/laughter mentioned as healing factor?"
    )
    
    # FACTOR 7: Embracing social support
    factor_social_support: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 7: Did they embrace social support?"
    )
    social_support_level: SocialSupportLevel = Field(
        SocialSupportLevel.NOT_MENTIONED,
        description="Level of social support."
    )
    support_sources: List[str] = Field(
        default_factory=list,
        description="Sources of support (family, friends, support group, church, etc.)."
    )
    support_group_participation: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they participate in a support group?"
    )
    relationship_improvement: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did relationships improve during illness?"
    )
    
    # FACTOR 8: Deepening spiritual connection
    factor_spiritual_connection: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 8: Did they deepen spiritual connection?"
    )
    spiritual_practices: List[SpiritualPracticeType] = Field(
        default_factory=list,
        description="Spiritual practices mentioned."
    )
    spiritual_practices_raw: Optional[str] = Field(
        None,
        description="Raw description of spiritual practices."
    )
    prayer_mentioned: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was prayer specifically mentioned?"
    )
    meditation_mentioned: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was meditation specifically mentioned?"
    )
    faith_strengthened: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was strengthening of faith mentioned?"
    )
    divine_intervention_belief: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they attribute healing to divine intervention?"
    )
    
    # FACTOR 9: Having strong reasons for living
    factor_purpose: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Factor 9: Did they have strong reasons for living?"
    )
    purpose_sources: List[str] = Field(
        default_factory=list,
        description="Sources of purpose (children, mission, unfinished work, etc.)."
    )
    purpose_details: Optional[str] = Field(
        None,
        description="What gave them purpose."
    )
    will_to_live: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was strong will to live explicitly mentioned?"
    )
    life_mission_discovered: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they discover a new life mission?"
    )
    
    # Aggregate factor count
    factors_present_count: Optional[int] = Field(
        None,
        ge=0,
        le=9,
        description="Number of Turner factors clearly present (0-9)."
    )


# =============================================================================
# SECTION 8: NESTED MODELS - PRE-ILLNESS STATE (CAUSAL ANALYSIS)
# =============================================================================


class PreIllnessStateSection(QuestionnaireBaseModel):
    """Pre-illness psychological/spiritual state for causal sequence analysis.
    
    Tests the hypothesis that specific spiritual/psychological states
    precede (and may contribute to) specific diseases.
    """
    
    # Life patterns before illness
    pre_illness_patterns: List[PreIllnessLifePattern] = Field(
        default_factory=list,
        description="Psychological/life patterns identified before illness."
    )
    pre_illness_description: Optional[str] = Field(
        None,
        description="Description of life situation before diagnosis."
    )
    
    # Stress and trauma
    high_stress_period: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was diagnosis preceded by high-stress period?"
    )
    stress_description: Optional[str] = Field(
        None,
        description="Description of stress if mentioned."
    )
    major_loss_event: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was there a major loss before diagnosis (death, divorce, job)?"
    )
    loss_description: Optional[str] = Field(
        None,
        description="Description of loss event."
    )
    unresolved_conflict: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was unresolved conflict mentioned?"
    )
    conflict_description: Optional[str] = Field(
        None,
        description="Nature of unresolved conflict."
    )
    
    # Emotional patterns
    suppressed_emotions: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were suppressed emotions mentioned as pre-illness pattern?"
    )
    chronic_resentment: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was chronic resentment mentioned?"
    )
    chronic_guilt: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was chronic guilt mentioned?"
    )
    chronic_fear: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was chronic fear/anxiety mentioned?"
    )
    people_pleasing: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was people-pleasing pattern mentioned?"
    )
    self_neglect: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was self-neglect mentioned?"
    )
    
    # Authenticity
    living_inauthentically: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were they living against their true self before illness?"
    )
    inauthenticity_details: Optional[str] = Field(
        None,
        description="Description of inauthentic living."
    )
    
    # Spiritual state
    spiritual_disconnection: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was spiritual disconnection mentioned before illness?"
    )
    lack_of_purpose: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was lack of purpose mentioned before illness?"
    )
    
    # Patient's own causal attribution
    patient_causal_belief: Optional[str] = Field(
        None,
        description="What did the patient believe caused their cancer?"
    )


# =============================================================================
# SECTION 9: NESTED MODELS - EXISTENTIAL SHIFT (SCHILDER ET AL.)
# =============================================================================


class ExistentialShiftSection(QuestionnaireBaseModel):
    """Existential reorganization markers (Schilder et al. research).
    
    Research shows spontaneous regression often preceded by specific
    psychological shifts toward autonomy, truth-telling, and congruence.
    """
    
    # Core existential shifts
    identity_shift: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Shift from ego/self-focus to unity/love/interconnection."
    )
    identity_shift_description: Optional[str] = Field(
        None,
        description="Description of identity shift."
    )
    
    authenticity_shift: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Started living true to self vs. pleasing others."
    )
    authenticity_details: Optional[str] = Field(
        None,
        description="How authenticity changed."
    )
    
    fear_to_love_shift: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Dissolution of fear (especially fear of death)."
    )
    fear_of_death_released: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was fear of death specifically released?"
    )
    
    surrender_event: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Moment of 'giving up' control to higher power."
    )
    surrender_description: Optional[str] = Field(
        None,
        description="Description of surrender moment."
    )
    
    # Locus of control
    internal_locus_shift: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Shift from external to internal locus of control."
    )
    
    # Time orientation
    present_moment_focus: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Shift to present-moment focus (vs. past/future worry)."
    )
    
    # Acceptance
    acceptance_of_mortality: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Acceptance of possibility of death."
    )
    acceptance_paradox: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did accepting death paradoxically enable living?"
    )
    
    # Transformation narrative
    transformation_narrative: Optional[str] = Field(
        None,
        description="Patient's description of the existential shift."
    )
    pivot_point_moment: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was there a specific pivot point moment?"
    )
    pivot_point_description: Optional[str] = Field(
        None,
        description="Description of the pivot point moment."
    )
    
    # Temporal sequence (CRITICAL for causal inference)
    transformation_preceded_healing: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did spiritual/psychological transformation clearly PRECEDE physical healing?"
    )
    transformation_timing: Optional[str] = Field(
        None,
        description="Timing of transformation relative to physical change."
    )
    
    # Life changes as result
    major_life_changes: List[str] = Field(
        default_factory=list,
        description="Major life changes made (quit job, ended relationship, moved, etc.)."
    )
    relationships_transformed: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were relationships fundamentally transformed?"
    )
    priorities_shifted: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were life priorities shifted?"
    )


# =============================================================================
# SECTION 10: NESTED MODELS - ANOMALOUS EXPERIENCE LINK
# =============================================================================


class AnomalousExperienceSection(QuestionnaireBaseModel):
    """Anomalous/transcendent experience linked to remission.
    
    Note: This section captures whether such experiences occurred and their
    relationship to healing, NOT detailed NDE phenomenology (separate project).
    """
    
    # Experience occurred
    has_anomalous_experience: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was there an anomalous/transcendent experience?"
    )
    experience_type: AnomalousExperienceType = Field(
        AnomalousExperienceType.NOT_MENTIONED,
        description="Type of anomalous experience."
    )
    experience_description: Optional[str] = Field(
        None,
        description="Brief description of the experience."
    )
    
    # Temporal relationship to healing
    experience_timing: Optional[str] = Field(
        None,
        description="When experience occurred relative to diagnosis/healing."
    )
    experience_preceded_healing: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did the experience precede physical healing?"
    )
    
    # Impact on healing
    attributed_to_healing: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did patient attribute healing to this experience?"
    )
    received_healing_message: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they receive a message about healing during experience?"
    )
    message_content: Optional[str] = Field(
        None,
        description="Content of message if received."
    )
    
    # External healing event
    healing_service_attended: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they attend a healing service/faith healer?"
    )
    pilgrimage: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did they go on a healing pilgrimage (Lourdes, etc.)?"
    )
    pilgrimage_location: Optional[str] = Field(
        None,
        description="Location of pilgrimage if applicable."
    )
    
    # External intercession
    others_praying: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were others praying for them?"
    )
    prayer_group: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was organized prayer (prayer chain, group) mentioned?"
    )


# =============================================================================
# SECTION 11: NESTED MODELS - CORRESPONDENTIAL MARKERS (SWEDENBORGIAN)
# =============================================================================


class CorrespondentialMarkersSection(QuestionnaireBaseModel):
    """Disease-spirit correspondence markers (Swedenborgian framework).
    
    Tests the hypothesis that specific diseases correspond to specific
    spiritual/psychological states, and that resolution of the spiritual
    state precedes resolution of the physical disease.
    """
    
    # Cancer ↔ Proprium (self-serving ego) correspondence
    proprium_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of self-serving ego patterns before illness."
    )
    proprium_description: Optional[str] = Field(
        None,
        description="Description of proprium/ego patterns."
    )
    proprium_dissolved: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was ego dissolution part of healing?"
    )
    
    # Autoimmune ↔ Self-attack/guilt correspondence
    self_attack_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of guilt/self-blame/self-attack before illness."
    )
    self_attack_description: Optional[str] = Field(
        None,
        description="Description of self-attack patterns."
    )
    self_acceptance_achieved: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was self-acceptance part of healing?"
    )
    
    # Heart ↔ Closed will/love correspondence
    closed_will_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of emotional hardening/bitterness before illness."
    )
    closed_will_description: Optional[str] = Field(
        None,
        description="Description of closed heart patterns."
    )
    heart_opened: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was opening to love part of healing?"
    )
    
    # Liver ↔ Purification/anger correspondence
    liver_anger_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of chronic anger/blocked purification."
    )
    anger_released: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was anger release part of healing?"
    )
    
    # Brain/CNS ↔ Truth/understanding correspondence
    truth_blockage_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of denial/truth avoidance before illness."
    )
    truth_accepted: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was truth acceptance part of healing?"
    )
    
    # Bone ↔ Foundation/structural truth correspondence
    foundation_indicators: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Evidence of foundational life issues before illness."
    )
    foundation_rebuilt: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was rebuilding life foundation part of healing?"
    )
    
    # Overall correspondence match
    disease_spirit_match: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Does disease type match expected spiritual correspondence?"
    )
    correspondence_notes: Optional[str] = Field(
        None,
        description="Notes on disease-spirit correspondence."
    )
    
    # Resolution sequence
    spiritual_resolution_preceded: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Did spiritual resolution clearly precede physical healing?"
    )
    resolution_type: Optional[str] = Field(
        None,
        description="Type of spiritual resolution that preceded healing."
    )


# =============================================================================
# SECTION 12: NESTED MODELS - VALIDATION & CONFIDENCE
# =============================================================================


class ValidationSection(QuestionnaireBaseModel):
    """Case validation and confidence metrics for statistical weighting."""
    
    # Verification tier
    verification_tier: VerificationTier = Field(
        VerificationTier.TIER_4_ANECDOTAL,
        description="Evidence quality tier (1=highest, 4=lowest)."
    )
    
    # Detail density
    medical_detail_density: Optional[str] = Field(
        None,
        description="Assessment of medical terminology density (high/medium/low)."
    )
    medical_detail_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Medical detail score (0-100)."
    )
    
    # Specific verification markers
    physician_named: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was treating physician named?"
    )
    hospital_named: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Was hospital/institution named?"
    )
    dates_specific: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were specific dates provided?"
    )
    treatment_names_specific: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Were specific treatment/drug names provided?"
    )
    
    # Lambertini criteria (for miraculous healings)
    lambertini_serious_disease: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 1: Serious, incurable disease?"
    )
    lambertini_medically_documented: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 2: Known/recorded by medicine?"
    )
    lambertini_organic: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 3: Organic/lesional (not psychiatric)?"
    )
    lambertini_no_treatment: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 4: No adequate treatment received?"
    )
    lambertini_sudden: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 5: Cure was sudden/instantaneous?"
    )
    lambertini_complete: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 6: Complete cure (no residual)?"
    )
    lambertini_lasting: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Lambertini 7: Lasting/definitive (no relapse)?"
    )
    lambertini_criteria_count: Optional[int] = Field(
        None,
        ge=0,
        le=7,
        description="Number of Lambertini criteria met (0-7)."
    )
    
    # Statistical improbability
    statistical_improbability_notes: Optional[str] = Field(
        None,
        description="Notes on statistical improbability of this remission."
    )
    exceeds_prognosis: MentionResponse = Field(
        MentionResponse.NOT_MENTIONED,
        description="Does outcome significantly exceed given prognosis?"
    )
    
    # Data quality
    narrative_coherence: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Narrative coherence score (0-100)."
    )
    extraction_confidence: ConfidenceLevel = Field(
        ConfidenceLevel.UNCERTAIN,
        description="Confidence in extracted data accuracy."
    )
    extraction_notes: Optional[str] = Field(
        None,
        description="Notes on extraction challenges or uncertainties."
    )


# =============================================================================
# SECTION 13: ROOT RESPONSE MODEL (LLM OUTPUT)
# =============================================================================


class RemissionAnalysisResponse(QuestionnaireBaseModel):
    """Complete structured response for remission case analysis.
    
    This schema is designed for LLM extraction from narrative text.
    ALL fields should be answerable based on the case narrative content.
    
    Pipeline metadata (source URL, scrape date, file paths, PDF availability, etc.)
    is handled separately in AnalysisOutputPayload, not here.
    
    Analysis dimensions:
    1. Demographics - Patient characteristics from narrative
    2. Diagnosis - Medical ground truth as described
    3. Treatment - Conventional and alternative treatments mentioned
    4. Remission outcome - Nature and verification of healing
    5. Turner factors - 9 Radical Remission factors
    6. Pre-illness patterns - Psychological state before illness
    7. Existential transformation - Schilder et al. markers
    8. Anomalous experience - Transcendent experiences linked to healing
    9. Correspondential markers - Disease-spirit patterns
    10. Validation - Internal consistency and detail quality
    """
    
    # Demographics (extractable from narrative)
    demographics: DemographicsSection = Field(
        ...,
        description="Patient demographic information as described in narrative."
    )
    
    # Medical sections
    diagnosis: DiagnosisSection = Field(
        ...,
        description="Medical diagnosis information (the 'ground truth')."
    )
    treatment: TreatmentSection = Field(
        ...,
        description="Treatment history and alternatives used."
    )
    remission_outcome: RemissionOutcomeSection = Field(
        ...,
        description="The remission event and verification."
    )
    
    # Psycho-spiritual factors
    turner_factors: TurnerFactorsSection = Field(
        ...,
        description="Kelly Turner's 9 Radical Remission Factors."
    )
    pre_illness_state: PreIllnessStateSection = Field(
        ...,
        description="Pre-illness psychological/spiritual state."
    )
    existential_shift: ExistentialShiftSection = Field(
        ...,
        description="Existential reorganization markers (Schilder et al.)."
    )
    
    # Anomalous experience
    anomalous_experience: AnomalousExperienceSection = Field(
        ...,
        description="Transcendent experience linked to remission."
    )
    
    # Correspondential analysis
    correspondential_markers: CorrespondentialMarkersSection = Field(
        ...,
        description="Disease-spirit correspondence indicators."
    )
    
    # Validation (LLM assesses internal consistency)
    validation: ValidationSection = Field(
        ...,
        description="Case validation and confidence metrics."
    )
    
    # Summary fields (LLM synthesis)
    case_summary: Optional[str] = Field(
        None,
        description="Brief narrative summary of the case (1-3 sentences)."
    )
    key_healing_factors: List[str] = Field(
        default_factory=list,
        description="Primary factors identified as contributing to healing."
    )
    unique_features: List[str] = Field(
        default_factory=list,
        description="Any unique or unusual features of this case."
    )
    analysis_notes: Optional[str] = Field(
        None,
        description="LLM notes on ambiguities or uncertainties in the narrative."
    )
    
    # Flags for statistical filtering (LLM determines from narrative)
    
    # CRITICAL: First filter - is this even a human case?
    is_human_case: bool = Field(
        False,
        description="Is this a HUMAN case study? False if animal study, in vitro, or unclear."
    )
    
    disease_category_flag: DiseaseCategory = Field(
        DiseaseCategory.UNKNOWN,
        description="Primary disease category for filtering."
    )
    is_cancer_case: bool = Field(
        False,
        description="Is this a cancer case?"
    )
    is_autoimmune_case: bool = Field(
        False,
        description="Is this an autoimmune case?"
    )
    is_infectious_case: bool = Field(
        False,
        description="Is this an infectious disease case?"
    )
    is_neurological_case: bool = Field(
        False,
        description="Is this a neurological case?"
    )
    is_verified_remission: bool = Field(
        False,
        description="Based on narrative, is remission verified by medical documentation?"
    )
    is_pure_spontaneous: bool = Field(
        False,
        description="Based on narrative, is this pure spontaneous (no conventional treatment)?"
    )
    is_considered_incurable: bool = Field(
        False,
        description="Based on narrative, was the condition considered incurable?"
    )
    has_transformation_narrative: bool = Field(
        False,
        description="Does the narrative include psychological/spiritual transformation?"
    )
    has_temporal_sequence: bool = Field(
        False,
        description="Can we establish transformation → healing temporal sequence from narrative?"
    )


# =============================================================================
# SECTION 13: PIPELINE OUTPUT MODELS (NOT FOR LLM - FOR ANALYSIS PIPELINE)
# =============================================================================


class AnalysisOutputPayload(BaseModel):
    """Complete output payload for a single case analysis.
    
    This wraps the LLM's RemissionAnalysisResponse with pipeline metadata.
    Written to output files - NOT sent to LLM.
    
    Pattern matches nde-analysis project structure.
    """
    
    model_config = ConfigDict(extra="allow")  # Allow additional metadata
    
    # Source identification (pipeline provides)
    dataset: str = Field(
        ...,
        description="Source dataset (pmc, radical_remission, nderf, iands)."
    )
    source_file: str = Field(
        ...,
        description="Relative path to source JSON file."
    )
    source_url: Optional[str] = Field(
        None,
        description="URL where case was originally retrieved."
    )
    source_id: Optional[str] = Field(
        None,
        description="Unique ID from source (PMCID, slug, etc.)."
    )
    
    # Original content (pipeline provides)
    title: Optional[str] = Field(
        None,
        description="Case title if available."
    )
    content: str = Field(
        ...,
        description="Full narrative text sent to LLM."
    )
    
    # Pipeline metadata (pipeline provides)
    analysis_model: str = Field(
        ...,
        description="LLM model used for analysis."
    )
    analysis_timestamp: str = Field(
        ...,
        description="ISO timestamp of analysis."
    )
    source_checksum: str = Field(
        ...,
        description="SHA256 of content for deduplication."
    )
    questionnaire_schema: str = Field(
        default="RemissionAnalysisResponse",
        description="Schema version used."
    )
    
    # LLM response (what LLM actually returns)
    analysis: RemissionAnalysisResponse = Field(
        ...,
        description="The LLM's structured analysis."
    )
    
    # API response metadata (pipeline provides)
    response_id: Optional[str] = Field(
        None,
        description="API response ID for tracing."
    )
    usage: Optional[dict] = Field(
        None,
        description="Token usage statistics."
    )


class BatchAnalysisResult(BaseModel):
    """Summary of a batch analysis run."""
    
    model_config = ConfigDict(extra="allow", protected_namespaces=())
    
    batch_id: str = Field(
        ...,
        description="Unique batch identifier."
    )
    timestamp: str = Field(
        ...,
        description="Batch completion timestamp."
    )
    total_cases: int = Field(
        ...,
        description="Total cases processed."
    )
    successful: int = Field(
        ...,
        description="Successful extractions."
    )
    failed: int = Field(
        ...,
        description="Failed extractions."
    )
    skipped: int = Field(
        default=0,
        description="Skipped (already processed)."
    )
    llm_model: str = Field(
        ...,
        description="LLM model used."
    )
    datasets_processed: List[str] = Field(
        default_factory=list,
        description="Which datasets were included."
    )
    error_summary: Optional[dict] = Field(
        None,
        description="Summary of errors encountered."
    )


class DatasetSummary(BaseModel):
    """Summary statistics for a dataset of extracted cases."""
    
    model_config = ConfigDict(extra="allow")
    
    total_cases: int = Field(
        ...,
        description="Total number of cases in dataset."
    )
    by_source: dict = Field(
        default_factory=dict,
        description="Count by data source."
    )
    by_disease_category: dict = Field(
        default_factory=dict,
        description="Count by disease category."
    )
    by_cancer_type: dict = Field(
        default_factory=dict,
        description="Count by cancer type (cancer cases only)."
    )
    by_stage: dict = Field(
        default_factory=dict,
        description="Count by cancer stage."
    )
    by_verification_tier: dict = Field(
        default_factory=dict,
        description="Count by verification tier."
    )
    by_remission_type: dict = Field(
        default_factory=dict,
        description="Count by remission type."
    )
    turner_factor_prevalence: dict = Field(
        default_factory=dict,
        description="Prevalence of each Turner factor."
    )
    transformation_preceded_healing_rate: Optional[float] = Field(
        None,
        description="Rate at which transformation preceded healing."
    )
