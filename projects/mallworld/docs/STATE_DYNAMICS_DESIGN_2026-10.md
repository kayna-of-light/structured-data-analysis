# State Dynamics in MallWorld: Design and Draft Pre-registration (October 2026)

**Status: DRAFT for review by the repository owner. This is not yet a registration.** It becomes the registration when it is committed with its status changed to "Registered", before `notebooks/10_state_dynamics_tests.ipynb` is written. No test in §5 has been computed. Measurement work is in `notebooks/09_state_measurement.ipynb`.

**Data:** the primary population of `scripts/mallworld_dataset.py` (1,918 dream reports, 8,685 locations, 1,303 authors). The existing GPT-5.2 extraction is used as it is; no re-extraction.

---

## 1. Why a redesign

The audited analyses (notebooks 02–07) answered the archived claims on their own terms. Three features of those terms were wrong for the framework being tested:
- **Pooling across visitors.** A location's atmosphere was averaged over everyone who reported it, whatever their state. Under the framework, how a place appears depends on the state of the one who is there. The height tests (M1, M2, M5, M8, M12) were of this kind.
- **Narrative readings.** Arcs, stage sequences and Markov "attractors" treat a report as a story with a template. The framework says nothing about story shapes; it speaks of states and their changes.
- **Single fields.** Each test used one coded field, although a state shows itself in several properties together.

**What is kept.**
- The verified loader, the populations and the reliability study.
- The scorecard M1–M14 in `CLAUDE.md` §6.5 remains the record of the simple tests. The height misses are **not** reclassified because a richer model could accommodate them. H6 below re-asks the height question in its conditional form, and is labelled as asked after the marginal result was seen.
- P1–P4 remain registered results.

## 2. The model, stated in advance

MallWorld is treated as a **common intermediate state** that each visitor experiences through his or her own state. The ontology stays a working hypothesis (`CLAUDE.md` §3): the question is what follows *if* it holds, and whether the data agree. Quotations follow J. C. Ager's translation of *Heaven and Hell* (*HH*).

1. **A common state, entered from one's own state.** Every person "even while he is living in the body, is in some society with spirits" (*HH* §438). The world of spirits is "an intermediate state", where all first meet, and people "are brought into one state after another, like those they experienced in the life of the body" (§§421–427).
2. **Space is state.** "Change of place is nothing else than change of state"; those in like states are near; the way "is lengthened and shortened in accordance with the desire" (§§192–195).
3. **What appears arises from state.** Things around spirits correspond to their interiors (§§173–176); a house and its contents correspond to the good of those who live there (§186).
4. **Influence comes from both directions, and choice decides which is followed.** Good descends from heaven and evil ascends from hell through the sphere around each person (§§590–591); "with every man there are spirits from hell and angels from heaven" (§599). The newly arrived are received by angels; one who "desires and seeks to get away from these angels" is left by them and "turns his face" toward his like (§548). Freedom is the ability "to choose one in preference to the other" (§597).
5. **Limits are asymmetric.** No one ascends beyond his state without "distress even to anguish", and he is "unable to see those who are there"; those raised higher are "prepared beforehand" and "encompassed by intermediate angels" (§35). Angels are sent down to moderate disturbances "by their presence" (§543); those not protected are set upon (§550).
6. **Good and light are as the experiencer sees them** (owner's principle, 2026-10-06). To those in hell "the light of heaven is thick darkness", and they see by a luminosity "as arises from burning coals" (*HH* §584). Evil spirits seek the stench that good spirits flee, because "as everyone in the world has been delighted with his own evil, so after death he is delighted with the stench to which his evil corresponds" (§429). One ascending beyond his state feels anguish (§35); the evil man "desires nothing so much as to be where his evil is" (§547). Whether an act is turning toward or away from the good therefore cannot be read from the act alone (fleeing, approaching); it depends on what the person treats as good.
7. **No degrees are assigned.** The analysis measures state and its change. It never assigns an observable to a degree (`CLAUDE.md` §5.1).

**What the model does not claim to observe.** A person's ruling love cannot be measured. The person's **choices** can, and how they go with the change of state is the observable trace (owner's proposal).

## 3. Measurement (notebook 09)

- **Scene state** at a location: the mean of up to seven scored properties (atmosphere, light, light temperature, cleanliness, state of the place, crowd behaviour, water). Available at 60.6% of locations. The items cohere (median pairwise ρ 0.365; every item–rest correlation positive) and do not track narrative length (r = +0.016).
- **Experiencer state:** the coded affect (somatic responses add little: 1.6% of locations). Available at 43.6% of locations.
- **The pre-specified scaling check failed as written.** The cause is diagnosed in notebook 09 (M2b): two near-equal dimensions, dominated by rare categories. Post hoc checks support the scoring. After the owner's principle (§3.1), the primary place measure is the scene state *without* atmosphere (Q: 3,882 locations; r with log words +0.091). Atmosphere enters only sensitivity analyses.
- **Transitions** (explicit connections, joined on `(post_id, location_id)`): 2,513 with a scene state at both ends (937 dreams); 1,726 with an experiencer state at both ends (720 dreams).
- **Choices:**
  - the mode of each movement: directed_active, passive, wandering, fleeing, instant, drifting, struggle;
  - the acts at a location: social, task, transaction, search, navigation, observation, escape, conflict.
- **Influences:** beings present at a location, by demeanor. Benign beings are present at 410 locations and hostile ones at 742.

### 3.1 Three things kept apart (after the owner's principle)

- **Place quality (Q):** what is coded about the place itself: light, light warmth, cleanliness, condition, crowd behaviour, water. This is the scene state *without* atmosphere. It is the closest the data come to "light" independent of the person.
- **The experiencer's evaluation (E):** the coded affect. It is how the person receives the place, not a measure of what is good.
- **What the experiencer treats as good (revealed):** the destinations of purposeful movement (`directed_active`) and the places fled (`fleeing`).

Atmosphere is the coder's reading of how a place feels; it mixes Q and E and is used only in sensitivity analyses. Entity demeanor is the experiencer's perception of a being, not the being's state.

**What the data contain** (notebook 09, M6):
- **Affect against quality.** Comfort or delight in a poor-quality place occurs at 35 locations in 32 dreams. Distress in a good-quality place occurs at 447 locations in 295 dreams; 108 of these are in clearly bright, clean or new places. Read in context, the first are mostly nostalgia and refuge ("reminiscent of stores from my childhood", a dirty store that "ends up being a safe zone"). The second are mostly driven by events (undead figures in a sunny field, a missing wallet). So affect alone does not reveal what a person sees as good.
- **Revealed choices with quality at both ends.** There are 1,522 transitions (663 dreams): 896 purposeful, in 461 dreams, and 125 flights, in 92 dreams. 208 dreams have at least two purposeful moves. Only 47 authors have such moves in two or more dreams.

## 4. Data acquisition and bias model

| Source of bias | Evidence in these data | Correction in every test |
|---|---|---|
| **Self-selection.** Posts come from people who recognised their dream in the community's theme | 48.9% of reports ask whether others share the experience | Within-dream and within-person contrasts; no prevalence claims about the general population |
| **Community contagion.** Reports may borrow the community's vocabulary and motifs | 42.8% use the name "mall world"; 13.1% mention childhood or long-standing onset | Bias check B1; stratify by onset and exposure markers |
| **One posting per person** | 78.7% of authors post once; 278 authors have ≥ 2 dreams | Person-level questions use only authors with ≥ 2 dreams, with permutation nulls |
| **Narrative length** | Longer reports code more of everything | Adjust for log word count; composites are means, not sums |
| **Same-source coding** | All variables are coded by one model from one text, often one sentence | Lagged designs (state at t → state at t+1); cross-dream designs for person-level questions |
| **Inferred ratings** | GPT-5.2 rates atmosphere and affect about twice as often as a blind second coder | Repeat on atmosphere alone; cite κ (0.75 atmosphere, 0.67 affect, where both rated) |
| **Prompt priming** | Framework meanings attached to light temperature, somatic distress, affect and transit mode | Sensitivity without primed items; state the priming in every result |
| **Nesting** | Locations and transitions are nested in dreams, and dreams in authors | Standard errors clustered by dream; bootstrap by dream or author |
| **Growing volume** | 27 dreams in 2021, 894 in 2025 | Era as a covariate in sensitivity analyses |

## 5. Questions and draft predictions

**Common rules.**
- **Model and data.** Linear models on the state measures (scale −1 to +1), with log word count as a covariate. Standard errors are clustered by dream unless stated. The unit is the explicit transition, joined on the full key.
- **Sensitivity.** Every test is repeated on list-order pairs, with dream fixed effects, with atmosphere added to Q, without the primed light-temperature item, and within the onset and exposure strata of B1.
- **Verdicts.**
  - **Hit:** the estimate is in the predicted direction with Holm-adjusted one-sided p < 0.05.
  - **Miss:** the estimate is in the opposite direction with a two-sided 95% CI that excludes zero, or the 90% CI lies within the stated margin of no effect (equivalence).
  - **Underdetermined:** otherwise.
- **Holm family:** H1, H2, H3 and H4. H5 and H6 are secondary. B1 is a bias check, not a framework test.

### H1 — Does the person lead the place, or the place the person? (primary)
- **Text:** what appears corresponds to the state of the one who is there (*HH* §§173–176, 186); change of place is change of state, and like is near like (§§192–193); the evil man "desires nothing so much as to be where his evil is" (§547).
- **Measure:** on transitions with Q and E at both ends, two cross-lagged models on standardised measures:
  - (A) Q at t+1 on Q at t and E at t;
  - (B) E at t+1 on E at t and Q at t.
- **Prediction:** the person leads. The effect of E on the next place's quality (from A) exceeds the effect of the place's quality on the next E (from B). The difference is tested with a dream-level bootstrap (2,000 resamples).
- **Margin of no effect:** ±0.05 SD.
- **Competing account:** ordinary perception, in which the place drives the feeling, predicts the reverse.
- **Already seen:** notebook 04 (R4) found that affect predicts the next *atmosphere* within dreams (OR 1.62). Nothing has been computed on Q, or in the reverse direction.
- **Bias note:** E is the less reliable measure (κ 0.67, one indicator). Its prior value is controlled less completely, which inflates the effect in (B). The bias works against H1.

### H2 — Does a person move toward what he or she treats as good? (primary)
- **Text:** good and light are as the experiencer sees them (§2, statement 6: *HH* §§35, 429, 547, 584).
- **Measure:**
  - **Orientation of a dream:** the Spearman correlation between E and Q over the dream's locations, leaving out the two ends of the transition being predicted. It is positive when the person feels better where the place is better, and zero or negative when not.
  - **Model:** on purposeful moves (`directed_active`) with Q at both ends in dreams with an estimable orientation, Q at the destination on Q at the origin, the orientation, and log words.
- **Prediction:** a more positive orientation goes with moving toward better places. People whose feelings run with the place's quality approach better places. People whose feelings do not run with it do not.
- **Margin of no effect:** ±0.05 SD per unit of orientation.
- **Competing account:** in ordinary dream psychology everyone moves toward better places when moving on purpose, and orientation does not matter.
- **Power:** comfort in poor places is rare (35 locations, notebook 09 M6), so few dreams will have a negative orientation. An underdetermined verdict is likely and will be reported as such.

### H3 — Is the influence of beings the experiencer perceives as benign perceptible? (primary)
- **Text:** the newly arrived are received by angels who "perform for him all good offices" (*HH* §548); angels moderate "by their presence" (§543).
- **Measure:** within dreams. Compare E at locations where a being perceived as benign is present with the same person's other locations in the same dream (dream fixed effects).
- **Prediction:** E is higher at those locations.
- **Margin of no effect:** ±0.10 on the −1 to +1 scale.
- **Reading:** demeanor is the experiencer's perception. The test therefore asks whether a presence the person receives as benign changes the person's state. It cannot say what the being is.
- **Competing account:** ordinary comfort from company predicts the same. This test establishes influence as experienced; it does not discriminate between explanations.
- **Also reported, not scored:** Q at the same contrast, and whether the benefit carries to the next location.

### H4 — Is what a person moves toward consistent across his or her dreams? (primary)
- **Text:** the ruling love persists (*HH* §§477–479), and a person goes where his love leads (§§547–548). The owner's proposal is to observe it through choices, not to infer it.
- **Measure:** on purposeful moves, the *direction of approach* is the destination's Q, residualised on the origin's Q. It is averaged per dream. Authors with purposeful moves in at least two dreams (up to 47) give a one-way ICC1 of the dream means, with 5,000 permutations of author labels across dreams.
- **Prediction:** ICC1 > 0.
- **Margin of no effect:** ICC1 within ±0.05.
- **Competing account:** a stable temperament or writing style predicts the same consistency, so a hit is not discriminating.
- **Power:** low.
- **Also reported, not scored:** the same ICC for flights.

### H5 — Common structure, personal state (secondary, descriptive)
- **Measure:** authors with at least two primary dreams (278 authors, 893 dreams). One-way ICC1 of:
  - (a) the dream's state: mean Q and mean E;
  - (b) the dream's structure: presence of each of the ten most common location types, and of escalator, elevator and stairs connections.
- **Status:** descriptive only. Under the model, a person returning to his or her own layout is the persistent state finding its own place (§§427, 547), not evidence against a common state. So a person-specific structure cannot count against the model, and this question cannot be scored.

### H6 — Height, conditional on state (secondary)
- **Text:** ascending beyond one's state brings anguish, because "the interiors of angels are what constitute heaven", not the place (*HH* §35).
- **Measure:** transitions upward (up, diagonal_up) or downward (down, diagonal_down) with E at both ends. Model: E at t+1 on E at t, direction, their interaction, and Q at t.
- **Prediction:** a positive interaction. Going up helps those already in a good state and not those in a poor one. Regression to the mean affects both directions alike, so the interaction is protected from it.
- **Already seen:** M2 (atmosphere by level, marginal) and C10 (direction and change in atmosphere, marginal). The interaction has not been computed. Power is low.

### Not tested: asymmetric limits
The asymmetry of ascent and descent (*HH* §§35, 543) needs to know what a being is. The data record only how the experiencer perceives it. The shares of perceived-benign and perceived-hostile beings by place quality are reported descriptively.

### B1 — Bias check: is the common structure contagion?
- **Measure:** compare the rates of the most common structural motifs across three splits:
  - reports that state childhood or long-standing onset (13.1%) vs the rest;
  - an author's first report vs later ones;
  - 2021–2023 vs 2024–2026.
- **Margin of equivalence:** ±10 percentage points per motif.
- **Reading:** if the motifs are as common in long-standing-onset reports, contagion is not the only source of the shared structure. If they are much rarer there, every claim about a common structure is qualified. This is not scored against the framework.

## 6. Decisions by the owner

- **Settled (2026-10-06).**
  - **Relative good.** "It depends on what the experiencer sees as light or good." Acts are therefore not classed as turning toward or away by their type. H2 and H4 read what a person treats as good from what he or she approaches, and the old asymmetry test is withdrawn.
  - **Measurement.** Compute state from several properties together; do not infer the ruling love; observe choices and how state changes with them; do not measure degrees.
- **Default unless the owner objects.**
  - **Recurrence.** A person returning to his or her own layout is read as an expression of a persistent state (H5 descriptive).
  - **The model in §2** is taken as confirmed.
