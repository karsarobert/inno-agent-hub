# Technical recovery — supplied code

Retain credit for demonstrated understanding. The tutor supplies one current complete cell at a time. The following sequence is tutor/instructor support rather than a request to run everything at once.

## Lost variables during CAM

Restore E01→C01→C02. C03 fixes target classes; C04 builds the probe; C05 defines CAM/plot helpers. C06/C07 can then be repeated. The classifier does not train; established understanding need not be repeated.

## Download failure

The instructor can pre-place the exact labels.csv and final_files.zip in dl10_data. Their hashes are in A01. They come from the Drive IDs in the supplied PTE_DL10_AGE_PRED demonstration. Do not bypass hashes or silently substitute synthetic data. C01 likewise accepts the already bundled sample files in assets.

## Kernel lost; local results remain

Restore E01, C01, C02, C03, C04, C05, A01, A02, A03, A04, A05, B02, F01, F02, M01 one cell at a time. Rechecking data/cache identity verifies the same samples; call a cache hit what it is. M01 rebuilds the small head from scratch. Then use R01 below to restore completed training without fit. R01 also rebuilds the evaluation stream from validation vectors.

```python
from types import SimpleNamespace
head_path = work / "age_head_best.weights.h5"
required = [head_path, work / "head_history.json", work / "selection.json"]
if not all(path.exists() for path in required):
    raise RuntimeError("Completed training files are missing. Restart head training at M01.")
head_val_data = tf.data.Dataset.from_tensor_slices((val_features, val_ages)).batch(BATCH).with_options(options)
age_head.load_weights(head_path)
history = SimpleNamespace(history=json.loads((work / "head_history.json").read_text()))
selection = json.loads((work / "selection.json").read_text())
cam_results_path = work / "cam_results.json"
cam_results = json.loads(cam_results_path.read_text()) if cam_results_path.exists() else {"status": "CAM execution not recovered"}
print("Restored completed head and the saved pre-test selection:", selection)
```

M03 can re-evaluate the selected checkpoint, but no different state may be selected from test outcomes. If test results were already discussed, quote existing results.json/test_errors.csv. When variables are needed, rerun V01→V02 with the unchanged head for technical recovery, not a new experiment or test tuning. V03 restores examples and X01 the regression map. The sequence above also restores C04/C05 helpers needed for X01.

For a new head-training run, with state through F02 and a valid cache, run M01→M02→M03. A partially interrupted M02 is not exactly resumable from best weights alone: use a fresh head, optimizer and history while retaining conceptual credit.

Optional instructor cache files can be placed in dl10_results/feature_cache. They require matching image order/hashes, backbone weights, preprocessing and TensorFlow version; otherwise extraction runs again. Never force a match by renaming cache files or changing a signature.

Supply R01 code unchanged, not as an incomplete task. No final files are requested.
