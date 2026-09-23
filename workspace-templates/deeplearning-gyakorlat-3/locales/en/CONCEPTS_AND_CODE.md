# Concepts and code - a quick reminder

| Concept | Code / meaning |
|---|---|
| Input | `Input(shape=(2,))`: one point's two coordinates |
| Target | A known class, for example 2; in one-hot form [0,0,1] |
| Weight and bias | The network's learnable parameters |
| Hidden layer | `Dense(50, activation="relu")`: 50 learned intermediate features |
| ReLU | Zero for a negative input, itself for a non-negative one |
| Softmax | Three estimates summing to 1 for three mutually exclusive classes |
| Learning rate | `Adam(learning_rate=0.01)`: the optimizer's step scale |
| Configuration | `compile`: optimizer, loss, metrics |
| Training | `fit`: updating the weights and the biases from training pairs |
| Epoch | One pass over the whole training set |
| Batch | A group of samples used for one update |
| Validation | Checking and configuration choice, without a direct weight update |
| Loss | The deviation reduced by training; here cross-entropy |
| Accuracy | The proportion of correctly classified samples |
| Prediction | `predict`: per-class values, without a weight update |
| Class index | `argmax(axis=1)`: the position of the largest value in every sample |
| Measurement result | `evaluate`: loss and metrics, without a weight update |
| Test | The check with held-out data after the choice is closed |
| View refresh | Makes the already created new files visible in the file list |

360 samples and a batch of 32: 12 updates per epoch, the last batch has 8 samples.
The rate/epoch/batch/neuron count is a hyperparameter, the weight/bias is a learned parameter.
More epochs or a larger network does not automatically guarantee a better validation result.


For the `[0,0,1]` one-hot target categorical_crossentropy fits, for the `2` integer label
sparse_categorical_crossentropy fits, both with three softmax outputs.
The loss also takes the probability of the correct class into account; the accuracy is the
proportion of correct decisions. That is why the two metrics may rank models differently.
The 100% refers exclusively to the sample set actually measured, not a guarantee for every new point.

In the compulsory rate experiment only 0.01 -> 0.001 changes on the 50-50 network.
Out of all the R1-R4 runs we choose with the rule of the smaller validation loss;
on an exact tie the fewer parameters decide. We write our own reason before the test.
