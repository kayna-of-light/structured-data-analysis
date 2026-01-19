# Mall World Extraction - Quick Reference Guide

**Last Updated**: January 19, 2026
**Schema Version**: v2.0 (Swedenborgian Phenomenology Engine)

---

## Critical Fixes from Analysis

### ✅ IMPLIED VERTICALITY (Flatness Artifact Fixed)

**Problem**: Old extraction showed 98.5% lateral movement (artifact from missing data)

**Solution**: System prompt now infers verticality from destination:

```
Basement/Cave/Underground → DOWN
Roof/Tower/Flying → UP
Check SpatialPosition.vertical changes
"Elevator to basement" = DOWN (even if not explicit)
```

### ✅ PRIVACY as Enum (Statistical Analysis)

**Problem**: privacy_level was Optional[str] (can't query statistically)

**Solution**: PrivacyStatus enum with 5 values:
- `PRIVATE` - Standard doors/walls
- `EXPOSED` - No doors, no walls, open concept
- `COMPROMISED` - Glass walls, broken locks
- `CROWDED_EXPOSURE` - Toilets in public view
- `NOT_MENTIONED`

### ✅ THWARTED INTENTION Mapping

**How to Extract**:
1. Create Interaction entry
2. Set `outcome = "prevented"`
3. Link to `somatic_response = "paralysis"/"heaviness"`
4. Description: "Tried to X but couldn't"

---

## Swedenborgian Markers Quick Reference

| Marker | Schema Field | Prompt Instruction |
|--------|--------------|-------------------|
| **Faith vs. Charity** | `light_temperature` | Warm/golden vs. cold/white |
| **Sphere Incompatibility** | `somatic_response` | Nausea, paralysis, glitching |
| **Ruling Love** | `affective_response` | Delight vs. disgust vs. indifference |
| **Flow vs. Effort** | `transit_mode` | Passive vs. directed_active vs. wandering |
| **Babylon Trap** | `reality_stability` | Plastic, shifting, decaying luxury |
| **Empty Intellect** | `intellectual_focus` | Archival, testing, argumentative |
| **Punishing Spirits** | `authority_nature` | Blocking, pursuing, punitive |
| **Shame/Nakedness** | `privacy_status` | Exposed, compromised, crowded_exposure |
| **Vertical Axis** | `MovementDirection` | **INFER from destination** |
| **State = Space** | `reality_stability.SHIFTING` | Non-Euclidean geometry |

---

## Extraction Command

```bash
python extract.py --max-concurrency 16 --log-level INFO
```

**Expected runtime**: ~4-6 hours for 3,748 posts

---

## Validation Checklist

Before re-extraction:
- [x] Schema validates (9 new enums)
- [x] PrivacyStatus enum added
- [x] privacy_status field replaces privacy_level
- [x] System prompt includes IMPLIED VERTICALITY
- [x] Thwarted Intention mapping detailed
- [x] Non-Euclidean geometry → reality_stability.SHIFTING
- [x] All phenomenological markers documented

---

## Expected Improvements Over Old Data

| Metric | Old Extraction | New Extraction (Expected) |
|--------|----------------|---------------------------|
| Light records | 1,461 (no temperature) | ~1,461 with warm/cold split |
| Vertical movement | 85 explicit (1.5%) | ~500+ inferred from destinations |
| Transit modes | Generic types | Passive/Active/Wandering/Fleeing |
| Affective tracking | None | Per-location emotional vectors |
| Somatic tracking | None | Per-location physical symptoms |
| Privacy tracking | Text only | Enum (statistical analysis) |
| Phantasy detection | Manual keywords | Schema-based (3 traps) |
| Non-Euclidean | Not captured | reality_stability.SHIFTING |

---

## Post-Extraction Analysis Updates

### Notebook Changes Needed

1. **Remove manual NLP passes** - now in schema:
   - Light temperature detection
   - Affect classification
   - Somatic markers

2. **Add new tests**:
   - H4: Vertical extremes (caves/towers) vs. affect intensity
   - H5: Privacy exposure vs. cleanliness (shame correspondence)
   - H6: Reality stability vs. luxury locations (Babylon trap)

3. **Update congruence calculation**:
   - Use transit_mode instead of manual active/passive detection
   - Vertical now includes inferred movements

4. **Phantasy detection**:
   - Query schema fields directly (no keyword matching)
   - Test combinations (luxury + shifting + cold_light)

---

## Key Theological Insights to Validate

1. **Elastic Tether Model**: Most on equilibrium plane, extremes stretch toward Heaven/Hell
2. **Faith-Charity Split**: Cold white light (fluorescent) vs. warm golden (sunlight)
3. **Sphere Compatibility**: Somatic distress in incompatible states
4. **Wandering vs. Direction**: World of Spirits (wandering) vs. Reformation (directed)
5. **Privacy = Internals**: Exposed bathrooms = externalized evils
6. **Non-Euclidean = State**: Spatial paradoxes prove space = state

---

## Troubleshooting

### If extraction fails:
1. Check Azure OpenAI credits/quotas
2. Reduce `--max-concurrency` to 8 or 4
3. Check model deployment name in secrets/azure_openai.env

### If results seem wrong:
1. Sample a few extractions manually
2. Check if privacy_status is being set (not just NOT_MENTIONED)
3. Verify verticality is inferred from location types
4. Look for thwarted intentions mapped to outcome=prevented

### If schema validation fails:
```bash
python -c "from models import MallworldResponse; print('OK')"
```

Should print "OK" - if not, check enum definitions in models/questionnaire.py

---

## Next Steps After Extraction

1. **Validate sample** - Check 10-20 extractions manually
2. **Run statistics** - Count populated fields vs. NOT_MENTIONED
3. **Update notebook** - Remove old NLP passes, add new tests
4. **Generate report** - Compare old vs. new extraction quality
5. **Validate theology** - Do patterns match Swedenborgian predictions?
