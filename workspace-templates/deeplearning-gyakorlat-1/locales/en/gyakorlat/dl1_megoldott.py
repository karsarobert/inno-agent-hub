# -*- coding: utf-8 -*-
"""
DL 1 practice - Introduction: history of neural networks, fundamentals of machine learning
============================================================================================
A simple MNIST digit classifier (NO curve analysis - overfitting is discussed
later, at point 4 of the syllabus).

Original source: pte_dl1_2.py (Colab notebook). Extended with TF 2.x (keras 3)
imports and an environment-independent (Colab + local) GPU check.

How to run: cell by cell with the teacher, as the code demo of session 1.
"""

import numpy as np

# ----------------------------------------------------------------------
# 0. ENVIRONMENT / IMPORTS
# ----------------------------------------------------------------------
# On Colab, enable the GPU: Runtime -> Change runtime type -> GPU
# ===================== COLAB ONLY ==========================
# !nvidia-smi
# ===========================================================

import tensorflow as tf
from tensorflow import keras

# ===================== LOCAL ONLY ==========================
# print(tf.config.list_physical_devices('GPU'))  # empty list = no GPU, CPU is fine
# ===========================================================

print("TensorFlow version:", tf.__version__)

# ----------------------------------------------------------------------
# 1. LOADING THE DATA
# ----------------------------------------------------------------------
# MNIST: 60000 training + 10000 test ~ 28x28 greyscale (digits)
mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print("X_train shape:", X_train.shape)   # (60000, 28, 28)
print("X_test  shape:", X_test.shape)    # (10000, 28, 28)


# ----------------------------------------------------------------------
# 2. LOOKING AT THE DATA  (matplotlib display)
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

# Every image is a 28x28 matrix -> pixel values in the 0-255 range
print("First 8x8 pixels of one image:")
print(X_train[0][:8, :8])


# ----------------------------------------------------------------------
# 3. RESHAPING: 28x28 image -> 784-long vector
# ----------------------------------------------------------------------
# X_train: (60000, 28, 28) -> (60000, 784)
# The -1 means: the size of that dimension is inferred by TensorFlow
RESHAPED = 784
X_train = X_train.reshape(60000, RESHAPED)
X_test  = X_test.reshape(10000, RESHAPED)

# whole (int) numbers -> decimal (float32) numbers, so the model computes well
X_train = X_train.astype('float32')
X_test  = X_test.astype('float32')

print("X_train after reshape:", X_train.shape)
print("One image as a vector (first 10 values):", X_train[0][:10])


# ----------------------------------------------------------------------
# 4. NORMALIZATION: 0-255 -> 0.0-1.0
# ----------------------------------------------------------------------
# Normalization matters because the model learns more stably from smaller,
# uniformly scaled numbers.
X_train /= 255
X_test  /= 255

print(X_train.shape[0], 'training samples')
print(X_test.shape[0],  'test samples')
print("Maximum pixel value after normalization:", X_train.max())   # should be 1.0


# ----------------------------------------------------------------------
# 5. ONE-HOT ENCODING
# ----------------------------------------------------------------------
# The label (e.g. 7) becomes a vector: [0,0,0,0,0,0,0,1,0,0]
# This way the output of the classification is directly usable.
print("Y_test[0] (original label):", Y_test[0])

NB_CLASSES = 10
Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test  = tf.keras.utils.to_categorical(Y_test,  NB_CLASSES)

print("Y_test[0] (one-hot vector):", Y_test[0])


# ----------------------------------------------------------------------
# 6. BUILDING THE MODEL
# ----------------------------------------------------------------------
# Sequential = layers one after another.
# Dense(10, softmax): 10 neurons (one per digit), softmax activation
#   -> the output gives the probabilities of the 10 classes (sum = 1).
model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(NB_CLASSES,
                             input_shape=(RESHAPED,),
                             name='dense_layer',
                             activation='softmax'))

# Print the parameters: how many weights are in the network
model.summary()


# ----------------------------------------------------------------------
# 7. COMPILING THE MODEL (compile)
# ----------------------------------------------------------------------
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# ----------------------------------------------------------------------
# 8. TRAINING THE MODEL (fit)
# ----------------------------------------------------------------------
EPOCHS = 5          # number of epochs (a few is enough here: just a demo)
BATCH_SIZE = 128    # batch size

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    verbose=1,
                    validation_data=(X_test, Y_test))
# epochs: how many times the model goes through the whole dataset
# batch_size: how many samples per "step"; the weights are updated

# We simply read the outcome from the final accuracy
final_acc = history.history['val_accuracy'][-1]
print(f"\nFinal test accuracy (session 1, demo): {final_acc:.4f}")

print("\nDone. You now understand the main steps: data -> reshape -> normalize ->",
      "one-hot -> model -> training.")
print("Overfitting and curve analysis come in later sessions.")
