# Detailed lesson · complete code

Follow the fixed checkpoint order. One active cell, then wait. Questions refer to the student’s actual output. Ask Z01 questions one at a time.

## [E01] Environment and GPU

All code is provided. In Colab, select a GPU runtime before loading data. A seed fixes the starting state of random operations; it does not promise bitwise identical training across devices. Path denotes a directory for local checkpoints. Local Jupyter can use a CPU with slower training.

```python
import os
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

SEED = 2026
keras.utils.set_random_seed(SEED)
try:
    import google.colab
    in_colab = True
except ImportError:
    in_colab = False
gpus = tf.config.list_physical_devices("GPU")
print("Environment:", "Colab" if in_colab else "Local Jupyter")
print("TensorFlow:", tf.__version__)
print("GPU:", gpus)
if in_colab and not gpus:
    print("Runtime -> Change runtime type -> Hardware accelerator -> GPU -> Save")
    raise RuntimeError("Select a GPU in Colab and rerun E01.")
work = Path("dl9_results")
work.mkdir(exist_ok=True)
EPSILON = 1e-3
```

**Question / minimal evidence:** Send the environment, TensorFlow and GPU lines. Which device will you use?


## [B01] Observe the updated BN demonstration

Open the accompanying BN HTML in a browser. Switch from N1 to N2 in the topology panel and inspect the mini-batch matrix. A row is one sample; a column contains one neuron’s weighted sums across samples. Change one input value and observe the statistics of the selected column. This is a discussion checkpoint, with no code cell.

**Question / minimal evidence:** Which entries in the matrix contribute to the mean of one selected neuron?


## [B02] Samples and features: axis=0

Read the array as the pre-activation values of two neurons: four rows are samples and two columns are neurons. mean(axis=0) reduces the rows and calculates each column separately. var uses the batch population variance (ddof=0). Epsilon is a small stabilizing term under the square root; this is not min–max scaling.

```python
samples = np.array([[2., 10.], [4., 18.], [6., 20.], [8., 40.]], dtype=np.float32)
mean = samples.mean(axis=0)
variance = samples.var(axis=0)
normalized = (samples - mean) / np.sqrt(variance + EPSILON)
print("Feature means:", mean)
print("Feature variances:", variance)
print("Normalized means:", normalized.mean(axis=0))
print("Normalized variances:", normalized.var(axis=0))
assert np.allclose(normalized.mean(axis=0), 0., atol=1e-6)
```

**Question / minimal evidence:** Using the printed means and variances, what did we treat separately? Send the four statistics lines.


## [B03] Gamma and beta per feature

The two entries of gamma and beta belong to the two columns. NumPy applies a (2,) array to every row, which is broadcasting. Learned scaling and shifting allow the output range to change; it is not restricted to [0,1].

```python
gamma = np.array([2., 0.5], dtype=np.float32)
beta = np.array([1., -3.], dtype=np.float32)
scaled = gamma * normalized + beta
print("Output means:", scaled.mean(axis=0))
print("Output standard deviations:", scaled.std(axis=0))
print("Output:\n", scaled)
```

**Question / minimal evidence:** Which column became wider, and which shifted to a negative mean? Use the printed values.


## [B04] Real Keras BN: weights and moving statistics

The first call builds the layer state. Gamma/beta are trainable; moving_mean/moving_variance are updated by training calls rather than gradients. We use momentum=0.5 for visibility: new = 0.5×old + 0.5×batch statistic. training=True normalizes with the current batch; a call alone does not optimize gamma/beta. numpy() converts a TensorFlow tensor to an array.

```python
bn = layers.BatchNormalization(momentum=0.5, epsilon=EPSILON)
_ = bn(samples, training=False)
before = [v.numpy().copy() for v in bn.weights]
training_output = bn(samples, training=True).numpy()
print("Trainable:", [v.name for v in bn.trainable_weights])
print("Non-trainable:", [v.name for v in bn.non_trainable_weights])
for variable, old in zip(bn.weights, before):
    print(variable.name, "before:", old, "after:", variable.numpy())
print("Matches NumPy:", np.allclose(training_output, normalized, atol=1e-5))
assert np.allclose(training_output, normalized, atol=1e-5)
```

**Question / minimal evidence:** Which state values changed in this call, and why did gamma/beta remain at their initial values?


## [B05] The same sample with different batch peers

Both batches start with 3, but their other values differ. training=True also changes moving statistics, so set_weights restores the same state before each probe. Inference uses the fixed moving_mean and moving_variance rather than batch peers. This avoids accidentally comparing different layer states.

```python
batch_a = np.array([[3.], [1.], [5.], [7.]], dtype=np.float32)
batch_b = np.array([[3.], [20.], [22.], [24.]], dtype=np.float32)
peer_bn = layers.BatchNormalization(epsilon=EPSILON)
_ = peer_bn(batch_a, training=False)
fixed_state = peer_bn.get_weights()
outputs = {}
for mode in [True, False]:
    values = []
    for batch in [batch_a, batch_b]:
        peer_bn.set_weights(fixed_state)
        values.append(float(peer_bn(batch, training=mode).numpy()[0, 0]))
    outputs[str(mode)] = values
    print("training=", mode, "first sample outputs:", values)
peer_bn.set_weights(fixed_state)
assert not np.isclose(*outputs["True"])
assert np.isclose(*outputs["False"])
```

**Question / minimal evidence:** How did changing the peers affect the first sample’s output in training and in inference?


## [B06] Freezing BN: link to lesson 8

trainable controls weight optimization and training controls the call mode. Keras BN has a special link: trainable=False also implies inference behavior, even with training=True. We check the separate layer built in B04; this is not a rule for every layer.

```python
bn.trainable = False
frozen_state = bn.get_weights()
frozen_output = bn(samples, training=True).numpy()
inference_output = bn(samples, training=False).numpy()
unchanged = all(np.array_equal(a, b) for a, b in zip(frozen_state, bn.get_weights()))
print("Trainable weights:", len(bn.trainable_weights))
print("BN state unchanged:", unchanged)
print("Matches inference:", np.allclose(frozen_output, inference_output))
assert unchanged and np.allclose(frozen_output, inference_output)
```

**Question / minimal evidence:** From the two checks, what happens to the frozen BN state and its output?


## [P01] Local and global pooling

Shape order is batch, height, width, channels. MaxPooling2D(2) takes a maximum in each 2×2 window, with default stride 2. Global pooling returns one value per channel over all spatial locations. keepdims=True would retain the 1×1 dimensions.

```python
image = np.arange(32, dtype=np.float32).reshape(1, 4, 4, 2)
for name, layer in [
    ("Local max", layers.MaxPooling2D(2)),
    ("Global max", layers.GlobalMaxPooling2D()),
    ("Global average", layers.GlobalAveragePooling2D()),
]:
    result = layer(image).numpy()
    print(name, "shape:", result.shape, "values:\n", result)
```

**Question / minimal evidence:** Which dimensions disappeared with global pooling, and were both channels retained?


## [P02] Flatten head and GAP head parameter counts

Four small models isolate the head:8 channels,5 outputs, two spatial sizes. Flatten makes every location an input to Dense; GAP first averages per channel. A full model’s Input shape may still constrain image size; here we build separate 8×8 and 16×16 models.

```python
for size in [8, 16]:
    for kind in ["Flatten", "GAP"]:
        inputs = keras.Input(shape=(size, size, 8))
        features = layers.Flatten()(inputs) if kind == "Flatten" else layers.GlobalAveragePooling2D()(inputs)
        head = keras.Model(inputs, layers.Dense(5)(features))
        print("Size:", size, "Head:", kind, "Parameters:", head.count_params())
```

**Question / minimal evidence:** Which head’s parameter count grew with spatial size? Use the four printed values.


## [C01] 1×1 convolution: channel mixing

A1×1 kernel with stride 1 applies the same learned channel mixing at each spatial location. This is not max pooling over channels. use_bias=False leaves only 8×3 weights.

```python
channels_input = tf.ones((1, 6, 6, 8))
mix = layers.Conv2D(3, 1, use_bias=False)
channels_output = mix(channels_input)
print("Input:", channels_input.shape, "Output:", channels_output.shape)
print("Parameters:", mix.count_params())
```

**Question / minimal evidence:** Using input and output shapes, what changed and what stayed the same?


## [R00] Observe the skip connection demonstration

Open the skip connection HTML. Select identity mode, F(x)=0. In the live vector panel, focus on the negative−1 input: H=x+F and y=ReLU(H) have separate columns. Toggle the skip off and on. The degradation curves and loss-landscape animation are illustrations, not training measurements from your notebook; deeper models are not guaranteed to improve.

**Question / minimal evidence:** For the negative input with F(x)=0, where does identity hold: at the sum or after the final ReLU?


## [R01] A real residual block: sum and ReLU

The Functional API builds two branches from tensors. The residual branch is Conv–BN–ReLU–Conv–BN; the second convolution deliberately starts with zero weights, making F=0. Add([x,F]) adds elementwise rather than concatenating channels. Three probe outputs expose the correction, sum and final ReLU. This probes one block rather than training a full ResNet.

```python
block_input = keras.Input(shape=(4, 4, 2))
branch = layers.Conv2D(2, 3, padding="same", use_bias=False)(block_input)
branch = layers.BatchNormalization(epsilon=EPSILON)(branch)
branch = layers.ReLU()(branch)
branch = layers.Conv2D(2, 3, padding="same", use_bias=False, kernel_initializer="zeros")(branch)
residual = layers.BatchNormalization(epsilon=EPSILON)(branch)
summed = layers.Add()([block_input, residual])
activated = layers.ReLU()(summed)
block_probe = keras.Model(block_input, [residual, summed, activated])
block_sample = np.linspace(-2., 2., 32, dtype=np.float32).reshape(1, 4, 4, 2)
correction, sum_output, relu_output = [v.numpy() for v in block_probe(block_sample, training=False)]
print("Maximum absolute F:", np.max(np.abs(correction)))
print("Maximum absolute H-x:", np.max(np.abs(sum_output - block_sample)))
print("First value x, H, ReLU(H):", block_sample.flat[0], sum_output.flat[0], relu_output.flat[0])
assert np.allclose(correction, 0.) and np.allclose(sum_output, block_sample)
```

**Question / minimal evidence:** Using the two difference checks and the negative sample, up to which point did the block preserve its input?


## [R02] Match shapes with a projection skip

Every dimension must match before Add. The learned branch uses stride 2 to halve 16×16 and changes 4 channels to 8. A1×1 convolution in the skip uses the same stride to match. The code shows the mismatch and its fix without deliberately executing an invalid Add.

```python
projection_input = tf.ones((1, 16, 16, 4))
learned_branch = layers.Conv2D(8, 3, strides=2, padding="same", use_bias=False)(projection_input)
projection = layers.Conv2D(8, 1, strides=2, padding="same", use_bias=False)
shortcut = projection(projection_input)
projection_sum = layers.Add()([learned_branch, shortcut])
print("Original:", projection_input.shape)
print("Branch:", learned_branch.shape, "Projection:", shortcut.shape)
print("Add output:", projection_sum.shape, "Projection parameters:", projection.count_params())
assert learned_branch.shape == shortcut.shape == projection_sum.shape
```

**Question / minimal evidence:** Why can we not add the input directly to the branch here? Use the three shapes.


## [R03] Gradient probe: help, not a guarantee

GradientTape records operations in its with block; watch marks the input and gradient computes output sensitivity. We repeat three scalar blocks: a plain a×x branch and a residual x+a×x branch. This is an illustrative calculation, not network training; no manual differentiation is required. With−1, the branch can cancel the identity contribution. A final probe measures ReLU on a negative input.

```python
for coefficient in [0.25, 0., -1.]:
    value = tf.constant(2.)
    with tf.GradientTape(persistent=True) as tape:
        tape.watch(value)
        plain, skip = value, value
        for _ in range(3):
            plain = coefficient * plain
            skip = skip + coefficient * skip
    print("a:", coefficient, "plain gradient:", float(tape.gradient(plain, value)),
          "skip gradient:", float(tape.gradient(skip, value)))
    del tape
negative = tf.constant(-2.)
with tf.GradientTape() as tape:
    tape.watch(negative)
    post_relu = tf.nn.relu(negative + 0. * negative)
print("Negative identity plus ReLU gradient:", float(tape.gradient(post_relu, negative)))
```

**Question / minimal evidence:** Which printed case contradicts the claim that a skip always guarantees an exactly 100%, nonzero gradient?


## [G01] Dropout in training and inference

Dropout(.5) randomly zeros activations during training and scales retained ones by 1/(1−.5). Inference passes inputs through. Two training calls usually get different masks; accidental equality is not an error. This is a separate probe; neither compared CNN uses Dropout.

```python
dropout = layers.Dropout(0.5, seed=SEED)
ones = tf.ones((2, 8))
print("Training call 1:\n", dropout(ones, training=True).numpy())
print("Training call 2:\n", dropout(ones, training=True).numpy())
print("Inference:\n", dropout(ones, training=False).numpy())
```

**Question / minimal evidence:** How does the inference output differ from the training calls?


## [G02] L2: a penalty added to the loss

regularizers.L2(.01) computes.01 times the sum of squared weights. During model training this regularization loss is added to the data loss. This is a separate numerical example; L2 with Adam is not claimed equivalent to AdamW’s decoupled weight decay.

```python
weights = tf.constant([1., -2.])
l2 = keras.regularizers.L2(0.01)
data_loss = 0.7
penalty = float(l2(weights))
print("Data loss:", data_loss, "Penalty:", penalty, "Total:", data_loss + penalty)
print("Penalty after doubling weights:", float(l2(2. * weights)))
```

**Question / minimal evidence:** What did L2 add to the data loss, and what happened when the weights doubled?


## [D01] CIFAR-10 images and labels

CIFAR-10 contains 50000 original training and 10000 test RGB images of 32×32. load_data downloads or uses a local cache. reshape(-1) turns a label column into a vector without changing categories. imshow displays raw 0–255 pixels; later Rescaling will be inside the model.

```python
(all_images, all_labels), (test_images_source, test_labels_source) = keras.datasets.cifar10.load_data()
all_labels = all_labels.reshape(-1)
test_labels_source = test_labels_source.reshape(-1)
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
print("Original training:", all_images.shape, all_labels.shape)
print("Original test:", test_images_source.shape, test_labels_source.shape)
print("Labels:", np.unique(all_labels), "Pixels:", all_images.dtype, all_images.min(), all_images.max())
fig, axes = plt.subplots(1, 5, figsize=(10, 2.5))
for index, axis in enumerate(axes):
    axis.imshow(all_images[index])
    axis.set_title(class_names[int(all_labels[index])])
    axis.axis("off")
plt.tight_layout()
plt.show()
```

**Question / minimal evidence:** What does a 32×32×3 image shape mean, and how many integer label values are present?


## [D02] Provided helper: disjoint splits

The cell fully defines split_indices; you do not write it. Inputs are a label vector and seed. It shuffles original training indices per class, returning the first 800 for training and next 200 for validation as two arrays. Call it with train_indices, val_indices = split_indices(all_labels, SEED). Separate test_indices select 200 per class from the original test source. Equal numeric indices in different sources do not mean the same image. split_indices.npz records the locally fixed selection.

```python
def split_indices(labels, seed):
    rng = np.random.default_rng(seed)
    train_parts, val_parts = [], []
    for label in range(10):
        indices = rng.permutation(np.flatnonzero(labels == label))
        train_parts.append(indices[:800])
        val_parts.append(indices[800:1000])
    return np.concatenate(train_parts), np.concatenate(val_parts)

train_indices, val_indices = split_indices(all_labels, SEED)
rng = np.random.default_rng(SEED + 1)
test_indices = np.concatenate([
    rng.permutation(np.flatnonzero(test_labels_source == label))[:200]
    for label in range(10)
])
assert np.intersect1d(train_indices, val_indices).size == 0
np.savez(work / "split_indices.npz", train=train_indices, validation=val_indices, test=test_indices)
train_images, train_labels = all_images[train_indices], all_labels[train_indices]
val_images, val_labels = all_images[val_indices], all_labels[val_indices]
test_images, test_labels = test_images_source[test_indices], test_labels_source[test_indices]
for name, labels in [("Train", train_labels), ("Validation", val_labels), ("Test", test_labels)]:
    print(name, "count:", len(labels), "per class:", np.bincount(labels, minlength=10))
print("Train/validation index overlap:", np.intersect1d(train_indices, val_indices).size)
```

**Question / minimal evidence:** Using the counts and overlap check, what role does each of the three sets play?


## [D03] Shared batches and retrieving the first element

We now create the training_data, validation_data and test_data Dataset streams. from_tensor_slices pairs each image with its label; batch(64) groups pairs into batches. One fixed preshuffled order is shared by both training runs and retained across epochs for this controlled experiment. In next(iter(...)), iter creates an iterator and next retrieves its first element: a complete images–labels batch pair, not one image or the entire set. Pixels are still raw.

```python
order = np.random.default_rng(SEED + 2).permutation(len(train_labels))
options = tf.data.Options()
options.threading.private_threadpool_size = 2
options.threading.max_intra_op_parallelism = 2
def make_data(images, labels):
    return tf.data.Dataset.from_tensor_slices((images, labels)).batch(64).with_options(options).prefetch(1)

training_data = make_data(train_images[order], train_labels[order])
validation_data = make_data(val_images, val_labels)
test_data = make_data(test_images, test_labels)
batch_images, batch_labels = next(iter(training_data))
print("Training/validation/test batches:", len(training_data), len(validation_data), len(test_data))
print("First batch:", batch_images.shape, batch_labels.shape)
print("Pixel range:", int(tf.reduce_min(batch_images)), int(tf.reduce_max(batch_images)))
print("First labels:", batch_labels[:8].numpy())
np.save(work / "training_order.npy", order)
```

**Question / minimal evidence:** From the retrieved shapes, what did next(iter(...)) return, and why do both models share the same data stream?


## [M01] Two small CNNs from one provided function

build_model(use_bn) is provided in full. Both models apply Rescaling(1/255) exactly once internally: preprocessing makes raw image pixels suitable for input. BN instead handles statistics of intermediate activations. The True branch inserts two BN layers between convolution and ReLU. There is no skip, Dropout, L2 or augmentation here; those were separate probes. This comparison studies BN, not ResNet performance.

```python
def build_model(use_bn):
    inputs = keras.Input(shape=(32, 32, 3))
    features = layers.Rescaling(1. / 255, name="rescale")(inputs)
    features = layers.Conv2D(16, 3, padding="same", use_bias=False, name="conv_1")(features)
    if use_bn:
        features = layers.BatchNormalization(epsilon=EPSILON, name="bn_1")(features)
    features = layers.ReLU(name="relu_1")(features)
    features = layers.MaxPooling2D(2, name="pool")(features)
    features = layers.Conv2D(32, 3, padding="same", use_bias=False, name="conv_2")(features)
    if use_bn:
        features = layers.BatchNormalization(epsilon=EPSILON, name="bn_2")(features)
    features = layers.ReLU(name="relu_2")(features)
    features = layers.GlobalAveragePooling2D(name="gap")(features)
    predictions = layers.Dense(10, activation="softmax", name="classifier")(features)
    return keras.Model(inputs, predictions, name="with_bn" if use_bn else "without_bn")

baseline = build_model(False)
bn_model = build_model(True)
for model in [baseline, bn_model]:
    print(model.name, [(layer.name, type(layer).__name__) for layer in model.layers])
```

**Question / minimal evidence:** Where do the two layer lists differ, and which operation preprocesses raw pixels?


## [M02] Shared initialization and separate optimizers

get_layer selects a named layer; get_weights/set_weights copies common Conv/Dense initial values. numpy.array_equal checks elements exactly; all three shared layers are checked rather than generalizing from one weight. BN starts with its own gamma/beta/moving state. Each model gets a separate fresh Adam; sparse loss expects integer labels. Initial weight files support local recovery.

```python
common_layers = ["conv_1", "conv_2", "classifier"]
for name in common_layers:
    bn_model.get_layer(name).set_weights(baseline.get_layer(name).get_weights())
    equal = all(np.array_equal(a, b) for a, b in zip(
        baseline.get_layer(name).get_weights(), bn_model.get_layer(name).get_weights()))
    print("Identical initial weights:", name, equal)
    assert equal
for model in [baseline, bn_model]:
    model.compile(optimizer=keras.optimizers.Adam(1e-3),
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    print(model.name, "total:", model.count_params(),
          "trainable:", sum(int(np.prod(v.shape)) for v in model.trainable_weights),
          "non-trainable:", sum(int(np.prod(v.shape)) for v in model.non_trainable_weights))
    model.save_weights(work / (model.name + "_initial.weights.h5"))
assert baseline.count_params() == 5370 and bn_model.count_params() == 5562
```

**Question / minimal evidence:** Which initial states are verified identical, and what does BN add to the parameter count?


## [M03] Train the CNN without BN

fit runs 6 full epochs on the shared stream. validation_data does not update weights. ModelCheckpoint saves weights with the lowest val_loss locally, which need not be the last epoch. history stores epoch metrics. Wait for completion rather than starting another fit. A full controlled rerun starts at M01, not by training an already trained model for another 6 epochs.

```python
baseline_path = work / "without_bn_best.weights.h5"
baseline_history = baseline.fit(
    training_data, validation_data=validation_data, epochs=6, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(baseline_path), monitor="val_loss",
               save_best_only=True, save_weights_only=True)]
)
(work / "baseline_history.json").write_text(json.dumps(baseline_history.history, indent=2))
print("Best validation-loss epoch:", int(np.argmin(baseline_history.history["val_loss"])) + 1)
```

**Question / minimal evidence:** Send train/val losses for the last two epochs. In your run, did they decrease together or behave differently?


## [M04] Train the BN CNN with the same budget

The second model gets the same images, batches,6 epochs and learning rate. BN is trainable=True and fit switches training/validation modes automatically. Its best checkpoint is separate. A single run does not prove all BN networks train faster or achieve higher accuracy; timing is not a controlled GPU benchmark either.

```python
bn_path = work / "with_bn_best.weights.h5"
bn_history = bn_model.fit(
    training_data, validation_data=validation_data, epochs=6, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(bn_path), monitor="val_loss",
               save_best_only=True, save_weights_only=True)]
)
(work / "bn_history.json").write_text(json.dumps(bn_history.history, indent=2))
print("Best validation-loss epoch:", int(np.argmin(bn_history.history["val_loss"])) + 1)
```

**Question / minimal evidence:** Using your outputs, how does the end of BN training differ from the previous model? Do not assume improvement.


## [M05] Restored checkpoints and validation selection

load_weights restores the best local state. evaluate measures this state, not the final epoch. Curves show fit training loss in training mode and validation loss in inference mode; BN uses different statistics in those modes. Lower re-evaluated val_loss selects the model; an exact tie favors the simpler baseline. selected_name is fixed before testing. BN improvement is not required.

```python
baseline.load_weights(baseline_path)
bn_model.load_weights(bn_path)
validation_results = {}
for name, model in [("without_bn", baseline), ("with_bn", bn_model)]:
    validation_results[name] = {k: float(v) for k, v in model.evaluate(validation_data, verbose=0, return_dict=True).items()}
selected_name = "with_bn" if validation_results["with_bn"]["loss"] < validation_results["without_bn"]["loss"] else "without_bn"
selected_model = bn_model if selected_name == "with_bn" else baseline
(work / "selection.json").write_text(json.dumps({"validation": validation_results, "selected": selected_name}, indent=2))
print("Restored validation:", validation_results)
print("Selected before test:", selected_name)
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
for name, history in [("without_bn", baseline_history), ("with_bn", bn_history)]:
    for axis, metric in zip(axes, ["loss", "accuracy"]):
        axis.plot(range(1, 7), history.history[metric], label=name + " train")
        axis.plot(range(1, 7), history.history["val_" + metric], linestyle="--", label=name + " validation")
        axis.set(xlabel="Epoch", ylabel=metric)
for axis in axes:
    axis.legend(fontsize=7)
plt.tight_layout()
plt.show()
```

**Question / minimal evidence:** Which model was selected from your restored val_loss values, and why?


## [V01] Final test after selection

We now document test results for the two predefined models once. No new selection, epochs or hyperparameters follow from test results. evaluate measures loss and correct-class proportion on the unshuffled test stream. The validation-selected model remains selected even if the other has higher test accuracy. This is the fixed balanced 2000-image subset, not all 10000 test images.

```python
test_results = {}
for name, model in [("without_bn", baseline), ("with_bn", bn_model)]:
    test_results[name] = {k: float(v) for k, v in model.evaluate(test_data, verbose=0, return_dict=True).items()}
print("Final test:", test_results)
print("Selection remains:", selected_name)
```

**Question / minimal evidence:** Send both test results. Why do we not reselect a model based on a possibly higher test accuracy?


## [V02] Predictions and confusion matrix step by step

First, argmax(axis=1) is shown on a separate 2×3 array: it returns the zero-based column index of each row’s maximum. Actual predict then returns 2000×10 probabilities. The test is unshuffled, so prediction rows align with D02 test labels without collecting labels again. Matrix rows are true classes, columns predicted classes; the diagonal is correct. Code finds an actual error, or the first image if none exists. Softmax is not validated confidence; possible visual explanations must rely on the image actually observed.

```python
toy_probabilities = np.array([[0.1, 0.7, 0.2], [0.6, 0.3, 0.1]])
print("Toy argmax:", toy_probabilities.argmax(axis=1))
probabilities = selected_model.predict(test_data, verbose=0)
predicted_labels = probabilities.argmax(axis=1)
matrix = tf.math.confusion_matrix(test_labels, predicted_labels, num_classes=10).numpy()
print("Confusion matrix (rows=true, columns=predicted):\n", matrix)
print("Matrix total:", matrix.sum(), "Row totals:", matrix.sum(axis=1))
assert matrix.sum() == 2000 and np.all(matrix.sum(axis=1) == 200)
assert np.isclose(np.trace(matrix) / 2000, test_results[selected_name]["accuracy"], atol=1e-6)
errors = np.flatnonzero(predicted_labels != test_labels)
example_index = int(errors[0]) if len(errors) else 0
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
plot = axes[0].imshow(matrix, cmap="Blues")
axes[0].set(xticks=range(10), yticks=range(10), xlabel="Predicted", ylabel="True")
fig.colorbar(plot, ax=axes[0])
axes[1].imshow(test_images[example_index])
axes[1].set_title("True: " + class_names[int(test_labels[example_index])] + "\nPredicted: " + class_names[int(predicted_labels[example_index])])
axes[1].axis("off")
plt.tight_layout()
plt.show()
np.savez(work / "test_predictions.npz", probabilities=probabilities, labels=test_labels, confusion_matrix=matrix)
```

**Question / minimal evidence:** Name one directed confusion from your matrix (true→predicted) and explain how you read it. If there are no errors, interpret the diagonal.


## [Z01] Three short reflections, one at a time

The tutor discusses the following questions one at a time; no new code is needed. A short, conceptually correct answer is sufficient.

**Question / minimal evidence:** 1. Why does BN use different statistics in training and inference?
2. Why did we distinguish the residual sum from the post-ReLU output?
3. What can you conclude from your BN comparison, and what can this single run not prove?


## [Z02] Local summary and completion

The code writes and displays your local results.json as a personal summary, not a submission. Saving your notebook for yourself is optional; no file, link, path or proof of saving is required.

```python
summary = {
    "seed": SEED, "tensorflow": tf.__version__, "batch_size": 64, "epochs_each": 6,
    "sizes": {"train": len(train_labels), "validation": len(val_labels), "test": len(test_labels)},
    "validation": validation_results, "selected_before_test": selected_name,
    "test": test_results, "confusion_matrix": matrix.tolist(),
    "scope": "One fixed CIFAR-10 subset and initialization; BN comparison, not ResNet training."
}
(work / "results.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
```

**Question / minimal evidence:** What was your most important takeaway from your own results?
