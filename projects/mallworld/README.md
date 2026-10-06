# MallWorld Analysis Project

Structured analysis of recurring "Mall World" dream reports from r/TheMallWorld. Swedenborg's correspondences are used as the hypothesis generator (see the repository `CLAUDE.md`, §§3–4 and §9).

> **Audit, October 2026.** The analyses and reports written before October 2026 have been withdrawn and moved to `notebooks/archive/` and `reports/archive/`. See `docs/STATISTICAL_AUDIT_2026-10.md` for every withdrawn figure and its correction. Cite only the current reports and notebooks below.

## Data

| Item | Count |
|---|---|
| Posts scraped (`data/mallworld/`) | 3,743 files |
| Posts extracted (GPT-5.2, `structured/`) | 3,732 |
| Primary population: dream reports with ≥ 1 location, exact duplicates removed | 1,918 dreams, 8,685 locations, 1,303 authors |

**Use the verified loader** `scripts/mallworld_dataset.py`, never ad-hoc JSON parsing. It:
- checks every comparison against the schema (`mw.isin`, `mw.has`, `mw.check_values`);
- keys entities, interactions and connections by `(post_id, location_id)`, because `location_id` repeats across dreams;
- defines the populations (`primary`, `extractable`, `all`);
- provides dream-clustered regression (`mw.clustered_logit`).

## Notebooks (executed top to bottom)

| Notebook | Content |
|---|---|
| `01_data_audit` | Populations, narrative length, nesting, coverage, prompt priming, the join bug, duplicate test–retest |
| `02_spatial_affective_correspondences` | Height, water, light, cleanliness, exposure, somatic distress, location type, movement |
| `03_entities_and_animals` | Entity census, entity "autonomy", entities by height, interactions, animals |
| `04_sequences_and_dreamer_effects` | Entries and exits, loops, Markov chains, arcs, variance components, archived ruling-love tests |
| `05_robustness_time_and_nde_comparison` | Author and time robustness, MallWorld vs NDE atmosphere |
| `06_exploratory_report_claims` | Claims of the archived exploratory report |
| `07_preregistered_correspondence_tests` | Tests registered in `docs/PREREGISTRATION_2026-10.md` |
| `08_extraction_reliability` | Blind second coding of 119 dreams (`validation/`) |
| `09_state_measurement` | State-dynamics redesign: scene and experiencer state measures, transitions, choices and influences (measurement only) |
| `10_state_dynamics_tests` | Registered state-dynamics tests (H1–H4), secondary analyses and the contagion check |

## State-dynamics redesign

`docs/STATE_DYNAMICS_DESIGN_2026-10.md` (registered, commit `6be44a3b`) treats MallWorld as a common intermediate state experienced through each visitor's own state. It asks how state evolves: who or what influences it, what arises from it, and how the person's choices go with its change.

**Results (notebook 10):**
- the person's state leads the next place, and not the reverse (**hit**);
- a presence perceived as benign is felt (**hit**, not discriminating);
- whether people move toward what they treat as good is untested: the registered index was a **miss** and did not measure orientation;
- consistency of approach across a person's dreams is **underdetermined**;
- the shared motifs are not mainly community contagion.

## Reports

- *Spatial Correspondences in MallWorld Dreams: A Corrected Re-analysis of Height, Water, Light and Exposure*
- *Entities, Animals and Narrative Dynamics in MallWorld Dreams: A Corrected Re-analysis*
- *Pre-registered Correspondential Tests in MallWorld Dreams: Animals, the Deceased and Ruling Love*
- *Reliability of MallWorld Dream Coding: Blind Second Coding of 119 Dream Reports*
- *State Dynamics in MallWorld Dreams: Registered Tests of Who Leads, What Is Approached and Perceived Influence*

The Markdown files in `reports/` are the source of truth. Regenerate the LaTeX with:

```bash
python ../nde/scripts/md_to_latex.py --project mallworld
```

## Main results (October 2026)

**Hits** (pattern fit):
- turbid water, darkness, cold light and exposure go with negative atmospheres;
- pre-registered: noxious animals appear in negative scenes (P1);
- pre-registered: the deceased appear in less negative scenes than living acquaintances (P3);
- pre-registered: a person's dreams share an atmosphere (P4).

**Partial hit:** below ground is worse than ground.

**Misses** (all concern height; each prediction is located in Swedenborg's text, see the audit §5):
- above ground is not better than ground;
- warm light is not more common above;
- noxious animals are not more common below (P2);
- authority functions do not follow height.

**Not observed, and not a framework prediction:** a characteristic arc of scenes within a dream.

**Withdrawn:** see the audit. These include the elevation gradient ρ = 0.25–0.30, entity "autonomy", animals "independent of atmosphere", "dreamer explains 56.4%", and the four "archetypes".

Every hit is also predicted by ordinary associations, and all variables are coded from the same narrative. The measured reliability of each field is in the reliability report.

## Usage

```bash
# Scrape (full history via Reddit API + PullPush)
python -m shared.scrapers.reddit_scraper --subreddit TheMallWorld --dataset mallworld --historical --chunk-days 30

# Extract
cd projects/mallworld && python extract.py --datasets mallworld --max-concurrency 4

# Test the loader and re-execute the notebooks
python -m pytest projects/mallworld/tests
cd projects/mallworld/notebooks && jupyter nbconvert --to notebook --execute --inplace 0*.ipynb
```

## Known limitations of the extraction

- **Primed fields.** The extraction prompt attaches framework meanings to several fields: warm light "indicates Charity/Good", exposure is "shameful" or "hellish", and verticality is inferred from location type. Treat associations on these fields as primed.
- **Inferred coverage.** GPT-5.2 rates atmosphere, level and affect about twice as often as a coder who requires explicit statements. Prevalence is convention-dependent.
- **Few cardinal directions.** Cardinal directions are coded in 33 dreams, so the East–West framing cannot be tested.

## Related

- [Framework documentation](../../README.md)
- [Literary Compilation](https://github.com/kayna-of-light/literary-compilation): theoretical framework
