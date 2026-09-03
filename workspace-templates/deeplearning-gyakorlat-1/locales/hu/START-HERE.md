# START-HERE — Indítási útmutató (olvasd el először!)

## 1. Környezet választása

Ez a gyakorlat **vegyes környezetben** is futtatható: Google Colab (felhő, GPU) vagy saját géped (lokális). Válaszd ki, melyiket használod.

### A) Google Colab (ajánlott, ha nincs beállított gépi környezeted)
1. Nyisd meg a [Colabot](https://colab.research.google.com/).
2. Hozz létre új notebookot (**Fájl → Új notebook**).
3. Másold be a `gyakorlat/dl1_megoldott.py` tartalmát cellánként, **vagy** töltsd fel/linkeld a fájlt.
4. A notebook tetején lévő `!nvidia-smi` cella futtatása megmutatja, hogy elérhető-e GPU (`Runtime → Change runtime type → GPU`).

### B) Lokális környezet (saját gép, pl. PyCharm / VS Code)
- Javasolt külön virtuális környezetben:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install tensorflow numpy pandas matplotlib
```

- GPU-ellenőrzés lokálisan (a `dl1_megoldott.py` elején lévő, megjegyzett sor):

```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

Ha üres listát kapsz, nincs GPU — **nem gond**, a gyakorlat CPU-n is végigvihető (esetleg kicsit lassabb).

## 2. A gyakorlat menete

1. Nyisd meg a **`gyakorlat/dl1_megoldott.py`** fájlt, és futtasd cellánként, a tanárral lépésről lépésre.
2. Közben a **`gyakorlat/dl1_atlathatoanyag.md`** egy oldalon összefoglalja a kulcsfogalmakat.
3. A **`feladatok/zaro_feladat.py`** az órai záró feladat (rejtett réteges hálózat).
4. Otthon a **`feladatok/hazifeladat.md`** alapján dolgozz tovább.

## 3. Ha elakadsz
- Ellenőrizd a TensorFlow verziót: `import tensorflow as tf; print(tf.__version__)`.
- Győződj meg róla, hogy az adatok **normalizálva** vannak (`X_train.max()` legyen 1.0).
- A leggyakoribb hiba az **alakítás** (shape). A biztos képlet:

```python
# 28×28 kép → 784 hosszú vektor (60000 darab)
X_train = X_train.reshape(60000, -1)
X_test  = X_test.reshape(10000, -1)

# egész (0-255) → tizedes (0.0-1.0) számok
X_train = X_train.astype('float32') / 255
X_test  = X_test.astype('float32') / 255
```