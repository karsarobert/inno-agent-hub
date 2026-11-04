# Practice 8 · guided code walkthrough · 1.1

Follow the method in agent.md.

## [E01] Environment and Colab GPU

TensorFlow lists the devices visible to the current runtime. GPU: [] is an empty list: no GPU is currently visible. In Colab, first select Runtime → Change runtime type → Hardware accelerator → GPU, for example T4 GPU → Save, then reconnect. Rerun E01 and continue only after the GPU list is nonempty. Changing runtimes can reset variables and uploaded files. Local Jupyter has no Colab menu; use the device environment prepared by the instructor there.

**Current full code – provide it from the first attempt:**

```python
# [E01] Environment and workflow
import os, json, time, hashlib, tarfile, shutil
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
SEED = 42
keras.utils.set_random_seed(SEED)
CLASS_NAMES = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
WORK = Path('dl08_work')
WORK.mkdir(exist_ok=True)
print('TensorFlow:', tf.__version__, '| NumPy:', np.__version__)
print('GPU:', tf.config.list_physical_devices('GPU'))

# In Colab, switch runtimes before continuing with an empty GPU list.
try:
    import google.colab
    COLAB = True
except ImportError:
    COLAB = False
gpu_devices = tf.config.list_physical_devices('GPU')
print('Environment:', 'Colab' if COLAB else 'Jupyter / local Python')
if COLAB and not gpu_devices:
    print('Colab: Runtime → Change runtime type → Hardware accelerator → GPU / T4 GPU → Save.')
    raise RuntimeError('E01: connect to the GPU runtime, then rerun E01.')
print('E01 OK')
```

Return the versions, environment name, and GPU list. If Colab lists no GPU, change the runtime first and return the new E01 output.

**Question:** Which reported value tells you whether a GPU is available to this session?

**Request:** Return the versions, environment name, and GPU list. If Colab lists no GPU, change the runtime first and return the new E01 output.

**Acceptance – internal guidance:** In Colab, require a nonempty GPU list before E02. For [], give the menu steps and recheck, rather than automatically continuing on CPU. Handle local Jupyter separately.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [E02] Data and already implemented helper functions

This longer provided cell performs technical preparation. It downloads or opens the official image archive, then defines several helpers. def prepare_split(...) creates an already implemented function in memory; it does not yet split the images. D02 will call it. You do not need to rewrite or master the archive and hash infrastructure.

**Current full code – provide it from the first attempt:**

```python
# [E02] Data loading and checked utilities
ARCHIVE_SHA256 = '4c54ace7911aaffe13a365c34f650e71dd5bf1be0a58b464e5a7183e3e595d9c'
DATA_URL = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
def file_hash(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

local_folder = Path('flower_photos')
if local_folder.is_dir():
    data_dir = local_folder
else:
    archive = Path('flower_photos.tgz')
    if not archive.is_file():
        archive = Path(keras.utils.get_file('flower_photos.tgz', origin=DATA_URL,
            file_hash=ARCHIVE_SHA256, hash_algorithm='sha256'))
    if file_hash(archive) != ARCHIVE_SHA256:
        raise ValueError('Archive checksum mismatch')
    extraction = WORK / 'source'
    data_dir = extraction / 'flower_photos'
    if not all((data_dir / name).is_dir() for name in CLASS_NAMES):
        extraction.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archive) as packed:
            destination = extraction.resolve()
            for member in packed.getmembers():
                target = (extraction / member.name).resolve()
                if not target.is_relative_to(destination) or member.issym() or member.islnk():
                    raise ValueError('Unsafe archive member')
                if not member.isfile() and not member.isdir():
                    raise ValueError('Unsupported archive member')
            packed.extractall(extraction, filter='data')
assert all((data_dir / name).is_dir() for name in CLASS_NAMES)

def prepare_split(root, train_per_class, val_per_class, test_per_class):
    # Check decoding and exact duplicates before the deterministic split.
    rng = np.random.default_rng(SEED)
    seen = {}
    candidates = {name: [] for name in CLASS_NAMES}
    rejected = []
    for name in CLASS_NAMES:
        for path in sorted((root / name).glob('*.jpg')):
            try:
                with Image.open(path) as image:
                    image.verify()
                with Image.open(path) as image:
                    image.convert('RGB').resize((224, 224)).load()
            except (OSError, ValueError) as error:
                rejected.append({'path': str(path), 'reason': type(error).__name__})
                continue
            digest = file_hash(path)
            if digest in seen:
                if seen[digest] != name:
                    for previous_name in CLASS_NAMES:
                        removed = [(old_path, old_hash) for old_path, old_hash in candidates[previous_name] if old_hash == digest]
                        for old_path, old_hash in removed:
                            rejected.append({'path': str(old_path), 'reason': 'conflicting_labels'})
                        candidates[previous_name] = [(old_path, old_hash) for old_path, old_hash in candidates[previous_name] if old_hash != digest]
                    seen[digest] = None
                rejected.append({'path': str(path), 'reason': 'duplicate_or_conflicting_labels'})
                continue
            seen[digest] = name
            candidates[name].append((path, digest))
    manifest = []
    counts = [('train', train_per_class), ('val', val_per_class), ('test', test_per_class)]
    for name in CLASS_NAMES:
        pool = candidates[name]
        order = rng.permutation(len(pool))
        if len(pool) < sum(count for _, count in counts):
            raise ValueError('Not enough valid images in class: ' + name)
        start = 0
        for split, count in counts:
            for index in order[start:start + count]:
                path, digest = pool[int(index)]
                manifest.append({'split': split, 'class': name, 'relative_path': str(path.relative_to(root)), 'sha256': digest})
            start += count
    signature = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()[:12]
    split_root = WORK / ('split_' + signature)
    for row in manifest:
        source = root / row['relative_path']
        target = split_root / row['split'] / row['class'] / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or file_hash(target) != row['sha256']:
            shutil.copy2(source, target)
    (WORK / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    (WORK / 'rejected.json').write_text(json.dumps(rejected, indent=2), encoding='utf-8')
    license_file = root / 'LICENSE.txt'
    if license_file.exists():
        shutil.copy2(license_file, WORK / 'DATA_LICENSE.txt')
    print('Rejected:', len(rejected))
    return split_root, manifest

def parameter_count(weights):
    return int(sum(np.prod(weight.shape) for weight in weights))

def plot_history(history, title):
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))
    for axis, metric in zip(axes, ['loss', 'accuracy']):
        epochs = np.arange(1, len(history.history[metric]) + 1)
        axis.plot(epochs, history.history[metric], label='Training')
        axis.plot(epochs, history.history['val_' + metric], label='Validation')
        axis.set(xlabel='Epoch', ylabel={'loss': 'Loss', 'accuracy': 'Accuracy'}[metric], title=title)
        axis.legend()
    plt.tight_layout()
    plt.show()

def load_picture(path):
    with Image.open(path) as image:
        return np.asarray(image.convert('RGB').resize((224, 224)), dtype=np.float32)[None, ...]

print('Data directory:', data_dir)
print('E02 OK')
```

Run the provided cell and return the data-directory path and E02 OK.

**Question:** Which operation actually starts the image split: defining the function or calling it later?

**Request:** Run the provided cell and return the data-directory path and E02 OK.

**Acceptance – internal guidance:** Five class folders are available and data loading succeeded. Understands that def defines the helper, while the call runs it.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [E03] Applying the demonstrations to a new problem

The demonstrations used food images and cats/dogs. This task uses different data, a different model, and five integer labels. The transfer-learning principle stays the same.

**Current full code – provide it from the first attempt:**

This discussion checkpoint has no program code.

Answer briefly in the conversation.

**Question:** What changes when adapting the demonstrations to five flower classes? One or two essential differences are enough.

**Request:** A short personal response; no notebook writing requirement.

**Acceptance – internal guidance:** One or two essential correct differences suffice. Combine prior answers; do not demand every term or a prescribed sentence.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [D01] Flower classes and sample images

Folder names represent categories. These counts describe the full source archive, not the selected training subset. Labels will follow the fixed class order.

**Current full code – provide it from the first attempt:**

```python
# [D01] Flower classes and sample images
source_counts = {name: len(list((data_dir / name).glob('*.jpg'))) for name in CLASS_NAMES}
print(source_counts)
fig, axes = plt.subplots(1, 5, figsize=(12, 3))
for axis, name in zip(axes, CLASS_NAMES):
    path = sorted((data_dir / name).glob('*.jpg'))[0]
    with Image.open(path) as image:
        axis.imshow(image)
    axis.set_title(name)
    axis.axis('off')
plt.tight_layout()
plt.show()
```

Run the complete provided code cell; no independent code writing is required.

**Question:** What actual variation in color, shape, or background do you notice in the sample images?

**Request:** Counts for all five classes and one personal observation.

**Acceptance – internal guidance:** Five nonempty classes; observation grounded in image or student description.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [D02] Calling the already implemented split helper

prepare_split was already defined in E02, so we only call it now. Supply four inputs in order: data_dir locates the source images; the next three numbers specify training, validation, and test images per class. The helper checks images, removes exact duplicates and conflicting labels, samples using the fixed seed, and copies the chosen images into separate folders. It returns two objects: split_root is the folder root and manifest is a list recording each image’s split, class, path, and hash. The two names on the left receive these results. The final for loop counts the manifest entries by their split field; use the provided code.

**Current full code – provide it from the first attempt:**

```python
# [D02] Call the helper already implemented in E02.
train_per_class = 100
val_per_class = 40
test_per_class = 40
# Four inputs, two returned objects.
split_root, manifest = prepare_split(
    data_dir, train_per_class, val_per_class, test_per_class
)
# Count existing manifest entries without changing the split.
for split, title in [('train', 'Training'), ('val', 'Validation'), ('test', 'Test')]:
    count = sum(1 for row in manifest if row['split'] == split)
    print(title + ':', count)
```

Run the complete provided cell and return the three split counts.

**Question:** Does train_per_class = 100 request 100 training images in total or in each category? How does that explain your total training count?

**Request:** Run the complete provided cell and return the three split counts.

**Acceptance – internal guidance:** 500/200/200, or100/40/40 per class. Understands four inputs and two returned objects. No function implementation or counting code must be invented.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [D03] Creating the three datasets and data loaders

D02 organized images into separate folders. This cell first checks file-hash overlap, then creates train_ds, val_ds, and test_ds. These are tf.data.Dataset pipelines: they describe how to read and resize images in batches of16, rather than putting every image in memory at once. make_dataset(...) is the loader helper defined in this cell. train, val, and test choose the folder. shuffle=True mixes training order; shuffle=False keeps validation and test order fixed. Shared CLASS_NAMES ensures the same integer always represents the same flower. No test evaluation happens yet.

**Current full code – provide it from the first attempt:**

```python
# [D03] Data loaders and overlap check
digests = {split: {row['sha256'] for row in manifest if row['split'] == split} for split in ['train', 'val', 'test']}
print('Overlaps:', [len(digests[a] & digests[b]) for a, b in [('train', 'val'), ('train', 'test'), ('val', 'test')]])
assert not (digests['train'] & digests['val'] or digests['train'] & digests['test'] or digests['val'] & digests['test'])
def make_dataset(split, shuffle):
    dataset = keras.utils.image_dataset_from_directory(split_root / split,
        class_names=CLASS_NAMES, label_mode='int', image_size=(224, 224),
        batch_size=16, shuffle=shuffle, seed=SEED)
    assert dataset.class_names == CLASS_NAMES
    options = tf.data.Options()
    options.threading.private_threadpool_size = 2
    return dataset.with_options(options).prefetch(1)
train_ds = make_dataset('train', True)
val_ds = make_dataset('val', False)
test_ds = make_dataset('test', False)
print('Classes:', CLASS_NAMES)
```

Run the cell and return overlap counts and class order.

**Question:** Which new variable supplies fit’s training input, which supports model selection, and why should test ordering stay fixed?

**Request:** Run the cell and return overlap counts and class order.

**Acceptance – internal guidance:** Zero overlaps, shared class order. Distinguishes the three Dataset roles and preserves alignment between predictions and labels.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [D04] Fetching a batch: iter and next

images, labels = next(iter(train_ds)) is a new operation, so we break it down. iter(train_ds) creates an iterator over the pipeline. next(...) requests one item from it: here that is a pair containing16 images and their16 labels, not one image. The two names on the left unpack that pair. The provided code shows two separate lines using batch_iterator, plus the short form in a comment. shape reports dimensions, dtype the element type, and .numpy() exposes values as a NumPy array. Images still contain raw0–255 RGB pixels.

**Current full code – provide it from the first attempt:**

```python
# [D04] Short form: images, labels = next(iter(train_ds))
# The same operation in two steps: create an iterator, then fetch a batch.
batch_iterator = iter(train_ds)
images, labels = next(batch_iterator)
print('Image shape:', images.shape)
print('Label shape:', labels.shape)
print('Dtypes:', images.dtype, labels.dtype)
print('Pixel min/max:', float(tf.reduce_min(images)), float(tf.reduce_max(images)))
print('Labels:', labels.numpy())
```

Run the complete cell and return shapes, dtypes, pixel range, and labels.

**Question:** What do the four numbers in your image shape mean, and why does the label shape have no color-channel dimension?

**Request:** Run the complete cell and return shapes, dtypes, pixel range, and labels.

**Acceptance – internal guidance:** Images(16,224,224,3), labels(16,), float32/int32, pixels0–255, labels0–4. iter/next returns one batch. No need to invent this syntax.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [D05] Augmentation without changing labels

Small rotations and horizontal flips can give another view of the same flower. Augmentation will be inside the model and active only during training; test images remain unchanged.

**Current full code – provide it from the first attempt:**

```python
# [D05] Augmentation without changing labels
augmentation = keras.Sequential([
    layers.RandomFlip('horizontal', seed=SEED),
    layers.RandomRotation(0.05, seed=SEED + 1),
], name='augmentation')
augmented = augmentation(images[:1], training=True)
fig, axes = plt.subplots(1, 2, figsize=(6, 3))
axes[0].imshow(np.clip(images[0].numpy(), 0, 255).astype('uint8'))
axes[1].imshow(np.clip(augmented[0].numpy(), 0, 255).astype('uint8'))
for axis, title in zip(axes, ['Original', 'Augmented']):
    axis.set_title(title)
    axis.axis('off')
plt.tight_layout()
plt.show()
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Does the transformation you observed change the flower category? Explain briefly.

**Request:** One observed transformation and interpretation; a short correct answer is enough.

**Acceptance – internal guidance:** Transformation retains flower identity; only training augmented; avoid hallucinating unseen image.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [F01] What does preprocess_input mean?

Preprocessing transforms pixel values into the range expected by the pretrained model. MobileNetV2 preprocess_input maps0–255 to−1..1 using the equivalent of pixel /127.5 −1. The import retrieves this model-specific function; it does not download the base model. np.array(..., dtype=np.float32) creates a simple probe; four nested brackets are unnecessary. .copy() preserves the original array so before/after values can be printed. The real model will later include this operation exactly once.

**Current full code – provide it from the first attempt:**

```python
# [F01] MobileNetV2-specific preprocessing.
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
probe = np.array([0.0, 127.5, 255.0], dtype=np.float32)
transformed = preprocess_input(probe.copy())
print('Original:', probe)
print('Preprocessed:', transformed)
```

Run the provided probe and return the original and transformed values.

**Question:** When you later pass a new image to the complete model, which part should handle preprocessing so it does not happen twice?

**Request:** Run the provided probe and return the original and transformed values.

**Acceptance – internal guidance:** 0/127.5/255 maps to−1/0/1. The complete model handles preprocessing once; do not add another /255 or preprocess call.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [F02] Freezing a pretrained base

The base transforms visual patterns into features. Remove the original1000-class ImageNet head. trainable=False freezes the base weights; the new head remains trainable.

**Current full code – provide it from the first attempt:**

```python
# [F02] Freezing a pretrained base
base = keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base.trainable = False
print('Base:', base.output_shape, parameter_count(base.trainable_weights))
```

Run the complete provided code cell; no independent code writing is required.

**Question:** What does include_top=False remove, and which reported count confirms that the base is frozen?

**Request:** Output shape and base trainable parameter count.

**Acceptance – internal guidance:** ImageNet weights, include_top False, frozen, (None,7,7,1280), zero trainable base parameters.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [F03] Five-class head and loss

GlobalAveragePooling2D converts spatial feature maps into a vector. Softmax returns a distribution over five classes. Integer labels require sparse categorical crossentropy. training=False keeps base BN layers in inference mode without disabling later gradients.

**Current full code – provide it from the first attempt:**

```python
# [F03] Five-class head and loss
inputs = keras.Input(shape=(224, 224, 3))
x = augmentation(inputs)
x = preprocess_input(x)
x = base(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.2, seed=SEED + 2)(x)
outputs = layers.Dense(len(CLASS_NAMES), activation='softmax')(x)
model = keras.Model(inputs, outputs, name='flower_mobilenet')
model.compile(optimizer=keras.optimizers.Adam(1e-3), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
```

Run the complete provided code cell; no independent code writing is required.

**Question:** What does5 mean in the final summary shape(None,5), and how does the loss match integer labels?

**Request:** Final output shape and a short interpretation.

**Acceptance – internal guidance:** Five softmax outputs; sparse loss for integer labels; raw RGB input; exactly one preprocess; base training=False; head trainable.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [F04] What is trainable now?

The head parameter count depends on feature dimension, class count, and biases. The base should currently have zero trainable parameters. You do not need to list every layer.

**Current full code – provide it from the first attempt:**

```python
# [F04] What is trainable now?
print('Trainable:', parameter_count(model.trainable_weights))
print('Nontrainable:', parameter_count(model.non_trainable_weights))
print('Base trainable:', parameter_count(base.trainable_weights))
```

Run the complete provided code cell; no independent code writing is required.

**Question:** If you already returned these counts in F03, use that evidence. Given the base’s trainable count, which model component can learn now?

**Request:** Three parameter counts, or the same already verified F03 output.

**Acceptance – internal guidance:** Do not request counts already verified in F03 again. Only the head learns:6405 trainable, base0.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [F05] Training the head

fit updates head weights from training data. Save the best val_loss state and allow stopping after two epochs without improvement. Five epochs is an upper limit. A checksum verifies the base stayed unchanged.

**Current full code – provide it from the first attempt:**

```python
# [F05] Training the head
def weight_digest(network):
    digest = hashlib.sha256()
    for weight in network.weights:
        digest.update(weight.numpy().tobytes())
    return digest.hexdigest()
head_checkpoint = WORK / 'head.weights.h5'
fine_checkpoint = WORK / 'fine.weights.h5'
base_before = weight_digest(base)
head_start = time.perf_counter()
head_history = model.fit(train_ds, validation_data=val_ds, epochs=5, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(head_checkpoint), monitor='val_loss', save_best_only=True, save_weights_only=True),
               keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)])
head_seconds = time.perf_counter() - head_start
base_unchanged = base_before == weight_digest(base)
assert base_unchanged
(WORK / 'stage_head.json').write_text(json.dumps({'history': head_history.history, 'seconds': head_seconds, 'base_unchanged': base_unchanged}, indent=2), encoding='utf-8')
print('F05:', len(head_history.history['loss']), 'best val_loss:', min(head_history.history['val_loss']), 'base unchanged:', base_unchanged)
plot_history(head_history, 'Head training')
```

Run the complete provided code cell; no independent code writing is required.

**Question:** How did training and validation loss change in your log? Does that prove more epochs will always help?

**Request:** Epoch count, best val_loss, unchanged-base check, and observation.

**Acceptance – internal guidance:** Finite losses,1..5epochs; base checksum identical; no minimum accuracy threshold.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T01] Preserving the first phase

The next fit modifies the same model object. Keep the best head-stage weights in a separate file and start from them. Both variants remain available for comparison.

**Current full code – provide it from the first attempt:**

```python
# [T01] Preserving the first phase
model.load_weights(head_checkpoint)
head_validation = model.evaluate(val_ds, verbose=0, return_dict=True)
print('Checkpoint:', head_checkpoint.name)
print('Head validation:', head_validation)
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Why preserve a separate head checkpoint before continuing to train the same model?

**Request:** Checkpoint name and restored validation result; this is not a submission request.

**Acceptance – internal guidance:** Loads head weights and evaluates validation only; checkpoint still exists.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T02A] Inspecting layers and demonstrating selection

Before unfreezing anything, inspect the end of the base. base.layers is a list of layer objects; [-25:] selects its last25 entries. layer.name is the name, type(layer).__name__ the type, and trainable its current flag. startswith("block_16_") checks a name prefix, while == "Conv_1" checks an exact name. isinstance(layer, layers.BatchNormalization) checks the layer type. The second loop only prints candidate layers: it changes neither weights nor trainability. In the next cell, selection by name and exclusion by BN type jointly determine trainability.

**Current full code – provide it from the first attempt:**

```python
# [T02A] Inspect first: this cell does not modify any layer.
print('Layer name | type | currently trainable')
for layer in base.layers[-25:]:
    print(layer.name, '|', type(layer).__name__, '|', layer.trainable)
print('Candidates selected by name and their BN types:')
for layer in base.layers:
    selected_name = layer.name.startswith('block_16_') or layer.name == 'Conv_1'
    if selected_name:
        is_bn = isinstance(layer, layers.BatchNormalization)
        print(layer.name, '| BatchNormalization:', is_bn)
```

Run this inspection cell and return the candidate-layer list.

**Question:** Name one selected convolution layer and one BN layer from your output that must stay frozen.

**Request:** Run this inspection cell and return the candidate-layer list.

**Acceptance – internal guidance:** Candidates include block_16_ layers and Conv_1; BN layers are excluded by type in T02. Inspection itself does not mutate trainability.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T02] Unfreezing with the demonstrated selection rule

Apply the rule introduced in T02A. base.trainable=True first enables the parent model. For every layer, selected_name tests its name and is_bn tests its BatchNormalization type. if selected_name and not is_bn keeps only matching non-BN layers trainable; else freezes the rest again. Prepared checks report trainable names, trainable BN count, and parameter count. This does not train yet; recompilation follows in the next step.

**Current full code – provide it from the first attempt:**

```python
# [T02] Enable the parent, then set each individual layer's flag.
base.trainable = True
for layer in base.layers:
    selected_name = layer.name.startswith('block_16_') or layer.name == 'Conv_1'
    is_bn = isinstance(layer, layers.BatchNormalization)
    if selected_name and not is_bn:
        layer.trainable = True
    else:
        layer.trainable = False
trainable_names = []
trainable_bn = 0
for layer in base.layers:
    if layer.trainable:
        trainable_names.append(layer.name)
        if isinstance(layer, layers.BatchNormalization):
            trainable_bn += 1
print('Trainable base layers:', trainable_names)
print('Trainable BN:', trainable_bn)
print('Trainable model parameters:', parameter_count(model.trainable_weights))
```

Run the full provided cell and return the trainable names, BN count, and parameter count.

**Question:** Compare your T02A and T02 lists: which condition prevented block_16_ BN layers from becoming trainable?

**Request:** Run the full provided cell and return the trainable names, BN count, and parameter count.

**Acceptance – internal guidance:** Only selected non-BN layers trainable; BN count0; model trainable parameters885445. Interprets the condition rather than writing it from scratch.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T03] Recompiling with smaller updates

After changing trainability, compile again. Create a new Adam optimizer with learning rate1e-5; keep loss and metric unchanged. Smaller updates cautiously adapt pretrained features.

**Current full code – provide it from the first attempt:**

```python
# [T03] Recompiling with smaller updates
model.compile(optimizer=keras.optimizers.Adam(1e-5), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print('Learning rate:', float(model.optimizer.learning_rate.numpy()))
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Why recompile after changing trainable flags, and why use a lower learning rate in stage two?

**Request:** New learning_rate and a short interpretation of the code.

**Acceptance – internal guidance:** Fresh Adam1e-5; correct sparse loss; compile after T02; not just optimizer.learning_rate assignment.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T04] Careful fine-tuning

Keep the same training and validation splits and augmentation rules. Check BN weights and statistics remain unchanged while selected convolutional weights can change.

**Current full code – provide it from the first attempt:**

```python
# [T04] Careful fine-tuning
def bn_digest(network):
    digest = hashlib.sha256()
    for layer in network.layers:
        if isinstance(layer, layers.BatchNormalization):
            for weight in layer.weights:
                digest.update(weight.numpy().tobytes())
    return digest.hexdigest()
bn_before = bn_digest(base)
conv_before = base.get_layer('Conv_1').get_weights()[0].copy()
fine_start = time.perf_counter()
fine_history = model.fit(train_ds, validation_data=val_ds, epochs=5, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(fine_checkpoint), monitor='val_loss', save_best_only=True, save_weights_only=True),
               keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)])
fine_seconds = time.perf_counter() - fine_start
bn_unchanged = bn_before == bn_digest(base)
conv_changed = not np.array_equal(conv_before, base.get_layer('Conv_1').get_weights()[0])
assert bn_unchanged and conv_changed
(WORK / 'stage_fine.json').write_text(json.dumps({'history': fine_history.history, 'seconds': fine_seconds, 'bn_unchanged': bn_unchanged, 'conv_changed': conv_changed}, indent=2), encoding='utf-8')
print('T04:', len(fine_history.history['loss']), 'best val_loss:', min(fine_history.history['val_loss']))
print('BN unchanged:', bn_unchanged, 'Conv_1 changed:', conv_changed)
plot_history(fine_history, 'Fine-tuning')
```

Run the complete provided code cell; no independent code writing is required.

**Question:** What exactly do the two True checks establish, and what do they not prove on their own about every base layer?

**Request:** Epochs, best val_loss, BN and Conv_1 checks.

**Acceptance – internal guidance:** T02 checks the full layer selection rule. BN stayed unchanged and Conv_1 changed, but those two checks alone do not prove every other layer stayed unchanged. Last-epoch val_accuracy need not belong to the restored best-val_loss checkpoint.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [T05] Selecting a model using validation

val_loss and accuracy measure different things and may move differently. The predefined selection rule is lower val_loss, with the head-only variant winning a tie. Test data is still unused.

**Current full code – provide it from the first attempt:**

```python
# [T05] Selecting a model using validation
model.load_weights(fine_checkpoint)
fine_validation = model.evaluate(val_ds, verbose=0, return_dict=True)
selected_stage = 'fine' if fine_validation['loss'] < head_validation['loss'] else 'head'
selected_checkpoint = fine_checkpoint if selected_stage == 'fine' else head_checkpoint
model.load_weights(selected_checkpoint)
selection = {'head_validation': head_validation, 'fine_validation': fine_validation, 'selected_stage': selected_stage}
(WORK / 'selection.json').write_text(json.dumps(selection, indent=2), encoding='utf-8')
print('Head:', head_validation)
print('Fine:', fine_validation)
print('Selected:', selected_stage)
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Why did the code select this stage according to your two validation rows?

**Request:** Both validation results and selected stage; do not use test results yet.

**Acceptance – internal guidance:** Choice based on val_loss only; fine checkpoint remains; selected restored; results written before any test evaluation.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [V00] Argmax, axes, and concatenation on tiny arrays

Before testing the model, inspect new operations on a tiny synthetic array; this is not test data. Two samples receive three class values each. Each row is a sample, each column a category. np.argmax(..., axis=1) returns the index of the largest value within each row, not the value itself. Python indices start at0. np.concatenate(...) joins smaller arrays in their supplied order. Real test labels also arrive in batches, so we will join them into one label array.

**Current full code – provide it from the first attempt:**

```python
# [V00] Two synthetic samples, three class values per sample.
example = np.array([[0.1, 0.7, 0.2], [0.8, 0.1, 0.1]])
print('Example array:', example)
print('Row-wise largest-value indices:', np.argmax(example, axis=1))
# Join two small label arrays into one.
label_batches = [np.array([0, 2]), np.array([1])]
print('Joined labels:', np.concatenate(label_batches))
```

Run the tiny example and return row-wise class indices and concatenated labels.

**Question:** Which value does the first row’s returned index point to? Why preserve label-batch order?

**Request:** Run the tiny example and return row-wise class indices and concatenated labels.

**Acceptance – internal guidance:** Indices[1,0]; joined labels[0,2,1]. Index is a position, not a probability; labels must align with image predictions.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [V01] Real test predictions and joining label batches

Model selection is fixed; this is the first test evaluation. model.predict(test_ds) returns predictions in the dataset’s fixed image order. probabilities has200 rows and five columns: five values per image. np.argmax(..., axis=1) chooses one class index for each image. We collect true labels using an explicit for loop: the image part is unused, indicated by an underscore; batch_labels.numpy() converts labels to a NumPy array; append adds each batch to a list. np.concatenate joins them as in V00. sum(axis=1) adds the five values for each image. Test shuffling therefore stays disabled. Five identical initial predictions are not automatically a bug: fixed folder ordering may place the same class first.

**Current full code – provide it from the first attempt:**

```python
# [V01] Five class values for each test image.
probabilities = model.predict(test_ds, verbose=0)
# axis=1 selects an index among the five classes within each row.
predictions = np.argmax(probabilities, axis=1)
# The Dataset returns labels in batches; the image part is unused here.
label_batches = []
for _, batch_labels in test_ds:
    label_batches.append(batch_labels.numpy())
truth = np.concatenate(label_batches)
print('Probability shape:', probabilities.shape)
print('Prediction shape:', predictions.shape)
print('True-label shape:', truth.shape)
print('First five predictions:', predictions[:5])
row_sums = probabilities.sum(axis=1)
print('Row-sum min/max:', row_sums.min(), row_sums.max())
```

Run the full provided cell and return all three shapes, the first five predictions, and min/max row sums.

**Question:** Why does the class-index array have shape(200,) while the direct model output has shape(200,5)?

**Request:** Run the full provided cell and return all three shapes, the first five predictions, and min/max row sums.

**Acceptance – internal guidance:** Shapes(200,5),(200,),(200,); class indices0–4, row sums near1. Prediction/label order matches. List comprehensions need not be known or written.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [V02] Accuracy and confusion matrix

Accuracy is the fraction of correct predictions. Matrix rows are true classes and columns are predicted classes. The diagonal contains correct predictions; the total must equal test size.

**Current full code – provide it from the first attempt:**

```python
# [V02] Accuracy and confusion matrix
test_accuracy = accuracy_score(truth, predictions)
matrix = confusion_matrix(truth, predictions, labels=np.arange(len(CLASS_NAMES)))
print('Test accuracy:', test_accuracy)
print('Matrix:', matrix)
print('Total:', matrix.sum())
display = ConfusionMatrixDisplay(matrix, display_labels=CLASS_NAMES).plot(xticks_rotation=45)
display.ax_.set_xlabel('Predicted category')
display.ax_.set_ylabel('True category')
plt.tight_layout()
plt.show()
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Select a nonzero off-diagonal cell in your matrix and explain which true class was predicted as which class. If none exists, interpret a diagonal cell.

**Request:** Accuracy, complete matrix and total, plus your cell interpretation.

**Acceptance – internal guidance:** 5x5 integer matrix total200, row sums40; accuracy trace/200; correct row/column interpretation; no minimum threshold.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [V03] Inspecting a prediction error

One image cannot prove a general cause, but it can reveal a concrete error pattern. If there are no errors, inspect the least confident correct prediction. Array indices start at0.

**Current full code – provide it from the first attempt:**

```python
# [V03] Inspecting a prediction error
error_indices = np.flatnonzero(predictions != truth)
index = int(error_indices[0]) if len(error_indices) else int(np.argmin(probabilities[np.arange(len(truth)), truth]))
test_images = np.concatenate([batch_images.numpy() for batch_images, _ in test_ds])
print('Index:', index, 'error:', bool(predictions[index] != truth[index]))
print('True:', CLASS_NAMES[truth[index]], 'predicted:', CLASS_NAMES[predictions[index]])
print('Probabilities:', probabilities[index])
plt.figure(figsize=(4, 4))
plt.imshow(np.clip(test_images[index], 0, 255).astype('uint8'))
plt.axis('off')
plt.show()
```

Run the complete provided code cell; no independent code writing is required.

**Question:** What do you actually observe in the displayed image? Mark possible causes as hypotheses rather than proof.

**Request:** Index, true/predicted classes, probabilities, and observation.

**Acceptance – internal guidance:** Accept a grounded observation; an unusual viewpoint is a possible cause, not proof about typical training views. With no errors, do not label a selected correct prediction as an error.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [V04] A previously unused image

The prepared loader returns raw RGB float32 pixels in0–255 as a single-image batch. The model already preprocesses them; do not preprocess or divide again. A held-out source image that has never been used is suitable.

**Current full code – provide it from the first attempt:**

```python
# [V04] A previously unused image
used_paths = {row['relative_path'] for row in manifest}
used_hashes = {row['sha256'] for row in manifest}
unused_paths = sorted(path for path in data_dir.glob('*/*.jpg') if str(path.relative_to(data_dir)) not in used_paths and file_hash(path) not in used_hashes)
new_path = unused_paths[0]
new_batch = load_picture(new_path)
new_probabilities = model.predict(new_batch, verbose=0)[0]
new_index = int(np.argmax(new_probabilities))
print('New image:', new_path)
print('Probabilities:', new_probabilities)
print('Predicted:', CLASS_NAMES[new_index], 'softmax:', float(new_probabilities[new_index]))
```

Run the complete provided code cell; no independent code writing is required.

**Question:** Which class has the largest value, and why does that number alone not prove the prediction is correct?

**Request:** Predicted class and five softmax values; a folder name may be a reference label but does not let the tutor see the image.

**Acceptance – internal guidance:** Code ensures one preprocessing pass. Softmax and folder names do not prove a visual check of an unseen image. With a reference label, report agreement with that label.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [Z01] Your conclusions

Evaluate the reasoning as well as the numbers. Fine-tuning does not improve every run. Do not tune again on the test results in this exercise.

**Current full code – provide it from the first attempt:**

This discussion checkpoint has no program code.

Answer briefly in the conversation.

**Question:** Discuss three short questions one at a time: what changed from the demonstrations; which weights could change in each stage and what checks support this; whether validation improved and what the test is for.

**Request:** Three personal responses in the conversation; do not re-examine concepts already demonstrated.

**Acceptance – internal guidance:** Three questions one at a time, with brief personal answers. Credit prior demonstrated understanding; follow up only for material misunderstanding.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**

## [Z02] Summarize results and finish

The cell summarizes your measurements and saves results.json locally. You may save the notebook for yourself, but you do not need to submit, upload, or share it at the end. Completion is based on the outputs and interpretations already discussed here.

**Current full code – provide it from the first attempt:**

```python
# [Z02] Save and finish
head_record = json.loads((WORK / 'stage_head.json').read_text(encoding='utf-8'))
fine_record = json.loads((WORK / 'stage_fine.json').read_text(encoding='utf-8'))
results = {**selection, 'test_accuracy': float(test_accuracy), 'confusion_matrix': matrix.tolist(),
    'head_epochs': len(head_record['history']['loss']), 'fine_epochs': len(fine_record['history']['loss']),
    'head_seconds': head_record['seconds'], 'fine_seconds': fine_record['seconds'],
    'base_unchanged': head_record['base_unchanged'], 'bn_unchanged': fine_record['bn_unchanged'], 'conv_changed': fine_record['conv_changed'],
    'tensorflow': tf.__version__, 'numpy': np.__version__, 'split_sizes': {split: sum(row['split'] == split for row in manifest) for split in ['train','val','test']}}
(WORK / 'results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print('Selected:', selected_stage, '| Test accuracy:', test_accuracy)
print('Results:', WORK / 'results.json')
```

Run the summary and return the selected stage and final test accuracy to the tutor.

**Question:** What is the most important lesson from your run?

**Request:** Run the summary and return the selected stage and final test accuracy to the tutor.

**Acceptance – internal guidance:** Actual summary and discussed interpretation are sufficient. Do not request the notebook, a file name/path, proof of saving, or submission.

**Stop and wait. Accept brief, substantively correct answers without mandatory rewording.**
