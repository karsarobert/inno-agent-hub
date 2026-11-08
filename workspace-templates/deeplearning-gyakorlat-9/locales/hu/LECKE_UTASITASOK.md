# Részletes lecke · teljes kódok

A pontok sorrendje kötött. Egy aktív cella, majd várakozás. Az alábbi kérdések a hallgató saját kimenetére vonatkoznak. Z01 kérdéseit egyenként kérdezd.

## [E01] Környezet és GPU

A teljes kód készen van. Colabban a menüben válassz GPU-s futtatókörnyezetet még az adatok betöltése előtt. A seed a véletlen műveletek kiindulását rögzíti; eltérő eszközök között nem ígér bitazonos tanítást. A Path mappát jelöl, ide kerülnek a helyi checkpointok. Helyi Jupyterben CPU is használható, lassabb tanítással.

```python
import os
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

SEED = 2026
keras.utils.set_random_seed(SEED)
try:
    import google.colab
    colabban = True
except ImportError:
    colabban = False
gpu_lista = tf.config.list_physical_devices("GPU")
print("Environment:", "Colab" if colabban else "Local Jupyter")
print("TensorFlow:", tf.__version__)
print("GPU:", gpu_lista)
if colabban and not gpu_lista:
    print("Runtime -> Change runtime type -> Hardware accelerator -> GPU -> Save")
    raise RuntimeError("Select a GPU in Colab and rerun E01.")
munkamappa = Path("dl9_results")
munkamappa.mkdir(exist_ok=True)
EPSILON = 1e-3
```

**Kérdés / minimális bizonyíték:** Küldd el a környezet, TensorFlow és GPU sorokat. Milyen eszközön fogsz dolgozni?


## [B01] Megfigyelés az új BN-bemutatóban

Nyisd meg a mellékelt BN HTML-t a böngészőben. A topológia panelen válts N1-ről N2-re, majd nézd meg a mini-batch mátrixát. Egy sor egy minta, az oszlop egy neuron súlyozott összege a különböző mintákon. Ezután módosíts egy bemeneti értéket, és figyeld a kiválasztott oszlop statisztikáját. Ez beszélgetési pont, nincs futtatandó cella.

**Kérdés / minimális bizonyíték:** A mátrixban mely értékekből számolódik egy kiválasztott neuron átlaga?


## [B02] Minták és jellemzők: axis=0

A kis tömböt egy réteg két neuronjának aktiváció előtti értékeiként olvassuk: négy sor = négy minta, két oszlop = két neuron. A mean(axis=0) a sorok mentén, külön-külön oszloponként számol. A var itt a teljes köteg varianciája (ddof=0). Az epsilon a gyök alatt kis stabilizáló tag; nem min–max skálázást végzünk.

```python
mintak = np.array([[2., 10.], [4., 18.], [6., 20.], [8., 40.]], dtype=np.float32)
atlag = mintak.mean(axis=0)
variancia = mintak.var(axis=0)
normalizalt = (mintak - atlag) / np.sqrt(variancia + EPSILON)
print("Feature means:", atlag)
print("Feature variances:", variancia)
print("Normalized means:", normalizalt.mean(axis=0))
print("Normalized variances:", normalizalt.var(axis=0))
assert np.allclose(normalizalt.mean(axis=0), 0., atol=1e-6)
```

**Kérdés / minimális bizonyíték:** A kiírt átlagok és varianciák alapján mit kezeltünk külön? Küldd el a négy statisztikai sort.


## [B03] Gamma és beta jellemzőnként

A két elemű gamma és beta a két oszlophoz tartozik. A NumPy a (2,) alakú értékeket minden sorra alkalmazza: ez a broadcasting. A normalizált értékek skálázása és eltolása tanulhatóvá teszi a kimeneti tartományt; nem kötelező [0,1]-ben maradniuk.

```python
gamma = np.array([2., 0.5], dtype=np.float32)
beta = np.array([1., -3.], dtype=np.float32)
sk_alakitott = gamma * normalizalt + beta
print("Output means:", sk_alakitott.mean(axis=0))
print("Output standard deviations:", sk_alakitott.std(axis=0))
print("Output:\n", sk_alakitott)
```

**Kérdés / minimális bizonyíték:** Melyik oszlop eloszlása lett szélesebb, és melyik tolódott negatív átlag köré? Használd a kiírt értékeket.


## [B04] Valódi Keras BN: súlyok és mozgóstatisztikák

A réteg első hívása létrehozza az állapotot. A gamma/beta tanulható, a moving_mean/moving_variance nem gradienssel tanul, hanem tanítási híváskor frissül. Itt momentum=0.5 a szemléltetéshez: új = 0.5×régi + 0.5×batch-statisztika. A training=True az aktuális kötegből normalizál; önmagában nem optimalizálja a gamma/beta értékét. A numpy() a TensorFlow-tenzort megjeleníthető tömbbé alakítja.

```python
bn = layers.BatchNormalization(momentum=0.5, epsilon=EPSILON)
_ = bn(mintak, training=False)
elotte = [v.numpy().copy() for v in bn.weights]
tanitasi_kimenet = bn(mintak, training=True).numpy()
print("Trainable:", [v.name for v in bn.trainable_weights])
print("Non-trainable:", [v.name for v in bn.non_trainable_weights])
for valtozo, regi in zip(bn.weights, elotte):
    print(valtozo.name, "before:", regi, "after:", valtozo.numpy())
print("Matches NumPy:", np.allclose(tanitasi_kimenet, normalizalt, atol=1e-5))
assert np.allclose(tanitasi_kimenet, normalizalt, atol=1e-5)
```

**Kérdés / minimális bizonyíték:** Mely állapotértékek változtak a hívásban, és miért maradt a gamma/beta az induló értéken?


## [B05] Ugyanaz a minta más batch-társakkal

A két batch első eleme egyaránt 3, a társai mások. A training=True hívás megváltoztatja a mozgóstatisztikákat is, ezért a set_weights minden vizsgálat előtt ugyanazt az állapotot tölti vissza. Inferenciában a rögzített moving_mean és moving_variance számít, nem a társak. Így nem hasonlítunk véletlenül eltérő állapotú rétegeket.

```python
batch_a = np.array([[3.], [1.], [5.], [7.]], dtype=np.float32)
batch_b = np.array([[3.], [20.], [22.], [24.]], dtype=np.float32)
tars_bn = layers.BatchNormalization(epsilon=EPSILON)
_ = tars_bn(batch_a, training=False)
rogzitett_allapot = tars_bn.get_weights()
kimenetek = {}
for mod in [True, False]:
    ertekek = []
    for batch in [batch_a, batch_b]:
        tars_bn.set_weights(rogzitett_allapot)
        ertekek.append(float(tars_bn(batch, training=mod).numpy()[0, 0]))
    kimenetek[str(mod)] = ertekek
    print("training=", mod, "first sample outputs:", ertekek)
tars_bn.set_weights(rogzitett_allapot)
assert not np.isclose(*kimenetek["True"])
assert np.isclose(*kimenetek["False"])
```

**Kérdés / minimális bizonyíték:** Hogyan változott az első minta kimenete tanításban, illetve inferenciában a társak cseréjével?


## [B06] BN befagyasztása: kapcsolat a 8. leckével

A trainable a súlyok optimalizálhatóságáról, a training a hívás módjáról szól. BN esetében speciális kapcsolat van: trainable=False inferencia-viselkedést is jelent a Kerasban, akkor is, ha a hívás training=True. Ezt a B04-ben már felépített külön rétegen ellenőrizzük; nem az összes rétegre érvényes szabályként tanuljuk.

```python
bn.trainable = False
fagyasztott_allapot = bn.get_weights()
fagyasztott_kimenet = bn(mintak, training=True).numpy()
inferencia_kimenet = bn(mintak, training=False).numpy()
valtozatlan = all(np.array_equal(a, b) for a, b in zip(fagyasztott_allapot, bn.get_weights()))
print("Trainable weights:", len(bn.trainable_weights))
print("BN state unchanged:", valtozatlan)
print("Matches inference:", np.allclose(fagyasztott_kimenet, inferencia_kimenet))
assert valtozatlan and np.allclose(fagyasztott_kimenet, inferencia_kimenet)
```

**Kérdés / minimális bizonyíték:** A két ellenőrzés alapján mi történik a befagyasztott BN állapotával és kimenetével?


## [P01] Lokális és globális pooling

A shape sorrendje: batch, magasság, szélesség, csatorna. A kis kétcsatornás képen a MaxPooling2D(2) 2×2-es ablakokból vesz maximumot, alapból 2-es lépéssel. A globális változatok az összes térbeli helyből adnak egy értéket csatornánként. A keepdims=True csak az 1×1 méreteket tartaná meg.

```python
kep = np.arange(32, dtype=np.float32).reshape(1, 4, 4, 2)
for name, reteg in [
    ("Local max", layers.MaxPooling2D(2)),
    ("Global max", layers.GlobalMaxPooling2D()),
    ("Global average", layers.GlobalAveragePooling2D()),
]:
    eredmeny = reteg(kep).numpy()
    print(name, "shape:", eredmeny.shape, "values:\n", eredmeny)
```

**Kérdés / minimális bizonyíték:** Mely dimenziók tűntek el a globális poolingnál, és megmaradt-e a két csatorna?


## [P02] Flatten-fej és GAP-fej paraméterszáma

Négy kész kicsi modell csak a fejet vizsgálja:8 csatorna és 5 kimenet, két térbeli méret. A Flatten az összes helyet bemenetté teszi a Dense számára. A GAP előbb csatornánként átlagol. Ettől még egy teljes modell Input-alakja korlátozhatja a képméretet; itt külön építünk 8×8 és 16×16 modelleket.

```python
for meret in [8, 16]:
    for tipus in ["Flatten", "GAP"]:
        inputs = keras.Input(shape=(meret, meret, 8))
        jellemzok = layers.Flatten()(inputs) if tipus == "Flatten" else layers.GlobalAveragePooling2D()(inputs)
        fej = keras.Model(inputs, layers.Dense(5)(jellemzok))
        print("Size:", meret, "Head:", tipus, "Parameters:", fej.count_params())
```

**Kérdés / minimális bizonyíték:** Melyik fej paraméterszáma nőtt a térbeli mérettel? Mit mutat a négy kiírás?


## [C01] 1×1 konvolúció: csatornakeverés

A kernel 1×1, stride 1; minden térbeli helyen ugyanazt a tanulható csatornakeverést használja. Ez nem max pooling a csatornákon. A use_bias=False miatt csak a8×3 súly van.

```python
csatorna_bemenet = tf.ones((1, 6, 6, 8))
keveres = layers.Conv2D(3, 1, use_bias=False)
csatorna_kimenet = keveres(csatorna_bemenet)
print("Input:", csatorna_bemenet.shape, "Output:", csatorna_kimenet.shape)
print("Parameters:", keveres.count_params())
```

**Kérdés / minimális bizonyíték:** A bemeneti és kimeneti shape alapján mi változott, és mi maradt meg?


## [R00] Megfigyelés a skip connection-bemutatóban

Nyisd meg a skip connection HTML-t. Válaszd az identitás módot: F(x)=0. Az élő vektorpanelen figyelj a negatív−1 bemenetre: külön oszlop mutatja a H=x+F összeget és a y=ReLU(H) kimenetet. Kapcsold ki, majd vissza a skipet. A degradációs ábra és a hiba-felszín animáció szemléltetés, nem a te notebookod tanítási mérése; a mélyebb modell javulása nem garancia.

**Kérdés / minimális bizonyíték:** A negatív bemenetnél az összeadás előtti/utáni és a ReLU utáni értékek közül hol teljesül az identitás F(x)=0 esetén?


## [R01] Valódi reziduális blokk: az összeg és a ReLU

A Functional API-ban a tenzorokból két ágat építünk. A reziduális ág Conv–BN–ReLU–Conv–BN; a második konvolúció most szándékosan nulla súlyú, így F=0. Az Add([x,F]) elemenként összead, nem csatornákat fűz össze. A próbamodell három kimenete külön mutatja a korrekciót, az összeget és a végső ReLU-t. Ez egy blokkpróba, nem teljes ResNet tanítása.

```python
blokk_bemenet = keras.Input(shape=(4, 4, 2))
ag = layers.Conv2D(2, 3, padding="same", use_bias=False)(blokk_bemenet)
ag = layers.BatchNormalization(epsilon=EPSILON)(ag)
ag = layers.ReLU()(ag)
ag = layers.Conv2D(2, 3, padding="same", use_bias=False, kernel_initializer="zeros")(ag)
rezidualis = layers.BatchNormalization(epsilon=EPSILON)(ag)
osszeg = layers.Add()([blokk_bemenet, rezidualis])
aktivalt = layers.ReLU()(osszeg)
blokk_proba = keras.Model(blokk_bemenet, [rezidualis, osszeg, aktivalt])
blokk_minta = np.linspace(-2., 2., 32, dtype=np.float32).reshape(1, 4, 4, 2)
korrekcio, osszeg_kimenet, relu_kimenet = [v.numpy() for v in blokk_proba(blokk_minta, training=False)]
print("Maximum absolute F:", np.max(np.abs(korrekcio)))
print("Maximum absolute H-x:", np.max(np.abs(osszeg_kimenet - blokk_minta)))
print("First value x, H, ReLU(H):", blokk_minta.flat[0], osszeg_kimenet.flat[0], relu_kimenet.flat[0])
assert np.allclose(korrekcio, 0.) and np.allclose(osszeg_kimenet, blokk_minta)
```

**Kérdés / minimális bizonyíték:** A két eltérésellenőrzés és a negatív minta alapján meddig őrizte meg a blokk változatlanul a bemenetet?


## [R02] Alakillesztés projekciós skippel

Az Add előtt minden dimenziónak egyeznie kell. A tanult ág stride 2-vel felezi a 16×16 térbeli méretet és 4-ről 8-ra váltja a csatornákat. A skip 1×1 konvolúciója ugyanilyen stride-dal igazít. A rétegek most először megmutatják az eltérést, majd a javítást; nem futtatunk szándékosan hibás Add-ot.

```python
projekcio_bemenet = tf.ones((1, 16, 16, 4))
tanult_ag = layers.Conv2D(8, 3, strides=2, padding="same", use_bias=False)(projekcio_bemenet)
projekcio = layers.Conv2D(8, 1, strides=2, padding="same", use_bias=False)
rovidites = projekcio(projekcio_bemenet)
projekcios_osszeg = layers.Add()([tanult_ag, rovidites])
print("Original:", projekcio_bemenet.shape)
print("Branch:", tanult_ag.shape, "Projection:", rovidites.shape)
print("Add output:", projekcios_osszeg.shape, "Projection parameters:", projekcio.count_params())
assert tanult_ag.shape == rovidites.shape == projekcios_osszeg.shape
```

**Kérdés / minimális bizonyíték:** Miért nem elég itt a bemenetet közvetlenül hozzáadni az ághoz? Használd a három shape-et.


## [R03] Gradienspróba: segítség, nem garancia

A GradientTape automatikusan követi a with-blokkban végzett műveleteket, a watch megjelöli a bemenetet, a gradient az eredmény érzékenységét számolja. Három egyszerű skalárblokkot ismétlünk: simaág a×x, reziduáliság x+a×x. Ez szemléltető számítás, nem hálózattanítás; nem kell deriválni. A−1 esetben az ág és az identitás hatása kiolthatja egymást. A végén a negatív bemenet utáni ReLU-t is külön mérjük.

```python
for egyutthato in [0.25, 0., -1.]:
    ertek = tf.constant(2.)
    with tf.GradientTape(persistent=True) as szalag:
        szalag.watch(ertek)
        sima, atkotes = ertek, ertek
        for _ in range(3):
            sima = egyutthato * sima
            atkotes = atkotes + egyutthato * atkotes
    print("a:", egyutthato, "plain gradient:", float(szalag.gradient(sima, ertek)),
          "skip gradient:", float(szalag.gradient(atkotes, ertek)))
    del szalag
negativ = tf.constant(-2.)
with tf.GradientTape() as szalag:
    szalag.watch(negativ)
    relu_utan = tf.nn.relu(negativ + 0. * negativ)
print("Negative identity plus ReLU gradient:", float(szalag.gradient(relu_utan, negativ)))
```

**Kérdés / minimális bizonyíték:** Melyik kiírt eset cáfolja, hogy a skip mindig pontosan 100%-os, nem nulla gradienst biztosít?


## [G01] Dropout tanításban és inferenciában

A Dropout(.5) tanításkor véletlen aktivációkat nulláz, a megmaradókat 1/(1−.5)-tel skálázza. Inferenciában átadja a bemenetet. A két tanítási hívás rendszerint más maszkot kap; a véletlen egyezés sem hiba. Ez külön próba, a két összehasonlított CNN-be nem kerül Dropout.

```python
dropout = layers.Dropout(0.5, seed=SEED)
egyesek = tf.ones((2, 8))
print("Training call 1:\n", dropout(egyesek, training=True).numpy())
print("Training call 2:\n", dropout(egyesek, training=True).numpy())
print("Inference:\n", dropout(egyesek, training=False).numpy())
```

**Kérdés / minimális bizonyíték:** Miben tér el az inferencia eredménye a tanítási hívásokétól?


## [G02] L2: veszteséghez adott büntetés

A regularizers.L2(.01) a súlynégyzetek összegének.01-szeresét számolja. A modell tanításakor ezt a regularizációs veszteséget az adatveszteséghez adjuk. Itt külön számpélda: nem állítjuk, hogy Adam melletti L2 mindenben azonos AdamW leválasztott weight decay műveletével.

```python
weights = tf.constant([1., -2.])
l2 = keras.regularizers.L2(0.01)
adatveszteseg = 0.7
buntetes = float(l2(weights))
print("Data loss:", adatveszteseg, "Penalty:", buntetes, "Total:", adatveszteseg + buntetes)
print("Penalty after doubling weights:", float(l2(2. * weights)))
```

**Kérdés / minimális bizonyíték:** Mit adott hozzá az L2 az adatveszteséghez, és mi történt a súlyok kétszerezésekor?


## [D01] CIFAR-10: képek és címkék

Az eredeti CIFAR-10 tanítórésze 50000, tesztrésze 10000 színes 32×32 kép. A load_data letölti vagy helyi gyorsítótárból olvassa. A reshape(-1) a címkeoszlopot egy dimenzióra alakítja, nem változtat a kategórián. Az imshow nyers 0–255 pixeleket jelenít meg; a későbbi Rescaling a modell része lesz.

```python
(osszes_kep, osszes_cimke), (teszt_kepek_forras, teszt_cimkek_forras) = keras.datasets.cifar10.load_data()
osszes_cimke = osszes_cimke.reshape(-1)
teszt_cimkek_forras = teszt_cimkek_forras.reshape(-1)
osztalynevek = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
print("Original training:", osszes_kep.shape, osszes_cimke.shape)
print("Original test:", teszt_kepek_forras.shape, teszt_cimkek_forras.shape)
print("Labels:", np.unique(osszes_cimke), "Pixels:", osszes_kep.dtype, osszes_kep.min(), osszes_kep.max())
fig, axes = plt.subplots(1, 5, figsize=(10, 2.5))
for index, axis in enumerate(axes):
    axis.imshow(osszes_kep[index])
    axis.set_title(osztalynevek[int(osszes_cimke[index])])
    axis.axis("off")
plt.tight_layout()
plt.show()
```

**Kérdés / minimális bizonyíték:** Mit jelent az első kép 32×32×3 alakja, és hányféle egész címke látható?


## [D02] Kész segédfüggvény: elkülönített halmazok

A felosztas_elokeszitese függvényt a cella már teljes egészében definiálja, nem kell megírnod. Bemenete a címkevektor és a seed. Osztályonként megkeveri az eredeti tanítóindexeket, az első 800-at tanításhoz, a következő 200-at validációhoz adja vissza két indextömbben. A hívás: tanito_indexek, validacios_indexek = felosztas_elokeszitese(osszes_cimke, SEED). A külön teszt_indexek az eredeti tesztrészből 200/osztályt választ. Az azonos számértékű index két külön forráshalmazban nem ugyanaz a kép. A split_indices.npz a helyi előre rögzített választást őrzi.

```python
def felosztas_elokeszitese(cimkek, seed):
    generator = np.random.default_rng(seed)
    tanito_reszek, validacios_reszek = [], []
    for cimke in range(10):
        indexek = generator.permutation(np.flatnonzero(cimkek == cimke))
        tanito_reszek.append(indexek[:800])
        validacios_reszek.append(indexek[800:1000])
    return np.concatenate(tanito_reszek), np.concatenate(validacios_reszek)

tanito_indexek, validacios_indexek = felosztas_elokeszitese(osszes_cimke, SEED)
generator = np.random.default_rng(SEED + 1)
teszt_indexek = np.concatenate([
    generator.permutation(np.flatnonzero(teszt_cimkek_forras == cimke))[:200]
    for cimke in range(10)
])
assert np.intersect1d(tanito_indexek, validacios_indexek).size == 0
np.savez(munkamappa / "split_indices.npz", train=tanito_indexek, validation=validacios_indexek, test=teszt_indexek)
tanito_kepek, tanito_cimkek = osszes_kep[tanito_indexek], osszes_cimke[tanito_indexek]
validacios_kepek, validacios_cimkek = osszes_kep[validacios_indexek], osszes_cimke[validacios_indexek]
teszt_kepek, teszt_cimkek = teszt_kepek_forras[teszt_indexek], teszt_cimkek_forras[teszt_indexek]
for name, cimkek in [("Train", tanito_cimkek), ("Validation", validacios_cimkek), ("Test", teszt_cimkek)]:
    print(name, "count:", len(cimkek), "per class:", np.bincount(cimkek, minlength=10))
print("Train/validation index overlap:", np.intersect1d(tanito_indexek, validacios_indexek).size)
```

**Kérdés / minimális bizonyíték:** A kiírt elemszámok és az átfedésellenőrzés alapján milyen szerepet kap a három halmaz?


## [D03] Közös batch-ek és az első elem lekérése

Most létrehozzuk a tanito_adatok/training_data, validacios_adatok/validation_data és teszt_adatok/test_data Dataset adatfolyamokat. A from_tensor_slices képenként párosítja a képet és címkéjét; a batch(64) párokat kötegekbe foglalja. A közös, egyszer előre kevert sorrend mindkét tanításnál és minden epochában azonos marad a kontroll kedvéért. A next(iter(...)) részek: iter bejárót készít; next az első elemét kéri, itt egy teljes képek–címkék batch-párt. Nem egyetlen képet és nem a teljes halmazt adja. Még nyers pixelek vannak benne.

```python
sorrend = np.random.default_rng(SEED + 2).permutation(len(tanito_cimkek))
beallitasok = tf.data.Options()
beallitasok.threading.private_threadpool_size = 2
beallitasok.threading.max_intra_op_parallelism = 2
def adatfolyam_keszitese(kepek, cimkek):
    return tf.data.Dataset.from_tensor_slices((kepek, cimkek)).batch(64).with_options(beallitasok).prefetch(1)

tanito_adatok = adatfolyam_keszitese(tanito_kepek[sorrend], tanito_cimkek[sorrend])
validacios_adatok = adatfolyam_keszitese(validacios_kepek, validacios_cimkek)
teszt_adatok = adatfolyam_keszitese(teszt_kepek, teszt_cimkek)
kepek, cimkek = next(iter(tanito_adatok))
print("Training/validation/test batches:", len(tanito_adatok), len(validacios_adatok), len(teszt_adatok))
print("First batch:", kepek.shape, cimkek.shape)
print("Pixel range:", int(tf.reduce_min(kepek)), int(tf.reduce_max(kepek)))
print("First labels:", cimkek[:8].numpy())
np.save(munkamappa / "training_order.npy", sorrend)
```

**Kérdés / minimális bizonyíték:** A lekért képek és címkék alakja alapján mit adott vissza a next(iter(...)), és miért ugyanazt az adatfolyamot használjuk mindkét modellhez?


## [M01] Két kis CNN egy kész függvényből

A modell_epitese(legyen_bn) kész függvény. Mindkét modell belül pontosan egyszer Rescaling(1/255)-öt használ: ez az előfeldolgozás, azaz a nyers képpixelek alkalmassá tétele. A BN ezzel szemben köztes aktivációk statisztikáját kezeli. A függvény True ága két BN-réteget tesz a konvolúció és ReLU közé. Nincs itt skip, Dropout, L2 vagy adatbővítés: ezek korábban külön próbák voltak. Így ez a mérés a BN bekapcsolását hasonlítja össze, nem a ResNet hatását.

```python
def modell_epitese(legyen_bn):
    inputs = keras.Input(shape=(32, 32, 3))
    jellemzok = layers.Rescaling(1. / 255, name="rescale")(inputs)
    jellemzok = layers.Conv2D(16, 3, padding="same", use_bias=False, name="conv_1")(jellemzok)
    if legyen_bn:
        jellemzok = layers.BatchNormalization(epsilon=EPSILON, name="bn_1")(jellemzok)
    jellemzok = layers.ReLU(name="relu_1")(jellemzok)
    jellemzok = layers.MaxPooling2D(2, name="pool")(jellemzok)
    jellemzok = layers.Conv2D(32, 3, padding="same", use_bias=False, name="conv_2")(jellemzok)
    if legyen_bn:
        jellemzok = layers.BatchNormalization(epsilon=EPSILON, name="bn_2")(jellemzok)
    jellemzok = layers.ReLU(name="relu_2")(jellemzok)
    jellemzok = layers.GlobalAveragePooling2D(name="gap")(jellemzok)
    becslesek = layers.Dense(10, activation="softmax", name="classifier")(jellemzok)
    return keras.Model(inputs, becslesek, name="with_bn" if legyen_bn else "without_bn")

alapmodell = modell_epitese(False)
bn_modell = modell_epitese(True)
for modell in [alapmodell, bn_modell]:
    print(modell.name, [(reteg.name, type(reteg).__name__) for reteg in modell.layers])
```

**Kérdés / minimális bizonyíték:** A két réteglistában hol van az eltérés, és melyik művelet végzi a nyers pixelek előfeldolgozását?


## [M02] Közös inicializálás és külön optimalizálók

A get_layer névvel kiválaszt egy réteget, a get_weights/set_weights átmásolja a közös Conv/Dense indulóértékeket. A numpy.array_equal elemről elemre ellenőriz; a listában mindhárom közös réteget vizsgáljuk, nem egyetlen kiválasztott súlyból általánosítunk. A BN sajátgamma/beta/mozgóállapottal indul. Mindkét modell külön friss Adamot kap; a sparse veszteség egész címkéket vár. A kezdeti súlyfájlok helyi helyreállítást segítenek.

```python
kozos_retegek = ["conv_1", "conv_2", "classifier"]
for name in kozos_retegek:
    bn_modell.get_layer(name).set_weights(alapmodell.get_layer(name).get_weights())
    azonos = all(np.array_equal(a, b) for a, b in zip(
        alapmodell.get_layer(name).get_weights(), bn_modell.get_layer(name).get_weights()))
    print("Identical initial weights:", name, azonos)
    assert azonos
for modell in [alapmodell, bn_modell]:
    modell.compile(optimizer=keras.optimizers.Adam(1e-3),
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    print(modell.name, "total:", modell.count_params(),
          "trainable:", sum(int(np.prod(v.shape)) for v in modell.trainable_weights),
          "non-trainable:", sum(int(np.prod(v.shape)) for v in modell.non_trainable_weights))
    modell.save_weights(munkamappa / (modell.name + "_initial.weights.h5"))
assert alapmodell.count_params() == 5370 and bn_modell.count_params() == 5562
```

**Kérdés / minimális bizonyíték:** Mely részek indulása bizonyítottan azonos, és milyen többletet ad a BN a paraméterszámhoz?


## [M03] A BN nélküli CNN tanítása

A fit 6 teljes epochát futtat a kész adatfolyamon. A validation_data nem súlyfrissítésre szolgál. A ModelCheckpoint a legkisebb val_loss súlyait menti a helyi fájlba, nem feltétlen az utolsóepochát. A history az epochánkénti tanulási értékeket tárolja. Várd meg a futás végét; ne indíts második fit-et. A teljes kontrollált újrafuttatás M01-től indul, nem egy már tanult modell újabb 6 epochájával.

```python
alapmodell_fajl = munkamappa / "without_bn_best.weights.h5"
alapmodell_tortenet = alapmodell.fit(
    tanito_adatok, validation_data=validacios_adatok, epochs=6, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(alapmodell_fajl), monitor="val_loss",
               save_best_only=True, save_weights_only=True)]
)
(munkamappa / "baseline_history.json").write_text(json.dumps(alapmodell_tortenet.history, indent=2))
print("Best validation-loss epoch:", int(np.argmin(alapmodell_tortenet.history["val_loss"])) + 1)
```

**Kérdés / minimális bizonyíték:** Küldd el az utolsó két epocha train/val loss értékeit. A saját futásodban együtt csökkentek, vagy eltérően alakultak?


## [M04] A BN-es CNN azonos tanítási kerete

A második modell ugyanazokat a képeket, batch-eket,6 epochát és tanulási rátát kapja. Most a BN has trainable=True és a fit a tanítási/validációs módot automatikusan kezeli. A bestcheckpoint külön fájlba kerül. Egyetlen futásból nem bizonyítjuk, hogy minden BN-es háló gyorsabb vagy pontosabb. Időmérést sem értelmezünk kontrollált GPU-benchmarkként.

```python
bn_fajl = munkamappa / "with_bn_best.weights.h5"
bn_tortenet = bn_modell.fit(
    tanito_adatok, validation_data=validacios_adatok, epochs=6, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(bn_fajl), monitor="val_loss",
               save_best_only=True, save_weights_only=True)]
)
(munkamappa / "bn_history.json").write_text(json.dumps(bn_tortenet.history, indent=2))
print("Best validation-loss epoch:", int(np.argmin(bn_tortenet.history["val_loss"])) + 1)
```

**Kérdés / minimális bizonyíték:** A saját kiírásaid alapján miben tér el a BN-es tanulás vége az előző modellétől? Ne jósolj előre javulást.


## [M05] Visszatöltött checkpointok és validációs döntés

A load_weights a legjobb helyi állapotot tölti vissza. Az evaluate ezen a visszatöltött állapoton mér, nem az utolsó epochán. A görbéken a fit train-loss tanítási módból, a val-loss inferenciából származik; BN-nél a két statisztikahasználat is eltér. A kisebb újramért val_loss dönt, pontos egyezésnél az egyszerűbb alapmodell. A valasztott_nev értékét a teszt előtt rögzítjük. Nem várunk szükségszerű BN-javulást.

```python
alapmodell.load_weights(alapmodell_fajl)
bn_modell.load_weights(bn_fajl)
validacios_eredmenyek = {}
for name, modell in [("without_bn", alapmodell), ("with_bn", bn_modell)]:
    validacios_eredmenyek[name] = {k: float(v) for k, v in modell.evaluate(validacios_adatok, verbose=0, return_dict=True).items()}
valasztott_nev = "with_bn" if validacios_eredmenyek["with_bn"]["loss"] < validacios_eredmenyek["without_bn"]["loss"] else "without_bn"
valasztott_modell = bn_modell if valasztott_nev == "with_bn" else alapmodell
(munkamappa / "selection.json").write_text(json.dumps({"validation": validacios_eredmenyek, "selected": valasztott_nev}, indent=2))
print("Restored validation:", validacios_eredmenyek)
print("Selected before test:", valasztott_nev)
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
for name, tortenet in [("without_bn", alapmodell_tortenet), ("with_bn", bn_tortenet)]:
    for axis, metrika in zip(axes, ["loss", "accuracy"]):
        axis.plot(range(1, 7), tortenet.history[metrika], label=name + " train")
        axis.plot(range(1, 7), tortenet.history["val_" + metrika], linestyle="--", label=name + " validation")
        axis.set(xlabel="Epoch", ylabel=metrika)
for axis in axes:
    axis.legend(fontsize=7)
plt.tight_layout()
plt.show()
```

**Kérdés / minimális bizonyíték:** A saját visszatöltött val_loss értékeid alapján melyik modell lett kiválasztva, és miért?


## [V01] Végső teszt a döntés után

A két előre rögzített modell teszteredményét most egyszer dokumentáljuk; ezután nincs teszt alapján új választás, epocha vagy hiperparaméter. Az evaluate a nem kevert tesztfolyamon méri a veszteséget és a helyes osztályok arányát. A modell így is a validációval kiválasztott marad, ha a másik tesztpontossága magasabb. Ez kis, osztályonként előre kijelölt 2000 képes tesztrész, nem a teljes 10000 kép.

```python
teszt_eredmenyek = {}
for name, modell in [("without_bn", alapmodell), ("with_bn", bn_modell)]:
    teszt_eredmenyek[name] = {k: float(v) for k, v in modell.evaluate(teszt_adatok, verbose=0, return_dict=True).items()}
print("Final test:", teszt_eredmenyek)
print("Selection remains:", valasztott_nev)
```

**Kérdés / minimális bizonyíték:** Küldd el a két teszteredményt. Miért nem választunk most új modellt egy esetleg kedvezőbb tesztpontosság alapján?


## [V02] Becslések és konfúziós mátrix lépésenként

Először egy külön 2×3 számpéldában látod az argmax(axis=1)-et: minden sor legnagyobb elemének 0-tól indexelt oszlopszámát adja. A valódi predict már 2000×10 valószínűséget ad. A teszt nincs keverve, így a predict sorai és a D02 tesztcímkéi ugyanabban a sorrendben vannak; nem kell új iterációból összefűzni őket. A mátrixban sor=valódi, oszlop=becsült, az átló a helyes döntés. A kód egy tényleges tévesztést keres; ha nincs, az első képet mutatja. A softmax nem bizonyított megbízhatóság, a hiba lehetséges vizuális okát csak a ténylegesen látott képből sejthetjük.

```python
pelda_valoszinusegek = np.array([[0.1, 0.7, 0.2], [0.6, 0.3, 0.1]])
print("Toy argmax:", pelda_valoszinusegek.argmax(axis=1))
valoszinusegek = valasztott_modell.predict(teszt_adatok, verbose=0)
becsult_cimkek = valoszinusegek.argmax(axis=1)
matrix = tf.math.confusion_matrix(teszt_cimkek, becsult_cimkek, num_classes=10).numpy()
print("Confusion matrix (rows=true, columns=predicted):\n", matrix)
print("Matrix total:", matrix.sum(), "Row totals:", matrix.sum(axis=1))
assert matrix.sum() == 2000 and np.all(matrix.sum(axis=1) == 200)
assert np.isclose(np.trace(matrix) / 2000, teszt_eredmenyek[valasztott_nev]["accuracy"], atol=1e-6)
hibak = np.flatnonzero(becsult_cimkek != teszt_cimkek)
pelda_index = int(hibak[0]) if len(hibak) else 0
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
abra = axes[0].imshow(matrix, cmap="Blues")
axes[0].set(xticks=range(10), yticks=range(10), xlabel="Predicted", ylabel="True")
fig.colorbar(abra, ax=axes[0])
axes[1].imshow(teszt_kepek[pelda_index])
axes[1].set_title("True: " + osztalynevek[int(teszt_cimkek[pelda_index])] + "\nPredicted: " + osztalynevek[int(becsult_cimkek[pelda_index])])
axes[1].axis("off")
plt.tight_layout()
plt.show()
np.savez(munkamappa / "test_predictions.npz", probabilities=valoszinusegek, labels=teszt_cimkek, confusion_matrix=matrix)
```

**Kérdés / minimális bizonyíték:** Nevezz meg a saját mátrixodból egy irányított tévesztést (valódi→becsült), és mondd el, hogyan olvastad le. Ha nincs tévesztés, az átlót értelmezd.


## [Z01] Három rövid reflexió, egyenként

A tutor egyenként beszéli meg az alábbi kérdéseket; nincs új kód. Rövid, tartalmilag helyes válasz elegendő.

**Kérdés / minimális bizonyíték:** 1. Miért használ eltérő statisztikát a BN tanításkor és inferenciában?
2. Miért különböztettük meg a reziduális összeget a ReLU utáni kimenettől?
3. Mit tudsz állítani a saját BN-összehasonlításodról, és mit nem bizonyít ez az egy futás?


## [Z02] Helyi összegzés és lezárás

A kész kód a saját eredményeket helyi results.json-ba írja, és megjeleníti. Ez személyes összegzés, nem beadandó. A notebook mentése saját célra opcionális; nem kell fájlt, linket, elérési utat vagy mentési igazolást küldened.

```python
osszefoglalo = {
    "seed": SEED, "tensorflow": tf.__version__, "batch_size": 64, "epochs_each": 6,
    "sizes": {"train": len(tanito_cimkek), "validation": len(validacios_cimkek), "test": len(teszt_cimkek)},
    "validation": validacios_eredmenyek, "selected_before_test": valasztott_nev,
    "test": teszt_eredmenyek, "confusion_matrix": matrix.tolist(),
    "scope": "One fixed CIFAR-10 subset and initialization; BN comparison, not ResNet training."
}
(munkamappa / "results.json").write_text(json.dumps(osszefoglalo, indent=2))
print(json.dumps(osszefoglalo, indent=2))
```

**Kérdés / minimális bizonyíték:** A saját eredményeidhez kapcsolódva mi volt a legfontosabb tanulságod?
