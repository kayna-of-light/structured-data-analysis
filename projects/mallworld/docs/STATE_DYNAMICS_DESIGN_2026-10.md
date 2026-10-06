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
6. **No degrees are assigned.** The analysis measures state and its change. It never assigns an observable to a degree (`CLAUDE.md` §5.1).

**What the model does not claim to observe.** A person's ruling love cannot be measured. The person's **choices** can, and how they go with the change of state is the observable trace (owner's proposal).

## 3. Measurement (notebook 09)

- **Scene state** at a location: the mean of up to seven scored properties (atmosphere, light, light temperature, cleanliness, state of the place, crowd behaviour, water). Available at 60.6% of locations. The items cohere (median pairwise ρ 0.365; every item–rest correlation positive) and do not track narrative length (r = +0.016).
- **Experiencer state:** the coded affect (somatic responses add little: 1.6% of locations). Available at 43.6% of locations.
- **The pre-specified scaling check failed as written.** The cause is diagnosed in notebook 09 (M2b): two near-equal dimensions, dominated by rare categories. Post hoc checks support the scoring. Every test below is therefore repeated on atmosphere alone and on the scene state without atmosphere.
- **Transitions** (explicit connections, joined on `(post_id, location_id)`): 2,513 with a scene state at both ends (937 dreams); 1,726 with an experiencer state at both ends (720 dreams).
- **Choices:**
  - the mode of each movement: directed_active, passive, wandering, fleeing, instant, drifting, struggle;
  - the acts at a location: social, task, transaction, search, navigation, observation, escape, conflict.
- **Influences:** beings present at a location, by demeanor. Benign beings are present at 410 locations and hostile ones at 742.

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
- **Sensitivity.** Every test is repeated on atmosphere alone, on the scene state without atmosphere, on list-order pairs, with dream fixed effects, and within the onset and exposure strata of B1.
- **Verdicts.**
  - **Hit:** the estimate is in the predicted direction with Holm-adjusted one-sided p < 0.05.
  - **Miss:** the estimate is in the opposite direction with a two-sided 95% CI that excludes zero, or the 90% CI lies within the stated margin of no effect (equivalence).
  - **Underdetermined:** otherwise.
- **Holm family:** H1, H2, H3, H4 and H5. H6 is secondary. B1 is a bias check, not a framework test.

### H1 — Does the person's state lead what appears, or the reverse? (primary)
- **Text:** what appears corresponds to the state of the one who is there (*HH* §§173–176, 186); change of place is change of state (§192); a person in a given state seeks "to be where his evil is" (§547).
- **Measure:** on transitions with both states present at both ends, two cross-lagged models on standardised measures:
  - (A) scene state at t+1 on scene state at t and experiencer state at t;
  - (B) experiencer state at t+1 on experiencer state at t and scene state at t.
- **Prediction:** the person leads. The effect of the person's state on the next scene (from A) exceeds the effect of the scene on the person's next state (from B). The difference is tested with a dream-level bootstrap (2,000 resamples).
- **Margin of no effect:** ±0.05 SD.
- **Competing account:** ordinary perception, in which the environment drives emotion, predicts the reverse.
- **Already seen:** notebook 04 (R4) found that affect predicts the next atmosphere within dreams (OR 1.62). That is half of the comparison, on one field. The reverse direction and the comparison have not been computed.
- **Bias note:** the experiencer state is the less reliable measure (κ 0.67, one indicator). Its prior value is therefore controlled less completely, which inflates the effect in (B). The bias works against H1.

### H2 — Are the limits asymmetric? (primary)
- **Text:** the lower cannot ascend (*HH* §35); the higher are sent down to moderate "by their presence" (§543), and those raised up are mediated and protected (§35).
- **Measure:** use the scene state without atmosphere, to reduce overlap with the coding of the beings. Let R_b be the share of benign-being locations that are in negative scenes, divided by the share of all locations in negative scenes. Let R_h be the share of hostile-being locations that are in positive scenes, divided by the share of all locations in positive scenes.
- **Prediction:** benign beings enter negative scenes more freely than hostile beings enter positive ones: R_h < R_b. The test uses a dream-level bootstrap of log(R_b / R_h).
- **Margin of no effect:** ratio within 1/1.15–1.15.
- **Competing account:** symmetric valence congruence (good with good, bad with bad) predicts R_h ≈ R_b.
- **Already seen:** notebook 03 (E2) gave negative-atmosphere shares by entity type, on atmosphere. Nothing is computed on the composite without atmosphere, or as this asymmetry.
- **Proxy:** demeanor stands in for good and evil beings. Ordinary friends count as benign.

### H3 — Is the influence of benign beings perceptible? (primary)
- **Text:** the newly arrived are received by angels who "perform for him all good offices" (*HH* §548); angels moderate "by their presence" (§543).
- **Measure:** within dreams. Compare the experiencer state at locations where a benign being is present with the same person's other locations in the same dream (dream fixed effects).
- **Prediction:** higher at the benign locations.
- **Margin of no effect:** ±0.10 on the −1 to +1 scale.
- **Competing account:** ordinary comfort from company predicts the same. This test establishes influence; it does not discriminate between explanations.
- **Also reported, not scored:** the scene state at the same contrast, and whether the benefit carries to the next location.

### H4 — Does the way a person chooses go with the way the state changes? (primary)
- **Text:** turning toward or away decides which influence a person follows (*HH* §548); freedom is the ability to choose (§597); one arrives as one desires (§195).
- **Measure (cross-dream, to remove same-text coupling):** authors with transitions in at least two dreams (122). A person's **choice style** is computed from his or her *other* dreams: the share of engaging choices among engaging and avoiding choices.
  - **Engaging:** directed_active movement; social, task, transaction, search and navigation acts.
  - **Avoiding:** fleeing; escape acts.

  The **outcome** is the mean change in scene state across the held-out dream's transitions.
- **Prediction:** a more engaging choice style goes with a more improving change of state. The test is the correlation across held-out dreams, against 5,000 permutations of author labels.
- **Margin of no effect:** ρ within ±0.10.
- **Also reported, not scored:** at the transition level, whether movement mode and acts explain the next state beyond the prior states (omnibus Wald test). Ordinary accounts also predict that choices matter here, and with this many transitions significance is cheap.
- **Owner to confirm:** which choices count as turning toward and away (§6).

### H5 — Common structure, personal state? (primary)
- **Text:** a common intermediate state where all meet (*HH* §§421–427); what appears corresponds to each person's state (§§173–176).
- **Measure:** authors with at least two primary dreams (278 authors, 893 dreams). One-way ICC1 of:
  - (a) the dream's **state**: mean scene state and mean experiencer state;
  - (b) the dream's **structure**: presence of each of the ten most common location types and of escalator, elevator and stairs connections, averaged over features.
- **Prediction:** the person accounts for more of the state than of the structure: ICC(state) > ICC(structure). The test uses an author-level bootstrap.
- **Margin of no effect:** ±0.02.
- **Competing account:** a recurring personal place (the same person returns to his or her own layout) predicts ICC(structure) ≥ ICC(state).
- **Already seen:** P4's ICC1 of atmosphere was 0.094. ICC1 of the composites and of structure have not been computed.
- **Owner to confirm:** how recurrence fits the model (§6).

### H6 — Height, conditional on state (secondary)
- **Text:** ascending beyond one's state brings anguish, because "the interiors of angels are what constitute heaven", not the place (*HH* §35).
- **Measure:** transitions upward (up, diagonal_up) or downward (down, diagonal_down) with an experiencer state at both ends. Model: experiencer state at t+1 on experiencer state at t, direction, their interaction, and scene state at t.
- **Prediction:** a positive interaction. Going up helps those already in a good state and not those in a poor one. Regression to the mean affects both directions alike, so the interaction is protected from it.
- **Already seen:** M2 (atmosphere by level, marginal) and C10 (direction and change in atmosphere, marginal). The interaction has not been computed. Power is low (about 1,000 vertical connections before the requirement for states at both ends). The verdict is reported but not scored on the main scorecard unless it is a hit or a miss with adequate precision.

### B1 — Bias check: is the common structure contagion?
- **Measure:** compare the rates of the most common structural motifs across three splits:
  - reports that state childhood or long-standing onset (13.1%) vs the rest;
  - an author's first report vs later ones;
  - 2021–2023 vs 2024–2026.
- **Margin of equivalence:** ±10 percentage points per motif.
- **Reading:** if the motifs are as common in long-standing-onset reports, contagion is not the only source of the shared structure. If they are much rarer there, every claim about a common structure is qualified. This is not scored against the framework.

## 6. Decisions for the owner before registration

1. **Model.** Are statements 1–6 in §2 a faithful account of how the framework works? What is wrong or missing?
2. **Choices (H4).** Is "engaging vs avoiding" the right reading of "the way someone chooses"? In particular, should fleeing from a threatening place count as turning away? The texts speak of turning away from the good (§548), not of fleeing from danger.
3. **Beings (H2, H3).** Is demeanor (benign vs hostile) an acceptable stand-in for beings of a higher or lower state?
4. **Recurrence (H5).** 68.7% of reports describe a recurring visit. Under the model, is a person returning to his or her own layout an expression of the common state, or evidence against it? The answer decides what H5 can test.
