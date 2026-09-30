# Final code-understanding quiz – 10 questions

Each question has one correct answer. Answer A, B, C or D. Inno asks one question
at a time, waits for your first answer and then explains the solution. Each
question scores 1 or 0, for a total of 10 points. Later corrections support
learning but do not change the score for the first answer. Any help requested
before answering is recorded separately in the feedback.

Assume that the libraries used in the snippets have been imported. You do not
need to run code or recall exact numbers from your training runs. This is a
conceptual self-check, not an evaluation of a network on a test set.

## Question 1 – One weight update

```python
weight = -1.0
learning_rate = 0.1
gradient = 2 * (weight - 3)
weight = weight - learning_rate * gradient
```

What is the value of weight after the update?

A. −1.8
B. −0.2
C. 0.8
D. 3.0

## Question 2 – Without momentum

```python
velocity = beta * velocity - learning_rate * gradient
position = position + velocity
```

What happens when beta = 0?

A. The program does not change the position.
B. The learning rate automatically becomes zero.
C. All previous gradients are retained with equal weight.
D. The previous velocity has no effect; we obtain a plain gradient step.

## Question 3 – ReLU output

```python
inputs = np.array([-2.0, 0.0, 3.0])
outputs = np.maximum(0, inputs)
```

What does outputs contain?

A. [0.0, 0.0, 3.0]
B. [-2.0, 0.0, 3.0]
C. [2.0, 0.0, 3.0]
D. [0.0, 0.0, 1.0]

## Question 4 – Sigmoid: output and derivative

```python
z = 0.0
value = 1 / (1 + np.exp(-z))
derivative = value * (1 - value)
```

What is the value of derivative?

A. 0.0
B. 0.5
C. 0.25
D. 1.0

## Question 5 – The regression network

```python
model = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(64, activation="relu"),
    layers.Dense(1),
])
```

Which description is correct?

A. 64 input samples, followed by one class probability.
B. One input feature per sample, 64 hidden ReLU units and one linear output.
C. One hidden layer with 1 unit and 64 output classes.
D. 64 hidden layers, followed by a sigmoid output.

## Question 6 – How many training updates?

```python
# The training set contains 64 samples.
# The dataset supplies batches of 16 samples.
# fit completes one epoch.
```

How many training batches, and therefore weight updates, occur in this epoch?

A. 1
B. 16
C. 64
D. 4

## Question 7 – L2 and total loss

```python
weights = np.array([2.0, -1.0])
l2_strength = 0.01
mae = 0.12
penalty = l2_strength * np.sum(weights ** 2)
total_loss = mae + penalty
```

What is total_loss?

A. 0.12
B. 0.05
C. 0.17
D. 0.62

## Question 8 – What should we compare?

```python
# Results measured on the same validation set:
# Model A: val_loss = 0.21, val_mae = 0.21
# Model B: val_loss = 0.27, val_mae = 0.19
# Model B's loss also includes an L2 penalty.
```

Which statement about prediction error on this validation set is correct?

A. B has lower prediction error because its validation MAE is lower.
B. A must have lower prediction error because its total loss is lower.
C. B has a classification error rate of 27%.
D. The penalty makes the two models' MAEs incomparable.

## Question 9 – A retained dropout activation

```python
input_value = 0.8
mask = 1
dropout_rate = 0.5
output_value = input_value * mask / (1 - dropout_rate)
```

What is output_value in training mode for this retained element?

A. 0.4
B. 1.6
C. 0.8
D. 0.0

## Question 10 – Dropout during evaluation

```python
training_mode = False
inputs = np.array([0.2, 0.8, 1.0])

if training_mode:
    outputs = inputs * mask / (1 - dropout_rate)
else:
    outputs = inputs.copy()
```

What happens in the run shown here?

A. The program doubles every element.
B. The program randomly zeros half the inputs.
C. The program learns new weights.
D. The output is [0.2, 0.8, 1.0], with no additional masking or scaling.
