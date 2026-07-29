# C/C++ programozás alapok — 10 alkalmas kezdő kurzus

## Cél és működés

- Célcsoport: teljesen kezdő hallgatók.
- Javasolt időkeret: 10 × 90 perc, alkalmonként rövid elmélet, közös kódolás, önálló gyakorlás és lezáró reflexió.
- Nyelvi keret: a megadott számozott anyagok C/C++ szemléletére épülünk, de az új programok C++20-stílusban készülnek (`<iostream>`, `std::string`, `std::vector`, RAII).
- Minden alkalom végén csak a tanuló jóváhagyásával frissüljön a `progress.json`.
- Technikai előfeltétel a Run-gombhoz: a szervert futtató gépen legyen a `PATH`-ból elérhető C++20-kompatibilis `g++`. Ubuntu/Debian rendszeren: `sudo apt install g++`.

## Alkalmak

| # | Modul | Fő eredmény | Elsődleges forrás |
|---|---|---|---|
| 1 | Algoritmikus gondolkodás és első program | probléma → pszeudokód → fordítható program | `1. Algoritmikus gondolkodas fejlesztese.pdf`, `2. Bevezetés.pdf`, `C++Programming.pdf` 1. fejezet |
| 2 | Változók és adattípusok | bemenet, számítás, típusválasztás | `3. Változók.pdf` |
| 3 | Vezérlési szerkezetek | döntés és ismétlés | `4. Vezérlési szerkezetek.pdf` |
| 4 | Tömbök és mutatók | adatsor feldolgozása, cím és érték elkülönítése | `5. Tömbök és mutatók.pdf` |
| 5 | Sztringek | biztonságos szövegkezelés `std::string`-gel | `6. Sztringek.pdf` |
| 6 | Függvények | felbontott, tesztelhető program | `7. Függvények.pdf` |
| 7 | Struktúrák és dinamikus adatok | összetartozó adatok modellezése | `8. Struct.pdf` |
| 8 | Objektumorientált programozás | osztály, adatrejtés, konstruktor | `9. Objektum.pdf` |
| 9 | Fájlkezelés | adat mentése és visszaolvasása | `10. Fájlkezelés.pdf` |
| 10 | `main`, parancssori argumentumok és mini-projekt | önálló, dokumentált program | `11. Main.pdf` |

## Referenciaanyagok

A kurzustervezéshez használt helyi források:

- `/home/karsa-robert/C++/1. Algoritmikus gondolkodas fejlesztese.pdf` – `/home/karsa-robert/C++/11. Main.pdf`
- `/home/karsa-robert/C++/LearnCProgramming.pdf` (Jeff Szuhay, *Learn C Programming*, 2nd ed.)
- `/home/karsa-robert/C++/C++Programming.pdf`

A kurzus feladatai új, magyar nyelvű, C++20-hoz igazított feladatok; nem a forráskönyvek megoldáskulcsai.

## Oktatási ritmus minden alkalommal

1. Rövid diagnosztikus visszakérdezés az előző alkalomról.
2. Az adott modul `lessons/<modul-azonosító>/theory.md` anyagának vezetett feldolgozása. Elméleti anyag nélkül nem indulhat új lecke.
3. Egy új, jól elkülönített fogalom bemutatása és közös, kis példa: előrejelzés → futtatás → hibajavítás.
4. Egyéni feladat a megfelelő `exercises/` mappából.
5. Rövid szóbeli kódmagyarázat és ellenőrzés.
6. A következő lépés rögzítése; `progress.json` csak jóváhagyással frissül.
