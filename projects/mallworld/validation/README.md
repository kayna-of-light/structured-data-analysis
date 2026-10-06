# Second-coder validation set (MallWorld)

`second_coder_codes.jsonl` holds the blind second coding used by `notebooks/08_extraction_reliability.ipynb` to measure how reproducible the GPT-5.2 extraction is. The codes were committed before any comparison with the extraction was run.

## Samples

| Set | Dreams | How drawn |
|---|---|---|
| A | 50 (253 locations) | `np.random.default_rng(20261008).choice(np.sort(primary["post_id"].values), 50, replace=False)` over the 1,918 primary dream reports of `mallworld_dataset.load_posts()` |
| B | 69 | Every dream that contributes to the pre-registered tests P1 (27 dreams with a noxious-animal location) and P3 (18 dreams with a deceased-person location), plus 27 of the 81 gentle-animal dreams drawn with `default_rng(20261009)`. Read in an order shuffled with `default_rng(1)` |

One dream is in both sets. Set B is selected on the extraction's codes, so the coder knew that each dream contained an animal or a deceased person somewhere. The coder did not know which location carried it, or which class it was. The notebook re-draws both samples and asserts that they match the coded dreams.

## Procedure

The second coder (Claude) saw the text GPT-5.2 received: title and body. It never saw an extracted value, except for one alignment aid. For each dream it saw the list of extracted locations, with their `location_id`, `location_type` and `location_name`, so that codes could be attached to the same locations. Images, which GPT-5.2 also received, were not available.

The codebook was the enum values and `Field(description=...)` text in `models/questionnaire.py`, plus the extraction prompt in `extract.py`. Dreams were read in full, in batches of five or six. Codes were appended to the file after each batch. No code was revised after the comparison.

## Fields

| Set | Field | Values | GPT-5.2 counterpart in notebook 08 |
|---|---|---|---|
| A | `atm` | schema `atmosphere` values | `atmosphere` (also collapsed to the loader's valence) |
| A | `vert` | schema `vertical` values | `vertical` |
| A | `light` | schema `light` values | `light` |
| A | `affect` | schema `affective_response` values | `affective_response` |
| A | `threat` | 0/1: an entity hostile to the dreamer or to others | any entity of type `threat` in the dream |
| A | `deceased` | 0/1: a person the dreamer knew, who has died, appears | any entity of type `deceased` in the dream |
| A, B | `animals` | living animals present in the scene (list) | the pre-registered gentle and noxious word lists applied to extracted entity and location text |
| B | `atm`, `animals`, `deceased_here` | per location | `valence`, word-list class, entity type `deceased` at the location |
| A | `image_only` | true when the text has no dream content beyond attached images | excluded from agreement statistics |
| all | `note` | free text: the coder's one-line summary of the evidence | — |

## Coder conventions where the schema is silent

These are reported because several disagreements may come from them, not from misreading:

- **Atmosphere.** Coded only when the text gives affective information about the place, such as "eerie", "felt dangerous" or "cozy". Otherwise `not_mentioned`. A place where something hostile happens is `threatening`. Empty, uncanny or "watched" places are `eerie`. Fake, physically impossible or "off" places are `wrong`. Dirty, cramped or embarrassing places are `uncomfortable`. Dark, gloomy, suffocating places are `oppressive`.
- **Vertical.** Coded from explicit level words or from places that are levels by definition:
  - basement → `lowest`;
  - attic, roof or "the top" → `uppermost`;
  - upstairs, second floor or upper floors → `upper`;
  - underground or tunnels under a building → `lower`;
  - "downstairs" → `lower`;
  - ground or main floor, and outdoor places at street level → `ground`.

  A house "on a hill" is not coded; a plateau described as "above" is `upper`. Subway stations and parking garages are not coded unless a level is stated.
- **Light.** Only literal descriptions of light, never "dark" as a mood.
- **Affect.** The dreamer's stated reaction to the place. "Beautiful" or "so cool" → `delight`; "cozy", "at peace" or relief → `comfort`; "trying to figure out where to go" → `confusion`.
- **Animals.** Living animals present in the scene. Not counted:
  - toys, pictures, wallpaper, models, taxidermy and food;
  - similes ("like rats", "like an insect hive");
  - names ("Dancing Spiders"), and creatures with animal heads ("toad-headed dream makers");
  - animals that are only feared or explicitly absent ("worried there were rats", "zero spiders");
  - word fragments ("worm hole", "dog park", "fish" as a verb).

  Dead fish for sale were listed and noted. Pets present in the scene count, including a pet the dreamer knows has died.
- **Deceased.** A person the dreamer knew, stated to have died, who appears. Unknown dead people (a dead rapper, "noble men of the past", a long-dead woman) are not counted. A deceased relative seen as a corpse was counted and noted.
- **Threat.** An entity that attacks, chases, abducts or threatens. Unfriendly or annoyed staff are not a threat.

## Limitations

- **Not ground truth.** The second coder is a language model from a different family, not a human. Agreement statistics measure reproducibility; they do not say which coder is right. There is no third coder to adjudicate.
- **Framework awareness.** The coder knew the research framework and the pre-registered predictions.
- **Images.** It did not see images. Two dreams in set A are image-only.
