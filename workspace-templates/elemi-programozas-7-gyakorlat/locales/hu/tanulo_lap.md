# EP_07 – Tuple, halmazok és tudatos függvényhasználat

Két 45 perces, magyar nyelvű programozási gyakorlat. Az EP_05 után a 6. alkalom ZH volt. A mai feladatok az EP_07.html fogalmait a büfé új adatfeldolgozó feladataihoz alkalmazzák. A könyvtári minták módszere átvihető; a saját megoldást a rendelési adatokhoz te készíted el.

A tutor bemutatja a program egészét és a rövid mintát. Te szerkesztesz, mentesz és a Futtatás gombbal futtatsz. A feladatokban nincs előzetes kimenetjóslás; a záró kódismereti teszt külön szakasz.

A kezdőprogramok futnak, de nem teljesítik a célkövetelményt. A helykitöltő eredmény vagy az eredetit módosító kezdőfüggvény tudatos kiindulás. Attól, hogy nem kapsz hibaüzenetet, még szükséges az átalakítás és a próbák elvégzése.

Minden .py a munkatér gyökerében van; a Futtatás gomb terminálja a megnyitott fájl mappájában álljon. A feladatok között nincs mappaváltás. A próbaadatokat a kódban változtatod, nem terminál-inputra válaszolsz. Mentés → Futtatás → eredmény összehasonlítása.

## Időterv

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| Bemutatkozás és érdemi kezdés | 2 | B1.b – Halmaz módosítása | 6 |
| A1 – Rendelési tételek tuple-ben | 8 | Z1 – Önálló rendelésellenőrzés | 12 |
| A2 – Kosárstatisztika | 10 | T1 – Elméleti teszt | 10 |
| A3 – Kosarak összehasonlítása | 15 | T2 – Kódismereti teszt | 15 |
| B1.a – Új kosár, eredeti megőrzése | 8 | S2 – Értékelés és lezárás | 2 |
| S1 – Rövid összegzés | 2 |  |  |
| **Összesen** | **45** | **Összesen** | **45** |

A szünet külön idő. Ez tömörített terv: a magyarázat, a szerkesztés és a próbák ideje is beletartozik. Lassabb haladásnál a tutor pontos folytatási pontot ad. A félbemaradt részt nem nevezzük késznek. A C1 csak tényleges időnyereség esetén választható; a két teszt és a lezárás 27 percét fenntartjuk.

## A1 – Rendelési tételek tuple-ben

**Fájl:** `tetelek.py`. **Tervezett idő:** 8 perc.

### Mit csinál majd a program?

A tétellista minden adat-hármasából terméknevet, darabszámot és egységárat kapsz, majd tételsoronként részösszeget számolsz.

### Mi van előkészítve?

Adott a tétellista és a fejléc. Egy tuple pontosan három mezőt tartalmaz ebben a sorrendben: terméknév, darabszám, egységár. A kezdőprogram csak egyben írja ki a listát. Darabszám pozitív egész, egységár nemnegatív egész; típusellenőrzés nem feladat.

### Rövid analóg minta

```python
konyvek = [("K104", "Python alapok")]
for azonosito, cim in konyvek:
    print(f"{azonosito}: {cim}")
```

A rövid mintában egy listaelem egy könyv két mezője; a ciklus ezeket kicsomagolja. A saját tételben három mező van, és két számból részösszeget is számolsz. A mezők pozícióját a jelentésükkel együtt figyeld.

### Most te alakítsd át

1. A lista egyben történő kiírását cseréld saját bejárásra. Az aktuális tuple három mezőjét beszédes nevekhez csomagold ki.
2. Számítsd ki az adott tétel darabszámának és egységárának szorzatát. A sor tartalmazza a nevet, a darabszámot, az egységárat és a részösszeget.
3. Ne írd át a tuple-öket vagy a listát. Ments, futtass, majd az adatok módosításával végezd el a próbákat.

### Kész, ha

- Minden tétel külön sorban szerepel, a három mező jelentése helyes.
- A részösszeg az aktuális adatokból származik, nem beírt állandó.
- Üres listánál nincs tételsor; a bemenet nem módosul.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | Az előkészített két tétel. | Kávé: 2 db × 450 Ft = 900 Ft; szendvics: 1 db × 890 Ft = 890 Ft. Mindkét tétel külön sor. |
| A1.2 | Csak a kávé tételét állítsd erre: ("kávé", 3, 500). | Kávé részösszege 1500 Ft; szendvicsé továbbra is 890 Ft. A feldolgozó kód nem változik. |
| A1.3 | tetelek = []. | A fejléc megjelenhet; tételsor nincs, és nincs hiba. |
| A1.4 | tetelek = [("víz", 2, 0)]. | Egy sor: 2 db, 0 Ft egységár, 0 Ft részösszeg. A nulla ár itt érvényes próbaadat. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#kicsomagolas).
## A2 – Mit mond el a kosár?

**Fájl:** `kosar_adatok.py`. **Tervezett idő:** 10 perc.

### Mit csinál majd a program?

Egy függvény visszaadja az összes tétel számát, a különböző termékfajták számát és egy keresett termék darabszámát, ebben a sorrendben.

### Mi van előkészítve?

A kosar_adatai paraméterei és az induló próbaadatok adottak. A visszatérés még (0, 0, 0), ezért nem valódi számítás. A főprogram egyelőre csak egyben mutatja ezt a tuple-t. A terméknevek már egységesített szövegek.

### Rövid analóg minta

```python
belepesek = ["O17", "O42", "O17"]
print(len(belepesek))
print(len(set(belepesek)))
print(belepesek.count("O42"))
```

A len az összes eseményt számolja. A set egyedi azonosítókat készít, ennek hossza más kérdésre felel. A lista count metódusa egy megadott érték előfordulásait adja; nem a teljes lista hossza és nem halmazművelet.

### Most te alakítsd át

1. A függvényben a paraméterekből számítsd ki a három különböző darabszámot. A kereséshez a keresett_termek paramétert használd.
2. A három eredményt a megadott sorrendben, egy tuple-ben add vissza. A függvény ne írjon ki, és ne módosítsa a kosarat.
3. A főprogramban csomagold ki a visszakapott tuple-t három beszédes névhez. Írasd ki mindhárom adatot a jelentését mutató felirattal, majd végezd el a próbákat.

### Kész, ha

- A visszatérési érték három egész számot tartalmazó tuple, a rögzített sorrendben.
- Külön kezeli az összes darabot, a termékfajtákat és a keresett terméket.
- Az eredeti kosár megőrzi sorrendjét és ismétlődéseit. A hívó jelenít meg.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | Az előkészített ötelemű kosár; keresett_termek = "kávé". | A visszakapott tuple (5, 3, 3). A főprogram a három értéket jelentésének megfelelő felirattal mutatja. |
| A2.2 | Ugyanez a kosár; keresett_termek = "tea". | (5, 3, 0). Hiányzó termékből nulla van. |
| A2.3 | kosar = []; keresett_termek = "kávé". | (0, 0, 0), hiba nélkül. |
| A2.4 | kosar = ["tea", "tea", "tea"]; keresett_termek = "tea". | (3, 1, 3). Az eredeti kosár minden próbában változatlan. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#valasztas).
## A3 – Két kosár termékfajtáinak összehasonlítása

**Fájl:** `kosarak.py`. **Tervezett idő:** 15 perc.

### Mit csinál majd a program?

Két kosárlistából halmazalapú összehasonlítást készítesz. A kimutatás öt halmazt és egy logikai értéket ad vissza az előkészített eredményszótárban.

### Mi van előkészítve?

A függvény paraméterei, a szótár kulcsai és az eredmények megjelenítése adott. Az üres halmazok és a False egyelőre helykitöltők. Egy kosárban ugyanaz a termék többször szerepelhet; itt csak a termékfajtákat hasonlítjuk össze.

### Rövid analóg minta

```python
hetfo = {"O17", "O42"}
kedd = {"O42", "O58"}
print(sorted(hetfo & kedd))
print(hetfo <= kedd)
```

A metszet új halmazt ad. A részhalmazvizsgálat logikai értéket ad: minden bal oldali elem szerepel-e a jobb oldalon? Az eredmény típusát is figyeld. A darabszámok összehasonlítása ettől külön feladat lenne.

### Most te alakítsd át

1. A3.a: készíts a két listából két helyi halmazt. Az osszes és kozos kulcsok értékét alakítsd valódi unióvá és metszetté. Ellenőrizd ezeket az A3.1 adataival; a többi helykitöltő még nem kész eredmény.
2. A3.b: készítsd el a két irányú különbséget és a szimmetrikus különbséget. A csak_egyik pontosan az egyik kosárban szereplő termékfajtákat jelentse. Az A3.1 öt halmazeredményét vizsgáld.
3. A3.c: készítsd el az elso_reszhalmaz logikai értékét. Ezután a teljes eredményre végezd el az A3.1–A3.5 próbát; az A3.1 korábban már ismert halmazeredményeit ne kelljen újra bizonyítanod, ha a kódjuk nem változott.
4. A függvény csak eredményt adjon vissza, a két bemeneti listát és az eredeti ismétlődéseket hagyja változatlanul. A rendezett kiírás a főprogramban már adott.

### Kész, ha

- Az első öt eredmény set; az elso_reszhalmaz bool.
- A különbség irányai és a szimmetrikus különbség jelentése helyes.
- Azonos termékfajták eltérő darabszámmal is részhalmazviszonyt adhatnak.
- Az üres bal oldali halmaz részhalmaz; minden kötelező próba ismert, a bemenetek változatlanok.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.1 | első: ["kávé", "üdítő", "kávé"]; második: ["üdítő", "szendvics"]. | Összes: {kávé, szendvics, üdítő}; közös: {üdítő}; csak első: {kávé}; csak második: {szendvics}; pontosan egyik: {kávé, szendvics}; részhalmaz: False. |
| A3.2 | első: ["kávé", "kávé"]; második: ["kávé"]. | Összes és közös: {kávé}; mindkét irányú és szimmetrikus különbség üres; részhalmaz: True. Darabszámot itt nem ellenőrzünk. |
| A3.3 | első: []; második: ["tea"]. | Összes: {tea}; közös és csak első üres; csak második és pontosan egyik: {tea}; részhalmaz: True. |
| A3.4 | első: ["tea"]; második: []. | Összes, csak első és pontosan egyik: {tea}; közös és csak második üres; részhalmaz: False. |
| A3.5 | Mindkét kosár üres. | Mind az öt halmazeredmény üres; részhalmaz: True. A bemeneti listák mindegyik próbában változatlanok. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#halmazmuveletek).
## B1.a – Új kosár az eredeti megőrzésével

**Fájl:** `modositas.py`. **Tervezett idő:** 8 perc.

### Mit csinál majd a program?

A bovitett_kosarat_keszit új, egy termékkel bővített listát adjon vissza, miközben a hívó eredeti kosara változatlan.

### Mi van előkészítve?

A kezdő függvény az append miatt még az eredeti kosarat bővíti, és ugyanazt a listát adja vissza. A főprogram megmutatja a hívás előtti és utáni állapotot, valamint az is összehasonlítást. A B1.b függvénye még szándékosan helykitöltő; most nem azt javítjuk.

### Rövid analóg minta

```python
eredeti = {"O17": 2}
terv = eredeti.copy()
terv["O17"] = 3
print(eredeti)
print(terv)
```

A másolat külön szótár; ebben a mintában egész értékeket tartalmaz. Listának is van copy metódusa. A paraméterhez kötött objektum automatikusan nem másolódik: a saját feladatban tudatosan kell külön listát készítened a bővítéshez.

### Most te alakítsd át

1. Alakítsd át a függvényt úgy, hogy a kapott lista alapján új listát készítsen. Az új terméket ezen az új listán helyezd el.
2. Az új listát add vissza. A paraméterként kapott eredeti listát ne módosítsd, és a sorrendet, ismétlődéseket őrizd meg.
3. Ments, futtass, majd a hívás előtti, hívás utáni és visszakapott adatokkal ellenőrizd a B1.a próbákat. A B1.b kimenetét most még ne minősítsd kész feladatnak.

### Kész, ha

- Új lista tér vissza; az eredeti tartalma és objektuma megmarad.
- Az új termék az új lista végére kerül; az ismétlődés megengedett.
- Az is összehasonlítás False; minden előírt próba ismert.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.a.1 | kosar = ["kávé", "üdítő"]; uj_termek = "tea". | Az eredeti ["kávé", "üdítő"]; az új ["kávé", "üdítő", "tea"]. Az is összehasonlítás False. |
| B1.a.2 | kosar = []; uj_termek = "tea". | Az eredeti []; az új ["tea"]. Két külön lista. |
| B1.a.3 | kosar = ["kávé", "kávé"]; uj_termek = "kávé". | Az eredetiben két, az újban három kávé. A sorrend és az ismétlődés megmarad. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#modositas).

## S1 – Rövid összegzés és folytatási pont

2 perc, új fájl nélkül. A saját kódod alapján mondd el röviden: melyik adatnál számít az ismétlődés, mikor kapsz halmazt, és a B1.a után melyik lista változott. A következő rész a B1.b; ne állítsd vissza a már megírt fájlt.

## B1.b – Törzsvásárló szándékos felvétele

**Fájl:** `modositas.py`. **Tervezett idő:** 6 perc.

### Mit csinál majd a program?

A torzsvevot_felvesz a kapott halmazt szándékosan módosítsa új névnél. Adjon True-t új név, False-t már meglévő név esetén.

### Mi van előkészítve?

A második függvény most mindig False-t ad, és nem módosít. A nevek már egységesített, nem üres szövegek; nincs külön input vagy névtisztítási feladat. Az első függvény korábban elkészített változata maradjon meg.

### Rövid analóg minta

```python
konyvazonositok = {"K104"}
konyvazonositok.add("K207")
konyvazonositok.add("K207")
print(len(konyvazonositok))
```

Az add a meglévő halmazt módosítja, és az ismételt elem nem növeli az elemszámot. A te függvényednek emellett azt is jeleznie kell, hogy most került-e be új név, ezért a hívás előtti jelenlét is számít.

### Most te alakítsd át

1. Vizsgáld meg a név jelenlétét a kapott halmazban. A meglévő névhez False tartozzon, változtatás nélkül.
2. Új névnél bővítsd a kapott halmazt, és adj vissza True-t. A függvény mindkét esetben logikai értéket adjon, ne printtel jelezzen.
3. Az első próbát futtasd az adott adatokkal. Az ismételt név próbájához ugyanazzal a halmazzal, egy futáson belül írj második hívást; az újraindítás újra létrehozná a kezdeti halmazt. Üres halmazzal is ellenőrizd.

### Kész, ha

- Új névnél a hívó halmaza bővül és True tér vissza.
- Meglévő névnél semmilyen név nem vész el, az elemszám nem nő és False tér vissza.
- A működés megkülönböztethető a B1.a új listát készítő működésétől.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.b.1 | Új futás: {"anna", "bela"}, név: "csilla". | True; a halmazban anna, bela és csilla. A kapott halmaz helyben módosul. |
| B1.b.2 | Ugyanazon halmazzal, újraindítás nélkül hívd még egyszer ugyanazzal a csilla névvel. | False; továbbra is három név. A meglévő bejegyzések megmaradnak. |
| B1.b.3 | Üres halmaz, név: "anna". | True; a halmaz egyetlen eleme anna. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#halmaz-modositas).
## Z1 – Teljesíthető-e a rendelés?

**Fájl:** `onallo.py`. **Tervezett idő:** 12 perc.

### Mit csinál majd a program?

A kosárlistából és az árjegyzékszótárból új halmazban visszaadod a hiányzó termékfajtákat. A hívó a hiány alapján érthető üzenetet jelenít meg.

### Mi van előkészítve?

A függvény jelenlegi üres halmaza csak helykitöltő. A próbaadatok és a visszatérés tárolása adott. A terméknevek már egységesítettek. Az árjegyzékben a kulcsok a terméknevek; itt elérhetőséget, nem készletdarabszámot vizsgálunk.

Első próbálkozáskor a követelményt és a teszteket kapod, kész algoritmust nem. A korábbi feladatokban már használtál egyedivé alakítást, csoportkülönbséget és függvényes visszatérést.

### Most te alakítsd át

1. Alakítsd át a hianyzo_termekek függvényt úgy, hogy a paraméterként kapott adatokból új halmazban adja vissza az árjegyzékben nem szereplő termékfajtákat. Ismételt hiányzó termék egyszer legyen benne.
2. A főprogram nyers eredménykiírását alakítsd érthető döntéssé. Ha nincs hiányzó elem, jelezze, hogy teljesíthető; egyébként mutassa meg a hiányzó termékeket rendezett megjelenítéssel.
3. A függvény ne kérdezzen, ne írjon ki, és ne módosítsa a kosarat vagy az árjegyzéket. Üres kosárból üres hiányzó halmaz készüljön.
4. Végezd el a Z1.1–Z1.5 próbákat. A kódot általánosítsd: az újonnan kínálatba vett tea miatt csak az adatot kelljen megváltoztatnod.

### Kész, ha

- Új set az eredmény, a hiányzó termékfajták helyesek és egyediek.
- A függvény paraméterekből dolgozik, nem globális kosárból/árjegyzékből.
- A két bemenet változatlan; a döntés és megjelenítés a hívóban van.
- Az összes előírt próba eredménye ismert; az üres eredmény nem None.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | Alapárjegyzék; kosár: ["kávé", "üdítő"]. | Üres halmaz; a hívó jelzi, hogy a rendelés teljesíthető. |
| Z1.2 | Alapárjegyzék; kosár: ["kávé", "tea"]. | A hiányzó halmaz egyetlen eleme tea; a hívó a hiányt és a termék nevét mutatja. |
| Z1.3 | Alapárjegyzék; kosár: ["tea", "tea", "pizza"]. | A hiányzó halmaz elemei tea és pizza, mindkettő egyszer. |
| Z1.4 | Alapárjegyzék; üres kosár. | Üres halmaz, hiba nélkül. A program szabálya szerint teljesíthető: nincs hiányzó termék. |
| Z1.5 | A Z1.2 adataihoz futás előtt vedd fel a "tea": 350 bejegyzést az árjegyzékbe. | Üres hiányzó halmaz, teljesíthető rendelés. Csak a próbaadat változik, a függvény nem. A függvény mindegyik próbában változatlanul hagyja a bemeneteket. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#atvitel).

## C1 – Választható összetett riport

Csak ténylegesen fennmaradó idő esetén, a két teszt előtt. Részletes leírás: [bovites.md](bovites.md). Nem automatikus házi feladat.

## T1 és T2 – Záró tesztek

T1: 10 rövid elméleti kérdés, 10 perc. T2: 5 kódértelmezési és 5 hibakeresési kérdés, 15 perc. A tutor ötös csoportokban adja őket; kérésre egyesével is haladhattok. Az első válaszadáskor ne nyisd meg a megoldókulcsot és ne futtasd a tesztkódokat. A két rész végén közösen értékeltek, és a javításhoz már futtathatsz.

## S2 – Az óra lezárása

2 perc. A tutor külön összegzi a programozási munka állapotát és a teszt eredményét. Megnevezi az esetleges hiányzó próbát vagy következő lépést. Az óra vége egyértelmű; új feladat nem indul automatikusan.
