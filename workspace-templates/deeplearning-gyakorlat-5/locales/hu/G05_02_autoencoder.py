"""Autoencoder tanítása – a bemeneti normál EKG-jelet kérjük vissza kimenetként.
Bemenet: 512 normál tanítójel, 128 külön normál validációs jel.
Kimenet: rekonstrukcio.png, tanulasi_gorbek.png és a mért MAE-értékek.
Módosítandó: epochok_szama (10 → 30); új Run új modellt tanít.
A 30 epochás futás a megfelelő saját 10 epochás futással összehasonlító képet is ment.
"""
from time import perf_counter
import hashlib
from cpu_kornyezet import keras, layers, uj_tanitas, adatcsomag, RovidJelzes
from segedletek import betolt_adatok, uj_mappa, tanitas_mentese

# 1. BEÁLLÍTÁSOK – egy epocha a teljes tanítóhalmaz egyszeri bejárása.
epochok_szama = 10
szuk_keresztmetszet = 8  # Csak az opcionális feladatban változtatjuk.

# Kész ellenőrzés és rögzített kezdőállapot – ezt nem kell módosítani.
if not isinstance(epochok_szama, int) or not 1 <= epochok_szama <= 100:
    raise SystemExit('Az epochok_szama 1 és 100 közötti egész szám legyen!')
if not isinstance(szuk_keresztmetszet, int) or not 1 <= szuk_keresztmetszet <= 32:
    raise SystemExit('A szuk_keresztmetszet 1 és 32 közötti egész szám legyen!')
uj_tanitas(42)

# 2. ADATOK BETÖLTÉSE – mindkét csoport csak normál jeleket tartalmaz.
# A validációs jelek nem vesznek részt a súlyok frissítésében.
adatok = betolt_adatok()
tanito_jelek = adatok['tanito_jelek']
validacios_jelek = adatok['validacios_jelek']

# 3. BEMENET–CÉL PÁROK – a kívánt kimenet maga a bemeneti jel.
# Ezért szerepel ugyanaz a tömb kétszer. A segéd 32-es csomagokat készít.
# 512 jel / 32 jel = 16 súlyfrissítés egy epochában.
tanito_csomag = adatcsomag(tanito_jelek, tanito_jelek, keveres=True)
validacios_csomag = adatcsomag(validacios_jelek, validacios_jelek)

# 4. A TELJES HÁLÓZAT – a belső 8 értékből 140 értéket állítunk vissza.
modell = keras.Sequential([
    keras.Input(shape=(140,)),  # Egy bemenet: egy 140 elemű jel.
    # Encoder: a jelből fokozatosan kisebb belső reprezentáció készül.
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    # Szűk keresztmetszet: tanult belső értékek, nem kiválasztott EKG-pontok.
    layers.Dense(szuk_keresztmetszet, activation='relu', kernel_initializer='he_normal'),
    # Decoder: a belső reprezentációból visszaállítja a jelalakot.
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    # A 140 kimenet amplitúdó 0 és 1 között, nem osztályvalószínűség.
    layers.Dense(140, activation='sigmoid'),
])

# 5. TANÍTÁS – compile: beállít; fit: ténylegesen módosítja a súlyokat.
# A MAE az eredeti és rekonstruált jel abszolút eltéréseinek átlaga.
modell.compile(optimizer='adam', loss='mae', jit_compile=False)
# Kész technikai azonosító: azonos kezdetből indul-e a két összehasonlított futás?
azonosito = hashlib.sha256(b''.join(s.tobytes() for s in modell.get_weights())).hexdigest()[:16]
print(f'CPU-s tanítás indul: 512 normál tanítójel, 128 normál validációs jel; {epochok_szama} epocha.', flush=True)
print(f'Kezdeti súlyok azonosítója: {azonosito}', flush=True)
kezdes = perf_counter()
tortenet = modell.fit(
    tanito_csomag,
    validation_data=validacios_csomag,  # Csak mérés, súlyfrissítés nélkül.
    epochs=epochok_szama,
    shuffle=False,  # A tanítócsomag már intézi a keverést.
    verbose=0,  # Hosszú napló helyett a callback rövid állapotjelzéseket ír.
    callbacks=[RovidJelzes()],
)
masodperc = perf_counter() - kezdes

# 6. MÉRÉS ÉS KÉPEK – nincs új tanítás; az utolsó súlyokkal rekonstruálunk.
# A segéd a görbéket, a számokat és a saját rekonstrukciókat is elmenti.
mappa = uj_mappa(__file__)
tanitas_mentese(mappa, modell, tortenet, adatok,
                {'epochok': epochok_szama, 'szuk_keresztmetszet': szuk_keresztmetszet,
                 'kezdeti_sulyok': azonosito, 'veletlen_mag': 42, 'batch_meret': 32}, masodperc)
