# Quick concept reference

| Concept | Meaning in these examples |
|---|---|
| Gradient | Sensitivity of loss to the current parameter; used to calculate updates. |
| Learning rate | A setting controlling the size of the step derived from the gradient. |
| Momentum | Retaining the effect of previous updates in a velocity variable. |
| Activation | A function transforming a neuron's weighted sum. |
| Local derivative | How the activation output responds to a small input change. |
| ReLU | `max(0, z)`; passes positive inputs through and zeros negative ones. |
| Leaky ReLU | Uses a fixed, usually small slope on the negative side as well. |
| Epoch | One complete pass through the training set. |
| Batch | A group of samples used together for one weight update. |
| MAE | Mean absolute difference between targets and predictions; not classification error rate. |
| Validation | Measurement used to investigate training settings, without directly updating weights. |
| L2 penalty | λ multiplied by the sum of squared selected weights. |
| Dropout | Randomly zeroing activations in training mode, with scaling of retained values. |

**Rule for comparison:** vary one experimental factor. Keep the task, data split
and suitable metric consistent. Change network size, epoch count and L2 strength
in separate experiments.

**Training error alone is insufficient:** performance on new samples may differ.
After repeated tuning against validation results, a final independent test would
be needed to assess a finalized model. This short demonstration has no such test.

**Interpret the output:** which setting changed, which metric changed, how large
was the difference and what in the figure supports your conclusion?
