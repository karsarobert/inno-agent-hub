# DL 1 — Key concepts at a glance (1 page)

## The neural network in a picture

```
Input (data)               Layer                Output (class)
┌──────────────┐  weights →  ┌──────────────┐  →  ┌──────────────┐
│ 28×28 image  │    w, b     │ Dense(10)    │     │ 0,1,2,…,9    │
│ = 784 vector │  ──────►    │ softmax      │ ──► │ (probability)│
└──────────────┘             └──────────────┘     └──────────────┘
```

## The short history arc

- **1958 — Perceptron** (Rosenblatt): the first simple unit that learns with weights.
- **MLP (multi-layer network)**: several layers combined → more complex tasks.
- **The deep-learning revival**: many hidden layers, large computing capacity.
- **Today**: processing images, text and sound — this is what the rest of the course builds on.

## The core concepts

| Concept | What it means, on the MNIST example |
|---|---|
| **Data** | the set of examples (60 000 training + 10 000 test images) |
| **Feature** | what the model learns from (the 784 pixel values as a vector) |
| **Supervision** | we know the correct label (the digit 0-9) during training |
| **Model** | the layers and weights together (the `Sequential` net) |
| **Training** | adjusting the weights from the error during `fit` |
| **Classification** | the model's output: the class of the 10 digits |

## The data-preparation steps (in the code)

```
load → reshape(60000,784) → astype(float32) → /255 → to_categorical
```

| Step | Code | Why? |
|---|---|---|
| Load | `mnist.load_data()` | 60 000 training + 10 000 test images (28×28) |
| Reshape | `reshape(60000, 784)` | the Dense layer expects a **vector**, not a 2D image |
| Type change | `astype('float32')` | continuous numbers, better computation |
| Normalize | `X /= 255` | values into 0.0–1.0; more stable training |
| One-hot | `to_categorical(Y, 10)` | the label becomes a vector for classification |

## Key concepts

- **Epoch**: how many times the model goes through the **whole** dataset.
- **Batch**: how many samples in one "step" before the weights are updated (e.g. 128).
- **Softmax**: the activation of the output layer → 10 probabilities, sum 1.
- **Loss**: how badly the model is guessing; training decreases it.
- **Adam**: an optimizer that adjusts the weights based on the loss.

> **Overfitting** (and the detailed analysis of learning curves) is covered by
> later topics of the syllabus — in session 1 we only see the main steps.

*Cheat sheet for the Deep Learning 1 lab — to be used next to `dl1_megoldott.py`.*
