"""Optional numerical BN demonstration. Gamma and beta are set manually here."""
from helpers import np, new_run_folder, save_data, bar_plot, finished

inputs = np.array([1.0, 2.0, 3.0, 4.0])
gamma = 1.0
beta = 0.0
training_mode = True
stored_mean = 2.5
stored_variance = 1.25
epsilon = 0.001

if training_mode:
    mean = np.mean(inputs)
    variance = np.mean((inputs - mean) ** 2)
else:
    mean = stored_mean
    variance = stored_variance
if variance < 0:
    raise SystemExit("Variance cannot be negative.")
normalized = (inputs - mean) / np.sqrt(variance + epsilon)
outputs = gamma * normalized + beta
print("Mean and variance used:", mean, variance)
print("Normalized values:", np.round(normalized, 4))
print("Final output:", np.round(outputs, 4))
print("The stored statistics are illustrative values. There is no learning in this program.")
folder = new_run_folder(__file__)
save_data(folder, {"gamma": gamma, "beta": beta, "training_mode": training_mode,
                       "mean_used": float(mean), "variance_used": float(variance)},
               ["input_value", "normalized", "output_value"], zip(inputs, normalized, outputs))
bar_plot(folder, inputs, outputs, "Batch normalization on four values", "batch_normalization.png")
finished(folder)
