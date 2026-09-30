"""Inverted dropout on eight values. Training mode does not train a network here."""
from helpers import np, new_run_folder, save_data, bar_plot, finished

# SETTINGS – the fixed seed makes the initial run reproducible.
dropout_rate = 0.5
training_mode = True
random_seed = 42
inputs = np.array([0.2, 0.5, 1.3, 0.8, 1.1, 0.4, 0.7, 1.0])

if not 0 <= dropout_rate <= 0.9:
    raise SystemExit("The dropout rate must be between 0 and 0.9 in this demonstration.")
rng = np.random.default_rng(random_seed)
if training_mode:
    mask = rng.random(len(inputs)) >= dropout_rate
    outputs = inputs * mask / (1 - dropout_rate)
else:
    mask = np.ones(len(inputs), dtype=bool)
    outputs = inputs.copy()

print("Mode:", "training" if training_mode else "evaluation")
print("Input:", inputs)
print("Mask:", mask.astype(int) if training_mode else "no masking")
print("Output:", np.round(outputs, 4))
print("Number of dropped elements:", int(np.sum(~mask)))
print("A zero here is temporary masking, not a deleted neuron or weight.")
folder = new_run_folder(__file__)
save_data(folder, {"dropout_rate": dropout_rate, "training_mode": training_mode,
                       "random_seed": random_seed, "outputs": outputs.tolist()},
               ["input_value", "mask", "output_value"], zip(inputs, mask.astype(int), outputs))
bar_plot(folder, inputs, outputs,
            "Dropout – " + ("training mode" if training_mode else "evaluation mode"), "dropout.png")
finished(folder)
