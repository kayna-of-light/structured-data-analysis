#!/usr/bin/env python3
"""Quick check of judgment classifications in extraction test."""
import json
import os

structured_dir = "structured"

for filename in sorted(os.listdir(structured_dir)):
    if not filename.endswith('.json'):
        continue
    
    filepath = os.path.join(structured_dir, filename)
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle nested structure - extraction or analysis contains the actual data
    analysis = data.get('extraction', data.get('analysis', data))
    life_review = analysis.get('life_review', {})
    occurrence = life_review.get('occurrence', 'no')
    judgment_source = life_review.get('judgment_source', 'N/A')
    judgment_intensity = life_review.get('judgment_intensity', 'N/A')
    
    print(f"{filename}:")
    print(f"  occurrence: {occurrence}")
    if occurrence not in ('no', 'not_mentioned'):
        print(f"  judgment_source: {judgment_source}")
        print(f"  judgment_intensity: {judgment_intensity}")
    print()
