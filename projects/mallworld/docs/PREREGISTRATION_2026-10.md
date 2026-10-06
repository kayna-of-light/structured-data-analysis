# Pre-registration: Correspondential Predictions in MallWorld Dreams (October 2026)

**Registered:** 2026-10-06, committed to git before the confirmatory notebook was written or run.
**Analysis notebook (to be written after this commit):** `notebooks/07_preregistered_correspondence_tests.ipynb`
**Data:** primary population of `scripts/mallworld_dataset.py` (1,918 dream reports with at least one location, exact duplicates removed). The extraction is final; no data will be added or recoded for these tests.

## Why a new pre-registration

The archived "pre-registered" plan (`correspondential_falsification_test_plan_20260120.md`) was written on 2026-01-20 at 14:59. The vertical, entity, sequence and exploratory reports had been committed earlier the same day. Its hypotheses H1–H3 restated patterns the analyst had already seen. This document registers predictions on relations that have **not** been estimated correctly in this project:

- The archived animal–atmosphere test used a join that attached each animal to locations from other dreams (audit notebook 01, D6), so its result carries no information.
- The deceased-entity figures rest on 27 coded encounters in an older population.
- Author-level consistency was never separated from within-dream clustering.

The analyst has read the archived claims, which are listed under each prediction, but has **not** computed any of these tests on the primary population with correct methods.

## Framework grounding

- **Animals.** Swedenborg's general rule is that animals correspond to affections: gentle and useful animals to good affections, fierce and harmful ones to evil affections (*Heaven and Hell* §110). In the spiritual world, appearances, animals among them, represent the affections of those present (*Heaven and Hell* §110; on surroundings corresponding to interiors, §§173–176). If the MallWorld environment expresses the state of the scene, harmful animals should appear where the scene is evil-toned, and gentle animals where it is good-toned.
- **The deceased.** After death people meet friends and acquaintances (*Heaven and Hell* §494), and the newly arrived are first attended by angels with kindness (*Heaven and Hell* §§449–450).
- **Ruling love.** A person's ruling love persists (*Heaven and Hell* §§477–479), and the surroundings of a spirit correspond to its interiors (*Heaven and Hell* §§173–176). A person should therefore meet similar atmospheres across different dreams.

## Operational definitions (fixed now)

**Outcome (P1–P3):** the location atmosphere. It is *negative* if `atmosphere` is threatening, oppressive, uncomfortable, wrong, eerie or chaotic, and *non-negative* if neutral, welcoming or peaceful. Nostalgic and not-mentioned locations are excluded. This is the loader's `valence` (−1 vs 0/+1).

**Animal classes.** A location carries an animal class if a word in the class list (whole-word match, case-insensitive) appears in either:
- the `entity_description` or `name_or_relation` of any entity involved in an interaction at that location; or
- the location's `raw_description`.

The class lists:
- **Gentle** (tame or useful): cat, cats, kitten, kittens, kitty, dog, dogs, puppy, puppies, sheep, lamb, lambs, horse, horses, pony, cow, cows, cattle, calf, deer, fawn, rabbit, rabbits, bunny, bunnies, bird, birds, dove, doves, chicken, chickens, duck, ducks, swan, swans, fish, goldfish, dolphin, dolphins, butterfly, butterflies, squirrel, squirrels, hamster, turtle, turtles, owl, owls.
- **Noxious** (fierce or harmful): snake, snakes, serpent, serpents, spider, spiders, rat, rats, mouse, mice, cockroach, cockroaches, roach, roaches, insect, insects, bug, bugs, ant, ants, wasp, wasps, hornet, hornets, scorpion, scorpions, worm, worms, maggot, maggots, leech, leeches, wolf, wolves, shark, sharks, crocodile, crocodiles, alligator, alligators, bear, bears, lion, lions, tiger, tigers, hound, hounds, hyena, hyenas, vulture, vultures, predator, predators.

The phrase "hot dog(s)" is removed before matching. A location matching both classes is excluded from P1 and P2. Monsters, dragons, demons, aliens and robots are not animals and are not classified.

**Deceased vs living known persons (P3):** the entity types present at a location (via interactions):
- *deceased* if any entity is `deceased`;
- *living known* if none is `deceased` and any is `known_person`, `family_member` or `friend`.

**Author consistency (P4):** authors with at least two primary dreams in which at least one location has a valence. The dream score is the mean valence of its coded locations.

## Predictions

| # | Prediction | Test | Counts as a hit | Counts as a miss |
|---|---|---|---|---|
| **P1** (primary) | Locations with noxious animals are more often negative than locations with gentle animals | Logistic regression of negative atmosphere on noxious (vs gentle), adjusted for log word count; SEs clustered by dream | OR > 1 and Holm-adjusted one-sided p < 0.05 | OR ≤ 1, or adjusted p ≥ 0.05 |
| **P2** (secondary) | Locations with noxious animals are more often underground than those with gentle animals | As P1 with outcome "vertical level < 0", among locations with a vertical level | OR > 1, one-sided p < 0.05 (not in the Holm family) | Otherwise; if fewer than 10 noxious locations have a vertical level, **underdetermined** |
| **P3** (primary) | Locations where a deceased person appears are less often negative than locations with living known persons only | As P1 with predictor deceased (vs living known) | OR < 1 and Holm-adjusted one-sided p < 0.05 | OR ≥ 1, or adjusted p ≥ 0.05 |
| **P4** (primary) | Authors meet consistent atmospheres across different dreams | One-way ICC of dream scores within authors; p from 5,000 permutations of author labels across dreams | ICC > 0 and Holm-adjusted permutation p < 0.05 | ICC ≤ 0, or adjusted p ≥ 0.05 |

The Holm family is P1, P3 and P4 at α = 0.05, one-sided in the predicted direction.

## Pre-stated limits on interpretation

- **Non-discrimination.** P1 and P3 are also predicted by ordinary associations (vermin are unpleasant; deceased loved ones are emotionally significant). P4 is also predicted by stable writing style or temperament. A hit supports pattern fit with the framework. It does not distinguish the framework from these alternatives. A miss counts against the framework's prediction regardless.
- **Same-source coding.** Animals and atmosphere are coded from the same text, often the same sentence. The atmosphere code depends on GPT-5.2 and on the extraction prompt, which was primed on other fields but did not mention animals.
- **Sensitivity analyses.** These are reported but do not change the verdict: excluding entities of type `threat`; animals detected from entity descriptions only; adding location type as a covariate.
- **No other tests.** Any other comparison in notebook 07 is labelled exploratory.
