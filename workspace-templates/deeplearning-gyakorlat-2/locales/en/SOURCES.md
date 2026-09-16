# Sources and adaptation decisions

The focused version is derived from the previously prepared Exercise 2 package
and its wine-quality regression example.

The pedagogical scope has been deliberately narrowed. Classification and the
separate NumPy neural-network demonstration were removed so more class time can
be spent on the data path, preprocessing, network construction, `compile()` and
`fit()`.

Technical API background:

- TensorFlow/Keras model construction and training APIs;
- Keras `Dense` layers and `Sequential` models;
- scikit-learn `train_test_split`;
- scikit-learn `MinMaxScaler`;
- pandas CSV/DataFrame operations;
- Matplotlib only for support visualizations.

The detailed origin and licence of the included wine dataset are described in
`data/SOURCE.md`.
