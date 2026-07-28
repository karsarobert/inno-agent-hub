# Számok statisztikája

## Tanulási cél

Bontsd a programot kis, egyértelmű feladatú függvényekre, és kezeld a `std::vector<int>` adatot konstans referencián keresztül.

## Előfeltétel

Ciklusok, `std::vector`, függvényparaméterek és visszatérési értékek.

## Feladat

Írj három függvényt, amelyek egy `std::vector<int>` elemeire kiszámítják az összeget, a legnagyobb értéket és az átlagot. A `main` állítson össze legalább öt számból álló mintavektort, majd írja ki mindhárom eredményt.

## Utalások

- A függvények paramétere legyen `const std::vector<int>&`.
- Döntsd el, mi legyen az üres vektor kezelése.
- Az átlaghoz figyelj az egész osztásra.

## Ellenőrzési szempontok

- A három számítás külön függvényben van.
- A bemeneti vektor nem másul feleslegesen és nem módosul.
- Ismert mintavektorral az összeg, maximum és átlag helyes.
- Az üres vektor esete dokumentált és kezelt.

## Lehetséges bővítés

Írj negyedik függvényt mediánszámításhoz úgy, hogy az eredeti vektort ne rendezd át.
