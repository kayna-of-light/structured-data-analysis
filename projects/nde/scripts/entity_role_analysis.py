"""
Entity Role Analysis for NDE Research Questions

Analyzes the structured NDE data to answer:
1. What functional roles do entities play in NDEs?
2. Do diverse imagery forms map to common functional states (correspondential analysis)?
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

ROOT = Path(__file__).parent
ANALYSIS_DIR = ROOT / "output" / "analysis"


def load_all_analyses() -> List[Dict[str, Any]]:
    """Load all analyzed NDE experiences."""
    experiences = []
    for path in sorted(ANALYSIS_DIR.glob("*.json")):
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if "analysis" in data:
                    experiences.append(data)
        except (json.JSONDecodeError, IOError):
            continue
    return experiences


def analyze_entity_roles(experiences: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze entity roles and functions in NDE encounters."""
    results = {
        "total_experiences": len(experiences),
        "being_identifications": Counter(),
        "spiritual_beings": Counter(),
        "greeting_types": Counter(),
        "guidance_levels": Counter(),
        "communication_modes": Counter(),
        "return_choices": Counter(),
        "return_reasons": Counter(),
        "deceased_relatives": Counter(),
        "other_souls_presence": Counter(),
        # Cross-tabulations for role analysis
        "guidance_by_being_type": defaultdict(Counter),
        "return_choice_by_being_type": defaultdict(Counter),
        "boundary_by_being_type": defaultdict(Counter),
    }
    
    for exp in experiences:
        analysis = exp.get("analysis", {})
        
        # Arrival section - being encounters
        arrival = analysis.get("passage", {}).get("arrival", {})
        for being in arrival.get("being_identifications", []):
            results["being_identifications"][being] += 1
        for greeting in arrival.get("greeting_types", []):
            results["greeting_types"][greeting] += 1
        
        # Encounters section - spiritual beings and guidance
        encounters = analysis.get("world_of_spirits", {}).get("encounters", {})
        for spirit in encounters.get("spiritual_beings", []):
            results["spiritual_beings"][spirit] += 1
        
        guidance = encounters.get("guidance_level", "not_mentioned")
        results["guidance_levels"][guidance] += 1
        
        comm = encounters.get("communication_mode", "not_mentioned")
        results["communication_modes"][comm] += 1
        
        relatives = encounters.get("deceased_relatives", "not_mentioned")
        results["deceased_relatives"][relatives] += 1
        
        souls = encounters.get("other_souls_presence", "not_mentioned")
        results["other_souls_presence"][souls] += 1
        
        # Boundary and return section - entity role in return
        boundary_return = analysis.get("boundary_and_return", {})
        return_choice = boundary_return.get("return_choice", "not_mentioned")
        results["return_choices"][return_choice] += 1
        
        return_reason = boundary_return.get("return_reason", "not_mentioned")
        results["return_reasons"][return_reason] += 1
        
        boundary = boundary_return.get("boundary_encounter", "not_mentioned")
        
        # Cross-tabulate: guidance level by being type
        for being in arrival.get("being_identifications", []):
            results["guidance_by_being_type"][being][guidance] += 1
            results["return_choice_by_being_type"][being][return_choice] += 1
            results["boundary_by_being_type"][being][boundary] += 1
    
    return results


def analyze_correspondences(experiences: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze whether diverse imagery maps to common functional states."""
    results = {
        "total_experiences": len(experiences),
        # Transition imagery → functional outcome
        "passage_types": Counter(),
        "passage_emotional_tone": Counter(),
        "passage_to_outcome": defaultdict(Counter),
        # Light encounter forms → functional roles
        "light_encounters": Counter(),
        "light_to_guidance": defaultdict(Counter),
        "light_to_return": defaultdict(Counter),
        # Being forms → functional roles
        "being_to_function": defaultdict(lambda: defaultdict(Counter)),
        # Environment features → comparative reality
        "environment_features": Counter(),
        "environment_to_reality": defaultdict(Counter),
        # Religious affiliation → being identification (cultural filter test)
        "religion_to_being": defaultdict(Counter),
        # Sequence patterns
        "canonical_adherence": Counter(),
        "stage_elements_frequency": Counter(),
    }
    
    for exp in experiences:
        analysis = exp.get("analysis", {})
        
        # Passage/transition analysis
        tunnel = analysis.get("passage", {}).get("tunnel", {})
        passage_type = tunnel.get("passage_type", "not_mentioned")
        results["passage_types"][passage_type] += 1
        
        emotional_tone = tunnel.get("emotional_tone", "not_mentioned")
        results["passage_emotional_tone"][emotional_tone] += 1
        
        # Arrival outcome
        arrival = analysis.get("passage", {}).get("arrival", {})
        sense_of_belonging = arrival.get("sense_of_belonging", "not_mentioned")
        results["passage_to_outcome"][passage_type][sense_of_belonging] += 1
        
        # Light encounter forms
        for light in arrival.get("light_encounter", []):
            results["light_encounters"][light] += 1
            
            # Cross-tabulate light form with guidance and return
            encounters = analysis.get("world_of_spirits", {}).get("encounters", {})
            guidance = encounters.get("guidance_level", "not_mentioned")
            results["light_to_guidance"][light][guidance] += 1
            
            boundary_return = analysis.get("boundary_and_return", {})
            return_choice = boundary_return.get("return_choice", "not_mentioned")
            results["light_to_return"][light][return_choice] += 1
        
        # Being form to function analysis
        for being in arrival.get("being_identifications", []):
            encounters = analysis.get("world_of_spirits", {}).get("encounters", {})
            guidance = encounters.get("guidance_level", "not_mentioned")
            comm = encounters.get("communication_mode", "not_mentioned")
            
            boundary_return = analysis.get("boundary_and_return", {})
            return_choice = boundary_return.get("return_choice", "not_mentioned")
            
            results["being_to_function"][being]["guidance"][guidance] += 1
            results["being_to_function"][being]["communication"][comm] += 1
            results["being_to_function"][being]["return"][return_choice] += 1
        
        # Environment to reality perception
        env = analysis.get("world_of_spirits", {}).get("environment", {})
        for feature in env.get("environment_features", []):
            results["environment_features"][feature] += 1
            comparative = env.get("comparative_reality", "not_mentioned")
            results["environment_to_reality"][feature][comparative] += 1
        
        # Religious affiliation to being identification
        demographics = analysis.get("person_demographics", {})
        religion = demographics.get("religious_affiliation", "not_mentioned")
        for being in arrival.get("being_identifications", []):
            results["religion_to_being"][religion][being] += 1
        
        # Sequence analysis
        stage_seq = analysis.get("stage_sequence", {})
        canonical = stage_seq.get("canonical_sequence", "indeterminate")
        results["canonical_adherence"][canonical] += 1
        
        for element in stage_seq.get("present_elements", []):
            results["stage_elements_frequency"][element] += 1
    
    return results


def format_counter(counter: Counter, total: int, top_n: int = 20) -> str:
    """Format a counter with percentages."""
    lines = []
    for item, count in counter.most_common(top_n):
        pct = (count / total * 100) if total > 0 else 0
        lines.append(f"  {item}: {count} ({pct:.1f}%)")
    return "\n".join(lines)


def format_cross_tab(cross_tab: Mapping[str, Counter], top_n: int = 10) -> str:
    """Format a cross-tabulation."""
    lines = []
    for key, subcounter in sorted(cross_tab.items(), 
                                   key=lambda x: sum(x[1].values()), 
                                   reverse=True)[:top_n]:
        total = sum(subcounter.values())
        lines.append(f"\n  {key} (n={total}):")
        for subkey, count in subcounter.most_common(5):
            pct = (count / total * 100) if total > 0 else 0
            lines.append(f"    {subkey}: {count} ({pct:.1f}%)")
    return "\n".join(lines)


def main():
    print("Loading NDE analysis data...")
    experiences = load_all_analyses()
    total = len(experiences)
    print(f"Loaded {total} analyzed experiences.\n")
    
    # === ENTITY ROLE ANALYSIS ===
    print("=" * 70)
    print("ENTITY ROLE ANALYSIS")
    print("=" * 70)
    
    roles = analyze_entity_roles(experiences)
    
    print("\n1. BEING IDENTIFICATIONS (who appears)")
    print(format_counter(roles["being_identifications"], total))
    
    print("\n2. SPIRITUAL BEINGS (guides, angels, etc.)")
    print(format_counter(roles["spiritual_beings"], total))
    
    print("\n3. GREETING TYPES (how experiencer is received)")
    print(format_counter(roles["greeting_types"], total))
    
    print("\n4. GUIDANCE LEVELS (functional role: guidance)")
    print(format_counter(roles["guidance_levels"], total))
    
    print("\n5. COMMUNICATION MODES (how entities communicate)")
    print(format_counter(roles["communication_modes"], total))
    
    print("\n6. DECEASED RELATIVES (specific category)")
    print(format_counter(roles["deceased_relatives"], total))
    
    print("\n7. OTHER SOULS PRESENCE (beyond personal connections)")
    print(format_counter(roles["other_souls_presence"], total))
    
    print("\n8. RETURN CHOICES (entity role in return)")
    print(format_counter(roles["return_choices"], total))
    
    print("\n9. RETURN REASONS (why sent back)")
    print(format_counter(roles["return_reasons"], total))
    
    print("\n10. GUIDANCE LEVEL BY BEING TYPE (cross-tabulation)")
    print(format_cross_tab(roles["guidance_by_being_type"]))
    
    print("\n11. RETURN CHOICE BY BEING TYPE (gatekeeper function)")
    print(format_cross_tab(roles["return_choice_by_being_type"]))
    
    print("\n12. BOUNDARY TYPE BY BEING TYPE")
    print(format_cross_tab(roles["boundary_by_being_type"]))
    
    # === CORRESPONDENTIAL ANALYSIS ===
    print("\n" + "=" * 70)
    print("CORRESPONDENTIAL ANALYSIS")
    print("(Do diverse imagery forms map to common functional states?)")
    print("=" * 70)
    
    corr = analyze_correspondences(experiences)
    
    print("\n1. PASSAGE TYPES (transition imagery)")
    print(format_counter(corr["passage_types"], total))
    
    print("\n2. PASSAGE EMOTIONAL TONE")
    print(format_counter(corr["passage_emotional_tone"], total))
    
    print("\n3. PASSAGE TYPE → BELONGING OUTCOME (functional convergence)")
    print(format_cross_tab(corr["passage_to_outcome"]))
    
    print("\n4. LIGHT ENCOUNTER FORMS")
    print(format_counter(corr["light_encounters"], total))
    
    print("\n5. LIGHT FORM → GUIDANCE LEVEL (functional equivalence test)")
    print(format_cross_tab(corr["light_to_guidance"]))
    
    print("\n6. LIGHT FORM → RETURN CHOICE")
    print(format_cross_tab(corr["light_to_return"]))
    
    print("\n7. BEING FORM → FUNCTION (comprehensive)")
    for being, functions in sorted(corr["being_to_function"].items(),
                                    key=lambda x: sum(sum(c.values()) for c in x[1].values()),
                                    reverse=True)[:10]:
        total_being = sum(sum(c.values()) for c in functions.values()) // 3
        print(f"\n  {being} (n≈{total_being}):")
        for func_name, func_counter in functions.items():
            func_total = sum(func_counter.values())
            top_value, top_count = func_counter.most_common(1)[0] if func_counter else ("none", 0)
            pct = (top_count / func_total * 100) if func_total > 0 else 0
            print(f"    {func_name}: {top_value} ({pct:.1f}%)")
    
    print("\n8. ENVIRONMENT FEATURES")
    print(format_counter(corr["environment_features"], total))
    
    print("\n9. ENVIRONMENT → COMPARATIVE REALITY")
    print(format_cross_tab(corr["environment_to_reality"]))
    
    print("\n10. RELIGIOUS AFFILIATION → BEING IDENTIFICATION (cultural filter)")
    print(format_cross_tab(corr["religion_to_being"]))
    
    print("\n11. CANONICAL SEQUENCE ADHERENCE")
    print(format_counter(corr["canonical_adherence"], total))
    
    print("\n12. STAGE ELEMENTS FREQUENCY")
    print(format_counter(corr["stage_elements_frequency"], total))
    
    # === SUMMARY ===
    print("\n" + "=" * 70)
    print("KEY FINDINGS SUMMARY")
    print("=" * 70)
    
    # Entity roles summary
    guidance_significant = roles["guidance_levels"]["significant_guidance"]
    guidance_comfort = roles["guidance_levels"]["comfort_or_reassurance"]
    guidance_total = guidance_significant + guidance_comfort
    print(f"\n• Entities providing guidance/comfort: {guidance_total} ({guidance_total/total*100:.1f}%)")
    
    told_return = roles["return_choices"]["told_to_return"]
    chose_return = roles["return_choices"]["chose_to_return"]
    print(f"• Told to return (gatekeeper function): {told_return} ({told_return/total*100:.1f}%)")
    print(f"• Chose to return (agency preserved): {chose_return} ({chose_return/total*100:.1f}%)")
    
    # Correspondence summary
    tunnel_count = corr["passage_types"]["tunnel"]
    void_count = corr["passage_types"]["void"]
    print(f"\n• Tunnel imagery: {tunnel_count} ({tunnel_count/total*100:.1f}%)")
    print(f"• Void imagery: {void_count} ({void_count/total*100:.1f}%)")
    
    # Check functional equivalence
    tunnel_peaceful = corr["passage_to_outcome"]["tunnel"].get("explicit", 0) + corr["passage_to_outcome"]["tunnel"].get("implied", 0)
    void_peaceful = corr["passage_to_outcome"]["void"].get("explicit", 0) + corr["passage_to_outcome"]["void"].get("implied", 0)
    print(f"• Tunnel → belonging (peaceful arrival): {tunnel_peaceful}")
    print(f"• Void → belonging (peaceful arrival): {void_peaceful}")
    
    print("\n[Analysis complete]")


if __name__ == "__main__":
    main()
