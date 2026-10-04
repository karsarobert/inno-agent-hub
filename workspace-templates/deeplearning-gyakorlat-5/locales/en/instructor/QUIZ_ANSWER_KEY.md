# Answer key for the ten-question closing quiz

| Question | Answer | Explanation after the student's answer |
|---|---|---|
| 1 | B | The desired reconstruction is the input signal itself. Anomaly decisions are made later by comparing error with a threshold. |
| 2 | D | One preprocessed signal segment contains 140 successive values. |
| 3 | A | We create input-target pairs. They are identical because the model learns reconstruction. |
| 4 | C | The encoder compresses information used for reconstruction into eight internal values. This does not guarantee lossless coding. |
| 5 | B | These are signal amplitudes, not class probabilities; they need not sum to one. |
| 6 | D | Each row is one signal. Averaging over the sample-point axis gives each signal its own MAE. |
| 7 | C | The programs read saved outputs of a real pretrained model. These do not follow the student's G02 changes. |
| 8 | A | Positive means anomalous. For FP, the prediction is positive but the actual signal is normal. |
| 9 | B | Recall = TP/(TP+FN). Option A describes precision. |
| 10 | D | A threshold is a decision rule. Signals, reconstructions, errors and actual labels stay unchanged. |

Key: B, D, A, C, B, D, C, A, B, D.
Score the first answer 1 or 0, up to 10 points. Record prior assistance separately.
A later correction supports learning; it does not rewrite the first-attempt score.
The key is readable in the package: this is guided learning, not a secure examination system.
