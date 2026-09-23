# Program guides - explanatory support for Inno

The overview is told by the tutor, it is not replaced by the request "read this file".
The examples show the initial code of the package; after a modification always explain the actual
source. The plotting of helpers.py does not have to be learned line by line.

## Mandatory presentation minimum - 1.2

The following table helps the tutor prepare; you must actually
show the affected code to the learner BEFORE the run. It is not enough that it is written here.
At most two short blocks per message, with one targeted learner step between them.

| Program | Details to present |
|---|---|
| L03_01 | Prediction/error; both np.mean gradients; the update of weight and bias |
| L03_02 | One-hot and integer label; Input/Dense; compile; the complete fit; evaluate and predict/argmax |
| L03_03 | The new hidden layer; the independent 50-50 build; changing the rate 0.01 -> 0.001 |
| L03_04 | Own choice and reason; load_model/evaluate; interpreting the test figure |

## L03_01 - A single linear neuron with a visible weight update

**What is the purpose of the program?** We predict a score from the learning time of an imagined
learner. Each line is a time-score pair; all 100 pairs are artificial.
The relation is roughly a straight line, with some noise. The neuron has a single input,
one weight and one bias; it gives a linear output. It learns the weight and the bias from the 80
selected training pairs, the 20 validation pairs serve only for checking.
This makes the manual gradient method of the notebook traceable in a standalone program.

**Data path:** generating the data -> prediction -> deviation and gradient ->
modifying weight/bias -> loss and figures. There is no file download.

```python
prediction = weight * train_x + bias
error = prediction - train_y
```

train_x contains 80 time values at once, so the multiplication gives 80 predictions.
train_y is the known target, the error is the prediction minus the target. A positive error means
an overestimate, a negative one an underestimate. The bias is a shift independent of the input:
at zero learning time the prediction is the bias. We cannot confirm a causal
relationship or real learner performance from synthetic data.

```python
weight_gradient = np.mean(error * train_x)
bias_gradient = np.mean(error)
```

np.mean averages over the training pairs. The weight is multiplied by the input,
therefore its gradient contains train_x; the bias gradient does not. The two numbers indicate
how the average loss would change for a small change of the given parameter.
L = mean((prediction - target)^2) / 2. The halving removes the 2 coming from the derivation.
The meaning of the formula has to be seen, not derived independently.

```python
weight = weight - LEARNING_RATE * weight_gradient
bias = bias - LEARNING_RATE * bias_gradient
```

We step in the direction opposite to the gradient. The rate scales the size of the step;
it is not the learned weight of the network. Subtracting a negative gradient increases the
parameter. Here every update uses the complete 80 samples: one epoch is one weight update.
The training repeats this 120 times. The figures show the loss AFTER the update;
the first point is already the result of the first step.

**Evaluation:** loss.png: two curves; regression.png: the learned line and the points.
Because of the noise the line does not have to pass through every point. A lower
loss means a smaller average squared error in this same task.
Before every image opening the View file list has to be refreshed.

## L03_02 - Three spiral classes, a simple baseline model

**What is the problem?** From the two coordinates of a point in the plane we have to say which
spiral arm's class it belongs to. The labels are 0, 1, 2; they do not mean a quality
order. We generate 600 points following the principle of the notebook,
with reproducible random noise. From the two coordinates the network gives a probability estimate
for three classes. This is classification, in contrast to the single continuous score of the
previous program.

**Data path:** spiral points -> 360/120/120 split -> one-hot targets ->
model and training -> validation curves, decision figure, saved model.
The coordinates here are already roughly between -1 and 1, therefore there is no separate scaler.
We now only set the test aside, we do not use it to select the architecture.

```python
train_target = keras.utils.to_categorical(train_labels, num_classes=3)
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(3, activation="softmax"),
])
```

The one-hot shape of label 2 is [0,0,1]. The shape of train_target is (360,3), that of train_x is
(360,2): the target is not a third input coordinate. shape=(2,) describes two features within one
sample, the comma forms a one-element Python tuple. Dense connects every output neuron to every
input. The three softmax values are non-negative and their sum is numerically close to 1. A class
estimate is not certainty.
In this model there is no hidden layer: we get pairwise straight decision boundaries.

**Two label representations, the same class:** teach this difference before the test.

| Target for one sample | Shape of the whole target set | Loss matching the three softmax outputs |
|---|---|---|
| `[0,0,1]` | `(N,3)` | `categorical_crossentropy` |
| `2` | `(N,)` | `sparse_categorical_crossentropy` |

to_categorical makes a one-hot shape from the integer label. The two losses handle the same
multi-class problem with a different target representation; it does not mean that the sparse one
is inherently better or worse. Here the one-hot target stays,
therefore we use categorical_crossentropy. The learner has to recognise this pairing, they do not
have to implement a new loss.

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
```

Adam updates the parameters based on the gradients, with its own adaptive
step rule. The learning_rate is still an important scaling setting.
The cross-entropy penalises the difference between the known one-hot target and the softmax
distribution; a small probability assigned to the correct class gives a large penalty.
Accuracy is the proportion of correctly classified samples; it is a metric, not a loss
minimised here. compile only prepares, it does not train yet.

```python
history = model.fit(
    train_x, train_target,
    validation_data=(val_x, val_target),
    epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=0,
)
```

The first two arguments of fit are the input coordinate array and the target array aligning with
it row by row. In the brackets of validation_data there is a separate checking input-target
pair. The return value, history, contains the measurement history of the training.
evaluate, by contrast, measures the metrics of the current model on the given data.
fit performs the training. An epoch is a single pass over the complete training set;
with a batch of 32 one step uses the gradient computed on at most 32 samples.
360 samples: 11 complete batches of 32 and one of 8, 12 updates per epoch in total.
On the validation data we measure once per epoch, but there is no weight update from them.
verbose=0 switches off the per-epoch screen text, not the training.
history.history contains the loss, val_loss, accuracy and val_accuracy series.

```python
probabilities = model.predict(val_x[:5], verbose=0)
predicted_classes = probabilities.argmax(axis=1)
```

[:5] selects the first five samples. The result of predict is a 5 x 3 array,
not five labels. argmax selects the index of the largest value row by row.
For example [0.10,0.75,0.15] -> 1. The 0.75 is the probability estimate,
the 1 is the class index. predict does not train. The ready plotting code uses the same conversion
to colour the points; it does not give the complete 3-vector to the scatter plot as an RGB colour.

**What should we watch?** The spiral is hard to separate with straight lines.
A weak result here may also indicate the limit of the simple model class.
The loss can change even when the argmax classes and the accuracy do not change.

## L03_03 - Creating and extending a hidden layer

**What changes?** We classify the same points, but the model also learns intermediate features.
The initial network has 16 ReLU neurons. The input is two coordinates, the output is still three
class estimates. Afterwards the learner builds two 50-neuron hidden layers. The plotting code is
the same, so the attention stays on the creation of the model and on its result.

```python
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

The first Dense computes 16 weighted sums from the two coordinates and 16 biases.
The ReLU puts a zero in place of a negative sum, and keeps the positive one.
The output layer then computes three softmax values from 16 learned intermediate values.
The non-linearity applied in the hidden layers makes bendable, piecewise
linear decision boundaries possible. Several linear layers without activation
would not give such new non-linear expressive power.

| Network | Parameters | Counting aid |
|---|---:|---|
| 2 -> 3 | 9 | 2x3 + 3 |
| 2 -> 16 -> 3 | 99 | (2x16+16) + (16x3+3) |
| 2 -> 50 -> 50 -> 3 | 2853 | (2x50+50) + (50x50+50) + (50x3+3) |

model.summary / count_params also give these numbers; the learner does not have to be examined
from memory. A larger model means more trainable parameters, not automatically a better
generalisation. The learning rate, epoch and batch stay the same in the mandatory architecture
comparison.

**Interpreting the four ready figures:**

- loss.png: training and validation cross-entropy; the lower one is more favourable.
- accuracy.png: the proportion of correct classifications on both sets; the higher one is more favourable.
- decision_regions.png: the background is the decision, on two panels the true / predicted point colour.
  The colour of the classes is the same on both panels: 0 blue, 1 orange, 2 green.
- confusion_matrix.png: the row is the true class, the column is the predicted class. Cell (0,2)
  for example counts the 0-class points that the model marked as 2.

If the training loss decreases and the validation one keeps getting worse, that may indicate
overfitting. If both are bad, the cause may also be too little training, hard optimisation or a
too simple model. The curve by itself does not prove any single diagnosis.
The identical seed of the runs helps to compare them, but a different architecture starts with a
different set of parameters, and a single seed does not give statistical evidence.

### Why can the ranking by accuracy and by loss differ?

The learner should first interpret the metrics of their own runs. Do not reveal the answer of the
independent comparison in advance. If help is needed, use this separate
teaching example, which is not the result of the learner's run:

The true label is 1. Two estimates: `[0.20,0.65,0.15]` and `[0.05,0.90,0.05]`.
Both choose class 1, therefore both are correct from the point of view of accuracy. The second
assigns more probability to the true class, therefore its cross-entropy is smaller:
`-ln(0.65)` is about 0.431, `-ln(0.90)` is about 0.105.
Nobody has to compute a logarithm. Over several samples the average loss can improve even while
the argmax decision gets worse on one sample. This explains how a smaller average loss is possible
with fewer correct labels.

The ranking does not prove that one model is better in every respect.
The rule of the lab, stated IN ADVANCE, chooses the smaller validation loss;
the more parameters of the larger network and its accuracy are interpreted separately.
100% holds only for the measured data set, not for every future point.

### Mandatory R4 - the same network with a different learning rate

**Overview:** in R3 the network with the 50-50 hidden layers and a rate of 0.01 is already ready.
Now we examine how the course of the training changes on the same data and epoch budget if we
decrease only the rate. We do not write a new program and we do not continue the training of the
earlier weights. A new run is made, the existing plotting code saves the curves of both runs into
separate folders.

```python
LEARNING_RATE = 0.001
```

The learner modifies this single setting. The Adam constructor receives it as
learning_rate. The two 50 layers, the 150 epochs (or the common budget selected in advance), the
batch of 32, the seed and the points are unchanged. The identical architecture and seed support a
comparable initialisation.
The smaller rate may result in a different optimisation path; it does not ensure a better
final result, and because of the adaptive updates of Adam we do not simply divide every step of
the whole training by ten. There is no prescribed "correct" curve shape.

After the Run, at the end of the log the actual rate of 0.001 and the 50-50-3 layers also have to
be checked. The learner refreshes the View, compares the loss.png figures of R3 and R4, and names
the behaviour of the training and validation curve separately.
What do they see in the initial decrease, in a later fluctuation or in a flattening,
and which run has the smaller final validation loss? They answer first,
the tutor only links the observation to the settings afterwards.

R4 is also part of the final comparison of four runs. It is not necessarily
the most recently run model that is chosen. Because of the earlier saves
there is no need to restore the code before starting L03_04.

## L03_04 - The independent test of the chosen model

**What is the goal?** The learning and the validation comparison are already done. Now we check
the chosen network on the points set aside earlier. The program
does not train a new model, it loads the .keras file of the earlier run. After comparing R1-R4 the
learner gives the SHORT LABEL of the run (R1, R2, R3 or R4) and the reason of the preliminary
choice in their own words; they do not have to paste the long folder name. The tutor must not give
them a ready-made justification in advance. The figures and metrics go into the final_test
subfolder of the given run.

**The program checks the choice.** Without a filled-in label it prints only the comparison table
of the runs (label, structure, parameter count, rate, validation loss), and does not test; it
deliberately does not mark the winner then, the learner has to determine that. With a filled-in
label it prints the "CHOICE CHECK" part (the table with the winner marked, the comparison of the
chosen run and the decision), and if the chosen run is not the one with the lowest validation
loss, it stops. For a deliberate deviation the OVERRIDE line has to contain "YES"; choice.json
also reports this fact.

```python
model = keras.models.load_model(run_dir / 'model.keras')
test_target = keras.utils.to_categorical(test_labels, num_classes=3)
result = model.evaluate(test_x, test_target, verbose=0, return_dict=True)
```

load_model restores the layers and the learned weights. evaluate computes the loss and the
accuracy from the data; with return_dict=True these are available by name in the result. There is
no fit, so the weights do not change and there is no new epoch curve. The test result is the
evaluation of the procedure selected in advance. If we started choosing another model based on it
afterwards, we could no longer regard it as an untouched final check.

**After the metrics there is still figure interpretation.** Refresh the View, then
final_test/decision_regions.png and confusion_matrix.png. The learner interprets one
true/predicted label pair and its count. In a perfect case they explain the meaning of the
diagonal and of the zeros, and that the accuracy is valid for the 120 examined test points. The
tutor waits for this answer before starting the closing code-comprehension test. A large softmax
output close to 1 by itself does not prove guaranteed correctness or proper calibration.

## Prepared technical background - briefly

helpers.py uniformly generates and splits the data, prepares the figures and saves the
experiments. The `Agg` plotting mode prepares a file instead of a pop-up window. The paths follow
the location of the .py file, not the random working directory of the terminal. Every training
gets its own folder, whose name starts with the short label of the run (for example
R3_50x2_lr0.01_0922-124351), containing the source snapshot, the settings, the model file and the
CSV of the curves. The label is computed from the actual network and the learning rate,
therefore the folder name cannot "slip away" from the settings; the
"run_label" field of settings.json records the same thing.
The source snapshot is documentation, the program is not to be restarted from it.
Refreshing the View only displays the newly created files.
