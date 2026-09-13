"""Kétdimenziós pontok négy osztályának megtanulása.

A bemenet két koordináta; a cél a pont ismert 0, 1, 2 vagy 3 címkéje.
A predict négy osztálybecslést ad; az argmax ezekből osztályindexet választ.
A kép háttere a modell döntése, a pont színe a valódi címke.
Részletes kódbemutatás: PROGRAM_BEMUTATOK.md.
Szemléltetés: szemlelteto.html (böngészőben megnyitható).
"""

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")

from pathlib import Path
from datetime import datetime
import json
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print('Kétdimenziós pontok négy osztályának megtanulása.')
print('A bemenet két koordináta; a cél a pont ismert 0, 1, 2 vagy 3 címkéje.\nA predict négy osztálybecslést ad; az argmax ezekből osztályindexet választ.\nA kép háttere a modell döntése, a pont színe a valódi címke.')

VELETLEN_MAG = 42
OSZTALYOK_SZAMA = 4
REJTETT_NEURONOK = (32, 16)
EPOCHOK = 40
BATCH_MERET = 32
TANULASI_RATA = 0.003
VEGSO_TESZT = False

# 1. ADATOK: minden sor egy pont, minden címke 0, 1, 2 vagy 3.
jellemzok, cimkek = make_blobs(
    n_samples=500, n_features=2, centers=OSZTALYOK_SZAMA,
    cluster_std=2.0, random_state=2,
)
tanulo_resz, teszt_jellemzok, tanulo_cimkek, teszt_cimkek = train_test_split(
    jellemzok, cimkek, test_size=0.2, random_state=VELETLEN_MAG, stratify=cimkek
)
tanito_jellemzok, validacios_jellemzok, tanito_cimkek, validacios_cimkek = train_test_split(
    tanulo_resz, tanulo_cimkek, test_size=0.25,
    random_state=VELETLEN_MAG, stratify=tanulo_cimkek,
)
skalazo = StandardScaler()
tanito_skala = skalazo.fit_transform(tanito_jellemzok).astype("float32")
validacios_skala = skalazo.transform(validacios_jellemzok).astype("float32")
teszt_skala = skalazo.transform(teszt_jellemzok).astype("float32")
tanito_cel = keras.utils.to_categorical(tanito_cimkek, OSZTALYOK_SZAMA)
validacios_cel = keras.utils.to_categorical(validacios_cimkek, OSZTALYOK_SZAMA)
teszt_cel = keras.utils.to_categorical(teszt_cimkek, OSZTALYOK_SZAMA)

# 2. MODELL: négy, egyre összegződő kimenet az osztályokhoz.
keras.utils.set_random_seed(VELETLEN_MAG)
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(REJTETT_NEURONOK[0], activation="relu"),
    layers.Dense(REJTETT_NEURONOK[1], activation="relu"),
    layers.Dense(OSZTALYOK_SZAMA, activation="softmax"),
])
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="categorical_crossentropy", metrics=["accuracy"],
)
modell.summary()
parameterek_szama = modell.count_params()
print("Tanito / validacios / teszt mintak:",
      len(tanito_cel), len(validacios_cel), len(teszt_cel))
print("Egy tanitocimke:", tanito_cimkek[0])
print("Ugyanez one-hot alakban:", tanito_cel[0])

# 3. TANÍTÁS és validáció.
tortenet = modell.fit(
    tanito_skala, tanito_cel,
    validation_data=(validacios_skala, validacios_cel),
    epochs=EPOCHOK, batch_size=BATCH_MERET, verbose=2,
)
validacios_eredmeny = modell.evaluate(validacios_skala, validacios_cel,
                                     verbose=0, return_dict=True)
valoszinusegek = modell.predict(validacios_skala[:5], verbose=0)
becsult_osztalyok = valoszinusegek.argmax(axis=1)
print("Ot becsult valoszinusegvektor:")
print(np.round(valoszinusegek, 3))
print("Becsult osztalyok:", becsult_osztalyok)
print("Helyes osztalyok:", validacios_cimkek[:5])
print(f"Validacios pontossag: {validacios_eredmeny['accuracy']:.4f}")
print(f"Validacios veszteseg: {validacios_eredmeny['loss']:.4f}")
teszt_eredmeny = None
if VEGSO_TESZT:
    teszt_eredmeny = modell.evaluate(teszt_skala, teszt_cel,
                                     verbose=0, return_dict=True)
    print("Lezart modell fuggetlen tesztje:", teszt_eredmeny)
else:
    print("A teszthalmazon nem ertekeltunk; a modellvalasztas validacio alapjan tortenik.")

# 4. ÁBRÁZOLÁS: a színt az osztályindex adja, nem a négy valószínűség.
# A rajzolási tartományt csak a tanítóadatokból választjuk.
x_tengely = np.linspace(tanito_jellemzok[:, 0].min() - 1,
                       tanito_jellemzok[:, 0].max() + 1, 120)
y_tengely = np.linspace(tanito_jellemzok[:, 1].min() - 1,
                       tanito_jellemzok[:, 1].max() + 1, 120)
racs_x, racs_y = np.meshgrid(x_tengely, y_tengely)
racspontok = np.column_stack([racs_x.ravel(), racs_y.ravel()])
racs_skala = skalazo.transform(racspontok).astype("float32")
racs_valoszinusegek = modell.predict(racs_skala, verbose=0)
racs_osztalyok = racs_valoszinusegek.argmax(axis=1).reshape(racs_x.shape)

gyoker = Path(__file__).resolve().parent
futas_neve = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
eredmenymappa = gyoker / "eredmenyek" / (Path(__file__).stem + "_" + futas_neve)
eredmenymappa.mkdir(parents=True, exist_ok=False)
abra, tengely = plt.subplots(figsize=(7, 5))
tengely.contourf(racs_x, racs_y, racs_osztalyok,
                levels=np.arange(5) - 0.5, cmap="tab10", alpha=0.25, vmin=0, vmax=3)
tengely.scatter(tanito_jellemzok[:, 0], tanito_jellemzok[:, 1],
                c=tanito_cimkek, cmap="tab10", vmin=0, vmax=3, s=18, label="Tanitas")
tengely.scatter(validacios_jellemzok[:, 0], validacios_jellemzok[:, 1],
                c=validacios_cimkek, cmap="tab10", vmin=0, vmax=3,
                s=35, marker="^", edgecolors="black", label="Validacio")
tengely.set(xlabel="Elso jellemzo", ylabel="Masodik jellemzo",
            title="Negy osztaly: a hatter a modell becslese")
tengely.legend()
abra.tight_layout()
abra.savefig(eredmenymappa / "osztalyok.png", dpi=140)
plt.close(abra)
gorbek = pd.DataFrame(tortenet.history)
gorbek.index = np.arange(1, len(gorbek) + 1)
gorbek.index.name = "epoch"
gorbek.to_csv(eredmenymappa / "tanulasi_gorbek.csv")
abra, tengely = plt.subplots(figsize=(8, 4.5))
tengely.plot(gorbek.index, gorbek["loss"], label="Tanitas")
tengely.plot(gorbek.index, gorbek["val_loss"], label="Validacio", linestyle="--")
tengely.set(xlabel="Epoch", ylabel="Keresztentropia", title="Osztalyozas: tanulasi gorbek")
tengely.legend()
abra.tight_layout()
abra.savefig(eredmenymappa / "tanulasi_gorbek.png", dpi=140)
plt.close(abra)
beallitasok = {
    "veletlen_mag": VELETLEN_MAG, "rejtett_neuronok": REJTETT_NEURONOK,
    "parameterek_szama": parameterek_szama, "epochkeret": EPOCHOK, "batch_meret": BATCH_MERET,
    "tanulasi_rata": TANULASI_RATA, "tensorflow": tf.__version__,
    "validacio": validacios_eredmeny, "vegso_teszt": VEGSO_TESZT,
    "teszt": teszt_eredmeny,
}
(eredmenymappa / "beallitasok.json").write_text(
    json.dumps(beallitasok, indent=2), encoding="utf-8"
)
shutil.copyfile(__file__, eredmenymappa / "futtatott_forras.py")
print("Eredmenymappa:", eredmenymappa)
print("Abrak: osztalyok.png, tanulasi_gorbek.png")

# Rövid, a napló végén is látható bizonyíték az aktuális konfigurációról.
print("FUTASI OSSZEFOGLALO")
print("Aktualis rejtett neuronok:", REJTETT_NEURONOK)
print("Parameterek szama:", parameterek_szama)
print("Epochkeret / lefutott:", EPOCHOK, len(gorbek))
print(f"Validacios pontossag: {validacios_eredmeny['accuracy']:.4f}")
print(f"Validacios veszteseg: {validacios_eredmeny['loss']:.4f}")
print("Becsult / helyes osztalyok:", becsult_osztalyok, "/", validacios_cimkek[:5])
print("Vegso teszt bekapcsolva:", VEGSO_TESZT)
print("Eredmenymappa:", eredmenymappa)
