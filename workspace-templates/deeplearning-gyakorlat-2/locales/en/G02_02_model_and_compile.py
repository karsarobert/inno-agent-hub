"""Exercise 2 / Part 2: build and compile the neural network.

Learning goal:
- connect the 11 prepared input features to the input shape,
- understand the 11 -> 32 -> 16 -> 1 architecture,
- understand what Dense and ReLU mean at a high level,
- understand what compile() configures,
- understand that compile() does NOT train the model.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers

print("PART 2 – BUILD AND COMPILE THE NETWORK")
print("Goal: turn the prepared data shape into a Keras neural-network architecture.\n")

RANDOM_SEED = 42
LEARNING_RATE = 0.003
DATA_FILE = Path(__file__).resolve().parent / "data" / "red-wine.csv"

# -----------------------------------------------------------------------------
# 1. DATA PREPARATION – ALREADY FAMILIAR FROM PART 1
# -----------------------------------------------------------------------------
# Do not re-learn every line here. The important result is:
# train_scaled contains rows of wines, with 11 scaled input values per row.
data = pd.read_csv(DATA_FILE).drop_duplicates().reset_index(drop=True)
features = data.drop(columns=["quality"])
target = data["quality"]

train_pool, test_features, train_pool_target, test_target = train_test_split(
    features, target, test_size=0.20, random_state=RANDOM_SEED
)
train_features, validation_features, train_target, validation_target = train_test_split(
    train_pool, train_pool_target, test_size=0.25, random_state=RANDOM_SEED
)

scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(train_features).astype("float32")
validation_scaled = scaler.transform(validation_features).astype("float32")
test_scaled = scaler.transform(test_features).astype("float32")

print("Prepared training input shape:", train_scaled.shape)
print("One row therefore contains", train_scaled.shape[1], "input values.\n")

# -----------------------------------------------------------------------------
# 2. BUILD THE NEURAL NETWORK
# -----------------------------------------------------------------------------
# Sequential means that data flows through the layers in this order.
# Input(shape=(11,)) says: one sample contains 11 input features.
# Dense(32) creates a fully connected layer with 32 neurons.
# Dense(16) creates another hidden layer with 16 neurons.
# Dense(1) produces one number: the predicted wine quality.
keras.utils.set_random_seed(RANDOM_SEED)

model = keras.Sequential([
    keras.Input(shape=(train_scaled.shape[1],)),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),
])

print("2) NETWORK ARCHITECTURE")
print("Data flow: 11 inputs -> 32 neurons -> 16 neurons -> 1 output")
print("The final output is one predicted quality value.\n")
model.summary()
print()

# -----------------------------------------------------------------------------
# 3. COMPILE THE MODEL
# -----------------------------------------------------------------------------
# compile() prepares the model for training.
# It answers three practical questions:
#   optimizer: HOW should the weights be updated?
#   loss:      WHAT error should training try to reduce?
#   metrics:   WHAT additional value should we report while evaluating?
#
# Adam is the optimization algorithm used here.
# MAE = mean absolute error. Smaller is better.
# The learning rate controls the size of weight updates.
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=["mae"],
)

print("3) COMPILE")
print("Optimizer: Adam")
print("Learning rate:", LEARNING_RATE)
print("Loss: MAE (mean absolute error)")
print("Metric: MAE")
print()
print("IMPORTANT: compile() configured the learning process, but no training happened yet.")
print("fit() will start the actual training in Part 3.")
