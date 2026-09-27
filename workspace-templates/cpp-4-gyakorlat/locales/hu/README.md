# C++ – 4. gyakorlat: tömbök és mutatók

A csomag a **CPP_04 – Tömbök és mutatók** elméleti anyag gyakorlati folytatása.
Időkeret: **3 × 45 perc** gyakorlat, a szüneteken felül.

## A gyakorlat célja

A gyakorlat végére a hallgató:

- érti a tömb indexelését és a 0-tól induló indexek szerepét;
- `for` ciklussal be tud járni egy tömböt;
- egyszerű összegzést, átlagot és feltételes számlálást tud készíteni;
- meg tudja különböztetni egy változó értékét és memóriacímét;
- érti, mit tárol egy mutató, mit jelent az `&` és a `*`;
- példán keresztül érti a dereferálás fogalmát;
- ismeri a `nullptr` alapvető szerepét;
- felismeri a `tomb[i]` és `*(mutato + i)` kapcsolatát;
- biztonságosan tud egyszerű tömböt mutató segítségével bejárni és módosítani.

## Munkamegosztás

**A kódot a hallgató szerkeszti, menti és futtatja.** Inno magyaráz, kérdez, kisebb mintát ad és segít a hibakeresésben, de nem írja meg helyette a teljes megoldást.

A legegyszerűbb futtatás a szerkesztőablak feletti **RUN / Futtatás** gomb. A terminálból is lehet fordítani és futtatni, például:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G04_01_tomb_alapok.cpp -o G04_01
./G04_01
```

A RUN gomb kezeli a fájl útvonalát, ezért használatához nem kell `cd` paranccsal mappát váltani.

## Felépítés

Minden kötelező `.cpp` fájl két lépést tartalmaz. A starterek csak a szükséges adatokat és minimális programkeretet adják; a kulcsfontosságú indexelést, ciklust, feltételt és mutatókifejezést a hallgató írja meg:

- **A feladat:** az új fogalom alapvető alkalmazása;
- **B feladat:** ugyanannak a fogalomnak egy önállóbb, módosított alkalmazása.

Így a hallgató nem egy előre kitöltött mintát egészít ki, hanem a tanult szintaxist maga idézi fel és rögtön alkalmazza is.

| Fájl | Téma |
|---|---|
| `G04_01_tomb_alapok.cpp` | Index, érték, utolsó elem |
| `G04_02_tomb_modositas.cpp` | Közvetlen és relatív módosítás |
| `G04_03_tomb_bejaras.cpp` | Bejárás, index + érték |
| `G04_04_osszegzes.cpp` | Összeg és átlag |
| `G04_05_felteteles_szamlalas.cpp` | Két feltételes számlálás |
| `G04_06_cim_es_mutato.cpp` | Érték, cím, mutató átállítása |
| `G04_07_dereferalas.cpp` | Dereferálás és két módosítás |
| `G04_08_nullptr.cpp` | `nullptr`, ellenőrzés, másik objektum |
| `G04_09_tomb_es_mutato.cpp` | Első és második elem címe mutatóval |
| `G04_10_mutato_bejaras.cpp` | Mutatós bejárás, módosítás, összegzés |

A programozási feladatsort **előre rögzített záróteszt** követi: 6 feleletválasztós fogalmi kérdés és 6 teljes C++ program kimenetjóslása. A kérdéseket a `ZARO_TESZT.md` tartalmazza; Inno ezeket egyenként vezeti, nem generál helyettük új tesztet.

## Adaptív további kihívás

A csomag tartalmaz egy összetettebb `K04_01_plusz.cpp` feladatot is. Ezt Inno csak akkor kínálja fel, ha a hallgató a kötelező programozási feladatokat és a záró ellenőrzést a tervezettnél lényegesen gyorsabban teljesíti. Ez nem része a kötelező teljesítésnek és nem házi feladat.

## Fontos

- A tömbhatáron kívüli indexelést nem próbáljuk ki szándékosan.
- `nullptr` értékű mutatót nem dereferálunk.
- A gyakorlatban nem használunk `new`, `delete`, `malloc`, `free`, `int**`, saját függvényt vagy dinamikus tömböt.
- A tömb és a mutató nem ugyanaz. A tömb neve sok kifejezésben az első elemére mutató mutatóvá alakul.
- Nem kell minden feladat előtt kimenetet jósolni; a jóslást csak ott használjuk, ahol egy új működési modellt segít ellenőrizni.
