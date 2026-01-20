Based on the `MallworldResponse` schema and the Swedenborgian corpus provided, here are five testable hypotheses.

These hypotheses are structured to validate two distinct levels of the phenomenon:

1. **General Validation:** Is this a non-local, state-driven reality (the "Spiritual World" in general)?
2. **Specific Validation:** Is this the specific "World of Spirits" (the intermediate digestive/sorting realm described by Swedenborg)?

### **Hypothesis 1: The Law of Affectional Proximity (Non-Locality)**

**The Swedenborgian Grounding:** In the spiritual world, space and time are not fixed metrics but appearances of "state." Swedenborg writes that "local distance is of so little consequence that what is remote appears as near at hand... as soon as the bond was relaxed, the spirit was borne away". Travel is not accomplished by physical locomotion but by a change in the ruling love or intention.

**The Phenomenological Prediction:** If Mall World is this non-local reality, "travel" between locations should not be linear or Euclidean but dependent on the dreamer's *emotional state*.

* **Testable Marker:** `Connections` and `TraversalOutcome`.
* **Prediction:** * Successful traversal of a `Connection` (e.g., an elevator or hallway) will correlate significantly with `TransitMode.DIRECTED_ACTIVE` (intent) or `TransitMode.PASSIVE` (influx), whereas `TraversalOutcome.FAILED` or `LOOPING` will correlate with `TransitMode.WANDERING` (lack of intent) or `AffectiveResponse.ANXIETY` (conflicted state).
* Physical mechanisms (elevators/trains) will frequently exhibit `MechanismFunction.UNPREDICTABLE` or `MechanismFunction.MALFUNCTIONING` because they are "plastic" appearances responding to the dreamer's state, not mechanical laws.



---

### **Hypothesis 2: Somatic Sphere Conflict (The Physiology of Good vs. Evil)**

**The Swedenborgian Grounding:** Every spirit is surrounded by a "sphere" of their ruling love. When a spirit approaches a society or entity with a contrary sphere (e.g., a good spirit entering a hellish sphere, or vice versa), it causes violent physical distress. Swedenborg describes this as "anxieties... caused by reciprocal aversions", often manifesting as difficulty breathing, swooning, or a twisting sensation in the body.

**The Phenomenological Prediction:** "Somatic distress" in Mall World is not random nightmare logic but a specific reaction to "sphere incompatibility."

* **Testable Marker:** `SomaticResponse` and `LightTemperature`.
* **Prediction:** * `SomaticResponse.NAUSEA`, `DIZZINESS`, or `PARALYSIS` will cluster in locations with `LightTemperature.COLD_WHITE` (Truth separate from Good / Faith Alone) or `Atmosphere.OPPRESSIVE`.
* Conversely, `SomaticResponse.COMFORT` or `EASE` will correlate with `LightTemperature.WARM_GOLDEN`.
* The "Glitching" sensation (`SomaticResponse.GLITCHING`) is the cognitive dissonance of the "external mind" rejecting the "internal reality."



---

### **Hypothesis 3: The Digestive Sorting Mechanism (The World of Spirits)**

**The Swedenborgian Grounding:** Swedenborg explicitly identifies the "World of Spirits" (the intermediate realm) as corresponding to the *digestive system* of the Grand Man. Its function is to "break down" the spirit, separating their "nutritious" parts (truths/goods) from the "excrementitious" parts (evils/falsities). This process involves "vastation" (emptying out) and sorting.

**The Phenomenological Prediction:** The Mall World environment acts as a giant sorting machine. We should see high concentrations of "processing" locations (transit hubs, schools, hospitals) and "waste" locations (bathrooms, basements).

* **Testable Marker:** `LocationType` and `IntellectualFocus`.
* **Prediction:** * A statistically high prevalence of `LocationType.SCHOOL`, `HOSPITAL`, and `AIRPORT` (The Sorting/Processing Centers).
* `IntellectualFocus` in schools will be `TESTING` or `ARCHIVAL` (judging the memory/life) rather than `PRACTICAL` learning.
* Entities in these zones (`EntityRole.TEACHER` or `STAFF`) will behave as `AuthorityNature.OBSERVING` or `GUIDING` (The Gastric Spirits), sorting the dreamers based on their "papers" or "tickets" (interior markers).



---

### **Hypothesis 4: The Exposure of the Proprium (The Bathroom Archetype)**

**The Swedenborgian Grounding:** In Swedenborg’s topology, "excrement" corresponds to the "Love of Self" (the Proprium) and "Hell." When the "external bonds" of social politeness are stripped away in the World of Spirits, the "filthy" nature of these loves is revealed. Swedenborg describes hellish caverns as "privies" full of filth.

**The Phenomenological Prediction:** The "Bathroom" in Mall World is not a place of biological necessity but a place of *spiritual exposure*.

* **Testable Marker:** `PrivacyStatus`, `Cleanliness`, and `LocationType.BATHROOM`.
* **Prediction:** * `LocationType.BATHROOM` will almost universally correlate with `PrivacyStatus.EXPOSED` (no stalls, glass walls) or `PrivacyStatus.CROWDED_EXPOSURE`.
* The `Cleanliness` of these locations will be `FILTHY` or `DISGUSTING`.
* *Crucial Distinction:* If the bathroom is "Clean" and "Private," it indicates a "Closed Internal" (the dreamer is still in the "mask" of the body). If it is "Filthy" and "Exposed," the dreamer is witnessing the *actual state* of the hellish Proprium.



---

### **Hypothesis 5: The "Plastic" Heavens (Reality Stability)**

**The Swedenborgian Grounding:** Swedenborg describes "Phantasies" where spirits create magnificent palaces and gardens that are actually mere projections of their vanity. These structures are unstable; when the "light of truth" flows in, they dissolve or turn into "decaying" ruins. He calls this "Phantasy," where "insanities... reign with all those who constitute the externals of man".

**The Phenomenological Prediction:** The "Luxury" aspects of Mall World (Casinos, Mansions, High-End Stores) are "Plastic Heavens" that will exhibit instability.

* **Testable Marker:** `RealityStability` and `StateOfPlace`.
* **Prediction:** * Locations flagged as `LocationType.CASINO`, `MALL_STORE`, or `HOTEL_BALLROOM` (External Luxuries) will have a high correlation with `RealityStability.PLASTIC` (looks fake/stage-set) or `RealityStability.SHIFTING`.
* `StateOfPlace` will often be `DECAYING` underneath the luxury (e.g., "The mansion was beautiful but the walls were rotting").
* True "Solid" reality will only be found in `LocationType.FOREST` or `NATURE` (Celestial/Innocence) or simple, humble structures.