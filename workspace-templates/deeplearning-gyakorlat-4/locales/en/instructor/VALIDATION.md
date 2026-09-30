# Validation and actual reference results

Date: **30 September 2026**. Package: **DL04 innoagent 1.1 EN**, translated
from Hungarian 1.1. Measurements below are fresh runs of the English programs,
not translated labels attached to earlier Hungarian screenshots.

## Environment

- Python 3.12.14; Linux x86_64.
- NumPy 2.3.5; Matplotlib 3.10.8.
- TensorFlow CPU 2.20.0; Keras 3.15.1.
- GPU use disabled; environment check reports an empty visible GPU list.
- Network programs use one intra-op, one inter-op and one data-loading thread.

## Checks performed

- Successful CPU computation and figure saving in environment_check.py.
- **26 configurations** executed successfully: 21 required initial/modified
  cases and five optional softmax/BN cases, at the full stated epoch counts.
- Runs started outside their script folders; outputs correctly go under each
  program workspace's view folder.
- Closed-form verification of all four learning-rate results.
- Matching full trajectories at zero momentum.
- Dropout evaluation passes all inputs through unchanged.
- Softmax outputs sum to one and remain unchanged under the common shift.
- Matching initial weight IDs for H2/H3 and all L2 runs.
- Matching H2 and unpenalized REG0 validation MAE.
- L2 penalty equals λ times the kernel sum of squares; total validation loss
  equals validation MAE plus penalty.
- Python syntax, translated internal imports and English output paths checked.
- Computational structure compared with the Hungarian source after renaming
  identifiers and excluding translated text.
- Exactly ten quiz questions and unchanged answer positions; code snippets
  checked against their Hungarian counterparts after identifier translation.
- English figure labels and layout visually checked on a contact sheet.

The English tutor has **not** been tested through a live Innoagent conversation.
Prompt review does not establish actual application behavior. The earlier
Hungarian trial identified missing pre-run explanations and later reported
verbatim repeated replies. The explanation update is retained; the repetition's
cause remains unverified and no application-level repair is claimed here.

## Runtime on this test machine

| Program group | Total Python-process time |
|---|---:|
| NumPy examples and optional demonstrations | 0.41–0.71 s |
| Neural networks, 120 or 400 epochs | 5.02–6.99 s |

Total process time includes imports, computation and figure saving. The program's
own “Training and measurement” field excludes imports and figure saving. These
measurements are not performance guarantees for all laptops; check locally.

## One weight learning

| Run | Rate | Steps | Final weight | Final loss |
|---|---:|---:|---:|---:|
| R1 | 0.1 | 8 | 2.328911 | 0.450360 |
| R2 | 0.8 | 8 | 2.932815 | 0.004514 |
| R3 | 1.1 | 8 | -14.199268 | 295.814814 |
| R4 | 0.1 | 25 | 2.984888 | 0.000228 |

## Network results

Every row uses the same 64/128 split. These are measurements of the final epoch's
weights, not earlier best values and not independent test-set results.

| Run | Units | Epochs | λ | Training MAE | Validation MAE | Penalty | Kernel sum of squares |
|---|---:|---:|---:|---:|---:|---:|---:|
| H1 | 8 | 120 | 0.0 | 0.218931 | 0.250036 | 0.000000 | 12.290650 |
| H2 | 64 | 120 | 0.0 | 0.218428 | 0.256901 | 0.000000 | 12.343403 |
| H3 | 64 | 400 | 0.0 | 0.206139 | 0.259742 | 0.000000 | 12.348137 |
| REG0 | 64 | 120 | 0.0 | 0.218428 | 0.256901 | 0.000000 | 12.343403 |
| REG1 | 64 | 120 | 0.001 | 0.219644 | 0.251515 | 0.011500 | 11.499766 |
| REG2 | 64 | 120 | 0.05 | 0.365231 | 0.380753 | 0.279174 | 5.583480 |

Interpret these as illustrative results for one seed and split. Small differences
are not statistical evidence. The tutor should interpret students' own output
rather than require these exact numbers.

## Dropout samples

| Run | Rate | Seed | Mode | Output |
|---|---:|---:|---|---|
| D1 | 0.5 | 42 | training | `[0.4, 0.0, 2.6, 1.6, 0.0, 0.8, 1.4, 2.0]` |
| D2 | 0.25 | 42 | training | `[0.2667, 0.6667, 1.7333, 1.0667, 0.0, 0.5333, 0.9333, 1.3333]` |
| D3 | 0.25 | 43 | training | `[0.2667, 0.0, 0.0, 1.0667, 1.4667, 0.0, 0.9333, 1.3333]` |
| D4 | 0.25 | 43 | evaluation | `[0.2, 0.5, 1.3, 0.8, 1.1, 0.4, 0.7, 1.0]` |

## Reference files

sample_outputs contains six figures copied from these actual checks.
verified_runs.json records all configurations and measured summaries, without
absolute workspace paths, model files or installed runtime packages.
