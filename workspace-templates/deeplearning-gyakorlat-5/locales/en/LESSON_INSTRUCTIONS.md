# Lesson plan — DL05, autoencoders · 2 × 45 minutes

Step IDs are internal state labels; do not read them aloud. Introduce every new
program using PROGRAM_WALKTHROUGHS.md. Wait after each task; never assign the whole
sequence in one message. No clear improvement can be a valid observation.
Every response to a successful run must include the View-refresh reminder, even
if only numbers are requested or the program already printed one. When opening
a file, explain its numbered sections before asking for a run.

## First block — 45 minutes

### E0 · Environment · 5 minutes

After the introduction, run `environment_check.py`. Evidence: the ENVIRONMENT OK
line. An empty GPU list is correct. For an error, ask for the final lines and
interpreter path; involve the instructor. Partial success is not full success.
Without TensorFlow, G01/G03/G04 may continue with instructor approval; mark G02 skipped.

### A1–A3 · ECG data · 10 minutes

**A1:** Introduce the program and key code, then run `G05_01_ecg_data.py` unchanged,
with `sample_index = 0`. Ask for the "One signal contains 140 sample points" line.
Remind the student to refresh View and open the current `ecg_signals.png`.

**A2:** Ask one observation question: "How do the shapes of the two signals differ?"
No medical interpretation is required; a peak, trough, waveform or location of a
difference is enough. The labels come from the dataset, not a visual diagnosis.

**A3:** Explain the selection first: indices 0, 1, 2 and 3 mean the first, second,
third and fourth example. Select the fourth normal and fourth anomalous signal
for closer examination; do not change their values. In the same file, set
`sample_index = 3`; save, Run, refresh View and open the new image. Ask for a short
comparison with the previous pair. Clarify that every row has 140 values, and
matching indices across the groups do not indicate a patient pair.

### B1–B3 · The first autoencoder · 20 minutes

**B1:** Full introduction before G02: 140 → 32 → 16 → 8 → 16 → 32 → 140,
input equals target, normal-only training, sigmoid amplitudes, compile and fit.
Run `G05_02_autoencoder.py` with `number_of_epochs = 10`, `bottleneck_size = 8`.
Wait for RUN COMPLETE. Ask for normal validation MAE and the normal practice
example's MAE at index 0: two related lines, not the entire log.

**B2:** Open the current `reconstruction.png` after the refresh reminder. Ask:
"Where does the reconstruction follow the original well, and where less well?"
Listen, then explain the two curves and shaded differences. Do not request exact
numbers that cannot be read from the image.

**B3:** Open `learning_curves.png`, again reminding the student to refresh View.
Ask: "How does the normal validation error change during training?" Validation
does not train, and its error need not decrease monotonically. Both curves in
this package use normal signals, unlike the mixed validation set in the original
notebook. There is no early stopping or restoration of best weights here.

### B4–B5 · Longer training · 10 minutes

**B4:** Change only `number_of_epochs = 30`; keep bottleneck_size at 8. Explain that
a new model starts from the same initial weights; this does not continue the
previous ten epochs. Save, Run, collect the same two MAE lines, refresh View and
open the current reconstruction image.

**B5:** Refresh View and open `comparison.png` in the current 30-epoch folder.
It shows the same signal and the student's two reconstructions on matching
scales, with pointwise absolute differences below. Identify the runs by the
names printed on the figure; do not compare from memory. If the image is missing,
the program reports that no matching own 10-epoch run in the new format was
found. Clarify this rather than claiming a completed comparison.
Ask one question about the visible change, then relate it to the numbers. Record
the two run identifiers and the observation. If initial-weight identifiers differ,
check whether other settings or the environment changed.

**Block transition:** "The network learned to reconstruct normal signals. Next,
we will examine what reconstruction error tells us about different signals."
After a break, resume here without another greeting or environment check.

## Second block — 45 minutes

### C1–C4 · Reconstruction error · 15 minutes

**C1:** Introduce `G05_03_reconstruction_error.py`. It reads the supplied 30-epoch
reference reconstructions, not the student's latest model. Everyone can examine
the same signals without training. Explain absolute differences, mean and axis=1
using a small worked example.

**C2a:** Run with `sample_index = 0`. Request the two selected MAE lines. Refresh
View and open `axis_1.png`. The two illustrative rows have means 0.2 and 0.4;
the overall mean is 0.3. Ask: "Why does axis=1 produce two results here?" WAIT,
then evaluate. If needed, point out that each row represents one signal. Connect
this to the real transformation (128, 140) → (128,).

**C2b:** With a fresh reminder, open `reconstructions.png`. Ask: "Do the error
values and curves show the same difference?" Do not reveal which error is larger first.

**C3:** Explain again that we select the fourth example in each group for closer
inspection: 0 is first, 3 is fourth. Change `sample_index = 3`; save, Run, refresh
View and open the new image. Ask for one observation. Different inputs have
different errors; do not generalise from one example.

**C4:** Open the current `error_distribution.png` with the refresh reminder.
Explain the axes, then ask whether the error ranges overlap. Changing the index
did not change this histogram: it still contains all 128+128 practice examples.

### D1–D5 · Thresholds and mistaken decisions · 15 minutes

**D1:** Introduce `G05_04_threshold.py`: `error >= threshold`, positive = anomalous.
First explain the plain-language TP/FN/FP/TN counts. Introduce precision and recall
formulas only after the counts are understood. There is no new training: the
same MAEs are recomputed from the fixed reconstructions.

**D2:** Baseline `threshold = 0.04`. Request the four counts, refresh View and
open `decisions.png`. Ask: "What does a false alarm mean here?" Let the student
explain, then refine the explanation.

**D3:** Change only `threshold = 0.025`. Run, request four counts and remind them
to refresh View. Ask: "What changed compared with the baseline?" TP may stay
unchanged because the baseline already detected all anomalies. Do not promise
an increase. `error_distribution.png` shows the same distribution with a moved
vertical line; remind them to refresh before opening it.

**D4:** Change only `threshold = 0.06`. Run, collect counts, refresh reminder.
Ask: "What is the cost of having fewer alerts here?" Wait, then give feedback
based on the actual FP and FN counts.

**D5a:** Introduce precision using that completed 0.06 run; no new run is needed.
Refresh View and open `precision_recall.png`. Explain only the upper bar first:
start with 127 alerts = 121 correct + 6 false. Precision = 121/127 ≈ 95.3%.
Ask: "Why do we divide by the 127 alerts here?" WAIT.

**D5b:** After the answer, explain the lower bar: start with 128 actual anomalies
= 121 detected + 7 missed. Recall = 121/128 ≈ 94.5%. Ask: "Which group contains
the seven missed anomalies, and why do they matter for recall?" WAIT. Always use
the student's actual output; the numbers above are the supplied reference results.

**D5c:** Summarise: the same 121 correct detections, but different starting groups.
Changing the threshold does not improve reconstruction. This repeated model
inspection is not an independent final evaluation. Begin the quiz only after
both understanding questions have been resolved.

### O1 · Optional bottleneck experiment

Only for genuinely fast progress, under the timing conditions in agent.md.
Use G02 with `number_of_epochs = 30`; change only `bottleneck_size = 16`.
Show just the affected layer again. Ask for validation MAE and the selected normal
example's MAE. More internal values do not guarantee better anomaly detection;
these numbers describe only normal reconstruction. **The G03/G04 reference does
not change**, so their existing counts cannot evaluate this modified model.
Evaluating its anomaly detection would require an additional experiment beyond this lesson.

### T1–T10 and Z · Closing · 15 minutes

Ask exactly the ten fixed questions, one at a time with explanatory feedback.
Give the score and summary at the end. Do not silently omit questions to fit time;
if interrupted, record the real progress and do not call the full lesson complete.
No homework and no advance CNN task set.
