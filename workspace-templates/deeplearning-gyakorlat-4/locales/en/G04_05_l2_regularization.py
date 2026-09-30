"""L2 experiment with the 64-unit network. Both Dense kernels are penalized."""
from time import perf_counter
from cpu_environment import keras, layers, regularizers, new_training_run, make_datasets, BriefProgress
from helpers import new_run_folder
from network_helpers import regression_data, initial_weight_id, save_network_results

# SETTINGS – this file also runs independently.
L2_STRENGTH = 0.0
HIDDEN_UNITS = 64
EPOCHS = 120
LEARNING_RATE = 0.01
BATCH_SIZE = 16
RANDOM_SEED = 42

if not 0 <= L2_STRENGTH <= 1:
    raise SystemExit("L2 strength must be between 0 and 1 in this example.")
new_training_run(RANDOM_SEED)
train_x, train_y, val_x, val_y = regression_data()
training_data, validation_data = make_datasets(
    train_x, train_y, val_x, val_y, BATCH_SIZE, RANDOM_SEED)

# MODEL – the same network; the weight penalty changes.
model = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(HIDDEN_UNITS, activation="relu",
                 kernel_regularizer=regularizers.l2(L2_STRENGTH)),
    layers.Dense(1, kernel_regularizer=regularizers.l2(L2_STRENGTH)),
])
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
identifier = initial_weight_id(model)
print(f"Starting CPU L2 experiment: λ={L2_STRENGTH}; {EPOCHS} epochs.", flush=True)
print(f"Initial weight ID: {identifier}", flush=True)
start_time = perf_counter()
history = model.fit(
    training_data,
    validation_data=validation_data,
    epochs=EPOCHS,
    shuffle=False,  # The prepared dataset already shuffles the training samples.
    verbose=0,
    callbacks=[BriefProgress(EPOCHS)],
)

folder = new_run_folder(__file__)
save_network_results(folder, model, history,
            (train_x, train_y, val_x, val_y),
            {"hidden_units": HIDDEN_UNITS, "epochs": EPOCHS,
             "learning_rate": LEARNING_RATE, "batch_size": BATCH_SIZE,
             "random_seed": RANDOM_SEED, "l2_strength": L2_STRENGTH,
             "initial_weights": identifier}, start_time)
