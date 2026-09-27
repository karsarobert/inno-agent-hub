"""Opcionális, számszerű BN-bemutató. A gamma és beta itt kézzel állítható."""
from segedletek import np, uj_mappa, adatok_mentese, oszlop_abra, kesz

bemenetek = np.array([1.0, 2.0, 3.0, 4.0])
gamma = 1.0
beta = 0.0
tanitasi_mod = True
tarolt_atlag = 2.5
tarolt_variancia = 1.25
epszilon = 0.001

if tanitasi_mod:
    atlag = np.mean(bemenetek)
    variancia = np.mean((bemenetek - atlag) ** 2)
else:
    atlag = tarolt_atlag
    variancia = tarolt_variancia
if variancia < 0:
    raise SystemExit("A variancia nem lehet negatív.")
normalizalt = (bemenetek - atlag) / np.sqrt(variancia + epszilon)
kimenetek = gamma * normalizalt + beta
print("Használt átlag és variancia:", atlag, variancia)
print("Normalizált értékek:", np.round(normalizalt, 4))
print("Végső kimenet:", np.round(kimenetek, 4))
print("A tárolt statisztikák szemléltető értékek. Ebben a programban nincs tanulás.")
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"gamma": gamma, "beta": beta, "tanitasi_mod": tanitasi_mod,
                       "hasznalt_atlag": float(atlag), "hasznalt_variancia": float(variancia)},
               ["bemenet", "normalizalt", "kimenet"], zip(bemenetek, normalizalt, kimenetek))
oszlop_abra(mappa, bemenetek, kimenetek, "Batch normalization négy értéken", "batch_normalization.png")
kesz(mappa)
