# Detailed program walkthroughs

This guide explains the code more deeply than the student needs to memorize. Use
it to teach the important blocks slowly and in context.

# G02_01_data_preparation.py

## What the program does

It prepares a real table for neural-network training. It does **not** create a
network. The main output is six objects: input and target data for training,
validation and testing.

## `Path` and the data file

```python
DATA_FILE = Path(__file__).resolve().parent / "data" / "red-wine.csv"
```

This constructs the file path relative to the Python script. The detailed syntax
is not a deep-learning concept. Students only need to know that `DATA_FILE`
points to the included CSV file.

## Reading the CSV

```python
raw_data = pd.read_csv(DATA_FILE)
```

`pandas` reads the CSV into a `DataFrame`. Think of a DataFrame as a table with
named columns. One row corresponds to one wine sample.

## Removing exact duplicate rows

```python
data = raw_data.drop_duplicates().reset_index(drop=True)
```

This keeps one copy of completely identical rows. `reset_index` creates a clean
row index afterwards. These are useful data-cleaning operations, but neither
method is the central learning objective.

## Separating X and y

```python
features = data.drop(columns=["quality"])
target = data["quality"]
```

This is one of the most important blocks of the lesson.

`features` (often called **X**) contains what the model is allowed to see.
`target` (often called **y**) contains the correct answer.

The model must not receive `quality` as an input, because that would reveal the
answer. For each wine the network receives 11 measured properties and learns to
predict one quality value.

## Splitting the data

First:

```python
train_pool, test_features, train_pool_target, test_target = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=RANDOM_SEED,
)
```

Twenty percent is reserved for testing. The remaining 80% is still a temporary
training pool.

Then:

```python
train_features, validation_features, train_target, validation_target = train_test_split(
    train_pool,
    train_pool_target,
    test_size=0.25,
    random_state=RANDOM_SEED,
)
```

A quarter of the remaining 80% becomes validation data. A quarter of 80% is 20%
of the original dataset, so the final proportions are approximately:

- 60% training;
- 20% validation;
- 20% test.

`random_state` makes the random split reproducible. The exact mechanism is not
important now; reproducibility is the useful idea.

## Scaling

```python
scaler = MinMaxScaler()
```

The scaler will create one scaling rule for each input column.

The key line is:

```python
train_scaled = scaler.fit_transform(train_features)
```

It performs two ideas at once:

1. **fit:** learn minimum and maximum values from the training columns;
2. **transform:** use those learned values to rescale the training data.

For validation and test data we only use `transform`:

```python
validation_scaled = scaler.transform(validation_features)
test_scaled = scaler.transform(test_features)
```

Why? Because validation and test data are supposed to represent unseen data. If
we let them influence the scaler, information from the future evaluation data
would leak into preprocessing.

A useful plain-language rule is:

> **Learn preprocessing rules from training data; apply those rules everywhere else.**

# G02_02_model_and_compile.py

## What is new in this program?

The data-preparation block is deliberately repeated. Students have already seen
it, so do not teach every line again. The new learning goals are the network and
`compile()`.

## Input shape

After preprocessing:

```python
train_scaled.shape
```

has two dimensions: number of training samples × number of features. The second
number is 11, therefore one wine enters the network as 11 numbers.

## Sequential model

```python
model = keras.Sequential([
    keras.Input(shape=(train_scaled.shape[1],)),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),
])
```

Read the code from top to bottom as a data path.

### `keras.Input(...)`

```python
keras.Input(shape=(train_scaled.shape[1],))
```

The shape describes **one sample**, not the whole dataset. Each sample has 11
features. Keras will handle the number of samples separately.

### First hidden layer

```python
layers.Dense(32, activation="relu")
```

`Dense(32)` means 32 neurons. “Dense” means each neuron receives all outputs from
the previous layer.

`activation="relu"` means the layer applies the ReLU activation. At this stage,
students only need the reason for using an activation: without non-linear
activations, stacking layers would not give the network the same ability to
model complex non-linear relationships.

### Second hidden layer

```python
layers.Dense(16, activation="relu")
```

The 32 values from the first hidden layer become inputs to 16 neurons in the
second hidden layer.

### Output layer

```python
layers.Dense(1)
```

There is one neuron because the task asks for one number: predicted wine quality.
There is no classification probability here.

## `model.summary()`

`summary()` prints the layer shapes and parameter counts. Students should learn
to read the architecture from it, but they do not need to calculate every
parameter count by hand in this lesson.

## `compile()`

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=["mae"],
)
```

This is configuration, not training.

### Optimizer

The optimizer controls how the network weights are updated using the information
from the error and gradients. We use Adam. The mathematical details of Adam are
outside the lesson.

### Learning rate

```python
learning_rate=0.003
```

The learning rate controls the size of update steps. It is an important training
hyperparameter, but this lesson does not compare many learning rates.

### Loss

```python
loss="mae"
```

MAE is mean absolute error. Conceptually, it asks: **on average, how far are our
predictions from the known target values, ignoring the sign of the error?**
Training attempts to reduce the loss.

### Metric

```python
metrics=["mae"]
```

Metrics are values reported for interpretation. Here the metric is the same
quantity as the loss, which keeps the exercise simple.

# G02_03_fit_and_evaluate.py

## Why repeat the first two sections?

The complete program must be runnable by itself. Data preparation and model
construction are therefore repeated, but labelled as already familiar. The new
focus starts at `fit()`.

## `fit()` – the central call

```python
history = model.fit(
    train_scaled,
    train_target,
    validation_data=(validation_scaled, validation_target),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=2,
)
```

Read the arguments as a sentence:

> Train this model using these training inputs and targets, check performance on
> this validation set, make at most 40 passes through the training data, process
> the data in groups of 64, and print a short progress line for each epoch.

## Training inputs and targets

```python
train_scaled,
train_target,
```

Each row in `train_scaled` is one wine. The corresponding position in
`train_target` contains its known quality. During supervised learning, this pair
provides both the input and the answer needed to calculate the error.

## Epoch

```python
epochs=EPOCHS
```

One epoch is one complete pass through the training set. `epochs=40` gives the
optimizer repeated opportunities to improve the weights.

Do not describe an epoch as “one update”. There are normally many updates inside
one epoch because the data is divided into batches.

## Batch size

```python
batch_size=BATCH_SIZE
```

With `BATCH_SIZE = 64`, the training data is handled in groups of about 64
samples. After processing a batch, the optimizer can perform a weight-update
step. The final batch of an epoch can be smaller.

The important distinction is:

- **batch:** a small group inside an epoch;
- **epoch:** one pass through the complete training set.

## Validation data

```python
validation_data=(validation_scaled, validation_target)
```

At the end of an epoch, Keras can evaluate the current model on validation data.
This lets us see whether improvements on training data are also reflected on data
that did not participate in the ordinary weight updates.

## History

```python
history = model.fit(...)
```

`fit()` returns a `History` object. It stores the sequence of values reported over
training, such as `loss` and `val_loss`.

Later:

```python
curves = pd.DataFrame(history.history)
```

converts that stored record into a small table that is convenient for saving and
plotting.

## Evaluation

```python
validation_result = model.evaluate(...)
```

`evaluate()` calculates the configured loss and metrics on a dataset without
training the model.

## Prediction

```python
predictions = model.predict(validation_scaled[:5], verbose=0)
```

`predict()` performs a forward pass using the current learned weights. Here we
only predict five examples so the result is easy to inspect.

## Plotting and saving – support code

Everything in the final “SUPPORT CODE” section exists to save the history and
draw a PNG figure. Students do not need to understand the detailed Matplotlib
syntax.

They **do** need to understand the meaning of the plotted curves:

- training loss comes from training data;
- validation loss comes from validation data;
- smaller MAE means smaller average absolute prediction error;
- the curves show how these values changed across epochs.

The pedagogical rule is simple:

> **Understand what the graph means; do not spend this lesson learning the graph-drawing library.**
