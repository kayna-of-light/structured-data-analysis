"""
Filter NDE experiences for physical healing/remission cases.

This script identifies NDE narratives that contain references to physical healing,
medical remission, or disease resolution. It uses a tiered keyword system to 
maximize accuracy and minimize false positives.

Strategy:
- Tier 1: Direct remission language (e.g., "cancer disappeared", "tumor gone")
- Tier 2: Medical condition + healing outcome combination
- Tier 3: General healing references requiring manual review
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import shutil


@dataclass
class HealingMatch:
    """Represents a potential healing case with confidence scoring."""
    file_path: Path
    title: str
    tier: int  # 1 = high confidence, 2 = medium, 3 = low
    matched_patterns: list[str] = field(default_factory=list)
    context_snippets: list[str] = field(default_factory=list)
    
    @property
    def confidence(self) -> str:
        return {1: "HIGH", 2: "MEDIUM", 3: "LOW"}[self.tier]


class HealingCaseFilter:
    """Filter NDE narratives for physical healing/remission cases."""
    
    # Tier 1: Explicit disease resolution patterns (highest confidence)
    # These patterns strongly indicate documented physical healing/remission
    TIER1_PATTERNS = [
        # Cancer-specific remission (tight proximity - within 100 chars)
        r'\b(?:cancer|tumor|tumour|malignant|carcinoma|leukemia|lymphoma|melanoma)\b.{0,100}\b(?:gone|disappeared|vanished|healed|cured|remission|free)\b',
        r'\b(?:gone|disappeared|vanished|healed|cured|remission|free)\b.{0,100}\b(?:cancer|tumor|tumour|malignant|carcinoma)\b',
        # Explicit remission language
        r'\b(?:complete|spontaneous|miraculous|unexplained)\s+(?:remission|recovery|healing)\b',
        r'\b(?:disease|illness)\s+(?:disappeared|vanished|gone|cleared)\b',
        # Medical verification of healing
        r'\bno\s+(?:trace|sign|evidence)\s+of\s+(?:cancer|tumor|disease|illness)\b',
        r'\b(?:cancer|tumor|illness|disease)\s+(?:was|is)\s+gone\b',
        # Terminal diagnosis reversal (tight proximity)
        r'\b(?:terminal|stage\s*(?:4|iv|four)|months?\s+to\s+live)\b.{0,150}\b(?:survived|healed|recovered|cured|remission|still\s+alive)\b',
        # Physical healing miracle language
        r'\bphysical(?:ly)?\s+healed?\b',
        r'\bbody\s+(?:was|is)\s+(?:healed|restored|cured)\b',
        r'\binstant(?:ly|aneous)?\s+(?:healed?|healing|recovery)\b',
    ]
    
    # Tier 2: Medical condition + healing outcome (medium confidence)
    # Requires both a disease mention AND healing language
    DISEASE_TERMS = [
        r'\bcancer\b', r'\btumou?r\b', r'\bmalignant\b', r'\bcarcinoma\b',
        r'\bleukemia\b', r'\blymphoma\b', r'\bmelanoma\b', r'\bsarcoma\b',
        r'\bmetasta(?:sis|tic|sized?)\b', r'\bbiopsy\b', r'\boncolog(?:y|ist)\b',
        r'\bchemotherapy\b', r'\bradiation\s+(?:therapy|treatment)\b',
        r'\bstage\s*(?:1|2|3|4|i|ii|iii|iv|one|two|three|four)\b',
        r'\bterminal(?:ly)?\b', r'\bprognosis\b', r'\bdiagnos(?:is|ed)\b',
        r'\bhospice\b', r'\bmonths?\s+to\s+live\b',
        # Other serious conditions
        r'\bheart\s+(?:disease|failure|attack)\b', r'\bstroke\b',
        r'\bparalyz(?:ed|sis)\b', r'\bblind(?:ness)?\b', r'\bdeaf(?:ness)?\b',
        r'\bdiabetes\b', r'\bmultiple\s+sclerosis\b', r'\bals\b',
        r'\bautoimmune\b', r'\blupus\b', r'\barthritis\b',
        r'\bkidney\s+(?:failure|disease)\b', r'\bliver\s+(?:failure|disease)\b',
        r'\bcoma\b', r'\bbrain\s+(?:damage|injury|tumor)\b',
    ]
    
    HEALING_OUTCOMES = [
        r'\bhealed?\b', r'\bcured?\b', r'\bremission\b', r'\brecovered?\b',
        r'\bdisappeared\b', r'\bvanished\b', r'\bgone\b', r'\bcleared?\b',
        r'\bmiracle\b', r'\bmiraculous(?:ly)?\b', r'\bunexplained\b',
        r'\bspontaneous\s+(?:recovery|healing|remission)\b',
        r'\bno\s+longer\s+(?:had|have|sick|ill)\b',
        r'\bcompletely\s+(?:healed|recovered|well)\b',
        r'\bfree\s+(?:of|from)\s+(?:cancer|disease|illness)\b',
        r'\bwalked?\s+again\b', r'\bsee(?:ing)?\s+again\b', r'\bhear(?:ing)?\s+again\b',
        r'\bregained?\b', r'\brestored?\b',
    ]
    
    # Tier 3: General healing language (requires review, may be spiritual only)
    TIER3_PATTERNS = [
        r'\bmedical\s+miracle\b',
        r'\bunexplained\s+(?:recovery|healing|remission)\b',
        r'\bdoctors?\s+(?:were|was)\s+(?:amazed|shocked|surprised|baffled)\b.{0,100}\b(?:heal|recover|remission)\b',
    ]
    
    # Exclusion patterns (reduce false positives)
    EXCLUSION_PATTERNS = [
        r'\bspiritual\s+healing\s+(?:only|alone)\b',
        r'\bemotional\s+healing\b',
        r'\binner\s+healing\b',
        r'\bhealing\s+of\s+(?:relationships?|emotions?|grief|trauma|memories)\b',
        r'\bno\s+physical\s+healing\b',
        r'\bstill\s+(?:have|had|sick|ill|dying)\b',
    ]
    
    def __init__(self, source_dir: Path, output_dir: Path):
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.matches: list[HealingMatch] = []
        
        # Compile all patterns
        self.tier1_compiled = [re.compile(p, re.IGNORECASE | re.DOTALL) for p in self.TIER1_PATTERNS]
        self.disease_compiled = [re.compile(p, re.IGNORECASE) for p in self.DISEASE_TERMS]
        self.healing_compiled = [re.compile(p, re.IGNORECASE) for p in self.HEALING_OUTCOMES]
        self.tier3_compiled = [re.compile(p, re.IGNORECASE) for p in self.TIER3_PATTERNS]
        self.exclusion_compiled = [re.compile(p, re.IGNORECASE) for p in self.EXCLUSION_PATTERNS]
    
    def check_exclusions(self, content: str) -> bool:
        """Return True if content matches exclusion patterns."""
        for pattern in self.exclusion_compiled:
            if pattern.search(content):
                return True
        return False
    
    def extract_context(self, content: str, match: re.Match, window: int = 200) -> str:
        """Extract surrounding context for a match."""
        start = max(0, match.start() - window)
        end = min(len(content), match.end() + window)
        snippet = content[start:end]
        # Clean up snippet
        snippet = re.sub(r'\s+', ' ', snippet).strip()
        return f"...{snippet}..."
    
    def analyze_file(self, file_path: Path) -> Optional[HealingMatch]:
        """Analyze a single JSON file for healing content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error reading {file_path}: {e}")
            return None
        
        content = data.get('content', '')
        title = data.get('title', file_path.stem)
        
        if not content or len(content) < 100:
            return None
        
        # Check exclusions first
        if self.check_exclusions(content):
            return None
        
        matched_patterns = []
        context_snippets = []
        tier = None
        
        # Tier 1: Explicit remission patterns
        for pattern in self.tier1_compiled:
            match = pattern.search(content)
            if match:
                tier = 1
                matched_patterns.append(f"T1: {match.group()[:100]}")
                context_snippets.append(self.extract_context(content, match))
        
        # Tier 2: Disease + Healing combination
        if tier is None:
            has_disease = False
            has_healing = False
            disease_match = None
            healing_match = None
            
            for pattern in self.disease_compiled:
                match = pattern.search(content)
                if match:
                    has_disease = True
                    disease_match = match
                    break
            
            for pattern in self.healing_compiled:
                match = pattern.search(content)
                if match:
                    has_healing = True
                    healing_match = match
                    break
            
            if has_disease and has_healing:
                tier = 2
                if disease_match:
                    matched_patterns.append(f"T2-disease: {disease_match.group()}")
                if healing_match:
                    matched_patterns.append(f"T2-healing: {healing_match.group()}")
                    context_snippets.append(self.extract_context(content, healing_match))
        
        # Tier 3: General healing language
        if tier is None:
            for pattern in self.tier3_compiled:
                match = pattern.search(content)
                if match:
                    tier = 3
                    matched_patterns.append(f"T3: {match.group()}")
                    context_snippets.append(self.extract_context(content, match))
                    break
        
        if tier is not None:
            return HealingMatch(
                file_path=file_path,
                title=title,
                tier=tier,
                matched_patterns=matched_patterns,
                context_snippets=context_snippets
            )
        
        return None
    
    def scan_directory(self) -> list[HealingMatch]:
        """Scan all JSON files in the source directory."""
        json_files = list(self.source_dir.glob('*.json'))
        print(f"Scanning {len(json_files)} files in {self.source_dir}...")
        
        for file_path in json_files:
            match = self.analyze_file(file_path)
            if match:
                self.matches.append(match)
        
        # Sort by tier (highest confidence first)
        self.matches.sort(key=lambda m: m.tier)
        return self.matches
    
    def copy_matches(self, tiers: list[int] = [1, 2]) -> int:
        """Copy matched files to output directory."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        copied = 0
        for match in self.matches:
            if match.tier in tiers:
                dest = self.output_dir / match.file_path.name
                shutil.copy2(match.file_path, dest)
                copied += 1
        
        return copied
    
    def generate_report(self) -> str:
        """Generate a detailed report of findings."""
        lines = [
            "# Healing/Remission Case Filter Report",
            f"\nSource: {self.source_dir}",
            f"Total matches: {len(self.matches)}",
            "",
            "## Summary by Tier",
            f"- Tier 1 (HIGH confidence): {sum(1 for m in self.matches if m.tier == 1)}",
            f"- Tier 2 (MEDIUM confidence): {sum(1 for m in self.matches if m.tier == 2)}",
            f"- Tier 3 (LOW confidence): {sum(1 for m in self.matches if m.tier == 3)}",
            "",
            "---",
            ""
        ]
        
        for tier in [1, 2, 3]:
            tier_matches = [m for m in self.matches if m.tier == tier]
            if tier_matches:
                lines.append(f"## Tier {tier} Matches ({len(tier_matches)} cases)")
                lines.append("")
                for match in tier_matches:
                    lines.append(f"### {match.title}")
                    lines.append(f"**File**: `{match.file_path.name}`")
                    lines.append(f"**Confidence**: {match.confidence}")
                    lines.append(f"**Patterns matched**:")
                    for p in match.matched_patterns:
                        lines.append(f"- {p}")
                    if match.context_snippets:
                        lines.append(f"\n**Context**:")
                        for ctx in match.context_snippets[:2]:
                            lines.append(f"> {ctx}")
                    lines.append("")
        
        return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Filter NDE cases for healing/remission")
    parser.add_argument("source", help="Source directory containing JSON files")
    parser.add_argument("output", help="Output directory for matched files")
    parser.add_argument("--tiers", type=int, nargs="+", default=[1, 2],
                        help="Which tiers to copy (default: 1 2)")
    parser.add_argument("--report", help="Path to save report file")
    parser.add_argument("--dry-run", action="store_true",
                        help="Don't copy files, just report")
    
    args = parser.parse_args()
    
    source = Path(args.source)
    output = Path(args.output)
    
    if not source.exists():
        print(f"Error: Source directory {source} does not exist")
        return 1
    
    filter_instance = HealingCaseFilter(source, output)
    matches = filter_instance.scan_directory()
    
    print(f"\nFound {len(matches)} potential healing cases:")
    print(f"  Tier 1 (HIGH): {sum(1 for m in matches if m.tier == 1)}")
    print(f"  Tier 2 (MEDIUM): {sum(1 for m in matches if m.tier == 2)}")
    print(f"  Tier 3 (LOW): {sum(1 for m in matches if m.tier == 3)}")
    
    if not args.dry_run:
        copied = filter_instance.copy_matches(tiers=args.tiers)
        print(f"\nCopied {copied} files to {output}")
    
    if args.report:
        report = filter_instance.generate_report()
        Path(args.report).write_text(report, encoding='utf-8')
        print(f"Report saved to {args.report}")
    
    return 0


if __name__ == "__main__":
    exit(main())
