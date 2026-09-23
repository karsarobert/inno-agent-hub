"""Classifying spiral points with a ReLU hidden layer.
Input: two coordinates. Target: class 0, 1 or 2.
The student focuses on the MODEL, SETTINGS and TRAINING blocks.
"""
from helpers import (check_packages, spiral_data, new_run_dir, save_spiral_run,
                     run_label)
check_packages(['tensorflow'])
from tensorflow import keras
from tensorflow.keras import layers

# SETTINGS - change only one factor at a time.
# R2: 16 neurons, rate 0.01. R3: 50-50 neurons, rate 0.01.
# R4: on the 50-50 network change ONLY the rate to 0.001; epoch and batch stay.
LEARNING_RATE = 0.01
EPOCHS = 150
BATCH_SIZE = 32
RANDOM_SEED = 42

# PREPARED DATA: 360 training, 120 validation, 120 test samples.
train_x, val_x, test_x, train_labels, val_labels, test_labels = spiral_data()
train_target = keras.utils.to_categorical(train_labels, num_classes=3)
val_target = keras.utils.to_categorical(val_labels, num_classes=3)
keras.utils.set_random_seed(RANDOM_SEED)

# MODEL - the student builds / modifies the network here.
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
model.summary()
print('Training / validation / test: 360 / 120 / 120 samples.')
print('Example label and one-hot shape:', train_labels[0], train_target[0])
print('Training starts. Wait for the run summary!')

# TRAINING - the weights change here. Validation is not a weight update.
history = model.fit(
    train_x, train_target,
    validation_data=(val_x, val_target),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    verbose=0,
)

# EVALUATION - the model does not learn any more here.
validation_result = model.evaluate(
    val_x, val_target, verbose=0, return_dict=True)
probabilities = model.predict(val_x[:5], verbose=0)
predicted_classes = probabilities.argmax(axis=1)
print('Five predicted classes:', predicted_classes)

# PREPARED FIGURES AND SAVING - you do not need to program these.
# The folder name gets the short label of the run from the actual model
# (R2_16n_, R3_50x2_lr0.01_, R4_50x2_lr0.001_); the name thus shows at a glance
# which run is which.
run_dir = new_run_dir(__file__, run_label(model, LEARNING_RATE))
settings = {
    'learning_rate': LEARNING_RATE, 'epochs': EPOCHS,
    'batch_size': BATCH_SIZE, 'random_seed': RANDOM_SEED,
    'validation': validation_result,
}
save_spiral_run(run_dir, model, history, settings, val_x,
                val_labels, test_x, test_labels)
