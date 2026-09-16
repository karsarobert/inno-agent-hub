# Core concepts and the code that represents them

This is a compact reference for the lesson.

## 1. One row = one sample

The wine CSV is a table. Each row represents one wine. Eleven measured columns
are inputs and `quality` is the target.

## 2. Inputs and target

```python
features = data.drop(columns=["quality"])
target = data["quality"]
```

**X / features:** information given to the model.  
**y / target:** correct answer the model tries to predict.

## 3. Three data roles

- **Training:** updates weights.
- **Validation:** checks the model during development.
- **Test:** kept untouched for final evaluation.

## 4. Scaling

```python
scaler.fit_transform(train_features)
scaler.transform(validation_features)
scaler.transform(test_features)
```

Fit preprocessing on training data only. Apply the learned rule to the other
sets. This avoids data leakage.

## 5. Architecture

```text
11 inputs → 32 hidden neurons → 16 hidden neurons → 1 output
```

```python
model = keras.Sequential([
    keras.Input(shape=(11,)),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),
])
```

## 6. Compile

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.003),
    loss="mae",
    metrics=["mae"],
)
```

`compile()` configures training. It does **not** train the network.

- optimizer: how weights are updated;
- loss: error training tries to reduce;
- metric: value reported for interpretation.

## 7. Fit

```python
history = model.fit(
    train_scaled,
    train_target,
    validation_data=(validation_scaled, validation_target),
    epochs=40,
    batch_size=64,
)
```

- epoch: one pass through the whole training set;
- batch: a smaller group processed before a weight-update step;
- validation data: separate data used to check the current model;
- history: record of training and validation values over epochs.

## 8. Support code

The plotting code, result-folder creation and formatting code are useful, but
not every line must be understood in this lesson. The focus is the neural-network
pipeline, not Matplotlib or file-management syntax.
