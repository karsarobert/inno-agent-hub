"""Train an autoencoder to reconstruct its normal ECG input signal.
Input: 512 normal training signals and 128 separate normal validation signals.
Output: reconstruction.png, learning_curves.png and measured MAE values.
Change number_of_epochs (10 to 30). Every Run trains a new model.
The 30-epoch run also compares against a matching 10-epoch run of your own.
"""
from time import perf_counter
import hashlib
from cpu_environment import keras, layers, start_training, make_batches, BriefProgress
from helpers import load_data, new_run_folder, save_training_results

# 1. SETTINGS: one epoch is one pass through the entire training set.
number_of_epochs = 10
bottleneck_size = 8  # Change this only in the optional experiment.

# Ready-made validation and a fixed starting point; no edits needed here.
if not isinstance(number_of_epochs, int) or not 1 <= number_of_epochs <= 100:
    raise SystemExit('number_of_epochs must be an integer between 1 and 100.')
if not isinstance(bottleneck_size, int) or not 1 <= bottleneck_size <= 32:
    raise SystemExit('bottleneck_size must be an integer between 1 and 32.')
start_training(42)

# 2. LOAD DATA: both groups contain normal signals only.
# Validation signals do not participate in weight updates.
data = load_data()
training_signals = data['training_signals']
validation_signals = data['validation_signals']

# 3. INPUT-TARGET PAIRS: the desired output is the input signal itself.
# This is why the same array appears twice. The helper creates batches of 32.
# 512 signals / 32 signals per batch = 16 weight updates per epoch.
training_batches = make_batches(training_signals, training_signals, shuffle=True)
validation_batches = make_batches(validation_signals, validation_signals)

# 4. THE COMPLETE NETWORK: reconstruct 140 values from 8 internal values.
model = keras.Sequential([
    keras.Input(shape=(140,)),  # One input is a signal containing 140 values.
    # Encoder: gradually reduce the size of the internal representation.
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    # Bottleneck: learned internal values, not selected ECG sample points.
    layers.Dense(bottleneck_size, activation='relu', kernel_initializer='he_normal'),
    # Decoder: reconstruct the waveform from the internal representation.
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    # The 140 outputs are amplitudes between 0 and 1, not class probabilities.
    layers.Dense(140, activation='sigmoid'),
])

# 5. TRAINING: compile configures training; fit actually updates the weights.
# MAE is the mean absolute difference between the original and reconstructed signal.
model.compile(optimizer='adam', loss='mae', jit_compile=False)
# Technical identifier: do the two compared runs start with the same weights?
identifier = hashlib.sha256(b''.join(w.tobytes() for w in model.get_weights())).hexdigest()[:16]
print(f'CPU training starts: 512 normal training signals, 128 normal validation signals; {number_of_epochs} epochs.', flush=True)
print(f'Initial weights identifier: {identifier}', flush=True)
start = perf_counter()
history = model.fit(
    training_batches,
    validation_data=validation_batches,  # Evaluation only, without weight updates.
    epochs=number_of_epochs,
    shuffle=False,  # The training dataset already handles shuffling.
    verbose=0,  # The callback prints brief progress instead of a long log.
    callbacks=[BriefProgress()],
)
seconds = perf_counter() - start

# 6. EVALUATION AND FIGURES: reconstruct using the final weights; no new training.
# The helper saves curves, numbers and the reconstructions from your own run.
folder = new_run_folder(__file__)
save_training_results(folder, model, history, data,
                      {'epochs': number_of_epochs, 'bottleneck_size': bottleneck_size,
                       'initial_weights': identifier, 'random_seed': 42, 'batch_size': 32}, seconds)
