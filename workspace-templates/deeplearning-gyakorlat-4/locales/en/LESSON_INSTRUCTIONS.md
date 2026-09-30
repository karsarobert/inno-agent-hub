# Lab 4 – step-by-step tutor plan

For every new program: detailed introduction and key-code explanation → initial
run → student observation and feedback → one change → rerun → observation and feedback.
PROGRAM_WALKTHROUGHS.md provides ready-to-deliver introductions. The short
introductions below are planning reminders, not substitutes for explaining the
code before the first Run request. Give the student only the next step. Run IDs
are internal progress labels and need not be memorized or repeated by the student.

## Timing

| Block | Content | Minutes |
|---|---|---:|
| 1 | Introduction and environment check | 5 |
| 1 | G04_01 – learning rate | 12 |
| 1 | G04_02 – momentum | 8 |
| 1 | G04_03 – activations | 10 |
| 1 | G04_04 – data, network and first training run | 10 |
| 2 | G04_04 – hidden units and epochs | 10 |
| 2 | G04_05 – L2 experiments | 10 |
| 2 | G04_06 – dropout | 10 |
| 2 | Ten quiz questions, feedback and ending | 15 |

Each block is 45 minutes. Instructor installation happens beforehand; the break
is outside this schedule. Execution time is included. If time is short, shorten
already understood repetition rather than giving several new tasks at once.
Do not report omitted sections as completed.

## 0. Start

Introduce yourself as described in agent.md, then ask for `environment_check.py`
→ Run. Wait for “ENVIRONMENT OK”. `Visible GPUs: []` is the intended state.
Refresh View before opening a figure. Missing packages require instructor help,
not student installation. Passing this check does not mean all later tasks are complete.

## 1. G04_01_learning_rate.py – a single weight

**Introduction:** change one weight towards w=3, where `(w-3)**2` is zero.
The program prints the weight and loss after updates and plots both. No dataset
or complete neural network is involved.

**Before R1:** show and explain the gradient, update and loss lines. The gradient
formula is supplied; no derivation is required. Work through the first update:
−1 − 0.1·(−8) = −0.2; its loss is 10.24. This is part of the introduction.

**R1 – initial run:** `learning_rate = 0.1`, `number_of_steps = 8`, initial weight −1.
Request the last row. Ask whether the weight moved closer to 3. Evaluate the
student's own result without repeating the entire introduction.

**R2 – larger steps:** change only `learning_rate` to `0.8`. Save and Run.
Ask the student to refresh View and open `learning_steps.png` from this run.
Ask: “Does the weight always approach 3 from the same side?” WAIT. Then explain
overshooting and shrinking oscillations. Loss can still decrease.

**R3 – excessively large steps:** change only the rate to `1.1`. Request the final
loss. Ask: “How does it compare with the original starting loss?” Do not reveal
the answer first. Relate growing error to the oversized update, not an incorrect gradient sign.

**R4 – more small steps:** restore the rate to `0.1`, then change the step count
to `25`. Present these as restoring the baseline and then changing the new
experimental factor. Compare **R1 with R4**, not R3 with R4. Request the final
weight and a short conclusion.

**Ready to move on:** the student distinguishes step size from step count and
understands that a larger rate is not automatically better.

## 2. G04_02_momentum.py – remembering previous updates

**Introduction:** two parameters, one flatter direction and one steeper direction.
Both panels show the same loss surface, starting point, learning rate and step
count. One update rule retains some previous velocity.

**Before M1:** explain `position`, `gradient`, `velocity` and how the setting
`momentum` becomes the function's `beta` argument. Velocity has two coordinates;
array arithmetic acts element by element. Explain contour lines.

**M1 – initial run:** momentum `0.9`, rate `0.1`, 40 steps. Run and open
`trajectories.png` after refreshing View. Ask for one concrete difference between
the paths; “they are different” alone is insufficient.

**M2 – without memory:** change only `momentum` to `0.0`. Run and request both
endpoints. Ask: “How do the two results differ now?” After the answer, explain
that beta=0 removes previous velocity, making the rules identical.

Do not infer that momentum always wins. Here x and y are parameter coordinates,
not the input–target pairs of the later regression example.

## 3. G04_03_activations.py – output and backward signal

**Introduction:** transform a fixed array using three activation functions.
No training occurs. The table separates output, local derivative and the
returned gradient obtained from an incoming gradient of 2.

**Before A1:** explain activation, local derivative and incoming / returned
gradient. Show the sigmoid calculation and the three result-array lines.
A worked point is z=0: output 0.5, derivative 0.25, returned gradient 0.5.

**A1 – sigmoid:** run with inputs −6, −1, 0, 1, 6. Ask the student to compare the
local derivatives at 0 and 6, then connect the observation to saturation.

**A2 – saturating input:** change only the two outer values of the input array:
`np.array([-8.0, -1.0, 0.0, 1.0, 8.0])`. The experimental factor is the input
array. Run and compare sigmoid derivatives at 6 and 8. Afterwards restore the
original inputs before comparing activation functions.

**A3 – ReLU:** on the original inputs, change only `activation = "relu"`.
Explain `np.maximum(0, z)` and the derivative branch before execution. After Run,
request the output and derivative at −1. A zero here is temporary inactivity,
not proof of a permanently dead neuron.

**A4 – Leaky ReLU:** change only `activation = "leaky_relu"`; keep slope 0.1.
Explain the two `np.where` branches. After Run, compare the −1 row with A3.

**A5 – slope:** change only `negative_slope` to `0.2`. Run. Ask how the output and
derivative changed at the same −1 input. After feedback, emphasize that the
slope is manually set; this is Leaky ReLU, not a learned PReLU parameter.
Do not assign manual differentiation at the kink at 0.

## 4. G04_04_small_network.py – real, small CPU training

**Introduction:** 192 synthetic points: 64 training and 128 validation. Each
sample has one x input and a noisy y target. The known noise-free curve in the
figure is a reference, not the training target supplied to the model.
One input → hidden ReLU layer → one linear prediction. Only noisy training
samples update weights; validation is for measurement.

**Before H1:** deliver the full network introduction: data, model construction,
compile versus fit, MAE, epoch and batch. Show the model and fit code. Prepared
datasets use batches of 16, giving four updates per 64-sample epoch. Validation
only measures; 120 epochs does not mean 120 samples. Explain this before training.

**H1 – initial run:** 8 hidden units, 120 epochs. Run; request final training and
validation MAE, then open `prediction.png`. Ask the student to identify training
points, validation points and the prediction line from the legend. The first
block can end here for a break.

**H2 – more hidden units:** change only `HIDDEN_UNITS = 64`; keep 120 epochs.
Run and request both final MAEs and parameter count. No mental parameter-count
calculation is required. Ask whether this larger model improved validation error
in their run. Compare with H1. Little difference is a valid observation.

**H3 – longer training:** keep 64 units and change only `EPOCHS = 400`.
Compare with **H2**. In `learning_curves.png`, ask the student to identify both
curves and find a region where the errors develop differently. If none is
clear, say so. One fluctuation does not justify a general conclusion.

The teaching goal is to judge results rather than assume that more units or
epochs is better. Lower training error and better generalization are different.
The code evaluates the last state; no early stopping is enabled.

## 5. G04_05_l2_regularization.py – only the penalty changes

**Introduction:** a new independent file, fixed at 64 units and 120 epochs.
This matches H2, not the 400-epoch H3. Add λ times the sum of squared kernel
weights to the prediction loss. Both Dense kernels receive L2; biases do not.

**Before REG0:** show both `kernel_regularizer` arguments and the separate MAE
metric. Explain prediction error versus total loss. A worked numerical example:
weights [2,−1], λ=0.01 → penalty 0.05; MAE 0.12 → total loss 0.17.
These are illustrative numbers, not measured results.

**REG0 – initial run:** `L2_STRENGTH = 0.0`. Check that the file says 120 epochs.
Run; request both MAEs and total validation loss. Matching initial weight IDs
between H2 and REG0 show the same starting weights. Call this the “unpenalized
baseline” when speaking to the student.

**REG1 – mild penalty:** change only `L2_STRENGTH = 0.001`. Run and request final
validation MAE and the kernel sum of squares. Ask how prediction error changed
from the baseline. Do not promise improvement. Then open `loss_and_mae.png`
and distinguish the two validation curves; their difference is the penalty.

**REG2 – strong penalty:** change only `L2_STRENGTH = 0.05`. Request the same
measurements and let the student interpret the change before explaining it.
Smaller weights and better predictions are different goals; excessive restriction
can hurt. Compare predictive quality using **validation MAE**, not total losses
with different λ. There is no model selection using a test set in this lab.

## 6. G04_06_dropout.py – mode and random mask

**Introduction:** eight fixed activations; a vector operation, not further
network training. A binary mask keeps or zeros each element, and retained
values receive a scaling factor determined by the dropout rate. The seed is fixed.

**Before D1:** show both mode branches. Explain the mask, `>= dropout_rate` and
the division. Rate 0.5 is an element's drop probability, not a promise of exactly
four zeros. A retained 0.8 becomes 1.6; a dropped value becomes zero.

**D1 – initial run:** rate 0.5, training mode True, seed 42. Run and request mask
and output. Ask the student to choose a retained element and explain its change.

**D2 – lower rate:** change only `dropout_rate = 0.25`. Run and open `dropout.png`.
The seed stays 42, so the same random numbers meet a different threshold.
Ask: “What is the multiplier for retained values now?” WAIT; if needed, recall 1/(1−p).

**D3 – new mask:** change only `random_seed = 43`. Run and compare masks.
The same probability can produce different dropped positions. A fixed seed makes
this run reproducible; it does not remove the underlying random model.

**D4 – evaluation:** change only `training_mode = False`. Run; request input and
output. Ask which values survived and whether they received an extra multiplier.
Then explain that inverted dropout passes values through unchanged during evaluation.

## 7. Quiz and ending

After discussing the required exercises, use exactly the ten questions in
CODE_UNDERSTANDING_TEST.md. One question, one answer, scoring and a short
explanation, then the next question. Questions and answer key are fixed.
Exact MAE values from the student's runs are not quiz questions. No TensorFlow
execution is needed for the quiz. After question 10, use the clear ending in
agent.md. No homework or additional required task; do not automatically start supplements.

## Optional supplements – only on request

Give the corresponding code introduction before its first run.

- **Softmax:** initial run → `common_shift = 1000.0` → compare results. Subtracting
  the maximum keeps the probabilities unchanged and prevents exponential
  overflow here. A separate experiment can change one logit. Allow 5 minutes.
- **Batch normalization:** initial run → gamma=2, then separately beta=1. Next,
  with training mode False, use stored statistics on the same inputs. A later
  input change does not update those statistics. Gamma/beta are learned in real
  layers but manually set here; stored statistics are illustrative. Allow 5–8 minutes.
