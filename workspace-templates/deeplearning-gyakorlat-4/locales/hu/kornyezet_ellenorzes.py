"""Olvas, importál, CPU-n egy rövid műveletet végez és képet ment. Nem telepít."""
import sys
from importlib import metadata
print("Python:", sys.version.split()[0], "| Értelmező:", sys.executable, flush=True)
from segedletek import np, plt, uj_mappa, kep_mentese, kesz
from cpu_kornyezet import tf, keras, layers, uj_tanitas

for csomag in ["numpy", "matplotlib", "keras"]:
    print(csomag + ":", metadata.version(csomag))
print("TensorFlow:", tf.__version__)
print("Látható GPU-k:", tf.config.get_visible_devices("GPU"))
uj_tanitas(42)
modell = keras.Sequential([keras.Input(shape=(1,)), layers.Dense(1)])
modell.compile(optimizer="sgd", loss="mse")
x = np.array([[1.0], [2.0]], dtype="float32")
modell.train_on_batch(x, 2*x)
assert not tf.config.get_visible_devices("GPU"), "A csomag CPU-s működést igényel."
mappa = uj_mappa(__file__)
abra, t = plt.subplots()
t.plot([1, 2], [2, 4], "o-")
t.set(title="Környezetellenőrzés: az ábramentés működik", xlabel="x", ylabel="2x")
kep_mentese(abra, mappa, "ellenorzes.png")
print("KÖRNYEZET RENDBEN – a CPU-s számítás és az ábramentés sikerült.")
kesz(mappa)
