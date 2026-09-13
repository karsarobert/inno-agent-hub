"""Borminőség becslése a mért tulajdonságokból.

A 11 jellemzőből egy minőségi pontszámot becslünk.
Adat-előkészítés → 11–32–16–1 alapmodell → tanítás → validáció → mentés.
A quality csak célérték, nem bemenet. A becslés tört szám is lehet.
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
matplotlib.use("Agg")  # Képfájlt mentünk; nem kell grafikus ablakot megnyitni.
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

print('Borminőség becslése a mért tulajdonságokból.')
print('A 11 jellemzőből egy minőségi pontszámot becslünk.\nAdat-előkészítés → 11–32–16–1 alapmodell → tanítás → validáció → mentés.\nA quality csak célérték, nem bemenet. A becslés tört szám is lehet.')

VELETLEN_MAG = 42
REJTETT_NEURONOK = (32, 16)
EPOCHOK = 40
BATCH_MERET = 64
TANULASI_RATA = 0.003

# 1. ADATOK: ugyanaz az előkészítés, mint a G02_04 programban.
gyoker = Path(__file__).resolve().parent
adatok = pd.read_csv(gyoker / "adatok" / "red-wine.csv")
adatok = adatok.drop_duplicates().reset_index(drop=True)
# Egy valódi sor rövid bemutatása: a pontszámot nem tesszük a bemenetbe.
print("Egy borminta nehany bemenete es az ismert cel:")
print(adatok.loc[[0], ["alcohol", "pH", "sulphates", "quality"]].to_string(index=False))
print("A harom bemutatott jellemzon kivul meg nyolc bemenetet hasznalunk.")
jellemzok = adatok.drop(columns=["quality"])
celertekek = adatok["quality"]
tanulo_resz, teszt_jellemzok, tanulo_cel, teszt_cel = train_test_split(
    jellemzok, celertekek, test_size=0.2, random_state=VELETLEN_MAG
)
tanito_jellemzok, validacios_jellemzok, tanito_cel, validacios_cel = train_test_split(
    tanulo_resz, tanulo_cel, test_size=0.25, random_state=VELETLEN_MAG
)
skalazo = MinMaxScaler()
tanito_skala = skalazo.fit_transform(tanito_jellemzok).astype("float32")
validacios_skala = skalazo.transform(validacios_jellemzok).astype("float32")
teszt_skala = skalazo.transform(teszt_jellemzok).astype("float32")
tanito_cel = tanito_cel.to_numpy(dtype="float32")
validacios_cel = validacios_cel.to_numpy(dtype="float32")
teszt_cel = teszt_cel.to_numpy(dtype="float32")

# 2. MODELL: a súlyokat ezúttal a tanítás állítja be.
keras.utils.set_random_seed(VELETLEN_MAG)
modell = keras.Sequential([
    keras.Input(shape=(tanito_skala.shape[1],)),
    layers.Dense(REJTETT_NEURONOK[0], activation="relu"),
    layers.Dense(REJTETT_NEURONOK[1], activation="relu"),
    layers.Dense(1),
])
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="mae",
)
modell.summary()
parameterek_szama = modell.count_params()
print("Tanito / validacios / teszt mintak:",
      len(tanito_cel), len(validacios_cel), len(teszt_cel))

# A konstans összehasonlító becslés csak a tanítócélok mediánját használja.
alap_becsles = np.median(tanito_cel)
alap_mae = np.mean(np.abs(validacios_cel - alap_becsles))
print(f"Konstans alapmodell validacios MAE: {alap_mae:.4f}")

# 3. TANÍTÁS: a validation_data nem vesz részt a gradiensszámításban.
tortenet = modell.fit(
    tanito_skala, tanito_cel,
    validation_data=(validacios_skala, validacios_cel),
    epochs=EPOCHOK,
    batch_size=BATCH_MERET,
    verbose=2,
)

# 4. ÉRTELMEZÉS: a visszakapott History tárolja az epochonkénti veszteséget.
gorbek = pd.DataFrame(tortenet.history)
gorbek.index = np.arange(1, len(gorbek) + 1)
gorbek.index.name = "epoch"
validacios_mae = modell.evaluate(validacios_skala, validacios_cel, verbose=0)
print(f"Lefutott epochok: {len(gorbek)}")
print(f"Vegso modell validacios MAE: {validacios_mae:.4f}")
print(f"Legkisebb naplozott val_loss: {gorbek['val_loss'].min():.4f}")
print(f"A naplozott minimum epochja: {gorbek['val_loss'].idxmin()}")
becslesek = modell.predict(validacios_skala[:5], verbose=0).ravel()
osszevetes = pd.DataFrame({"cel": validacios_cel[:5], "becsles": becslesek})
print("Ot validacios minta:")
print(osszevetes.round(3).to_string(index=False))

print("A teszthalmazt most erintetlenul hagyjuk a vegso ertekeleshez.")

# 5. MENTÉS: minden futás új mappát kap; a korábbi eredményeket megőrizzük.
futas_neve = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
eredmenymappa = gyoker / "eredmenyek" / (Path(__file__).stem + "_" + futas_neve)
eredmenymappa.mkdir(parents=True, exist_ok=False)
gorbek.to_csv(eredmenymappa / "tanulasi_gorbek.csv")
osszevetes.to_csv(eredmenymappa / "becslesek.csv", index=False)
abra, tengely = plt.subplots(figsize=(8, 4.5))
tengely.plot(gorbek.index, gorbek["loss"], label="Tanitas")
tengely.plot(gorbek.index, gorbek["val_loss"], label="Validacio", linestyle="--")
tengely.set(xlabel="Epoch", ylabel="MAE", title="Borminoseg: tanulasi gorbek")
tengely.legend()
tengely.grid(alpha=0.25)
abra.tight_layout()
abra.savefig(eredmenymappa / "tanulasi_gorbek.png", dpi=140)
plt.close(abra)
beallitasok = {
    "veletlen_mag": VELETLEN_MAG, "rejtett_neuronok": REJTETT_NEURONOK,
    "parameterek_szama": parameterek_szama, "epochkeret": EPOCHOK, "batch_meret": BATCH_MERET,
    "tanulasi_rata": TANULASI_RATA, "tensorflow": tf.__version__,
    "validacios_mae": float(validacios_mae), "alapmodell_mae": float(alap_mae),
}
(eredmenymappa / "beallitasok.json").write_text(
    json.dumps(beallitasok, indent=2, ensure_ascii=False), encoding="utf-8"
)
shutil.copyfile(__file__, eredmenymappa / "futtatott_forras.py")
print("Eredmenymappa:", eredmenymappa)
print("Abra: tanulasi_gorbek.png | Adatok: tanulasi_gorbek.csv")

# Rövid, a napló végén is látható bizonyíték az aktuális konfigurációról.
print("FUTASI OSSZEFOGLALO")
print("Aktualis rejtett neuronok:", REJTETT_NEURONOK)
print("Parameterek szama:", parameterek_szama)
print("Epochkeret / lefutott:", EPOCHOK, len(gorbek))
print(f"Vegso modell validacios MAE: {validacios_mae:.4f}")
print(f"Konstans alapmodell validacios MAE: {alap_mae:.4f}")
print(f"Elso validacios cel / becsles: {validacios_cel[0]:.3f} / {becslesek[0]:.3f}")
print("Eredmenymappa:", eredmenymappa)
