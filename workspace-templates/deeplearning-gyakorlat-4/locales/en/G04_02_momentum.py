"""Two update rules on the same L(x,y)=x²/20+y² function."""
from helpers import np, new_run_folder, save_data, momentum_plot, finished

# SETTINGS – only momentum changes in the required experiment.
momentum = 0.9
learning_rate = 0.1
number_of_steps = 40

if not 0 <= momentum < 1 or not 0 < learning_rate <= 0.8 or not 1 <= number_of_steps <= 500:
    raise SystemExit("Allowed: 0 <= momentum < 1, 0 < rate <= 0.8, 1–500 steps.")

def trajectory(beta):
    position = np.array([-7.0, 2.0])
    velocity = np.zeros(2)
    points = [position.copy()]
    for _ in range(number_of_steps):
        gradient = np.array([position[0] / 10, 2 * position[1]])
        velocity = beta * velocity - learning_rate * gradient
        position = position + velocity
        points.append(position.copy())
    return np.array(points)

# With beta=0, the previous velocity has no effect.
paths = {"Plain gradient descent": trajectory(0.0),
        f"Momentum (β={momentum})": trajectory(momentum)}
rows = []
for name, points in paths.items():
    x, y = points[-1]
    print(f"{name}: endpoint=({x:.4f}, {y:.4f}), loss={x*x/20+y*y:.6f}")
    rows.extend([name, i, float(p[0]), float(p[1]), float(p[0]**2/20+p[1]**2)]
                 for i, p in enumerate(points))
folder = new_run_folder(__file__)
save_data(folder, {"momentum": momentum, "learning_rate": learning_rate,
                       "number_of_steps": number_of_steps, "exact_gradient": True},
               ["method", "step", "x", "y", "loss"], rows)
momentum_plot(folder, paths)
finished(folder)
