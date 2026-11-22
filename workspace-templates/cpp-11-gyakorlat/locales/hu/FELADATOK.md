# C++ 07–10 – rövid InnoAgent-gyakorlatok

24 önálló kódolási feladat, mindegyik után 1–2, a saját kódra vonatkozó elméleti kérdés. Négy blokk, blokkonként 6 feladat. A 47 elméleti kérdés a kódolás utáni megbeszélés része.

## Tartalom

- [G07_01 – Termékadatok](#g07_01)
- [G07_02 – Másolat módosítása](#g07_02)
- [G07_03 – Kikapcsolás mutatóval](#g07_03)
- [G07_04 – Kölcsönözhető könyvek](#g07_04)
- [G07_05 – Hatókörhiba](#g07_05)
- [G07_06 – Az aktív union-tag](#g07_06)
- [G08_01 – Üres-e a két készlet?](#g08_01)
- [G08_02 – Hozzáférési hiba javítása](#g08_02)
- [G08_03 – Érvényes foglalás](#g08_03)
- [G08_04 – Lekérdezés const objektumon](#g08_04)
- [G08_05 – Két persely további befizetései](#g08_05)
- [G08_06 – Küszöböt elérő eredmények](#g08_06)
- [G09_01 – Kétféle téglalap-létrehozás](#g09_01)
- [G09_02 – Töltöttség korlátozása](#g09_02)
- [G09_03 – Objektumtömb inicializálása](#g09_03)
- [G09_04 – Inicializáló listára átírás](#g09_04)
- [G09_05 – Utolsó könyv kivétele](#g09_05)
- [G09_06 – Hívás az adott mutatón keresztül](#g09_06)
- [G10_01 – Rövid számlista mentése](#g10_01)
- [G10_02 – Hozzáfűzés két futtatásban](#g10_02)
- [G10_03 – Negatív értékek számlálása](#g10_03)
- [G10_04 – Fájl végi többletszámlálás](#g10_04)
- [G10_05 – Két egész mező szigorú ellenőrzése](#g10_05)
- [G10_06 – Betöltés a régi adatok megőrzésével](#g10_06)

<a id="g07_01"></a>

## G07_01 – Termékadatok

**Fájl:** `g07_01.cpp` · Kiegészítendő kód

**Cél:** Struktúramezők beolvasása és használata egy számításban.

A két TODO helyén olvasd be a darabszámot és egységárat a Termek objektum mezőibe, majd írd ki a darabszám és egységár szorzatát. A darabszám 0…20 közötti egész, az egységár 0…100 közötti véges valós szám. A kimenet egy szám, két tizedesjeggyel, felirat nélkül. A megadott formázást tartsd meg.

### Ellenőrző próbák

**1. Szokásos vásárlás**


Bemenet:

```text
3 2.50
```

Elvárt kimenet:

```text
7.50
```

**2. Nulla darab**


Bemenet:

```text
0 8.25
```

Elvárt kimenet:

```text
0.00
```

**3. Felső határ**


Bemenet:

```text
20 100
```

Elvárt kimenet:

```text
2000.00
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért lehet eltérő típusú a két mező ebben a struktúrában?
2. Melyik kifejezés éri el a te programodban az objektum egységárát?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g07_02"></a>

## G07_02 – Másolat módosítása

**Fájl:** `g07_02.cpp` · Kiegészítendő kód

**Cél:** Másoló inicializálás és önálló objektumállapot követése.

Az első TODO-s sort alakítsd másoló inicializálássá: a masolat az eredeti alapján jöjjön létre. A második TODO helyén csak a masolat darab mezőjét állítsd a beolvasott uj értékre. A bemenet két 0…20 közötti egész. A kiíró sort tartsd meg.

### Ellenőrző próbák

**1. Eltérő új érték**


Bemenet:

```text
5 2
```

Elvárt kimenet:

```text
5 2
```

**2. Nullás másolat**


Bemenet:

```text
9 0
```

Elvárt kimenet:

```text
9 0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért maradt meg az eredeti darabszáma?
2. Mi a különbség a másolat létrehozása és a későbbi mezőértékadás között?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g07_03"></a>

## G07_03 – Kikapcsolás mutatóval

**Fájl:** `g07_03.cpp` · Kiegészítendő kód

**Cél:** Egy mező célzott módosítása érvényes mutatón keresztül.

Írd meg a kikapcsol függvény törzsét. Érvényes mutatónál az aktiv mezőt false-ra állítsa, az azonosítót hagyja meg; nullptr esetén ne tegyen semmit. A függvény nem ír ki. A bemenet egy 0…99 közötti azonosító és egy 0/1 jelző. A main a nullmutatós hívást is kipróbálja.

### Ellenőrző próbák

**1. Aktív eszköz**


Bemenet:

```text
12 1
```

Elvárt kimenet:

```text
12 0
```

**2. Már inaktív**


Bemenet:

```text
3 0
```

Elvárt kimenet:

```text
3 0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Mit rövidít a p->aktiv kifejezés?
2. Miért kell a nullmutatót a mezőelérés előtt kizárni?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g07_04"></a>

## G07_04 – Kölcsönözhető könyvek

**Fájl:** `g07_04.cpp` · Kiegészítendő kód

**Cél:** Feltételes számlálás struktúratömbben.

Egészítsd ki a szamol függvényt: az első n könyv közül hány kölcsönözhető? Ne az oldalszámokat add össze. 0 ≤ n ≤ 5; ezután n darab oldalszám–jelző pár következik (oldalszám: 1…1000, jelző: 0 vagy 1). A tömböt ne módosítsd. Üres tartomány eredménye 0.

### Ellenőrző próbák

**1. Vegyes lista**


Bemenet:

```text
3
120 1
80 0
250 1
```

Elvárt kimenet:

```text
2
```

**2. Üres lista**


Bemenet:

```text
0
```

Elvárt kimenet:

```text
0
```

**3. Egyik sem kölcsönözhető**


Bemenet:

```text
2
20 0
30 0
```

Elvárt kimenet:

```text
0
```

**4. Mindenki kölcsönözhető**


Bemenet:

```text
2
20 1
30 1
```

Elvárt kimenet:

```text
2
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért az n értékéig, és nem mindig az öt férőhelyig járunk?
2. Milyen bemenet mutatná ki, ha a feltétel nélkül minden könyvet megszámolnánk?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g07_05"></a>

## G07_05 – Hatókörhiba

**Fájl:** `g07_05.cpp` · Szándékos fordítási hiba

**Cél:** Lokális nevek láthatóságának javítása és névelrejtés követése.

A kezdőkód szándékosan nem fordul le. A szorzás maradjon a belső blokkban, az eredmény kiírása azon kívül. Úgy helyezd el az eredmeny deklarációját és értékadását, hogy a program kiírja a beolvasott szám háromszorosát, majd 9-et, végül az eredeti számot. A bemenet −20…20 közötti egész. A második belső blokkot tartsd meg.

### Ellenőrző próbák

**1. Pozitív szám**


Bemenet:

```text
4
```

Elvárt kimenet:

```text
12
9
4
```

**2. Negatív szám**


Bemenet:

```text
-2
```

Elvárt kimenet:

```text
-6
9
-2
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért nem volt látható az eredmeny az eredeti kiírásnál?
2. Mi változna, ha a második blokkban az int szam = 9; helyett szam = 9; lenne?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g07_06"></a>

## G07_06 – Az aktív union-tag

**Fájl:** `g07_06.cpp` · Kiegészítendő kód

**Cél:** Jelző alapján biztonságos mezőelérés és a memóriaelrendezés megfigyelése.

A bemenet I és egy egész, vagy D és egy véges valós szám. A kész kód a megfelelő union-tagba olvas. A TODO helyén csak ezt az aktív tagot írd ki egy sorban. Az adott sizeof-sort hagyd meg. Előbb válaszd ki a megfelelő mezőt, csak utána futtass; inaktív mezőt ne olvass. A méretek környezetfüggők, nincs kötelező számszerű bájtméret.

### Ellenőrző próbák

**1. Egész tag**


Bemenet:

```text
I 7
```

Az első kimeneti sor: `7`.

A második sor négy bájtméret: `sizeof(KetSzam) sizeof(Szam) sizeof(int) sizeof(double)`. Konkrét számot nem kell megjegyezni. A struktúra legalább a két adattag méretének összegét, az unió legalább a nagyobb adattag méretét foglalja; kitöltés növelheti a méretet.

**2. Valós tag**


Bemenet:

```text
D 2.5
```

Az első kimeneti sor: `2.5`.

A második sor négy bájtméret: `sizeof(KetSzam) sizeof(Szam) sizeof(int) sizeof(double)`. Konkrét számot nem kell megjegyezni. A struktúra legalább a két adattag méretének összegét, az unió legalább a nagyobb adattag méretét foglalja; kitöltés növelheti a méretet.

### Elméleti kérdések – a kód ellenőrzése után

1. Miért a tipus jelző szerinti mezőt olvassuk?
2. Miért lehet a struktúra mérete nagyobb a két mezőméret összegénél?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_01"></a>

## G08_01 – Üres-e a két készlet?

**Fájl:** `g08_01.cpp` · Kiegészítendő kód

**Cél:** Nyilvános logikai lekérdező és példányonkénti állapot.

Az ures tagfüggvény true-t adjon, ha a saját objektum darabszáma 0; egyébként false-t. Csak a TODO-s visszatérési kifejezést javítsd. A bemenet két 0…100 közötti egész; a kimenet a két készlet ürességjelzője (0/1), szóközzel elválasztva.

### Ellenőrző próbák

**1. Két nem üres készlet**


Bemenet:

```text
4 9
```

Elvárt kimenet:

```text
0 0
```

**2. Az első üres**


Bemenet:

```text
0 100
```

Elvárt kimenet:

```text
1 0
```

**3. A második üres**


Bemenet:

```text
100 0
```

Elvárt kimenet:

```text
0 1
```

### Elméleti kérdések – a kód ellenőrzése után

1. Mi az osztály, és melyik két objektum jön létre ebben a mainben?
2. Miért nem írja felül a második beállítás az első objektum állapotát?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_02"></a>

## G08_02 – Hozzáférési hiba javítása

**Fájl:** `g08_02.cpp` · Szándékos fordítási hiba

**Cél:** Fordítási hiba felismerése és publikus felület használata.

A kezdőkód szándékosan nem fordul. Javítsd a main kiíró sorát a meglévő lekérdező használatával. Az adatmezőt hagyd privátnak. A bemenet egy −10…10 közötti egész; ezt az értéket kell kiírni.

**Kódellenőrzés:** A mező privát maradt, a main a nyilvános lekérdezőt hívja.

### Ellenőrző próbák

**1. Pozitív**


Bemenet:

```text
6
```

Elvárt kimenet:

```text
6
```

**2. Negatív**


Bemenet:

```text
-3
```

Elvárt kimenet:

```text
-3
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért volt hibás a közvetlen mezőelérés a mainből?
2. Mi az alapértelmezett hozzáférés class és struct esetén?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_03"></a>

## G08_03 – Érvényes foglalás

**Fájl:** `g08_03.cpp` · Kiegészítendő kód

**Cél:** Állapotváltozás feltétellel, hibánál változatlan állapot.

Írd meg a lefoglal függvényt. Pozitív, a megmaradt készletnél nem nagyobb kérésnél csökkentse a készletet és adjon true-t; egyébként false-t adjon változtatás nélkül. A készlet kezdetben 20. Két egymást követő, −5…25 közötti kérés érkezik. Mindkét sorban a sikerjelző (0/1) és a megmaradt darabszám jelenjen meg.

### Ellenőrző próbák

**1. Két siker**


Bemenet:

```text
3 5
```

Elvárt kimenet:

```text
1 17
1 12
```

**2. Nulla majd siker**


Bemenet:

```text
0 1
```

Elvárt kimenet:

```text
0 20
1 19
```

**3. Két elutasítás**


Bemenet:

```text
-2 21
```

Elvárt kimenet:

```text
0 20
0 20
```

**4. Teljes készlet**


Bemenet:

```text
20 1
```

Elvárt kimenet:

```text
1 0
0 0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért a jelenlegi készlethez kell hasonlítani a második kérést?
2. Melyik teszt bizonyítja, hogy az elutasított kérés nem módosított állapotot?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_04"></a>

## G08_04 – Lekérdezés const objektumon

**Fájl:** `g08_04.cpp` · Szándékos fordítási hiba

**Cél:** Consthelyesség egy számító lekérdezőben.

A kód szándékosan nem fordul. A szabadHely tagfüggvény deklarációját egészítsd ki, hogy const objektumon is hívható legyen. A mainben a const maradjon meg. Bemenet: kapacitás és foglaltság, 0 ≤ foglaltság ≤ kapacitás ≤ 100. Kimenet: a szabad helyek száma.

**Kódellenőrzés:** A lekérdező const, és a main const objektuma megmaradt.

### Ellenőrző próbák

**1. Részben foglalt**


Bemenet:

```text
12 5
```

Elvárt kimenet:

```text
7
```

**2. Nullás kapacitás**


Bemenet:

```text
0 0
```

Elvárt kimenet:

```text
0
```

**3. Tele**


Bemenet:

```text
10 10
```

Elvárt kimenet:

```text
0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Mit vállal a tagfüggvény neve és paraméterlistája utáni const?
2. Végezhet-e kivonást egy const lekérdező? Miért?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_05"></a>

## G08_05 – Két persely további befizetései

**Fájl:** `g08_05.cpp` · Kiegészítendő kód

**Cél:** Másolatok önálló módosítása tagfüggvényekkel.

A másolás után fizess be y összeget az első és z összeget a második perselybe. A másolás helyét és a kiírást tartsd meg. A bemenet x, y, z: három 0…100 közötti egész. A kimenet az első és a második egyenleg.

### Ellenőrző próbák

**1. Eltérő befizetések**


Bemenet:

```text
10 2 7
```

Elvárt kimenet:

```text
12 17
```

**2. Nullás indulás**


Bemenet:

```text
0 5 0
```

Elvárt kimenet:

```text
5 0
```

**3. Határértékek**


Bemenet:

```text
100 100 100
```

Elvárt kimenet:

```text
200 200
```

### Elméleti kérdések – a kód ellenőrzése után

1. Melyik objektumot módosítja az elso.befizet(y) hívás?
2. Miért tartalmazza a második persely az x értéket is?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g08_06"></a>

## G08_06 – Küszöböt elérő eredmények

**Fájl:** `g08_06.cpp` · Kiegészítendő kód

**Cél:** Objektumtömb bejárása publikus lekérdezővel.

Az elerte függvény számolja meg az első n objektum közül azokat, amelyek pontszáma legalább kuszob. Az üres tömb eredménye 0. A privát mezőkhöz ne nyúlj; a gettert használd. Bemenet: n (0…5), küszöb, majd n pontszám; minden pontszám és a küszöb −100…100 közötti egész.

### Ellenőrző próbák

**1. Vegyes**


Bemenet:

```text
4 10
9 10 15 -2
```

Elvárt kimenet:

```text
2
```

**2. Üres**


Bemenet:

```text
0 5
```

Elvárt kimenet:

```text
0
```

**3. Pontosan a küszöb**


Bemenet:

```text
1 10
10
```

Elvárt kimenet:

```text
1
```

**4. Egyik sem**


Bemenet:

```text
2 10
1 9
```

Elvárt kimenet:

```text
0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért hívható a lekérdező a const tömb elemein?
2. Melyik teszt különbözteti meg a > és a >= feltételt?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_01"></a>

## G09_01 – Kétféle téglalap-létrehozás

**Fájl:** `g09_01.cpp` · Kiegészítendő kód

**Cél:** Alapértelmezett és paraméteres konstruktor.

Javítsd a két konstruktor inicializáló listáját. Paraméter nélkül 1×1-es, két paraméterrel a×b méretű téglalap jöjjön létre. Bemenet: két 1…20 közötti egész. Kimenet: az alapértelmezett és a paraméteres téglalap területe.

### Ellenőrző próbák

**1. Eltérő oldalak**


Bemenet:

```text
3 7
```

Elvárt kimenet:

```text
1 21
```

**2. Egységnégyzet**


Bemenet:

```text
1 1
```

Elvárt kimenet:

```text
1 1
```

**3. Felső határ**


Bemenet:

```text
20 20
```

Elvárt kimenet:

```text
1 400
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért nincs a két konstruktor neve előtt visszatérési típus?
2. Mi alapján választódik ki a két konstruktor közül az egyik?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_02"></a>

## G09_02 – Töltöttség korlátozása

**Fájl:** `g09_02.cpp` · Kiegészítendő kód

**Cél:** Érvényes kezdőállapot és kétoldali határkezelés.

A konstruktor a beolvasott egész töltöttséget korlátozza a 0…100 tartományra: a negatívból 0, a 100-nál nagyobból 100, az érvényesből önmaga legyen. Bemenet: egy −200…200 közötti egész; kimenet: a tárolt érték.

### Ellenőrző próbák

**1. Alsó határ alatt**


Bemenet:

```text
-1
```

Elvárt kimenet:

```text
0
```

**2. Alsó határ**


Bemenet:

```text
0
```

Elvárt kimenet:

```text
0
```

**3. Belső érték**


Bemenet:

```text
38
```

Elvárt kimenet:

```text
38
```

**4. Felső határ**


Bemenet:

```text
100
```

Elvárt kimenet:

```text
100
```

**5. Felső határ felett**


Bemenet:

```text
102
```

Elvárt kimenet:

```text
100
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miben különbözik ez a korlátozás egy kérés elutasításától?
2. Miért külön teszt a 0 és a −1?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_03"></a>

## G09_03 – Objektumtömb inicializálása

**Fájl:** `g09_03.cpp` · Szándékos fordítási hiba

**Cél:** Tömbelemek létrehozása paraméteres konstruktorral.

A kezdőkód szándékosan nem fordul. A szobak tömb két elemét a deklarációban inicializáld a és b alapján. Az osztályt ne módosítsd. Bemenet: két 1…4 közötti egész; kimenet: a két szoba ágyszáma.

**Kódellenőrzés:** Mindkét tömbelem a deklarációban paraméteresen inicializált; az osztály változatlan.

### Ellenőrző próbák

**1. Eltérő szobák**


Bemenet:

```text
1 4
```

Elvárt kimenet:

```text
1 4
```

**2. Egyforma szobák**


Bemenet:

```text
2 2
```

Elvárt kimenet:

```text
2 2
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért nem fordult a paraméterek nélküli tömbdeklaráció?
2. Milyen konstruktor kellene az eredeti deklarációhoz?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_04"></a>

## G09_04 – Inicializáló listára átírás

**Fájl:** `g09_04.cpp` · Működő kód előírt átalakítása

**Cél:** Inicializálás és későbbi értékadás megkülönböztetése.

A kezdőkód már helyes kimenetet ad. Írd át a konstruktort úgy, hogy a két adatmező inicializáló listában, a deklarációjuk sorrendjében kapjon kezdőértéket, és a konstruktortörzs üres legyen. A többi részt hagyd meg. Bemenet: sor és szék, két 1…20 közötti egész. A feladat teljesítéséhez forráskód-ellenőrzés is kell.

**Kódellenőrzés:** A két mező deklarációs sorrendben inicializáló listában szerepel; a konstruktortörzs üres. A kezdőkód kimenete is jó, ezért a futtatás önmagában nem elég.

### Ellenőrző próbák

**1. Szokásos hely**


Bemenet:

```text
4 12
```

Elvárt kimenet:

```text
4 12
```

**2. Első hely**


Bemenet:

```text
1 1
```

Elvárt kimenet:

```text
1 1
```

### Elméleti kérdések – a kód ellenőrzése után

1. Mi határozza meg az adatmezők inicializálási sorrendjét?
2. Mikor fut le a konstruktortörzs a mezők inicializálásához képest?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_05"></a>

## G09_05 – Utolsó könyv kivétele

**Fájl:** `g09_05.cpp` · Kiegészítendő kód

**Cél:** Kompozíció és logikai elemszám kezelése.

Írd meg az utolsotKivesz függvényt: üres polcnál false változtatás nélkül, egyébként az elemszám csökkenjen eggyel és az eredmény true legyen. A tömböt nem kell átméretezni vagy nullázni. Bemenet: kezdeti elemszám n (0…2), kivételi próbák száma k (1…3). Minden próbáról sikerjelző és új elemszám jelenjen meg.

### Ellenőrző próbák

**1. Üres polc**


Bemenet:

```text
0 1
```

Elvárt kimenet:

```text
0 0
```

**2. Egy könyv**


Bemenet:

```text
1 2
```

Elvárt kimenet:

```text
1 0
0 0
```

**3. Két könyv**


Bemenet:

```text
2 3
```

Elvárt kimenet:

```text
1 1
1 0
0 0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miben különbözik a kapacitás az aktuális elemszámtól?
2. Miért kompozíció a polc és a könyvek kapcsolata?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g09_06"></a>

## G09_06 – Hívás az adott mutatón keresztül

**Fájl:** `g09_06.cpp` · Kiegészítendő kód

**Cél:** Virtuális hívás megfigyelése egy kész, rövid példán.

Az osztálydefiníciók készen vannak, azokat ne módosítsd. A két TODO helyén a mutato mutatón keresztül hívd meg és írd ki a jelzes eredményét. Bemenet: 0 vagy 1. A 0 az alapobjektumot hagyja meg, az 1 a második híváshoz a csengőt választja. Ne hardkódold a kimenetet; a megadott mutatót használd.

**Kódellenőrzés:** Mindkét kiírás a megadott alapmutatón keresztül hívja a virtuális függvényt. Az osztályok változatlanok; nincs hardkódolt válasz.

### Ellenőrző próbák

**1. Alapobjektum marad**


Bemenet:

```text
0
```

Elvárt kimenet:

```text
BASE
BASE
```

**2. Átváltás csengőre**


Bemenet:

```text
1
```

Elvárt kimenet:

```text
BASE
DING
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért lehet DING a második eredmény Eszkoz* típusú mutató mellett is?
2. Miben segít itt az override?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_01"></a>

## G10_01 – Rövid számlista mentése

**Fájl:** `g10_01.cpp` · Kiegészítendő kód

**Cél:** Fájlba írás, felülírás és ellenőrzött lezárás.

A mentes függvényben írd az első n egész számot külön sorokba. A fájlnyitás és hibaellenőrzés kész. A mentés mindig felülírja az out01.txt korábbi tartalmát, n=0 esetén üres fájlt eredményez. Bemenet: n (0…4), majd n darab −99…99 közötti egész. A main OK után visszaolvassa és kiírja a fájlt.

### Ellenőrző próbák

**1. Három szám**


Bemenet:

```text
3
4 -2 9
```

Elvárt kimenet:

```text
OK
4
-2
9
```

Elvárt fájltartalom: `out01.txt`

```text
4
-2
9
```

**2. Felülírás**

Kezdés előtt az `out01.txt` tartalma:

```text
99
88
```

Bemenet:

```text
1
7
```

Elvárt kimenet:

```text
OK
7
```

Elvárt fájltartalom: `out01.txt`

```text
7
```

**3. Üres mentés**

Kezdés előtt az `out01.txt` tartalma:

```text
99
```

Bemenet:

```text
0
```

Elvárt kimenet:

```text
OK
```

Elvárt fájltartalom: `out01.txt`

*Üres fájl (0 bájt).*

### Elméleti kérdések – a kód ellenőrzése után

1. Miért ofstream-et használ a mentőfüggvény?
2. Miért ellenőrizzük az állapotot a close után is?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_02"></a>

## G10_02 – Hozzáfűzés két futtatásban

**Fájl:** `g10_02.cpp` · Javítandó működés

**Cél:** Hozzáfűző megnyitás és megmaradó fájltartalom.

A kezdőkód hibásan felülír. Javítsd csak a megnyitási módot, hogy a beolvasott számot hozzáfűzze az out02.txt végéhez. Az első közös próbához a fájl tartalma egy 2-es sor legyen (a csomagban ezt kapod). Futtasd 5-tel, majd ugyanabban a mappában −1-gyel; a két futás között ne állítsd vissza a fájlt. Külön próbában hiányzó fájllal is ellenőrizd. A bemenet egy −99…99 közötti egész.

### Ellenőrző próbák

**1. Két egymást követő futás**

Kezdés előtt: `out02.txt` = egy sor, `2`. A két lépés között nincs visszaállítás.

Futtatás 1:

Bemenet:

```text
5
```

Elvárt kimenet:

```text
2
5
```

Elvárt fájltartalom: `out02.txt`

```text
2
5
```

Futtatás 2:

Bemenet:

```text
-1
```

Elvárt kimenet:

```text
2
5
-1
```

Elvárt fájltartalom: `out02.txt`

```text
2
5
-1
```

**2. Hiányzó fájl létrehozása**

Külön próbához az `out02.txt` ne létezzen; előbb őrizd meg az előző próba fájlját.

Bemenet:

```text
7
```

Elvárt kimenet:

```text
7
```

Elvárt fájltartalom: `out02.txt`

```text
7
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miben különbözik az ios::app az itt használt eredeti megnyitástól?
2. Melyik mappához képest értelmeződik az out02.txt relatív útvonala?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_03"></a>

## G10_03 – Negatív értékek számlálása

**Fájl:** `g10_03.cpp` · Kiegészítendő kód

**Cél:** Beolvasásvezérelt ciklus és eredmény átadása csak siker esetén.

A TODO 1 helyén számold a negatív számokat az ideiglenes változóban; a TODO 2 helyén csak a már ellenőrzött beolvasás után add át az eredményt a kapott mutatón keresztül. A fájlnevet a standard bemenet adja. A feladat fájljaiban csak −99…99 közötti egész tokenek, szóközök vagy a hibát jelölő X szerepelnek; nincs túlcsordulás vagy részben numerikus token. Hiányzó/hibás fájlnál maradjon 99 az eredmény. Az üres fájl sikeres, 0 darabbal.

### Ellenőrző próbák

**1. Vegyes számok**


Bemenet:

```text
data/neg_ok.txt
```

Elvárt kimenet:

```text
1 2
```

**2. Üres**


Bemenet:

```text
data/neg_empty.txt
```

Elvárt kimenet:

```text
1 0
```

**3. Záró sortörés nélkül**


Bemenet:

```text
data/neg_no_newline.txt
```

Elvárt kimenet:

```text
1 1
```

**4. Hibás token**


Bemenet:

```text
data/neg_bad.txt
```

Elvárt kimenet:

```text
0 99
```

**5. Hiányzó fájl**


Bemenet:

```text
data/missing.txt
```

Elvárt kimenet:

```text
0 99
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért egy ideiglenes változóban számolunk?
2. Mikor módosul a hívó eredményváltozója?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_04"></a>

## G10_04 – Fájl végi többletszámlálás

**Fájl:** `g10_04.cpp` · Javítandó működés

**Cél:** A while (!eof()) hibájának javítása.

A kezdőkód néhány fájlnál egy értéket még egyszer feldolgoz. Alakítsd a ciklust sikeres beolvasással vezéreltté, és hagyd el a törzsből a külön beolvasást. A bemenet a fájlnév; a fájlokban csak érvényes −99…99 közötti egészek vannak, vagy üresek. Kimenet: a páros számok darabszáma. A nulla páros.

### Ellenőrző próbák

**1. Záró sortöréssel**


Bemenet:

```text
data/even_newline.txt
```

Elvárt kimenet:

```text
1
```

**2. Záró sortörés nélkül**


Bemenet:

```text
data/even_no_newline.txt
```

Elvárt kimenet:

```text
2
```

**3. Üres**


Bemenet:

```text
data/even_empty.txt
```

Elvárt kimenet:

```text
0
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért kell a beolvasás sikerét még a feldolgozás előtt ellenőrizni?
2. Miért nem jelzi előre az eof(), hogy a következő olvasás sikerül-e?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_05"></a>

## G10_05 – Két egész mező szigorú ellenőrzése

**Fájl:** `g10_05.cpp` · Kiegészítendő kód

**Cél:** Mezőszám és értéktartomány ellenőrzése kész tokenellenőrzővel.

A sorEllenoriz függvény pontosan két egész tokent fogadjon el: kód és 0…20 közötti darabszám. Az egeszToken segédfüggvény kész, azt ne módosítsd. Az első TODO helyén ellenőrizd a két mező meglétét és a harmadik hiányát; a másodiknál a darabszám tartományát. A kód bármely int érték lehet. Hibánál mindkét kimeneti változó maradjon az eredeti értékén (77, 88). A standard bemenet egy teljes sora a vizsgált adat.

### Ellenőrző próbák

**1. Érvényes**


Bemenet:

```text
12 7
```

Elvárt kimenet:

```text
1 12 7
```

**2. Hiányzó mező**


Bemenet:

```text
12
```

Elvárt kimenet:

```text
0 77 88
```

**3. Többletmező**


Bemenet:

```text
12 7 extra
```

Elvárt kimenet:

```text
0 77 88
```

**4. Hibás token**


Bemenet:

```text
12x 7
```

Elvárt kimenet:

```text
0 77 88
```

**5. Alsó határ**


Bemenet:

```text
0 0
```

Elvárt kimenet:

```text
1 0 0
```

**6. Felső határ**


Bemenet:

```text
-4 20
```

Elvárt kimenet:

```text
1 -4 20
```

**7. Túl nagy**


Bemenet:

```text
12 21
```

Elvárt kimenet:

```text
0 77 88
```

**8. Negatív mennyiség**


Bemenet:

```text
12 -1
```

Elvárt kimenet:

```text
0 77 88
```

**9. Üres sor**


Bemenet:

```text

```

Elvárt kimenet:

```text
0 77 88
```

**10. Részben numerikus mennyiség**


Bemenet:

```text
12 7x
```

Elvárt kimenet:

```text
0 77 88
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért külön ellenőrzés a mezők száma és az egyes tokenek teljes egészszám-volta?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.

<a id="g10_06"></a>

## G10_06 – Betöltés a régi adatok megőrzésével

**Fájl:** `g10_06.cpp` · Javítandó működés

**Cél:** Ideiglenes tároló és egyetlen végső állapotcsere.

A kész segédfüggvényekhez és a mainhez ne nyúlj. A betolt függvény jelenleg túl korán törli és módosítja a célt. Javítsd úgy, hogy a kapacitásellenőrzés és minden új érték az ideiglenes listán történjen; a célt csak teljes siker után cseréld le. Fájlformátum: soronként pontosan egy 0…50 közötti egész, legfeljebb két sor. Az üres fájl érvényes üres lista, az üres sor hibás. Hibánál a 40, 41 értékű eredeti lista maradjon meg. Bemenet a fájlnév; kimenet: sikerjelző, elemszám, majd az elemek.

### Ellenőrző próbák

**1. Sikeres csere**


Bemenet:

```text
data/load_ok.txt
```

Elvárt kimenet:

```text
1 2 5 7
```

**2. Üres fájl**


Bemenet:

```text
data/load_empty.txt
```

Elvárt kimenet:

```text
1 0
```

**3. Hibás második sor**


Bemenet:

```text
data/load_bad.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

**4. Kapacitástúllépés**


Bemenet:

```text
data/load_full.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

**5. Üres sor**


Bemenet:

```text
data/load_blank.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

**6. Negatív érték**


Bemenet:

```text
data/load_negative.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

**7. Többletmező**


Bemenet:

```text
data/load_extra.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

**8. Hiányzó fájl**


Bemenet:

```text
data/missing.txt
```

Elvárt kimenet:

```text
0 2 40 41
```

### Elméleti kérdések – a kód ellenőrzése után

1. Miért csak a teljes beolvasás után történhet meg a cél lecserélése?
2. Mi a különbség az üres fájl és az egy üres sort tartalmazó fájl között ebben a feladatban?

**Kész, ha:** a kód megfelel a feladatnak, az összes fenti próba sikeres, és mindegyik kérdésre saját szavaiddal válaszoltál.
