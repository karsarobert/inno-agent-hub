"""Prepared data generation, measurement and plotting for programs 4–5."""
import hashlib
from time import perf_counter
from helpers import np, plt, BLUE, ORANGE, TEAL, save_figure, save_data, finished


def regression_data():
    """Fixed 64 training and 128 validation samples. No test-set evaluation."""
    rng = np.random.default_rng(2026)
    x = rng.uniform(-3, 3, (192, 1)).astype("float32")
    y = (np.sin(1.5*x) + .3*x + rng.normal(0, .3, x.shape)).astype("float32")
    return x[:64], y[:64], x[64:], y[64:]


def initial_weight_id(model):
    buffer = b"".join(s.tobytes() for s in model.get_weights())
    return hashlib.sha256(buffer).hexdigest()[:16]


def save_network_results(folder, model, history, data, settings, start_time):
    train_x, train_y, val_x, val_y = data
    training_prediction = model(train_x, training=False).numpy()
    validation_prediction = model(val_x, training=False).numpy()
    training_mae = float(np.mean(np.abs(train_y-training_prediction)))
    validation_mae = float(np.mean(np.abs(val_y-validation_prediction)))
    penalty = sum(float(v.numpy()) for v in model.losses)
    sum_of_squares = sum(float(np.sum(r.kernel.numpy()**2)) for r in model.layers if hasattr(r, "kernel"))
    result = dict(settings)
    result.update({"final_training_mae": training_mae, "final_validation_mae": validation_mae,
                    "l2_penalty": penalty, "final_validation_loss": validation_mae+penalty,
                    "kernel_sum_of_squares": sum_of_squares, "parameters": model.count_params(),
                    "training_and_measurement_seconds": round(perf_counter()-start_time, 3),
                    "device": "CPU", "training_samples": 64, "validation_samples": 128,
                    "data_seed": 2026, "best_val_mae_epoch": int(np.argmin(history.history["val_mae"])+1),
                    "evaluated_state": "last epoch; no weight restoration", "test_set_used": False})
    keys = ["loss", "mae", "val_loss", "val_mae"]
    rows = [[i+1]+[float(history.history[k][i]) for k in keys]
             for i in range(len(history.history["loss"]))]
    save_data(folder, result, ["epoch"]+keys, rows)
    # The epoch average and measurement using the final weights are different quantities.
    figure, t = plt.subplots()
    epoch_numbers = np.arange(1, len(history.history["mae"])+1)
    t.plot(epoch_numbers, history.history["mae"], color=BLUE, label="Training MAE (epoch average)")
    t.plot(epoch_numbers, history.history["val_mae"], color=ORANGE, label="Validation MAE (end of epoch)")
    t.set(xlabel="Epoch", ylabel="MAE", title="Prediction errors during training")
    t.legend(); t.grid(alpha=.2)
    save_figure(figure, folder, "learning_curves.png")
    grid = np.linspace(-3, 3, 400, dtype="float32").reshape(-1, 1)
    prediction = model(grid, training=False).numpy()
    figure, t = plt.subplots()
    t.scatter(train_x, train_y, s=25, color=BLUE, label="Training samples")
    t.scatter(val_x, val_y, s=20, marker="x", color=ORANGE, alpha=.6, label="Validation samples")
    t.plot(grid, np.sin(1.5*grid)+.3*grid, "--", color="gray", label="Noise-free data-generating curve")
    t.plot(grid, prediction, color=TEAL, linewidth=2, label="Network prediction")
    t.set(xlabel="Input x", ylabel="Continuous target / prediction", title="What did the network learn?")
    t.legend(fontsize=9)
    save_figure(figure, folder, "prediction.png")
    figure, t = plt.subplots()
    t.plot(epoch_numbers, history.history["val_loss"], color=ORANGE, label="Validation loss: MAE + penalty")
    t.plot(epoch_numbers, history.history["val_mae"], color=BLUE, label="Validation MAE: prediction error")
    t.set(xlabel="Epoch", ylabel="Value", title="Loss and prediction error")
    t.legend(); t.grid(alpha=.2)
    save_figure(figure, folder, "loss_and_mae.png")
    print("\nRUN SUMMARY")
    print(f"Device: CPU | Samples: 64 training / 128 validation")
    print(f"Network: 1 → {settings['hidden_units']} ReLU → 1 linear output")
    print(f"Epochs: {settings['epochs']} | L2: {settings['l2_strength']}")
    print(f"Trainable parameters: {model.count_params()}")
    print(f"Final training MAE: {training_mae:.6f}")
    print(f"Final validation MAE: {validation_mae:.6f}")
    print(f"L2 penalty: {penalty:.6f} | Total validation loss: {validation_mae+penalty:.6f}")
    print(f"Sum of squared Dense kernel weights: {sum_of_squares:.6f}")
    print(f"Training and measurement: {result['training_and_measurement_seconds']:.3f} s (excluding imports)")
    print("We evaluate the final epoch model; validation was not used to restore earlier weights.")
    finished(folder)
