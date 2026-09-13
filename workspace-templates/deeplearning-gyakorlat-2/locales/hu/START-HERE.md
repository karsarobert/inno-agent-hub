# Helyi indítás – az óra előtt

Alapkörnyezet: **64 bites Linux x86-64, Python 3.12, CPU**.
A programokhoz nincs szükség Colabra, Jupyterre vagy GPU-ra. Az ellenőrzött
főcsomag-verziókat a `requirements.txt` tartalmazza. Ez nem az összes
közvetett függőség teljes zárolása; a főcsomagok verziói rögzítettek.

## 1. Munkamappa és Python

Nyisd meg a kicsomagolt `DL_02_Innoagent` mappát a fájlkezelőben,
majd ott nyiss terminált. A forrásfájlokat a megszokott szövegszerkesztővel nyisd meg.

```bash
pwd
ls
python3.12 --version
```

Az `ls` eredményében az `agent.md`, a `requirements.txt` és a `G02_01_egy_suly.py`
fájlnak is szerepelnie kell. Ubuntu 24.04-en a szokásos Python 3.12 használható.
Ha a `python3.12` parancs hiányzik, az oktatóval egyeztess a telepítésről;
ne cseréld le a rendszer Pythonját. A tananyag más platformra nincs külön ellenőrizve.

## 2. Külön virtuális környezet

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

A `.venv` a munkamappa saját csomagkörnyezete. A `source` aktiválja;
ezután a `python` és `python -m pip` ennek a környezetnek a programját használja.
A telepítés internetet és több száz MB letöltést igényelhet, ezért előre végezd el.
Ne használd a `sudo pip` parancsot, és ne telepíts a rendszer Pythonjára.

Ha a virtuális környezet létrehozása a `venv` vagy `ensurepip` hiányát jelzi,
Ubuntu alatt az oktató/rendszergazda a megfelelő `python3.12-venv` csomag
telepítésével tudja előkészíteni a gépet. Ezt nem a tanítási feladat részeként végezzük.

## 3. Ellenőrzés

```bash
python kornyezet_ellenorzes.py
mkdir -p naplok
python G02_01_egy_suly.py
```

Az ellenőrző program kiírja a Python elérési útját, a csomagverziókat,
a helyi adatfájl meglétét és egy TensorFlow-próbaszámítást. A sikeres végén
„A kornyezetellenorzes sikeres” jelenik meg. Ez a környezet működését ellenőrzi;
a teljes tanítási példákat külön dolgozzuk fel.

A hiányzó GPU nem hiba. A csomag a TensorFlow CPU-változatát használja,
a programok CPU-futtatásra vannak beállítva. A futásidő a helyi géptől függ.

## 4. Új terminál megnyitásakor

A munkamappában ismét aktiváld a környezetet:

```bash
source .venv/bin/activate
```

Ezután például:

```bash
python G02_02_eloreterjesztes.py
```

A `python` parancsot az aktivált környezetben használd. A programok minden
futtatáskor újraindulnak; a notebookokkal ellentétben nincs korábban futtatott
cellákból megmaradó változóállapot.

## 5. Tipikus technikai akadályok

| Jelenség | Mit ellenőrizz? |
|---|---|
| `ModuleNotFoundError` | Aktív-e a `.venv`, sikerült-e a telepítés? Futtasd újra a környezetellenőrzést. |
| Nem található a `.py` fájl | A csomag megfelelő mappájában állsz-e? Nézd meg a `pwd` és `ls` eredményét. |
| Nem található a CSV | Az `adatok/red-wine.csv` része a csomagnak; a teljes mappát csomagold ki. |
| Nem nyílik meg ábraablak | A program képfájlt ment. Nyisd meg a kimenetben megadott mappa PNG-fájlját. |
| Nem látszik élő tanítási kimenet | Naplózott futtatásnál a fájlba kerül. Befejezés után használd a tutor által adott `tail` parancsot. |
| `Traceback` és kivétel | Küldd el a hiba végén látható kivételnevet és az érintett forrássort. |
| A TensorFlow importja alacsony szintű hibával leáll | Az oktatóval ellenőrizd a CPU és a csomagok kompatibilitását; a mai TensorFlow binárisai CPU-utasításkészletet is feltételeznek. |

Ne indíts több tanítást egyszerre a saját gépen. Egy futás befejezését várd meg,
majd a hozzá tartozó mappa eredményét vizsgáld. Ha leállítottad a programot,
a részleges logot ne tekintsd teljes sikeres futásnak.

Telepítési háttér: [TensorFlow hivatalos pip-útmutató](https://www.tensorflow.org/install/pip).

## 6. A szemléltető megnyitása

A `szemlelteto.html` fájlt nyisd meg a helyi böngészőben. Ehhez nem kell
webszerver vagy internet. Az „Egy súly” és „Kis hálózat” lapokon az előző és
következő gombbal léptethetsz. A hálózat súlyai és biasai a nyilakon, illetve
a neuronoknál láthatók. A lenyitható beállításokban minden paraméter módosítható.

A HTML-ben megváltoztatott szám nem módosítja a Python-kódot. Futás előtti
összehasonlításnál a megfelelő példát válaszd, vagy állítsd be a saját értékeket.
