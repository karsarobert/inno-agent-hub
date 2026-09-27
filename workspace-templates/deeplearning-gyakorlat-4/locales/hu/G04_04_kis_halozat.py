"""Egy bemenet → egy ReLU rejtett réteg → egy folytonos becslés. CPU-s tanítás."""
from time import perf_counter
from cpu_kornyezet import keras, layers, uj_tanitas, adatcsomagok, RovidJelzes
from segedletek import uj_mappa
from halo_seged import regresszios_adatok, kezdeti_azonosito, halo_mentese

# BEÁLLÍTÁSOK – első futás: 8 neuron, 120 epocha.
REJTETT_NEURONOK = 8
EPOCHOK = 120
TANULASI_RATA = 0.01
BATCH_MERET = 16
VELETLEN_MAG = 42

if not 1 <= REJTETT_NEURONOK <= 128 or not 1 <= EPOCHOK <= 1000:
    raise SystemExit("Ebben a gyakorlatban 1–128 neuron és 1–1000 epocha használható.")
uj_tanitas(VELETLEN_MAG)
tanito_x, tanito_y, validacios_x, validacios_y = regresszios_adatok()
tanito_adatok, validacios_adatok = adatcsomagok(
    tanito_x, tanito_y, validacios_x, validacios_y, BATCH_MERET, VELETLEN_MAG)

# MODELL – egy mintához egyetlen x szám tartozik.
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(REJTETT_NEURONOK, activation="relu"),
    layers.Dense(1),
])
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
azonosito = kezdeti_azonosito(modell)
print(f"CPU-s tanítás indul: 1 → {REJTETT_NEURONOK} → 1; {EPOCHOK} epocha.", flush=True)
print(f"Kezdeti súlyok azonosítója: {azonosito}", flush=True)

# TANÍTÁS – egy epochában 64/16 = 4 tanítási batch.
kezdes = perf_counter()
tortenet = modell.fit(
    tanito_adatok,
    validation_data=validacios_adatok,
    epochs=EPOCHOK,
    shuffle=False,  # Az előkészített adatcsomag már keveri a tanítómintákat.
    verbose=0,
    callbacks=[RovidJelzes(EPOCHOK)],
)

# KÉSZ MÉRÉS ÉS ÁBRÁZOLÁS – nem indít újabb tanítást.
mappa = uj_mappa(__file__)
halo_mentese(mappa, modell, tortenet,
            (tanito_x, tanito_y, validacios_x, validacios_y),
            {"rejtett_neuronok": REJTETT_NEURONOK, "epochok": EPOCHOK,
             "tanulasi_rata": TANULASI_RATA, "batch_meret": BATCH_MERET,
             "veletlen_mag": VELETLEN_MAG, "l2_erosseg": 0.0,
             "kezdeti_sulyok": azonosito}, kezdes)
