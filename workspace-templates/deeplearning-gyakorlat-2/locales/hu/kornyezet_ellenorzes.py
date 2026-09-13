"""Ezt a programot az óra előtt futtasd az aktivált virtuális környezetben."""

import os
import sys
import importlib
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

print("Python:", sys.version.split()[0])
print("Python eleresi ut:", sys.executable)
hianyzo = []
for nev in ["numpy", "pandas", "sklearn", "matplotlib", "tensorflow", "keras"]:
    try:
        modul = importlib.import_module(nev)
        print(nev + ":", modul.__version__)
    except ImportError as hiba:
        hianyzo.append(nev)
        print(nev + " nem toltheto be:", hiba)

adatfajl = Path(__file__).resolve().parent / "adatok" / "red-wine.csv"
print("Helyi adatfajl:", "megvan" if adatfajl.is_file() else "HIANYZIK")
if hianyzo or not adatfajl.is_file():
    print("Ellenorizd a START-HERE.md telepitesi lepeseit.")
    raise SystemExit(1)

import tensorflow as tf
eredmeny = tf.reduce_sum(tf.constant([1.0, 2.0, 3.0]))
print("TensorFlow probaszamitas:", float(eredmeny))
print("A kornyezetellenorzes sikeres. A gyakorlat CPU-n fut.")
