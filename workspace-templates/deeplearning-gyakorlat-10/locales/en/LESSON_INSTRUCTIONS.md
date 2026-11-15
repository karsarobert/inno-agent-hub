# Detailed lesson: complete code and interpretation questions

One checkpoint, then wait. Ask Z01 questions separately.


## [E01] Environment and workflow

All code is provided. Run it in Colab or Jupyter and discuss its meaning with the tutor. Select a GPU in Colab before downloading data. A seed fixes the starting state of random operations. assets holds samples, dl10_data holds data and dl10_results holds local results. The cell installs gdown if missing; TensorFlow and the other packages require a working environment.

```python
import os
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")
import sys, json, hashlib, zipfile, subprocess
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications.resnet import preprocess_input
from sklearn.model_selection import train_test_split
try:
    import gdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown==5.2.0", "-q"])
    import gdown
SEED, SIZE, BATCH = 2026, (224, 224), 32
keras.utils.set_random_seed(SEED)
try:
    import google.colab
    in_colab = True
except ImportError:
    in_colab = False
gpus = tf.config.list_physical_devices("GPU")
print("Environment:", "Colab" if in_colab else "Local Jupyter")
print("TensorFlow:", tf.__version__, "GPU:", gpus)
if in_colab and not gpus:
    raise RuntimeError("Runtime > Change runtime type > GPU > Save; reconnect and rerun E01.")
assets, data_dir, work = Path("assets"), Path("dl10_data"), Path("dl10_results")
for folder in [assets, data_dir, work]:
    folder.mkdir(exist_ok=True)
def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()
```

**Question / minimal evidence:** Send the environment, TensorFlow and GPU lines. Which device are you using?


## [K01] A class or a number?

A classifier returns scores for classes; a regression head approximates a numerical label with one number. First we inspect a pretrained system, then train a new small head. This is a discussion checkpoint, without a code cell.

**Question / minimal evidence:** How does an elephant class score differ from a number approximating an age label?


## [C01] Two new sample images

The supplied load_rgb helper reads three RGB channels, resizes to 224×224 and returns float32 values. It does not apply ResNet preprocessing yet. SHA-256 verifies file identity, not image semantics or class correctness. These differ from the demonstration images.

```python
asset_specs = {'elephant.png': {'url': 'https://i.imgur.com/Bvro0YD.png', 'sha256': '51f9c798db2cbff325032496d9a54e7ddd9471924d7c57583f12ae16d550919d'}, 'sunflower.jpg': {'url': 'https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg', 'sha256': 'ff9b4c356d65c2e9708dd0b07cc4c3f2080996cfdb9db7cee259aca7bcedfe6a'}, 'imagenet_class_index.json': {'url': 'https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json', 'sha256': 'a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc'}}
for filename, spec in asset_specs.items():
    path = assets / filename
    if not path.exists():
        keras.utils.get_file(fname=filename, origin=spec["url"],
            cache_dir=str(assets.resolve().parent), cache_subdir=assets.name,
            file_hash=spec["sha256"], hash_algorithm="sha256")
    if sha256_file(path) != spec["sha256"]:
        raise ValueError("Sample file checksum mismatch: " + filename)
def load_rgb(path):
    image = tf.image.decode_image(tf.io.read_file(str(path) if isinstance(path, Path) else path),
                                  channels=3, expand_animations=False)
    image.set_shape([None, None, 3])
    return tf.image.resize(image, SIZE, method="bilinear")
sample_images = [load_rgb(assets / name).numpy() for name in ["elephant.png", "sunflower.jpg"]]
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for axis, image in zip(axes, sample_images):
    axis.imshow(image.astype(np.uint8)); axis.axis("off")
    print("RGB shape:", image.shape, "range:", image.min(), image.max())
plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** What do 224, 224 and 3 mean in the image shapes?


## [C02] ResNet50 and the preprocessing helper

The supplied prepare_batch adds a batch dimension to a raw RGB image, copies it and applies ResNet preprocess_input once: RGB→BGR and ImageNet channel-mean subtraction, rather than 0–1 rescaling. classifier returns logits; softmax is applied separately. This pretrained model does not train here.

```python
classifier = keras.applications.ResNet50(weights="imagenet", classifier_activation=None)
classifier.trainable = False
def prepare_batch(image):
    return preprocess_input(np.array(image, dtype=np.float32, copy=True)[None, ...])
prepared_sample = prepare_batch(sample_images[0])
print("Prepared batch:", prepared_sample.shape, "range:", prepared_sample.min(), prepared_sample.max())
print("Classifier output:", classifier.output_shape)
class_index = json.loads((assets / "imagenet_class_index.json").read_text())
```

**Question / minimal evidence:** Why would an additional /255 before prepare_batch break the expected input contract?


## [C03] Logits, softmax and top 5

argmax returns the index of the maximum; argsort returns sorting indices. [::-1] reverses the order and [: 5] takes the first five. JSON maps the same class index to its name. Softmax values sum to 1, but are not validated confidence or ground truth.

```python
classification_logits = [classifier(prepare_batch(image), training=False).numpy()[0] for image in sample_images]
classification_probabilities = [tf.nn.softmax(values).numpy() for values in classification_logits]
for image_number, probabilities in enumerate(classification_probabilities):
    top_indices = np.argsort(probabilities)[::-1][:5]
    print("Image:", image_number)
    for index in top_indices:
        print(int(index), class_index[str(index)][1], "probability:", round(float(probabilities[index]), 5),
              "logit:", round(float(classification_logits[image_number][index]), 4))
target_class = int(np.argmax(classification_probabilities[0]))
control_class = next(int(k) for k, v in class_index.items() if v[0] == "n03063599")
print("Fixed target:", target_class, class_index[str(target_class)][1])
print("Control:", control_class, class_index[str(control_class)][1])
```

**Question / minimal evidence:** Send the first image’s top 1 line. Is it a prediction or a verified image label?


## [C04] Feature maps and weighted sums

get_layer selects a named layer; Model exposes two outputs together. get_weights returns a kernel and bias. tensordot sums the last, channel axis with the weight vector, retaining two spatial axes. We first use a 2×2×3 array; no manual calculation is required.

```python
activation_probe = keras.Model(classifier.inputs,
    [classifier.get_layer("conv5_block3_out").output, classifier.output])
class_kernel, class_bias = classifier.get_layer("predictions").get_weights()
activation_values, logits = activation_probe(prepare_batch(sample_images[0]), training=False)
print("Activation shape:", activation_values.shape, "Kernel:", class_kernel.shape)
toy_features = np.arange(12, dtype=np.float32).reshape(2, 2, 3)
toy_weights = np.array([0.2, -0.4, 0.7])
toy_map = np.tensordot(toy_features, toy_weights, axes=([-1], [0]))
print("Toy map shape:", toy_map.shape, "values:\n", toy_map)
print("GAP then Dense:", toy_features.mean(axis=(0, 1)) @ toy_weights + 0.3)
print("CAM mean plus bias:", toy_map.mean() + 0.3)
```

**Question / minimal evidence:** Why is the toy weighted map 2×2, and which dimension disappeared?


## [C05] Classic CAM and logit reconstruction

classic_cam and draw_signed are fully supplied. The first returns a raw signed map and target logit; the second plots a symmetric positive/negative scale. mean(CAM)+bias verifies the GAP→Dense computation, not the image class. The positive-map normalizer returns zeros for constant/nonpositive maps rather than dividing by zero.

```python
def classic_cam(image, class_id):
    activations, scores = activation_probe(prepare_batch(image), training=False)
    raw_map = np.tensordot(activations.numpy()[0], class_kernel[:, class_id], axes=([-1], [0]))
    score = float(scores.numpy()[0, class_id])
    reconstructed = float(raw_map.mean() + class_bias[class_id])
    assert np.isclose(score, reconstructed, atol=1e-4, rtol=1e-4)
    return raw_map, score

def normalize_positive(raw_map):
    positive = np.maximum(raw_map, 0.)
    if np.ptp(positive) < 1e-8 or positive.max() <= 1e-8:
        return np.zeros_like(positive)
    return positive / positive.max()

def draw_signed(axis, image, raw_map, title, limit):
    axis.imshow(image.astype(np.uint8), extent=(0, 1, 0, 1))
    plot = axis.imshow(raw_map, extent=(0, 1, 0, 1), cmap="coolwarm", alpha=0.55,
                       vmin=-limit, vmax=limit, interpolation="bilinear")
    axis.set_title(title, fontsize=10); axis.axis("off")
    return plot

first_cam, first_score = classic_cam(sample_images[0], target_class)
print("Target logit:", first_score, "CAM mean+bias:", float(first_cam.mean() + class_bias[target_class]))
print("Raw CAM min/max:", first_cam.min(), first_cam.max())
print("Constant-map guard:", np.array_equal(normalize_positive(np.ones((2, 2))), np.zeros((2, 2))))
fig, axis = plt.subplots(figsize=(6, 4))
plot = draw_signed(axis, sample_images[0], first_cam, class_index[str(target_class)][1], max(float(np.abs(first_cam).max()), 1e-8))
fig.colorbar(plot, ax=axis, label="Signed contribution"); plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** Do the raw CAM and its 0–1 display use the same numerical scale?


## [C06] Two target classes, one scale

We compare the fixed top 1 class with the coffee_mug control on the same image, printing both names and probabilities. Both maps use the same color range, allowing numerical color comparisons. This differs from separately min–max-normalized plots.

```python
control_cam, control_score = classic_cam(sample_images[0], control_class)
shared_limit = max(float(np.abs(first_cam).max()), float(np.abs(control_cam).max()), 1e-8)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for axis, class_id, raw_map in zip(axes, [target_class, control_class], [first_cam, control_cam]):
    probability = float(classification_probabilities[0][class_id])
    print(class_id, class_index[str(class_id)][1], "probability:", probability,
          "raw min/max:", float(raw_map.min()), float(raw_map.max()))
    plot = draw_signed(axis, sample_images[0], raw_map, class_index[str(class_id)][1], shared_limit)
fig.colorbar(plot, ax=axes.tolist(), label="Shared signed scale"); plt.show()
second_class = int(np.argmax(classification_probabilities[1]))
second_cam, second_score = classic_cam(sample_images[1], second_class)
print("Second image CAM-logit agreement:", True, class_index[str(second_class)][1])
```

**Question / minimal evidence:** Why can the heatmaps differ when the input image is unchanged?


## [C07] A fixed occlusion experiment

The supplied code replaces one fixed central rectangle with gray. The target remains the original top 1 even if the new top 1 changes. Thus we repeat the same measurement. The gray patch changes the input distribution, so this is not a clean causal proof.

```python
occluded_image = sample_images[0].copy()
occluded_image[64:176, 64:176, :] = 127.5
occluded_cam, occluded_score = classic_cam(occluded_image, target_class)
occluded_probabilities = tf.nn.softmax(classifier(prepare_batch(occluded_image), training=False)[0]).numpy()
new_top = int(occluded_probabilities.argmax())
print("Fixed target:", class_index[str(target_class)][1])
print("Target logits original/occluded:", first_score, occluded_score, "change:", occluded_score - first_score)
print("Target probabilities:", float(classification_probabilities[0][target_class]), float(occluded_probabilities[target_class]))
print("New top1:", class_index[str(new_top)][1])
limit = max(float(np.abs(first_cam).max()), float(np.abs(occluded_cam).max()), 1e-8)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for axis, image, raw_map, title in zip(axes, [sample_images[0], occluded_image], [first_cam, occluded_cam], ["Original", "Fixed occlusion"]):
    plot = draw_signed(axis, image, raw_map, title, limit)
fig.colorbar(plot, ax=axes.tolist(), label="Shared signed scale"); plt.show()
cam_results = {"target": target_class, "target_name": class_index[str(target_class)][1],
               "original_logit": first_score, "occluded_logit": occluded_score,
               "control_probability": float(classification_probabilities[0][control_class])}
_ = (work / "cam_results.json").write_text(json.dumps(cam_results, indent=2))
```

**Question / minimal evidence:** How did the original target logit change, and what can this one measurement not establish?


## [C08] What does a heatmap not prove?

CAM shows weighted spatial contributions for a selected class. It is neither object detection nor a ground-truth pixel mask. Grad-CAM is a separate gradient-based method; this classic CAM uses weights rather than derivatives. No cell is executed here.

**Question / minimal evidence:** Why can a bright, independently normalized map for a low-probability class mislead?


## [A01] Load the age dataset

The supplied download/extraction code uses the demonstration CSV/ZIP and pins their hashes. file_name identifies an image; real_age is the numerical target. The repackaged files do not establish the original APPA-REAL split, so we use a documented custom split. The code does not identify people.

```python
data_specs = {'labels.csv': {'id': '15G625qvDsp8wDgydwaiAgAXzfSq3I7NS', 'sha256': '7fc5cd15a21e17eccbb3242963bbd2bafa78cbf4ab1453339c9670f88f7f5e65'}, 'final_files.zip': {'id': '1rXFvWYz6UCv4aD_YT741wbthqm_BBnqY', 'sha256': '716bc1f6ce68406f3212b024592241ecc0131f234c8f5a82af6a2f333e72fff5'}}
for filename, spec in data_specs.items():
    path = data_dir / filename
    if not path.exists():
        gdown.download(id=spec["id"], output=str(path), quiet=False)
    if not path.exists() or sha256_file(path) != spec["sha256"]:
        raise RuntimeError("Dataset missing or checksum differs: " + filename)
image_dir = data_dir / "final_files"
if not image_dir.exists():
    with zipfile.ZipFile(data_dir / "final_files.zip") as archive:
        for member in archive.infolist():
            target = (data_dir / member.filename).resolve()
            if not target.is_relative_to(data_dir.resolve()):
                raise ValueError("Invalid archive member")
        archive.extractall(data_dir)
labels = pd.read_csv(data_dir / "labels.csv")
print("CSV rows:", len(labels), "columns:", labels.columns.tolist())
print(labels.head().to_string(index=False))
assert {"file_name", "real_age"}.issubset(labels.columns) and image_dir.is_dir()
```

**Question / minimal evidence:** Which CSV columns link the image file to its numerical target?


## [A02] Data checks and distribution

The supplied check opens every file, hashes decoded RGB content and requires numerical labels in 0–120. It excludes corrupt images and conflicting labels for identical content; one copy is retained when labels agree. Exclusions are recorded. This is not identity-based separation: distinct photos of one person may remain.

```python
records, excluded = [], []
for row in labels[["file_name", "real_age"]].itertuples(index=False):
    try:
        age = float(row.real_age)
        path = image_dir / str(row.file_name)
        if not path.resolve().is_relative_to(image_dir.resolve()) or not np.isfinite(age) or not 0 <= age <= 120:
            raise ValueError("Invalid path or age")
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            content_hash = hashlib.sha256(str(rgb.size).encode() + rgb.tobytes()).hexdigest()
        records.append({"file_name": str(row.file_name), "real_age": age, "image_hash": content_hash})
    except Exception as error:
        excluded.append({"file_name": str(row.file_name), "reason": type(error).__name__})
checked = pd.DataFrame(records).sort_values("file_name").reset_index(drop=True)
conflicting = checked.groupby("image_hash")["real_age"].nunique()
conflict_hashes = set(conflicting[conflicting > 1].index)
conflict_mask = checked.image_hash.isin(conflict_hashes)
for filename in checked.loc[conflict_mask, "file_name"]:
    excluded.append({"file_name": filename, "reason": "Conflicting duplicate labels"})
checked = checked.loc[~conflict_mask].copy()
duplicate_mask = checked.duplicated("image_hash", keep="first")
for filename in checked.loc[duplicate_mask, "file_name"]:
    excluded.append({"file_name": filename, "reason": "Duplicate RGB content"})
clean_labels = checked.loc[~duplicate_mask].reset_index(drop=True)
pd.DataFrame(excluded, columns=["file_name", "reason"]).to_csv(work / "excluded.csv", index=False)
print("Valid unique images:", len(clean_labels), "Excluded:", len(excluded))
print("Age range:", clean_labels.real_age.min(), clean_labels.real_age.max())
print(pd.DataFrame(excluded).get("reason", pd.Series(dtype=str)).value_counts().to_string())
fig, axis = plt.subplots(figsize=(8, 3))
axis.hist(clean_labels.real_age, bins=np.arange(0, 125, 5), color="#6c5bb4")
axis.set(xlabel="Dataset age label (years)", ylabel="Count"); plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** How many valid images remain in your report, and which limitation does an image hash not resolve?


## [A03] Call the provided split helper

The cell fully defines split_data: it accepts a checked DataFrame and seed and returns three DataFrames. It preserves the proportions of age-label groups 0–19, 20–39, 40–59, 60+in an approximately 60/20/20 custom split. Two train_test_split calls implement it for you. Image hashes must not overlap across splits.

```python
AGE_BINS = [-0.001, 20, 40, 60, 121]
AGE_GROUPS = ["0-19", "20-39", "40-59", "60+"]
def split_data(frame, seed):
    frame = frame.copy()
    frame["age_group"] = pd.cut(frame.real_age, bins=AGE_BINS, labels=AGE_GROUPS, right=False)
    train_frame, remaining = train_test_split(frame, test_size=0.4, random_state=seed, stratify=frame.age_group)
    val_frame, test_frame = train_test_split(remaining, test_size=0.5, random_state=seed + 1, stratify=remaining.age_group)
    return [part.sort_values("file_name").reset_index(drop=True) for part in [train_frame, val_frame, test_frame]]
train_frame, val_frame, test_frame = split_data(clean_labels, SEED)
manifest = pd.concat([part.assign(split=name) for name, part in [("train", train_frame), ("validation", val_frame), ("test", test_frame)]], ignore_index=True)
assert manifest.image_hash.is_unique
manifest.to_csv(work / "split_manifest.csv", index=False)
print("Custom split (not official APPA-REAL):")
print(pd.crosstab(manifest.split, manifest.age_group).to_string())
print("Split sizes:", len(train_frame), len(val_frame), len(test_frame))
```

**Question / minimal evidence:** Which split updates weights, selects the checkpoint and remains for final evaluation?


## [A04] Data streams and one whole batch

from_tensor_slices pairs file paths and labels; map loads images and batch(32)groups them. All three raw streams now exist, before ResNet preprocessing. iter creates an iterator and next retrieves one item: a whole images–labels batch pair. Raw streams remain ordered to align feature caches later.

```python
options = tf.data.Options()
options.threading.private_threadpool_size = 2
options.threading.max_intra_op_parallelism = 2
def raw_data(frame):
    paths = [str(image_dir / name) for name in frame.file_name]
    dataset = tf.data.Dataset.from_tensor_slices((paths, frame.real_age.to_numpy(np.float32)))
    dataset = dataset.map(lambda path, age: (load_rgb(path), age), num_parallel_calls=2)
    return dataset.batch(BATCH).with_options(options).prefetch(1)
raw_train = raw_data(train_frame)
raw_validation = raw_data(val_frame)
raw_test = raw_data(test_frame)
batch_images, batch_labels = next(iter(raw_train))
print("First raw batch:", batch_images.shape, batch_labels.shape)
print("Raw pixel range:", float(tf.reduce_min(batch_images)), float(tf.reduce_max(batch_images)))
```

**Question / minimal evidence:** From the two shapes, did next return one image or a whole batch pair?


## [A05] Preprocess once and consistently

map now transforms raw_train/raw_validation/raw_test into ResNet inputs. Keep raw images for display: mean-centered BGR arrays are not ordinary RGB inputs for imshow. A known[10, 20, 30]RGB pixel supplies a separate check.

```python
def model_data(dataset):
    return dataset.map(lambda images, ages: (preprocess_input(images), ages), num_parallel_calls=2)
training_data = model_data(raw_train)
validation_data = model_data(raw_validation)
test_data = model_data(raw_test)
processed_images, processed_labels = next(iter(training_data))
known_pixel = np.array([[[[10., 20., 30.]]]], dtype=np.float32)
print("Known RGB pixel -> model input:", preprocess_input(known_pixel.copy()).reshape(-1))
print("Model batch:", processed_images.shape, "range:", float(tf.reduce_min(processed_images)), float(tf.reduce_max(processed_images)))
assert processed_images.shape == batch_images.shape
```

**Question / minimal evidence:** Why display the original RGB array rather than the preprocessed array directly?


## [B01] What does MAE mean?

First use three known labels/predictions. Signed error is prediction−label; absolute value removes direction and mean averages the absolute errors. MAE is neither a guaranteed±bound for each person nor a confidence interval.

```python
example_labels = np.array([10., 30., 70.])
example_predictions = np.array([14., 22., 72.])
example_errors = example_predictions - example_labels
print("Signed errors:", example_errors)
print("Absolute errors:", np.abs(example_errors))
print("MAE in years:", np.abs(example_errors).mean())
```

**Question / minimal evidence:** Which absolute error exceeds the mean, and why is that not a contradiction?


## [B02] An image-free median baseline

The median uses training labels only, returning that same constant for every validation image. It measures an image-free reference. Validation labels do not determine the median.

```python
training_median = float(train_frame.real_age.median())
baseline_validation_mae = float(np.abs(val_frame.real_age.to_numpy() - training_median).mean())
print("Training median:", training_median)
print("Baseline validation MAE:", baseline_validation_mae)
```

**Question / minimal evidence:** Why compare the CNN with this simple prediction too?


## [F01] Frozen feature extraction

feature_extractor exposes the same ResNet’s final convolutional features. GAP averages spatial positions, leaving 2048 values per image. We disable trainability and call with training=False, so BN moving state also remains fixed.

```python
feature_extractor = keras.Model(classifier.inputs, classifier.get_layer("conv5_block3_out").output)
feature_extractor.trainable = False
gap = layers.GlobalAveragePooling2D()
first_features = feature_extractor(processed_images, training=False)
first_vectors = gap(first_features)
print("Spatial features:", first_features.shape, "GAP vectors:", first_vectors.shape)
print("Trainable extractor weights:", len(feature_extractor.trainable_weights))
assert first_vectors.shape[-1] == 2048 and not feature_extractor.trainable_weights
```

**Question / minimal evidence:** Which two dimensions did GAP remove from the feature map?


## [F02] An ordered feature cache

The supplied extract_features reads the ordered stream and stores only GAP vectors. Cache identity covers image hashes/order, weights, TensorFlow version and preprocessing. Loading requires matching identifiers. We extract training/validation features now; testing comes later. Output distinguishes extraction from a cache hit.

```python
weight_digest = hashlib.sha256()
for variable in feature_extractor.weights:
    weight_digest.update(variable.numpy().tobytes())
extractor_hash = weight_digest.hexdigest()
cache_dir = Path(os.environ.get("DL10_CACHE_DIR", str(work / "feature_cache")))
cache_dir.mkdir(parents=True, exist_ok=True)
def extract_features(dataset, frame, name):
    identity = {"files": frame.file_name.tolist(), "hashes": frame.image_hash.tolist(),
                "weights": extractor_hash, "tensorflow": tf.__version__,
                "preprocess": "tf_decode_rgb_resize_bilinear224_resnet_caffe_v1"}
    signature = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
    path = cache_dir / (name + "_" + signature[:16] + ".npz")
    if path.exists():
        with np.load(path, allow_pickle=False) as saved:
            if str(saved["signature"].item()) != signature or not np.array_equal(saved["files"], frame.file_name.to_numpy(str)):
                raise ValueError("Cache identity mismatch")
            features, ages = saved["features"], saved["ages"]
        print("Cache hit:", name, features.shape)
    else:
        feature_parts, age_parts = [], []
        for number, (images, ages) in enumerate(dataset):
            feature_parts.append(gap(feature_extractor(images, training=False)).numpy())
            age_parts.append(ages.numpy())
            if number % 30 == 0:
                print("Extracting:", name, "batch", number + 1, "/", len(dataset))
        features, ages = np.concatenate(feature_parts), np.concatenate(age_parts)
        np.savez_compressed(path, features=features, ages=ages, files=frame.file_name.to_numpy(str), signature=signature)
    assert len(features) == len(frame) and np.array_equal(ages, frame.real_age.to_numpy(np.float32))
    assert np.isfinite(features).all()
    return features, ages
train_features, train_ages = extract_features(training_data, train_frame, "train")
val_features, val_ages = extract_features(validation_data, val_frame, "validation")
print("Cached vector shapes:", train_features.shape, val_features.shape)
```

**Question / minimal evidence:** What do later head-training epochs avoid, and why does this cache require a frozen backbone?


## [M01] A single linear regression output

The head trains 2048 weights and one bias: 2049 parameters. It has no softmax and returns a real-valued number interpreted in years. Zero kernels and a training-median bias initially reproduce the baseline. The backbone remains fixed. Later negative/unusual predictions are not silently clipped.

```python
keras.utils.set_random_seed(SEED)
head_input = keras.Input(shape=(2048,))
head_output = layers.Dense(1, name="age_output", kernel_initializer="zeros",
    bias_initializer=keras.initializers.Constant(training_median))(head_input)
age_head = keras.Model(head_input, head_output, name="age_head")
age_head.compile(optimizer=keras.optimizers.Adam(1e-3), loss="mae", metrics=["mae"])
initial_predictions = age_head(val_features[:8], training=False).numpy().reshape(-1)
print("Head parameters:", age_head.count_params())
print("Initial predictions:", initial_predictions)
print("Matches training median:", np.allclose(initial_predictions, training_median))
assert age_head.count_params() == 2049 and np.allclose(initial_predictions, training_median)
```

**Question / minimal evidence:** Why one output instead of 1000 ImageNet outputs, and which parameters train?


## [M02] Train the small head

Run up to 20 short epochs on cached vectors. from_tensor_slices now pairs vectors and labels rather than decoding images. EarlyStopping stops after three epochs without improvement; the checkpoint stores the lowest val_mae. Wait for fit to finish. A fresh experiment starts at M01, not another 20 epochs on an already trained head.

```python
head_train_data = tf.data.Dataset.from_tensor_slices((train_features, train_ages)).shuffle(len(train_ages), seed=SEED).batch(BATCH).with_options(options)
head_val_data = tf.data.Dataset.from_tensor_slices((val_features, val_ages)).batch(BATCH).with_options(options)
head_path = work / "age_head_best.weights.h5"
history = age_head.fit(head_train_data, validation_data=head_val_data, epochs=20, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(head_path), monitor="val_mae", mode="min", save_best_only=True, save_weights_only=True),
               keras.callbacks.EarlyStopping(monitor="val_mae", mode="min", patience=3)])
(work / "head_history.json").write_text(json.dumps(history.history, indent=2))
print("Best validation epoch:", int(np.argmin(history.history["val_mae"])) + 1)
```

**Question / minimal evidence:** How did train/val MAE behave over your final two epochs?


## [M03] Evaluate the restored best state

load_weights restores the head with minimum validation MAE, then we evaluate validation again. This can differ from the final epoch. The baseline is a reference rather than a mandatory score to beat. No test information is involved in checkpoint selection.

```python
age_head.load_weights(head_path)
after_digest = hashlib.sha256()
for variable in feature_extractor.weights:
    after_digest.update(variable.numpy().tobytes())
assert after_digest.hexdigest() == extractor_hash
print("All backbone weights unchanged:", True)
validation_metrics = age_head.evaluate(head_val_data, verbose=0, return_dict=True)
validation_metrics = {key: float(value) for key, value in validation_metrics.items()}
selection = {"best_epoch": int(np.argmin(history.history["val_mae"])) + 1,
             "validation": validation_metrics, "baseline_validation_mae": baseline_validation_mae}
(work / "selection.json").write_text(json.dumps(selection, indent=2))
print("Restored validation:", validation_metrics, "Baseline:", baseline_validation_mae)
fig, axis = plt.subplots(figsize=(8, 3))
axis.plot(range(1, len(history.history["mae"]) + 1), history.history["mae"], label="Train MAE")
axis.plot(range(1, len(history.history["val_mae"]) + 1), history.history["val_mae"], label="Validation MAE")
axis.axhline(baseline_validation_mae, linestyle="--", color="gray", label="Median baseline validation")
axis.set(xlabel="Epoch", ylabel="MAE (years)"); axis.legend(); plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** Is your restored validation MAE lower or higher than the baseline?


## [V01] Final test and individual errors

The best head is fixed. Now extract test features and evaluate CNN/median on the final test. Positive signed_error means prediction exceeds label. Verify cache order and attach errors to file IDs. Do not retrain or reselect checkpoints from test results.

```python
test_features, test_ages = extract_features(test_data, test_frame, "test")
head_test_data = tf.data.Dataset.from_tensor_slices((test_features, test_ages)).batch(BATCH).with_options(options)
test_metrics = {k: float(v) for k, v in age_head.evaluate(head_test_data, verbose=0, return_dict=True).items()}
age_predictions = np.concatenate([age_head(test_features[start:start+BATCH], training=False).numpy().reshape(-1)
                                  for start in range(0, len(test_features), BATCH)])
errors = test_frame[["file_name", "real_age", "age_group"]].copy()
errors["prediction"] = age_predictions
errors["signed_error"] = errors.prediction - errors.real_age
errors["absolute_error"] = errors.signed_error.abs()
baseline_test_mae = float(np.abs(test_ages - training_median).mean())
assert np.isclose(errors.absolute_error.mean(), test_metrics["mae"], atol=1e-4)
errors.to_csv(work / "test_errors.csv", index=False)
print("CNN test:", test_metrics, "Median baseline test MAE:", baseline_test_mae)
print("Negative predictions:", int((age_predictions < 0).sum()))
print(errors.head().to_string(index=False))
```

**Question / minimal evidence:** How does CNN test MAE differ from the baseline in your run?


## [V02] Group errors and sample counts

Groups were fixed before splitting rather than chosen from test results. Each group reports n, MAE and mean signed error together. Small n can produce unstable comparisons. This is descriptive test analysis, not a fairness certification.

```python
group_errors = errors.groupby("age_group", observed=False).agg(
    n=("absolute_error", "size"), mae=("absolute_error", "mean"), mean_signed_error=("signed_error", "mean"))
print(group_errors.to_string())
group_errors.to_csv(work / "age_group_errors.csv")
fig, axis = plt.subplots(figsize=(7, 3))
axis.bar(group_errors.index.astype(str), group_errors.mae, color="#6c5bb4")
axis.set(xlabel="Fixed age-label group", ylabel="Test MAE (years)"); plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** Which group has the fewest samples, and why interpret its average more cautiously?


## [V03] Actual samples with small and large errors

The supplied code displays the smallest- and largest-absolute-error test samples. Labels come from the dataset, not a tutor’s age guess from appearance. Describe only what is actually observed. A possible explanation does not establish what the training set generally looks like.

```python
example_indices = [int(errors.absolute_error.idxmin()), int(errors.absolute_error.idxmax())]
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
for axis, index in zip(axes, example_indices):
    row = errors.loc[index]
    image = load_rgb(image_dir / row.file_name).numpy()
    axis.imshow(image.astype(np.uint8)); axis.axis("off")
    axis.set_title(f"Dataset label: {row.real_age:.1f}\nPrediction: {row.prediction:.1f}; abs error: {row.absolute_error:.1f}", fontsize=10)
    print(row[["file_name", "real_age", "prediction", "absolute_error"]].to_dict())
plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** What can you actually observe in the high-error image, and what remains a hypothesis?


## [X01] A regression contribution map

The linear age head weights the same 2048 channels for one scalar. Signed-map mean plus bias equals the output. Positive contributions increase the model’s number; they are not a facial region’s real age. Agreement verifies computation rather than accuracy or causality. This is neither an age-class CAM nor Grad-CAM.

```python
index = example_indices[1]
image = load_rgb(image_dir / errors.loc[index, "file_name"]).numpy()
spatial = feature_extractor(prepare_batch(image), training=False).numpy()[0]
regression_kernel, regression_bias = age_head.get_layer("age_output").get_weights()
regression_map = np.tensordot(spatial, regression_kernel[:, 0], axes=([-1], [0]))
reconstructed_age = float(regression_map.mean() + regression_bias[0])
image_prediction = float(age_head(gap(tf.convert_to_tensor(spatial[None])), training=False).numpy()[0, 0])
print("Map mean:", float(regression_map.mean()), "Bias:", float(regression_bias[0]))
print("Reconstructed/image/cache predictions:", reconstructed_age, image_prediction, float(age_predictions[index]))
assert np.isclose(reconstructed_age, image_prediction, atol=2e-3, rtol=1e-4)
assert np.isclose(image_prediction, age_predictions[index], atol=2e-3, rtol=1e-4)
fig, axis = plt.subplots(figsize=(6, 4))
plot = draw_signed(axis, image, regression_map, "Regression contribution (not a class)", max(float(np.abs(regression_map).max()), 1e-8))
fig.colorbar(plot, ax=axis, label="Signed contribution to prediction"); plt.tight_layout(); plt.show()
```

**Question / minimal evidence:** What does a positive contribution mean, and why must the bias be retained?


## [Z01] Three final connections

The tutor asks these three questions in separate messages. No new code; a short correct answer suffices.

**Question / minimal evidence:** 1. How does a class logit differ from the regression scalar?
2. Why is MAE not a±error bound?
3. What can a visually compelling contribution map not establish on its own?


## [Z02] Personal summary, no submission

The supplied code writes a local results.json summary as a personal artifact, not a submission. You may save your notebook for yourself; no upload, sharing, filename or proof of saving is required. Finish after your own takeaway.

```python
summary = {"seed": SEED, "tensorflow": tf.__version__, "split": "custom stratified 60/20/20; not official APPA-REAL",
           "sizes": {"train": len(train_frame), "validation": len(val_frame), "test": len(test_frame)},
           "trainable_head_parameters": age_head.count_params(), "selection": selection,
           "cnn_test": test_metrics, "baseline_test_mae": baseline_test_mae,
           "group_errors": group_errors.reset_index().to_dict(orient="records"), "cam": cam_results,
           "limits": "MAE is not an individual bound; heatmaps are not causal evidence or age-eligibility verification."}
(work / "results.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
```

**Question / minimal evidence:** What was your main takeaway from your own results?
