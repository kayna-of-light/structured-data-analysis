"""
Extract verified statistics for thesis document.
Run this to get exact numbers for the scientific paper.
"""
import json
import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

# Load all analyzed cases
analysis_path = Path('output/analysis')
records = []

for json_file in analysis_path.glob('*.json'):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            record = json.load(f)
            records.append(record)
    except Exception as e:
        pass

print(f"Total cases loaded: {len(records)}")

# Extract flat data
def extract_case_data(record):
    analysis = record.get('analysis', {}) or {}
    data = {
        'dataset': record.get('dataset', 'unknown'),
    }
    
    demo = analysis.get('demographics', {}) or {}
    data['sex'] = demo.get('sex', 'not_mentioned')
    
    diag = analysis.get('diagnosis', {}) or {}
    data['disease_category'] = diag.get('disease_category', 'unknown')
    data['organ_system'] = diag.get('organ_system', 'other')
    
    outcome = analysis.get('remission_outcome', {}) or {}
    data['verification_tier'] = analysis.get('validation', {}).get('verification_tier', 'unknown')
    data['remission_speed'] = outcome.get('remission_speed', 'not_specified')
    
    tf = analysis.get('turner_factors', {}) or {}
    for factor in ['diet_change', 'agency', 'intuition', 'supplements', 
                   'emotional_release', 'positive_emotions', 'social_support',
                   'spiritual_connection', 'purpose']:
        data[f'factor_{factor}'] = tf.get(f'factor_{factor}', 'not_mentioned')
    data['factors_count'] = tf.get('factors_present_count', 0)
    
    es = analysis.get('existential_shift', {}) or {}
    data['transformation_preceded'] = es.get('transformation_preceded_healing', 'not_mentioned')
    data['fear_to_love_shift'] = es.get('fear_to_love_shift', 'not_mentioned')
    data['surrender_event'] = es.get('surrender_event', 'not_mentioned')
    
    ae = analysis.get('anomalous_experience', {}) or {}
    data['anomalous_type'] = ae.get('experience_type', 'not_mentioned')
    data['experience_preceded'] = ae.get('experience_preceded_healing', 'not_mentioned')
    
    data['has_transformation'] = analysis.get('has_transformation_narrative', False)
    
    return data

df = pd.DataFrame([extract_case_data(r) for r in records])

# Split by source type (lowercase in data)
testimonial = df[df['dataset'].isin(['rrp', 'nderf', 'iands'])]
clinical = df[df['dataset'] == 'pmc']

print("\n" + "="*70)
print("THESIS STATISTICS - VERIFIED FROM DATA")
print("="*70)

print(f"\n--- DATASET COMPOSITION ---")
print(f"Total cases: N = {len(df)}")
print(f"Testimonial (RRP, NDERF, IANDS): n = {len(testimonial)}")
print(f"Clinical (PMC): n = {len(clinical)}")
print(f"\nBy source:")
for src, count in df['dataset'].value_counts().items():
    print(f"  {src}: {count} ({100*count/len(df):.1f}%)")

# Disease categories
print(f"\n--- DISEASE DISTRIBUTION ---")
for cat, count in df['disease_category'].value_counts().items():
    print(f"  {cat}: {count} ({100*count/len(df):.1f}%)")

# Organ systems (all cases)
print(f"\n--- ORGAN SYSTEM DISTRIBUTION (All cases, N={len(df)}) ---")
for organ, count in df['organ_system'].value_counts().head(10).items():
    print(f"  {organ}: {count} ({100*count/len(df):.1f}%)")

# Organ systems (testimonial only)
print(f"\n--- ORGAN SYSTEM DISTRIBUTION (Testimonial, n={len(testimonial)}) ---")
for organ, count in testimonial['organ_system'].value_counts().head(10).items():
    print(f"  {organ}: {count} ({100*count/len(testimonial):.1f}%)")

# KEY FINDING: Transformation preceded healing
print("\n--- KEY FINDING: TRANSFORMATION TEMPORAL SEQUENCE ---")

# Only testimonial subset has this data
has_narrative = testimonial[testimonial['has_transformation'] == True]
print(f"Testimonial cases with transformation narrative: {len(has_narrative)}/{len(testimonial)} ({100*len(has_narrative)/len(testimonial):.1f}%)")

# Among those with narratives, what % showed transformation preceding?
preceded_yes = has_narrative['transformation_preceded'].isin(['yes_explicit', 'implied']).sum()
preceded_no = (has_narrative['transformation_preceded'] == 'no').sum()
preceded_unclear = has_narrative['transformation_preceded'].isin(['not_mentioned', 'unclear']).sum()

print(f"\nAmong those with narrative (n={len(has_narrative)}):")
print(f"  Transformation preceded: {preceded_yes} ({100*preceded_yes/len(has_narrative):.1f}%)")
print(f"  Did not precede: {preceded_no} ({100*preceded_no/len(has_narrative):.1f}%)")
print(f"  Unclear/not mentioned: {preceded_unclear} ({100*preceded_unclear/len(has_narrative):.1f}%)")

# Clear cases only
clear_cases = has_narrative[has_narrative['transformation_preceded'].isin(['yes_explicit', 'implied', 'no'])]
if len(clear_cases) > 0:
    clear_yes = clear_cases['transformation_preceded'].isin(['yes_explicit', 'implied']).sum()
    clear_no = (clear_cases['transformation_preceded'] == 'no').sum()
    
    print(f"\nAmong CLEAR temporal ordering (n={len(clear_cases)}):")
    print(f"  Preceded: {clear_yes} ({100*clear_yes/len(clear_cases):.1f}%)")
    print(f"  Did not: {clear_no} ({100*clear_no/len(clear_cases):.1f}%)")
    
    # Binomial test
    binom = stats.binomtest(clear_yes, len(clear_cases), 0.5, alternative='greater')
    print(f"  Binomial test vs 50%: p = {binom.pvalue:.2e}")
    
    # Chi-square
    observed = np.array([clear_yes, clear_no])
    expected = np.array([len(clear_cases)/2, len(clear_cases)/2])
    chi2, p = stats.chisquare(observed, expected)
    print(f"  Chi-square test: χ² = {chi2:.2f}, p = {p:.2e}")

# SURRENDER × TRANSFORMATION
print("\n--- SURRENDER × TRANSFORMATION ANALYSIS ---")

def is_present(series):
    return series.isin(['yes_explicit', 'implied'])

has_surrender = is_present(testimonial['surrender_event'])
has_transform = testimonial['has_transformation'] == True

surr_yes = has_surrender.sum()
print(f"Cases with surrender event: {surr_yes}/{len(testimonial)} ({100*surr_yes/len(testimonial):.1f}%)")

# Among those who surrendered, what % had transformation?
surr_with_trans = has_transform[has_surrender].mean() * 100
no_surr_with_trans = has_transform[~has_surrender].mean() * 100
print(f"\nTransformation rate WITH surrender: {surr_with_trans:.1f}%")
print(f"Transformation rate WITHOUT surrender: {no_surr_with_trans:.1f}%")
print(f"Difference: +{surr_with_trans - no_surr_with_trans:.1f}%")

# Fisher's exact test
crosstab = pd.crosstab(has_surrender, has_transform)
if crosstab.shape == (2, 2):
    odds, p_fisher = stats.fisher_exact(crosstab)
    print(f"Fisher's exact test: OR = {odds:.2f}, p = {p_fisher:.4f}")

# SPIRITUAL CONNECTION
print("\n--- SPIRITUAL CONNECTION ANALYSIS ---")
has_spiritual = is_present(testimonial['factor_spiritual_connection'])
spirit_rate = has_spiritual.mean() * 100
print(f"Spiritual connection present: {has_spiritual.sum()}/{len(testimonial)} ({spirit_rate:.1f}%)")

# Spiritual connection × Surrender
surr_spirit = has_spiritual[has_surrender].mean() * 100
no_surr_spirit = has_spiritual[~has_surrender].mean() * 100
print(f"\nSpiritual connection WITH surrender: {surr_spirit:.1f}%")
print(f"Spiritual connection WITHOUT surrender: {no_surr_spirit:.1f}%")
print(f"Difference: +{surr_spirit - no_surr_spirit:.1f}%")

# NDE ANALYSIS
print("\n--- NDE CASES ANALYSIS ---")
nde_cases = df[df['anomalous_type'] == 'nde']
print(f"NDE-linked cases: {len(nde_cases)}")

if len(nde_cases) > 0:
    nde_preceded = nde_cases['experience_preceded'].isin(['yes_explicit', 'implied']).sum()
    print(f"NDE preceded healing: {nde_preceded}/{len(nde_cases)} ({100*nde_preceded/len(nde_cases):.1f}%)")
    
    nde_spiritual = is_present(nde_cases['factor_spiritual_connection']).sum()
    print(f"Spiritual connection in NDE cases: {nde_spiritual}/{len(nde_cases)} ({100*nde_spiritual/len(nde_cases):.1f}%)")
    
    # Mean factor count
    nde_factors = nde_cases['factors_count'].mean()
    non_nde = df[df['anomalous_type'] != 'nde']
    non_nde_factors = non_nde['factors_count'].mean()
    print(f"\nMean Turner factors - NDE: {nde_factors:.2f}")
    print(f"Mean Turner factors - Non-NDE: {non_nde_factors:.2f}")
    
    # Mann-Whitney U
    u_stat, p_mw = stats.mannwhitneyu(nde_cases['factors_count'], non_nde['factors_count'])
    print(f"Mann-Whitney U: U = {u_stat:.0f}, p = {p_mw:.2e}")

# FACTOR PREVALENCE
print("\n--- TURNER FACTOR PREVALENCE (Testimonial) ---")
factor_cols = [c for c in testimonial.columns if c.startswith('factor_') and c != 'factors_count']
for col in factor_cols:
    present = is_present(testimonial[col]).sum()
    rate = 100 * present / len(testimonial)
    name = col.replace('factor_', '').replace('_', ' ').title()
    print(f"  {name}: {present}/{len(testimonial)} ({rate:.1f}%)")

print("\n" + "="*70)
print("END VERIFIED STATISTICS")
print("="*70)
