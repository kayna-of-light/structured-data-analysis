"""Quality assurance report for scraped and analyzed remission case data."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).parent
DATA_ROOT = ROOT / "data"
ANALYSIS_DIR = ROOT / "output" / "analysis"

ISSUE_LABELS = {
    "invalid_json": "Invalid JSON files",
    "empty_content": "Empty content",
    "missing_diagnosis": "Missing diagnosis info",
    "missing_outcome": "Missing remission outcome",
    "low_validation_tier": "Low validation tier (Tier 4)",
    "no_factors_identified": "No Turner factors identified",
}


def track_issue(issues: Dict[str, Dict], key: str, example: str, max_examples: int = 5) -> None:
    """Track an issue with limited examples."""
    if key not in issues:
        issues[key] = {"count": 0, "examples": []}
    issues[key]["count"] += 1
    if len(issues[key]["examples"]) < max_examples:
        issues[key]["examples"].append(example)


def record_issue_metadata(
    registry: Dict[str, List[Dict[str, str]]],
    issue_type: str,
    **metadata: str,
) -> None:
    """Record metadata for an issue."""
    registry[issue_type].append(metadata)


def analyze_scraped_data(data_dir: Path) -> Dict[str, Any]:
    """Analyze raw scraped data quality."""
    stats = {
        "total_files": 0,
        "by_dataset": Counter(),
        "issues": {},
    }
    
    for dataset_dir in data_dir.iterdir():
        if not dataset_dir.is_dir():
            continue
        
        for json_path in dataset_dir.glob("*.json"):
            stats["total_files"] += 1
            stats["by_dataset"][dataset_dir.name] += 1
            
            try:
                with json_path.open("r", encoding="utf-8") as fh:
                    data = json.load(fh)
            except json.JSONDecodeError as exc:
                track_issue(stats["issues"], "invalid_json", f"{json_path.name}: {exc}")
                continue
            
            content = data.get("content") or data.get("narrative") or data.get("text", "")
            if not content or len(content.strip()) < 50:
                track_issue(stats["issues"], "empty_content", json_path.name)
    
    return stats


def analyze_processed_data(analysis_dir: Path) -> Dict[str, Any]:
    """Analyze LLM-processed data quality."""
    stats = {
        "total_analyzed": 0,
        "by_dataset": Counter(),
        "validation_tiers": Counter(),
        "remission_types": Counter(),
        "turner_factors": Counter(),
        "has_nde_ste": 0,
        "transformation_preceded": 0,
        "issues": {},
    }
    
    if not analysis_dir.exists():
        return stats
    
    for json_path in sorted(analysis_dir.glob("*.json")):
        stats["total_analyzed"] += 1
        
        try:
            with json_path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except json.JSONDecodeError as exc:
            track_issue(stats["issues"], "invalid_json", f"{json_path.name}: {exc}")
            continue
        
        metadata = data.get("metadata", {})
        analysis = data.get("analysis", {})
        
        dataset = metadata.get("dataset", "unknown")
        stats["by_dataset"][dataset] += 1
        
        # Validation tier
        validation = analysis.get("validation", {})
        tier = validation.get("verification_tier", "unknown")
        stats["validation_tiers"][tier] += 1
        
        if tier == "tier_4_anecdotal":
            track_issue(stats["issues"], "low_validation_tier", json_path.name)
        
        # Remission type
        outcome = analysis.get("remission_outcome", {})
        rem_type = outcome.get("remission_type", "unknown")
        stats["remission_types"][rem_type] += 1
        
        if rem_type == "not_specified":
            track_issue(stats["issues"], "missing_outcome", json_path.name)
        
        # Turner factors
        factors = analysis.get("turner_factors", {})
        factor_count = 0
        for key, value in factors.items():
            if key.startswith("factor_") and value in ("yes_explicit", "implied"):
                factor_count += 1
                factor_name = key.replace("factor_", "")
                stats["turner_factors"][factor_name] += 1
        
        if factor_count == 0:
            track_issue(stats["issues"], "no_factors_identified", json_path.name)
        
        # Anomalous experience
        anomalous = analysis.get("anomalous_experience", {})
        if anomalous.get("has_experience") in ("yes_explicit", "implied"):
            stats["has_nde_ste"] += 1
        
        # Transformation sequence
        corresp = analysis.get("correspondential_markers", {})
        if corresp.get("transformation_preceded_healing") in ("yes_explicit", "implied"):
            stats["transformation_preceded"] += 1
        
        # Diagnosis quality
        diagnosis = analysis.get("diagnosis", {})
        if not diagnosis.get("cancer_type") and not diagnosis.get("diagnosis_raw"):
            track_issue(stats["issues"], "missing_diagnosis", json_path.name)
    
    return stats


def print_report(scraped: Dict[str, Any], analyzed: Dict[str, Any]) -> None:
    """Print the QA report."""
    print("=" * 70)
    print("REMISSION DATA QUALITY REPORT")
    print("=" * 70)
    
    print("\n--- SCRAPED DATA ---")
    print(f"Total files: {scraped['total_files']}")
    print("\nBy dataset:")
    for dataset, count in sorted(scraped["by_dataset"].items()):
        print(f"  {dataset}: {count}")
    
    if scraped["issues"]:
        print("\nIssues found:")
        for key, label in ISSUE_LABELS.items():
            if key in scraped["issues"]:
                issue = scraped["issues"][key]
                print(f"  {label}: {issue['count']}")
                for example in issue["examples"][:3]:
                    print(f"    - {example}")
    
    print("\n--- ANALYZED DATA ---")
    print(f"Total analyzed: {analyzed['total_analyzed']}")
    
    if analyzed["total_analyzed"] > 0:
        print("\nBy dataset:")
        for dataset, count in sorted(analyzed["by_dataset"].items()):
            print(f"  {dataset}: {count}")
        
        print("\nValidation tiers:")
        for tier, count in sorted(analyzed["validation_tiers"].items()):
            pct = count / analyzed["total_analyzed"] * 100
            print(f"  {tier}: {count} ({pct:.1f}%)")
        
        print("\nRemission types:")
        for rem_type, count in sorted(analyzed["remission_types"].items()):
            pct = count / analyzed["total_analyzed"] * 100
            print(f"  {rem_type}: {count} ({pct:.1f}%)")
        
        print("\nTurner factors frequency:")
        for factor, count in analyzed["turner_factors"].most_common():
            pct = count / analyzed["total_analyzed"] * 100
            print(f"  {factor}: {count} ({pct:.1f}%)")
        
        print(f"\nNDE/STE linked: {analyzed['has_nde_ste']} "
              f"({analyzed['has_nde_ste']/analyzed['total_analyzed']*100:.1f}%)")
        print(f"Transformation preceded healing: {analyzed['transformation_preceded']} "
              f"({analyzed['transformation_preceded']/analyzed['total_analyzed']*100:.1f}%)")
        
        if analyzed["issues"]:
            print("\nAnalysis issues:")
            for key, label in ISSUE_LABELS.items():
                if key in analyzed["issues"]:
                    issue = analyzed["issues"][key]
                    print(f"  {label}: {issue['count']}")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="QA report for remission case data.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DATA_ROOT,
        help="Path to scraped data directory.",
    )
    parser.add_argument(
        "--analysis-dir",
        type=Path,
        default=ANALYSIS_DIR,
        help="Path to analyzed data directory.",
    )
    args = parser.parse_args()
    
    scraped_stats = analyze_scraped_data(args.data_dir)
    analyzed_stats = analyze_processed_data(args.analysis_dir)
    print_report(scraped_stats, analyzed_stats)


if __name__ == "__main__":
    main()
