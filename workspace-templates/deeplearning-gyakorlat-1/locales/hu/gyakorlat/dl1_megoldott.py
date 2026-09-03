# -*- coding: utf-8 -*-
"""
DL 1. gyakorlat - Bevezetes: a neurális hálózatok története, gépi tanulás alapjai
=================================================================================
Egy egyszeru MNIST-szamjegyosztalo (görbe-elemzes NELKÜL - a túltanulast
kesobb, a tematika 4. pontjanal tárgyaljuk).

Eredeti forras: pte_dl1_2.py (Colab notebook). Kiegészítve TF 2.x (keras 3)
importtal es környezetfüggetlen (Colab + lokalis) GPU-ellenorzeshez.

Futtatas: cellanként a tanárral, az 1. alkalom kód-demo reszenként.
"""

import numpy as np

# ----------------------------------------------------------------------
# 0. KORNYEZET / IMPORT
# ----------------------------------------------------------------------
# Colab-ben futasnal engedélyezd a GPU-t: Runtime -> Change runtime type -> GPU
# ===================== COLAB-ON ERVENYES ==========================
# !nvidia-smi
# ================================================================

import tensorflow as tf
from tensorflow import keras

# ===================== LOKALIS ERVENYES ==========================
# print(tf.config.list_physical_devices('GPU'))  # ures lista = nincs GPU, CPU is jo
# ================================================================

print("TensorFlow verzio:", tf.__version__)

# ----------------------------------------------------------------------
# 1. ADATOK LETOLTESE
# ----------------------------------------------------------------------
# MNIST: 60000 tanulo + 10000 teszt ~ 28x28-as szurkeskalak (szamjegyek)
mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print("X_train shape:", X_train.shape)   # (60000, 28, 28)
print("X_test  shape:", X_test.shape)    # (10000, 28, 28)


# ----------------------------------------------------------------------
# 2. ADATOK ATNEZESE  (matplotlib megjelenites)
# ----------------------------------------------------------------------
import matplotlib.pyplot as plt

fig = plt.figure(0, figsize=(12, 10))
for i in range(9):
    fig.add_subplot(3, 3, i + 1)
    plt.imshow(X_train[i * 100, :, :], cmap='gray')
    plt.title(str(round(Y_train[i * 100], 3)), fontsize=24)
    plt.axis('off')
plt.tight_layout()
plt.show()

# Minden kep egy 28x28-as mátrix -> épp ertekei 0-255 terjedoben
print("Egy epit elso 8x8 pixele:")
print(X_train[0][:8, :8])


# ----------------------------------------------------------------------
# 3. ALASZABLAS: 28x28 kep -> 784 hosszu vektor
# ----------------------------------------------------------------------
# X_train: (60000, 28, 28) -> (60000, 784)
# A -1 azt jelenti: a kerete a meretet maga a TensorFlow
RESHAPED = 784
X_train = X_train.reshape(60000, RESHAPED)
X_test  = X_test.reshape(10000, RESHAPED)

# egész (int) szamok -> tizedes (float32) szamok, hogy a modell jol szamoljon
X_train = X_train.astype('float32')
X_test  = X_test.astype('float32')

print("X_train alakitas utan:", X_train.shape)
print("Egy kep vektor formaban (elso 10 ertek):", X_train[0][:10])


# ----------------------------------------------------------------------
# 4. NORMALIZALAS: 0-255 -> 0.0-1.0
# ----------------------------------------------------------------------
# A normalizalas azert fontos, mert a kisebb, egyseges tartomanyu szamokon
# a modell stabilabban tanul.
X_train /= 255
X_test  /= 255

print(X_train.shape[0], 'tanulo minta')
print(X_test.shape[0],  'teszt minta')
print("Maximalis pixel-ertek normalizalas utan:", X_train.max())   # 1.0 kell legyen


# ----------------------------------------------------------------------
# 5. ONE-HOT ENCODING
# ----------------------------------------------------------------------
# A címke (pl. 7) egy vektorra alakul: [0,0,0,0,0,0,0,1,0,0]
# Igy az osztályozás közvetlenül használható.
print("Y_test[0] (eredeti címke):", Y_test[0])

NB_CLASSES = 10
Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test  = tf.keras.utils.to_categorical(Y_test,  NB_CLASSES)

print("Y_test[0] (one-hot vektor):", Y_test[0])


# ----------------------------------------------------------------------
# 6. MODELL FELÉPÍTESE
# ----------------------------------------------------------------------
# Sequential = rétegek egymas után.
# Dense(10, softmax): 10 idegsejt (a 10 szamjegyhez), softmax aktivacio
#   -> a kimenet a 10 osztaly valoszinusegeit adja (osszeg = 1).
model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(NB_CLASSES,
                             input_shape=(RESHAPED,),
                             name='dense_layer',
                             activation='softmax'))

# Parameterek kiirása: hany suly van a halozatban
model.summary()


# ----------------------------------------------------------------------
# 7. MODELL FORDÍTASA (compile)
# ----------------------------------------------------------------------
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# ----------------------------------------------------------------------
# 8. MODELL TANÍTASA (fit)
# ----------------------------------------------------------------------
EPOCHS = 5          # korszakok szama (itt elég kevés: csak demo)
BATCH_SIZE = 128    # batch meret

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    verbose=1,
                    validation_data=(X_test, Y_test))
# epochs: hanyszor megy át a teljes adathalmazon
# batch_size: hany minta egy "lepesben"; a sulyok frissulnek

# A tanulás mértékét egyszerűen a végso pontossággal nezzuk meg
final_acc = history.history['val_accuracy'][-1]
print(f"\nVegso teszt-pontossag (elso alkalom, demo): {final_acc:.4f}")

print("\nVége. Most már érted a fő lépéseket: adat -> alakitas -> normalizalas ->",
      "-> one-hot -> modell -> tanítás.")
print("A túltanulast és a görbék elemzését a későbbi alkalmakon tanuljuk meg.")