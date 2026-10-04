# Deep Learning 2026 — practice 5

**Version 1.1 · Autoencoders and ECG anomaly detection · English Innoagent package · 2 × 45 minutes · CPU**

Four short, working Python examples: observe signals, train a real autoencoder,
measure reconstruction error, and explore decision thresholds. Students change
one setting at a time. Before each new program, the agent explains its purpose
and important code sections. Ten questions with explanatory feedback close the
lesson. CNNs belong to the next practice and are not included here.

## Getting started

1. Extract the ZIP into a new workspace. `agent.md` and the four `G05_...py` files
   must be directly in the opened folder, with the `data` subfolder beside them.
2. In Innoagent, select the workspace and tutor instructions in your usual way.
   This package does not install or reconfigure the application.
3. Start a new conversation: **"Let's start Deep Learning practice 5!"**
4. Students use Run. The programs do not install packages or download anything.

## Programs

| File | Purpose | Change | Main figures |
|---|---|---|---|
| `environment_check.py` | Local data, CPU and figure saving | None | `check.png` |
| `G05_01_ecg_data.py` | Normal and anomalous waveforms | `sample_index`: 0 → 3 | `ecg_signals.png` |
| `G05_02_autoencoder.py` | Learning and reconstruction | `number_of_epochs`: 10 → 30 | `reconstruction.png`, `learning_curves.png`, `comparison.png` |
| `G05_03_reconstruction_error.py` | Per-signal MAE and error distributions | `sample_index`: 0 → 3 | `axis_1.png`, `reconstructions.png`, `error_distribution.png` |
| `G05_04_threshold.py` | Alerts and mistaken decisions | `threshold`: 0.04 → 0.025 → 0.06 | `decisions.png`, `error_distribution.png`, `precision_recall.png` |

Only for fast progress: G02 with 30 epochs and bottleneck_size 8 → 16.
The core lesson requires no custom classes, new functions, manual gradients or
programming from an empty file.

## Local data and reference

- 512 normal training signals and 128 separate normal validation signals.
- Another 128 normal and 128 anomalous practice signals, each with 140 points.
- The scaling minimum and maximum come only from training data and are applied
  to all subsets. Labels are not among the 140 input values.
- G02 really trains, creating a new model on every Run with a fixed random seed.
- G03 and G04 **always use the supplied reference reconstructions**, not the
  latest results from the student's G02. The reference comes from a real run
  with 30 epochs and an eight-value bottleneck.
- The repeatedly inspected practice set is not an untouched final test set.
  The closing quiz is a conceptual assessment, not a model evaluation dataset.

Source labels mean 1=normal, 0=anomalous. For threshold decisions, however,
**positive = anomalous**; all TP/FP/FN/TN counts and precision/recall use this meaning.

## Results

Each run creates its own short numbered folder under `view` and prints its path:
for example `01_data_01`, `02_model_01`, `02_model_02`, `03_error_01`, `04_threshold_01`.
Previous results remain available. `result.json` stores settings, numbers and
the exact save time. **Refresh the View folder / file list after every run.**
G02 also saves its own reconstructions in NPZ and learning curves in CSV;
these never overwrite the supplied reference.

## Illustrations

`axis_1.png` uses two short artificial error rows to compare per-signal means
with one overall mean. These values are separate from real ECG results.
`precision_recall.png` uses two count bars: precision starts with alerts, while
recall starts with actual anomalies.

At 30 epochs, G02 selects the latest completed own 10-epoch run in the current
format with matching data, architecture, training configuration and initial weights.
If found, `comparison.png` shows two reconstructions on matching scales and
absolute differences underneath. Both run names appear on the figure. If none
is found, the program explains why; it does not secretly retrain or substitute
reference images. Existing Hungarian or old long-name run folders are not used
for this comparison. Extract the English package into a fresh workspace and
follow the 10 → 30 sequence.

## Guides

- `START-HERE.md`: student start and troubleshooting.
- `agent.md`: tutor behaviour, progress and avoiding repetition.
- `LESSON_INSTRUCTIONS.md`: step-by-step plan and waiting points.
- `PROGRAM_WALKTHROUGHS.md`: detailed explanations before each first run.
- `CODE_UNDERSTANDING_QUIZ.md`: ten prepared questions.
- `concepts_and_code.md`: student revision sheet.
- `instructor/`: preparation, keys, measured runs, verification and sample figures.
- `SOURCES.md`, `data/data_metadata.json`, `data/reference_metadata.json`: provenance and preprocessing.
- `CHANGELOG.md`: changes carried over from the latest Hungarian package.

## Requirements and scope

With a prepared Python environment, the programs run without a GPU or internet.
G01/G03/G04 need NumPy and Matplotlib. G02 and the complete environment check
also require TensorFlow/Keras. Installation is instructor preparation, not a
student activity during the lesson. Innoagent's own network requirements are separate.

Training results may differ slightly across environments; do not require identical
last digits. Counts from the fixed reference can be checked. Tutor instructions
alone cannot repair duplicate message delivery or rendering in the application;
the instructor checklist includes a separate live test. The answer key is
readable: this package supports guided learning, not a secure examination.
There is no homework. These examples are not clinical diagnostic tools.

This English edition translates filenames, code identifiers, comments, output,
figure labels, data keys and all guides. Numeric data, reference reconstructions,
model structure, exercise settings and quiz answers are unchanged.
