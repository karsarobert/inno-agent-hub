"""Az előző kis hálózat Keras-rétegekkel.

A bemenet itt az eredeti [1, 2, -1], másik fájl módosítása nem kerül át ide.
A set_weights kézzel állítja be a paramétereket; a predict becslést készít.
Nincs tanítás. A Keras kernel oszlopai tartoznak az egyes neuronokhoz.
Részletes kódbemutatás: PROGRAM_BEMUTATOK.md.
Szemléltetés: szemlelteto.html (böngészőben megnyitható).
"""

import os

# Az alapgyakorlat CPU-n fut. Ezek az import előtti futtatási beállítások.
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Kerasban egy sor egy minta: itt 1 minta és 3 jellemző szerepel.
print('Az előző kis hálózat Keras-rétegekkel.')
print('A bemenet itt az eredeti [1, 2, -1], másik fájl módosítása nem kerül át ide.\nA set_weights kézzel állítja be a paramétereket; a predict becslést készít.\nNincs tanítás. A Keras kernel oszlopai tartoznak az egyes neuronokhoz.')

bemenetek = np.array([[1.0, 2.0, -1.0]], dtype=np.float32)
modell = keras.Sequential([
    keras.Input(shape=(3,)),
    layers.Dense(2, activation="relu", name="rejtett"),
    layers.Dense(1, name="kimenet"),
])

# A Keras kernel alakja: (bemenetek száma, neuronok száma).
# Ez a G02_02 súlymátrixainak transzponált elrendezése.
modell.layers[0].set_weights([
    np.array([[1.0, -0.5], [-1.0, 1.0], [0.5, 1.0]], dtype=np.float32),
    np.array([0.0, -1.0], dtype=np.float32),
])
modell.layers[1].set_weights([
    np.array([[2.0], [-1.0]], dtype=np.float32),
    np.array([0.5], dtype=np.float32),
])

modell.summary()
print("Aktualis bemenetek:", bemenetek)
print("Rejtett kernel (oszloponkent egy neuron):", modell.layers[0].get_weights()[0])
print("Rejtett biasok:", modell.layers[0].get_weights()[1])
becslesek = modell.predict(bemenetek, verbose=0)
print("Bemeneti adatok alakja:", bemenetek.shape)
print("Becslesek alakja:", becslesek.shape)
print("Parameterek szama:", modell.count_params())
print(f"Vegso becsles: {becslesek[0, 0]:.4f}")
print("Ebben a programban nincs tanitas; a sulyokat mi adtuk meg.")
