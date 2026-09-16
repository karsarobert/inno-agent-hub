# Deep Learning 2026 – Exercise 2 tutor script

## Central teaching goal

The class should answer one question clearly:

> **How does a table of data become a trained neural network?**

Use one continuous example: wine-quality regression. Do not introduce a second
classification problem or a separate NumPy network. Depth is more important than
number of topics.

## 2 × 45 minute lesson flow

| Block | Topic | Time |
|---|---|---:|
| 1 | Big picture: the complete data path | 5 min |
| 1 | G02_01: rows, columns, X and y | 12 min |
| 1 | G02_01: train/validation/test split | 13 min |
| 1 | G02_01: scaling and data leakage | 15 min |
| 2 | G02_02: network architecture | 15 min |
| 2 | G02_02: `compile()` | 10 min |
| 2 | G02_03: `fit()`, epoch, batch, validation | 12 min |
| 2 | History, learning curve, interpretation | 5 min |
| 2 | Final pipeline recap | 3 min |

Total: 90 minutes.

## Teaching method

Before showing code, explain **what problem the next block solves**. Then show a
small block of code, connect each important argument to the visualizer, and only
then ask the student to interpret it.

Use this pattern repeatedly:

**What are we trying to do? → Which data goes in? → Which lines do it? → What
comes out? → Why does the next step need that result?**

Do not ask students to explain an API call that has not yet been introduced.
Avoid large manual calculations. The goal is conceptual understanding of data
flow and model training.

## Two levels of code

Explicitly distinguish:

### Core code – understand this now

Examples:

```python
features = data.drop(columns=["quality"])
target = data["quality"]
```

```python
model = keras.Sequential([...])
```

```python
model.compile(...)
```

```python
history = model.fit(...)
```

Students should understand what these blocks mean at a practical level.

### Support code – useful, but not today's learning objective

Examples include detailed Matplotlib plotting, timestamped result folders and
some formatting/printing code. Say this explicitly:

> “This block draws or saves the result. You do not need to understand every
> line of it today. Our focus is what the neural network is doing and what the
> graph tells us.”

Never let support code become the main difficulty of the exercise.

# First 45 minutes – the path of the data

## Introduction – 5 minutes

Open `visualizer.html` on the first page. Show the complete path:

**CSV → table → X/y → split → scaling → neural network → compile → fit → history**

Explain that only the first half of this chain will be studied in the first
45-minute block. The neural network cannot learn from a CSV file directly; the
data must first be prepared into a suitable numerical form.

## G02_01 – data preparation – 40 minutes

Run:

```bash
python G02_01_data_preparation.py
```

### 1. Rows and columns

Explain that one row is one wine sample. Eleven measured properties are possible
inputs. `quality` is the target: the known answer during training.

Show:

```python
raw_data = pd.read_csv(DATA_FILE)
```

Students do not need a full pandas lesson. They should understand only that
`read_csv` turns the file into a table in memory.

### 2. X and y

Spend time here. Show visually that `quality` moves out of the input table:

```python
features = data.drop(columns=["quality"])
target = data["quality"]
```

Ask: “Would it be valid to leave `quality` inside the input features?” Expected
idea: no, because then the model would receive the answer it is supposed to
predict.

### 3. Split

Use the visualizer to show approximately 60% training, 20% validation, 20% test.
Explain the roles using plain language:

- training: changes the weights;
- validation: checks the model during development;
- test: kept untouched until the final evaluation.

Do not teach statistical sampling theory here. The important concept is that the
three sets have different jobs.

### 4. Scaling

Show a real row before and after scaling. Explain that the columns use different
units and ranges, so scaling puts them on a more comparable numerical scale.

Emphasize this line:

```python
train_scaled = scaler.fit_transform(train_features)
```

and contrast it with:

```python
validation_scaled = scaler.transform(validation_features)
```

`fit` means the scaler **learns** the training-column ranges. `transform` means
it applies the already learned rule. The validation/test sets must not teach the
scaler anything. Introduce “data leakage” only at this intuitive level.

End the first block by reconstructing the path from the CSV to `train_scaled`.

# Second 45 minutes – from prepared data to learning

## G02_02 – architecture – 15 minutes

Run:

```bash
python G02_02_model_and_compile.py
```

Connect `train_scaled.shape[1]` to the 11 input values in one row. Then map each
code line to the network drawing:

```python
model = keras.Sequential([
    keras.Input(shape=(train_scaled.shape[1],)),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),
])
```

Translate it into ordinary language:

**11 input values → 32 hidden neurons → 16 hidden neurons → 1 predicted number.**

Explain `Dense` as “every neuron receives information from all outputs of the
previous layer”. Explain ReLU only as an activation that introduces non-linearity;
do not derive it mathematically in this class.

## G02_02 – compile – 10 minutes

Treat `compile()` as a separate conceptual step:

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=["mae"],
)
```

Use three questions:

- **loss:** What error are we trying to make smaller?
- **optimizer:** How will the program update the weights?
- **metric:** What useful value should we report?

The most important sentence: **`compile()` does not train the network.** It
configures how training will work.

## G02_03 – fit – 12 minutes

Run:

```bash
python G02_03_fit_and_evaluate.py
```

Before starting, explain every important `fit()` argument:

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

Use the visualizer for epochs and batches. One epoch means one complete pass
through the training dataset. A batch is a smaller group processed before a
weight-update step.

Make clear that validation data is observed for evaluation but does not drive
the ordinary gradient updates.

## History and plot – 5 minutes

Explain that `fit()` returns `history`, which is a record of what happened during
training. The graph is simply a visual version of some of these recorded values.

Say explicitly that the plotting syntax is support code. Students should read the
graph, not memorize Matplotlib.

Ask only interpretive questions: Did loss generally decrease? Are training and
validation curves telling roughly the same story? Do not turn this into an
advanced overfitting lesson yet.

## Final recap – 3 minutes

Have the student say the full chain in their own words:

**CSV → X/y → split → scaling → network architecture → compile → fit → validation → history.**

If they can explain why each arrow exists, the lesson has achieved its goal.
