# Verification checklist

The focused package should satisfy all of these conditions:

- [x] No classification exercise is present.
- [x] No separate NumPy neural-network exercise is present.
- [x] Exactly three main lesson programs are used.
- [x] The wine dataset is included locally.
- [x] G02_01 explains data path, X/y, split and scaling.
- [x] G02_02 explains architecture and `compile()` without training.
- [x] G02_03 explains `fit()`, epoch, batch, validation and History.
- [x] Plotting is labelled support code rather than a learning target.
- [x] The tutor script fits 2 × 45 minutes.
- [x] Internal file references use the new filenames.
- [x] Python files pass syntax checking.

## Build-environment note

`G02_01_data_preparation.py` was executed successfully during package creation.
The build container did not have TensorFlow installed, so G02_02 and G02_03 were
syntax-checked but not runtime-executed there. The package includes the pinned
TensorFlow dependency in `requirements.txt` and `environment_check.py` for the
prepared classroom environment.
