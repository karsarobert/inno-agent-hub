# Changes in the focused version

This revision intentionally reduces scope and increases explanation depth.

Removed:

- the separate NumPy forward-pass / hand-built network sequence;
- the classification example;
- early stopping as a separate lesson topic;
- extra architecture experiments that competed for class time.

Expanded:

- the complete path of data from CSV to network input;
- X versus y;
- training, validation and test roles;
- scaling and the reason for fitting preprocessing on training data only;
- interpreting shapes;
- mapping Keras layer code to the network diagram;
- `compile()` as a separate conceptual step;
- every important argument of `fit()`;
- epoch versus batch;
- the meaning of `History`, training loss and validation loss;
- explicit distinction between core neural-network code and support/plotting code.

The lesson now uses one regression example throughout the full 2 × 45 minutes.
