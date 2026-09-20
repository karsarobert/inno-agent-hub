"""Spirálpontok osztályozása rejtett réteg nélkül.
Bemenet: két koordináta. Cél: a 0., 1. vagy 2. osztály.
A hallgató a MODELL, BEÁLLÍTÁS és TANÍTÁS blokkokra koncentrál.
"""
from segedletek import (csomagok_ellenorzese, spiral_adatok, uj_mappa, spiral_mentes)
csomagok_ellenorzese(['tensorflow'])
from tensorflow import keras
from tensorflow.keras import layers

# BEÁLLÍTÁS – egyszerre egy vizsgált tényezőt módosíts.
TANULASI_RATA = 0.01
EPOCHOK = 150
BATCH_MERET = 32
VELETLEN_MAG = 42

# ELŐKÉSZÍTETT ADATOK: 360 tanító-, 120 validációs, 120 tesztminta.
tanito_x, validacios_x, teszt_x, tanito_cimke, validacios_cimke, teszt_cimke = spiral_adatok()
tanito_cel = keras.utils.to_categorical(tanito_cimke, num_classes=3)
validacios_cel = keras.utils.to_categorical(validacios_cimke, num_classes=3)
keras.utils.set_random_seed(VELETLEN_MAG)

# MODELL – a hallgató itt építi / módosítja a hálózatot.
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(3, activation="softmax"),
])
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
modell.summary()
print('Tanítás / validáció / teszt: 360 / 120 / 120 minta.')
print('Példa címke és one-hot alakja:', tanito_cimke[0], tanito_cel[0])
print('Tanítás indul. Várd meg a futási összefoglalót!')

# TANÍTÁS – a súlyok itt változnak. A validáció nem súlyfrissítés.
tortenet = modell.fit(
    tanito_x, tanito_cel,
    validation_data=(validacios_x, validacios_cel),
    epochs=EPOCHOK,
    batch_size=BATCH_MERET,
    verbose=0,
)

# ÉRTÉKELÉS – itt már nem tanul a modell.
validacios_eredmeny = modell.evaluate(
    validacios_x, validacios_cel, verbose=0, return_dict=True)
valoszinusegek = modell.predict(validacios_x[:5], verbose=0)
becsult_osztalyok = valoszinusegek.argmax(axis=1)
print('Öt becsült osztály:', becsult_osztalyok)

# ELŐKÉSZÍTETT ÁBRÁK ÉS MENTÉS – ezeket nem kell programoznod.
mappa = uj_mappa(__file__)
beallitasok = {
    'tanulasi_rata': TANULASI_RATA, 'epochok': EPOCHOK,
    'batch_meret': BATCH_MERET, 'veletlen_mag': VELETLEN_MAG,
    'validacio': validacios_eredmeny,
}
spiral_mentes(mappa, modell, tortenet, beallitasok, validacios_x,
              validacios_cimke, teszt_x, teszt_cimke)
