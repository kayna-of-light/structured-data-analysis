#!/usr/bin/env python3
"""Analyze extraction results for judgment source and emotional_tone.

The key research question: Do people experience judgment FROM the Being of Light,
or do they judge THEMSELVES? This validates/contradicts the 84.8% statistic.
"""

import json
from pathlib import Path

def main():
    structured = Path(__file__).parent / "structured"
    
    print(f"{'File':<38} {'Occurrence':<12} {'Judgment Source':<18} {'Emotional Tone':<18}")
    print("-" * 90)
    
    results = []
    for f in sorted(structured.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        ext = data.get("extraction", {})
        lr = ext.get("life_review", {})
        has_lr = lr.get("occurrence", "not_mentioned")
        judgment = lr.get("judgment", "n/a")
        tone = lr.get("emotional_tone", "n/a")
        title = data.get("title", f.stem)[:40]
        results.append({
            "file": f.stem[:37],
            "life_review": has_lr,
            "judgment": judgment,
            "emotional_tone": tone,
            "title": title,
        })
        print(f"{f.stem[:37]:<38} {has_lr:<12} {judgment:<18} {tone:<18}")
    
    print("\n" + "=" * 90)
    print("SUMMARY - CASES WITH LIFE REVIEW:")
    
    # Filter to cases with life review
    lr_cases = [r for r in results if r["life_review"] in ("extensive", "brief")]
    
    # Count judgment sources
    judgments = {}
    for r in lr_cases:
        j = r["judgment"]
        judgments[j] = judgments.get(j, 0) + 1
    
    print(f"\nTotal with life review: {len(lr_cases)}")
    print("\nJUDGMENT SOURCE (Key research question: external vs self):")
    for j, count in sorted(judgments.items()):
        pct = count / len(lr_cases) * 100 if lr_cases else 0
        print(f"  {j:<20}: {count:>2} ({pct:5.1f}%)")
    
    # Calculate "no external condemnation" - self + none
    no_external = judgments.get("self_judgment", 0) + judgments.get("none", 0)
    external = judgments.get("guide_or_light", 0)
    print(f"\n  → No external judgment: {no_external} ({no_external/len(lr_cases)*100:.1f}%)" if lr_cases else "")
    print(f"  → External (guide/light): {external} ({external/len(lr_cases)*100:.1f}%)" if lr_cases else "")
    
    # Count emotional tones
    tones = {}
    for r in lr_cases:
        t = r["emotional_tone"]
        tones[t] = tones.get(t, 0) + 1
    
    print("\nEMOTIONAL TONE:")
    for t, count in sorted(tones.items()):
        pct = count / len(lr_cases) * 100 if lr_cases else 0
        print(f"  {t:<20}: {count:>2} ({pct:5.1f}%)")
    
    # Calculate love:shame ratio
    love = tones.get("love", 0)
    shame = tones.get("shame_or_regret", 0)
    if shame > 0:
        ratio = love / shame
        print(f"\n  → Love:Shame ratio: {ratio:.2f}:1")
    
    # Cross-tabulation: judgment source vs emotional tone
    print("\n" + "=" * 90)
    print("CROSS-TAB: Judgment Source × Emotional Tone")
    print("-" * 50)
    
    cross = {}
    for r in lr_cases:
        key = (r["judgment"], r["emotional_tone"])
        cross[key] = cross.get(key, 0) + 1
    
    for (j, t), count in sorted(cross.items()):
        print(f"  {j:<18} + {t:<18}: {count}")

if __name__ == "__main__":
    main()
