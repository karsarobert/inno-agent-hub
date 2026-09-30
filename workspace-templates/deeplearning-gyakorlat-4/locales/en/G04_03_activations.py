"""Same inputs, different activations. No network is trained here."""
from helpers import np, new_run_folder, save_data, activation_plot, finished

# SETTINGS
activation = "sigmoid"       # Other options: "relu", "leaky_relu"
inputs = np.array([-6.0, -1.0, 0.0, 1.0, 6.0])
negative_slope = 0.1
incoming_gradient = 2.0

if activation not in {"sigmoid", "relu", "leaky_relu"}:
    raise SystemExit('activation must be "sigmoid", "relu" or "leaky_relu".')
if not 0 < negative_slope <= 1:
    raise SystemExit("The negative slope must be greater than 0 and at most 1.")

def activation_function(z):
    if activation == "sigmoid":
        return 1 / (1 + np.exp(-z))
    if activation == "relu":
        return np.maximum(0, z)
    return np.where(z > 0, z, negative_slope * z)

def derivative(z):
    if activation == "sigmoid":
        value = activation_function(z)
        return value * (1 - value)
    if activation == "relu":
        return np.where(z > 0, 1.0, 0.0)
    return np.where(z > 0, 1.0, negative_slope)

outputs = activation_function(inputs)
local_derivatives = derivative(inputs)
returned_gradients = incoming_gradient * local_derivatives
print("Activation:", activation)
print("Input | Output | Local derivative | Returned gradient")
rows = list(zip(inputs, outputs, local_derivatives, returned_gradients))
for row in rows:
    print(" | ".join(f"{v: .6f}" for v in row))
if activation != "sigmoid":
    print("At the kink at 0, the code selects the left-branch value; a classical derivative generally does not exist there.")
folder = new_run_folder(__file__)
save_data(folder, {"activation": activation, "negative_slope": negative_slope,
                       "incoming_gradient": incoming_gradient, "inputs": inputs.tolist()},
               ["input_value", "output_value", "local_derivative", "returned_gradient"], rows)
activation_plot(folder, activation_function, derivative, inputs)
finished(folder)
