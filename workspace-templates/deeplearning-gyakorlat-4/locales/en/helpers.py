"""Prepared plotting and saving. No changes needed for the student exercises."""
from datetime import datetime
from pathlib import Path
import csv
import json
import sys

try:
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError as error:
    raise SystemExit(
        f"A Python package could not be loaded: {error}\n"
        f"Interpreter: {sys.executable}\nAsk your instructor for help!"
    ) from error

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "figure.figsize": (10, 4.5),
                     "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, TEAL = "#075ac8", "#b54a17", "#087e87"


def new_run_folder(program):
    name = Path(program).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    folder = ROOT / "view" / f"{name}_{timestamp}"
    folder.mkdir(parents=True, exist_ok=False)
    return folder


def save_data(folder, settings, header, rows):
    (folder / "result.json").write_text(
        json.dumps(settings, ensure_ascii=False, indent=2, allow_nan=False),
        encoding="utf-8")
    with (folder / "values.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


def save_figure(figure, folder, name):
    figure.tight_layout()
    figure.savefig(folder / name, dpi=145)
    plt.close(figure)


def finished(folder):
    print("\nRUN COMPLETE. Figures and numerical results are saved in:")
    print(folder)
    print("Refresh the View folder / file list, then open the image from the CURRENT run folder!")


def gradient_plot(folder, rows):
    values = np.asarray(rows)
    figure, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(values[:, 0], values[:, 1], "o-", color=BLUE)
    axes[0].axhline(3, color=ORANGE, linestyle="--", label="Minimum: w = 3")
    axes[0].set(xlabel="Number of updates", ylabel="Weight", title="How does the weight change?")
    axes[0].legend()
    axes[1].plot(values[:, 0], values[:, 2], "o-", color=ORANGE)
    axes[1].set(xlabel="Number of updates", ylabel="L = (w − 3)²", title="Loss")
    for t in axes:
        t.grid(alpha=.2)
    save_figure(figure, folder, "learning_steps.png")


def momentum_plot(folder, paths):
    figure, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    x_limit = max(8, *(np.max(np.abs(u[:, 0])) * 1.05 for u in paths.values()))
    y_limit = max(3, *(np.max(np.abs(u[:, 1])) * 1.05 for u in paths.values()))
    x, y = np.meshgrid(np.linspace(-x_limit, x_limit, 220),
                       np.linspace(-y_limit, y_limit, 160))
    for axis, (name, path) in zip(axes, paths.items()):
        axis.contour(x, y, x*x/20+y*y,
                       levels=[.05, .2, .5, 1, 2, 4, 8, 16, 32], colors="#b7c7d8")
        axis.plot(path[:, 0], path[:, 1], ".-", color=BLUE, linewidth=1.2)
        axis.scatter(*path[0], color=TEAL, s=55, label="Starting point")
        axis.scatter(*path[-1], color=ORANGE, s=55, label="Final point", zorder=5)
        axis.plot(0, 0, "+", color="black", markersize=10)
        axis.set(title=name, xlabel="x parameter", ylabel="y parameter",
                    xlim=(-x_limit, x_limit), ylim=(-y_limit, y_limit))
        axis.legend(fontsize=9)
    save_figure(figure, folder, "trajectories.png")


def activation_plot(folder, activation_function, derivative, inputs):
    x = np.linspace(-8, 8, 801)
    figure, t = plt.subplots(1, 2, figsize=(11, 4.5))
    t[0].plot(x, activation_function(x), color=BLUE)
    t[0].scatter(inputs, activation_function(inputs), color=ORANGE, zorder=5)
    t[1].plot(x, derivative(x), color=TEAL)
    t[1].scatter(inputs, derivative(inputs), color=ORANGE, zorder=5)
    for axis, title, label in zip(t, ["Activation", "Local derivative"], ["f(z)", "f′(z)"]):
        axis.set(title=title, xlabel="Input z", ylabel=label)
        axis.axhline(0, color="gray", linewidth=.6)
        axis.axvline(0, color="gray", linewidth=.6)
        axis.grid(alpha=.2)
    save_figure(figure, folder, "activation_and_derivative.png")


def bar_plot(folder, input_value, output_value, title, file):
    position = np.arange(1, len(input_value)+1)
    figure, t = plt.subplots()
    t.bar(position-.18, input_value, width=.36, color=BLUE, label="Input")
    t.bar(position+.18, output_value, width=.36, color=ORANGE, label="Output")
    t.axhline(0, color="gray", linewidth=.6)
    t.set(xlabel="Element number", ylabel="Value", title=title, xticks=position)
    t.legend()
    save_figure(figure, folder, file)
