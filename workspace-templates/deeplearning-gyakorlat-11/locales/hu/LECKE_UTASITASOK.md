# Deep Learning · 11. gyakorlat — Tutorutasítások

Belső tutoranyag. Mindig csak az aktuális pontot add ki: cél, teljes kód, Colab-futtatás, kérdés, várakozás. A tutor ellenőrzési támpontját ne áruld el előre.

## W01 — Gensim telepítése

A cella telepíti a Gensimet, vagy jelzi, hogy már elérhető. Várd meg, amíg a telepítés befejeződik.

```python
pip install gensim
```

**Futtasd a meglévő W01 cellát. Futtatás után:** Mi a szerepe ennek a cellának: könyvtárat telepít vagy modellt tanít?

**Tutor ellenőrzése:** Könyvtárat telepít. A „Requirement already satisfied” is normális.

## W02 — Könyvtárak betöltése

A NumPy a vektorműveletekhez, a Gensim az előre tanult vektorok betöltéséhez kell. A cella siker esetén nem ír ki eredményt.

```python
import numpy as np
from gensim.models import KeyedVectors
import gensim.downloader as api
import gensim # generate similar rövidítése
# Gensim egy nyílt forráskódú Python-könyvtár témamodellezéshez, dokumentumfürtözéshez és más, nem felügyelt tanulási feladatokhoz
%matplotlib inline
```

**Futtasd a meglévő W02 cellát. Futtatás után:** Melyik könyvtár downloader modulját használjuk majd a vektorokhoz?

**Tutor ellenőrzése:** A Gensimét, az api néven.

## W03 — A GloVe-vektorok betöltése

A Gensim letöltője a glove-wiki-gigaword-100 nevű erőforrást tölti a word_vectors változóba. Az első letöltés nagyjából 128 MB; várd meg a végét.

```python
word_vectors = api.load("glove-wiki-gigaword-100")
```

**Futtasd a meglévő W03 cellát. Futtatás után:** Most a Colab tanítja a vektorokat, vagy kész vektorokat töltünk be?

**Tutor ellenőrzése:** Kész GloVe-vektorokat töltünk be. A feladat szóbeágyazásokkal dolgozik, a notebook neve ellenére nem tanít Word2Vec-modellt.

## W04 — Elérhető modellek listája

Ez a cella a letölthető modellek nevét listázza. A word_vectors változó ettől nem változik.

```python
print(list(gensim.downloader.info()['models'].keys()))
```

**Futtasd a meglévő W04 cellát. Futtatás után:** A lista megjelenítése letölti a felsorolt modelleket is?

**Tutor ellenőrzése:** Nem. A lista a katalógust mutatja; a korábban betöltött GloVe-modellt használjuk tovább.

## W05 — Szavak vektorai

A get_vector megkeresi az adott szóhoz tartozó vektort; a len az elemek számát adja.

```python
apple = word_vectors.get_vector('apple')
pear  = word_vectors.get_vector('pear')
dog   = word_vectors.get_vector('dog')
hotel = word_vectors.get_vector('hotel')
motel = word_vectors.get_vector('motel')
bird = word_vectors.get_vector('bird')
len(apple), len(pear), len(dog)
```

**Futtasd a meglévő W05 cellát. Futtatás után:** Milyen közös tulajdonságot mutat a három kiírt hossz?

**Tutor ellenőrzése:** Az apple, pear és dog vektorának egyaránt 100 komponense van.

## W06 — Egy konkrét szóvektor

Az apple kiírása az előző cellában kikeresett számsort mutatja.

```python
apple
```

**Futtasd a meglévő W06 cellát. Futtatás után:** A kiírt tömb minden eleme egy másik szó, vagy ugyanannak a szónak egy komponense?

**Tutor ellenőrzése:** Ugyanazon szóvektor egy komponense; a számok nem külön szavak.

## W07 — Koszinusz-hasonlóság függvény

A függvény a skalárszorzatból számolja a koszinusz-hasonlóságot, majd négy tizedesre kerekít. Most a számítás szabályát rögzítjük.

```python
def cosine_similarity(v1, v2):
    sim = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return np.round(sim, 4)
```

**Futtasd a meglévő W07 cellát. Futtatás után:** Milyen két mennyiséggel normalizál a függvény?

**Tutor ellenőrzése:** A két vektor normájával: ezek szorzata a nevező. A definíció önmagában nem ír ki értéket.

## W08 — Gyümölcsök és állat összevetése

Három pár koszinusz-hasonlóságát számítjuk ki ugyanazzal a függvénnyel. Az értékek a hívások sorrendjében jelennek meg.

```python
cosine_similarity(apple, pear), cosine_similarity(apple, dog), cosine_similarity(pear, dog),
```

**Futtasd a meglévő W08 cellát. Futtatás után:** Melyik pár a leghasonlóbb a saját kimeneted szerint, és miből látod?

**Tutor ellenőrzése:** A referenciafutásban apple–pear. A hallgató saját sorrendjét indokolja a legnagyobb értékkel.

## W09 — Szálláshelyek és más szavak

Most négy párt hasonlítunk össze. Ugyanazt az értelmezést alkalmazzuk más szavakra.

```python
cosine_similarity(motel, hotel), cosine_similarity(motel, dog), cosine_similarity(hotel, dog), cosine_similarity(motel, apple)
```

**Futtasd a meglévő W09 cellát. Futtatás után:** A négy értékből melyik tartozik a motel–hotel párhoz, és hogyan viszonyul a többihez?

**Tutor ellenőrzése:** Az első, a referenciafutásban a legnagyobb. Az a lényeg, hogy az érték helyét a híváshoz kapcsolja.

## W10 — Párok névvel kiírva

A print a gyümölcsös példa eredményei mellé odateszi a pár nevét. A számítás ugyanaz.

```python
print('apple-pear:', cosine_similarity(apple, pear))
print('apple-dog:', cosine_similarity(apple, dog))
print('pear-dog:', cosine_similarity(pear, dog))
```

**Futtasd a meglévő W10 cellát. Futtatás után:** Mit tesz olvashatóbbá ez a kiírás a korábbi hármashoz képest?

**Tutor ellenőrzése:** Minden szám mellé odaírja, melyik szópárhoz tartozik.

## W11 — Különbségvektorok

A függvény bemenete most két különbségvektor: king−queen és man−woman. Az irányuk hasonlóságát mérjük.

```python
cosine_similarity(word_vectors.get_vector('king')-word_vectors.get_vector('queen'),
                  word_vectors.get_vector('man')-word_vectors.get_vector('woman'))
```

**Futtasd a meglévő W11 cellát. Futtatás után:** Miért nem azonos ez a king és queen közvetlen hasonlóságával?

**Tutor ellenőrzése:** Szóvektorok különbségeit hasonlítja össze, nem a két különálló szóvektort.

## W12 — King − man + woman

A most_similar a pozitív és negatív tagokból lekérdezési irányt képez, és öt közeli szót ad pontszámmal. A címsorban szereplő egyenlet analógia, nem pontos egyenlőség.

```python
word_vectors.most_similar(positive=['king', 'woman'], negative=['man'], topn=5)
```

**Futtasd a meglévő W12 cellát. Futtatás után:** Mit jelent a negative=['man'] ebben a keresésben?

**Tutor ellenőrzése:** A man a keresésben negatív irányú, másképp: a lekérdezési kombinációból kivonandó tag. A kapott lista nem bizonyít egzakt egyenlőséget.

## W13 — Egyes szám és többes szám

A cats−cat irányt a carrot szóhoz kapcsoljuk. Az öt találat azt mutatja, milyen közel kerülnek a szótár szavai ehhez az irányhoz.

```python
word_vectors.most_similar(positive=['cats', 'carrot'], negative=['cat'], topn=5)
```

**Futtasd a meglévő W13 cellát. Futtatás után:** Milyen nyelvi viszonyt próbál átvinni a cella?

**Tutor ellenőrzése:** Az egyes szám → többes szám viszonyt a cat/cats párról a carrot szóra.

## W14 — Mozart szomszédai

Itt nincs összeadás vagy kivonás. A keresés a mozart szó közeli szomszédait listázza.

```python
word_vectors.most_similar('mozart', topn=5)
```

**Futtasd a meglévő W14 cellát. Futtatás után:** Melyik találatot tudod egy rövid indoklással Mozarthoz kapcsolni?

**Tutor ellenőrzése:** Például Beethoven vagy Haydn: mindketten zeneszerzők. A hallgató saját találata alapján is válaszolhat.

## W15 — A Messi–Mozart analógia

A kód a Messihez rendelt foglalkozás viszonyát próbálja zenei névre átvinni. A modell közeli találatokat ad, nem életrajzi tényeket ellenőriz.

```python
word_vectors.most_similar(positive=['footballer', 'mozart'], negative=['messi'], topn=5)
```

**Futtasd a meglévő W15 cellát. Futtatás után:** Melyik találat áll legközelebb a keresett foglalkozáshoz?

**Tutor ellenőrzése:** A referenciafutásban composer. Elfogadható más találat is a hallgató kimenetéből, értelmezéssel.

## W16 — Sushi és Olaszország

A sushi és Italy pozitív, Japan negatív tag a lekérdezésben. A rangsort a megadott vektortér alakítja.

```python
word_vectors.most_similar(positive=['sushi', 'italy'], negative=['japan'], topn=5)
```

**Futtasd a meglévő W16 cellát. Futtatás után:** Miért nem tekintjük automatikusan helyes olasz ételnek az első találatot?

**Tutor ellenőrzése:** A pontszám korpuszból tanult vektorhasonlóság, nem kulturális vagy kulináris tényellenőrzés.

## W17 — Sushi és Magyarország

Itt Italy helyett Hungary kerül a lekérdezésbe. A cél megfigyelni, mi változik a találati listában.

```python
word_vectors.most_similar(positive=['sushi', 'hungary'], negative=['japan'], topn=5)
```

**Futtasd a meglévő W17 cellát. Futtatás után:** Milyen eltérést látsz az előző listához képest?

**Tutor ellenőrzése:** Bármely, a két tényleges listában látható eltérés, például az első találat változása.

## W18 — A goulash közeli szavai

Ez egy közvetlen szomszédkeresés a goulash vektorából. A kód a most_similar alapértelmezett találatszámát használja.

```python
word_vectors.most_similar("goulash")
```

**Futtasd a meglévő W18 cellát. Futtatás után:** Miben tér el a keresés az előző, sushi–ország példától?

**Tutor ellenőrzése:** Egyetlen szóvektorból keres, vektoranalógia nélkül.

## W19 — Kilógó ország

A split a szöveget szavakra bontja, a doesnt_match a csoport vektormintájához legkevésbé illeszkedő szót keresi.

```python
word_vectors.doesnt_match('germany hungary slovakia usa france italy'.split())
```

**Futtasd a meglévő W19 cellát. Futtatás után:** Mi lett a kilógó szó, és hogyan tudnád értelmezni?

**Tutor ellenőrzése:** A referencia szerint usa; a többi megadott ország európai. A pontosságot a saját kimenet alapján értékeljük.

## W20 — Kilógó személynév

Ugyanazt a műveletet neveken próbáljuk ki. A névsorhoz tartozó korpuszbeli kapcsolatok alakítják a választ.

```python
word_vectors.doesnt_match('einstein hawking darwin bohr curie tesla'.split())
```

**Futtasd a meglévő W20 cellát. Futtatás után:** Mitől függ, kit talál kilógónak a program?

**Tutor ellenőrzése:** A betöltött vektoroktól és az adott csoporttól; nem általános tudománytörténeti osztályozás.

## W21 — Az azonos cella ismétlése

Az eredeti forrás két külön cellában tartalmazza ugyanazt az utasítást. Futtasd ezt a második példányt is.

```python
word_vectors.doesnt_match('einstein hawking darwin bohr curie tesla'.split())
```

**Futtasd a meglévő W21 cellát. Futtatás után:** Miért várható ugyanaz a kilógó név, mint az előző cellában?

**Tutor ellenőrzése:** Ugyanazok a bemenetek és ugyanaz a betöltött vektortér, a művelet sem változott.

## W22 — Kilógó tantárgy

A doesnt_match műveletet ezúttal tantárgyakon próbáljuk ki.

```python
word_vectors.doesnt_match('physics mathematics chemistry biology history'.split())
```

**Futtasd a meglévő W22 cellát. Futtatás után:** Mit mutat a kiemelt tantárgy a többihez képest?

**Tutor ellenőrzése:** A referenciafutásban history illeszkedik a legkevésbé a csoporthoz a vektortérben. Ez nem a tantárgy értékéről szól.

## W23 — Eredmény eltárolása

A rupee–India–Japan analógia találatlistája a results változóba kerül. Az eredeti cella nem tartalmaz kiírást.

```python
results = word_vectors.most_similar(positive=['rupee', 'japan'], negative=['india'])
```

**Futtasd a meglévő W23 cellát. Futtatás után:** Ha nem jelent meg lista a cella alatt, miért lehet mégis sikeres?

**Tutor ellenőrzése:** Az értékadás normálisan nem jelenít meg kimenetet; a lista a results változóban van.

## S01 — Váltás a szöveggenerálós notebookra

Nyisd meg a **PTE_DL11_text_generation_COLAB.ipynb** fájlt Google Colabban. A **Futtatókörnyezet → Futtatókörnyezet típusának módosítása** menüben válaszd a **GPU** gyorsítót és a **2026.04** futtatókörnyezet-verziót, majd mentsd. Ez a notebook külön állapotból indul. Jelezd, amikor beállítottad. Várd meg a választ; utána következik a T00 kódja.

## T00 — TensorFlow, Keras és GPU ellenőrzése

A régi Keras-felület kell az eredeti modellhez. Ez a technikai cella az első TensorFlow-import előtt állítja be, majd kiírja a betöltött környezetet.

```python
# T00 — Colab setup for the original legacy Keras model.
import os
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version

try:
    tf_version = version("tensorflow")
except PackageNotFoundError:
    tf_version = ""
if not tf_version.startswith("2.19."):
    raise RuntimeError("Colab: choose GPU and runtime version 2026.04 (TensorFlow 2.19), then rerun T00.")

try:
    legacy_version = version("tf-keras")
except PackageNotFoundError:
    legacy_version = None

if legacy_version != "2.19.0":
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q", "--no-deps", "tf-keras==2.19.0"
    ])

os.environ["TF_USE_LEGACY_KERAS"] = "1"
import tensorflow as tf

keras_backend = tf.keras.__name__
gpu_devices = tf.config.list_physical_devices("GPU")
print("TensorFlow:", tf.__version__)
print("Keras:", keras_backend)
print("GPU:", gpu_devices)
if not keras_backend.startswith("tf_keras"):
    raise RuntimeError("Legacy Keras was not loaded. Restart the Colab session and run T00 first.")
if not gpu_devices:
    raise RuntimeError("Colab: Runtime > Change runtime type > GPU > Save. Then rerun T00.")

```

**Futtasd a meglévő T00 cellát. Futtatás után:** Mi jelent meg a TensorFlow:, Keras: és GPU: sorokban?

**Tutor ellenőrzése:** TensorFlow 2.19.x, tf_keras kezdetű modulnév és nem üres GPU-lista.

## T01 — TensorFlow és segédkönyvtárak

A notebook betölti a TensorFlow-t és a NumPyt. A környezeti változó a régi tf.keras felülethez kapcsolódik; ezt már beállítottuk a külön Colab-előkészítésben.

```python
import tensorflow as tf

import numpy as np
import os
import time

import os
os.environ['TF_USE_LEGACY_KERAS']='1'
```

**Futtasd a meglévő T01 cellát. Futtatás után:** Ebben a cellában már építünk modellt?

**Tutor ellenőrzése:** Nem, a futtatáshoz szükséges könyvtárakat töltjük be.

## T02 — A korpusz letöltése

A futó sor a Piszkos Fred forrásszövegének fájlját kéri le. A Shakespeare-sor megjegyzés, nem fut.

```python
#path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
path_to_file = tf.keras.utils.get_file('piszkosfred.txt', 'https://raw.githubusercontent.com/karsarobert/DeepLearning2026/main/piszkosfred.txt')
```

**Futtasd a meglévő T02 cellát. Futtatás után:** Melyik korpuszt használja ez a notebook?

**Tutor ellenőrzése:** A Piszkos Fred, a kapitány szövegét; a Shakespeare-sor ki van kommentezve.

## T03 — UTF-8 szöveg beolvasása

A bájtokat UTF-8 szöveggé dekódoljuk. A len(text) a Python-karakterlánc hosszát adja.

```python
# Read, then decode for py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
print(f'Length of text: {len(text)} characters')
```

**Futtasd a meglévő T03 cellát. Futtatás után:** Karaktereket vagy bájtokat számol a kiírt érték?

**Tutor ellenőrzése:** Karaktereket. Az ékezetes karakter UTF-8-ban több bájtot is foglalhat.

## T04 — Az első 250 karakter

A szelet a szöveg elejét mutatja; ékezet, szóköz, sortörés és írásjel is lehet benne.

```python
# Take a look at the first 250 characters in text
print(text[:250])
```

**Futtasd a meglévő T04 cellát. Futtatás után:** A modell szavakat vagy egyes karaktereket fog itt tanulási egységként használni?

**Tutor ellenőrzése:** Egyes karaktereket, a szóközzel és írásjelekkel együtt.

## T05 — A karakterkészlet

A set(text) eltávolítja az ismétlődéseket, a sorted rendezett listát ad.

```python
# The unique characters in the file
vocab = sorted(set(text))
print(f'{len(vocab)} unique characters')
```

**Futtasd a meglévő T05 cellát. Futtatás után:** A kiírt érték az összes karaktert számolja, vagy a különböző típusokat?

**Tutor ellenőrzése:** A különböző karaktertípusokat. Az eredeti futásban 98-at.

## T06 — Karakterből azonosító, azonosítóból karakter

A char2idx karakterből egész indexet ad, az idx2char az ellenkező irányban működik. Az eredeti szöveg sorrendben indexsorozattá válik.

```python
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text]) #szöveget pontosabban a karaktereket számokká konvertáljuk
```

**Futtasd a meglévő T06 cellát. Futtatás után:** Melyik változóval alakítanál vissza egy kiválasztott indexet karakterré?

**Tutor ellenőrzése:** Az idx2char tömbbel; az index a tömb pozíciója.

## T07 — Az indexszótár megtekintése

A ciklus az első húsz karakter–index kapcsolatot írja ki. A repr láthatóvá teszi például a sortörés jelét.

```python
print('{')
for char,_ in zip(char2idx, range(20)):
    print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
print('  ...\n}')
```

**Futtasd a meglévő T07 cellát. Futtatás után:** Miért hasznos itt a repr?

**Tutor ellenőrzése:** A nem látható karakterek, például a sortörés, jelölésként is megjelennek.

## T08 — Az első 13 karakter kódolása

A kiírás a szöveg elejét és ugyanannak a részletnek az indexeit teszi egymás mellé.

```python
print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))
```

**Futtasd a meglévő T08 cellát. Futtatás után:** Mit jelent, ha egy index többször szerepel ebben a sorban?

**Tutor ellenőrzése:** Ugyanaz a karakter több pozícióban fordul elő.

## T09 — Karakterenkénti adatfolyam

A from_tensor_slices az egyes indexekből egyenként bejárható adatfolyamot készít. A take(10) csak tíz elemet mutat.

```python
seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)


char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

for i in char_dataset.take(10):
  print(idx2char[i.numpy()])
```

**Futtasd a meglévő T09 cellát. Futtatás után:** Mit tartalmaz ekkor egy Dataset-elem?

**Tutor ellenőrzése:** Egyetlen karakter egész azonosítóját.

## T10 — 101 karakteres darabok

A batch itt 101 egymás utáni karakterindexet csoportosít. A drop_remainder a túl rövid utolsó darabot elhagyja.

```python
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

for item in sequences.take(5):
  print(repr(''.join(idx2char[item.numpy()])))
```

**Futtasd a meglévő T10 cellát. Futtatás után:** Miért kell 101 karakter egy 100 hosszú tanítópárhoz?

**Tutor ellenőrzése:** Egy további karakter kell a jobbra eltolt cél utolsó eleméhez.

## T11 — Bemenet és cél szétválasztása

A függvény bemenetként elhagyja az utolsó, célként az első karaktert. Minden pozícióhoz így a következő karakter lesz a címke.

```python
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


```

**Futtasd a meglévő T11 cellát. Futtatás után:** Ha a darab „abc”, mi a bemenet és mi a cél?

**Tutor ellenőrzése:** „ab” a bemenet, „bc” a cél.

## T12 — Az eltolás kipróbálása

A „Tensorflow” karakterlistáján kipróbáljuk az előbb definiált függvényt.

```python
split_input_target(list("Tensorflow"))
```

**Futtasd a meglévő T12 cellát. Futtatás után:** Az első bemeneti T-hez melyik célkarakter tartozik?

**Tutor ellenőrzése:** Az e, mert a T után az e következik.

## T13 — Címkepárok a teljes adatfolyamon

A map minden korábbi darabra alkalmazza a split_input_target függvényt. A cella az átalakítást állítja be; nem jelenít meg példát.

```python
dataset = sequences.map(split_input_target)
```

**Futtasd a meglévő T13 cellát. Futtatás után:** Mi lesz mostantól egy Dataset-elem?

**Tutor ellenőrzése:** Egy bemeneti sorozat és a vele azonos hosszú, egy karakterrel eltolt célsorozat.

## T14 — Egy bemeneti–cél pár megtekintése

A cella visszafejti az első bemenetet és célt olvasható szövegre.

```python
for input_example, target_example in  dataset.take(1):
  print ('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
  print ('Target data:', repr(''.join(idx2char[target_example.numpy()])))
```

**Futtasd a meglévő T14 cellát. Futtatás után:** Milyen eltolást látsz a két sor között?

**Tutor ellenőrzése:** A cél egy karakterrel később kezdődik ugyanabban a szövegben.

## T15 — Öt időlépés párosítása

A zip azonos pozícióban párosítja a bemeneti és célindexet. A cella a számok mellett a karaktereket is megmutatja.

```python
for i, (input_idx, target_idx) in enumerate(zip(input_example[:5], target_example[:5])):
    print("Step {:4d}".format(i))
    print("  input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    print("  expected output: {} ({:s})".format(target_idx, repr(idx2char[target_idx])))
```

**Futtasd a meglévő T15 cellát. Futtatás után:** Mit ellenőrizhetünk az első néhány input–expected output páron?

**Tutor ellenőrzése:** Hogy minden időlépés céleleme a korpuszban következő karakter.

## T16 — Keverés és 64-es batch

A shuffle a sorozatpárok sorrendjét keveri, a batch 64 párt csoportosít. Egy adott sorozat belső karaktersorrendje változatlan.

```python
BATCH_SIZE = 64
BUFFER_SIZE = 10000
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

dataset
```

**Futtasd a meglévő T16 cellát. Futtatás után:** Mit jelent a (64, 100) alak a bemenetnél?

**Tutor ellenőrzése:** Egy batchben 64 darab, egyenként 100 karakterindexet tartalmazó sorozat van.

## T17 — A modell fő méretei

A vocab_size a különböző karakterek száma, az embedding_dim az egy karakterhez tanult vektor mérete, a rnn_units a GRU állapotának mérete.

```python
# Length of the vocabulary in StringLookup Layer
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024
```

**Futtasd a meglévő T17 cellát. Futtatás után:** A 256 a szókincs mérete vagy az egy karakterhez tartozó beágyazás mérete?

**Tutor ellenőrzése:** A beágyazás dimenziója. A szókincs méretét a len(vocab) adja.

## T18 — Embedding, GRU, Dense

A build_model három réteget definiál. Az Embedding vektort keres ki, a GRU időbeli állapotot kezel, a Dense karakterenként egy pontszámot ad. A függvény még nem tanít.

```python
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):

    model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,return_sequences=True,stateful=True,recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
    return model

#Ez a kaggleről van
```

**Futtasd a meglévő T18 cellát. Futtatás után:** Miért kapunk minden időlépéshez kimenetet?

**Tutor ellenőrzése:** A GRU return_sequences=True beállítása minden időlépés kimenetét továbbadja.

## T19 — A tanítómodell létrehozása

A függvényhívás elkészíti a modellt a tanítás 64-es batchméretéhez. A stateful GRU batchpozíciónként viszi tovább az állapotot, ezért kell rögzített batchméret.

```python
model = build_model(vocab_size=vocab_size,
    embedding_dim=embedding_dim,
    rnn_units=rnn_units, batch_size=BATCH_SIZE)
```

**Futtasd a meglévő T19 cellát. Futtatás után:** Miért egyezik meg a batchméret az adatfolyam batchméretével?

**Tutor ellenőrzése:** A stateful modell állapota batchpozíciónként tárolódik; a bemenetnek illeszkednie kell a felépítéshez.

## T20 — A modell összefoglalója

A summary listázza a rétegek típusát, alakját és paraméterszámát. A Dense utolsó tengelye a karakterosztályokhoz tartozik.

```python
model.summary()
```

**Futtasd a meglévő T20 cellát. Futtatás után:** Melyik három rétegtípust látod?

**Tutor ellenőrzése:** Embedding, GRU és Dense.

## T21 — Próba egy batchen

Egy batch átmegy a modellen súlyfrissítés nélkül. A tengelyek jelentése: batch, időlépés, karakterosztály.

```python
for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)
  print(example_batch_predictions.shape, "# (batch_size, sequence_length, vocab_size)")
```

**Futtasd a meglévő T21 cellát. Futtatás után:** Mit jelent a kimenet utolsó dimenziója?

**Tutor ellenőrzése:** Minden időlépésben ennyi karakterhez rendel logitot a Dense; a forrásadatnál 98.

## T22 — Második modell-összefoglaló

Ez ismét summary, ezúttal a próbaelőrejelzés után. A cella kiírja az architektúrát, nem változtatja meg.

```python
model.summary()
```

**Futtasd a meglévő T22 cellát. Futtatás után:** Egy második summary futtatásától megváltoznak a súlyok?

**Tutor ellenőrzése:** Nem. Ez ellenőrző kiírás.

## T23 — Mintavétel a próbakimenetből

A batch első sorozatából időlépésenként egy karakterindexet mintázunk. A squeeze elhagyja az egy hosszú mintatengelyt.

```python
sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()
```

**Futtasd a meglévő T23 cellát. Futtatás után:** Miért nincs szükség kézi softmaxra a tf.random.categorical előtt?

**Tutor ellenőrzése:** A művelet logitokat fogad; ezekből végzi a mintavételezést.

## T24 — A mintavett karakterindexek

A cella az előző lépés indexsorát mutatja. Ez még nem szöveg.

```python
sampled_indices
```

**Futtasd a meglévő T24 cellát. Futtatás után:** Egy index mit jelöl ebben a tömbben?

**Tutor ellenőrzése:** Egy adott időlépésben mintavett következő karakter szótári azonosítóját.

## T25 — A tanítatlan modell dekódolt próbája

Az idx2char olvashatóvá teszi a bemenetet és a mintavett kimenetet. Itt a pozíciók az ismert bemenethez tartoznak, még nem az önálló generálási ciklust látjuk.

```python
print("Input: \n", repr("".join(idx2char[input_example_batch[0]])))
print()
print("Next Char Predictions: \n", repr("".join(idx2char[sampled_indices ])))
```

**Futtasd a meglévő T25 cellát. Futtatás után:** Miért nem várunk értelmes mondatot ettől a kimenettől?

**Tutor ellenőrzése:** A modell súlyai még nem tanultak a korpuszon; ez alak- és működéspróba.

## T26 — A veszteségfüggvény

A SparseCategoricalCrossentropy egész célindexeket használ. A függvénynek azt is meg kell mondani, hogyan kezelje a modell kimenetét.

```python
loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
```

**Futtasd a meglévő T26 cellát. Futtatás után:** Melyik argumentum mondja meg a veszteségfüggvénynek, hogy nyers pontszámokat kap?

**Tutor ellenőrzése:** A from_logits=True. A Dense ebben a modellben nyers logitokat ad.

## T27 — Kezdeti átlagos veszteség

A veszteség a batch valódi célkaraktereit a próbakimenet logitjaival hasonlítja össze. A kapott érték egyetlen átlagos szám.

```python
example_batch_mean_loss = loss(target_example_batch, example_batch_predictions)
print("Prediction shape: ", example_batch_predictions.shape, " # (batch_size, sequence_length, vocab_size)")
print("Mean loss:        ", example_batch_mean_loss)
```

**Futtasd a meglévő T27 cellát. Futtatás után:** A kiírt veszteség a tanítás előtti vagy utáni állapotot jellemzi?

**Tutor ellenőrzése:** A tanítás előttit: még nem futott a fit.

## T28 — A veszteség exponenciálisa

Ha a modell a karakterekhez nagyjából azonos esélyt rendel, a keresztentrópia a szókincsméret természetes logaritmusa körüli. Az exponenciális ekkor a szókincsméret közelében van.

```python
tf.exp(example_batch_mean_loss).numpy()
```

**Futtasd a meglévő T28 cellát. Futtatás után:** Mihez hasonlítható a kiírt eredmény?

**Tutor ellenőrzése:** A vocab_size értékéhez. Ez kezdeti ellenőrzés, nem tesztpontosság.

## T29 — A modell konfigurálása

A compile összeköti az Adam optimalizálót a korábban megadott veszteséggel. A tanítás még nem indul el.

```python
model.compile(optimizer='adam', loss=loss)
```

**Futtasd a meglévő T29 cellát. Futtatás után:** Melyik művelet indítja ténylegesen a súlyfrissítéseket?

**Tutor ellenőrzése:** A következő tanítási fit, nem a compile.

## T30 — Súlymentés beállítása

A callback az epochák során súlyállapotokat ment a training_checkpoints mappába. A save_weights_only miatt nem egy teljes, önálló modellfájlt mentünk.

```python
# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)
```

**Futtasd a meglévő T30 cellát. Futtatás után:** A callback létrehozásakor már elkészült a súlymentés?

**Tutor ellenőrzése:** Nem, a fit hívja meg a callbacket a képzés közben.

## T31 — Az epochák száma

Az eredeti kód 30-ra állítja az EPOCHS változót. Ez határozza meg a tanítás hosszát.

```python
EPOCHS = 30
```

**Futtasd a meglévő T31 cellát. Futtatás után:** A változatlan kód hány adathalmazbejárást kér?

**Tutor ellenőrzése:** 30 epochát. A névleges bejárás az előkészített tanító adatfolyamra vonatkozik.

## T32 — A modell tanítása

A fit mind a 30 epochát futtatja. Maradj csatlakozva, és várd meg a 30. epocha végét. A tanítási veszteségeket hasonlítjuk össze.

```python
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
```

**Futtasd a meglévő T32 cellát. Futtatás után:** Hogyan változott a saját futásod vesztesége az első és az utolsó epocha között?

**Tutor ellenőrzése:** A hallgató saját értékein alapuló összehasonlítás. A csökkenés tanítási illeszkedést jelez, önmagában nem bizonyít jó általánosítást.

## T33 — A legutóbbi checkpoint

A latest_checkpoint az elérhető legutóbbi mentést keresi a futtatókörnyezet helyi mappájában.

```python
tf.train.latest_checkpoint(checkpoint_dir)
```

**Futtasd a meglévő T33 cellát. Futtatás után:** Milyen útvonalat ad vissza a cella, és mit jelöl?

**Tutor ellenőrzése:** A nem üres útvonal a legutóbbi helyi mentés előtagja, például a 30. epocháé. None esetén nem lépünk tovább.

## T34 — Egyes batch és visszatöltött súlyok

Újra felépítjük ugyanazokat a rétegeket egyetlen sorozathoz, majd visszatöltjük a tanított súlyokat. Itt a model változó már az új példányra mutat.

```python
model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))
```

**Futtasd a meglévő T34 cellát. Futtatás után:** Miért kell a modellt újraépíteni 1-es batchmérettel?

**Tutor ellenőrzése:** A stateful állapot alakja a batchmérethez kötött, generáláskor pedig egyetlen szövegsorozatot viszünk tovább.

## T35 — A generáló függvény

A start_string indexeit adjuk az első futáshoz, a GRU állapotát nullázzuk. Ezután a függvény a legutolsó időlépés eloszlásából mintáz egy karaktert és visszaadja a modellnek következő bemenetként. A temperature most 1.0.

```python
def generate_text(model, start_string):

    num_generate = 1000
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)


    text_generated = []

    temperature = 1.0

    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0) #1-es dimenziókat eltávolítja
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))
```

**Futtasd a meglévő T35 cellát. Futtatás után:** Mi lesz a ciklus következő körének közvetlen bemenete?

**Tutor ellenőrzése:** Az előző körben mintavett karakter indexe. Az állapot frissül, de a súlyok nem tanulnak tovább.

## T36 — Szöveg generálása az „Azok” prefixből

A print megjeleníti a kezdőszöveget és az 1000 hozzáadott karaktert. A véletlen mintavétel miatt a saját szöveg eltérhet a mentett példától.

```python
print(generate_text(model, start_string=u"Azok"))
```

**Futtasd a meglévő T36 cellát. Futtatás után:** Milyen felismerhető mintát vagy jól látható hibát találsz a saját szövegedben?

**Tutor ellenőrzése:** Például szóközök, írásjelek, párbeszédszerű sorok, magyaros szóalakok vagy értelmetlen szavak. Nincs elvárt egyezés a mintaszöveggel.

## T37 — Egy generálási lépés külön

A záró szemléltetés az „A” karakterből készít egyes batchbemenetet, majd jósol. A text név itt már egy üres gyűjtőlistát jelöl; a cella nem hív állapotnullázást.

```python
text =[]
input_eval = [char2idx[s] for s in 'A']
input_eval = tf.expand_dims(input_eval, 0)
predictions = model(input_eval)
```

**Futtasd a meglévő T37 cellát. Futtatás után:** Módosítja-e ez az előrefuttatás a modell súlyait?

**Tutor ellenőrzése:** Nem. A stateful modell belső állapota változhat, de nincs fit vagy súlyfrissítés.

## T38 — Az egyes batchtengely eltávolítása

A squeeze(predictions, 0) az egyetlen elemű batchtengelyt veszi ki. Az időlépés és a szókincs tengelye megmarad.

```python
predictions = tf.squeeze(predictions, 0)
```

**Futtasd a meglévő T38 cellát. Futtatás után:** Melyik tengely tűnik el?

**Tutor ellenőrzése:** A 0. tengely, az egyes batchméret.

## T39 — Egyetlen pontszám kiválasztása

A predictions[0,1] az első időlépés 1-es indexű karakterosztályának logitja.

```python
predictions[0,1]
```

**Futtasd a meglévő T39 cellát. Futtatás után:** Ez garantáltan 0 és 1 közötti valószínűség?

**Tutor ellenőrzése:** Nem, nyers logitot olvasunk ki. Lehet negatív vagy 1-nél nagyobb is.

## T40 — Egy karakterazonosító mintavétele

A categorical után a [-1,0] a legutolsó időlépés első mintáját veszi ki. Az érték egy egész azonosító, nem maga a karakter.

```python
predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
```

**Futtasd a meglévő T40 cellát. Futtatás után:** A predicted_id mit tárol?

**Tutor ellenőrzése:** A mintavett következő karakter szótári indexét.

## T41 — Új bemenet és a karakter eltárolása

Az azonosító új, 1×1 alakú bemenetté válik. Az idx2char megkeresi a karaktert, az append a listához teszi. Az eredeti cella nem ír ki semmit.

```python
input_eval = tf.expand_dims([predicted_id], 0)
text.append(idx2char[predicted_id])
```

**Futtasd a meglévő T41 cellát. Futtatás után:** Hol van a mintavett karakter, ha nincs kimenet a cella alatt?

**Tutor ellenőrzése:** A text gyűjtőlistában. Az input_eval közben a következő modellhívás indexelt bemenete.

## Z01 — Záróteszt

Mit csinál az api.load("glove-wiki-gigaword-100") ebben a gyakorlatban?

- **A.** A korpuszból új 100 dimenziós vektorokat tanít.
- **B.** Egy előre tanult GloVe-vektorteret tölt be.
- **C.** A szóvektorokból karakterazonosítókat készít.
- **D.** A fájlban található összes modell nevét listázza.

## Z02 — Záróteszt

Mit hasonlít össze elsősorban a koszinusz-hasonlóság?

- **A.** A szavak karakterszámát.
- **B.** A vektorok normáinak különbségét.
- **C.** A szavak korpuszbeli darabszámát.
- **D.** A vektorok irányát.

## Z03 — Záróteszt

Mit kérdezünk a king − man + woman példában?

- **A.** Mely szótári vektorok állnak közel az analógiához képzett irányhoz?
- **B.** Melyik szóvektornak van pontosan ugyanannyi komponense, mint a king szónak?
- **C.** Melyik szó jelentése matematikailag pontosan egyenlő a queen szóval?
- **D.** Melyik szó fordul elő leggyakrabban a tanító korpuszban?

## Z04 — Záróteszt

Milyen információt ad a doesnt_match eredménye?

- **A.** A nyelvtanilag hibás szót adja meg.
- **B.** A leghosszabb szót adja meg.
- **C.** A megadott csoporthoz a vektortérben legkevésbé illeszkedő szót adja meg.
- **D.** Az egész szótár legkevésbé gyakori szavát adja meg.

## Z05 — Záróteszt

Mi a bemenet és a cél a „abcd” darabból a split_input_target szabályával?

- **A.** Bemenet „abc”, cél „bcd”.
- **B.** Bemenet „abc”, cél „abc”.
- **C.** Bemenet „bcd”, cél „abc”.
- **D.** Bemenet „abcd”, cél „d”.

## Z06 — Záróteszt

Mit jelent a modell kimenetének (64, 100, 98) alakjában a 98?

- **A.** A tanító batch méretét.
- **B.** A tanítási epochák számát.
- **C.** Az egy példában levő időlépések számát.
- **D.** A karakterosztályok számát időlépésenként.

## Z07 — Záróteszt

Miért használjuk a from_logits=True flaget?

- **A.** Mert a célkarakterek nincsenek egész indexekkel kódolva.
- **B.** Mert a modell kimenete nyers Dense-pontszám.
- **C.** Mert a modell csak egyetlen karakterosztályt kezel.
- **D.** Mert a kimenet már normalizált valószínűség.

## Z08 — Záróteszt

Mit ad vissza a tf.train.latest_checkpoint, ha nem talál mentést?

- **A.** A legutóbbi epocha sorszámát.
- **B.** Az utolsó epocha veszteségét.
- **C.** None értéket.
- **D.** A korpusz fájlnevét.

## Z09 — Záróteszt

Miért épül új modell batch_size=1-gyel a súlybetöltés előtt?

- **A.** Mert csak egy karakter lehet összesen a szótárban.
- **B.** Mert a mentett súlyokat újra kell tanítani.
- **C.** Mert egy szövegsorozatot generálunk, a stateful állapot batchmérete rögzített.
- **D.** Mert generáláskor el kell hagyni a GRU-réteget.

## Z10 — Záróteszt

Mi a következő modellhívás közvetlen bemenete a generálási ciklusban, miután egy karaktert mintáztunk?

- **A.** A kiválasztott karakter indexe.
- **B.** A teljes tanító korpusz.
- **C.** Egy új, 64 sorozatos batch.
- **D.** Az előző epocha vesztesége.
