# Closing code-comprehension test - 10 questions

Every question has one correct answer. Answer with the letter A, B, C or D.
Inno shows the questions one by one, waits for your answer, and then explains
the result. The first answer is worth 1 or 0 points per question; 10 points in
total. The test builds on creating, configuring, training and evaluating the
network. It starts after we have discussed the R1-R4 experiments, your own model
choice and the final test figures. The operations appearing in the questions are
worked through beforehand.

## Question 1 - The meaning of the input

```python
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

What does `shape=(2,)` mean here?

A. In one run exactly two samples can be processed.
B. Every input sample contains two features.
C. The model has two output classes.
D. The network contains two hidden layers.

## Question 2 - The layers of the network

```python
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(50, activation="relu"),
    layers.Dense(50, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

Which description matches this model?

A. One hidden layer with 100 neurons, then 3 outputs.
B. Three hidden layers, the last one with 3 neurons.
C. Two hidden layers, 50 neurons each, then 3 outputs.
D. Two hidden layers, 3 neurons each, then 50 outputs.

## Question 3 - Correct target-output-loss pairing

```python
train_target = keras.utils.to_categorical(train_labels, num_classes=3)
# One target vector, for example: [0, 0, 1]
```

For three mutually exclusive classes, which output and which loss match directly
the target vectors produced this way?

A. `Dense(3, activation="softmax")` and `loss="categorical_crossentropy"`.
B. `Dense(3, activation="softmax")` and `loss="sparse_categorical_crossentropy"`.
C. `Dense(1, activation="sigmoid")` and `loss="binary_crossentropy"`.
D. `Dense(2, activation="softmax")` and `loss="categorical_crossentropy"`.

## Question 4 - When does the model learn?

```python
model.compile(optimizer="adam", loss="categorical_crossentropy",
                metrics=["accuracy"])
history = model.fit(train_x, train_target, epochs=10)
result = model.evaluate(val_x, val_target)
prediction = model.predict(val_x[:5])
```

Which call performs the updating of the weights and biases during learning?

A. `compile`.
B. `evaluate`.
C. `predict`.
D. `fit`.

## Question 5 - Epoch and batch

```python
# train_x and train_target contain exactly 360 samples.
model.fit(train_x, train_target, epochs=1, batch_size=32)
```

With the default behaviour, keeping the short last batch, how many batches does
it process in this one epoch?

A. 11; the last 8 samples are left out.
B. 12; the last batch contains 8 samples.
C. 32; that is what `batch_size` prescribes.
D. 360; every sample is a batch of its own.

## Question 6 - The effect of the learning rate

```python
weight = 1.0
weight_gradient = -4.0
LEARNING_RATE = 0.1
weight = weight - LEARNING_RATE * weight_gradient
```

How much will the weight be after the single update printed?

A. 0.6
B. -0.4
C. 1.1
D. 1.4

## Question 7 - Predicted classes

```python
probabilities = np.array([
    [0.10, 0.70, 0.20],
    [0.80, 0.15, 0.05],
])
predicted = probabilities.argmax(axis=1)
```

What does `predicted` contain, if the class indices start at 0?

A. `[1, 0]`
B. `[0.70, 0.80]`
C. `[2, 1]`
D. `[1, 0, 0]`

## Question 8 - The role of validation

```python
model.fit(
    train_x, train_target,
    validation_data=(val_x, val_target),
    epochs=150,
)
```

Which statement describes correctly the role of `validation_data` in this call?

A. Together with the training data it serves direct weight updates.
B. It automatically replaces the designated training data.
C. It gives a check measurement in every epoch, without a direct weight update.
D. It automatically stops the training at the first worse result.

## Question 9 - Loss and accuracy

```python
# On one sample, the target: [0, 1, 0]
first_prediction = np.array([0.10, 0.60, 0.30])
second_prediction = np.array([0.10, 0.80, 0.10])
```

What happens on this one sample with the categorical crossentropy loss and with
the correct/wrong decision computed by argmax when we switch to the second
prediction?

A. The loss grows, the decision becomes wrong.
B. The loss decreases, the decision is correct in both cases.
C. The loss stays the same, the decision turns from wrong to correct.
D. The loss decreases, the decision is wrong in both cases.

## Question 10 - The final test

```python
model = keras.models.load_model(run_dir / "model.keras")
result = model.evaluate(test_x, test_target, verbose=0, return_dict=True)
```

We have already chosen the model on the basis of the validation. What do these
two lines do?

A. They retrain the model on the test samples with new random weights.
B. They automatically select the best run on the basis of the test accuracy.
C. They load the saved model, then measure on the test data without a weight update.
D. They continue the training from the previous last epoch.
