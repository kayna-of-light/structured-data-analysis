# Second-coder validation set

`second_coder_codes.jsonl` holds the blind second coding used by `notebooks/08_extraction_reliability.ipynb` to measure how reproducible the GPT-5.2 extraction is.

## Samples

| Set | Accounts | How drawn |
|---|---|---|
| A | 100 | `np.random.default_rng(20261006).choice(df["file"], 100, replace=False)` over all 6,751 records from `nde_dataset.load_frame()` |
| B | 44 | 40 drawn with `default_rng(20261007)` from the 428 life reviews GPT-5.2 rated on judgment intensity, plus all 6 rated `harsh_condemning` (2 already drawn) |

Three accounts are in both sets. The notebook re-draws both samples and asserts that they match the coded accounts.

## Procedure

The second coder (Claude) saw only the text GPT-5.2 received: dataset, title, reported date, narrative. It never saw any extracted value. The codebook was the `Field(description=...)` text and enum values in `models/questionnaire.py`. Accounts were read in full, in small batches, and their codes were appended to the file before any comparison with the extraction was run. No code was revised after the comparison.

## Fields

| Field | Values | GPT-5.2 counterpart used in notebook 08 |
|---|---|---|
| `light` | schema `light_encounter` values | `light_encounter` |
| `unknown` | 0/1: an unidentified being or presence anywhere in the account | `unknown_presence` in `being_identifications` |
| `godjesus` | 0/1: God or Jesus encountered | `god` or `jesus` in `being_identifications` |
| `relatives` | 0/1: deceased relatives or friends | `deceased_relatives` named/unnamed, or `deceased_relative_guide` |
| `guidance` | yes / no / not_mentioned | `guidance_received` |
| `teaching` | 0/1 | `teaching` in `guidance_types` |
| `telepathic` | 0/1 | `telepathic` in `communication_modes` |
| `lr` | extensive / brief / no / not_mentioned | `occurrence` (life review) |
| `tunnel` | 0/1 | `passage_type == "tunnel"` |
| `boundary` | schema `boundary_encounter` values | `boundary_encounter` |
| `agency` | schema `return_agency` values | `return_agency` |
| `mission` | 0/1: given a specific task or mission | `mission_commissioned` in yes_explicit/implied |
| `em` | 0/1: earthly mission given as a reason to return | `earthly_mission` in `return_reasons` |
| `morereal` | 0/1: environment more real than earthly life | `comparative_reality` more_real_explicit/implied |
| `religion` | schema `religious_background` values | `religious_background` |
| `jsource`, `jint` (set B) | schema `judgment_source`, `judgment_intensity` values | same fields |
| `note` | free text: the coder's one-line summary of the evidence | — |

## Coder conventions where the schema is silent

These are reported because several disagreements come from them, not from misreading:

- **Boundary type:** `verbal_limit` takes precedence when a being says "not your time" (or equivalent), even if a gate, wall or other barrier is also described.
- **Absence:** `not_mentioned` is used when the narrative is silent; `no` only when the narrative denies the feature.
- **Beings:** flagged anywhere in the account, not only "upon arrival". An unidentified being or voice counts as `unknown`.
- **Mission:** coded only for a specific task or purpose (raise a child, heal, write the account, help a named person). General life lessons such as "love more" are not a mission.
- **Questionnaire answers:** where NDERF accounts include answered questionnaire items, an explicit endorsement counts as evidence.
- **Religion:** "none" or "unaffiliated" → `atheist_agnostic`; LDS, Quaker and Nazarene → `christian`.
- **Judgment source:** `self` when the experiencer judges themselves and beings explicitly do not judge. `being_of_light` for a divine or luminous evaluator. `none` / `not_applicable` when a review is described without any evaluation.

## Limitations

The second coder is a language model from a different family, not a human. It knew the research framework. There is no third coder to adjudicate disagreements. Agreement statistics measure reproducibility; they do not say which coder is right.
