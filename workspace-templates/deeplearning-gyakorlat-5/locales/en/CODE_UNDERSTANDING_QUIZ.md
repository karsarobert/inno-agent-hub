# Fixed closing quiz — 10 questions

The agent asks one question at a time. Each has one correct answer. Score the
first unambiguous answer, then explain using the answer key. These assess concepts
and code understanding; they are not predictions requested before running the examples.

## 1. What is the training objective of the autoencoder?

A. Output a normal/anomalous label for every input.
B. Reconstruct the input signal at its output.
C. Turn every input into zeros.
D. Randomly reorder the 140 sample points.

## 2. What does 140 mean in the ECG example?

A. The number of training epochs.
B. The number of diseases to recognise.
C. The percentage of normal signals.
D. The number of input values in one signal segment.

## 3. Why does the same set of signals appear twice?

```python
training_batches = make_batches(training_signals, training_signals, shuffle=True)
```

A. The first supplies inputs; the second supplies desired outputs.
B. We accidentally downloaded the same file twice.
C. This gives the model twice as many classes.
D. One contains normal labels and the other anomalous labels.

## 4. What is the role of the eight-value bottleneck?

A. Name eight predefined diseases.
B. Select the eight largest original sample points.
C. Pass on a learned internal representation of limited size.
D. Guarantee perfect, lossless reconstruction.

## 5. What do the 140 sigmoid output values represent?

A. Probabilities for 140 classes that sum to one.
B. Reconstructed signal amplitudes between 0 and 1.
C. Row numbers of the training signals.
D. Learning rates used by Adam.

## 6. What does axis=1 do in this calculation?

```python
errors = np.mean(np.abs(signals - reconstructed_signals), axis=1)
```

A. Select the first signal and discard the rest.
B. Average every point of every signal into one overall error.
C. Use only differences with a positive sign.
D. Average the absolute differences across sample points separately for each signal.

## 7. Which statement is true of G05_03 and G05_04?

A. They train a new autoencoder every time they run.
B. They automatically use the student's latest G05_02 model.
C. They use fixed reference reconstructions supplied with the package.
D. They call random numbers reconstructions.

## 8. What is a false alarm in this lesson?

A. A genuinely normal signal is flagged as anomalous.
B. A genuinely anomalous signal is correctly flagged.
C. The training loss decreases.
D. A normal signal is classified as normal.

## 9. What does anomaly recall mean?

A. The proportion of alerts that are genuine anomalies.
B. The proportion of actual anomalies that are detected.
C. The proportion of sample points reconstructed perfectly.
D. The number of normal training signals.

## 10. What changes in G05_04 when we change only the threshold?

A. The learned weights automatically retrain.
B. Every reconstructed signal changes.
C. The actual labels adapt to the threshold.
D. Decisions based on the fixed error values may change.
