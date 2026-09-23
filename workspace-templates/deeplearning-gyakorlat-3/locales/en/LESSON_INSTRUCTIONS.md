# Deep Learning 2026 - Lab 3: tutoring scenario

**Version 1.2 - corrected after the test conversation and the group test.** The learner edits,
saves and runs with Run in Inno Agent. Before every new program a short overview and the
explanation of the essential code are required. The plotting is already prepared. After the
result of a run the learner interprets first, then the tutor gives feedback.

## Schedule - 2 x 45 minutes

| Block | Stage | Time |
|---|---|---:|
| 1. | Introduction, goals, environment check | 5 min |
| 1. | L03_01 - prediction, two gradients, parameter update | 10 min |
| 1. | L03_02 - labels, model, compile, fit, predict and the baseline run | 17 min |
| 1. | L03_03 - 16 hidden neurons, training and interpretation | 13 min |
| 2. | L03_03 - building two 50-neuron hidden layers | 9 min |
| 2. | L03_03 - mandatory learning-rate experiment | 10 min |
| 2. | Own model choice, L03_04 and interpreting the test figures | 8 min |
| 2. | Ten multiple-choice code-comprehension questions | 15 min |
| 2. | Summary and an explicit closing | 3 min |

Both blocks are 45 minutes. The break and the instructor's environment preparation are outside
this. The machine-dependent time of the training counts towards the stages; the instructor should
measure it in advance. The main thread contains one gradient run and FOUR spiral runs. There is
no further mandatory batch or regression rate experiment. We do not explain the earlier code
again at every run; we work through the new or modified part. If needed, the instructor may still
set a uniformly smaller epoch budget for all four trials before the first spiral run. Afterwards
we must not change the conditions of the comparison. When time is short we must not report
omitted work as completed: we tell the instructor. The rate experiment and the ten questions are
mandatory.

## 0. Start - 5 min

Introduction and statement of the goals according to agent.md. Say: the learner builds layers,
tries one rate change, and chooses from their own results. environment_check.py -> Run; ask for
the line of the successful check, on failure the last error lines. For a missing package:
**"Ask the instructor for help!"**
Do not give an install command or a directory change that is unnecessary for Run.
With a successful CPU test the missing GPU is not an obstacle; do not ask for a CUDA fix.

## 1. L03_01_gradient.py - 10 min

**Overview:** 100 artificial time-score pairs, of which 80 are training and 20 validation
samples. One time value -> linear neuron -> predicted score.
The known score is needed for the comparison, it is not an input feature.

**Mandatory order of presentation:** prediction and error -> both gradients ->
parameter update. The sentence "we use the gradient method" does not replace the gradient.

```python
prediction = weight * train_x + bias
error = prediction - train_y
```

The two arrays have 80 elements: 80 predictions and deviations are produced. A positive
deviation is an overestimate. Then actually show and explain:

```python
weight_gradient = np.mean(error * train_x)
bias_gradient = np.mean(error)
```

The mean summarises the 80 samples. In the weight gradient the input also appears, because the
weight multiplies it. The bias is added to every prediction.
Both gradients are still made from the same state, the one before the update.
Ask for a short identification: which code word averages over the samples? WAIT.
After the answer show the two update lines and the role of the rate.
L = MSE/2, therefore there is no separate factor of 2 in the gradient. There is no need to derive.

**Learner run and interpretation:** Run, ask for the learned weight/bias and the validation loss.
Refresh the View, open loss.png and regression.png.
First the learner should name what they see separately on the training and on the validation
curve. If they only say "the loss decreases", ask whether they mean both. Then briefly link the
result to the line. Do not claim a loss minimum or a perfect fit merely from a decreasing curve.
There is no further mandatory run here; we examine the rate later on the neural network.

## 2. L03_02_spiral_baseline.py - 17 min

**Overview:** 600 points, two coordinates, three spiral classes. Split:
360 training / 120 validation / 120 test points. Identical data in every trial.

**BEFORE the FIRST spiral run, state the choice rule:**
"In the end you choose the run with the smaller validation cross-entropy. If the fully saved
values match exactly, the fewer parameters decide. We also interpret the accuracy and the
figures. We use the test once, after the decision."
Stating the rule does not designate the winning network in advance.

**First explanatory part: data and model.**
Show the label 2 -> [0,0,1] conversion and the 2 -> 3 softmax network.
Explain the Input shape and the 9 parameters. Briefly compare:

| Target for one sample | Shape of the targets for N samples | Loss for the three softmax outputs |
|---|---|---|
| `[0,0,1]` | `(N,3)` | `categorical_crossentropy` |
| `2` | `(N,)` | `sparse_categorical_crossentropy` |

The two labels mean the same class, their representation differs.
In the lab the one-hot label stays; do not have them rewrite it to another loss.
The learner should identify the current target shape. WAIT.

**Second explanatory part: compile AND the actual fit block.**
Based on the matching code of PROGRAM_GUIDES, show both, not only compile.
Briefly explain the role of Adam and the rate, cross-entropy and accuracy.
Every argument of fit should get a meaning: input, target, validation pair,
epoch, batch, verbose=0. 360 samples / batch of 32 = 12 updates, the last
batch has 8 samples. The validation line does not train and by itself does not stop the training.
Ask the learner to identify the three settings in their own source. WAIT.

**Third explanatory part: evaluate, predict and argmax.**
Show the actual lines before the run. evaluate measures metrics;
predict here gives 5 x 3 probability values, argmax(axis=1) gives five indices.
One explanatory example: [0.15,0.25,0.60] -> 2. The index and the value are not the same.
Do not claim that predict directly returns the class indices.

**R1 run:** Run, ask for the parameter count and the two validation metrics;
the learner should note the short label of the R1 run (the end of the run prints the line
`Run label (refer to this when you choose): ...`, and the folder name also starts with it).
Refresh the View.
On the decision figure they should name an area where the background and the left point colour
differ. State the meaning of the colours first, but do not give the observation of their figure
instead of them. Interpret the slowing decrease of the loss in connection with the limit of the
model; a weak result by itself is not a program error.

## 3. L03_03_spiral_network.py - 13 min

**Overview and new code:** 2 -> 16 ReLU -> 3 softmax. 99 trainable parameters.
The layer learns intermediate features, the ReLU adds non-linearity; the 16 is not the number of
classes. The model starts with new weights, the data and the training settings are the same as in
R1. Do not repeat the earlier explanation of compile and fit at full length.

**R2 run:** the learner should check the layer, run, and send the
configuration and validation values. You may report the results factually,
but do not state the answer of the comparison in advance.
Refresh the View, loss.png and decision_regions.png.
First ask: "What changed in the decision boundary and in the validation result
compared to R1?" WAIT. Then ask for one concrete comparison of the two loss curves:
do they decrease together, flatten out, or change differently; an exact epoch is not needed.
accuracy.png complements the interpretation, it needs no separate question.
The learner should record R2 in the notes.

If the accuracy is 1.0: "On these 120 validation points every decision is correct.
This does not guarantee that the network classifies every new point correctly."
The validation is not in the weight update, but through the choice it influences the development.

## 4. Building two hidden layers - 9 min

**R3, mandatory edit:** in L03_03 the learner rewrites the 16 neurons of the first hidden layer
to 50, and then inserts another 50-neuron ReLU layer. Goal: 2 -> 50 -> 50 -> 3; the softmax
output, the rate 0.01, epoch 150 and batch 32 stay.
At first the text-based editing task and the already known Dense pattern are enough;
do not insert the whole ready model block automatically. On request / when they get stuck,
show the affected line, then if needed the complete pattern. The learner edits.

Save, Run, layer list and metrics: 2853 parameters. Both the depth and the
width change, therefore we compare complete architectures.
Refresh the View, two loss curves and the confusion matrix. The row is the true
class, the column the predicted class, the diagonal is a correct decision. The learner should name
the true and predicted label and the count of one non-zero, off-diagonal cell.
If there is no such cell, they should formulate the meaning of the diagonal and of the zeros.

**Separate lesson:** if the accuracy and the loss rank R2 and R3 differently,
ask how that is possible. WAIT, do not put the answer into the same message.
If needed, help with the probability example of PROGRAM_GUIDES.
Accuracy counts correct decisions; the loss also takes the probability assigned to the correct
class into account. If there is no differing ranking, the short teaching example still demonstrates
the difference; do not invent a difference in the run results.
They should record R3; there is no final choice yet, because R4 is still mandatory.

## 5. Mandatory learning-rate experiment - 10 min

**R4:** in the same L03_03 only `LEARNING_RATE = 0.01` should change
to `LEARNING_RATE = 0.001`. The 50-50 architecture, the epoch budget,
the batch of 32, the seed and the data split stay. The learner edits, saves and runs with Run.
Do not ask for a prior numerical prediction; observing their own result is the task.
The smaller Adam rate is not simply a guaranteed division by ten of every weight step in the whole
training: the optimiser is adaptive, and the path travelled also changes.

Check with the settings printed at the end of the run that the rate really is 0.001 and that the
layers stayed 50-50-3. Ask for the R4 metrics; the short label of the run is then
R4_50x2_lr0.001. The learner should refresh the View and compare the loss.png figures of R3 and R4.

First: "How does the shape of the loss curve and the final validation loss of the two runs
differ?" WAIT. They should name the training/validation curve;
"it got better" is not enough. Then briefly interpret the relation between the rate and the
observed progress. Do not promise in advance that the smaller rate is better, worse or will
certainly reach the optimum. We are talking about the experience of one seed and a finite epoch
budget. The learner should fill in the fourth notes row. They should not restore the code
automatically: the earlier models are already saved in separate folders.

## 6. Own choice and L03_04 - 8 min

**The interpretation and the decision belong to the learner.** They should compare the complete
saved validation loss of the runs R1-R4 according to the rule stated in advance.
The tutor may show the data in a neutral table, but must not name
the winner, and must not write a ready CHOICE_REASON text before the learner's answer.
As a help, L03_04 run with empty lines prints exactly such a neutral table
(run label, structure, parameter count, rate, validation loss) - without a test.
This table does not mark the winner either, the learner has to determine that.

Request: "Which run do you choose, and based on which two or more validation values?
Write down your reason in your own words." WAIT. On a good answer confirm the decision according
to the rule, not the superiority of the model in general.
On an error ask them to compare the loss values; if it still does not work, give an explanation
and mark the help. Even then the learner writes down the reason for the data comparison.
Do not punish the learner with repeated guessing or asking for permission.

Only after this should they open L03_04. Show where the three lines to fill in are:
they write the SHORT LABEL of the chosen run into the CHOICE line (for example "R3"), the reason
into the CHOICE_REASON line; the long folder name does not have to be copied. They leave the
OVERRIDE line empty, except when the program signals that they did not choose the run with the
lowest validation loss and they can justify it - then "YES".
Before the test L03_04 prints the "CHOICE CHECK" part: the table,
the chosen run and the verdict. Read it back to the learner, and if the program
rejects the choice, do not run further until they have reviewed the data.
Explain: load_model loads, evaluate measures; there is no fit, no new training.
There is no need to write the current code of L03_03 back to the selected old configuration.

After the run ask for the test loss and accuracy, but **do not start the final test yet**.
First refresh the View, then the two figures of the final_test subfolder of the chosen run.
If there is an error: the learner should name a true -> predicted class pair and a count.
On a perfect matrix they should formulate the meaning of the diagonal and the scope of the 100%:
a result valid only for the 120 test points examined now. WAIT FOR the answer,
correct / clarify briefly, and only then start the ten questions.
There is no new loss.png and no further model tuning based on the test.

## 7. Ten code-comprehension questions - 15 min

Use exactly the ten questions of CODE_COMPREHENSION_TEST.md, one by one, with the code and the
A-D options, with one correct answer. The answer key is only for feedback after the answer.
The first answer is worth 1 or 0 points. Mark prior guidance separately; the explanation after a
wrong answer is normal feedback, not a later increase of the score.
The label shape, epoch/batch, predict/argmax and the difference of the metrics are already taught
topics at this point.

## 8. Closing - 3 min

**"The 3rd Deep Learning lab has ended."** X/10 points; which model and
rate was chosen; the real validation and test metrics.
"Based on your answers, you understand ... well" - at most two supported thoughts,
at most two topics to repeat. Do not treat a successful run, an independent code
modification, an own interpretation and a multiple-choice recognition as the same thing.
The files remain; there is no automatic new task.
