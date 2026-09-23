"""Training a single linear neuron: synthetic score from learning time.
The gradient steps of the weight and the bias are computed with NumPy.
The plotting is ready.
"""
from helpers import (np, regression_data, new_run_dir, save_curves,
                     regression_figure, save_json, refresh_view)

LEARNING_RATE = 0.02
EPOCHS = 120
weight = 1.0
bias = 1.0

train_x, val_x, train_y, val_y = regression_data()
history = {'loss': [], 'val_loss': []}
print('One input -> one linear neuron: prediction = weight x time + bias.')
print('80 training samples, 20 validation samples; synthetic teaching data.')

# THE STUDENT INTERPRETS THIS PART: one epoch here is one full batch.
for epoch in range(EPOCHS):
    prediction = weight * train_x + bias
    error = prediction - train_y
    weight_gradient = np.mean(error * train_x)
    bias_gradient = np.mean(error)
    weight = weight - LEARNING_RATE * weight_gradient
    bias = bias - LEARNING_RATE * bias_gradient
    # L = MSE / 2, so there is no separate factor of 2 in the gradient.
    train_loss = np.mean((weight * train_x + bias - train_y) ** 2) / 2
    val_loss = np.mean((weight * val_x + bias - val_y) ** 2) / 2
    if not np.isfinite(train_loss) or not np.isfinite(val_loss):
        raise SystemExit('The loss is not finite. Check the learning rate with '
                         'Inno\'s help!')
    history['loss'].append(float(train_loss))
    history['val_loss'].append(float(val_loss))

# PREPARED EVALUATION - you do not need to write or modify this.
# The folder name gets a short label (G01_gradient), not a long timestamp.
run_dir = new_run_dir(__file__, 'G01_gradient')
save_curves(run_dir, history)
regression_figure(run_dir, train_x, train_y, val_x, val_y, weight, bias)
save_json(run_dir / 'settings.json', {
    'learning_rate': LEARNING_RATE, 'epochs': EPOCHS,
    'weight': float(weight), 'bias': float(bias),
    'loss_type': 'MSE / 2', 'val_loss': history['val_loss'][-1]})
print(f'Weight: {weight:.4f}; bias: {bias:.4f}; validation MSE/2: '
      f'{history["val_loss"][-1]:.4f}')
print(f'Learning rate: {LEARNING_RATE}; epochs: {EPOCHS}')
refresh_view(run_dir)
