# Program introductions and code explanations

The first part of each section is a ready-to-deliver student introduction.
Give it BEFORE the first run, including the code blocks and their explanations.
Do not reduce it to a statement of purpose or assign it as reading. End with one
execution task and wait for the result. “Further explanation” supports questions
and revision; do not deliver all of that background at once. Always check the
actual file: these examples show starting versions that the student may have
changed. The snippets explain existing code; they are not new programs to paste in.

## G04_01 – turning a gradient into a weight update

### Introduction to give before the first run

In `G04_01_learning_rate.py`, we explore how the learning rate affects a single
weight. We change one number, `weight`, towards the target 3. The loss is
`(weight - 3) ** 2`: the squared distance from the target, which becomes zero
at the target. We are examining weight updates without a dataset or a complete network.

The starting settings are:

```python
learning_rate = 0.1
number_of_steps = 8
initial_weight = -1.0
```

The initial weight determines where we start. The learning rate controls the
size of an update, while the step count determines how often we perform it.
Inside the loop, these three lines do the calculation:

```python
gradient = 2 * (weight - 3)
weight = weight - learning_rate * gradient
loss = (weight - 3) ** 2
```

The gradient is the local slope of the loss; its formula is already supplied.
Its sign indicates the direction of increase, so the second line subtracts the
gradient multiplied by the rate. The third line measures loss using the **new**
weight. Let's work through the first update: at −1 the gradient is −8, so the
new weight is −1 − 0.1·(−8) = −0.2. Subtracting a negative value increased the
weight. The new loss is (−0.2−3)² = 10.24.

The output columns show the step, weight and loss. Row 0 is the starting state.
`learning_steps.png` plots their changes. Later, you will change the learning
rate and step count separately. For now, run the file without changes using Run
and send the last row. We will use it to see where the weight ended up.

### Further explanation – for questions or revision

The first line calculates sensitivity at the old weight; the second uses it to
update the weight; the third evaluates the new state. You do not need to compute
many updates mentally. We work through one step together, and the program and
figure show the rest. `range(number_of_steps)` sets the repetition count.
Formatting or `round` affects displayed decimal places, not the underlying
calculation's precision. CSV output retains every step; long console output is shortened.

## G04_02 – the momentum update

### Introduction to give before the first run

The previous example based every update on the current gradient. In
`G04_02_momentum.py`, we explore what happens when an update also retains some
previous movement. We have two parameters, x and y. The loss is `x*x/20 + y*y`,
with its minimum at (0, 0). The surface is flatter in one direction and steeper
in the other. Again, there is no dataset or complete neural network.

The `trajectory(beta)` function starts with:

```python
position = np.array([-7.0, 2.0])
velocity = np.zeros(2)
```

`position` is an array of two parameters. `position[0]` is the first value and
`position[1]` the second. Velocity also contains two numbers, initially both zero.
Inside the loop:

```python
gradient = np.array([position[0] / 10, 2 * position[1]])
velocity = beta * velocity - learning_rate * gradient
position = position + velocity
```

The first line calculates the loss slope in both directions. The next line
combines `beta` times the old velocity with the current gradient step. The last
line moves the point using this velocity. Array operations apply to both
coordinates. The `momentum = 0.9` setting becomes the function's `beta` argument:
90% of the previous velocity contributes to the next update.

The program computes two paths from the same point: `trajectory(0.0)` and
`trajectory(momentum)`. Both use rate 0.1 and 40 steps. Console output gives the
endpoints and final losses; `trajectories.png` shows the paths. Contour lines
connect positions with equal loss. Later you will change only momentum. Now run
the file without changes and send the two endpoints and losses for comparison.

### Further explanation – for questions or revision

The gradient components are x/10 and 2*y. `copy()` stores an independent copy of
the state for the figure. With beta=0, previous velocity has no effect and the
rule reduces to plain gradient descent. On the figure, green marks the start,
orange marks the final point and a black cross marks the minimum. Both panels
use the same axis limits, allowing the paths to be compared.

## G04_03 – activation output and derivative are different

### Introduction to give before the first run

`G04_03_activations.py` isolates another part of a neuron: its activation and
its role in passing gradients backwards. The five inputs are −6, −1, 0, 1 and 6.
Treat them as weighted sums that have already been calculated. We do not train
a network; we only transform these values. `activation = "sigmoid"` selects the
first function. Later you will also try ReLU and Leaky ReLU.

The sigmoid branch inside `activation_function(z)` is:

```python
if activation == "sigmoid":
    return 1 / (1 + np.exp(-z))
```

`z` is the input, and `np.exp` calculates the exponential function. Sigmoid
produces a value between 0 and 1. The separate `derivative(z)` function describes
how sensitive the output is to a small input change. For sigmoid, it uses
`value * (1 - value)`; you are not expected to derive this formula.

The program then creates three separate arrays:

```python
outputs = activation_function(inputs)
local_derivatives = derivative(inputs)
returned_gradients = incoming_gradient * local_derivatives
```

The first holds the forward activation outputs. The second holds local slopes.
The third holds gradients passed backwards: the signal arriving from a later
part of a network is multiplied by the local derivative. Here that incoming
gradient is a supplied value of 2, separate from the activation input. At z=0,
for example, sigmoid is 0.5, its derivative is 0.25 and the returned gradient is
2·0.25 = 0.5.

The four table columns show input, output, local derivative and returned
gradient. The figure displays the function and derivative separately. Later you
will change the inputs and then the activation. Now run the unchanged file and
send the rows for inputs 0 and 6. We will compare their local derivatives.

### Further explanation – for questions or revision

We do not calculate a weighted sum here; only the nonlinear transformation is
being examined. For sigmoid, large absolute inputs lead to saturation and a small
derivative. The output cannot be negative, but gradients of a full network's
weights can still be negative.

The relevant expressions inside the activation function are:

```python
np.maximum(0, z)
np.where(z > 0, z, negative_slope * z)
```

The first is ReLU: choose the larger of 0 and z for each element. The second is
Leaky ReLU: use z for a positive input, otherwise multiply z by the negative
slope. `np.where` takes a condition, the true branch and the false branch.
The derivative function returns the slope of the selected branch.

```python
returned_gradients = incoming_gradient * local_derivatives
```

This is the local chain-rule step. The incoming gradient 2 is not an activation
input. At zero, the program selects derivative 0 for ReLU and the left-branch
slope for Leaky ReLU. This is a computational convention at a kink, not a claim
that the two one-sided slopes are equal. One inactive negative ReLU input does
not prove that a neuron is permanently dead.

## G04_04 – a small regression network

### Introduction to give before the first run

`G04_04_small_network.py` trains a real neural network on the CPU. It predicts a
continuous y value from a single x number: this is regression. The program
creates 192 synthetic points from a wavy function with added noise. There are
64 training points and 128 validation points. Validation points do not update
weights. The prepared data-handling code stays in the background for now.

First we build the model:

```python
model = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(HIDDEN_UNITS, activation="relu"),
    layers.Dense(1),
])
```

`Sequential` connects layers in order. `Input(shape=(1,))` means one input feature
per sample. The hidden Dense layer initially has eight units: each calculates a
weighted sum with a learned bias and then applies ReLU. The final `Dense(1)`
combines these into one prediction. It has no sigmoid; its output need not stay
between 0 and 1.

Next, `model.compile(...)` configures training. Adam uses a learning rate of
0.01; `loss="mae"` means mean absolute error. If a target is 0.7 and a prediction
is 0.5, that sample's absolute error is 0.2. MAE averages these errors in the
target's units; it is not a percentage. Compile does not train yet. Training
starts here:

```python
history = model.fit(
    training_data,
    validation_data=validation_data,
    epochs=EPOCHS,
    shuffle=False,  # The prepared dataset already shuffles the training samples.
    verbose=0,
    callbacks=[BriefProgress(EPOCHS)],
)
```

`training_data` contains input–target pairs. An epoch visits all 64 training
samples once. With batches of 16, that gives four weight updates per epoch.
`EPOCHS = 120` means 120 such passes. `validation_data` is measured at each epoch's
end. The prepared dataset handles shuffling; `verbose` and the progress callback
control messages. `history` retains per-epoch measurements.

At the end, the program reports training and validation MAE for the final model
state. `prediction.png` shows points and predictions; `learning_curves.png`
shows how errors developed. Later you will change the hidden-unit count and
epoch count, starting a fresh model each time. Now run the unchanged file, wait
for RUN SUMMARY and RUN COMPLETE, then send the two final MAEs.

### Further explanation – for questions or revision

Each sample has one x value between −3 and 3 and one noisy target y. Noise is not
an extra input. Each run generates the same 64/128 sample split. `shape=(1,)`
means one feature per sample, not one sample. Bias is a learned offset.
Eight hidden units give 25 trainable parameters; 64 units give 193. The program
prints this count, so no mental calculation is required.

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
```

Adam uses gradients to calculate updates. Rate 0.01 remains fixed in the required
network experiments. MAE is also tracked as a separate metric, which matters
when we add L2. `jit_compile=False` is a technical setting, not an exercise.

The prepared datasets already contain paired inputs and targets, arranged into
batches of 16 and reproducibly shuffled. Therefore fit does not need a separate
`batch_size` argument or another shuffling operation. `shuffle=False` does not
mean there is never any shuffling: the dataset does it. The progress callback
only prints selected epoch numbers; it does not stop training or restore weights.

Measurement in the prepared helper uses:

```python
validation_prediction = model(val_x, training=False).numpy()
validation_mae = float(np.mean(np.abs(val_y-validation_prediction)))
```

`training=False` requests evaluation behavior. This two-Dense-layer model has
no dropout or batch normalization, but the argument clarifies that we are
predicting. This call does not train. `.numpy()` returns tensor values as a
NumPy array for measurement and plotting.

The three figures mean:

- `prediction.png`: data points and the network's continuous prediction. The
  dashed gray line is the known noise-free data-generating function, not a test result.
- `learning_curves.png`: training and validation MAE by epoch. Training MAE
  averages measurements made while weights change; validation measures the epoch-end state.
- `loss_and_mae.png`: without a penalty, the two validation quantities coincide;
  they can separate in the next program.

The 400-epoch run restarts from the initial state rather than continuing the
120-epoch model. Final output measures the last weights, not the lowest plotted value.

## G04_05 – adding L2

### Introduction to give before the first run

`G04_05_l2_regularization.py` adds a weight penalty to the previous network.
It uses the same training and validation data. This independent file specifies
64 hidden units and 120 epochs: it corresponds to the earlier 64-unit,
120-epoch experiment and trains a fresh model. `L2_STRENGTH` is the only setting
we will investigate. Initially it is 0.0, so the penalty is zero.

The model introduces the new argument here:

```python
model = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(HIDDEN_UNITS, activation="relu",
                 kernel_regularizer=regularizers.l2(L2_STRENGTH)),
    layers.Dense(1, kernel_regularizer=regularizers.l2(L2_STRENGTH)),
])
```

`kernel_regularizer` assigns a penalty to the layer's weight matrix. The L2
strength, also called λ, multiplies the sum of squared weights. Keras adds this
to prediction loss, making large weights costly during training. Both Dense
kernels are penalized here, but biases are not. In the related HTML/Spotify
example, only hidden-layer kernels receive this penalty.

Two compile arguments serve different roles:

```python
loss="mae",
metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
```

These are arguments inside the existing function call. The prediction component
of loss is MAE; Keras adds L2 to form total loss. The separate `mae` metric
measures prediction error alone. A worked example, not a measured result:
weights [2, −1] with λ=0.01 give penalty 0.01·(4+1)=0.05. If MAE is 0.12,
total loss is 0.17.

Output reports MAE, penalty, total loss and kernel sum of squares separately.
`loss_and_mae.png` plots the two validation quantities. We will compare
prediction quality using validation MAE. Now run the starting version with
L2 strength 0.0 and 120 epochs, then send both final MAEs and total validation loss.

### Further explanation – for questions or revision

The model, data, rate and 120 epochs are fixed; only λ changes. The regularizer
adds λ times the sum of squared entries in each selected kernel. It does not
penalize biases. This formula describes its meaning:

```python
# Conceptual relationship; Keras performs the addition during training.
# total_loss = prediction_mae + l2_penalty
```

The separately tracked MAE excludes regularization. Compare models trained with
different λ using validation MAE on the same data. The printed sum of squares
is not the L2 norm; a square root would be needed for that norm. Smaller weights
under a stronger penalty do not guarantee better predictions.

## G04_06 – dropout on a short array

### Introduction to give before the first run

`G04_06_dropout.py` makes the dropout mechanism visible using eight positive
numbers, representing a layer's activations. We are not training another
network; we are observing which values pass through and how their sizes change.
`training_mode = True` selects the transformation mode. The initial
`dropout_rate = 0.5` gives each element a 50% probability of being dropped.

The training branch is:

```python
if training_mode:
    mask = rng.random(len(inputs)) >= dropout_rate
    outputs = inputs * mask / (1 - dropout_rate)
```

For every input, the first calculation generates a random number between 0 and 1.
A true comparison means retain the element; false means drop it. In multiplication,
the Boolean mask behaves like ones and zeros. The next line zeros dropped values
and divides retained values by the retention probability. At a dropout rate of
0.5 this doubles retained values: a retained 0.8 becomes 1.6. That is an example,
not a prediction of the mask you have not yet seen. Scaling preserves expected
activation magnitude. A short vector is not guaranteed to lose exactly half its
elements or preserve its actual average.

The other branch is:

```python
else:
    mask = np.ones(len(inputs), dtype=bool)
    outputs = inputs.copy()
```

In evaluation mode, every value passes through. `copy()` creates a separate
array with the same values; there is no further scaling. A zero is not a deleted
neuron. With `random_seed = 42`, rerunning unchanged settings gives the same
sample. Later you will separately change the rate, seed and mode.

Console output shows inputs, mask and outputs; `dropout.png` compares input and
output values. Now run the unchanged file and send the mask and output. We will
use your own values to examine masking and scaling.

### Further explanation – for questions or revision

Using eight positive activations makes random zeros visible. `>= p` gives a
retention probability of 1−p. Mask 0 produces zero; mask 1 gives multiplication
by 1/(1−p). This preserves each activation's expected value, not necessarily the
actual average of one short vector. Evaluation passes inputs through unchanged.
The example demonstrates a mechanism, not evidence that dropout must improve
the previous regression model.

## K04_01 – optional softmax introduction

Use only on request. `K04_01_softmax.py` turns three class scores, called logits,
into jointly normalized probabilities. The starting scores 2, 1 and 0 are not
yet probabilities. There is no training.

```python
shifted_logits = logits + common_shift
exponentials = np.exp(shifted_logits - np.max(shifted_logits))
probabilities = exponentials / np.sum(exponentials)
```

The first line adds the same number to every score. The second subtracts the
maximum before exponentiating, avoiding exponential overflow from very large
positive scores here. The third divides positive values by their sum, so the
result sums to 1. The elements depend on each other through the shared denominator.
The program prints scores, probabilities and their sum, then saves a bar chart.
Later you will change the common shift. Now run the starting version and send
the three probabilities and their sum.

## K04_02 – optional batch normalization introduction

Use only on request. `K04_02_batch_normalization.py` shows normalization followed
by scaling and shifting on values 1, 2, 3 and 4. Gamma and beta are manually set
here; in a real layer they are trainable. This program does not train a network.

```python
if training_mode:
    mean = np.mean(inputs)
    variance = np.mean((inputs - mean) ** 2)
else:
    mean = stored_mean
    variance = stored_variance
```

Training mode calculates the mean and variance, or mean squared deviation,
from the current four values. The other branch uses supplied stored statistics.
These are illustrative values, not measurements from an earlier training run.

```python
normalized = (inputs - mean) / np.sqrt(variance + epsilon)
outputs = gamma * normalized + beta
```

First we subtract the mean and divide by a quantity close to the standard
deviation; a small epsilon stabilizes division. Gamma scales; beta shifts.
Initially gamma=1 and beta=0. Output separately reports the statistics used,
normalized values and final outputs. The figure compares outputs with inputs.
Later you will change gamma, beta and mode separately. Now run the starting
version and send the normalized values and final outputs.
