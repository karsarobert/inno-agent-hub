# START-HERE — Getting started (read this first!)

## 1. Choose your environment

This lab runs in a **mixed environment**: Google Colab (cloud, GPU) or your own
machine (local). Pick the one you will use.

### A) Google Colab (recommended if you have no local setup yet)
1. Open [Colab](https://colab.research.google.com/).
2. Create a new notebook (**File → New notebook**).
3. Paste the content of `gyakorlat/dl1_megoldott.py` cell by cell, **or**
   upload/link the file.
4. Running the `!nvidia-smi` cell at the top of the notebook shows whether a
   GPU is available (`Runtime → Change runtime type → GPU`).

### B) Local environment (your own machine, e.g. PyCharm / VS Code)
- It is recommended to use a separate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install tensorflow numpy pandas matplotlib
```

- GPU check locally (the commented line at the top of `dl1_megoldott.py`):

```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

If you get an empty list, there is no GPU — **no problem**, the lab runs fine
on CPU too (maybe a bit slower).

## 2. How the lab proceeds

1. Open the **`gyakorlat/dl1_megoldott.py`** file and run it section by section,
   step by step with the teacher.
2. Meanwhile **`gyakorlat/dl1_atlathatoanyag.md`** summarises the key concepts
   on one page.
3. **`feladatok/zaro_feladat.py`** is the in-class closing task (classifier
   without a hidden layer).
4. At home, continue with **`feladatok/hazifeladat.md`**.

## 3. If you get stuck
- Check the TensorFlow version: `import tensorflow as tf; print(tf.__version__)`.
- Make sure the data is **normalized** (`X_train.max()` should be 1.0).
- The most common mistake is the **shape**. The safe recipe:

```python
# 28×28 image → 784-long vector (60000 samples)
X_train = X_train.reshape(60000, -1)
X_test  = X_test.reshape(10000, -1)

# integers (0-255) → decimals (0.0-1.0)
X_train = X_train.astype('float32') / 255
X_test  = X_test.astype('float32') / 255
```
