# C++ 3. gyakorlat – belső foglalkozási forgatókönyv

## Időkeret

Teljes idő: 3 × 45 perc. A gyakorlat gyakorlati fókuszú. A magyarázat legyen rövid,
a hallgatói kódírás, fordítás, futtatás és értelmezés kapja a legtöbb időt.

Javasolt beosztás:

- 1. blokk: E0 5 perc, G03_01 9, G03_02 9, G03_03 11, G03_04 9, S1 2.
- 2. blokk: G03_05 12, G03_06 10, G03_07 15, összegzés 8.
- 3. blokk: G03_08 12, G03_09 12, T1 8, T2 10, lezárás 3.

A percértékek becslések. Ne találj ki eltelt időt.

## E0 – indulás és munkamód

Az agent mutatkozzon be a saját útmutatója szerint. A hallgatónak mondd el, hogy
most már rövid kódrészleteket ő ír meg, de nem kell teljes programot üres lapról
felépítenie. A fájlokban a keret és a szükséges változók egy része készen van.

Az elején egyszer mutasd be a futtatás két módját:

1. a kódszerkesztő ablak feletti **RUN** gomb: mentés után ezzel egyszerűen
   lefordíthatja és futtathatja az aktuális fájlt;
2. terminálból, például:
   `g++ -std=c++20 -Wall -Wextra -Wpedantic G03_01_if.cpp -o G03_01_if`
   majd `./G03_01_if`.

Mondd ki, hogy bármelyiket használhatja. A RUN gomb használatához ne kérj `cd`-t.
A teljes `g++` parancsot később csak szükség esetén ismételd.

Minden feladat előtt ellenőrizd az aktuális feladatleírást és a kapcsolódó `.cpp`
fájlt. A G03_01 például **fagyveszély-feladat**; ne cseréld fel más `if` példára.

Ellenőrzés csak szükség esetén: `g++ --version`. Ne töltsétek az időt kötelező
környezetdiagnosztikával, ha a fordítás működik. A TODO-k kitöltése előtt egyes
kiinduló fájloknál `unused variable` figyelmeztetés jelenhet meg; ez várható, mert
a megadott változók még nincsenek használva. Ne kezeld hibaként.

## G03_01 – egyszerű if

**Fájl:** `G03_01_if.cpp`

**Cél:** negatív hőmérsékletnél jelenjen meg a `Fagyveszély.` üzenet, majd minden
esetben az `Ellenőrzés vége.` sor.

**Új fogalom:** az `if` törzse csak akkor fut, ha a feltétel igaz. A program az
elágazás után folytatódik.

**Analóg mikropélda, ha kell:**

```cpp
if (eletkor >= 18) {
    std::cout << "Nagykoru.\n";
}
```

Ne add meg a saját feladat teljes kész `if` blokkját rögtön.

**Hallgatói feladat:** a TODO helyére írja meg az `if` blokkot a már létező
`homerseklet` és `fagyhatar` változókkal.

**Próba 1:** `homerseklet = -3` → két sor: `Fagyveszély.` és `Ellenőrzés vége.`

**Próba 2:** módosítsa `homerseklet` értékét `2`-re → csak `Ellenőrzés vége.`

**Kódértés:** kérdezd meg röviden: miért jelenik meg a második sor mindkét futásban?

## G03_02 – if–else

**Fájl:** `G03_02_if_else.cpp`

**Cél:** döntse el egy egész számról, hogy páros vagy páratlan.

**Előismeret:** `%` maradékos osztás. Ha szükséges, röviden idézd fel:
`17 % 2` eredménye 1, `18 % 2` eredménye 0.

**Hallgatói feladat:** a TODO helyén írjon `if–else` szerkezetet. A feltétel a
`szam % 2 == 0` összehasonlítás legyen vagy ezzel azonos jelentésű megoldás.

**Próbák:** 17 → `A szám páratlan.`; 18 → `A szám páros.`; 0 → `A szám páros.`

Az első két próba után külön kérdezz rá a nullára, mert jó határeset.

**Kódértés:** miért pontosan az egyik ág fut le?

## G03_03 – else if lánc

**Fájl:** `G03_03_pontszam.cpp`

**Cél:** a 0–100 közötti pontszámot három kategóriába sorolni:

- 80 vagy több: `Kiváló`
- 60–79: `Megfelelő`
- 0–59: `Fejlesztendő`
- 0 alatti vagy 100 feletti: `Hibás pontszám`

A fájlban a határértékek és a `pontszam` változó adott. A hallgató írja meg a
teljes elágazási láncot.

**Tanítás:** először a hibás tartomány ellenőrzését beszéljétek meg. Ezután az
első igaz ág elvét. Nem kell minden köztes tartományhoz kétoldali feltétel, ha a
korábbi ágak már kizárták a nagyobb értékeket.

**Próbák:** -1, 0, 59, 60, 79, 80, 100, 101. Nem kell mindet egy körben futtatni;
a négy határpárból legalább egy-egy érték szerepeljen.

**Gyakori hiba:** egymástól független `if` blokkokkal több kategória is kiíródhat.
Ne mondd rögtön a javítást; kérdezd meg, miért lehet több feltétel egyszerre igaz.

## G03_04 – switch

**Fájl:** `G03_04_switch.cpp`

**Cél:** 1, 2 vagy 3 esetén írja ki rendre `Első`, `Második`, `Harmadik`; más
értéknél `Ismeretlen`.

**Új fogalom:** a `switch` egyetlen egész/enum jellegű kifejezés értéke alapján
választ `case` ágak között. A `break` lezárja az adott ágat.

A hallgató írja meg a `switch` szerkezetet. Ha elakad, előbb csak egy `case` mintát
mutass más adatokkal.

**Próbák:** 2 → `Második`; 5 → `Ismeretlen`.

**Rövid demonstráció, csak a működő megoldás után:** kérd meg, hogy ideiglenesen
törölje egy középső ág `break` sorát, fordítsa/futtassa, figyelje meg a továbbfutást,
majd **ő javítsa vissza a break-et**. Ez szándékos működésvizsgálat, nem maradó állapot.

## S1 – első blokk lezárása

Rövid összegzés: egyszerű `if`; kétútú `if–else`; első igaz ág az `else if`
láncban; `switch` és `break`. A tényleges állapotot írd memóriába. Nincs házi.

## G03_05 – while

**Fájl:** `G03_05_while.cpp`

**Cél:** írja ki 1-től 5-ig a számokat külön sorokba.

A fájlban adott a `const int utolso_szam = 5;` és `int aktualis_szam = 1;`.
A hallgató írja meg a teljes `while` ciklust.

**Tanítás:** három kérdés köré szervezd:

1. Mi az induló érték?
2. Mikor folytatódhat a ciklus?
3. Mitől változik úgy az állapot, hogy egyszer kilépünk?

**Próba:** 1..5.

**Módosítás:** `aktualis_szam = 6` → ne írjon ki számot. Ezzel látható, hogy a
`while` törzse akár egyszer sem fut.

Végtelen ciklust ne futtassatok szándékosan.

## G03_06 – do–while

**Fájl:** `G03_06_do_while.cpp`

**Cél:** 1-től 3-ig írja ki a számokat egy `do–while` ciklussal.

A hallgató írja meg a szerkezetet a megadott kezdőértékkel és határral.

**Első próba:** kezdőérték 1 → 1, 2, 3.

**Második próba:** kezdőérték 4 → a program egyszer írja ki a 4-et. Itt kérdezd
meg: miért futott le egyszer, miközben a folytatási feltétel már kezdetben hamis?

A végén állítsa vissza a működő tanpéldát 1-es kezdőértékre vagy hagyja meg a
második próbát; nincs szükség erőltetett alaphelyzetre, ha a forrás egyértelmű.

## G03_07 – for

**Fájl:** `G03_07_for.cpp`

**Cél:** 1-től 5-ig írja ki a számokat egy `for` ciklussal.

A fájlban csak az `utolso_szam` adott. A hallgató írja meg a teljes `for` ciklust.
A tutor előtte magyarázza el a három részt: inicializálás; feltétel; léptetés.

**Próba 1:** 1..5.

**Próba 2:** módosítsa a léptetést és kezdőértéket úgy, hogy 2, 4, 6, 8, 10 jelenjen
meg. Itt már ne adj kész fejlécet elsőre. A végértékhez új `const int` használható.

**Kódértés:** mi történik a ciklusváltozóval egy iteráció végén, és mikor áll le?

## S2 – második blokk lezárása

A hallgató saját próbái alapján foglald össze:

- `while` előtt ellenőriz;
- `do–while` után ellenőriz;
- `for` számlálásos esetben egy helyen tartja a vezérlés három elemét.

Írj memóriába folytatási pontot. Nincs házi.

## G03_08 – kis összekapcsolás: páros számok darabszáma

**Fájl:** `G03_08_paros_darabszam.cpp`

**Cél:** 1-től 10-ig vizsgálva számolja meg, hány páros szám van, majd írja ki a
darabszámot `Páros számok darabszáma: ...` formában.

A fájlban adott:

- `const int elso_szam = 1;`
- `const int utolso_szam = 10;`
- `int paros_darabszam{};`

A hallgató feladata:

1. írjon `for` ciklust a tartomány bejárására;
2. a ciklus törzsében `if` segítségével vizsgálja a párosságot;
3. igaz esetben növelje a számlálót;
4. a ciklus után írja ki a végeredményt.

Ez már összekapcsoló feladat. Elsőre csak a célt és a meglévő változókat mondd el.
Ne add meg előre a `for` fejlécet, a párosság feltételét vagy a számláló növelésének
konkrét kódsorát. Ne mondd meg előre, hány páros számot kell kapnia. Ha elakad,
előbb kérdéssel vezesd rá: hogyan döntöttük el korábban egy számról, hogy páros-e?

**Próba 1:** 1..10. Az agent belső ellenőrzéséhez a helyes darabszám 5, de ezt csak
a hallgató saját futása vagy jóslata után mondd ki.

**Próba 2 – önálló módosítás:** legyen a tartomány 3..9. Előre itt se add meg a
számszerű eredményt; a helyes darabszám belső ellenőrzéshez 3.

## G03_09 – kis összekapcsolás: 3-mal oszthatók összege

**Fájl:** `G03_09_oszthato_osszeg.cpp`

**Cél:** 1-től 15-ig adja össze a 3-mal osztható számokat, majd írja ki az
eredményt `Összeg: ...` formában.

A fájlban adott a tartomány és az `osszeg{}` változó. A hallgató írja meg a
`for` + `if` megoldást és az összegzést.

Elsőre ne add meg a kész oszthatósági feltételt és az `osszeg += aktualis_szam`
kódsort. A hallgatónak kell felidéznie a maradékos osztást és az összegző szerepét.
Ha elakad, segíts lépcsőzetesen: kérdés → rövid pszeudokód → csak végül konkrét sor.

**Próba 1:** 1..15. Belső ellenőrzéshez a helyes összeg 45, de ezt a hallgató
próbálkozása előtt ne közöld, és ne sorold fel előre a 3-mal osztható számokat.

**Próba 2:** 1..10. Belső ellenőrzéshez a helyes összeg 18; ezt is csak a hallgató
saját eredménye után használd ellenőrzésre.

Ha a hallgató a konkrét számokat kézzel összeadva égeti be a 45-öt, az nem teljesíti
a feladatot. A forrásban legyen ciklus, feltétel és összegző változó.

## T1 – feleletválasztós záróteszt

A kérdéseket a `ZARO_TESZT.md` fájlból egyenként tedd fel. Helyes válaszok:

1. B
2. C
3. A
4. C
5. B
6. D

Pontozás: 0–6 helyes. Ne alakítsd át százalékos tudásszintté.

Rövid indoklások:

1. `if` törzse csak igaz feltételnél fut.
2. `if–else` pontosan az egyik ágat választja.
3. `else if` láncban az első igaz ág után a további ágak kimaradnak.
4. `break` lezárja az aktuális `case` ágat.
5. `do–while` törzse legalább egyszer végrehajtódik.
6. `for` számlálásnál az inicializálás, feltétel és léptetés egy helyen látszik.

## T2 – kimenetjóslós záróteszt

Kérdésenként mutasd a kódot, és várd meg a hallgató pontos jóslatát.

Megoldások:

1. `A` majd `C` külön sorban – ellenőrzi, észreveszi-e az `if` utáni külön utasítást.
2. `Megfelelő` – pontos határértékes `else if` követés.
3. `Kettő` – `switch` és `break`.
4. `6` – `while` ciklus és összegző változó követése.
5. `4` – kezdetben hamis feltételű `do–while`, amely még egyszer lefut.
6. `2 4 6` – `for` + `if` együtt.

Pontozás: 0–6 helyes. Kisebb formázási eltérést ne tekints hibának, ha a végrehajtási
út és a kiírt értékek helyesek.

## ZARAS

A tesztek után ne indíts új kötelező feladatot. Rövid, tényszerű összegzés után
rögzítsd a végső tanulási eseményt. Mondd ki, hogy nincs házi feladat.

A kötelező lezárásban jól láthatóan szerepeljen:

**A CPP_03 kötelező gyakorlat itt véget ért.**

Csak ezután ajánld fel az egyetlen opcionális `G03_PLUSZ_gyakorlas.cpp` feladatot.
Ne kezdd el automatikusan; várd meg, hogy a hallgató kéri-e. Az opcionális feladat
nem módosítja a kötelező gyakorlat vagy a záróteszt eredményét.

## PLUSZ – opcionális egyfeladatos gyakorlás

**Fájl:** `G03_PLUSZ_gyakorlas.cpp`

**Cél:** járja be az 1..12 tartományt, írja ki a 3-mal osztható számokat, és a végén
írja ki, hány ilyen szám volt. Ez röviden összekapcsolja a `for`, `if`, oszthatóság
és darabszámlálás elemeit.

Elsőre csak a célt mondd el. Ne add meg a kiválasztandó számokat, a darabszámot, a
kész feltételt vagy a számláló növelésének sorát. Ugyanazt a fokozatos segítségi
létrát használd, mint G03_08–G03_09-ben.
