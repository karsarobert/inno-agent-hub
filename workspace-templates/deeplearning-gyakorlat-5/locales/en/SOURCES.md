# Sources and deliberate simplifications

## User-provided materials

- PTE_DL5_ECG.ipynb: the basis for the Dense autoencoder and ECG reconstruction task.
- DL_05.html: theory material beginning with autoencoders; not a runtime dependency.
- Earlier DL04 Innoagent material: tutoring sequence, figure saving, CPU batching
  and closing quiz format.
- DL_05_innoagent_HU.zip, version 1.1: source for this complete English edition,
  including the latest code explanations, refresh reminders and illustrations.

## Data source

The binary-labelled CSV prepared for the TensorFlow tutorial from the ECG5000 data family:
https://storage.googleapis.com/download.tensorflow.org/data/ecg.csv

Description and related tutorial:
https://www.tensorflow.org/tutorials/generative/autoencoder

Original dataset collection:
https://www.timeseriesclassification.com/description.php?Dataset=ECG5000

The CSV downloaded when the Hungarian package was prepared had 4,998 rows and
141 columns, despite the ECG5000 family name. The first 140 values are the
signal, followed by a label: 1=normal, 0=anomalous. The source CSV checksum and
selection metadata are in `data/data_metadata.json`. The raw CSV is not included;
the package contains only 896 selected, scaled signals and their source-row indices.

Selection used NumPy `default_rng(2026)` and separate permutations of normal and
anomalous row indices. Normal: first 512 for training, next 128 for validation,
next 128 for observation. Anomalous: first 128 for observation. The source rows
are disjoint. This does not establish patient-level clinical validation;
we do not infer a patient-level split from this CSV.

Scaling uses the shared minimum and maximum across the 512 normal training
signals. The same linear transformation applies to every subset. Values are
float32 without clipping. New values may fall outside 0–1, although the model's
sigmoid outputs remain within that interval.

## Differences from the full notebook

A smaller local dataset, shorter CPU training, separate normal validation and
ready-made figure saving keep the lesson accessible. The architecture remains
140–32–16–8–16–32–140, with hidden ReLU and he_normal, sigmoid output, Adam
(default learning rate 0.001) and MAE. A helper creates batches of 32 using one
background thread. Input=target training is unchanged.

The threshold is manually adjustable to make decision trade-offs visible.
It is not automatically set to mean plus two standard deviations. Reference
reconstructions come from a real 30-epoch run, not artificially designed errors.
G03/G04 can run independently, but always use this supplied reference.

The English edition renames data keys and file paths. Every numeric data array
and reference reconstruction is unchanged from the Hungarian edition. NPZ file
checksums therefore differ, and the English metadata records the new checksums.
The original reference run identifier is retained as historical provenance.
The small two-row axis illustration is explicitly artificial and separate from ECG data.

## Documentation and attribution

- Keras training API: https://keras.io/api/models/model_training_apis/
- TensorFlow datasets: https://www.tensorflow.org/api_docs/python/tf/data/Dataset
- NumPy mean: https://numpy.org/doc/stable/reference/generated/numpy.mean.html

The links above preserve data attribution. We do not claim authorship of the
ECG data or assign it a new licence different from its source. TensorFlow tutorial
code refers to Apache License 2.0; the related licence text is supplied in
`instructor/APACHE-2.0.txt`. These programs are adaptations for this lesson,
translated into English; the changes and parameters are documented above.
