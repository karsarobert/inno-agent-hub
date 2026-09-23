# Verification - instructor's note

## Technical trials of the first edition

Verification date: 20 September 2026.
Environment: Linux x86-64, Python 3.12.14, TensorFlow CPU 2.20.0,
Keras 3.15.1, NumPy 2.3.5, Matplotlib 3.10.8, scikit-learn 1.8.0.
The trials ran in a separate verification copy. The distributed package contains
no finished learner results or filled-in final model-choice fields.

### Checks actually carried out for the first edition

- All six Python files are syntactically correct.
- The environment check succeeds in the full environment, the TensorFlow probe result is 6.
- In an environment without TensorFlow the checker does not install; it prints that
  the learner should ask the instructor for help, and stops with an error code.
- L03_01 full baseline run: loss curve, regression figure, settings save successful.
- L03_02 full 150-epoch baseline run: training, validation, four figures, model save successful.
- L03_03 full 150-epoch run with 16 neurons, then with the
  50-50 hidden layers required by the learner task: both successful,
  with 99 and 2853 parameters.
- L03_04 successfully reloaded and evaluated the model preselected by the
  smaller validation loss, without retraining.
- The saved validation tables contain 120 rows per run. The sum of the three softmax
  values is 1 within floating-point tolerance. The accuracy computed from the labels
  matches the printed validation metric.
- The visual check of the training/validation curves, decision figures and confusion
  matrices was carried out. The images are produced with English captions and readable axes.
- The test contains exactly ten questions with code snippets, each with A-D answers.
  The answer key and the computations are verified.

### Trial results of the first edition - not mandatory learner targets

| Model | Validation loss | Validation accuracy |
|---|---:|---:|
| 2 -> 3 | 0.682190 | 0.566667 |
| 2 -> 16 -> 3 | 0.042400 | 1.000000 |
| 2 -> 50 -> 50 -> 3 | 0.020447 | 0.991667 |

The designated rule was the smaller validation loss, therefore the two models with
50 layers were taken to the final test. Its test loss was 0.012168,
its test accuracy 1.000000 on these 120 synthetic samples. This does not prove
general perfection, and the same is not guaranteed with another version / machine.

The 16-neuron model's higher validation accuracy and the larger network's
smaller loss are a useful example that the two metrics can rank models differently.
The final test can be flawless; in that case the tutor does not ask for a
non-existent mistake, but has the diagonal of the matrix and the off-diagonal
zeros interpreted.

The regression baseline run's weight was 7.3598, its bias 10.1694, and the
validation MSE/2 became 23.7610 after 120 steps. This is the result of finite
training, not proof of reaching the loss minimum, and it is not directly
comparable with the cross-entropy.

### Limit of the first technical verification

The Python programs and the produced files were actually checked.
On the user's own Inno Agent interface no live tutoring conversation or
Run/View click trial took place. The preset loading and Python selection
there are local settings; the instructor should check them before the lesson.
The tutor's introduction, help request, per-question waiting and closing are
prescribed by agent.md.


## Verification of the improved 1.1 version

The user also tried the first version in a live Inno Agent conversation;
based on the full test conversation provided we modified the methodology.
We have not yet performed a live tutoring retest with the new 1.1 instructions.
The technical verification of the programs happened separately from this,
with actual runs.

- Both blocks of the schedule are 45 minutes; it contains four mandatory spiral runs.
- The agent, scenario, guides, start guide and experiment notes
  prescribe the same mandatory 0.01 -> 0.001 learning-rate experiment.
- The label-loss pairing, the two gradients, the fit arguments and the predict/argmax
  demonstration moved specifically to the pre-run phase.
- Stating the choice rule, waiting for the learner's decision and reason,
  and the test-figure interpretation are separate conditions for progressing.
- All six .py files pass the syntax check. The code of L03_01, L03_02,
  helpers and the environment check is byte-identical to the first edition.
  L03_03's run logic is unchanged, its session comment was extended.
- The 50-50 network with rate 0.01 and 0.001, 150 epochs and batch 32
  ran again in a separate verification copy. Both runs saved 2853 parameters,
  a 150-row curve table and a 120-row validation estimate.
- The softmax row sums are 1 within numerical tolerance. Saving the figures and
  models succeeded; the new rate-experiment loss image was visually checked.

| Verification run | Rate | Validation loss | Validation accuracy |
|---|---:|---:|---:|
| R3 - 50-50 | 0.01 | 0.0204438064 | 0.9916666746 |
| R4 - 50-50 | 0.001 | 0.0338100046 | 1.0000000000 |

These are instructor trial results, they do not replace the learner's own runs.
The smaller rate in this trial gave a more smoothly decreasing curve and a higher
final validation loss, while the accuracy became higher.
The difference between the two metrics can therefore be discussed from own results.
In another environment the values may differ; the direction is not guaranteed.

The new L03_04 actually ran by loading the model saved with rate 0.01:
test loss about 0.0122, test accuracy 1.0. The modified closing message asks for
figure interpretation first, and only then signals the code-comprehension question set.
No retraining took place during the evaluation.

The ten questions and the correct answers remained; every question has Python code
and exactly four A-D options. The distributed package still contains the
16-neuron, 0.01-rate starting model and empty final choice fields.
The trial run folders do not go into the learner ZIP.


## Verification of version 1.2

Version 1.2 touches the run identification and the check of the model choice
(helpers.py, L03_01-L03_04), the training schedule and the quiz are unchanged.

Automated check (`scripts/08_dl03_teszt.py` in the processing project):
30 checks, all successful. The test runs the control flow of the real `helpers.py`
and the real `L03_04`, with substitute (stub) numpy/matplotlib/tensorflow
modules, because the developer machine has no TensorFlow installation.

- Run label computation for all four mandatory structures and one non-mandatory one
  (X_32r-3s_lr0.01); the folder name starts with the label, longest name 27 characters.
- It also recognizes the label from a 1.1 long folder name (R4_50x2_lr0.001).
- The rule-based winner is the run with the lowest validation loss.
- Resolving the label: "R3", "r3", "3" and the full folder name all work; for an
  unknown label there is no match.
- Empty CHOICE: only the neutral table appears, the test does not start, and
  the winner is not marked.
- Wrong choice: the program stops, it does not test; with an override (OVERRIDE = "YES")
  it runs, and choice.json records the label, the validation loss, the
  rule-based winner and the fact of the override.
- Correct choice: the test runs, result.json is created.

Still to do: a real TensorFlow run and a live tutoring trial on the lab machine.
The stub-based check proves the control flow and the computations, not the numerical
results of training. Before live use it is worth running a full session in the
usual way, in a fresh workspace.


## Verification of the English version (EN 1.2)

The English package is a mirror of the Hungarian 1.2 version: the same programs,
the same behaviour, with English file names, identifiers and console messages.

- 20 files: helpers.py, environment_check.py, L03_01_gradient.py, L03_02_spiral_baseline.py,
  L03_03_spiral_network.py, L03_04_final_evaluation.py, agent.md, README.md, START-HERE.md,
  LESSON_INSTRUCTIONS.md, PROGRAM_GUIDES.md, EXPERIMENT_NOTES.md, CONCEPTS_AND_CODE.md,
  CODE_COMPREHENSION_TEST.md, TEACHER_ANSWER_KEY.md, TEACHER_PREPARATION.md, CHANGELOG.md,
  VERIFICATION.md, SOURCES.md, requirements.txt.
- The same automated check set was run on the English files with the mirror script
  scripts/09_dl03_en_teszt.py (derived mechanically from scripts/08_dl03_teszt.py):
  30 OK, 0 failures. The labels are R1_baseline_lr0.01, R2_16n_lr0.01, R3_50x2_lr0.01,
  R4_50x2_lr0.001 and G01_gradient; the choice lines are CHOICE, CHOICE_REASON, OVERRIDE.
- Every file is pure ASCII, except agent.md, which uses en dashes and arrows
  exactly like the published English tutor guide of the card.
- The Hungarian reference package (DL03_javitott) was not modified by the translation.
- Still to do here as well: a real TensorFlow run, and the instructor's check of the
  preset loading in the English locale.
