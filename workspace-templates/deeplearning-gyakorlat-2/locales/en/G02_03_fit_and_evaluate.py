"""Exercise 2 / Part 3: train the neural network with fit().

Learning goal:
- understand what fit() receives,
- understand epoch, batch size and validation data,
- understand what History stores,
- connect the loss curve to the learning process,
- distinguish core neural-network code from support/plotting code.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers

print("PART 3 – TRAIN WITH fit()")
print("Goal: use the prepared data to train the network and inspect the learning history.\n")

RANDOM_SEED = 42
LEARNING_RATE = 0.003
EPOCHS = 40
BATCH_SIZE = 64
DATA_FILE = Path(__file__).resolve().parent / "data" / "red-wine.csv"

# =============================================================================
# A. DATA PREPARATION – ALREADY FAMILIAR
# =============================================================================
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

train_target = train_target.to_numpy(dtype="float32")
validation_target = validation_target.to_numpy(dtype="float32")
test_target = test_target.to_numpy(dtype="float32")

print("Training input shape:  ", train_scaled.shape)
print("Validation input shape:", validation_scaled.shape)
print("Test input shape:      ", test_scaled.shape)
print()

# =============================================================================
# B. MODEL + COMPILE – ALREADY FAMILIAR
# =============================================================================
keras.utils.set_random_seed(RANDOM_SEED)
model = keras.Sequential([
    keras.Input(shape=(train_scaled.shape[1],)),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1),
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=["mae"],
)

print("Network: 11 inputs -> 32 -> 16 -> 1 output")
print("Compiled with Adam and MAE.\n")

# =============================================================================
# C. TRAINING – THIS IS THE MAIN NEW PART
# =============================================================================
# fit() starts the actual learning process.
#
# train_scaled, train_target:
#   the input examples and their known correct answers.
#
# validation_data:
#   a separate set used to check how well the model works on data that is not
#   used to update the weights.
#
# epochs=40:
#   the model can go through the complete training set up to 40 times.
#
# batch_size=64:
#   training examples are processed in smaller groups of 64 before the next
#   weight update step.
#
# history:
#   fit() returns a History object. It remembers the loss/metrics after epochs.
print("STARTING TRAINING")
print("Epoch limit:", EPOCHS)
print("Batch size:", BATCH_SIZE)
print()

history = model.fit(
    train_scaled,
    train_target,
    validation_data=(validation_scaled, validation_target),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=2,
)

# =============================================================================
# D. EVALUATION AND A FEW PREDICTIONS
# =============================================================================
validation_result = model.evaluate(
    validation_scaled,
    validation_target,
    verbose=0,
    return_dict=True,
)

predictions = model.predict(validation_scaled[:5], verbose=0).reshape(-1)
comparison = pd.DataFrame({
    "known quality": validation_target[:5],
    "model prediction": predictions,
})

print("\nVALIDATION RESULT")
print(f"Validation MAE: {validation_result['mae']:.4f}")
print("Five examples:")
print(comparison.round(3).to_string(index=False))
print()
print("The test set is still untouched. We are not using it during model development.")

# =============================================================================
# E. SUPPORT CODE – YOU DO NOT NEED TO UNDERSTAND EVERY LINE YET
# =============================================================================
# The next block converts the History object into a small table and draws a
# figure. This is useful, but Matplotlib is NOT the learning goal of this class.
# Focus on what the graph means:
#   - training loss = error on training data,
#   - validation loss = error on validation data,
#   - lower MAE means smaller average prediction error.
curves = pd.DataFrame(history.history)
curves.insert(0, "epoch", range(1, len(curves) + 1))

run_name = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
results_dir = Path(__file__).resolve().parent / "results" / ("fit_" + run_name)
results_dir.mkdir(parents=True, exist_ok=False)

curves.to_csv(results_dir / "learning_history.csv", index=False)
comparison.to_csv(results_dir / "predictions.csv", index=False)

figure, axis = plt.subplots(figsize=(8, 4.5))
axis.plot(curves["epoch"], curves["loss"], label="Training loss")
axis.plot(curves["epoch"], curves["val_loss"], label="Validation loss")
axis.set(
    xlabel="Epoch",
    ylabel="MAE",
    title="Wine quality model – learning history",
)
axis.legend()
axis.grid(alpha=0.25)
figure.tight_layout()
figure.savefig(results_dir / "learning_curve.png", dpi=140)
plt.close(figure)

print("\nLEARNING HISTORY")
print("Completed epochs:", len(curves))
print(f"First training loss: {curves['loss'].iloc[0]:.4f}")
print(f"Last training loss:  {curves['loss'].iloc[-1]:.4f}")
print(f"First validation loss: {curves['val_loss'].iloc[0]:.4f}")
print(f"Last validation loss:  {curves['val_loss'].iloc[-1]:.4f}")
print()
print("Support code saved the learning curve here:")
print(results_dir / "learning_curve.png")
print()
print("MAIN PIPELINE:")
print("CSV -> X/y -> split -> scaling -> model -> compile() -> fit() -> validation -> history")
