# Deep Learning – Exercise 2: from data to a trained neural network

This focused version deliberately contains **less material, explained more deeply**.
Classification, the separate NumPy neural-network example, dropout, batch
normalization and early stopping are not part of this exercise.

The whole class follows one question:

> **How does a table of data become a trained neural network?**

We use the same wine-quality regression task throughout the lesson so students
can follow the same data from the CSV file all the way to `model.fit()`.

## The three programs

1. `G02_01_data_preparation.py` – CSV → DataFrame → X/y → split → scaling.
2. `G02_02_model_and_compile.py` – 11 → 32 → 16 → 1 network and `compile()`.
3. `G02_03_fit_and_evaluate.py` – `fit()`, epochs, batches, validation and learning history.

Open `visualizer.html` during class. It mirrors the same sequence visually.

## Learning priorities

Students should be able to explain the **meaning and data flow** of the central
lines of code. They are not expected to understand every library detail. For
example, the plotting block that creates the learning-curve image is useful
support code, but understanding Matplotlib syntax is not a learning objective of
this lesson.

See `PROGRAM_WALKTHROUGHS.md` for detailed code explanations and
`LESSON_INSTRUCTIONS.md` for the 2 × 45 minute teaching flow.
