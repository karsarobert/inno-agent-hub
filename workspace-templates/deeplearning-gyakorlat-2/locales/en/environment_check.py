"""Run this program before class inside the activated virtual environment."""

import os
import sys
import importlib
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

print("Python:", sys.version.split()[0])
print("Python executable:", sys.executable)
missing = []
for name in ["numpy", "pandas", "sklearn", "matplotlib", "tensorflow", "keras"]:
    try:
        module = importlib.import_module(name)
        print(name + ":", module.__version__)
    except ImportError as error:
        missing.append(name)
        print(name + " cannot be imported:", error)

data_file = Path(__file__).resolve().parent / "data" / "red-wine.csv"
print("Local data file:", "found" if data_file.is_file() else "MISSING")
if missing or not data_file.is_file():
    print("Check the installation steps in START-HERE.md.")
    raise SystemExit(1)

import tensorflow as tf
result = tf.reduce_sum(tf.constant([1.0, 2.0, 3.0]))
print("TensorFlow test calculation:", float(result))
print("Environment check successful. The exercise runs on CPU.")
