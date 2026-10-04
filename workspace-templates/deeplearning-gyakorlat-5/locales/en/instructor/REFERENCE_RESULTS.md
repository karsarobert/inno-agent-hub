# Measured reference results and interpretation

These results were measured on CPU while preparing the English package. Do not reveal them before the student runs the program: evaluate their own results and observations. Fixed-reference counts can be checked; the last digits of newly trained models may vary across environments.

## Training

| Epochs | Bottleneck | Training MAE with final weights | Normal validation MAE | Normal practice example 0 MAE | Total run |
|---:|---:|---:|---:|---:|---:|
| 10 | 8 | 0.033397 | 0.030211 | 0.019023 | 7.24 s |
| 30 | 8 | 0.025963 | 0.023619 | 0.016702 | 9.24 s |
| 30 | 16 | 0.026187 | 0.023750 | 0.017864 | 9.46 s |

The 10- and 30-epoch runs with bottleneck 8 have the same initial-weights identifier. Longer training improved normal reconstruction in this run. Bottleneck 16 did not improve validation MAE here: this is a valid finding, not a failed exercise. A different architecture also changes the weight matrices and their identifiers.

## Individual reference MAEs

| Index | Normal | Anomalous |
|---:|---:|---:|
| 0 | 0.016702 | 0.071006 |
| 3 | 0.010389 | 0.067872 |

The selected anomalous examples have larger errors. The full distributions nevertheless overlap: not every normal error is smaller than every anomalous error. The histogram is identical for both selected indices.

## Threshold: positive = anomalous

| Threshold | TP | FN | FP | TN | Precision | Recall |
|---:|---:|---:|---:|---:|---:|---:|
| 0.025 | 128 | 0 | 49 | 79 | 72.3% | 100.0% |
| 0.040 | 128 | 0 | 11 | 117 | 92.1% | 100.0% |
| 0.060 | 121 | 7 | 6 | 122 | 95.3% | 94.5% |

- 0.04 → 0.025: TP cannot increase here because the baseline already detected all 128 anomalies. FP rises from 11 to 49. The lower threshold produces more false alarms with unchanged recall.
- 0.04 → 0.06: FP falls from 11 to 6, while FN rises from 0 to 7. Fewer false alarms come at the cost of seven missed anomalies.
- At 0.06, precision = 121/(121+6) ≈ 95.3%; recall = 121/(121+7) ≈ 94.5%.
- Threshold 0: all signals trigger alerts, TP=128, FP=128, precision=50%, recall=100%.
- Threshold 1: no alerts here, TP=0, FP=0, recall=0%, precision undefined. The program avoids division by zero.

The 100% recall at 0.04 is a result for this small practice subset and fixed model, not a general performance promise or a clinical sensitivity estimate. We explore thresholds on this set; final evaluation would need separate untouched data representative of the intended use.
