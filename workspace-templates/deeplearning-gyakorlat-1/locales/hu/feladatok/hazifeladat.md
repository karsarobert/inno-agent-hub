# Házi feladat — Deep Learning 1. gyakorlat, 1. alkalom (differenciált)

Téma: **a neurális hálózatok története, gépi tanulás alapjai** + egyszerű MNIST-demó.
(A túltanulást és a görbe-elemzést a tematikában **később** tárgyaljuk — ezért itt még nem szerepel.)

Válaszd ki a saját szintedhez illő részt. Az **alap** mindenkinek kötelező; a **fejlesztő** és a **bővítő** a haladóknak.

---

## Alap (mindenki) — kötelező

1. A `feladatok/zaro_feladat.py` futtatása után **írd le a végső teszt-pontosságot** (`val_accuracy`), és a `model.summary()` paraméterszámát.
2. **Magyarázd meg 3-4 mondatban:** mit jelent „tanítás" a demóban (mi történik a `fit` során)?
3. Válassz **2 történeti mérföldkövet** az 1. alkalom anyagából (pl. perceptron, MLP), és **1-1 mondatban** foglald össze, miért fontosak a mait modellek számára.

---

## Fejlesztő (az alap felett)

4. Adj meg egy **tetszőleges számjegyet** az MNIST-ből (pl. `X_train[i]`): milyen **alakra** került, hány dimenziós, és mekkora a **legnagyobb értéke** a normalizálás után?
5. Nézd meg az `Y_train[0]` one-hot vektort, és magyarázd el, **miért alkalmas ez a forma** az osztályozás kimenetéül.
6. **(Elosztott ismétlés)** idézd fel a NumPy-ból az `astype` és a `reshape` szerepét — 1-1 rövid egysoros példával igazold, mit csinál mindkettő.

---

## Bővítő (önálló kutatás)

7. Keress rá röviden, **mi volt a perceptron korlátja** (a XOR-probléma kapcsán), és miért lett ezért szükséges a többrétegű (MLP) hálózat.
8. Próbálj ki egy **2 rejtett rétegű** változatot a demóra (pl. `Dense(128, relu)` → `Dense(128, relu)` → `Dense(10, softmax)`), és kövesd nyomon, hogyan változik a `model.summary()` paraméterszáma.
9. Nézd meg a **`!nvidia-smi` / `tf.config.list_physical_devices('GPU')`** kimenetét, és írd le: van-e GPU, és miért hasznos a mély tanulásban.

---

## Beadás / következő alkalomra

- Hozd magaddal a demó futtatásának eredményét (végső pontosság + paraméterszám).
- A következő téma: **a perceptron-modell és a mély/előrecsatolt neurális hálózatok**.
- Minden szintnél a beadott megoldás tartalmazza a **mérhető adatokat** (accuracy, shape, max-érték), nem csak a kódot.