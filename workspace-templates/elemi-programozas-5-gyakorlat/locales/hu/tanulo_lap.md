# EP_05 – szótáras árjegyzék, saját átalakításokkal

Az EP_04 folytatása, két 45 perces blokkban. A tutor elmagyarázza a példát, rövid mintát mutat, majd te szerkeszted, mented és futtatod a saját fájlodat. A kódíró feladatokat két záró teszt követi; csak a kódismereti tesztben lesz futtatás előtti kimenetértelmezés.

A .py fájlok futtatható, de szándékosan hiányos kezdőminták. Néhány eredményük kezdetben hibás vagy hiányos a célfeladathoz képest: például az összegző még darabot számol, a szűrő még kiír és None-t ad vissza. Ezeket alakítod át. Egy sikeres indítás önmagában nem kész feladat.

Minden .py a munkatér gyökerében van. A Futtatás gombhoz a felület terminálja is a megnyitott fájl mappájában álljon; itt ez mindig ugyanaz a gyökér. A feladatok között nincs mappaváltás. Mentés után kattints a Futtatás gombra. A B2 input-kérdéseire a terminálban válaszolj, Enterrel.

A külön kis fájlok saját próbaárjegyzékeket használnak. Ezek önálló példák, nem egy közös élő rendszer. A végső bufe_05.py-ban már egyetlen kézzel karbantartott árjegyzék legyen.

## Időterv

| Első 45 perc | Perc | Második 45 perc | Perc |
|---|---:|---|---:|
| A1 – Árkeresés | 8 | B2.b – Próbák és új termék | 8 |
| A2 – Ellenőrzött árfrissítés | 8 | Z1 – Önálló kódátalakítás | 10 |
| A3 – Kínálatszűrés | 8 | T1 – 10 elméleti kérdés | 10 |
| B1 – Kosárösszeg és blokk | 10 | T2 – 10 kódismereti kérdés | 15 |
| S1 – Rövid összegzés | 2 | S2 – Eredmény és lezárás | 2 |
| B2.a – Függvények összekapcsolása | 9 | | |
| **Összesen** | **45** | **Összesen** | **45** |

Ez a gyorsabban haladó csoportnak szánt, tömörített 90 perces terv; a két teszt együtt 25 perc. A szünet külön idő. A B2.a az első blokk végére kerül, a B2.b a második elejére. Az idő becslés: a szükséges próbákat nem szabad igazolás nélkül késznek nevezni. Lassabb haladásnál a félbemaradt programozás vagy teszt kimondott folytatási ponttal kerül későbbre. A tesztet sem teljesítjük kész válaszok átadásával. A beépített C1–C3 és K5 feladatok tényleges időnyereség esetén, a régi K-feladatok külön választásra indulnak; nem férnek automatikusan ebbe a keretbe.

## A1 – Árkeresés egységesített névvel

**Fájl:** `arkereses.py`. **Időkeret:** 8 perc.

### A program célja

A termék nevét egységesíted, és megkülönbözteted az ismert árat a hiányzó terméktől.

### Értsük meg a kezdőmintát

A szótár kulcsa a terméknév, értéke az ár. A get hiányzó kulcsnál None-t ad; ez nem 0 és nem a "None" szöveg. Az arat_keres már lekérdez, de még a nyers nevet használja. A hívó rész egyelőre magyarázat nélkül írja ki az eredményt. A számot visszaadó keresés és az üzenet megjelenítése külön feladat.

### Rövid analóg minta

```python
telefonok = {"anna": "06201234567"}
telefonszam = telefonok.get("bela")
if telefonszam is None:
    print("Nincs ilyen név.")
else:
    print(telefonszam)
```

### Most te alakítsd át

1. Az arat_keres függvényben készíts egységes terméknevet a kapott szövegből: szélső szóközök levágása, kisbetűsítés. Ezzel a kulccsal kérdezz le a kapott arak szótárból; ismeretlen terméknél maradjon None az eredmény.
2. A főprogram nyers print sorát alakítsd if–else elágazássá. Hiánynál Nincs ilyen termék., egyébként a talált ár és Ft jelenjen meg. A függvényen belül ne legyen print vagy input.
3. Ments és futtasd a Futtatás gombbal. A keresett_termek értékét átírva próbáld ki az A1.1–A1.3 esetet. Az árjegyzéket ne módosítsa a keresés.

### Kész, ha

- A függvény a paraméter szövegét egységesíti, és a paraméter árjegyzékből kérdez le.
- Hiány és 0 nem keveredik: a hívó None-t vizsgál, nem az ár igazságértékét.
- Az árjegyzék változatlan; a függvény visszaad, a hívó kiír.

### Próbák

### A1.1

Alapárjegyzék; keresett_termek = "  KÁVÉ  ".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Ár: 450 Ft


### A1.2

Alapárjegyzék; keresett_termek = "pizza".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Nincs ilyen termék.
- A pizza nem kerül bele az árjegyzékbe.


### A1.3

Alapárjegyzék; keresett_termek = "   ".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Nincs ilyen termék.


### A1.4 – választható pluszpróba

Pluszpróba: ideiglenesen vedd fel a "víz": 0 bejegyzést; keresd a vizet.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Ár: 0 Ft; nem hiányjelzés.


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#lekerdezes). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## A2 – Meglévő ár ellenőrzött frissítése

**Fájl:** `arfrissites.py`. **Időkeret:** 8 perc.

### A program célja

Csak létező termék pozitív egész próbaárát írod át, és jelzed, hogy megtörtént-e a módosítás.

### Értsük meg a kezdőmintát

A kezdőminta minden kulcsot beállít: új kulcsot is felvesz, és hibás árat is elfogad. Ezt ellenőrzött frissítéssé alakítod. A szótár paraméterként átadása nem készít másolatot, ezért a függvény a hívó szótárát módosítja. A frissítés eredménye logikai érték, nem az új ár.

### Rövid analóg minta

```python
ferohelyek = {"a101": 24, "b204": 40}
ferohelyek["a101"] = 28
ferohelyek["c012"] = 18
print(len(ferohelyek))
```

### Most te alakítsd át

1. Az arat_frissit elején egységesítsd a terméknevet. A meglévő értékadást csak akkor engedd végrehajtani, ha a név már kulcs az arak szótárban és az uj_ar nagyobb 0-nál.
2. Elutasításkor False legyen a visszatérési érték, és semmi ne változzon az árjegyzékben. Sikeres frissítéskor True legyen az eredmény. A függvény ne írjon ki.
3. A kezdő főprogram már kiírja a visszatérési értéket és a teljes szótárat. Ezt használd a próbákhoz: írd át a keresett_termek és uj_ar adatokat, ments, futtass. Minden próba az eredeti négy árból induljon.

### Kész, ha

- Csak meglévő kulcs pozitív egész próbaárát módosítja.
- Elutasításkor nem hoz létre új kulcsot, és a régi árat sem írja felül.
- Egységesít és True/False értéket ad vissza; nem printtel jelzi a függvény eredményét.

### Próbák

### A2.1

Új futás az alapárakkal; " KÁVÉ ", 500.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- True; a kávé ára 500 Ft.
- Továbbra is négy kulcs van; a többi ár változatlan.


### A2.2

Új futás az alapárakkal; "pizza", 700.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; nincs pizza kulcs; az árjegyzék teljesen változatlan.


### A2.3

Új futás az alapárakkal; "kávé", 0.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; a kávé ára 450 marad.


### A2.4

Új futás az alapárakkal; "kávé", -50.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; a kávé ára 450 marad.


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#modositas). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## A3 – Megfizethető termékek listája

**Fájl:** `kinalat.py`. **Időkeret:** 8 perc.

### A program célja

A kiíró bejárásból szűrő függvényt alakítasz: új listát kapsz a keretből megfizethető terméknevekkel.

### Értsük meg a kezdőmintát

A kezdő függvény már items() segítségével bejárja a párokat, de minden terméket kiír, és nincs hasznos visszatérési értéke. A két ciklusváltozó a kulcsot és az árat kapja. A te feladatod a feltétel és az új eredménylista hozzáadása. A keretbe pontosan beleférő termék is megfelelő.

### Rövid analóg minta

```python
ferohelyek = {"a101": 24, "b204": 40, "c012": 25}
letszam = 25
for terem_neve, ferohely in ferohelyek.items():
    if ferohely >= letszam:
        print(terem_neve)
```

### Most te alakítsd át

1. A megfizetheto_termekek függvényben a ciklus előtt hozz létre új üres eredménylistát.
2. A ciklusban a feltétel nélküli kiírás helyére írj ellenőrzést. Legfeljebb a keretbe kerülő termék nevét add az eredménylistához; az árat ne tedd bele.
3. A ciklus után add vissza a listát. A meglévő főprogram írja ki az eredményt. A függvény ne írjon ki és ne módosítsa az árjegyzéket.
4. Ments, majd a keret változtatásával futtasd az A3.1–A3.3 próbát. Az üres árjegyzéket is próbáld ki.

### Kész, ha

- A keret paramétert használja, <= feltétellel; a határértéket is elfogadja.
- Új listát épít nevekkel, a return a teljes bejárás után van.
- Nincs kiírás a függvényben és nem változtatja az arak szótárat.

### Próbák

### A3.1

Alapárjegyzék; keret = 450.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- ["kávé", "üdítő"]; a megadott beszúrási sorrendben.


### A3.2

Alapárjegyzék; keret = 389.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- []


### A3.3

Alapárjegyzék; keret = 890.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- ["kávé", "szendvics", "üdítő", "croissant"]


### A3.4

arak = {}; keret = 450.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- []; hiba nélkül.


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#bejaras). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## B1 – Kosárból összeg, fizetés nélkül

**Fájl:** `osszegzes.py`. **Időkeret:** 10 perc.

### A program célja

A kosár minden tételéhez árat keresel, és a darabszámot számoló kezdőmintát pénzösszegzéssé alakítod.

### Értsük meg a kezdőmintát

A kosár a feldolgozandó terméknevek listája. Az árjegyzék névhez árat rendel. A kezdő kosar_osszege még minden tétel után csak 1-et ad hozzá: tehát most darabot számol, nem forintot. A blokkot_mutat egyelőre csak a termékneveket írja. Ebben a fájlban kizárólag rögzített kosár és számítás van, nincs input és fizetés.

### Rövid analóg minta

```python
meresek = [12, 8, 15]
osszeg = 0
for meres in meresek:
    osszeg += meres
print(osszeg)
```

### Most te alakítsd át

1. A kosar_osszege ciklusában az 1 helyett minden tételhez az arak paraméterből keresett árat add az összeghez. A függvény a teljes kosár összegét adja vissza; ne módosítsa a kosarat vagy az árjegyzéket.
2. A blokkot_mutat ciklusának kiírását egészítsd ki a termék egységárával és Ft-tal. A két kávé külön sor maradjon. A kosár hossza már megjelenik.
3. Ments és futtasd a B1.1 próbát. Ezután az adatokat módosítsd a többi próbához: áremelés, üres kosár, majd új termék. Az algoritmus maradjon változatlan.

### Kész, ha

- A kosár listáját járja be, nem az összes kínált terméket.
- Az árat a paraméter szótárból kéri, nincs beégetett árlánc vagy visszatérés az első körben.
- Ismétlődő termék minden alkalommal számít; üres kosárra 0.
- A blokk az adott árjegyzékből mutat árat; ebben a fájlban nincs fizetés.

### Próbák

### B1.1

Alapárjegyzék; kosar = ["kávé", "üdítő", "kávé"].

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Blokksorok: kávé 450 Ft; üdítő 390 Ft; kávé 450 Ft.
- Tételek száma: 3; rendelés: 1290 Ft.


### B1.2

Ugyanez a kosár; csak a kávé árát állítsd 500-ra.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- A két kávés sorban 500 Ft; rendelés: 1390 Ft.


### B1.3

kosar = []; bármelyik fenti árjegyzék.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Tételek száma: 0; rendelés: 0 Ft.


### B1.4

Kávé ismét 450; az árjegyzékbe vedd fel a "tea": 350 párt; kosar = ["tea", "kávé"].

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Két tétel; rendelés: 800 Ft.
- Az új termékhez nem kellett új elágazás a függvénybe.


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#lista-egyutt). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## S1 – Rövid összegzés

**Fájl:** nincs új fájl. **Időkeret:** 2 perc.

### A program célja

Röviden összekapcsolod a lista, a szótár és a függvény szerepét.

### Értsük meg a kezdőmintát

A kosár kiválasztja, mit számolunk; az árjegyzék megadja az árat. A számoló függvény visszaad, a blokkfüggvény megjelenít.

### Most te alakítsd át

1. A saját osszegzes.py alapján mutasd meg, melyik sor olvas a kosárból, és melyik kér le árat. Ez a már megírt kód rövid értelmezése, nem kimenetjóslás.
2. A tutor összefoglalja a ténylegesen kész részeket és az esetleges hiányzó próbát. Ezután a B2.a összekapcsolás következik, még az első blokk végén.

### Kész, ha

- Valós folytatási pont; részleges válasz esetén rövid pontosítás.

Kapcsolódó magyarázat: [EP_05.html](EP_05.html#osszegzes). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## B2 – A szótáras árjegyzék bekapcsolása a büfébe

**Fájl:** `bufe_05.py`. **Időkeret:** 17 perc.

### A program célja

A saját számoló és blokkfüggvényt összekapcsolod a korábbi, előkészített kosárbekéréssel és fizetéssel.

### Értsük meg a kezdőmintát

A fájl első része az EP_04-ből ismert kész segédkód: szövegegységesítés, kosárbekérés, igen/nem bekérés, kedvezmény és pénzpótlás. Ezeket most nem kell újragépelni. A kosarat_beker kinalat paraméteréhez szótárat is adhatunk: az in és a bejárás annak kulcsait használja. A főprogram végén az üres és nem üres ág készen van, de a kosár és összeg kezdőértékei még nem kapcsolódnak a saját függvényeidhez.

### Most te alakítsd át

1. B2.a: a jelölt helyre vidd át az osszegzes.py két saját függvénydefinícióját: kosar_osszege és blokkot_mutat. Mindkettő kapjon kosar és arak paramétert. Csak a definíciókat másold, az árjegyzéket és a régi főprogramot ne.
2. B2.a: a főprogram MODOSITSD 1 során az üres lista helyett hívd a kosarat_beker függvényt az arak szótárral. A HOZZAAD jelöléshez kerüljön a saját blokkfüggvényed hívása a kosárral és az árjegyzékkel.
3. B2.a: a nem üres ágban a MODOSITSD 2 során a 0 helyére a saját összegződ hívása kerüljön a két szükséges adattal. A kedvezmény- és fizetési részt hagyd meg. Ments, majd futtasd a B2.1 próbát.
4. B2.b: végezd el a pénzpótlás, az üres kosár és a visszavonás próbáját. A pénzt a program a terminálban kérdezi; inputra várás közben ne indíts új futást.
5. B2.b: végül ugyanebben az egy árjegyzékben módosítsd a kávét 500 Ft-ra és adj hozzá 350 Ft-os teát. A B2.5 próba igazolja, hogy a kínálat, a blokk és az összegzés is ebből dolgozik. A kész függvényekbe ne adj új termékenkénti elágazást.

**Belső szakaszok:** B2.a – saját definíciók és három kapcsolódás (9 perc); B2.b – működés, határesetek és adatmódosítás (8 perc).

### Kész, ha

- Az árjegyzék az egyetlen kézzel karbantartott kínálati és áradat a bufe_05.py-ban.
- Saját B1-függvényeket hív, mindkettőnek átadja az árjegyzéket.
- Az ürességet a kosár alapján ellenőrzi; üres kosárnál nincs diákkérdés vagy pénzkérdés.
- Ismeretlen és üres bevitel nem kerül a kosárba; a mégse biztonságosan visszavon.
- Az új ár és termék megjelenik a blokkban és a számításban. A pénzpótlás előtt nincs visszajárós sor.

### Próbák

### B2.1

A négy alapár szerepeljen; a kávé 450 Ft.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `" KÁVÉ "`
2. `"szendvics"`
3. `"kávé"`
4. `"üdítő"`
5. `"fizetek"`
6. `" IGEN "`
7. `"2000"`

Elvárt viselkedés:

- Rendelés: 2180 Ft
- Kedvezmény: 218 Ft
- Fizetendő: 1962 Ft
- Visszajáró: 38 Ft


### B2.2

Alapárjegyzék; hibás igen/nem után nem diák.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `"kávé"`
2. `"üdítő"`
3. `"fizetek"`
4. `"talán"`
5. `" NEM "`
6. `"800"`
7. `"40"`

Elvárt viselkedés:

- A talán után újra kérdez.
- Fizetendő: 840 Ft
- Még hiányzik: 40 Ft
- Csak a pótlás után: Visszajáró: 0 Ft.


### B2.3

Új futás, üres kosár.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `"mégse"`
2. `"fizetek"`

Elvárt viselkedés:

- Üres a kosár, nincs mit törölni.
- Tételek száma: 0; Nincs fizetendő tétel.
- Nincs diákság- és pénzbekérés.


### B2.4

Alapárjegyzék; érvénytelen bevitel és visszavonás.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `""` – csak Enter
2. `"pizza"`
3. `"kávé"`
4. `"croissant"`
5. `"mégse"`
6. `"ÜDÍTŐ"`
7. `"fizetek"`
8. `"nem"`
9. `"1000"`

Elvárt viselkedés:

- Az üres szövegre és pizzára figyelmeztetés.
- Törölve: croissant
- A végső kosár kávé és üdítő, két tétel.
- Fizetendő: 840 Ft; visszajáró: 160 Ft.


### B2.5

Csak a bufe_05.py egyetlen árjegyzékében: kávé 500, új tea 350. A többi ár változatlan.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `" TEA "`
2. `"kávé"`
3. `"fizetek"`
4. `"nem"`
5. `"1000"`

Elvárt viselkedés:

- A tea elfogadott termék.
- Blokk: tea 350 Ft, kávé 500 Ft.
- Fizetendő: 850 Ft; visszajáró: 150 Ft.


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#bufe-terv). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.


## Z1 – Önálló átalakítás: drága tételek száma

10 perc, `onallo.py`. A részletes követelmény és a négy próba: [zaro_feladatok.md](zaro_feladatok.md).

## Büfébővítések a gyorsan végzőknek

Z1 után, a tesztek előtt következhetnek a [bufe_bovitesek.md](bufe_bovitesek.md) feladatai:

- C1: termékenkénti darabszám, 10 perc.
- C2: összevont blokk, C1-re építve, 15 perc.
- C3: legnagyobb részösszeg, 10 perc.
- K5: új árjegyzék árkorrekcióval, 10 perc.

C1–C2 az elsőként választandó bővítés. A tesztek 25 percét tartsuk meg: a tanuló tényleges tempójától függ, mennyi bővítés fér bele. Teljes tervezett idő: alapút 90, C1–C2-vel 115, mind a négy új feladattal 135 perc. A félbemaradt rész folytatási pont, nem teljesített feladat. A teszteket a kiválasztott programozási részek után kezdjük.

## T1 – Elméleti teszt

10 perc, 10 rövid kérdés, 10 pont: [teszt_elmelet.md](teszt_elmelet.md).

## T2 – Kódismereti teszt

15 perc, 5 kimenetértelmezés és 5 hibakeresés, 10 pont: [teszt_kodismeret.md](teszt_kodismeret.md).
Előbb önálló válaszok, utána közös javítás. Mindkét teszt eredménye külön szerepel az értékelésben.

## S2 – Lezárás és folytatási pont

**Fájl:** nincs új fájl. **Időkeret:** 2 perc.

### A program célja

Összefoglalod, hogyan függ össze a kosár, az árjegyzék és a saját függvényed.

### Értsük meg a kezdőmintát

A feladatokban különböző eredmény készült: ár vagy None, módosítási sikerjelzés, új lista, pénzösszeg és darabszám. Ezeket az eredmények jelentése különbözteti meg.

### Most te alakítsd át

1. A saját kódodon mutasd meg röviden: hol keresel kulcs alapján, hol változtatsz adatot, és miért számít kétszer a kétszer vásárolt termék. Nem kell hosszú esszé.
2. A tutor közli a két teszt külön pontszámát, a támogatott vagy kihagyott válaszokat és egy-két gyakorlási célt. Ezután lezárja a mai gyakorlatot a ténylegesen kész és esetleg folytatásra váró részek megnevezésével.

### Kész, ha

- Nincs megalapozatlan teljesítésállítás; a segítség és a saját átalakítás megnevezése pontos.
- Az óra vége egyértelmű; nincs automatikusan indított kötelező pluszfeladat vagy házi feladat.

Kapcsolódó magyarázat: [EP_05.html](EP_05.html#osszegzes). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.
