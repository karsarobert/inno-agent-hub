# -*- coding: utf-8 -*-
"""
ORA ZARO FELADAT - egyszeru MNIST-osztalyozo (1. alkalom)
========================================================
Cél: készíts a demó alapján egy egyszeru, rejtett réteg NELKÜLI osztályozót,
és írasd ki a vegso (teszt) pontosságot. Görbét NEM kell rajzolni.

Ez a fájl váz; a "TODO" jelölésekre írd be a hiányzó részeket, majd futtasd.
A kurzusszervezo feladat szerint ez a demó már fél úton van: hasonlítsd össze
a mentor által látott, rejtett réteg nélküli pontossággal.
"""

import tensorflow as tf
from tensorflow import keras

# --- adatok betöltése és előkészítése (ugyanaz, mint a gyakorlaton) ---
mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

RESHAPED = 784
NB_CLASSES = 10

X_train = X_train.reshape(60000, RESHAPED)
X_test  = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32') / 255
X_test  = X_test.astype('float32') / 255

Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test  = tf.keras.utils.to_categorical(Y_test,  NB_CLASSES)

# --- Egyszeru modell (rejtett réteg nélkül) ---
model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(NB_CLASSES,
                             input_shape=(RESHAPED,),
                             activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# EPOCHS: hany korszak? (pl. 5, ahogy a demóban)
EPOCHS = 5
BATCH_SIZE = 128

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    verbose=1,
                    validation_data=(X_test, Y_test))

# a tanulás mértekét az utolso validacios pontosságból olvasd ki
final_acc = history.history['val_accuracy'][-1]
print(f"\nVegso teszt-pontossag: {final_acc:.4f}")

# --- kérdés megválaszolásához ---
# 1) Hány paramétere lett ennek a hálónak a summary alapján? (10 osztaly + biasyk)
# 2) Mit jelent itt a "tanítás"? (mi történt a fit alatt)
# 3) A túltanulás kérdését most miért nem elemezzük? (a tematikában később lesz)