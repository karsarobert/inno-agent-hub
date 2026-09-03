# Homework — Deep Learning 1 practice, session 1 (differentiated)

Topic: **the history of neural networks, fundamentals of machine learning** +
a simple MNIST demo.
(Overfitting and curve analysis are covered **later** in the syllabus — that is
why they do not appear here yet.)

Pick the part that fits your level. The **base** part is mandatory for
everyone; **advanced** and **extension** are for faster learners.

---

## Base (everyone) — mandatory

1. After running `feladatok/zaro_feladat.py`, **write down the final test
   accuracy** (`val_accuracy`) and the parameter count from `model.summary()`.
2. **Explain in 3-4 sentences:** what does "training" mean in the demo (what
   happens during `fit`)?
3. Pick **2 historical milestones** from the session 1 material (e.g.
   perceptron, MLP) and summarise in **1-1 sentence** why they matter for
   today's models.

---

## Advanced (on top of the base)

4. Take any digit from MNIST (e.g. `X_train[i]`): what **shape** did it end up
   in, how many dimensions does it have, and what is its **largest value**
   after normalization?
5. Look at the one-hot vector of `Y_train[0]`, and explain **why this form is
   suitable** as the output of classification.
6. **(Spaced repetition)** recall from NumPy the role of `astype` and
   `reshape` — prove with 1 short one-liner example each what both do.

---

## Extension (independent research)

7. Look up briefly **what the limitation of the perceptron was** (the XOR
   problem) and why this made the multi-layer (MLP) network necessary.
8. Try a **2-hidden-layer** variant of the demo (e.g. `Dense(128, relu)` →
   `Dense(128, relu)` → `Dense(10, softmax)`), and track how the parameter
   count of `model.summary()` changes.
9. Look at the output of **`!nvidia-smi` / `tf.config.list_physical_devices('GPU')`**
   and describe: is there a GPU, and why is it useful in deep learning?

---

## Submission / next session

- Bring the result of running the demo (final accuracy + parameter count).
- Next topic: **the perceptron model and deep/feed-forward neural networks**.
- At every level the submitted solution contains the **measurable data**
  (accuracy, shape, max value), not only the code.
