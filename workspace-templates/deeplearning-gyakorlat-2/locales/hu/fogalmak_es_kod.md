# Deep Learning 2026 – fogalom és kód

Ez a segédlet az órai beszélgetéshez és későbbi ismétléshez készült.
Nem kell a teljes kód minden technikai részletét megtanulnod.

## 1. Adat, paraméter, becslés

| Matematikai jel | A kódban | Szerep |
|---|---|---|
| x | `bemenet` | Az adatból ismert bemenet |
| y | `celertek` | A tanítóadatból ismert helyes cél |
| w | `suly` | Módosítható modellparaméter |
| ŷ | `becsles` | A modell által kiszámított kimenet |
| L | `veszteseg` | A becslés és cél eltérését mérő érték |
| η | `TANULASI_RATA` | A gradiensalapú lépés mértékét szabályozó beállítás |

A modell: ŷ = wx. Az adott tanítópélda vesztesége: L(w) = (wx − y)².
Ha x = 1 és y = 3, akkor L(w) = (w − 3)². Ebben a példában x és y rögzített,
w változik. A `suly` egy szám; a veszteségfüggvény külön fogalom.

```python
becsles = suly * bemenet
veszteseg = (becsles - celertek) ** 2
gradiens = 2 * (becsles - celertek) * bemenet
```

Az utolsó sor a négyzetes hiba w szerinti deriváltja. A `**` hatványozás.
Az `uj_suly` kiszámítása után az új becslést és veszteséget is újra kell számolni.
Az y ismerete teszi lehetővé a felügyelt tanítást. Új, címke nélküli adatnál
becslést adhatunk, de az ismert célérték nélkül a valódi hibát nem tudjuk kiszámítani.

## 2. Vektor, mátrix és batch

| Kifejezés | Értelmezés |
|---|---|
| `np.array([1.0, 2.0, -1.0])` | Háromelemű vektor |
| `np.array([[1.0, 2.0, -1.0]])` | Egy minta, három jellemző: (1, 3) |
| `.shape` | A tömb méreteit tartalmazó tuple |
| `rejtett_sulyok @ bemenetek` | A példában mátrix–vektor szorzás |
| `np.maximum(0.0, ertekek)` | Elemenkénti ReLU |
| `adatok[0, :3]` | Az első sor első három eleme |
| `becslesek[0, 0]` | Az első minta első kimenete |

A G02_02 súlymátrixa (2, 3) alakú: két neuron, három bemenet.
A Keras ugyanazt a kernelt (3, 2) alakban tárolja; sorban adja át a mintákat.
Ez eltérő elrendezés, ugyanazzal a számítási tartalommal.

Egy Dense-réteg n bemenettel és m neuronnal, bias használatával n · m + m
tanulható paramétert tartalmaz. A 3 → 2 → 1 hálózatban (3 · 2 + 2) +
(2 · 1 + 1) = 11 paraméter van. A minták száma nem növeli a paraméterszámot.

## 3. A Keras-hívások különböző szerepei

| Hívás | Mit csinál? | Mit kapunk? |
|---|---|---|
| `keras.Input(shape=(3,))` | Megadja az egy mintához tartozó jellemzőalakot | A bemenet leírása |
| `layers.Dense(2, activation="relu")` | Súlyozott összeget, biast és ReLU-t használó réteget ír le | Két kimeneti érték mintánként |
| `set_weights([kernel, bias])` | Kézzel beállítja a réteg paramétereit | Rögzített súlyok; ez önmagában nem tanítás |
| `compile(...)` | Kiválasztja a tanítás veszteségét, optimalizálóját és metrikáit | Tanításra konfigurált modell |
| `fit(...)` | Adatok alapján frissíti a súlyokat | Betanított modellállapot és History objektum |
| `predict(...)` | Előreterjesztést végez a jelenlegi súlyokkal | Mintánkénti becslések |
| `evaluate(...)` | Becslésekből és ismert célokból összesített mutatókat számít | Veszteség, illetve megadott metrikák |

Egy **epoch** a teljes tanítóhalmaz egyszeri feldolgozása. Egy **mini-batch**
az egy frissítéshez használt mintacsoport. A mintákból álló batch nem azonos
a neuronszámmal. A `learning_rate` tanítási beállítás; nem egy tanult súly.

## 4. Regresszió és osztályozás

| Szempont | Boros regresszió | Négyosztályos példa |
|---|---|---|
| Bemenet | 11 mérési jellemző | 2 koordináta |
| Cél | Minőségi pontszám | One-hot osztályvektor |
| Kimenet | Egy lineáris érték | Négy softmax-érték |
| Veszteség | MAE | Kategorikus keresztentrópia |
| Előrejelzés értelmezése | Becsült pontszám | `argmax` alapján választott osztály |

A MAE a célérték egységében mér; az accuracy a helyes osztályozások aránya.
A keresztentrópia és az accuracy más tulajdonságot mutat. Előbbi változhat
akkor is, amikor a legnagyobb valószínűségű osztály, így az accuracy változatlan.

```python
becsult_osztalyok = valoszinusegek.argmax(axis=1)
```

Az `axis=1` soronként vizsgálja az oszlopokat. A hívás indexet ad vissza,
nem a legnagyobb valószínűség számértékét. Az `argmax(axis=0)` más feladatot
végezne: oszloponként választana a minták közül.

## 5. Tanítás, validáció és teszt

- A tanítóadat alapján módosítjuk a modell súlyait és illesztjük a skálázót.
- A validációs eredmény alapján figyeljük a tanulást és választunk beállításokat.
- A külön tartott teszt a rögzített tanítási eljárás végső értékeléséhez tartozik.

A szerepet a felhasználás határozza meg. Ha egy „teszt” nevű halmaz eredményét
használjuk modellválasztásra, az a folyamatban validációs halmazként működik.
A `fit_transform` tanulja meg a skálázás szabályát; a `transform` már csak
alkalmazza azt. Az új adatok kilóghatnak a tanítóadatok tartományából.

## 6. A tanulási görbék olvasása

`tortenet.history` egy szótár, amelyben például a `loss` és `val_loss`
epochonkénti listája szerepel. A DataFrame ezekből táblázatot készít.
A görbe vízszintes tengelye az epoch, a függőleges a választott veszteség.

Mindkét görbe csökkenése kedvező jel. Ha a tanítási tovább csökken, miközben
a validációs tartósan emelkedik, az túlilleszkedésre utalhat. Egyetlen kiugrásból
nem vonunk le biztos következtetést, és a lapos görbe sem bizonyít optimális modellt.

A korai leállítás a kijelölt érték javulását figyeli. A `patience` a javulás
nélkül megengedett epochok száma, a `min_delta` a javulás abszolút küszöbe.
A `restore_best_weights` visszaállítja a követett legjobb eredmény súlyait.
A korábbi naplósorok ettől nem íródnak át. Ezért külön számítjuk ki a
visszaállított modell validációs MAE-jét.

## 7. Osztályindex és érték

| Index | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| Szemléltető softmax-becslés | 0,05 | 0,10 | 0,80 | 0,05 |

A harmadik elem indexe 2. A predict bemeneti jellemzőket kap; a fentihez
hasonló becslési vektort visszaadja. Az argmax eredménye itt 2, nem 0,80.

A teljes programok bemutatása a PROGRAM_BEMUTATOK.md-ben olvasható.
A számításokat a szemlelteto.html-ben követheted; ez nem módosítja a kódodat.
