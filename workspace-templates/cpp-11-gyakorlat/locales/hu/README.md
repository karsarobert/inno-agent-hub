# C++ 07–10 – rövid InnoAgent-gyakorlatok

24 önálló kódolási feladat, mindegyik után 1–2, a saját kódra vonatkozó elméleti kérdés. Négy blokk, blokkonként 6 feladat. A 47 elméleti kérdés a kódolás utáni megbeszélés része.

## Indulás

1. A teljes magyar csomagot bontsd ki egy külön munkamappába; a `data` mappát is tartsd meg.
2. Nyisd meg a mappát az InnoAgentben. A tutor kezdőutasítása az `agent.md`. Ha a felület nem olvassa automatikusan, ezt add meg neki, és tedd elérhetővé a csomag fájljait.
3. Nyisd meg a `g07_01.cpp` fájlt. Egyszerre egy `.cpp`-t fordíts és futtass; mindegyik külön `main` függvényt tartalmaz.
4. A tutor kis lépésekben végigvezet. A feladatlapot a `FELADATOK.md`, saját jegyzeteidet a `TANULOI_MUNKALAP.md` tartalmazza.

## Futtatási feltételek

C++17, szabványos könyvtár, külön telepítendő C++-csomag nélkül. Terminálból például:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic g07_01.cpp -o g07_01 && ./g07_01
```
Az `&&` miatt sikertelen fordítás után nem indul régi program. InnoAgentben az adott fájl RUN műveletét használd. A futási munkakönyvtár a csomag gyökere legyen: innen érhető el a `data/...` útvonal. Minden futásnál a feladatlap pontos bemenetét add meg; a megadott tartományokon kívüli konzolbemenet kezelése nem része ezeknek a feladatoknak.

A G07_05, G08_02, G08_04 és G09_03 szándékosan fordítási hibával indul. Más kezdőkód lefordulhat, de még hiányos vagy hibás. A G09_04 működő kód átalakítása. Kezdőkód nem egyenlő mintamegoldással.

A fájlkezelő feladatok az `out01.txt` és `out02.txt` fájlokat írják; a `data` tesztfájlokat őrizd meg változatlanul. Az `out02.txt` kezdetben `2`-t tartalmaz. A G10_02 két összetartozó futása között ne állítsd vissza. Új fájl megjelenítéséhez szükség lehet a fájlnézet frissítésére.

## Felosztás

| Blokk | Témakör | Tervezett idő |
|---|---|---|
| 07 | Struktúra, másolás, mutató, hatókör, unió | 45–60 perc |
| 08 | Osztály, privát mező, getter, const, objektumtömb | 45–60 perc |
| 09 | Konstruktor, inicializálás, kompozíció, kész virtuális példa | 45–60 perc |
| 10 | Fájlírás, hozzáfűzés, beolvasás, ellenőrzés, biztonságos csere | 60–75 perc |

Az idő tájékoztató; több alkalomra bontható. Nincs záróprojekt, külön záróteszt vagy beadandó. A kód ellenőrzése után a tutor egyenként teszi fel a feladathoz tartozó kérdéseket. A haladás mentett állapotból folytatható.
