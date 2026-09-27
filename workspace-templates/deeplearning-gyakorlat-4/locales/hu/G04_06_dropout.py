"""Inverted dropout nyolc értéken. A tanítási mód itt nem hálózattanítást jelent."""
from segedletek import np, uj_mappa, adatok_mentese, oszlop_abra, kesz

# BEÁLLÍTÁSOK – a rögzített mag miatt az alapfutás megismételhető.
kiesesi_arany = 0.5
tanitasi_mod = True
veletlen_mag = 42
bemenetek = np.array([0.2, 0.5, 1.3, 0.8, 1.1, 0.4, 0.7, 1.0])

if not 0 <= kiesesi_arany <= 0.9:
    raise SystemExit("A kiesési arány ebben a bemutatóban 0 és 0.9 közötti legyen.")
veletlen = np.random.default_rng(veletlen_mag)
if tanitasi_mod:
    maszk = veletlen.random(len(bemenetek)) >= kiesesi_arany
    kimenetek = bemenetek * maszk / (1 - kiesesi_arany)
else:
    maszk = np.ones(len(bemenetek), dtype=bool)
    kimenetek = bemenetek.copy()

print("Üzemmód:", "tanítási" if tanitasi_mod else "kiértékelési")
print("Bemenet:", bemenetek)
print("Maszk:", maszk.astype(int) if tanitasi_mod else "nincs maszkolás")
print("Kimenet:", np.round(kimenetek, 4))
print("Kiesett elemek száma:", int(np.sum(~maszk)))
print("A nulla érték itt ideiglenes nullázás; nem törölt neuron vagy súly.")
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"kiesesi_arany": kiesesi_arany, "tanitasi_mod": tanitasi_mod,
                       "veletlen_mag": veletlen_mag, "kimenetek": kimenetek.tolist()},
               ["bemenet", "maszk", "kimenet"], zip(bemenetek, maszk.astype(int), kimenetek))
oszlop_abra(mappa, bemenetek, kimenetek,
            "Dropout – " + ("tanítási mód" if tanitasi_mod else "kiértékelési mód"), "dropout.png")
kesz(mappa)
