# Kernel- és futáshelyreállítás

Ez a tutor kész útmutatója, nem plusz vizsga. Egyszerre egy cellát adj; a már igazolt megértés elfogadott marad.

## Kisebb próbák

Kernelújraindítás után E01 kell. B03/B04-hez B02; B05 önálló E01 után; B06-hoz B02 és B04. P/C/R/G-próbák E01 után önállóak. A kódokat a részletes leckéből teljesen másold; ne kérj hallgatói rekonstrukciót. R00/B01 fogalmi megértését ne kérdezd újra csak a kernel miatt.

## Teljesen új kontrollált kísérlet

Ha az adatok/állapotfájlok elvesztek vagy az aktuális fit megszakadt, a biztonságos teljes újrafuttatás: E01, D01, D02, D03, M01, M02, M03, M04, M05. A M01/M02 friss kétmodelles kísérletet indít, felülírja az induló súlyfájlokat; ne használd M02-t félúti helyreállításhoz. A régi legjobb súlyfájlok teljes 6 epochás újfutás végén frissülnek, az új history csak a mostani futásra vonatkozik. A tesztet ne használd hangolásra.

## Az első tanítás kész, a második még nem kezdődött el

Csak ha a helyi `dl9_results` fájlok megvannak ÉS M03 befejezése igazolt. Egyenként futtasd E01,D01,D02,D03,M01 celláit. M02-t NE futtasd, mert felülírná az eredeti induló állapotot. Ezután add az alábbi RC01 helyreállítást; utána M04 jön. Az eredeti két kezdeti súlyfájlból állítja vissza a közös indulást, a kész alapmodellcheckpointját és historyját is helyrehozza. Ez nem részben lefutott M04 folytatása.

```python
from types import SimpleNamespace
alapmodell_fajl = munkamappa / "without_bn_best.weights.h5"
bn_fajl = munkamappa / "with_bn_best.weights.h5"
required = [munkamappa / "without_bn_initial.weights.h5", munkamappa / "with_bn_initial.weights.h5",
            alapmodell_fajl, munkamappa / "baseline_history.json"]
if not all(path.exists() for path in required):
    raise RuntimeError("Required local files are missing. Restart the controlled comparison at M01.")
alapmodell.load_weights(munkamappa / "without_bn_initial.weights.h5")
bn_modell.load_weights(munkamappa / "with_bn_initial.weights.h5")
for modell in [alapmodell, bn_modell]:
    modell.compile(optimizer=keras.optimizers.Adam(1e-3),
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
alapmodell.load_weights(alapmodell_fajl)
alapmodell_tortenet = SimpleNamespace(history=json.loads((munkamappa / "baseline_history.json").read_text()))
print("Baseline completed; BN model restored to the saved common initial state.")
```

## Mindkét tanítás kész

E01,D01,D02,D03,M01, majd RC01 után az alábbi RC02 következik. A betöltött állapotból M05 folytatható, ha még nem történt választás. Ha van korábbi selection.json, RC02 megőrzi a teszt ELŐTTI döntést: ne válassz újra későbbi teszteredmény alapján. A korábban el nem végzett V01,V02,Z01,Z02 következhet. Ha a tesztet már kiértékeltétek, az eredményeket a meglévő results.json-ból idézd; szükség esetén ugyanazon súlyok kiértékelése technikai visszaállítás, nem új kísérlet vagy hangolás. A V02 újrafuttatása a mátrixot helyreállítja; nem kell a már értett fogalmakat újrakérdezni.

```python
required = [bn_fajl, munkamappa / "bn_history.json"]
if not all(path.exists() for path in required):
    raise RuntimeError("The second training run is not documented as complete. Do not claim an exact mid-fit resume.")
bn_modell.load_weights(bn_fajl)
bn_tortenet = SimpleNamespace(history=json.loads((munkamappa / "bn_history.json").read_text()))
selection_path = munkamappa / "selection.json"
if selection_path.exists():
    stored_selection = json.loads(selection_path.read_text())
    validacios_eredmenyek = stored_selection["validation"]
    valasztott_nev = stored_selection["selected"]
    valasztott_modell = bn_modell if valasztott_nev == "with_bn" else alapmodell
    print("Saved pre-test selection preserved:", valasztott_nev)
else:
    print("Both models restored. Run M05 before any test.")
```
