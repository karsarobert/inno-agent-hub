# Closing test - teacher answer key

The tutor uses this for the feedback AFTER the answer; do not show it in advance.
A single correct answer per question. First answer: 1 or 0 points. In case of
help, indicate separately next to the point that it was not an independent answer.

| Question | Answer | Concept tested |
|---|---|---|
| 1 | B | Input features of one sample |
| 2 | C | Hidden layers and output layer |
| 3 | A | One-hot target, softmax, crossentropy |
| 4 | D | `fit` trains |
| 5 | B | Batches within an epoch |
| 6 | D | Update against the gradient |
| 7 | A | Per-sample argmax, index starting at 0 |
| 8 | C | Validation measurement |
| 9 | B | Divergence of crossentropy and accuracy |
| 10 | C | Independent evaluation of the saved model |

## 1. B

The 2 is the per-sample number of features. The two coordinates describe one point.
A: the sample count is the other dimension; C: we have three output classes;
D: the number of hidden layers is given by the layer lines, here there is one.
Help: separate the number of points from the data of one point.

## 2. C

Two `Dense(50, relu)` are the two hidden layers, `Dense(3, softmax)` is the output.
A: two consecutive 50-wide layers are not the same as one 100-wide;
B: the output layer is not counted as hidden;
D: it swaps the neuron counts.
Help: the last `Dense` is the output; read the lines standing before it.

## 3. A

Three one-hot target values need three softmax values and categorical_crossentropy.
B: the sparse variant expects an integer class index, not such a one-hot vector.
C: one sigmoid output does not describe this three-class one-hot task.
D: two outputs do not fit the three-element one-hot target vector.
Help: look at the shape of the target, and at the number of output neurons.

## 4. D

`fit` computes gradients and updates the trainable parameters.
A: `compile` configures; B: `evaluate` measures metrics; C: `predict` gives an estimate.
Help: which call did we give the training pairs and the number of epochs to?

## 5. B

11 x 32 = 352, and 360 - 352 = 8. The short last batch also runs, so there are
12 batches.
A: according to the task we do not drop the remainder;
C: `batch_size` is the sample count of a batch, not the number of batches;
D: this would be true with `batch_size=1`.
Help: divide the sample count by 32, and take the remainder into account as well.

## 6. D

1 - 0.1 x (-4) = 1 + 0.4 = 1.4. Subtracting the negative gradient increases the weight.
A: it ignores the sign of the gradient;
B: only the product of the rate and the gradient, not the new weight;
C: it adds only the rate, ignoring the gradient.
Help: first decide the sign of the product.

## 7. A

The maximum of the first row is at index 1, that of the second at index 0: [1, 0].
B: it gives maximum values, not indices;
C: it uses numbering starting at 1;
D: that would be the result of a column-wise argmax, with `axis=0`.
Help: with `axis=1` walk through the rows one by one.

## 8. C

A check measurement is made from the validation pairs; there is no direct weight
update.
A: it confuses the training and validation role;
B: it does not replace the training data;
D: that would need a separate early-stopping callback, there is none here.
Help: measuring and training are two different operations.

## 9. B

The maximum of both vectors belongs to class 1, and that is the correct label.
The loss for the given one-hot target is -ln(p_correct), so it decreases from
-ln(0.6), about 0.511, to -ln(0.8), about 0.223. The single-sample accuracy is 1 in
both cases.
A: a larger probability of the correct class gives a smaller loss;
C: the initial decision is also correct, and the loss does change;
D: the correct index holds the largest value in both cases.
Help: look separately at the position of the largest value and at the probability
of the correct class.

## 10. C

`load_model` loads the earlier layers and weights, `evaluate` measures on the
designated data. There is no `fit`, so there is no new training.
A: it does not start with new weights, and it does not train;
B: there is no model search or selection in these lines;
D: continuing the training would need `fit`.
Help: look for whether there is a training call in the snippet.

## Feedback

Keep the pre-answer guidance separate from the usual post-answer explanation.
In the closing, use the phrase "based on your answers you understand ... well", and
do not claim certain independent programming skill from the test result alone.
The score is not an automatic grade. Name the concepts to be repeated on the basis
of the mistakes. After that, the mandatory sentence:
**"The 3rd Deep Learning lab has ended."**
Do not start a further test or homework without the learner's separate request.
