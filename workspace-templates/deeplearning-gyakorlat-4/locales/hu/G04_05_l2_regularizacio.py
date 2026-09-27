"""L2-kísérlet a 64 neuronos hálózaton. Mindkét Dense kerneljét büntetjük."""
from time import perf_counter
from cpu_kornyezet import keras, layers, regularizers, uj_tanitas, adatcsomagok, RovidJelzes
from segedletek import uj_mappa
from halo_seged import regresszios_adatok, kezdeti_azonosito, halo_mentese

# BEÁLLÍTÁSOK – ez a fájl önállóan is futtatható.
L2_EROSSEG = 0.0
REJTETT_NEURONOK = 64
EPOCHOK = 120
TANULASI_RATA = 0.01
BATCH_MERET = 16
VELETLEN_MAG = 42

if not 0 <= L2_EROSSEG <= 1:
    raise SystemExit("Ebben a példában az L2-erősség 0 és 1 közötti legyen.")
uj_tanitas(VELETLEN_MAG)
tanito_x, tanito_y, validacios_x, validacios_y = regresszios_adatok()
tanito_adatok, validacios_adatok = adatcsomagok(
    tanito_x, tanito_y, validacios_x, validacios_y, BATCH_MERET, VELETLEN_MAG)

# MODELL – ugyanaz a hálózat; a súlymátrixok büntetése változik.
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(REJTETT_NEURONOK, activation="relu",
                 kernel_regularizer=regularizers.l2(L2_EROSSEG)),
    layers.Dense(1, kernel_regularizer=regularizers.l2(L2_EROSSEG)),
])
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
azonosito = kezdeti_azonosito(modell)
print(f"CPU-s L2-kísérlet indul: λ={L2_EROSSEG}; {EPOCHOK} epocha.", flush=True)
print(f"Kezdeti súlyok azonosítója: {azonosito}", flush=True)
kezdes = perf_counter()
tortenet = modell.fit(
    tanito_adatok,
    validation_data=validacios_adatok,
    epochs=EPOCHOK,
    shuffle=False,  # Az előkészített adatcsomag már keveri a tanítómintákat.
    verbose=0,
    callbacks=[RovidJelzes(EPOCHOK)],
)

mappa = uj_mappa(__file__)
halo_mentese(mappa, modell, tortenet,
            (tanito_x, tanito_y, validacios_x, validacios_y),
            {"rejtett_neuronok": REJTETT_NEURONOK, "epochok": EPOCHOK,
             "tanulasi_rata": TANULASI_RATA, "batch_meret": BATCH_MERET,
             "veletlen_mag": VELETLEN_MAG, "l2_erosseg": L2_EROSSEG,
             "kezdeti_sulyok": azonosito}, kezdes)
