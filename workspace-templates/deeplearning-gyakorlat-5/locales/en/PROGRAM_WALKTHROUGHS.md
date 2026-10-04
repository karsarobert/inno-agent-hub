# Explanations before the first run

These are teacher walkthroughs for the agent. Explain them conversationally;
do not assign this document as student reading. Each introduction ends with one
baseline run. For later modifications, explain only the new setting instead of
repeating the entire introduction.

## File maps: explain these before the key lines whenever a file is opened

Help the student locate the parts of the program using its numbered comments.

| File | Main sections in order |
|---|---|
| G05_01 | 1. Select example → 2. Load data → 3. Select rows → 4. Figure and output. |
| G05_02 | 1. Epoch count → 2. Normal data → 3. Input-target pairs → 4. Full model → 5. Training → 6. Evaluation and figures. |
| G05_03 | 1. Select example → 2. Reference → 3. Two-row illustration → 4. MAE in three steps → 5. Figures → 6. Summary. |
| G05_04 | 1. Threshold → 2. Recompute the same MAEs → 3. Alerts → 4. Four counts → 5. Precision → 6. Recall → 7. Output → 8. Figures. |

Do not read the entire source aloud. For example: "At the top we choose a sample.
Then we load the two groups, select a row from each, and finally save the two
curves. Let's look at the lines that select those rows."
Every response to a successful run must include a View-refresh reminder before
requesting an image. This is independent of the program's printed reminder.

## 1. ECG data: no network yet

First, we will examine the data that the network will process. One ECG example
here is a preprocessed signal segment containing 140 numbers. Their order
matters: they are successive points along a curve, not 140 diseases or classes.
The horizontal axis shows the point index, and the vertical axis the scaled signal value.

The package contains examples labelled normal and anomalous. This program neither
learns nor decides which signal is anomalous. It uses the existing labels to
show one example from each group. You do not need to make a medical diagnosis;
we will observe the shapes of the curves.

```python
sample_index = 0
normal_signal = normal_signals[sample_index]
anomalous_signal = anomalous_signals[sample_index]
```

`sample_index` selects the displayed row. Python counts from zero, so 0 selects
the first example. The groups are separate: the same index does not mean two
measurements from the same person. `normal_signal` is one row of 140 values,
whereas `normal_signals` contains the entire normal practice group.

The run prints the array shape for one signal and saves two curves in
`ecg_signals.png`. First, run `G05_01_ecg_data.py` unchanged. Send the line starting
with "One signal contains 140 sample points". We will examine the image next.

**Before changing the index, explain:** "Now we will inspect another waveform.
Set sample_index to 3. In Python, 0 is first, 1 second, 2 third and 3 fourth.
We are selecting the fourth normal and fourth anomalous signal for closer
inspection. We are not changing their values, only choosing different examples."
The program accepts integer indices from 0 to 127. Then save, Run, refresh View
and open the new image.

## 2. Autoencoder: what are we training?

Now we will train a network to reconstruct the ECG signal it receives. It sees
512 normal signals during training. It does not learn normal/anomalous labels:
the desired output is the same set of 140 signal values as the input.

The first part gradually reduces the number of internal values: 140 → 32 → 16 → 8.
This is the encoder. The eight values form the bottleneck. The decoder uses them
to reconstruct the signal through 16 → 32 → 140 values. These eight numbers are
a learned internal representation, not eight preselected ECG sample points.
Reconstruction is approximate.

Show the complete network with encoder/decoder comments:

```python
model = keras.Sequential([
    keras.Input(shape=(140,)),
    # Encoder
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    # Bottleneck
    layers.Dense(bottleneck_size, activation='relu', kernel_initializer='he_normal'),
    # Decoder
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(140, activation='sigmoid'),
])
```

Do not present two nonadjacent layers as if they were the full model. Each Dense
neuron computes from a weighted sum of the previous layer's values. ReLU adds
nonlinearity. The final sigmoid outputs reconstructed amplitudes between 0 and 1,
not class probabilities. `he_normal` sets the initial weights; tuning it is not
the task in this lesson.

```python
training_batches = make_batches(training_signals, training_signals, shuffle=True)
model.compile(optimizer='adam', loss='mae', jit_compile=False)
history = model.fit(training_batches, validation_data=validation_batches,
                    epochs=number_of_epochs, shuffle=False, verbose=0,
                    callbacks=[BriefProgress()])
```

The first line uses the same signal as input and target. This expresses the same
idea as `fit(data, data)` in the notebook; the helper creates batches of 32.
Adam updates the weights, while MAE measures reconstruction error. `compile`
configures training; `fit` carries it out. The dataset handles shuffling, so
fit does not request an additional shuffle. Each epoch visits all 512 training
signals in 16 updates of 32 signals each.

The separate 128 normal validation signals do not update weights. They help us
track reconstruction on normal signals not used for training. The reconstruction
figure uses another separate signal from the practice set.

Run the baseline `G05_02_autoencoder.py`: 10 epochs and a bottleneck of 8.
Wait for RUN COMPLETE and send the final normal validation MAE and the normal
practice example's MAE at index 0.

**Before the 30-epoch run:** More epochs mean more passes through the same data.
Each Run starts a new model from the fixed initial state. Here 30 means 30 total,
not 30 additional epochs after the previous ten. More training does not guarantee
improvement. The curve contains training epoch averages; the summary remeasures
training error using the final weights, so these values may differ slightly.

## 3. Reconstruction error: one number for each signal

We have seen that the reconstructed curve can differ from the original. Now we
will describe that difference numerically and compare normal and anomalous signals.
There is no training in this program. It reads supplied reconstructions from a
real, previously completed 30-epoch training run. This fixed reference is not
your latest model and remains usable even if you could not complete training.

```python
differences = normal_signals - normal_reconstructed
absolute_differences = np.abs(differences)
normal_errors = np.mean(absolute_differences, axis=1)
```

Subtraction compares the original and reconstructed values point by point.
`np.abs` takes absolute values so that positive and negative differences cannot
cancel. `np.mean(..., axis=1)` averages the differences across the 140 points,
separately for each signal. Thus 128 signals produce 128 error values. Averaging
across all axes instead would produce one overall number.

The program also includes this separate two-row illustration:

```python
illustrative_differences = np.array([
    [0.1, 0.1, 0.3, 0.3],
    [0.4, 0.4, 0.4, 0.4],
])
individual_means = np.mean(illustrative_differences, axis=1)
overall_mean = np.mean(illustrative_differences)
```

The first row averages to 0.2, the second to 0.4. With axis=1, averaging stays
within each row: two signals, two results, [0.2, 0.4]. Without axis, all eight
values contribute to one overall mean of 0.3. axis=1 does not select the first
signal. `axis_1.png` shows separate rows and separate results. This small array
is an artificial illustration; real ECG errors are computed separately.
For the actual (128, 140) array, the same operation returns 128 MAEs. MAE is not a percentage.

`sample_index` selects which normal and anomalous signal to highlight.
`reconstructions.png` shows them, while `error_distribution.png` includes all
128+128 practice signals. In the histogram, the horizontal axis is error and
the vertical axis is a count. The groups can differ while still overlapping.

Run `G05_03_reconstruction_error.py` unchanged and send the selected normal and
anomalous signal MAEs. Then we will examine the curves together.

**Before changing the index:** Explain here too that 3 selects the fourth normal
and fourth anomalous example for closer inspection, because 0 is first. Only
the highlighted pair changes, not the full group or histogram. Do not expect
new learning or errors from a newly trained model.

## 4. Threshold: when does an error become an alert?

So far we have calculated reconstruction errors. Now we add a rule for flagging
anomalies. The network and error values remain the same; only the decision
boundary moves. We use the same supplied reference as in the previous program.
The program recomputes its MAEs from those fixed reconstructions.

```python
threshold = 0.04
normal_alerts = normal_errors >= threshold
anomalous_alerts = anomalous_errors >= threshold
```

Each signal's error is compared with the threshold. Equality also triggers an
alert. True values in these Boolean arrays mean the rule predicts an anomaly;
they do not change the actual labels.

```python
false_alarms = int(np.sum(normal_alerts))
correct_anomalous = int(np.sum(anomalous_alerts))
```

The first line counts alerts on genuinely normal signals: false alarms.
The second counts alerts in the genuinely anomalous group: correct detections.
An anomalous signal without an alert is a missed anomaly. The output gives all
four counts, and `decisions.png` shows them in a table. The vertical line in
`error_distribution.png` marks the decision boundary. `~` inverts a Boolean
array, so it lets us count signals that were not flagged.

The positive class in this lesson is anomalous. The baseline 0.04 is a setting
for comparison, not a general medical limit or a threshold suitable for every model.

Run `G05_04_threshold.py` unchanged and send the four counts. We will interpret
these first and introduce percentage metrics afterwards.

**Precision and recall: separate explanations, separate questions.**

The upper bar in the current `precision_recall.png` starts with all alerts.
At reference threshold 0.06, there are 127: 121 correct and 6 false.
"Precision asks: what proportion of our alerts are correct?" Start with counts,
then show precision = 121/(121+6) = 121/127 ≈ 95.3%.
Ask: "Why are we dividing by 127 here?" Wait for the answer and clarify it.

The lower bar starts with all 128 actual anomalies: 121 detected and 7 missed.
"Recall asks: what proportion of the actual anomalies did we find?"
Recall = 121/(121+7) = 121/128 ≈ 94.5%.
Ask: "Why do the seven missed signals belong in recall's starting group?" Wait.

The numerator is the same: correct detections. The denominators differ: all
alerts versus all actual anomalies. The bars show counts, not bars stretched
to 100% each. The console also explains the groups in words. Use the student's
actual numbers. With no alerts, precision is undefined; both program and image
say so. Do not jump directly from definitions to the quiz: both short answers
must be discussed first.
