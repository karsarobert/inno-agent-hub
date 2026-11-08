# Kernel and run recovery

This is ready-to-use tutor support, not an extra exam. Present one active cell at a time and retain credit for demonstrated understanding.

## Small probes

Rerun E01 after restart. B03/B04 need B02; B05 is independent after E01; B06 needs B02 and B04. P/C/R/G probes are independent after E01. Copy complete cells from the lesson, rather than asking the student to reconstruct code. Do not repeat B01/R00 understanding just because a kernel restarted.

## Restart the complete controlled comparison

If data/state files are gone or the current fit was interrupted, restart E01,D01,D02,D03,M01,M02,M03,M04,M05, one cell at a time. M01/M02 start a fresh comparison and overwrite initial-weight files; do not use M02 for partial recovery. The old best files are refreshed during the full new 6-epoch runs; new histories describe the new runs. Do not tune on the test set.

## First run complete; second run not yet started

Use only if local `dl9_results` files exist AND M03 completion was verified. Run E01,D01,D02,D03,M01 one cell at a time. Do NOT run M02: it would overwrite the original saved initial states. Then supply RC01 below and continue with M04. It restores the original two initial states and the completed baseline checkpoint/history. It does not resume an interrupted M04.

```python
from types import SimpleNamespace
baseline_path = work / "without_bn_best.weights.h5"
bn_path = work / "with_bn_best.weights.h5"
required = [work / "without_bn_initial.weights.h5", work / "with_bn_initial.weights.h5",
            baseline_path, work / "baseline_history.json"]
if not all(path.exists() for path in required):
    raise RuntimeError("Required local files are missing. Restart the controlled comparison at M01.")
baseline.load_weights(work / "without_bn_initial.weights.h5")
bn_model.load_weights(work / "with_bn_initial.weights.h5")
for model in [baseline, bn_model]:
    model.compile(optimizer=keras.optimizers.Adam(1e-3),
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
baseline.load_weights(baseline_path)
baseline_history = SimpleNamespace(history=json.loads((work / "baseline_history.json").read_text()))
print("Baseline completed; BN model restored to the saved common initial state.")
```

## Both training runs complete

After E01,D01,D02,D03,M01 and RC01, use RC02 below. Continue with M05 if selection has not happened. If selection.json exists, RC02 preserves the PRE-test choice: do not reselect using later test results. Continue with any unfinished V01,V02,Z01,Z02 checkpoints. If testing was already discussed, quote existing results.json; evaluating unchanged weights again for technical recovery is not a new experiment or tuning. Rerunning V02 restores the matrix without re-examining established understanding.

```python
required = [bn_path, work / "bn_history.json"]
if not all(path.exists() for path in required):
    raise RuntimeError("The second training run is not documented as complete. Do not claim an exact mid-fit resume.")
bn_model.load_weights(bn_path)
bn_history = SimpleNamespace(history=json.loads((work / "bn_history.json").read_text()))
selection_path = work / "selection.json"
if selection_path.exists():
    stored_selection = json.loads(selection_path.read_text())
    validation_results = stored_selection["validation"]
    selected_name = stored_selection["selected"]
    selected_model = bn_model if selected_name == "with_bn" else baseline
    print("Saved pre-test selection preserved:", selected_name)
else:
    print("Both models restored. Run M05 before any test.")
```
