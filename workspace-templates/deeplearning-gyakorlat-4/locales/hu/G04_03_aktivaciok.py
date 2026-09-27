"""Ugyanazok a bemenetek, különböző aktivációk. Itt nem tanítunk hálózatot."""
from segedletek import np, uj_mappa, adatok_mentese, aktivacio_abra, kesz

# BEÁLLÍTÁSOK
aktivacio = "sigmoid"       # További lehetőségek: "relu", "leaky_relu"
bemenetek = np.array([-6.0, -1.0, 0.0, 1.0, 6.0])
negativ_meredekseg = 0.1
beerkezo_gradiens = 2.0

if aktivacio not in {"sigmoid", "relu", "leaky_relu"}:
    raise SystemExit('Az aktivacio értéke: "sigmoid", "relu" vagy "leaky_relu".')
if not 0 < negativ_meredekseg <= 1:
    raise SystemExit("A negatív meredekség 0 és 1 közé essen, és ne legyen nulla.")

def fuggveny(z):
    if aktivacio == "sigmoid":
        return 1 / (1 + np.exp(-z))
    if aktivacio == "relu":
        return np.maximum(0, z)
    return np.where(z > 0, z, negativ_meredekseg * z)

def derivalt(z):
    if aktivacio == "sigmoid":
        ertek = fuggveny(z)
        return ertek * (1 - ertek)
    if aktivacio == "relu":
        return np.where(z > 0, 1.0, 0.0)
    return np.where(z > 0, 1.0, negativ_meredekseg)

kimenetek = fuggveny(bemenetek)
lokalis_derivaltak = derivalt(bemenetek)
visszaadott_gradiensek = beerkezo_gradiens * lokalis_derivaltak
print("Aktiváció:", aktivacio)
print("Bemenet | Kimenet | Lokális derivált | Visszaadott gradiens")
sorok = list(zip(bemenetek, kimenetek, lokalis_derivaltak, visszaadott_gradiensek))
for sor in sorok:
    print(" | ".join(f"{v: .6f}" for v in sor))
if aktivacio != "sigmoid":
    print("A 0 töréspontban a kód a bal ág értékét választja; ott általában nincs klasszikus derivált.")
mappa = uj_mappa(__file__)
adatok_mentese(mappa, {"aktivacio": aktivacio, "negativ_meredekseg": negativ_meredekseg,
                       "beerkezo_gradiens": beerkezo_gradiens, "bemenetek": bemenetek.tolist()},
               ["bemenet", "kimenet", "lokalis_derivalt", "visszaadott_gradiens"], sorok)
aktivacio_abra(mappa, fuggveny, derivalt, bemenetek)
kesz(mappa)
