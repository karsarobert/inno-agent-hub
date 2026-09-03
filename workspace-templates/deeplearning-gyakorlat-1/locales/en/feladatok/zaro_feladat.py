# -*- coding: utf-8 -*-
"""
IN-CLASS CLOSING TASK - a simple MNIST classifier (session 1)
=============================================================
Goal: build a simple classifier WITHOUT a hidden layer, based on the demo,
and print the final (test) accuracy. No plots are needed.

This file is a working starting point; run it, then answer the three
questions at the end of the file. According to the course organiser's brief
this demo is already halfway there: compare it with the hidden-layer-free
accuracy shown by the mentor.
"""

import tensorflow as tf
from tensorflow import keras

# --- load and prepare the data (same as in the lab) ---
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

# --- simple model (no hidden layer) ---
model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(NB_CLASSES,
                             input_shape=(RESHAPED,),
                             activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# EPOCHS: how many epochs? (e.g. 5, as in the demo)
EPOCHS = 5
BATCH_SIZE = 128

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    verbose=1,
                    validation_data=(X_test, Y_test))

# read the outcome from the last validation accuracy
final_acc = history.history['val_accuracy'][-1]
print(f"\nFinal test accuracy: {final_acc:.4f}")

# --- to answer the questions ---
# 1) How many parameters does this network have according to summary? (10 classes + biases)
# 2) What does "training" mean here? (what happened during fit)
# 3) Why do we not analyse overfitting now? (it is a later topic)
