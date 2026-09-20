# CPP_03 – gyakorlati feladatok

A feladatok rövid programokra épülnek. A fájlokban a program kerete már készen van;
a kijelölt részeket te írod meg. Ments minden módosítás után, majd fordítsd és futtasd.

Két lehetőséged van:

1. **RUN gomb:** a kódszerkesztő ablak feletti RUN gombbal az aktuális fájlt
   lefordíthatod és futtathatod. Ehhez nem kell könyvtárat váltanod.
2. **Terminál:** például az első fájlnál:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G03_01_if.cpp -o G03_01_if
./G03_01_if
```

A fájl- és programnevet mindig az aktuális feladathoz igazítsd. A gyakorlat során
bármelyik módszert használhatod. A kiinduló TODO-s fájloknál előfordulhat
`unused variable` figyelmeztetés; ez azért van, mert a megadott változót még nem
használtad fel. A feladat megoldása után ez rendszerint eltűnik.

## G03_01 – egyszerű if

**Fájl:** `G03_01_if.cpp`

Írj `if` szerkezetet, amely akkor írja ki a `Fagyveszély.` sort, ha a hőmérséklet
kisebb a fagyhatárnál. Az `Ellenőrzés vége.` sor mindig jelenjen meg.

Próbáld ki legalább `-3` és `2` hőmérséklettel.

## G03_02 – if–else

**Fájl:** `G03_02_if_else.cpp`

Döntsd el a `szam` változóról, hogy páros vagy páratlan. Pontosan az egyik üzenet
jelenjen meg:

- `A szám páros.`
- `A szám páratlan.`

Próbák: 17, 18 és 0.

## G03_03 – több lehetőség

**Fájl:** `G03_03_pontszam.cpp`

Kategorizáld a pontszámot:

- 80–100: `Kiváló`
- 60–79: `Megfelelő`
- 0–59: `Fejlesztendő`
- 0 alatt vagy 100 felett: `Hibás pontszám`

Használj `if / else if / else` láncot. Határértékekkel is próbáld ki.

## G03_04 – switch

**Fájl:** `G03_04_switch.cpp`

A `sorszam` alapján írd ki:

- 1 → `Első`
- 2 → `Második`
- 3 → `Harmadik`
- más érték → `Ismeretlen`

Használj `switch`, `case`, `break` és `default` elemeket.

## G03_05 – while

**Fájl:** `G03_05_while.cpp`

`while` ciklussal írd ki 1-től 5-ig a számokat külön sorokba. Figyelj arra, hogy a
ciklusváltozó minden iterációban közelebb kerüljön a kilépési feltételhez.

Ezután próbáld ki 6-os kezdőértékkel is.

## G03_06 – do–while

**Fájl:** `G03_06_do_while.cpp`

`do–while` ciklussal írd ki 1-től 3-ig a számokat. Ezután legyen a kezdőérték 4,
és figyeld meg a különbséget a `while` feladathoz képest.

## G03_07 – for

**Fájl:** `G03_07_for.cpp`

`for` ciklussal írd ki 1-től 5-ig a számokat. Ezután módosítsd úgy, hogy ezt kapd:

```text
2
4
6
8
10
```

## G03_08 – páros számok darabszáma

**Fájl:** `G03_08_paros_darabszam.cpp`

Járd be az 1..10 tartományt egy `for` ciklussal, és `if` segítségével számold meg a
páros számokat. A végén ilyen formában jelenjen meg az eredmény:

```text
Páros számok darabszáma: <eredmény>
```

Ezután próbáld ki a 3..9 tartományt is. A második eredményt is te határozd meg a
program futásából.

## G03_09 – 3-mal osztható számok összege

**Fájl:** `G03_09_oszthato_osszeg.cpp`

Járd be az 1..15 tartományt. Csak a 3-mal osztható számokat add hozzá az
`osszeg` változóhoz. A végén ilyen formában jelenjen meg az eredmény:

```text
Összeg: <eredmény>
```

Ezután próbáld ki az 1..10 tartományt is. A számszerű eredményt most a programmal
ellenőrizd, ne a feladatleírásból olvasd ki.

## Záróteszt

A tutor a kódírás után két rövid tesztet vezet:

1. feleletválasztós kérdések;
2. egyszerű C++ kódrészletek kimenetének megjóslása.

A kimenetjóslásnál előbb válaszolj, és csak utána ellenőrizzétek a végrehajtást.

**Nincs házi feladat.** A kötelező gyakorlat a záróteszttel és a tutor lezáró
összegzésével befejeződik. A lezárás után a tutor felajánlhat **egy rövid opcionális
plusz feladatot**. Ez nem része a kötelező CPP_03 gyakorlatnak.

## Opcionális plusz gyakorlás

A kötelező CPP_03 gyakorlat lezárása után, ha még szeretnél egyetlen rövid feladatot
megoldani, a tutor felajánlhatja a `G03_PLUSZ_gyakorlas.cpp` fájlt. Ez **nem házi
feladat**, nem kötelező, és nem része a záróteszt eredményének.
