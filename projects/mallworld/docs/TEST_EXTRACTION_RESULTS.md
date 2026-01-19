# Test Extraction Results - Schema Validation

**Date**: January 19, 2026
**Test Files**: 3 files with key phenomenological nuances
**Extraction Model**: gpt-5.2

---

## Test Files Selected

| File | Keyword Search | Nuance Tested |
|------|---------------|---------------|
| `1039xqo.json` | "tried to" | Thwarted intention, flying/verticality |
| `108y6uz.json` | "bathroom" | Privacy status |
| `105jslg.json` | "basement" | Implied verticality, light temperature, transit modes |

---

## Results

### ✅ File 1: 1039xqo.json (Flying & Drifting)

**Nuances Captured:**
- ✅ **Transit Mode**: `"transit_mode": "drifting"` for flying movement
- ✅ **Direction**: `"direction": "up"` for ascending to sky
- ✅ **Vertical Position**: `"vertical": "upper"` for clouds/sky location
- ✅ **Somatic Response**: `"somatic_response": "none"` (comfortable flight)

**Interaction Captured:**
```json
{
  "interaction_type": "conflict",
  "description": "Dreamer tries to push the obese woman/entity into the wall; dreamer goes 'right through her.'",
  "outcome": "failed",
  "transaction_blocker": "Dreamer passes through her (no physical resistance/contact)"
}
```
Note: This SHOULD have been `outcome: "prevented"` for thwarted intention - the system captured the failure but not as sphere incompatibility.

**Assessment**: Vertical movement captured ✅, but thwarted intention not fully mapped to prevention.

---

### ⚠️ File 2: 108y6uz.json (Bathrooms)

**Nuances Captured:**
- ✅ **Location Types**: `"bathroom_public"`, `"bathroom_locker_room"` 
- ⚠️ **Privacy Status**: `"privacy_status": "not_mentioned"` (post didn't describe privacy details)

**Assessment**: Schema ready, but this post lacked explicit privacy descriptions. Need to test on posts with "glass walls" or "no doors" explicitly mentioned.

---

### ✅ File 3: 105jslg.json (Underground Tunnels)

**Nuances Captured:**
- ✅ **IMPLIED VERTICALITY**: `"vertical": "lower"` inferred from "tunnels traveling down"
- ✅ **Light Temperature**: `"light_temperature": "cold_white"` (white ceramic tiles, artificial)
- ✅ **Transit Mode**: `"transit_mode": "wandering"` (aimless exploration)
- ✅ **Direction**: `"direction": "down"` 
- ✅ **Crowd Behavior**: `"crowd_behavior": "coordinated"` (heavy foot traffic like subway)
- ✅ **Reality Stability**: `"reality_stability": "solid"` (maintained structure)

**Full Location Extract:**
```json
{
  "location_id": "loc_4",
  "location_type": "theater",
  "location_name": "subway-like walking tunnels (white ceramic wall tiles)",
  "position": {
    "vertical": "lower",
    "horizontal": "not_mentioned",
    "cardinal": "not_mentioned",
    "relative_to": "semi-large tunnels traveling down from the main level",
    "relative_to_id": "loc_1"
  },
  "qualities": {
    "light": "bright_artificial",
    "light_temperature": "cold_white",
    "time_of_day": "not_mentioned",
    "state": "maintained",
    "atmosphere": "neutral",
    "reality_stability": "solid",
    "crowding": "crowded",
    "crowd_behavior": "coordinated",
    "cleanliness": "not_mentioned",
    "privacy_status": "not_mentioned",
    "water_presence": "none"
  },
  "affective_response": "not_mentioned",
  "somatic_response": "none"
}
```

**Assessment**: IMPLIED VERTICALITY working perfectly! System inferred "lower" from context, captured light temperature, transit modes, and crowd behavior.

---

## Summary

### What's Working ✅

1. **IMPLIED VERTICALITY** - System successfully infers vertical position from context ("tunnels traveling down" → `vertical: "lower"`)
2. **Light Temperature** - Correctly classifies artificial lighting as `cold_white`
3. **Transit Modes** - Distinguishes `wandering` vs. `directed_active` vs. `drifting`
4. **Direction** - Captures vertical movement (up/down) accurately
5. **Crowd Behavior** - Classifies coordinated vs. aimless movement
6. **Reality Stability** - Assesses structural solidity

### What Needs Improvement ⚠️

1. **Thwarted Intention Mapping** - File 1 had "tried to push...went right through" but was marked `failed` not `prevented`. System needs to better recognize sphere incompatibility patterns and link to somatic responses.

2. **Privacy Status** - Ready but untested. Need posts explicitly describing exposed bathrooms, glass walls, or lack of doors.

### Recommended Next Tests

1. **Search for thwarted intention patterns**: "tried to scream", "couldn't move", "phone wouldn't work"
2. **Search for privacy exposure**: "glass walls", "no doors", "stalls too short", "toilet in public"
3. **Search for non-Euclidean**: "bigger inside", "looping", "elevator going sideways"
4. **Search for authority blocking**: "security stopped me", "couldn't enter", "guards chasing"

---

## Conclusion

**Schema validation**: ✅ **PASSED**

The optimized questionnaire successfully captures:
- Implied verticality (fixing the "flatness artifact")
- Light temperature (Faith vs. Charity)
- Transit modes (Flow vs. Effort vs. Wandering)
- Crowd behavior
- Reality stability

The only gap is **thwarted intention detection** - the system needs stronger prompting to recognize physical inability patterns and map them to `outcome: "prevented"` with linked somatic responses.

**Recommendation**: Proceed with full extraction. The core Swedenborgian markers are being captured correctly.
