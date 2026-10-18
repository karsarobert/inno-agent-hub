# Concept and code guide for the tutor

Teach only what the current cell needs; do not read this file aloud.

## Data and shapes

- (N, F) means N samples with F features each. Shape alone does not explain column meaning.
- X[i] may remove the sample dimension; X[i:i+1] keeps a two-dimensional single-sample batch.
- float32 is a numeric type. Type conversion and scaling are distinct operations.
- reshape(-1, F) changes layout while preserving element count; -1 asks NumPy to infer one dimension.
- For an N×F reconstruction-error array, np.mean(..., axis=1) averages features within each row,
  producing N error values. axis=0 would instead produce one value per feature.

## Scaling and separation

MinMaxScaler learns a minimum and maximum per feature. Use fit_transform on training data;
use the same scaler’s transform on all other subsets and new inputs. New values may fall outside 0–1.
Dividing pixels by the known constant 255 differs from estimating a maximum on the complete dataset.
Training directly updates weights; validation supports selection; final test data supports final evaluation.
Calibration fixes the anomaly threshold independently of both stopping data and final test data.

## The three models

| Task | Input | Target | Output | Loss |
|---|---|---|---|---|
| Housing | 13 features | One real number | One linear value | MAE |
| MNIST | 784 pixels | Ten-position one-hot vector | Ten softmax values | categorical_crossentropy |
| Autoencoder | Five numbers | The same five numbers | Five sigmoid values | MSE |

compile configures; fit trains; evaluate measures against targets; predict produces outputs without
needing targets. Softmax output becomes an index through argmax. Autoencoder outputs are reconstructed
features, not fraud probabilities; a later error threshold creates the binary decision.

## Training

A batch is the group used for one update; an epoch traverses the training set. The epoch budget is a maximum.
EarlyStopping monitors val_loss. Patience counts consecutive epochs without sufficient improvement.
restore_best_weights restores the selected state. With min_delta, this need not be exactly the epoch
having the smallest raw logged value. A second fit continues existing weights; rebuild for a fresh experiment.
Dropout is active during training and inactive during prediction/evaluation. Relative curve heights alone
do not prove leakage or overfitting: interpret actual trends and context.

## Metrics

MAE averages absolute errors in target units; it is not a percentage or every sample’s individual error.
Accuracy counts correct class decisions. Cross-entropy also reflects the value assigned to the correct class.
For labels=[0,1], the binary confusion matrix is [[TN,FP],[FN,TP]]. Positive class 1 is the anomaly.
Precision=TP/(TP+FP): the fraction of alerts that are real anomalies.
Recall=TP/(TP+FN): the fraction of real anomalies that were found.
zero_division=0 is a convention for undefined ratios, not proof of model quality.
With only ten test anomalies, avoid strong generalization claims.

## Explaining plots

Identify axes and curves first, then request one specific observation. For a confusion matrix, ask for
true label, predicted label and count. For histograms, discuss overlap and the fixed threshold.
For unseen plots, use the student’s actual description. Reloading a browser page does not recompute results.
