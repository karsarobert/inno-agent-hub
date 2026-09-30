"""Reads, imports, performs a short CPU computation and saves an image. Installs nothing."""
import sys
from importlib import metadata
print("Python:", sys.version.split()[0], "| Interpreter:", sys.executable, flush=True)
from helpers import np, plt, new_run_folder, save_figure, finished
from cpu_environment import tf, keras, layers, new_training_run

for package in ["numpy", "matplotlib", "keras"]:
    print(package + ":", metadata.version(package))
print("TensorFlow:", tf.__version__)
print("Visible GPUs:", tf.config.get_visible_devices("GPU"))
new_training_run(42)
model = keras.Sequential([keras.Input(shape=(1,)), layers.Dense(1)])
model.compile(optimizer="sgd", loss="mse")
x = np.array([[1.0], [2.0]], dtype="float32")
model.train_on_batch(x, 2*x)
assert not tf.config.get_visible_devices("GPU"), "This package requires CPU-only execution."
folder = new_run_folder(__file__)
figure, t = plt.subplots()
t.plot([1, 2], [2, 4], "o-")
t.set(title="Environment check: saving figures works", xlabel="x", ylabel="2x")
save_figure(figure, folder, "check.png")
print("ENVIRONMENT OK – CPU computation and figure saving succeeded.")
finished(folder)
