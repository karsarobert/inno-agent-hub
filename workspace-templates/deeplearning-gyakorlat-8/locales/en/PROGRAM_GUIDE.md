# Conceptual support and resuming · 1.1

## Goal

All code is supplied. Learn transfer learning by running and interpreting it. The demonstrations used food and cats/dogs; this task uses five flower categories and MobileNetV2. Explain only what the current cell needs.

| New operation | Meaning and location |
|---|---|
| def and function call | E02 already implements prepare_split. D02 calls it with four inputs and receives two objects: folder root and per-image manifest. |
| Dataset | D03 creates three iterable pipelines: training, validation, test. Actual images arrive in batches. |
| iter and next | D04 creates an iterator and requests one item: an entire images–labels batch pair. |
| shape and dtype | Image batch(16,224,224,3), float32. Labels(16,), integer int32. |
| preprocess_input | F01 demonstrates MobileNetV2 scaling from0–255 to−1..1. This is not loading the model. |
| GAP | Spatial averages per channel, producing1280 features per image. |
| Dropout | Random activation dropping during training, disabled for prediction. |
| trainable | Which weights may update? |
| training=False | How does the base run? BN uses stored statistics; selected convolution weights may still receive gradients. |
| startswith and == | T02A demonstrates name-prefix versus exact-name selection without changing trainability. |
| isinstance | Checks the BN layer type, excluded from training in T02. |
| Compile | Configuration rather than training; repeat after changing trainability, using a new optimizer. |
| Argmax, axis=1 | V00 uses a tiny array and V01 real predictions: choose the largest class-value index within each row. |
| append and concatenate | Collect label batches into a list, then join them in order. |
| Accuracy and loss | The former is correct-class fraction; the latter also considers probability assigned to the true class. |

## Splits, outputs, and test

Five classes,100/40/40 images per class,500/200/200 total. Labels are integers0–4, so use sparse categorical loss, without one-hot encoding. The final head outputs five softmax values. Row sums near1 do not prove correct predictions.

Training updates weights. Validation affects stopping and model selection. Test follows only after choices are fixed. Unshuffled test order aligns predictions and true labels. Matrix rows are true classes and columns predicted classes; the diagonal counts correct decisions.

## Claims and evidence

Two True checks concern BN and Conv_1, not automatically every layer’s weights. T02 code and layer list separately check the selection rule. Accuracy after restoring the best-val_loss checkpoint may differ from the last epoch’s accuracy. Decreasing curves do not guarantee improvement from further training. An observed image property is not a proven error cause.

## Reconnecting and resuming

In Colab, stop at E01 and change to a GPU runtime when GPU: []. Variables may be lost after runtime changes. For local Jupyter, clarify the device setup with the instructor.

Do not repeat verified conceptual learning after a kernel restart, but restore imports, helpers, and datasets. E01–E02, D02–D05, F01–F04 provide the technical foundation. A checkpoint provides weights; recreate the architecture first. F05 saves stage_head.json, T04 saves stage_fine.json, and T05 records the choice in selection.json.

If checkpoints remain, do not retrain unnecessarily: the tutor should supply complete runnable recovery code containing required definitions/paths from F05/T04 without their fit calls, then restore weights. Reconstruct validation comparisons as needed, never reselect from test results. Do not invent lost timing data.

## Closing

Discuss personal results and concise interpretations. Saving for personal use is optional. No submission, upload, sharing, file-name request, or proof of saving is required. No automatic extra exercise.
