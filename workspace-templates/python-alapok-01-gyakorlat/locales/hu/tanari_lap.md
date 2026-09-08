# Python alapok · 01. gyakorlat — Tanári lap (megoldásokkal és magyarázattal)

> **Tárgy:** Programozás Alapjai · **Lecke:** Python alapok 01. (EP_01)
> **A tanulói lap** feldolgozásához került **javasolt időbecslés:** ~90 perc (környezet-átállás ~20 perc, feladatok ~70 perc).
> Minden feladatnál a tanulási cél, a mintamegoldás és a részletes magyarázat szerepel.

---

## A környezet összefoglalása (oktatónak)

**Két szerkesztő + két terminál, szabadon kombinálható:**

- **Szerkesztők:** Notepad++ (Linux) **és** az inno-agent beépített szerkesztője (a jobb oldali panel).
- **Terminálok:** a diák saját (külső) Linux-terminálja **és** az inno-agent beépített terminálja (a munkaterület alatt).

**Központi munkamappa (minden `.py` fájl itt él):**
```
/home/diak/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat
```
Rövid `cd`: `cd ~/.local/opt/inno-agent/workspace/.presets/python-alapok-01-gyakorlat-hu/python_gyakorlat`

**Pozicionálás (fontos, hogy a diák megértse):**
- A **beépített terminál** a munkaterület gyökerében indul → relatív úttal: `cd python_gyakorlat`.
- A **külső terminál** bárhonnan indul → teljes úttal kell belépni a mappába.
- A két terminál **azonos fájlokat** futtat, mert ugyanabba a mappába navigálnak. Ha a kimenet eltér,
  mindig a `pwd`-vel és az `ls`-sel ellenőriztessük a mappát.

---

## FELADATOK

### 1. szint · Alapismeretek megszilárdítása

#### 1.1. feladat – Az első módosítás *(hello.py)* — Kiírás, idézőjel szerepe

**Kapcsolódó tudáselem:** `print()`, argumentum, az idézőjel mint a kód része.

**Feladat:** Írd át az első sort `print("2 + 2")`-re, majd idézőjelek nélkül `print(2 + 2)`.

**Mintamegoldás:**
```
print("2 + 2")   →  2 + 2        (a kimenetben nincs idézőjel)
print(2 + 2)     →  4            (a Python összeadást végez)
```

**Magyarázat:** Az idézőjelek közé zárt szöveg **literál**, a Python nem értelmezi: a `"2 + 2"` a
`2 + 2` hat karaktert printeli. Idézőjel nélkül a `2 + 2` **kifejezés**, amelyet a Python kiértékel
(`4`). A zárójel mindkét esetben a `print()` hívás része marad. **Gyakori hiba:** a diák azt gondolja,
hogy a kimenetben is megjelenik az idézőjel — nem; az idézőjel csak a kódban látszik.

---

#### 1.2. feladat – A végrehajtás sorrendje *(hello.py)* — Utasítás-végrehajtási sorrend

**Kapcsolódó tudáselem:** az utasítások felülről lefelé hajtódnak végre; `print()` új sort kezd.

**Feladat:** `print("Első sor")` majd `print("Második sor")`; majd cseréld fel őket.

**Mintamegoldás:**
```
print("Első sor")
print("Második sor")
   ↓
Első sor
Második sor
```
A felcserélt változatban `Második sor` jelenik meg felül.

**Magyarázat:** A sorok **szövege** nem vezérli a végrehajtást; a **kódbeli sorrendjük** határozza meg.
Minden `print()` külön sort kezd (az `end` alapértéke sortörés). **Gyakori hiba:** a tanuló hiszi, hogy
az „első" szó miatt az a sor fut előbb — a szöveg tartalma közömbös.

---

#### 1.3. feladat – Megjegyzés (#) *(hello.py)* — Kommentek

**Kapcsolódó tudáselem:** a `#` jeltől a sor végéig tartó megjegyzés; az értelmező nem hajtja végre.

**Feladat:** Tedd a `#` jelet a `print("Szia!")` sor elejére, ments, futtass, majd állítsd vissza.

**Mintamegoldás:**
```python
# Üdvözöljük a felhasználót.
# print("Szia!")   # ebből megjegyzés lett
print("Szia!")      # visszaállítva — fut
```
A `#`-elt változat kimenete **üres** (semmi nem íródik ki).

**Magyarázat:** A `print()` is megjegyzéssé válik, ezért a program nem ír ki semmit — ez **nem hiba**.
Megjegyzésekbe a kód ideiglenes kikapcsolásához is használható. **Gyakori félreértés:** az idézőjelen
**belüli** `#` (pl. `print("# Ez most szöveg.")`) **nem** megjegyzés, hanem a szöveg része — a jelentést
a `#` pozíciója határozza meg.

---

### 2. szint · Készségfejlesztés

#### 2.1. feladat – Hány teljes doboz? *(doboz.py)* — `//` és `%`

**Kapcsolódó tudáselem:** lefelé kerekített hányados (`//`) és maradékképzés (`%`).

**Feladat:** Kód futtatása, majd `darab = 17` → `20` módosítás.

**Mintamegoldás:**
```
darab=17, doboz=5:   3   és   2      →  17 = 3·5 + 2
darab=20, doboz=5:   4   és   0      →  20 = 4·5 + 0
```

**Magyarázat:** A `//` azt mondja meg, **hány teljes (egész) doboz** tölthető meg; a `%` azt, **mennyi
marad**. Az összefüggés mindig: `darab = doboz_szam * doboz_meret + maradek`. Az `5` tizedelésével a
maradék `0` lesz. **Gyakori hiba:** a diák a `/`-t, `//`-t és `%`-t összekeveri — a `/` itt `3.4`-et ad,
a `//` egész hányadost, a `%` maradékot.

---

#### 2.2. feladat – Beszédes változónevek — Névadás, `NameError`

**Kapcsolódó tudáselem:** snake_case névadás; a név minden előfordulásátikor módosítsd következetesen.

**Feladat:** Nevezd át az `a`, `b`, `c` változókat beszédes, ékezet nélküli magyar névre.

**Mintamegoldás:**
```python
egysegar = 450
darabszam = 2
fizetendo = darabszam * egysegar
print(fizetendo)      # kimenet: 900 (változatlan)
```

**Magyarázat:** A jól elnevezett változók **olvashatóvá** teszik a számítás célját, a kimenet nem változik.
Kulcspont: a (át)nevezés **minden előfordulásra** vonatkozik. Ha csak az elsőt írod át, a számítás sorában
`NameError` keletkezik, mert az a név még nem kapott értéket. **Gyakori hiba:** az `=`, `/=` megnevezés
informatikai elvárása; itt pusztán a névadás a cél.

---

#### 2.3. feladat – Büfé 3/5 – árhelyesbítés *(bufe3.py)* — Érték-módosítás hatása

**Kapcsolódó tudáselem:** a bemeneti adat külön változóban tartása; egy adat módosítása.

**Feladat:** A `kave_darabszam` értékét növeld `2`→`3`-ra, és magyarázd az eredményt.

**Mintamegoldás:**
```
Eredeti:  kave_osszeg = 2·450 = 900,  fizetendo = 900 + 890 = 1790
Módosított: kave_osszeg = 3·450 = 1350, fizetendo = 1350 + 890 = 2240
Különbség: +450 Ft (= egy kávé egységára)
```

**Magyarázat:** Mivel az ár és a mennyiség **külön változóban** van, egyetlen adatot módosítottunk, és a
számítás automatikusan követte. A részösszegek külön sora megkönnyíti az ellenőrzést (ellenőrizhetjük:
`3·450 = 1350`). **Gyakori hiba:** ha a diák fejben "újraszámolja" a teljes program helyett, nehézsége
akad — a változók olvasásával triviális.

---

### 3. szint · Bővítés és elmélyítés

#### 3.1. feladat – Két szám összege, az input() útján *(osszeg.py)* — `input()` + `int()`

**Kapcsolódó tudáselem:** `input()` mindig szöveget ad; számtanhoz `int()` konverzió szükséges.

**Feladat:** Futtasd `5` és `2`-vel, majd módosítsd az összeadást szöveg-összefűzésre.

**Mintamegoldás:**
```
int() átalakítással:   elso_szam + masodik_szam = 5 + 2 = 7
konverzió nélkül:      "5" + "2" = "52"
```

**Magyarázat:** Az `input()` **mindig szöveget** ad vissza. A `"5" + "2"` **szöveg-összefűzés** (`"52"`),
nem összeadás. Az `int(szoveg)` eredményét **fel kell használni** — a `szoveg` változó a konverzió után
is szöveg marad. **Gyakori hiba:** a tanuló szerint az `int()` „átalakítja" a változót; valójában a
függvény **új értéket ad vissza**, amit változóhoz rendelünk.

---

#### 3.2. feladat – Téglalap kerülete és területe *(teglalap.py)* — `float()`, `:.2f`

**Kapcsolódó tudáselem:** `float()` törtméretű bemenetekhez; f-string tizedesjegy-formázás.

**Feladat:** Futtasd `3.5` és `2` bemenettel.

**Mintamegoldás:**
```
Kerület: 2*(3.5 + 2) = 11.00 cm
Terület: 3.5 * 2 = 7.00 cm²
```

**Magyarázat:** A `float()` a **tizedestört** méreteket is megengedi (a `2` egész szám beérhető `float()`-nál,
eredmény `2.0`). A `:.2f` **két tizedesjegyre** formázza a kiírást — **csak a megjelenítést**, az értéket
nem kerekíti. **Gyakori hiba:** a diák az `int()`-et használja, ami a `3.5`-öt `3`-ra csonkolja, és hibás
kerületet okoz; itt `float()` kell.

---

#### 3.3. feladat – Büfé 5/5 az inno-agent terminálban *(bufe5.py)* — vegyes alkalmazás

**Kapcsolódó tudáselem:** a teljes bemenet→feldolgozás→kimenet ciklus; a két terminál azonossága.

**Feladat:** Futtasd a `bufe5.py`-t a **belső** és a **külső** terminálban is, `Anna`, `2`, `1` bemenettel.

**Mintamegoldás (mindkét terminálban azonos):**
```
Mi a neved? Anna
Hány kávét kérsz? 2
Hány szendvicset kérsz? 1
Köszönjük, Anna!
Kávé: 2 db, 900 Ft
Szendvics: 1 db, 890 Ft
Fizetendő: 1790 Ft
```

**Magyarázat:** Itt már a teljes programozási mintát gyakoroljuk: **rögzített adatok** (egységárak) →
**felhasználói bemenet** (`input()`) → **konverzió** (`int()`) → **számítás** → **formázott kimenet**
(f-string). A **név** szöveg marad (nem számolunk vele), a **darabszámokat** `int()`-té alakítjuk.
A két terminál ugyanabba a mappába navigálva **azonos kimenetet** ad — ez a feladat lényege. Ha a kimenet
eltér, `pwd` + `ls` ellenőrzés javasolt. **Gyakori hiba (tágabb kontextus):** a diák a `bufe5.py`-t másik
mappából futtatja, és `No such file` hibát kap; a `cd` előírása itt döntő.

---

## Irodalom / forrás

Az EP_01 tananyag (`EP_01.html`) alapján, az SZTE Informatikai Intézet „Programozás Alapjai jegyzet – 01.
gyakorlat" című anyagához és Kégl Tímea „Snake it easy 1." c. könyvének első fejezetéhez illeszkedve.
A feladatlapok a munkaterület `quiz-builder` skillje szerint készültek (tanulói és tanári lap).