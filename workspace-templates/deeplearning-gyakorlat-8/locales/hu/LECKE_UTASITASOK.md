# 8. gyakorlat · vezetett kódfeldolgozás · 1.1

A módszertani szabályokat az agent.md adja.

## [E01] Környezet és Colab GPU

A TensorFlow a futtatókörnyezet eszközeit listázza. A GPU: [] üres listát jelent: a TensorFlow jelenleg nem lát GPU-t. Colabban ilyenkor előbb válts GPU-ra: Futtatókörnyezet (Runtime) → Futtatókörnyezet típusának módosítása (Change runtime type) → Hardveres gyorsító (Hardware accelerator) → GPU, például T4 GPU → Mentés (Save), majd csatlakozz újra. Futtasd újra az E01-et, és csak a nem üres GPU-lista után folytasd. A váltás új munkamenetet indíthat, ezért az addigi változók és feltöltött fájlok elveszhetnek. Helyi Jupyterben nincs ilyen Colab-menü; ott az oktató által előkészített eszközkörnyezetet használjuk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [E01] Környezet és munkamenet
import os, json, time, hashlib, tarfile, shutil
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
MAG = 42
keras.utils.set_random_seed(MAG)
OSZTALYNEVEK = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
MUNKA = Path('dl08_work')
MUNKA.mkdir(exist_ok=True)
print('TensorFlow:', tf.__version__, '| NumPy:', np.__version__)
print('GPU:', tf.config.list_physical_devices('GPU'))

# Colabban üres GPU-listával előbb környezetet váltunk.
try:
    import google.colab
    COLAB = True
except ImportError:
    COLAB = False
gpu_eszkozok = tf.config.list_physical_devices('GPU')
print('Környezet:', 'Colab' if COLAB else 'Jupyter / helyi Python')
if COLAB and not gpu_eszkozok:
    print('Colab: Futtatókörnyezet → Futtatókörnyezet típusának módosítása → GPU / T4 GPU → Mentés.')
    raise RuntimeError('E01: csatlakozz a GPU-s környezethez, majd futtasd újra az E01-et.')
print('E01 OK')
```

A verziósorokat, a környezet nevét és a GPU-listát küldd vissza. Colabban üres GPU-listánál előbb állítsd át a környezetet, majd küldd az új E01-kimenetet.

**Kérdés:** Melyik kiírt adatból állapítod meg, hogy ebben a munkamenetben használható-e GPU?

**Bekérendő:** A verziósorokat, a környezet nevét és a GPU-listát küldd vissza. Colabban üres GPU-listánál előbb állítsd át a környezetet, majd küldd az új E01-kimenetet.

**Elfogadás – belső támpont:** Colabban csak nem üres GPU-lista fogadható el kész E01-ként. Üres listánál konkrét menüút és ismételt ellenőrzés, nem automatikus CPU-s továbblépés. Helyi Jupyternél külön eszközkörnyezet.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [E02] Adatok és előre elkészített segédfüggvények

Ez a hosszabb, készen kapott cella technikai előkészítést végez. Letölti vagy helyi fájlból megnyitja a hivatalos képcsomagot, majd definiál több segédfüggvényt. A def felosztas_elokeszitese(...) sor egy már megírt függvényt hoz létre a memóriában; ettől a felosztás még nem fut le. A D02-ben ezt a függvényt fogjuk meghívni. A tömörítési és hash-kezelési részeket nem kell újraírnod vagy részletesen ismerned.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [E02] Adatok betöltése és ellenőrzött segédek
ARCHIV_SHA256 = '4c54ace7911aaffe13a365c34f650e71dd5bf1be0a58b464e5a7183e3e595d9c'
ADAT_URL = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'

def fajl_hash(utvonal):
    lenyomat = hashlib.sha256()
    with open(utvonal, 'rb') as folyam:
        for reszlet in iter(lambda: folyam.read(1024 * 1024), b''):
            lenyomat.update(reszlet)
    return lenyomat.hexdigest()
helyi_mappa = Path('flower_photos')
if helyi_mappa.is_dir():
    adat_mappa = helyi_mappa
else:
    archiv = Path('flower_photos.tgz')
    if not archiv.is_file():
        archiv = Path(keras.utils.get_file('flower_photos.tgz', origin=ADAT_URL, file_hash=ARCHIV_SHA256, hash_algorithm='sha256'))
    if fajl_hash(archiv) != ARCHIV_SHA256:
        raise ValueError('Eltérő archív ellenőrzőösszeg')
    kicsomagolas = MUNKA / 'source'
    adat_mappa = kicsomagolas / 'flower_photos'
    if not all(((adat_mappa / nev).is_dir() for nev in OSZTALYNEVEK)):
        kicsomagolas.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archiv) as csomagolt:
            cel_mappa = kicsomagolas.resolve()
            for tag in csomagolt.getmembers():
                cel = (kicsomagolas / tag.name).resolve()
                if not cel.is_relative_to(cel_mappa) or tag.issym() or tag.islnk():
                    raise ValueError('Nem biztonságos archívelem')
                if not tag.isfile() and (not tag.isdir()):
                    raise ValueError('Nem támogatott archívelem')
            csomagolt.extractall(kicsomagolas, filter='data')
assert all(((adat_mappa / nev).is_dir() for nev in OSZTALYNEVEK))

def felosztas_elokeszitese(gyoker, tanito_osztalyonkent, val_osztalyonkent, teszt_osztalyonkent):
    veletlen = np.random.default_rng(MAG)
    latott = {}
    jeloltek = {nev: [] for nev in OSZTALYNEVEK}
    elutasitottak = []
    for nev in OSZTALYNEVEK:
        for utvonal in sorted((gyoker / nev).glob('*.jpg')):
            try:
                with Image.open(utvonal) as kep:
                    kep.verify()
                with Image.open(utvonal) as kep:
                    kep.convert('RGB').resize((224, 224)).load()
            except (OSError, ValueError) as error:
                elutasitottak.append({'path': str(utvonal), 'reason': type(error).__name__})
                continue
            lenyomat = fajl_hash(utvonal)
            if lenyomat in latott:
                if latott[lenyomat] != nev:
                    for elozo_nev in OSZTALYNEVEK:
                        eltavolitottak = [(regi_utvonal, regi_hash) for regi_utvonal, regi_hash in jeloltek[elozo_nev] if regi_hash == lenyomat]
                        for regi_utvonal, regi_hash in eltavolitottak:
                            elutasitottak.append({'path': str(regi_utvonal), 'reason': 'conflicting_labels'})
                        jeloltek[elozo_nev] = [(regi_utvonal, regi_hash) for regi_utvonal, regi_hash in jeloltek[elozo_nev] if regi_hash != lenyomat]
                    latott[lenyomat] = None
                elutasitottak.append({'path': str(utvonal), 'reason': 'duplicate_or_conflicting_labels'})
                continue
            latott[lenyomat] = nev
            jeloltek[nev].append((utvonal, lenyomat))
    jegyzek = []
    darabok = [('train', tanito_osztalyonkent), ('val', val_osztalyonkent), ('test', teszt_osztalyonkent)]
    for nev in OSZTALYNEVEK:
        minta_jeloltek = jeloltek[nev]
        sorrend = veletlen.permutation(len(minta_jeloltek))
        if len(minta_jeloltek) < sum((darab for _, darab in darabok)):
            raise ValueError('Nincs elég érvényes kép az osztályban: ' + nev)
        kezdet = 0
        for halmaz, darab in darabok:
            for index in sorrend[kezdet:kezdet + darab]:
                utvonal, lenyomat = minta_jeloltek[int(index)]
                jegyzek.append({'split': halmaz, 'class': nev, 'relative_path': str(utvonal.relative_to(gyoker)), 'sha256': lenyomat})
            kezdet += darab
    alairas = hashlib.sha256(json.dumps(jegyzek, sort_keys=True).encode()).hexdigest()[:12]
    halmaz_mappa = MUNKA / ('split_' + alairas)
    for sor in jegyzek:
        forras = gyoker / sor['relative_path']
        cel = halmaz_mappa / sor['split'] / sor['class'] / forras.name
        cel.parent.mkdir(parents=True, exist_ok=True)
        if not cel.exists() or fajl_hash(cel) != sor['sha256']:
            shutil.copy2(forras, cel)
    (MUNKA / 'manifest.json').write_text(json.dumps(jegyzek, indent=2), encoding='utf-8')
    (MUNKA / 'rejected.json').write_text(json.dumps(elutasitottak, indent=2), encoding='utf-8')
    licenc_fajl = gyoker / 'LICENSE.txt'
    if licenc_fajl.exists():
        shutil.copy2(licenc_fajl, MUNKA / 'DATA_LICENSE.txt')
    print('Kihagyott fájlok:', len(elutasitottak))
    return (halmaz_mappa, jegyzek)

def parameterszam(sulyok):
    return int(sum((np.prod(suly.shape) for suly in sulyok)))

def gorbek(tortenet, cim):
    abra, tengelyek = plt.subplots(1, 2, figsize=(10, 3))
    for tengely, meroszam in zip(tengelyek, ['loss', 'accuracy']):
        epochok = np.arange(1, len(tortenet.history[meroszam]) + 1)
        tengely.plot(epochok, tortenet.history[meroszam], label='Tanító')
        tengely.plot(epochok, tortenet.history['val_' + meroszam], label='Validáció')
        tengely.set(xlabel='Epocha', ylabel={'loss': 'Veszteség', 'accuracy': 'Pontosság'}[meroszam], title=cim)
        tengely.legend()
    plt.tight_layout()
    plt.show()

def kep_betoltese(utvonal):
    with Image.open(utvonal) as kep:
        return np.asarray(kep.convert('RGB').resize((224, 224)), dtype=np.float32)[None, ...]
print('Adatmappa:', adat_mappa)
print('E02 OK')
```

Futtasd a kész cellát, és küldd az adatmappa útvonalát és az E02 OK sort.

**Kérdés:** A függvény definiálása és későbbi meghívása közül melyik indítja majd el ténylegesen a képek felosztását?

**Bekérendő:** Futtasd a kész cellát, és küldd az adatmappa útvonalát és az E02 OK sort.

**Elfogadás – belső támpont:** Öt osztálymappa elérhető; az adatok betöltődtek. Megérti, hogy a def létrehozza a segédet, a hívás futtatja.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [E03] A látott módszer alkalmazása új helyzetben

A bemutatók ételképeket és kutya–macska képeket használtak. Itt más adatok, más modell és öt egész címke szerepel. A transzfer tanulás elve ugyanaz.

**Az aktuális teljes kód – elsőre is add meg:**

Nincs programkód ezen a beszélgetési ponton.

Válaszolj röviden a beszélgetésben.

**Kérdés:** Mit változtatunk meg az öt virágkategóriás feladathoz a bemutatókhoz képest? Egy-két lényegi különbség elegendő.

**Bekérendő:** Saját rövid válasz; nincs kötelező írás a notebookba.

**Elfogadás – belső támpont:** Egy-két helyes lényegi különbség elegendő. A korábbi válaszokat együtt értékeld; ne követeld a teljes fogalomlista vagy egy adott mondat szó szerinti visszaadását.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [D01] Virágkategóriák és mintaképek

A mappanevek a kategóriákat jelölik. A fájlok száma most a teljes forráscsomag méretét mutatja, nem a tanításhoz kiválasztott képek számát. A címkéket később a rögzített osztálysorrend adja.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [D01] Virágkategóriák és mintaképek
forras_darabok = {nev: len(list((adat_mappa / nev).glob('*.jpg'))) for nev in OSZTALYNEVEK}
print(forras_darabok)
abra, tengelyek = plt.subplots(1, 5, figsize=(12, 3))
for tengely, nev in zip(tengelyek, OSZTALYNEVEK):
    utvonal = sorted((adat_mappa / nev).glob('*.jpg'))[0]
    with Image.open(utvonal) as kep:
        tengely.imshow(kep)
    tengely.set_title(nev)
    tengely.axis('off')
plt.tight_layout()
plt.show()
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Milyen tényleges szín-, forma- vagy háttérbeli változatosságot láttál a mintaképeken?

**Bekérendő:** Az öt osztály képszáma és egy saját képi megfigyelés.

**Elfogadás – belső támpont:** Öt nem üres osztály és a valóban látott képre vagy a hallgató leírására alapozott megfigyelés.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [D02] A már megírt felosztófüggvény meghívása

A felosztas_elokeszitese függvény már elkészült az E02 cellában, ezért most csak meghívjuk. Négy bemenetet adunk át sorrendben: az adat_mappa megmondja, hol vannak a képek; a következő három szám az egy osztályból kiválasztandó tanító-, validációs és tesztképek száma. A segéd ellenőrzi a képeket, kizárja a pontos duplikációkat és konfliktusos címkéket, a rögzített seed szerint válogat, majd külön mappákba másolja a kiválasztott képeket. Két eredményt ad vissza: a halmaz_mappa az új mappák gyökere, a jegyzek pedig egy lista, amely képenként rögzíti a halmazt, kategóriát, útvonalat és hash-t. A bal oldali két név ezt a két eredményt veszi át. A kiíró for-ciklus a jegyzék split mezője alapján számolja a képeket; a kódot készen használjuk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [D02] Az E02-ben már megírt segéd meghívása.
tanito_osztalyonkent = 100
val_osztalyonkent = 40
teszt_osztalyonkent = 40
# Négy bemenetet adunk át. Két eredményt kapunk vissza.
halmaz_mappa, jegyzek = felosztas_elokeszitese(
    adat_mappa, tanito_osztalyonkent, val_osztalyonkent, teszt_osztalyonkent
)
# A kiírás a kész jegyzékben számol, nem módosítja a felosztást.
for halmaz, cim in [('train', 'Tanító'), ('val', 'Validációs'), ('test', 'Teszt')]:
    darab = sum(1 for sor in jegyzek if sor['split'] == halmaz)
    print(cim + ':', darab)
```

Futtasd a megadott teljes cellát. Küldd a három halmaz kiírt létszámát.

**Kérdés:** A tanito_osztalyonkent = 100 sor összesen 100 tanítóképet vagy kategóriánként 100 képet kér? Hogyan kapcsolódik ez a saját tanítólétszámodhoz?

**Bekérendő:** Futtasd a megadott teljes cellát. Küldd a három halmaz kiírt létszámát.

**Elfogadás – belső támpont:** 500/200/200, osztályonként 100/40/40. A segéd már definiált függvény; négy argumentumot és két visszatérési értéket értelmez. Nem kell megírnia a függvényt vagy a számlálást.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [D03] A három adathalmaz és az adattöltők létrehozása

A D02 külön mappákba válogatta a képeket. Ez a cella előbb ellenőrzi, hogy nincs közös fájlhash két halmazban, majd létrehozza a tanito_adatok, validacios_adatok és teszt_adatok adatfolyamokat. Ezek tf.data.Dataset objektumok: azt írják le, hogyan olvassunk és méretezzünk képeket 16-os batch-ekben, nem egyszerre töltik az összes képet a memóriába. Az adatok_letrehozasa(...) a most definiált betöltősegéd. A train, val és test a megfelelő mappát választja. Tanításkor a keveres=True változatos sorrendet ad, a validáció és teszt keveres=False beállítása rögzített sorrendet őriz. A közös OSZTALYNEVEK-lista biztosítja, hogy ugyanaz az egész szám mindenütt ugyanazt a virágot jelentse. Itt még nem végzünk tesztértékelést.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [D03] Adattöltők és átfedésvizsgálat
lenyomatok = {halmaz: {sor['sha256'] for sor in jegyzek if sor['split'] == halmaz} for halmaz in ['train', 'val', 'test']}
print('Átfedések:', [len(lenyomatok[a] & lenyomatok[b]) for a, b in [('train', 'val'), ('train', 'test'), ('val', 'test')]])
assert not (lenyomatok['train'] & lenyomatok['val'] or lenyomatok['train'] & lenyomatok['test'] or lenyomatok['val'] & lenyomatok['test'])

def adatok_letrehozasa(halmaz, keveres):
    adatok = keras.utils.image_dataset_from_directory(halmaz_mappa / halmaz, class_names=OSZTALYNEVEK, label_mode='int', image_size=(224, 224), batch_size=16, shuffle=keveres, seed=MAG)
    assert adatok.class_names == OSZTALYNEVEK
    beallitasok = tf.data.Options()
    beallitasok.threading.private_threadpool_size = 2
    return adatok.with_options(beallitasok).prefetch(1)
tanito_adatok = adatok_letrehozasa('train', True)
validacios_adatok = adatok_letrehozasa('val', False)
teszt_adatok = adatok_letrehozasa('test', False)
print('Osztályok:', OSZTALYNEVEK)
```

Futtasd a cellát. Küldd az átfedéslistát és az osztálysorrendet.

**Kérdés:** A három új változó közül melyiket adjuk majd a fit tanító bemenetének, melyik segíti a modellválasztást, és miért fontos a teszt rögzített sorrendje?

**Bekérendő:** Futtasd a cellát. Küldd az átfedéslistát és az osztálysorrendet.

**Elfogadás – belső támpont:** Átfedések 0/0/0, közös osztálysorrend. Megkülönbözteti a három Dataset szerepét; a teszt képei és címkéi később ugyanabban a sorrendben kellenek.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [D04] Egy batch lekérése: iter és next

A kepek, cimkek = next(iter(tanito_adatok)) új művelet, ezért most részekre bontjuk. Az iter(tanito_adatok) létrehoz egy bejáró objektumot az adatfolyamhoz. A next(...) ebből egy következő elemet kér le, ami itt nem egyetlen kép, hanem egy 16 képből és a hozzájuk tartozó 16 címkéből álló pár. A bal oldali kepek, cimkek a pár két tagját veszi át. A kódban ugyanezt két sorban, adag_bejaro változóval mutatjuk meg, és kommentben a rövid alak is látható. A shape az alakot, a dtype az elemtípust, a .numpy() a megjeleníthető NumPy-értékeket adja. A képek ekkor még nyers, 0–255 közötti RGB-pixelek.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [D04] A rövid alak: kepek, cimkek = next(iter(tanito_adatok))
# Ugyanez két lépésben: előbb bejárót hozunk létre, majd egy batch-et kérünk.
adag_bejaro = iter(tanito_adatok)
kepek, cimkek = next(adag_bejaro)
print('Képek alakja:', kepek.shape)
print('Címkék alakja:', cimkek.shape)
print('Típusok:', kepek.dtype, cimkek.dtype)
print('Pixelek min/max:', float(tf.reduce_min(kepek)), float(tf.reduce_max(kepek)))
print('Címkék:', cimkek.numpy())
```

Futtasd a teljes cellát. Küldd a két alakot, típust, pixeltartományt és a címkéket.

**Kérdés:** A saját képalakod négy száma rendre mit jelent, és a címkék alakjában miért nincs három színcsatorna?

**Bekérendő:** Futtasd a teljes cellát. Küldd a két alakot, típust, pixeltartományt és a címkéket.

**Elfogadás – belső támpont:** Képek (16,224,224,3), címkék (16,), float32/int32, 0–255 és 0–4. Az iter/next egy teljes batch-et ad, nem egy képet. Nem kell ezt a szintaxist önállóan kitalálnia.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [D05] Adatbővítés címkeváltozás nélkül

A kis elforgatás és vízszintes tükrözés más nézetet adhat ugyanarról a virágról. Az adatbővítés a modell része lesz, de csak tanításkor működik; a teszt képeit nem torzítjuk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [D05] Adatbővítés címkeváltozás nélkül
adatbovites = keras.Sequential([layers.RandomFlip('horizontal', seed=MAG), layers.RandomRotation(0.05, seed=MAG + 1)], name='augmentation')
bovitett = adatbovites(kepek[:1], training=True)
abra, tengelyek = plt.subplots(1, 2, figsize=(6, 3))
tengelyek[0].imshow(np.clip(kepek[0].numpy(), 0, 255).astype('uint8'))
tengelyek[1].imshow(np.clip(bovitett[0].numpy(), 0, 255).astype('uint8'))
for tengely, cim in zip(tengelyek, ['Eredeti', 'Átalakított']):
    tengely.set_title(cim)
    tengely.axis('off')
plt.tight_layout()
plt.show()
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Az általad látott átalakítás megváltoztatja-e a virág kategóriáját? Indokold röviden.

**Bekérendő:** Egy konkrét átalakítás és értelmezés; a rövid, helyes megfogalmazás elegendő.

**Elfogadás – belső támpont:** Az átalakítás megőrzi a virágkategóriát; csak tanításkor aktív. Nem látott ábráról nem állítható konkrétum.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [F01] Mit jelent a preprocess_input?

A preprocess előfeldolgozást jelent: a képpixeleket olyan számtartományba alakítjuk, amilyenre az előtanított modell számít. A MobileNetV2 saját preprocess_input függvénye a pixel / 127.5 - 1 képletnek megfelelően 0–255-ről −1 és 1 közé skáláz. Az import sor a MobileNetV2-hez tartozó függvényt hozza be, nem magát a bázismodellt tölti le. Az np.array(..., dtype=np.float32) itt egy egyszerű próbatömböt készít; nincs szükség négyszeres szögletes zárójelre. A .copy() megőrzi az eredeti tömböt, így kiírhatjuk az előtte–utána értékeket. A valódi modellben ugyanez az előfeldolgozás később egyszer kerül be a képi műveletek közé.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [F01] A MobileNetV2 saját előfeldolgozó függvénye.
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
proba = np.array([0.0, 127.5, 255.0], dtype=np.float32)
atalakitas = preprocess_input(proba.copy())
print('Eredeti:', proba)
print('Előfeldolgozott:', atalakitas)
```

Futtasd a kész próbacellát, és küldd az eredeti és átalakított értékeket.

**Kérdés:** Ha egy új képet majd a teljes modellnek adunk át, a kód melyik részének kell felelnie az előfeldolgozásért, hogy az ne történjen kétszer?

**Bekérendő:** Futtasd a kész próbacellát, és küldd az eredeti és átalakított értékeket.

**Elfogadás – belső támpont:** 0/127.5/255 → −1/0/1. A teljes modell tartalmazza az egyszeri MobileNetV2-előfeldolgozást; külön /255 vagy újabb preprocess nem kell.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [F02] Előtanított bázis befagyasztása

A bázis képi mintázatokat alakít jellemzőkké. Az ImageNet 1000 osztályos eredeti fejét elhagyjuk. A trainable=False a bázis súlyainak tanítását tiltja; a később létrehozott fej tanítható marad.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [F02] Előtanított bázis befagyasztása
bazis = keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
bazis.trainable = False
print('Bázis:', bazis.output_shape, parameterszam(bazis.trainable_weights))
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Mit hagy el az include_top=False, és melyik kiírt szám igazolja a bázis befagyasztását?

**Bekérendő:** A kimeneti alak és a tanítható bázisparaméterek száma.

**Elfogadás – belső támpont:** ImageNet-súlyok, include_top=False, befagyasztott bázis, (None,7,7,1280), nulla tanítható bázisparaméter.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [F03] Öt osztályos fej és veszteség

A GlobalAveragePooling2D a térbeli jellemzőtérképekből egy vektort készít. A softmax öt osztályra ad eloszlást. A címkék egész számok, így sparse categorical crossentropy illik hozzájuk. A training=False a bázis BN-rétegeit inferencia módban tartja, és nem tiltja le a későbbi gradienseket.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [F03] Öt osztályos fej és veszteség
bemenetek = keras.Input(shape=(224, 224, 3))
x = adatbovites(bemenetek)
x = preprocess_input(x)
x = bazis(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.2, seed=MAG + 2)(x)
kimenetek = layers.Dense(len(OSZTALYNEVEK), activation='softmax')(x)
modell = keras.Model(bemenetek, kimenetek, name='virag_mobilenet')
modell.compile(optimizer=keras.optimizers.Adam(0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
modell.summary()
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** A summary utolsó (None,5) alakjában mit jelent az 5, és hogyan illik ehhez az egész címkéket fogadó veszteség?

**Bekérendő:** A summary utolsó rétegének alakja és rövid saját értelmezés.

**Elfogadás – belső támpont:** Öt softmax kimenet; sparse categorical veszteség egész címkékre; nyers RGB-bemenet; egyszeri előfeldolgozás; bázishívás training=False; tanítható fej.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [F04] Mit tanítunk most?

A fej paraméterszáma a bemeneti jellemzők számából, az osztályszámból és az eltolásokból adódik. A bázisban most nulla tanítható súlyt várunk. Nem kell minden réteget kilistázni.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [F04] Mit tanítunk most?
print('Tanítható:', parameterszam(modell.trainable_weights))
print('Nem tanítható:', parameterszam(modell.non_trainable_weights))
print('Bázis tanítható:', parameterszam(bazis.trainable_weights))
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Ha az F03-ban már ugyanazokat a számokat elküldted, azokat használjuk. A bázis tanítható száma alapján most melyik modellrész tanulhat?

**Bekérendő:** A három paraméterszám, vagy a már ellenőrzött azonos F03-kimenet.

**Elfogadás – belső támpont:** A már F03-ban ellenőrzött számokat ne kérd újra. Csak a fej tanulhat: 6405 tanítható, bázis nulla.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [F05] A fej tanítása

A fit a tanítóból frissíti a fej súlyait. A val_loss alapján a legjobb állapotot mentjük, és két javulás nélküli epoch után megállhatunk. Az 5 epocha felső korlát. Egy ellenőrző lenyomat azt is vizsgálja, hogy a bázis valóban változatlan maradt-e.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [F05] A fej tanítása
def suly_lenyomat(halozat):
    lenyomat = hashlib.sha256()
    for suly in halozat.weights:
        lenyomat.update(suly.numpy().tobytes())
    return lenyomat.hexdigest()
fej_checkpoint = MUNKA / 'head.weights.h5'
finom_checkpoint = MUNKA / 'fine.weights.h5'
bazis_elotte = suly_lenyomat(bazis)
fej_kezdet = time.perf_counter()
fej_tortenet = modell.fit(tanito_adatok, validation_data=validacios_adatok, epochs=5, verbose=2, callbacks=[keras.callbacks.ModelCheckpoint(str(fej_checkpoint), monitor='val_loss', save_best_only=True, save_weights_only=True), keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)])
fej_masodperc = time.perf_counter() - fej_kezdet
bazis_valtozatlan = bazis_elotte == suly_lenyomat(bazis)
assert bazis_valtozatlan
(MUNKA / 'stage_head.json').write_text(json.dumps({'history': fej_tortenet.history, 'seconds': fej_masodperc, 'base_unchanged': bazis_valtozatlan}, indent=2), encoding='utf-8')
print('F05:', len(fej_tortenet.history['loss']), 'legjobb val_loss:', min(fej_tortenet.history['val_loss']), 'bázis változatlan:', bazis_valtozatlan)
gorbek(fej_tortenet, 'Fejtanítás')
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** A saját naplód szerint hogyan változott a tanító és a validációs loss? Ez bizonyítja-e, hogy további epochok mindig javítanának?

**Bekérendő:** Epochszám, legjobb val_loss, bázisváltozatlanság és saját megfigyelés.

**Elfogadás – belső támpont:** Véges veszteségek és 1–5 epocha; a bázis lenyomata változatlan. Nincs minimum accuracy.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T01] Az első fázis állapotának megőrzése

A következő fit ugyanazt a modellobjektumot módosítja. Ezért külön fájlban megőrizzük a legjobb fejállapotot, és abból indulunk tovább. A változatok között így később is visszaléphetünk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T01] Az első fázis állapotának megőrzése
modell.load_weights(fej_checkpoint)
fej_validacio = modell.evaluate(validacios_adatok, verbose=0, return_dict=True)
print('Checkpoint:', fej_checkpoint.name)
print('Fej validáció:', fej_validacio)
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Miért őrizzük meg külön a fejcheckpointot, mielőtt ugyanazt a modellt tovább tanítjuk?

**Bekérendő:** Checkpoint neve és a visszatöltött validációs eredmény; nem beadandó fájlútvonal.

**Elfogadás – belső támpont:** A legjobb fejsúlyokat visszatölti és csak validáción értékel. Az első checkpoint megmarad.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T02A] Rétegek megtekintése és kiválasztásuk bemutatása

Mielőtt bármit taníthatóvá tennénk, nézzük meg a bázis végét. A bazis.layers a rétegobjektumok listája, a [-25:] az utolsó 25 elemet választja ki. A reteg.name a nevet, a type(reteg).__name__ a réteg fajtáját adja; a trainable az aktuális taníthatóság. A startswith("block_16_") azt kérdezi, ezzel az előtaggal kezdődik-e a név, a == "Conv_1" pedig pontos névegyezést vizsgál. Az isinstance(reteg, layers.BatchNormalization) a réteg típusát ellenőrzi. A második ciklus ezeket csak kiírja: itt még nem változtatjuk a súlyokat vagy a taníthatóságot. A következő cellában a kijelölt név és a nem BN típus együtt dönti el a taníthatóságot.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T02A] Előbb nézzük meg a bázis rétegeit. Itt még nem módosítunk semmit.
print('Rétegnév | típus | jelenleg tanítható')
for reteg in bazis.layers[-25:]:
    print(reteg.name, '|', type(reteg).__name__, '|', reteg.trainable)
print('Név alapján kijelölt jelöltek és BN-típusuk:')
for reteg in bazis.layers:
    kijelolt_nev = reteg.name.startswith('block_16_') or reteg.name == 'Conv_1'
    if kijelolt_nev:
        bn_reteg = isinstance(reteg, layers.BatchNormalization)
        print(reteg.name, '| BatchNormalization:', bn_reteg)
```

Futtasd a rétegbemutató cellát, és küldd a kijelölt jelöltek listáját.

**Kérdés:** Nevezz meg a saját listádból egy kijelölt konvolúciós réteget és egy BN-réteget, amelynek befagyasztva kell maradnia.

**Bekérendő:** Futtasd a rétegbemutató cellát, és küldd a kijelölt jelöltek listáját.

**Elfogadás – belső támpont:** A listában szerepelnek a block_16_ rétegek és a Conv_1. A block_16_*_BN és Conv_1_bn típus alapján kimarad; a bemutató cella nem módosít trainable állapotot.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T02] A bemutatott szabállyal kiválasztott rétegek feloldása

Most a T02A-ban megismert szűrést alkalmazzuk. A bazis.trainable=True először engedélyezi a szülőmodell taníthatóságát. Ezután minden rétegen végigmegyünk: a kijelolt_nev logikai érték a névszabályt, a bn_reteg a BatchNormalization típust jelzi. Az if kijelolt_nev and not bn_reteg csak a megfelelő nem BN-rétegeknek állít True értéket, az else minden mást visszafagyaszt. A végén készen kapott ellenőrzők kiírják a tanítható neveket, a tanítható BN-rétegek számát és a paraméterszámot. Ezzel még nem tanítunk; a következő pontban újrakompilálunk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T02] A szülő engedélyezése után rétegenként pontosítjuk a taníthatóságot.
bazis.trainable = True
for reteg in bazis.layers:
    kijelolt_nev = reteg.name.startswith('block_16_') or reteg.name == 'Conv_1'
    bn_reteg = isinstance(reteg, layers.BatchNormalization)
    if kijelolt_nev and not bn_reteg:
        reteg.trainable = True
    else:
        reteg.trainable = False
tanithato_nevek = []
tanithato_bn = 0
for reteg in bazis.layers:
    if reteg.trainable:
        tanithato_nevek.append(reteg.name)
        if isinstance(reteg, layers.BatchNormalization):
            tanithato_bn += 1
print('Tanítható bázisrétegek:', tanithato_nevek)
print('Tanítható BN:', tanithato_bn)
print('Tanítható modellparaméterek:', parameterszam(modell.trainable_weights))
```

Futtasd a teljes megadott cellát. Küldd a tanítható réteglistát, a BN-darabszámot és a paraméterszámot.

**Kérdés:** A saját T02A és T02 listádat összevetve melyik szabály akadályozta meg, hogy a block_16_ névvel kezdődő BN-rétegek is taníthatók legyenek?

**Bekérendő:** Futtasd a teljes megadott cellát. Küldd a tanítható réteglistát, a BN-darabszámot és a paraméterszámot.

**Elfogadás – belső támpont:** Csak a kijelölt nem BN-rétegek taníthatók, BN száma 0; modellparaméter 885445. A kódot készen használja és a feltétel hatását értelmezi.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T03] Újrakompilálás kisebb lépésekkel

A taníthatóság megváltoztatása után új compile kell. Új Adam optimalizálót hozunk létre 1e-5 tanulási rátával; a veszteség és a metrika változatlan. A kisebb lépés óvatosan igazítja az előtanított jellemzőket.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T03] Újrakompilálás kisebb lépésekkel
modell.compile(optimizer=keras.optimizers.Adam(1e-05), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print('Tanulási ráta:', float(modell.optimizer.learning_rate.numpy()))
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Miért kell a trainable állapot módosítása után új compile, és miért kisebb a második tanulási ráta?

**Bekérendő:** Az új learning_rate és a kód szerepének rövid értelmezése.

**Elfogadás – belső támpont:** Új Adam 1e−5, helyes sparse veszteség, compile a rétegmódosítás után. Csak a learning_rate átírása nem elég.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T04] Óvatos finomhangolás

A tanító- és validációs halmaz és az adatbővítés szabálya ugyanaz marad. A BN-rétegek ellenőrzése azt vizsgálja, hogy mozgóátlagaik és súlyaik változatlanok-e. A kijelölt konvolúciós súlyoknak viszont változhat az értéke.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T04] Óvatos finomhangolás
def bn_lenyomat(halozat):
    lenyomat = hashlib.sha256()
    for reteg in halozat.layers:
        if isinstance(reteg, layers.BatchNormalization):
            for suly in reteg.weights:
                lenyomat.update(suly.numpy().tobytes())
    return lenyomat.hexdigest()
bn_elotte = bn_lenyomat(bazis)
konv_elotte = bazis.get_layer('Conv_1').get_weights()[0].copy()
finom_kezdet = time.perf_counter()
finom_tortenet = modell.fit(tanito_adatok, validation_data=validacios_adatok, epochs=5, verbose=2, callbacks=[keras.callbacks.ModelCheckpoint(str(finom_checkpoint), monitor='val_loss', save_best_only=True, save_weights_only=True), keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)])
finom_masodperc = time.perf_counter() - finom_kezdet
bn_valtozatlan = bn_elotte == bn_lenyomat(bazis)
konv_valtozott = not np.array_equal(konv_elotte, bazis.get_layer('Conv_1').get_weights()[0])
assert bn_valtozatlan and konv_valtozott
(MUNKA / 'stage_fine.json').write_text(json.dumps({'history': finom_tortenet.history, 'seconds': finom_masodperc, 'bn_unchanged': bn_valtozatlan, 'conv_changed': konv_valtozott}, indent=2), encoding='utf-8')
print('T04:', len(finom_tortenet.history['loss']), 'legjobb val_loss:', min(finom_tortenet.history['val_loss']))
print('BN változatlan:', bn_valtozatlan, 'Conv_1 változott:', konv_valtozott)
gorbek(finom_tortenet, 'Finomhangolás')
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** A két True ellenőrzés pontosan mit igazol, és mi az, amit ezek önmagukban még nem bizonyítanak minden bázisrétegről?

**Bekérendő:** Epochok, legjobb val_loss, BN- és Conv_1-ellenőrzés.

**Elfogadás – belső támpont:** A bázis rétegszabályát T02 igazolja. A BN-lenyomat változatlan és a Conv_1 módosult, de ez a két ellenőrzés önmagában nem bizonyítja az összes többi réteg változatlanságát. A végső epocha val_accuracy értéke nem feltétlenül a visszatöltött legjobb val_loss állapotáé.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [T05] Modellválasztás validáción

A val_loss és az accuracy eltérő dolgot mér, ezért egyszerre változhatnak különböző irányba. Az előre rögzített döntési szabály a kisebb val_loss; döntetlenben a befagyasztott változatot választjuk. A tesztet még nem használjuk.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [T05] Modellválasztás validáción
modell.load_weights(finom_checkpoint)
finom_validacio = modell.evaluate(validacios_adatok, verbose=0, return_dict=True)
kivalasztott_fazis = 'fine' if finom_validacio['loss'] < fej_validacio['loss'] else 'head'
kivalasztott_checkpoint = finom_checkpoint if kivalasztott_fazis == 'fine' else fej_checkpoint
modell.load_weights(kivalasztott_checkpoint)
valasztas = {'head_validation': fej_validacio, 'fine_validation': finom_validacio, 'selected_stage': kivalasztott_fazis}
(MUNKA / 'selection.json').write_text(json.dumps(valasztas, indent=2), encoding='utf-8')
print('Fej:', fej_validacio)
print('Finomhangolt:', finom_validacio)
print('Kiválasztott:', kivalasztott_fazis)
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** A saját két validációs sorod alapján miért ezt a fázist választotta a kód?

**Bekérendő:** Két validációs sor és a kiválasztott fázis. A tesztet itt még ne használd.

**Elfogadás – belső támpont:** Csak a val_loss alapján választ, a legjobb kiválasztott súlyokat betölti, a döntést teszt előtt menti.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [V00] Argmax, axis és összefűzés kis tömbökön

A végső teszt előtt kis, mesterséges tömbön nézzük meg az új műveleteket; ez nem tesztadat. A példában két minta három-három osztályértéket kap. Egy sor egy minta, egy oszlop egy kategória. Az np.argmax(..., axis=1) minden soron belül a legnagyobb érték indexét adja, nem magát az értéket. A Python-index 0-tól indul. Az np.concatenate(...) több kisebb tömböt fűz össze a megadott sorrendben. A valódi tesztadatok címkéi is batch-enként érkeznek, ezért ezeket egyetlen címketömbbé kell majd összefűzni.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [V00] Két mesterséges minta, mintánként három osztályérték.
pelda = np.array([[0.1, 0.7, 0.2], [0.8, 0.1, 0.1]])
print('Példatömb:', pelda)
print('Soronkénti legnagyobb érték indexe:', np.argmax(pelda, axis=1))
# Két kisebb címketömböt egyetlen tömbbé fűzünk.
cimke_adagok = [np.array([0, 2]), np.array([1])]
print('Összefűzött címkék:', np.concatenate(cimke_adagok))
```

Futtasd a kis példát. Küldd a soronkénti osztályindexeket és az összefűzött címkéket.

**Kérdés:** Az első sorhoz kapott index a sor melyik értékére mutat? Miért fontos megőrizni a címkebatch-ek sorrendjét?

**Bekérendő:** Futtasd a kis példát. Küldd a soronkénti osztályindexeket és az összefűzött címkéket.

**Elfogadás – belső támpont:** Indexek [1,0], összefűzve [0,2,1]. Az index pozíció, nem valószínűség. A sorrendnek a képek becsléseivel egyeznie kell.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [V01] Valós tesztbecslések és a címkebatch-ek összefűzése

A modellválasztás lezárult; most használjuk először a tesztet. A modell.predict(teszt_adatok) a batch-ek képeire ugyanabban a rögzített sorrendben ad becslést. A valoszinusegek táblában 200 sor és öt oszlop lesz: képenként öt kategóriaérték. Az np.argmax(..., axis=1) minden képhez egy osztályindexet választ. A valódi címkéket most szándékosan egyszerű for-ciklussal gyűjtjük: a batch képrésze most nem kell, az aláhúzás ezt jelzi; az adag_cimkek.numpy() a címkéket teszi NumPy-tömbbé; az append az adagokat listába teszi. Az np.concatenate a V00-hoz hasonlóan egyetlen tömbbé fűzi őket. A sum(axis=1) az egy képhez tartozó öt értéket adja össze. A teszt keverését ezért nem kapcsoljuk be. Az első öt becslés azonossága önmagában nem hiba: a teszt mappasorrendje miatt az első képek azonos kategóriából jöhetnek.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [V01] Az összes tesztképhez öt osztályérték tartozik.
valoszinusegek = modell.predict(teszt_adatok, verbose=0)
# Az axis=1 minden soron belül, az öt osztály között választ indexet.
becslesek = np.argmax(valoszinusegek, axis=1)
# A Dataset batch-ekben adja a címkéket. A képrészt most nem használjuk.
cimke_adagok = []
for _, adag_cimkek in teszt_adatok:
    cimke_adagok.append(adag_cimkek.numpy())
valodi_cimkek = np.concatenate(cimke_adagok)
print('Valószínűségek alakja:', valoszinusegek.shape)
print('Becslések alakja:', becslesek.shape)
print('Valódi címkék alakja:', valodi_cimkek.shape)
print('Első öt becslés:', becslesek[:5])
sorosszegek = valoszinusegek.sum(axis=1)
print('Sorösszegek min/max:', sorosszegek.min(), sorosszegek.max())
```

Futtasd a teljes cellát. Küldd a három shape-et, az első öt becslést és a sorösszegek min/max értékét.

**Kérdés:** A saját kimenetedben miért lesz egy osztályindexet tartalmazó tömb alakja (200,), miközben a modell közvetlen kimenete (200,5)?

**Bekérendő:** Futtasd a teljes cellát. Küldd a három shape-et, az első öt becslést és a sorösszegek min/max értékét.

**Elfogadás – belső támpont:** Alakok (200,5), (200,), (200,); indexek 0–4, sorösszeg közel 1. A kép- és címkesorrend azonos. Nem kell listakomprehenziót írnia vagy korábbról ismernie.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [V02] Accuracy és tévesztési mátrix

Az accuracy az összes helyes osztályozás aránya. A mátrix sorai a valódi, oszlopai a becsült kategóriák. A főátló a helyes találatokat mutatja; az összegnek a tesztmintaszámmal kell egyeznie.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [V02] Accuracy és tévesztési mátrix
teszt_pontossag = accuracy_score(valodi_cimkek, becslesek)
matrix = confusion_matrix(valodi_cimkek, becslesek, labels=np.arange(len(OSZTALYNEVEK)))
print('Tesztpontosság:', teszt_pontossag)
print('Mátrix:', matrix)
print('Összeg:', matrix.sum())
megjelenites = ConfusionMatrixDisplay(matrix, display_labels=OSZTALYNEVEK).plot(xticks_rotation=45)
megjelenites.ax_.set_xlabel('Becsült kategória')
megjelenites.ax_.set_ylabel('Valódi kategória')
plt.tight_layout()
plt.show()
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Válassz a saját mátrixodból egy nem nulla, főátlón kívüli cellát, és mondd el, melyik valódi kategóriát minek becsülte. Ha nincs ilyen, értelmezz egy főátlóbeli cellát.

**Bekérendő:** Accuracy, teljes mátrix és összeg; saját cellaértelmezés.

**Elfogadás – belső támpont:** 5×5 egész mátrix; összeg 200, sorösszegek 40. Accuracy = főátlóösszeg/200; sor valódi, oszlop becsült.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [V03] Egy tévesztés megvizsgálása

Egy képből nem bizonyítható általános ok, de konkrét hibajelenség megfigyelhető. Ha nincs hibás kép, a legkevésbé magabiztos helyes döntést vizsgáljuk. A tömbindex 0-tól indul.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [V03] Egy tévesztés megvizsgálása
hibas_indexek = np.flatnonzero(becslesek != valodi_cimkek)
index = int(hibas_indexek[0]) if len(hibas_indexek) else int(np.argmin(valoszinusegek[np.arange(len(valodi_cimkek)), valodi_cimkek]))
teszt_kepek = np.concatenate([adag_kepek.numpy() for adag_kepek, _ in teszt_adatok])
print('Index:', index, 'hibás:', bool(becslesek[index] != valodi_cimkek[index]))
print('Valódi:', OSZTALYNEVEK[valodi_cimkek[index]], 'becsült:', OSZTALYNEVEK[becslesek[index]])
print('Valószínűségek:', valoszinusegek[index])
plt.figure(figsize=(4, 4))
plt.imshow(np.clip(teszt_kepek[index], 0, 255).astype('uint8'))
plt.axis('off')
plt.show()
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** A megjelenített képen mit figyelsz meg ténylegesen? A lehetséges hibaokot jelöld feltételezésnek, ne bizonyítéknak.

**Bekérendő:** Index, valódi/becsült kategória, valószínűségek és saját megfigyelés.

**Elfogadás – belső támpont:** A saját képi leírás elfogadható; egy furcsa nézőpont lehetséges ok, de a kimenetből nem állapítható meg a tanítóképek tipikus nézete. Hibamentes esetben ne nevezd tévesztésnek a választott helyes becslést.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [V04] Egy eddig nem használt kép

A kész betöltő RGB float32 képet ad 0–255 tartományban, egyképes batchként. A modell maga végzi az előfeldolgozást, ezért itt nem szabad ismét preprocess_inputot vagy /255-öt alkalmazni. Egy félretett, eddig nem használt forráskép is megfelel.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [V04] Egy eddig nem használt kép
hasznalt_utvonalak = {sor['relative_path'] for sor in jegyzek}
hasznalt_hashek = {sor['sha256'] for sor in jegyzek}
felreallitott_utvonalak = sorted((utvonal for utvonal in adat_mappa.glob('*/*.jpg') if str(utvonal.relative_to(adat_mappa)) not in hasznalt_utvonalak and fajl_hash(utvonal) not in hasznalt_hashek))
uj_utvonal = felreallitott_utvonalak[0]
uj_adag = kep_betoltese(uj_utvonal)
uj_valoszinusegek = modell.predict(uj_adag, verbose=0)[0]
uj_index = int(np.argmax(uj_valoszinusegek))
print('Új kép:', uj_utvonal)
print('Valószínűségek:', uj_valoszinusegek)
print('Becsült:', OSZTALYNEVEK[uj_index], 'softmax:', float(uj_valoszinusegek[uj_index]))
```

Futtasd a megadott teljes kódcellát; önálló kódírás nem szükséges.

**Kérdés:** Melyik kategóriához tartozik a legnagyobb érték, és miért nem bizonyítja önmagában ez a szám a becslés helyességét?

**Bekérendő:** Becsült kategória és öt softmax-érték; a mappanév referencia-címke lehet, nem láttatja automatikusan a képet.

**Elfogadás – belső támpont:** A kód egyszeri előfeldolgozást biztosít. A softmax és a mappanév alapján ne állíts nem látott képi ellenőrzést. Ha van referencia-címke, ahhoz viszonyított egyezés mondható ki.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [Z01] Saját következtetések

A számok mellett a megoldási döntéseket is értékeljük. A finomhangolás nem minden futásban javít. A teszt alapján ezen a gyakorlaton már nem hangolunk újra.

**Az aktuális teljes kód – elsőre is add meg:**

Nincs programkód ezen a beszélgetési ponton.

Válaszolj röviden a beszélgetésben.

**Kérdés:** Három rövid kérdést beszélünk meg egyenként: mi változott a bemutatókhoz képest; mely súlyok változhattak a két fázisban és ezt mi igazolja; segített-e a finomhangolás validáción és mire való a teszt?

**Bekérendő:** Három saját válasz a beszélgetésben; a korábban már megértett részeket nem kell újravizsgáztatni.

**Elfogadás – belső támpont:** Három kérdés egyenként, rövid saját válaszokkal. A korábban már tisztázott részeket számítsd be; csak lényegi félreértésnél kérj további magyarázatot.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**

## [Z02] Eredmények összefoglalása és a gyakorlat lezárása

A cella összegzi a saját mérési eredményeket és helyben results.json fájlba menti őket. A notebookot saját használatra elmentheted, de a gyakorlat végén nem kell beküldened, feltöltened vagy megosztanod. A lezáráshoz elég az itt megbeszélt futási kimenet és a saját értelmezésed.

**Az aktuális teljes kód – elsőre is add meg:**

```python
# [Z02] Mentés és lezárás
fej_naplo = json.loads((MUNKA / 'stage_head.json').read_text(encoding='utf-8'))
finom_naplo = json.loads((MUNKA / 'stage_fine.json').read_text(encoding='utf-8'))
eredmenyek = {**valasztas, 'test_accuracy': float(teszt_pontossag), 'confusion_matrix': matrix.tolist(), 'head_epochs': len(fej_naplo['history']['loss']), 'fine_epochs': len(finom_naplo['history']['loss']), 'head_seconds': fej_naplo['seconds'], 'fine_seconds': finom_naplo['seconds'], 'base_unchanged': fej_naplo['base_unchanged'], 'bn_unchanged': finom_naplo['bn_unchanged'], 'conv_changed': finom_naplo['conv_changed'], 'tensorflow': tf.__version__, 'numpy': np.__version__, 'split_sizes': {halmaz: sum((sor['split'] == halmaz for sor in jegyzek)) for halmaz in ['train', 'val', 'test']}}
(MUNKA / 'results.json').write_text(json.dumps(eredmenyek, indent=2), encoding='utf-8')
print('Kiválasztott:', kivalasztott_fazis, '| Tesztpontosság:', teszt_pontossag)
print('Eredmények:', MUNKA / 'results.json')
```

Futtasd az összegző cellát. A kiválasztott fázist és a végső tesztpontosságot küldd el az agentnek.

**Kérdés:** Mi a saját futásod legfontosabb tanulsága?

**Bekérendő:** Futtasd az összegző cellát. A kiválasztott fázist és a végső tesztpontosságot küldd el az agentnek.

**Elfogadás – belső támpont:** Elég a saját összegző kimenet és a megbeszélt értelmezés. Nem kérhető notebook, fájlnév, útvonal, mentési bizonyíték vagy beadás.

**Itt állj meg és várj. Rövid, tartalmilag helyes választ fogadj el; ne kérj kötelező újrafogalmazást.**
