# Python alapok · 01. gyakorlat — Gyakorlati útmutató

> **Tárgy:** Programozás Alapjai · **Lecke:** Python alapok 01. (EP_01)
> **Cél:** Az első Python-program írása, mentése és futtatása kétféle szerkesztővel és kétféle terminállal.

---

## 1. A munkakörnyezet: mi hol van?

Ebben a gyakorlatban **két dolgot** használsz: egy **szerkesztőt** (ide írod a kódot) és egy
**terminált** (itt futtatod). Mindkettőből **két választási lehetőséged** van:

| Szerkesztő (kód írása + mentése) | Terminál (kód futtatása) |
|---|---|
| **A. Notepad++** – a Linuxra telepített szövegszerkesztő | **A. Saját beépített Linux-terminál** (+ gomb a kód futtatásához) |
| **B. inno-agent beépített szerkesztője** – a felületen a **jobb oldalon** | **B. inno-agent beépített terminálja** – a munkaterület alatt |

**A lényeg:** a négy elem **szabadon kombinálható**. A kódot írhatod Notepad++-ban, és futtathatod
az inno-agent beépített termináljában — vagy fordítva. Csak arra ügyelj, hogy **mindig a jó fájlt
és a jó mappát** használd.

---

## 2. A munkamappa (a legfontosabb!)

Minden `.py` fájlod egy **azonos mappában** él. Ez a **python_gyakorlat** mappa.

**Pontos elérési út (`cd`-hez):**

```
/home/diak/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
```

**Rövid, másolható `cd` parancs:**
```bash
cd ~/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
```

> ✱ **`~` a saját mappádat jelenti** – itt `/home/diak`. A fenti rövid parancs ugyanoda visz.

### Mi van ebben a mappában?
Jelenleg ezek a fájlok (a gyakorlat során fogod elkészíteni/módosítani őket):

| Fájl | Tartalma (EP_01 alapján) |
|---|---|
| `hello.py` | Az első program: kiírás, idézőjel-vizsgálat |
| `bufe1.py` | Büfé 1/5 – csak üdvözlés |
| `bufe2.py` | Büfé 2/5 – változók és `print()` |
| `bufe3.py` | Büfé 3/5 – műveletek, végösszeg |
| `bufe4.py` | Büfé 4/5 – f-string formázás |
| `bufe5.py` | Büfé 5/5 – `input()` + típuskonverzió |

---

## 3. Hogyan írd a kódot? (a két szerkesztő)

### A) Notepad++ (Linuxon)
1. Nyisd meg a Notepad++-t.
2. **Fájl → Új** (Ctrl+N), majd másold be a kódot az EP_01-ből.
3. **Fájl → Mentés másként…** (vagy Ctrl+S), és navigálj ide:
   ```
   /home/diak/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
   ```
   A fájl neve pontosan `hello.py` legyen (**ne** `hello.py.txt`!). Válassz **UTF-8 kódolást**
   az ékezetes szövegek miatt.
4. A későbbi módosításokat **Ctrl+S**-sel mented.

> ⚠️ **Kódolás:** A Notepad++ a mentésnél **UTF-8** kódolást használjon, különben az ékezetes
> magyar szövegek (`üdv`, `büfé`) romlottan jelennek meg.

### B) inno-agent beépített szerkesztője (jobb oldal)
1. A képernyő **jobb oldalán** találod a **fájl-előnézeti / szerkesztő panelt**.
2. A `python_gyakorlat` mappában kattints a kívánt `.py` fájlra (pl. `hello.py`), és az előugró
   szerkesztőben írd/módosítsd a kódot.
3. A módosítás **automatikusan mentésre** kerül, vagy a panel mentésgombját nyomd meg.
4. A fájl a **munkaterület-struktúrában** tárolódik: ugyanott, ahová a külső Notepad++ is ment.

> ✅ **Előny:** A beépített szerkesztőben **azonnal látod a fájlokat** a bal/jobb oldali fálra nézeten,
> és a mentett fájl rögtön elérhető a terminálból futtatva — nincs navigálgatás a mappák között.

---

## 4. Hogyan futtasd a kódot? (a két terminál)

A Python-programot **a terminál indítja el**, nem a szerkesztő. A futtató parancs mindig:
```bash
python3 <fájlneve>.py
```

### A) Saját beépített terminál (külső)
Ha **saját terminálablakot** nyitsz, előbb **állj be a munkamappába**, majd futtasd:

```bash
cd ~/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
python3 hello.py
```

**Miért kell a `cd`?** Mert a `python3 hello.py` parancs a **fájl nevét** kapja, és a Python abban a
mappában keresi, ahol a terminálod áll. Ha nem a `python_gyakorlat` mappában állsz, a parancs ezt írja:
```
python3: can't open file 'hello.py': [Errno 2] No such file or directory
```
Ha ezt látod, írd be a `cd …`-t, és próbáld újra.

**Ellenőrzés és segédparancsok:**
```bash
pwd     # mutatja, melyik mappában állsz (kötelezően a python_gyakorlat)
ls      # felsorolja a mappa fájljait (köztük a hello.py-t)
python3 --version   # ellenőrzi a Python meglétét
```

### B) inno-agent beépített terminálja
1. A munkaterület **alján/jobb oldalán** találod az inno-agent **beépített terminálját** (a Practice Lab
   / terminál panel).
2. Ez a terminál **alapból a munkaterület mappájában** indít (a `python_gyakorlat` szülőmappájában).
3. Ezért innen egyszerűen lépj be a mappába, és futtass:
   ```bash
   cd python_gyakorlat
   python3 hello.py
   ```
   (Mivel az inno-agent terminálja a munkaterület gyökerében áll, itt a relatív `cd python_gyakorlat` visz
   a fájlokhoz — nincs szükség a teljes útvonal begépelésére.)

> 💡 **Ugyanaz a mappa, két út.** A belső terminál relatív úttal (`cd python_gyakorlat`), a külső
> terminál teljes úttal (`cd ~/.local/opt/inno-agent/.../python_gyakorlat`) ér ugyanabba a mappába.
> A két terminál **ugyanazokat a fájlokat** látja és futtatja.

---

## 5. A teljes munkamenet – lépésről lépésre

**Mentés és futtatás ciklusa (jegyezd meg):**
```
Szerkesztés → Ctrl+S (mentés) → terminál → python3 fájlnév.py
```

Példa a `hello.py` első futására:
1. **Notepad++**-ban vagy az **inno-agent szerkesztőjében** másold be:
   ```python
   print("Hello, világ!")
   ```
2. **Mentsd** `hello.py` néven a `python_gyakorlat` mappába.
3. Nyisd meg a **terminált** (akár saját, akár beépített), állj a mappába, és futtasd:
   ```bash
   python3 hello.py
   ```
4. A kimenet: `Hello, világ!`

**Módosítás + újrafuttatás:**
1. Változtasd meg az idézőjelben a szöveget: `print("2 + 2")` → ments (Ctrl+S).
2. Válts a terminálra, és újra:
   ```bash
   python3 hello.py
   ```
3. A felfelé nyíllal előhívhatod a korábbi parancsot. **Ellenőrizd** mindig, hogy a megfelelő fájl neve szerepel.

---

## 6. Gyakorló feladatok (EP_01 alapján)

> Minden feladatnál: **olvasd el → jósolj → ments → futtass → magyarázd.** A megoldást a tanári lap tartalmazza.

### 1. szint · Alapismeretek megszilárdítása

**1.1. feladat – Az első módosítás** *(hello.py)*
Írd át a `hello.py` első sorát erre: `print("2 + 2")`. Jósold meg a kimenetet, mentsd, futtasd.
Ezután vegyél le az idézőjeleket (`print(2 + 2)`), és futtasd újra. Mit látsz, és miért?

**1.2. feladat – A végrehajtás sorrendje** *(hello.py)*
Írj két `print()` sort: `print("Első sor")` majd `print("Második sor")`. Jósold meg, melyik jelenik meg
előbb. Cseréld fel a két sor teljes egészét, ments, futtass. Írd le, mi változott.

**1.3. feladat – Megjegyzés (#)** *(hello.py)*
A megjegyzés `#` jele elrejti a sort. Futtatandó példa:
```python
# Üdvözöljük a felhasználót.
print("Szia!")  # Ide komment
```
Tedd a `#` jelet a `print("Szia!")` sor elejére, ments, futtass. Mi történik? Írd vissza a `#`-et.

### 2. szint · Készségfejlesztés

**2.1. feladat – Hány teljes doboz?** *(új fájl: doboz.py)*
Kód:
```python
darab = 17
doboz_meret = 5
print(darab // doboz_meret)
print(darab % doboz_meret)
```
Fejtsd ki, mit jelent a `//` és a `%`. Módosítsd a `darab = 17`-et `darab = 20`-ra, ments, futtass, és magyarázd az új kimenetet.

**2.2. feladat – Beszédes változónevek**
Az alábbi kód helyesen számol, de a `c` változó nem árulja el a jelentését:
```python
a = 450
b = 2
c = a * b
print(c)
```
Nevezd át a változókat beszédes, ékezet nélküli magyar névre (pl. `egysegar`, `darabszam`, `fizetendo`),
majd futtasd. A kimenet nem változhat. *(Ügyelj: ha csak az egyik előfordulást írod át, `NameError` lesz!)*

**2.3. feladat – Büfé 3/5 – árhelyesbítés** *(bufe3.py)*
Futtasd a `bufe3.py`-t (kimenet: `Fizetendő: 1790 Ft`). Csak a `kave_darabszam` értékét növeld `2`-ről
`3`-ra, ments, futtass. Hány Ft-tal nő az összeg és miért?

### 3. szint · Bővítés és elmélyítés

**3.1. feladat – Két szám összege, az input() útján** *(új fájl: osszeg.py)*
Készítsd el a következő programot:
```python
elso_szoveg = input("Első szám: ")
masodik_szoveg = input("Második szám: ")
elso_szam = int(elso_szoveg)
masodik_szam = int(masodik_szoveg)
osszeg = elso_szam + masodik_szam
print(f"Az összeg: {osszeg}")
```
Futtasd `5` és `2` bemenettel. Ezután csak a `+`-t használó sort cseréld erre:
`osszeg = elso_szoveg + masodik_szoveg`. Ismét `5` és `2`. Miért lesz a kimenet `52` nem pedig `7`?

**3.2. feladat – Téglalap kerülete és területe** *(új fájl: teglalap.py)*
Készítsd el ezt:
```python
szelesseg = float(input("Szélesség (cm): "))
magassag = float(input("Magasság (cm): "))
kerulet = 2 * (szelesseg + magassag)
terulet = szelesseg * magassag
print(f"Kerület: {kerulet:.2f} cm")
print(f"Terület: {terulet:.2f} cm²")
```
Futtasd `3.5` és `2` bemenettel. Magyarázd meg: miért `float()`, és mit csinál a `:.2f`?

**3.3. feladat – Büfé 5/5 az inno-agent terminálban** *(bufe5.py)*
A `bufe5.py` a felhasználótól kér be adatokat. Futtasd az **inno-agent beépített termináljában**:
```bash
cd python_gyakorlat
python3 bufe5.py
```
Adj meg `Anna`, `2`, `1` adatokat. Ellenőrizd a blokkot. Ezután futtasd **saját (külső) terminálban**
is a teljes úttal. A két futás eredményének **azonosnak** kell lennie — ha nem, ellenőrizd, hogy ugyanabban
a mappában jársz (`pwd`).

---

## 7. Gyors hibakeresés

| Hibaüzenet | Mit ellenőrizz először? |
|---|---|
| `No such file or directory` | A terminál a megfelelő mappában áll-e (`pwd`, majd `cd`)? |
| `NameError: name '...' is not defined` | Helyes-e a változónév, nincs elgépelés / kis-nagybetű eltérés? |
| `TypeError` | Szöveghez nem adhatsz számot: `"Pont: " + 10` hibás. |
| `ValueError` | `int("3.14")` hibás — szöveg formátuma nem illik a konverzióhoz. |
| Romlott ékezetes szöveg | A Notepad++ **UTF-8** kódolással mentett-e? |
| `python3: command not found` | Nincs Python telepítve — szólj az oktatónak. |

> **Az utolsó (hiba)sor a legfontosabb** — általában ott van a hiba neve és rövid oka. Olvasd onnan felfelé.

---

## 8. Ami fontos, hogy megjegyezd

- **A név értékre hivatkozik** — az `=` jobb oldala előbb számolódik ki.
- **A típus meghatározó** — `12` szám, `"12"` szöveg; `type()` megmutatja.
- **`input()` szöveget ad** — számolás előtt `int()` vagy `float()` kell.
- **A kimenetet megtervezzük** — `print()` megjelenít, az f-string (`f"..."`) összeállít.
- **Szerkesztés → Ctrl+S → terminál → `python3 fájlnév.py`** — ez a munkamenet keringője, mindig így járj el.

**Végső ellenőrző `cd` + futtató parancsok (külső terminál):**
```bash
cd ~/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
python3 hello.py
python3 bufe5.py
```