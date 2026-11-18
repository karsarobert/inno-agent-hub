# Részletes lecke: teljes kód és értelmezési kérdések

Egy pont, majd várakozás. Z01 három kérdése egyenként.


## [E01] Környezet és munkamegosztás

**Mielőtt bármelyik kódcellát futtatnád, állítsd be a Colab GPU-ját:** Futtatókörnyezet → Futtatókörnyezet típusának módosítása → Hardveres gyorsító: GPU (például T4) → Mentés. A váltás a már feltöltött fájlokat és változókat törölheti, ezért ezzel kezdj. Helyi Jupyter használatát külön jelezd a tutornak. Ezután jöhet E01 ellenőrzése.

Minden kód készen adott. A notebookot Colabban vagy Jupyterben futtatod, a tutorral a működését értelmezed. Colabban GPU-t válassz még az adatok letöltése előtt. A seed a véletlen műveletek kiindulását rögzíti. Az assets mappa a mintaképeké, a dl10_data az adatoké, a dl10_results a helyi eredményeké. Ha a gdown hiányzik, a cella telepíti; a TensorFlow és a többi csomag már működő környezetet feltételez.

```python
import os
os.environ.setdefault("TF_NUM_INTRAOP_THREADS", "2")
os.environ.setdefault("TF_NUM_INTEROP_THREADS", "2")
import sys, json, hashlib, zipfile, subprocess
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications.resnet import preprocess_input
from sklearn.model_selection import train_test_split
try:
    import gdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown==5.2.0", "-q"])
    import gdown
SEED, SIZE, BATCH = 2026, (224, 224), 32
keras.utils.set_random_seed(SEED)
try:
    import google.colab
    colabban = True
except ImportError:
    colabban = False
gpu_lista = tf.config.list_physical_devices("GPU")
print("Environment:", "Colab" if colabban else "Local Jupyter")
print("TensorFlow:", tf.__version__, "GPU:", gpu_lista)
if colabban and not gpu_lista:
    raise RuntimeError("Runtime > Change runtime type > GPU > Save; reconnect and rerun E01.")
mintakepek, adatmappa, munkamappa = Path("assets"), Path("dl10_data"), Path("dl10_results")
for mappa in [mintakepek, adatmappa, munkamappa]:
    mappa.mkdir(exist_ok=True)
def fajl_sha256(utvonal):
    kivonat = hashlib.sha256()
    with open(utvonal, "rb") as folyam:
        for blokk in iter(lambda: folyam.read(1024 * 1024), b""):
            kivonat.update(blokk)
    return kivonat.hexdigest()
```

**Kérdés / minimális bizonyíték:** Küldd el a környezet, TensorFlow és GPU sorait. Milyen eszközön dolgozol?


## [K01] Osztály vagy szám?

A képosztályozó több osztály pontszámát adja; a regressziós fej egyetlen számmal közelít egy numerikus címkét. Az első részben egy előtanított rendszer kimenetét vizsgáljuk, a másodikban új kis fejet tanítunk. Ez beszélgetési pont, nincs kódcella.

**Kérdés / minimális bizonyíték:** Miben különbözik egy „elefánt” osztálypontszám egy életkorcímkét közelítő számtól?


## [C01] Két új mintakép

A két mintaképet és az ImageNet-címkelistát a tananyaghoz mellékelt **DL10_assets.zip** tartalmazza; C01 nem kér képet az Imgurtól vagy más külső képforrástól. Ha az assets fájljai már helyesek, ezeket használja. Egyébként a notebook munkamappájában lévő ZIP-et bontja ki; Colabban hiányzó ZIP esetén feltöltőgombot nyit. Válaszd ki a kicsomagolt tananyag innoagent mappájából a DL10_assets.zip fájlt. Ezt a Colabba töltöd fel a futtatáshoz, nem az Innoagentnek, és nem beadásként. Helyi Jupyterben tedd a ZIP-et a notebook munkamappájába. A teljes kód készen adott: ellenőrzi mindhárom fájl SHA-256 értékét, majd a kész rgb_betoltese segéd RGB-ként 224×224 méretre alakítja a képeket. ResNet-előfeldolgozás még nincs.

```python
# A csomag mintakepeit hasznaljuk, kulso kepforrasrol nem toltunk le.
import io
kep_hashek = {'elephant.png': '51f9c798db2cbff325032496d9a54e7ddd9471924d7c57583f12ae16d550919d', 'imagenet_class_index.json': 'a1e7a966a1f601d39e4b43e119b3e7dd4a2ad3ea08cf69847cbaf021013767bc', 'sunflower.jpg': 'ff9b4c356d65c2e9708dd0b07cc4c3f2080996cfdb9db7cee259aca7bcedfe6a'}
hianyzo_kepek = [fajlnev for fajlnev, elvart_hash in kep_hashek.items()
    if not (mintakepek / fajlnev).exists() or fajl_sha256(mintakepek / fajlnev) != elvart_hash]
if hianyzo_kepek:
    kepcsomag_utvonal = Path("DL10_assets.zip")
    if kepcsomag_utvonal.exists():
        kepcsomag_bajtok = kepcsomag_utvonal.read_bytes()
    elif colabban:
        from google.colab import files
        print("Valaszd ki a kicsomagolt tananyag DL10_assets.zip fajljat. A Colabba toltod fel, nem a tutornak.")
        feltoltott_fajlok = files.upload()
        if len(feltoltott_fajlok) != 1:
            raise RuntimeError("Pontosan egy fajlt valassz: DL10_assets.zip. Futtasd ujra a C01 cellat.")
        kepcsomag_bajtok = next(iter(feltoltott_fajlok.values()))
    else:
        raise FileNotFoundError("Tedd a DL10_assets.zip fajlt a notebook munkamappajaba, majd futtasd ujra a C01 cellat.")
    with zipfile.ZipFile(io.BytesIO(kepcsomag_bajtok)) as archivum:
        ellenorzott_kepek = {}
        for fajlnev, elvart_hash in kep_hashek.items():
            if fajlnev not in archivum.namelist():
                raise ValueError("A kepcsomagbol hianyzik: " + fajlnev)
            fajltartalom = archivum.read(fajlnev)
            if hashlib.sha256(fajltartalom).hexdigest() != elvart_hash:
                raise ValueError("Hibas kepellenorzo osszeg. Az eredeti DL10_assets.zip szukseges: " + fajlnev)
            ellenorzott_kepek[fajlnev] = fajltartalom
    mintakepek.mkdir(exist_ok=True)
    for fajlnev, fajltartalom in ellenorzott_kepek.items():
        (mintakepek / fajlnev).write_bytes(fajltartalom)
    if not kepcsomag_utvonal.exists():
        _ = kepcsomag_utvonal.write_bytes(kepcsomag_bajtok)
for fajlnev, elvart_hash in kep_hashek.items():
    assert fajl_sha256(mintakepek / fajlnev) == elvart_hash, fajlnev
print("Mintakepek ellenorizve; nem volt szukseg kulso kepforrasrol letoltesre.")
def rgb_betoltese(utvonal):
    kep = tf.image.decode_image(tf.io.read_file(str(utvonal) if isinstance(utvonal, Path) else utvonal),
                                  channels=3, expand_animations=False)
    kep.set_shape([None, None, 3])
    return tf.image.resize(kep, SIZE, method="bilinear")
mintakepek_tombje = [rgb_betoltese(mintakepek / nev).numpy() for nev in ["elephant.png", "sunflower.jpg"]]
abra, tengelyek = plt.subplots(1, 2, figsize=(9, 4))
for tengely, kep in zip(tengelyek, mintakepek_tombje):
    tengely.imshow(kep.astype(np.uint8)); tengely.axis("off")
    print("RGB shape:", kep.shape, "range:", kep.min(), kep.max())
plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** A két shape-ben mit jelent a 224, a másik 224 és a 3?


## [C02] ResNet50 és az előfeldolgozó segéd

A batch_elokeszitese kész segéd egy nyers RGB-képhez batch-dimenziót ad, másolatot készít, majd egyszer lefuttatja a ResNet preprocess_input műveletét. Ez RGB→BGR váltást és ImageNet-csatornaátlagok kivonását jelenti, nem 0–1 skálázást. Az osztalyozo logitot ad; a valószínűséget külön softmax számolja. A bázis itt már betanított és nem tanul.

```python
osztalyozo = keras.applications.ResNet50(weights="imagenet", classifier_activation=None)
osztalyozo.trainable = False
def batch_elokeszitese(kep):
    return preprocess_input(np.array(kep, dtype=np.float32, copy=True)[None, ...])
elokeszitett_minta = batch_elokeszitese(mintakepek_tombje[0])
print("Prepared batch:", elokeszitett_minta.shape, "range:", elokeszitett_minta.min(), elokeszitett_minta.max())
print("Classifier output:", osztalyozo.output_shape)
osztaly_index = json.loads((mintakepek / "imagenet_class_index.json").read_text())
```

**Kérdés / minimális bizonyíték:** Miért lenne hibás a batch_elokeszitese előtt külön /255-öt is alkalmazni?


## [C03] Logit, softmax és top-5

Az argmax a legnagyobb érték indexét, az argsort a rendezés indexeit adja. A [::-1] fordított sorrend, a [: 5] az első öt elem. A JSON ugyanazt az osztályindexet kapcsolja névhez. A softmaxértékek összege 1, de ez nem igazolt megbízhatóság vagy referencia-címke.

```python
osztaly_logitok = [osztalyozo(batch_elokeszitese(kep), training=False).numpy()[0] for kep in mintakepek_tombje]
osztaly_valoszinusegek = [tf.nn.softmax(ertekek).numpy() for ertekek in osztaly_logitok]
for kep_sorszam, valoszinusegek in enumerate(osztaly_valoszinusegek):
    legjobb_indexek = np.argsort(valoszinusegek)[::-1][:5]
    print("Image:", kep_sorszam)
    for index in legjobb_indexek:
        print(int(index), osztaly_index[str(index)][1], "probability:", round(float(valoszinusegek[index]), 5),
              "logit:", round(float(osztaly_logitok[kep_sorszam][index]), 4))
celosztaly = int(np.argmax(osztaly_valoszinusegek[0]))
kontrollosztaly = next(int(kulcs) for kulcs, ertek in osztaly_index.items() if ertek[0] == "n03063599")
print("Fixed target:", celosztaly, osztaly_index[str(celosztaly)][1])
print("Control:", kontrollosztaly, osztaly_index[str(kontrollosztaly)][1])
```

**Kérdés / minimális bizonyíték:** Küldd el az első kép top-1 sorát. Ez a modell becslése vagy bizonyított képcímke?


## [C04] Jellemzőtérkép és súlyozott összeg

A get_layer név szerint kiválasztja a réteget, a Model két kimenetet tesz egyszerre megfigyelhetővé. A get_weights kernel- és biastömböt ad. A tensordot itt az utolsó, csatornatengelyt összegzi a súlyvektorral; a két térbeli tengely megmarad. Először 2×2×3 tömbön nézzük meg, nem kell kézzel kiszámolni.

```python
aktivacios_proba = keras.Model(osztalyozo.inputs,
    [osztalyozo.get_layer("conv5_block3_out").output, osztalyozo.output])
osztaly_sulyok, osztaly_bias = osztalyozo.get_layer("predictions").get_weights()
aktivacios_ertekek, logitok = aktivacios_proba(batch_elokeszitese(mintakepek_tombje[0]), training=False)
print("Activation shape:", aktivacios_ertekek.shape, "Kernel:", osztaly_sulyok.shape)
pelda_jellemzok = np.arange(12, dtype=np.float32).reshape(2, 2, 3)
pelda_sulyok = np.array([0.2, -0.4, 0.7])
pelda_terkep = np.tensordot(pelda_jellemzok, pelda_sulyok, axes=([-1], [0]))
print("Toy map shape:", pelda_terkep.shape, "values:\n", pelda_terkep)
print("GAP then Dense:", pelda_jellemzok.mean(axis=(0, 1)) @ pelda_sulyok + 0.3)
print("CAM mean plus bias:", pelda_terkep.mean() + 0.3)
```

**Kérdés / minimális bizonyíték:** Miért 2×2 a kis súlyozott térkép, és melyik dimenzió tűnt el?


## [C05] Klasszikus CAM és a logit ellenőrzése

A klasszikus_cam és a elojeles_rajz már teljesen megadott függvény. Az első nyers, előjeles térképet és a cél logitját adja; a második közös pozitív/negatív színskálán rajzol. Az átlag(CAM)+bias egyezés a GAP→Dense szerkezet ellenőrzése, nem bizonyítja a kép osztályát. A pozitív térkép normalizálója konstans/nem pozitív térképnél nullát ad, nem oszt nullával.

```python
def klasszikus_cam(kep, osztaly_id):
    aktivaciok, pontszamok = aktivacios_proba(batch_elokeszitese(kep), training=False)
    nyers_terkep = np.tensordot(aktivaciok.numpy()[0], osztaly_sulyok[:, osztaly_id], axes=([-1], [0]))
    pontszam = float(pontszamok.numpy()[0, osztaly_id])
    visszaszamolt = float(nyers_terkep.mean() + osztaly_bias[osztaly_id])
    assert np.isclose(pontszam, visszaszamolt, atol=1e-4, rtol=1e-4)
    return nyers_terkep, pontszam

def pozitiv_normalizalas(nyers_terkep):
    pozitiv = np.maximum(nyers_terkep, 0.)
    if np.ptp(pozitiv) < 1e-8 or pozitiv.max() <= 1e-8:
        return np.zeros_like(pozitiv)
    return pozitiv / pozitiv.max()

def elojeles_rajz(tengely, kep, nyers_terkep, cim, hatar):
    tengely.imshow(kep.astype(np.uint8), extent=(0, 1, 0, 1))
    rajz = tengely.imshow(nyers_terkep, extent=(0, 1, 0, 1), cmap="coolwarm", alpha=0.55,
                       vmin=-hatar, vmax=hatar, interpolation="bilinear")
    tengely.set_title(cim, fontsize=10); tengely.axis("off")
    return rajz

elso_cam, elso_pontszam = klasszikus_cam(mintakepek_tombje[0], celosztaly)
print("Target logit:", elso_pontszam, "CAM mean+bias:", float(elso_cam.mean() + osztaly_bias[celosztaly]))
print("Raw CAM min/max:", elso_cam.min(), elso_cam.max())
print("Constant-map guard:", np.array_equal(pozitiv_normalizalas(np.ones((2, 2))), np.zeros((2, 2))))
abra, tengely = plt.subplots(figsize=(6, 4))
rajz = elojeles_rajz(tengely, mintakepek_tombje[0], elso_cam, osztaly_index[str(celosztaly)][1], max(float(np.abs(elso_cam).max()), 1e-8))
abra.colorbar(rajz, ax=tengely, label="Signed contribution"); plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** A nyers CAM és a 0–1-re megjelenített térkép ugyanazt a számskálát jelenti?


## [C06] Két célosztály, közös skála

Ugyanarra a képre kérjük a rögzített top-1 és a coffee_mug kontrollosztály térképét. Az osztály nevét és saját valószínűségét mindig kiírjuk. A két térkép azonos színtartományt kap, így a szín abszolút skálája összevethető. Ez nem egyezik a külön-külön min–max normalizált megjelenítéssel.

```python
kontroll_cam, kontroll_pontszam = klasszikus_cam(mintakepek_tombje[0], kontrollosztaly)
kozos_hatar = max(float(np.abs(elso_cam).max()), float(np.abs(kontroll_cam).max()), 1e-8)
abra, tengelyek = plt.subplots(1, 2, figsize=(10, 4))
for tengely, osztaly_id, nyers_terkep in zip(tengelyek, [celosztaly, kontrollosztaly], [elso_cam, kontroll_cam]):
    valoszinuseg = float(osztaly_valoszinusegek[0][osztaly_id])
    print(osztaly_id, osztaly_index[str(osztaly_id)][1], "probability:", valoszinuseg,
          "raw min/max:", float(nyers_terkep.min()), float(nyers_terkep.max()))
    rajz = elojeles_rajz(tengely, mintakepek_tombje[0], nyers_terkep, osztaly_index[str(osztaly_id)][1], kozos_hatar)
abra.colorbar(rajz, ax=tengelyek.tolist(), label="Shared signed scale"); plt.show()
masodik_osztaly = int(np.argmax(osztaly_valoszinusegek[1]))
masodik_cam, masodik_pontszam = klasszikus_cam(mintakepek_tombje[1], masodik_osztaly)
print("Second image CAM-logit agreement:", True, osztaly_index[str(masodik_osztaly)][1])
```

**Kérdés / minimális bizonyíték:** Miért lehet más a két hőtérkép, ha a bemeneti kép ugyanaz maradt?


## [C07] Rögzített kitakarási kísérlet

A kész kód egy előre rögzített középső téglalapot szürkére cserél. A célosztály az eredeti top-1 marad, akkor is, ha a kitakart képen megváltozik a top-1. Így ugyanazt a kérdést mérjük újra. A változás a kitakarás hatása az adott modellen; az eloszláson kívüli szürke folt miatt nem tiszta oksági bizonyítás.

```python
kitakart_kep = mintakepek_tombje[0].copy()
kitakart_kep[64:176, 64:176, :] = 127.5
kitakart_cam, kitakart_pontszam = klasszikus_cam(kitakart_kep, celosztaly)
kitakart_valoszinusegek = tf.nn.softmax(osztalyozo(batch_elokeszitese(kitakart_kep), training=False)[0]).numpy()
uj_legjobb = int(kitakart_valoszinusegek.argmax())
print("Fixed target:", osztaly_index[str(celosztaly)][1])
print("Target logits original/occluded:", elso_pontszam, kitakart_pontszam, "change:", kitakart_pontszam - elso_pontszam)
print("Target probabilities:", float(osztaly_valoszinusegek[0][celosztaly]), float(kitakart_valoszinusegek[celosztaly]))
print("New top1:", osztaly_index[str(uj_legjobb)][1])
hatar = max(float(np.abs(elso_cam).max()), float(np.abs(kitakart_cam).max()), 1e-8)
abra, tengelyek = plt.subplots(1, 2, figsize=(10, 4))
for tengely, kep, nyers_terkep, cim in zip(tengelyek, [mintakepek_tombje[0], kitakart_kep], [elso_cam, kitakart_cam], ["Original", "Fixed occlusion"]):
    rajz = elojeles_rajz(tengely, kep, nyers_terkep, cim, hatar)
abra.colorbar(rajz, ax=tengelyek.tolist(), label="Shared signed scale"); plt.show()
cam_eredmenyek = {"target": celosztaly, "target_name": osztaly_index[str(celosztaly)][1],
               "original_logit": elso_pontszam, "occluded_logit": kitakart_pontszam,
               "control_probability": float(osztaly_valoszinusegek[0][kontrollosztaly])}
_ = (munkamappa / "cam_results.json").write_text(json.dumps(cam_eredmenyek, indent=2))
```

**Kérdés / minimális bizonyíték:** Hogyan változott az eredeti célosztály logitja? Mire nem elegendő ez az egy mérés?


## [C08] Mit nem bizonyít a hőtérkép?

A CAM a választott osztályhoz kapcsolódó, súlyozott térbeli hozzájárulás. Nem tárgydetektálás vagy pixelszintű referencia-maszk. A Grad-CAM más, gradiensalapú eljárás; a mostani klasszikus CAM súlyokat használ, nem deriváltat. Nincs futtatandó cella.

**Kérdés / minimális bizonyíték:** Miért lehet félrevezető egy kis osztályvalószínűséghez tartozó, külön normalizált élénk térkép?


## [A01] Az életkoros adatok betöltése

A biztosított letöltő és kicsomagoló kód a bemutató CSV-jét és ZIP-jét használja. A SHA-256 a referencia fájlváltozatot rögzíti. A CSV file_name oszlopa képhez, a real_age numerikus célcímkéhez kapcsolódik. A helyi csomagból az eredeti APPA-REAL-felosztás nem igazolható, ezért itt dokumentált saját felosztást készítünk. A kód nem azonosít személyeket.

```python
adatforrasok = {'labels.csv': {'id': '15G625qvDsp8wDgydwaiAgAXzfSq3I7NS', 'sha256': '7fc5cd15a21e17eccbb3242963bbd2bafa78cbf4ab1453339c9670f88f7f5e65'}, 'final_files.zip': {'id': '1rXFvWYz6UCv4aD_YT741wbthqm_BBnqY', 'sha256': '716bc1f6ce68406f3212b024592241ecc0131f234c8f5a82af6a2f333e72fff5'}}
for fajlnev, leiras in adatforrasok.items():
    utvonal = adatmappa / fajlnev
    if not utvonal.exists():
        gdown.download(id=leiras["id"], output=str(utvonal), quiet=False)
    if not utvonal.exists() or fajl_sha256(utvonal) != leiras["sha256"]:
        raise RuntimeError("Dataset missing or checksum differs: " + fajlnev)
kepmappa = adatmappa / "final_files"
if not kepmappa.exists():
    with zipfile.ZipFile(adatmappa / "final_files.zip") as archivum:
        for elem in archivum.infolist():
            cel = (adatmappa / elem.filename).resolve()
            if not cel.is_relative_to(adatmappa.resolve()):
                raise ValueError("Invalid archive member")
        archivum.extractall(adatmappa)
cimkek = pd.read_csv(adatmappa / "labels.csv")
print("CSV rows:", len(cimkek), "columns:", cimkek.columns.tolist())
print(cimkek.head().to_string(index=False))
assert {"file_name", "real_age"}.issubset(cimkek.columns) and kepmappa.is_dir()
```

**Kérdés / minimális bizonyíték:** Melyik CSV-oszlop kapcsolja össze a képfájlt a numerikus célértékkel?


## [A02] Adatellenőrzés és eloszlás

A kész ellenőrzés minden fájlt megnyit, a dekódolt RGB-tartalom hashét is számolja, és numerikus, 0–120 közötti címkét vár. Hibás képet és ellentmondó címkéjű azonos képeket kizár; azonos címkéjű másolatból egy marad. A kizárásokat táblázat őrzi. Ez nem személyazonosság szerinti elkülönítés: két különböző kép ugyanarról a személyről megmaradhat.

```python
rekordok, kizartak = [], []
for sor in cimkek[["file_name", "real_age"]].itertuples(index=False):
    try:
        kor = float(sor.real_age)
        utvonal = kepmappa / str(sor.file_name)
        if not utvonal.resolve().is_relative_to(kepmappa.resolve()) or not np.isfinite(kor) or not 0 <= kor <= 120:
            raise ValueError("Invalid path or age")
        with Image.open(utvonal) as kep:
            rgb = kep.convert("RGB")
            kep_hash = hashlib.sha256(str(rgb.size).encode() + rgb.tobytes()).hexdigest()
        rekordok.append({"file_name": str(sor.file_name), "real_age": kor, "image_hash": kep_hash})
    except Exception as hiba:
        kizartak.append({"file_name": str(sor.file_name), "reason": type(hiba).__name__})
ellenorzott = pd.DataFrame(rekordok).sort_values("file_name").reset_index(drop=True)
ellentmondasok = ellenorzott.groupby("image_hash")["real_age"].nunique()
ellentmondo_hashek = set(ellentmondasok[ellentmondasok > 1].index)
ellentmondas_maszk = ellenorzott.image_hash.isin(ellentmondo_hashek)
for fajlnev in ellenorzott.loc[ellentmondas_maszk, "file_name"]:
    kizartak.append({"file_name": fajlnev, "reason": "Conflicting duplicate labels"})
ellenorzott = ellenorzott.loc[~ellentmondas_maszk].copy()
masolat_maszk = ellenorzott.duplicated("image_hash", keep="first")
for fajlnev in ellenorzott.loc[masolat_maszk, "file_name"]:
    kizartak.append({"file_name": fajlnev, "reason": "Duplicate RGB content"})
tiszta_cimkek = ellenorzott.loc[~masolat_maszk].reset_index(drop=True)
pd.DataFrame(kizartak, columns=["file_name", "reason"]).to_csv(munkamappa / "excluded.csv", index=False)
print("Valid unique images:", len(tiszta_cimkek), "Excluded:", len(kizartak))
print("Age range:", tiszta_cimkek.real_age.min(), tiszta_cimkek.real_age.max())
print(pd.DataFrame(kizartak).get("reason", pd.Series(dtype=str)).value_counts().to_string())
abra, tengely = plt.subplots(figsize=(8, 3))
tengely.hist(tiszta_cimkek.real_age, bins=np.arange(0, 125, 5), color="#6c5bb4")
tengely.set(xlabel="Dataset age label (years)", ylabel="Count"); plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** A saját adatjelentésedben hány használható kép maradt, és milyen korlátozást nem old meg a képhash?


## [A03] A megadott felosztósegéd hívása

A felosztas_elokeszitese függvényt a cella már definiálja: egy ellenőrzött adatkeretet és seedet kap, három adatkeretet ad vissza. A 0–19, 20–39, 40–59 és 60+ címkecsoportok arányait őrzi a 60/20/20 körüli saját felosztásban. A két train_test_split hívás egy kész technikai megoldás; nem kell megírnod. Az eltérő halmazok kép-hashei nem fedhetik egymást.

```python
AGE_BINS = [-0.001, 20, 40, 60, 121]
AGE_GROUPS = ["0-19", "20-39", "40-59", "60+"]
def felosztas_elokeszitese(adatkeret, veletlenmag):
    adatkeret = adatkeret.copy()
    adatkeret["age_group"] = pd.cut(adatkeret.real_age, bins=AGE_BINS, labels=AGE_GROUPS, right=False)
    tanito_tabla, maradek = train_test_split(adatkeret, test_size=0.4, random_state=veletlenmag, stratify=adatkeret.age_group)
    validacios_tabla, teszt_tabla = train_test_split(maradek, test_size=0.5, random_state=veletlenmag + 1, stratify=maradek.age_group)
    return [resz.sort_values("file_name").reset_index(drop=True) for resz in [tanito_tabla, validacios_tabla, teszt_tabla]]
tanito_tabla, validacios_tabla, teszt_tabla = felosztas_elokeszitese(tiszta_cimkek, SEED)
manifest = pd.concat([resz.assign(split=nev) for nev, resz in [("train", tanito_tabla), ("validation", validacios_tabla), ("test", teszt_tabla)]], ignore_index=True)
assert manifest.image_hash.is_unique
manifest.to_csv(munkamappa / "split_manifest.csv", index=False)
print("Custom split (not official APPA-REAL):")
print(pd.crosstab(manifest.split, manifest.age_group).to_string())
print("Split sizes:", len(tanito_tabla), len(validacios_tabla), len(teszt_tabla))
```

**Kérdés / minimális bizonyíték:** Melyik halmaz frissíti a súlyokat, melyik választ checkpointot, és melyik marad a végső értékeléshez?


## [A04] Adatfolyamok és egy teljes batch

A from_tensor_slices összepárosítja a fájlútvonalat és címkét. A map betölti a képet, a batch(32) csoportosít. A tanító-, validációs és tesztadatfolyam most létrejött; még egyik sincs ResNet-előfeldolgozva. Az iter bejárót készít, a next egy elemet kér: itt egy egész képek–címkék köteget. A nyers adatfolyamok rendezettek a későbbi jellemzőcache illesztéséhez.

```python
beallitasok = tf.data.Options()
beallitasok.threading.private_threadpool_size = 2
beallitasok.threading.max_intra_op_parallelism = 2
def nyers_adatok(adatkeret):
    utvonalak = [str(kepmappa / nev) for nev in adatkeret.file_name]
    adatfolyam = tf.data.Dataset.from_tensor_slices((utvonalak, adatkeret.real_age.to_numpy(np.float32)))
    adatfolyam = adatfolyam.map(lambda utvonal, kor: (rgb_betoltese(utvonal), kor), num_parallel_calls=2)
    return adatfolyam.batch(BATCH).with_options(beallitasok).prefetch(1)
nyers_tanito = nyers_adatok(tanito_tabla)
nyers_validacios = nyers_adatok(validacios_tabla)
nyers_teszt = nyers_adatok(teszt_tabla)
batch_kepek, batch_cimkek = next(iter(nyers_tanito))
print("First raw batch:", batch_kepek.shape, batch_cimkek.shape)
print("Raw pixel range:", float(tf.reduce_min(batch_kepek)), float(tf.reduce_max(batch_kepek)))
```

**Kérdés / minimális bizonyíték:** A két shape alapján a next egyetlen képet vagy egy teljes batch-párt adott?


## [A05] Előfeldolgozás egyszer és következetesen

A nyers_tanito/nyers_validacios/nyers_teszt nyers adatfolyamából a map most a ResNet által várt tömböket készíti. A nyers képet megőrizzük rajzoláshoz, mert a BGR-csatornákból kivont átlagú tömb közvetlen imshow-ja nem normál RGB-megjelenítés. Egy ismert [10, 20, 30] RGB-pixel külön ellenőrzést ad.

```python
def modell_adatok(adatfolyam):
    return adatfolyam.map(lambda kepek, korok: (preprocess_input(kepek), korok), num_parallel_calls=2)
tanito_adatok = modell_adatok(nyers_tanito)
validacios_adatok = modell_adatok(nyers_validacios)
teszt_adatok = modell_adatok(nyers_teszt)
feldolgozott_kepek, feldolgozott_cimkek = next(iter(tanito_adatok))
ismert_pixel = np.array([[[[10., 20., 30.]]]], dtype=np.float32)
print("Known RGB pixel -> model input:", preprocess_input(ismert_pixel.copy()).reshape(-1))
print("Model batch:", feldolgozott_kepek.shape, "range:", float(tf.reduce_min(feldolgozott_kepek)), float(tf.reduce_max(feldolgozott_kepek)))
assert feldolgozott_kepek.shape == batch_kepek.shape
```

**Kérdés / minimális bizonyíték:** Miért az eredeti RGB-tömböt rajzoljuk, és nem közvetlenül az előfeldolgozott tömböt?


## [B01] Mit jelent a MAE?

Előbb három ismert címkén és becslésen számolunk. Az előjeles hiba becslés−címke; az abszolút érték az irányt eltávolítja. A mean az abszolút eltéréseket átlagolja. Ez nem személyenként garantált ± hibahatár, és nem konfidenciaintervallum.

```python
pelda_cimkek = np.array([10., 30., 70.])
pelda_becslesek = np.array([14., 22., 72.])
pelda_hibak = pelda_becslesek - pelda_cimkek
print("Signed errors:", pelda_hibak)
print("Absolute errors:", np.abs(pelda_hibak))
print("MAE in years:", np.abs(pelda_hibak).mean())
```

**Kérdés / minimális bizonyíték:** A saját kiírásban melyik abszolút hiba nagyobb az átlagnál, és miért nem ellentmondás ez?


## [B02] Kép nélküli medián-baseline

A medián csak a tanítócímkékből készül. Minden validációs képhez ugyanezt az állandó számot adja. Ez azt vizsgálja, mit tud egy képet egyáltalán nem használó viszonyítási alap. A validáció címkéit nem használjuk a medián meghatározásához.

```python
tanito_median = float(tanito_tabla.real_age.median())
alap_validacios_mae = float(np.abs(validacios_tabla.real_age.to_numpy() - tanito_median).mean())
print("Training median:", tanito_median)
print("Baseline validation MAE:", alap_validacios_mae)
```

**Kérdés / minimális bizonyíték:** Miért fontos, hogy a CNN eredményét ehhez az egyszerű becsléshez is hasonlítsuk?


## [F01] Befagyasztott jellemzőkinyerő

A jellemzokinyero ugyanannak a ResNetnek a végső konvolúciós jellemzőit adja. A GAP térbeli átlagot számol, ezért képenként 2048 szám marad. A taníthatóság le van tiltva, és a hívás training=False módú: a BN mozgóállapota sem frissül.

```python
jellemzokinyero = keras.Model(osztalyozo.inputs, osztalyozo.get_layer("conv5_block3_out").output)
jellemzokinyero.trainable = False
terbeli_atlag = layers.GlobalAveragePooling2D()
elso_jellemzok = jellemzokinyero(feldolgozott_kepek, training=False)
elso_vektorok = terbeli_atlag(elso_jellemzok)
print("Spatial features:", elso_jellemzok.shape, "GAP vectors:", elso_vektorok.shape)
print("Trainable extractor weights:", len(jellemzokinyero.trainable_weights))
assert elso_vektorok.shape[-1] == 2048 and not jellemzokinyero.trainable_weights
```

**Kérdés / minimális bizonyíték:** Melyik két dimenziót tüntette el a GAP a jellemzőtérképből?


## [F02] Rendezett jellemzőcache

A kész jellemzok_kinyerese végigolvassa a rendezett adatfolyamot és csak a GAP-vektorokat tárolja. A cache azonosítja a képhasheket, sorrendet, súlyokat, TensorFlow-verziót és előfeldolgozást. Csak egyező azonosítók mellett tölthető vissza. Most tanító és validációs jellemzőket készítünk; a teszt később következik. A kiírás külön jelzi a friss kinyerést és a cache betöltését.

```python
suly_kivonat = hashlib.sha256()
for valtozo in jellemzokinyero.weights:
    suly_kivonat.update(valtozo.numpy().tobytes())
kinyero_hash = suly_kivonat.hexdigest()
cache_mappa = Path(os.environ.get("DL10_CACHE_DIR", str(munkamappa / "feature_cache")))
cache_mappa.mkdir(parents=True, exist_ok=True)
def jellemzok_kinyerese(adatfolyam, adatkeret, nev):
    azonosito = {"files": adatkeret.file_name.tolist(), "hashes": adatkeret.image_hash.tolist(),
                "weights": kinyero_hash, "tensorflow": tf.__version__,
                "preprocess": "tf_decode_rgb_resize_bilinear224_resnet_caffe_v1"}
    alairas = hashlib.sha256(json.dumps(azonosito, sort_keys=True).encode()).hexdigest()
    utvonal = cache_mappa / (nev + "_" + alairas[:16] + ".npz")
    if utvonal.exists():
        with np.load(utvonal, allow_pickle=False) as mentett:
            if str(mentett["signature"].item()) != alairas or not np.array_equal(mentett["files"], adatkeret.file_name.to_numpy(str)):
                raise ValueError("Cache identity mismatch")
            jellemzok, korok = mentett["features"], mentett["ages"]
        print("Cache hit:", nev, jellemzok.shape)
    else:
        jellemzo_reszek, kor_reszek = [], []
        for sorszam, (kepek, korok) in enumerate(adatfolyam):
            jellemzo_reszek.append(terbeli_atlag(jellemzokinyero(kepek, training=False)).numpy())
            kor_reszek.append(korok.numpy())
            if sorszam % 30 == 0:
                print("Extracting:", nev, "batch", sorszam + 1, "/", len(adatfolyam))
        jellemzok, korok = np.concatenate(jellemzo_reszek), np.concatenate(kor_reszek)
        np.savez_compressed(utvonal, features=jellemzok, ages=korok, files=adatkeret.file_name.to_numpy(str), signature=alairas)
    assert len(jellemzok) == len(adatkeret) and np.array_equal(korok, adatkeret.real_age.to_numpy(np.float32))
    assert np.isfinite(jellemzok).all()
    return jellemzok, korok
tanito_jellemzok, tanito_korok = jellemzok_kinyerese(tanito_adatok, tanito_tabla, "train")
validacios_jellemzok, validacios_korok = jellemzok_kinyerese(validacios_adatok, validacios_tabla, "validation")
print("Cached vector shapes:", tanito_jellemzok.shape, validacios_jellemzok.shape)
```

**Kérdés / minimális bizonyíték:** Mit takarítunk meg a következő tanítási epochákban, és miért csak befagyasztott bázissal érvényes ez?


## [M01] Egykimenetű, lineáris regressziós fej

A fej 2048 súlyt és egy biast tanít, összesen 2049 paramétert. Nincs softmax: évben értelmezett valós számot ad. Nulla kernelsúly és tanítómedián bias mellett kezdetben minden mintára a baseline-t adja. A bázis változatlan. Negatív vagy szokatlan becslést később nem vágunk le észrevétlenül.

```python
keras.utils.set_random_seed(SEED)
fej_bemenet = keras.Input(shape=(2048,))
fej_kimenet = layers.Dense(1, name="age_output", kernel_initializer="zeros",
    bias_initializer=keras.initializers.Constant(tanito_median))(fej_bemenet)
korfej = keras.Model(fej_bemenet, fej_kimenet, name="age_head")
korfej.compile(optimizer=keras.optimizers.Adam(1e-3), loss="mae", metrics=["mae"])
kezdeti_becslesek = korfej(validacios_jellemzok[:8], training=False).numpy().reshape(-1)
print("Head parameters:", korfej.count_params())
print("Initial predictions:", kezdeti_becslesek)
print("Matches training median:", np.allclose(kezdeti_becslesek, tanito_median))
assert korfej.count_params() == 2049 and np.allclose(kezdeti_becslesek, tanito_median)
```

**Kérdés / minimális bizonyíték:** Miért egy kimenetünk van az ImageNet 1000 kimenete helyett, és mi tanul most?


## [M02] A kis fej tanítása

Legfeljebb 20 rövid epochát futtatunk a cache-elt vektorokon. A from_tensor_slices itt már jellemzővektorokat és korcímkéket párosít, nem képet dekódol. Az EarlyStopping három javulás nélküli epocha után leállít, a checkpoint a legkisebb val_mae súlyait őrzi. Várd meg a fit végét. Új teljes próbához M01-től indulj, ne adj újabb 20 epochát a már tanult fejhez.

```python
fej_tanito_adatok = tf.data.Dataset.from_tensor_slices((tanito_jellemzok, tanito_korok)).shuffle(len(tanito_korok), seed=SEED).batch(BATCH).with_options(beallitasok)
fej_validacios_adatok = tf.data.Dataset.from_tensor_slices((validacios_jellemzok, validacios_korok)).batch(BATCH).with_options(beallitasok)
fej_fajl = munkamappa / "age_head_best.weights.h5"
tortenet = korfej.fit(fej_tanito_adatok, validation_data=fej_validacios_adatok, epochs=20, verbose=2,
    callbacks=[keras.callbacks.ModelCheckpoint(str(fej_fajl), monitor="val_mae", mode="min", save_best_only=True, save_weights_only=True),
               keras.callbacks.EarlyStopping(monitor="val_mae", mode="min", patience=3)])
(munkamappa / "head_history.json").write_text(json.dumps(tortenet.history, indent=2))
print("Best validation epoch:", int(np.argmin(tortenet.history["val_mae"])) + 1)
```

**Kérdés / minimális bizonyíték:** A saját utolsó két epochád train/val MAE értékei hogyan alakultak?


## [M03] A legjobb állapot külön mérése

A load_weights a legkisebb validációs MAE-hez tartozó fejállapotot állítja vissza. Ezután újramérünk a validáción; ez eltérhet az utolsó epocha értékétől. A baseline összehasonlítási alap, nem kötelezően legyőzendő célérték. A teszt még nem szerepel ebben a választásban.

```python
korfej.load_weights(fej_fajl)
utani_kivonat = hashlib.sha256()
for valtozo in jellemzokinyero.weights:
    utani_kivonat.update(valtozo.numpy().tobytes())
assert utani_kivonat.hexdigest() == kinyero_hash
print("All backbone weights unchanged:", True)
validacios_metrikak = korfej.evaluate(fej_validacios_adatok, verbose=0, return_dict=True)
validacios_metrikak = {kulcs: float(ertek) for kulcs, ertek in validacios_metrikak.items()}
valasztas = {"best_epoch": int(np.argmin(tortenet.history["val_mae"])) + 1,
             "validation": validacios_metrikak, "baseline_validation_mae": alap_validacios_mae}
(munkamappa / "selection.json").write_text(json.dumps(valasztas, indent=2))
print("Restored validation:", validacios_metrikak, "Baseline:", alap_validacios_mae)
abra, tengely = plt.subplots(figsize=(8, 3))
tengely.plot(range(1, len(tortenet.history["mae"]) + 1), tortenet.history["mae"], label="Train MAE")
tengely.plot(range(1, len(tortenet.history["val_mae"]) + 1), tortenet.history["val_mae"], label="Validation MAE")
tengely.axhline(alap_validacios_mae, linestyle="--", color="gray", label="Median baseline validation")
tengely.set(xlabel="Epoch", ylabel="MAE (years)"); tengely.legend(); plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** A saját visszatöltött validációs MAE-d kisebb vagy nagyobb a baseline-nál?


## [V01] Végső teszt és egyéni hibák

A legjobb fejállapot már rögzített. Most készül a tesztjellemző és a CNN/medián végső tesztmérése. A signed_error pozitív, ha a becslés nagyobb a címkénél. A cache sorrendjét ellenőrizzük, a hibákat fájlnévhez rendeljük. A teszt alapján nincs új tanítás vagy új checkpointválasztás.

```python
teszt_jellemzok, teszt_korok = jellemzok_kinyerese(teszt_adatok, teszt_tabla, "test")
fej_teszt_adatok = tf.data.Dataset.from_tensor_slices((teszt_jellemzok, teszt_korok)).batch(BATCH).with_options(beallitasok)
teszt_metrikak = {kulcs: float(ertek) for kulcs, ertek in korfej.evaluate(fej_teszt_adatok, verbose=0, return_dict=True).items()}
kor_becslesek = np.concatenate([korfej(teszt_jellemzok[kezdet:kezdet+BATCH], training=False).numpy().reshape(-1)
                                  for kezdet in range(0, len(teszt_jellemzok), BATCH)])
hibak = teszt_tabla[["file_name", "real_age", "age_group"]].copy()
hibak["prediction"] = kor_becslesek
hibak["signed_error"] = hibak.prediction - hibak.real_age
hibak["absolute_error"] = hibak.signed_error.abs()
alap_teszt_mae = float(np.abs(teszt_korok - tanito_median).mean())
assert np.isclose(hibak.absolute_error.mean(), teszt_metrikak["mae"], atol=1e-4)
hibak.to_csv(munkamappa / "test_errors.csv", index=False)
print("CNN test:", teszt_metrikak, "Median baseline test MAE:", alap_teszt_mae)
print("Negative predictions:", int((kor_becslesek < 0).sum()))
print(hibak.head().to_string(index=False))
```

**Kérdés / minimális bizonyíték:** Mennyivel tér el a CNN teszt-MAE-je a baseline-tól a saját futásodban?


## [V02] Csoportonkénti hiba és elemszám

A csoportokat még a felosztás előtt rögzítettük, nem a teszteredmény alapján választjuk őket. Minden csoportnál az n, a MAE és az előjeles átlaghiba együtt szerepel. A kis n ingadozóbb összehasonlítást adhat. Ez leíró tesztelemzés, nem teljes méltányossági tanúsítvány.

```python
csoport_hibak = hibak.groupby("age_group", observed=False).agg(
    n=("absolute_error", "size"), mae=("absolute_error", "mean"), mean_signed_error=("signed_error", "mean"))
print(csoport_hibak.to_string())
csoport_hibak.to_csv(munkamappa / "age_group_errors.csv")
abra, tengely = plt.subplots(figsize=(7, 3))
tengely.bar(csoport_hibak.index.astype(str), csoport_hibak.mae, color="#6c5bb4")
tengely.set(xlabel="Fixed age-label group", ylabel="Test MAE (years)"); plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** Melyik csoportodban van a legkevesebb minta, és miért óvatosabb az ottani átlag értelmezése?


## [V03] Kis és nagy hiba: valódi minták

A kész kód a legkisebb és a legnagyobb teszt-abszolút hibájú mintát rajzolja. A címke az adathalmazból ismert, nem a tutor arckép alapján kitalált életkora. Csak a ténylegesen látott képről mondj megfigyelést. A lehetséges ok nem bizonyítja, hogyan néz ki általában a tanítóhalmaz.

```python
pelda_indexek = [int(hibak.absolute_error.idxmin()), int(hibak.absolute_error.idxmax())]
abra, tengelyek = plt.subplots(1, 2, figsize=(9, 4))
for tengely, index in zip(tengelyek, pelda_indexek):
    sor = hibak.loc[index]
    kep = rgb_betoltese(kepmappa / sor.file_name).numpy()
    tengely.imshow(kep.astype(np.uint8)); tengely.axis("off")
    tengely.set_title(f"Dataset label: {sor.real_age:.1f}\nPrediction: {sor.prediction:.1f}; abs error: {sor.absolute_error:.1f}", fontsize=10)
    print(sor[["file_name", "real_age", "prediction", "absolute_error"]].to_dict())
plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** A nagy hibájú mintán milyen tényleges képi megfigyelést tudsz tenni, és mi marad csupán hipotézis?


## [X01] Regressziós hozzájárulási térkép

A lineáris korfej ugyanúgy súlyozza a 2048 csatornát, de most egyetlen skalárhoz. Az előjeles térkép átlaga és a bias együtt adja a kimenetet. A pozitív térképrész a modell számát növeli, nem az arcrész „valódi életkora”. Az egyezés a számítási szerkezetet igazolja, nem a becslés pontosságát vagy okságot. Ez nem korosztály-CAM és nem Grad-CAM.

```python
index = pelda_indexek[1]
kep = rgb_betoltese(kepmappa / hibak.loc[index, "file_name"]).numpy()
terbeli_jellemzok = jellemzokinyero(batch_elokeszitese(kep), training=False).numpy()[0]
regresszios_sulyok, regresszios_bias = korfej.get_layer("age_output").get_weights()
regresszios_terkep = np.tensordot(terbeli_jellemzok, regresszios_sulyok[:, 0], axes=([-1], [0]))
visszaszamolt_kor = float(regresszios_terkep.mean() + regresszios_bias[0])
kep_becsles = float(korfej(terbeli_atlag(tf.convert_to_tensor(terbeli_jellemzok[None])), training=False).numpy()[0, 0])
print("Map mean:", float(regresszios_terkep.mean()), "Bias:", float(regresszios_bias[0]))
print("Reconstructed/image/cache predictions:", visszaszamolt_kor, kep_becsles, float(kor_becslesek[index]))
assert np.isclose(visszaszamolt_kor, kep_becsles, atol=2e-3, rtol=1e-4)
assert np.isclose(kep_becsles, kor_becslesek[index], atol=2e-3, rtol=1e-4)
abra, tengely = plt.subplots(figsize=(6, 4))
rajz = elojeles_rajz(tengely, kep, regresszios_terkep, "Regression contribution (not a class)", max(float(np.abs(regresszios_terkep).max()), 1e-8))
abra.colorbar(rajz, ax=tengely, label="Signed contribution to prediction"); plt.tight_layout(); plt.show()
```

**Kérdés / minimális bizonyíték:** Mit jelent a pozitív hozzájárulás, és miért kell a bias értékét is megtartani?


## [Z01] Három záró összefüggés

A következő három kérdést a tutor külön-külön teszi fel. Nincs új kód; a rövid, tartalmilag helyes válasz elegendő.

**Kérdés / minimális bizonyíték:** 1. Miben különbözik a CAM osztálylogitja a regressziós fej skalárjától?
2. Miért nem ± hibahatár a MAE?
3. Mit nem igazol önmagában egy látványos hozzájárulási térkép?


## [Z02] Saját összegzés, beadás nélkül

A kész kód helyi results.json összegzést ír. Ez személyes kimenet, nem beadandó. A notebookot saját célra elmentheted; nem kell feltölteni, megosztani, fájlnevet vagy mentési bizonyítékot küldeni. A saját tanulság után lezárjuk a gyakorlatot.

```python
osszefoglalo = {"seed": SEED, "tensorflow": tf.__version__, "split": "custom stratified 60/20/20; not official APPA-REAL",
           "sizes": {"train": len(tanito_tabla), "validation": len(validacios_tabla), "test": len(teszt_tabla)},
           "trainable_head_parameters": korfej.count_params(), "selection": valasztas,
           "cnn_test": teszt_metrikak, "baseline_test_mae": alap_teszt_mae,
           "group_errors": csoport_hibak.reset_index().to_dict(orient="records"), "cam": cam_eredmenyek,
           "limits": "MAE is not an individual bound; heatmaps are not causal evidence or age-eligibility verification."}
(munkamappa / "results.json").write_text(json.dumps(osszefoglalo, indent=2))
print(json.dumps(osszefoglalo, indent=2))
```

**Kérdés / minimális bizonyíték:** Mi volt a legfontosabb tanulságod a saját eredményeidből?
