"""One input → one hidden ReLU layer → one continuous prediction. CPU training."""
from time import perf_counter
from cpu_environment import keras, layers, new_training_run, make_datasets, BriefProgress
from helpers import new_run_folder
from network_helpers import regression_data, initial_weight_id, save_network_results

# SETTINGS – first run: 8 units, 120 epochs.
HIDDEN_UNITS = 8
EPOCHS = 120
LEARNING_RATE = 0.01
BATCH_SIZE = 16
RANDOM_SEED = 42

if not 1 <= HIDDEN_UNITS <= 128 or not 1 <= EPOCHS <= 1000:
    raise SystemExit("Use 1–128 hidden units and 1–1000 epochs in this lab.")
new_training_run(RANDOM_SEED)
train_x, train_y, val_x, val_y = regression_data()
training_data, validation_data = make_datasets(
    train_x, train_y, val_x, val_y, BATCH_SIZE, RANDOM_SEED)

# MODEL – each sample has one x value.
model = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(HIDDEN_UNITS, activation="relu"),
    layers.Dense(1),
])
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
identifier = initial_weight_id(model)
print(f"Starting CPU training: 1 → {HIDDEN_UNITS} → 1; {EPOCHS} epochs.", flush=True)
print(f"Initial weight ID: {identifier}", flush=True)

# TRAINING – each epoch contains 64/16 = 4 training batches.
start_time = perf_counter()
history = model.fit(
    training_data,
    validation_data=validation_data,
    epochs=EPOCHS,
    shuffle=False,  # The prepared dataset already shuffles the training samples.
    verbose=0,
    callbacks=[BriefProgress(EPOCHS)],
)

# PREPARED MEASUREMENT AND PLOTTING – no additional training.
folder = new_run_folder(__file__)
save_network_results(folder, model, history,
            (train_x, train_y, val_x, val_y),
            {"hidden_units": HIDDEN_UNITS, "epochs": EPOCHS,
             "learning_rate": LEARNING_RATE, "batch_size": BATCH_SIZE,
             "random_seed": RANDOM_SEED, "l2_strength": 0.0,
             "initial_weights": identifier}, start_time)
