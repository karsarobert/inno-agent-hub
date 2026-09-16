# Origin of red-wine.csv

The included file comes from the course's public repository:
[DeepLearning2026 – red-wine.csv](https://raw.githubusercontent.com/karsarobert/DeepLearning2026/main/red-wine.csv).
Downloaded: 13 September 2026. The included CSV file has not been modified.

Original data source: **Cortez, P., Cerdeira, A., Almeida, F., Matos, T.,
& Reis, J. (2009). Wine Quality. UCI Machine Learning Repository.**
DOI: [10.24432/C56S3T](https://doi.org/10.24432/C56S3T).

[UCI dataset page](https://archive.ics.uci.edu/dataset/186/wine+quality).
Dataset licence: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
The data comes from Portuguese red- and white-wine analyses; this file contains
**1599 red-wine observations**. We use the 11 physicochemical features to predict
the `quality` score.

## Preparation used in the examples

- The original file contains 1599 rows and 12 columns, with no missing values.
- The programs remove 240 duplicate full rows, leaving 1359 distinct rows.
- With the selected random seed, the split produces 815 training, 272 validation,
  and 272 test samples.
- Keeping identical rows only once is a teaching decision so that the same full
  observation does not appear in multiple sets. This does not mean that every
  duplicate row in every real-world data task is necessarily an error.
- Scaler parameters are calculated only from the training set.

File size: 100951 bytes. SHA-256:

```text
d6a0d9bd24806944818795f22500c46cb6424cbff517aacda36595d3ed9b2daa
```
