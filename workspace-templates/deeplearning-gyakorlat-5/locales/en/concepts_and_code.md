# Quick revision — autoencoders and ECG

| Concept / code | Meaning here |
|---|---|
| One signal | 140 scaled values with their temporal order preserved. |
| `sample_index` | Zero-based index of the displayed example. |
| Encoder | Network section that converts 140 input values into a smaller internal representation. |
| Bottleneck | A limited internal representation; eight values in the baseline model. |
| Decoder | Produces 140 reconstructed values from the internal representation. |
| `Dense` | Fully connected layer: every neuron uses all outputs of the previous layer. |
| ReLU | Replaces a negative pre-activation with zero; a positive value passes through. |
| Output sigmoid | Produces a 0–1 amplitude at each sample point, not class probabilities. |
| Input = target | We train reconstruction, so we want the same signal back. |
| `compile` | Configures the optimiser and loss. |
| `fit` | Updates model weights based on the loss. |
| Epoch | One pass through the complete training set. |
| Batch | A group of samples used for one update; 32 signals here. |
| Validation | Evaluation on separate data without weight updates. |
| MAE | Mean absolute difference between original and reconstructed values. |
| `axis=1` | Average across sample points, obtaining a separate error for each signal. |
| `error >= threshold` | An alert: a signal predicted to be anomalous. Equality also triggers an alert. |
| TP | Actually anomalous and an alert was raised. |
| FN | Actually anomalous but no alert was raised. |
| FP | Actually normal but an alert was raised: a false alarm. |
| TN | Actually normal and no alert was raised. |
| Precision | TP/(TP+FP): actual anomalies among alerts. |
| Recall | TP/(TP+FN): detected anomalies among all actual anomalies. |

## Three important distinctions

**Error and decision:** Reconstruction error is a continuous number. A threshold
turns it into a decision. Moving the boundary does not retrain or improve the network.

**Your own run and the reference:** G02 trains in your own run. G03 and G04 inspect
outputs of the supplied 30-epoch model. The program states their origin at startup.

**Good reconstruction and good anomaly detection:** If a model reconstructs
anomalous signals very well too, low error alone does not help separate the
groups. Their error distributions and mistaken decisions also matter.

## Two rows, two individual errors

| Signal | Illustrative absolute differences | Individual mean |
|---|---|---|
| 1 | 0.1, 0.1, 0.3, 0.3 | 0.2 |
| 2 | 0.4, 0.4, 0.4, 0.4 | 0.4 |

`axis=1` → [0.2, 0.4], two separate errors. Without `axis` → 0.3, one overall mean.
The same principle gives 128 separate MAEs for the 128 real signals.

## Same correct detections, different starting groups

For the reference run at threshold 0.06:

- Precision: **127 alerts** = 121 correct + 6 false. 121/127 ≈ 95.3%.
- Recall: **128 actual anomalies** = 121 detected + 7 missed. 121/128 ≈ 94.5%.

Always name the starting group first. Both numerators are 121. With no alerts,
precision is undefined because its denominator is zero.
