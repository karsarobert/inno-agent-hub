"""Learning one weight. The target is w = 3; each row is a state AFTER an update."""
from helpers import new_run_folder, save_data, gradient_plot, finished

# SETTINGS – run without changes the first time.
learning_rate = 0.1
number_of_steps = 8
initial_weight = -1.0

if not 0 < learning_rate <= 1.2 or not 1 <= number_of_steps <= 100:
    raise SystemExit("In this example: 0 < rate <= 1.2; 1–100 steps.")

# THE COMPUTATION WE ARE EXPLORING
weight = initial_weight
rows = [[0, weight, (weight-3)**2]]
print("Step | Weight | Loss")
print(f"{0:5d} | {weight: .6f} | {(weight-3)**2:.6f}  (initial)")
for step in range(number_of_steps):
    gradient = 2 * (weight - 3)
    weight = weight - learning_rate * gradient
    loss = (weight - 3) ** 2
    rows.append([step+1, weight, loss])
    if step < 8 or step+1 == number_of_steps:
        print(f"{step+1:5d} | {weight: .6f} | {loss:.6f}")

# PREPARED PLOTTING – all steps are also saved in the CSV file.
folder = new_run_folder(__file__)
save_data(folder, {"learning_rate": learning_rate, "number_of_steps": number_of_steps,
                       "initial_weight": initial_weight, "final_weight": weight, "final_loss": loss},
               ["step", "weight", "loss"], rows)
gradient_plot(folder, rows)
finished(folder)
