# CPP_09 – InnoAgent hallgatói csomag

**3 × 45 perc.** Konstruktorok, érvényes kezdőállapot, együttműködő osztályok és kompozíció.

## Indítás

1. Csomagold ki egy új, üres munkamappába; ne másold rá a korábbi leckére vagy a másik nyelvi változatra.
2. Nyisd meg a mappát InnoAgent-munkaterületként a korábban használt beállítással.
3. Írd: **„Kezdjük a 9. C++-gyakorlatot!”**
4. A kódot te írod és mented. Egyetlen `.cpp` fájlt futtass egyszerre a RUN gombbal.

| Fájl | Tartalom |
|---|---|
| G09_01_versenyzo.cpp | Versenyző: háromféle konstruktor |
| G09_02_fenyero.cpp | Fényerő: `?:`, kezdőállapot és módosítás |
| G09_03_kuldemeny.cpp | Küldemény és díjszámító |
| G09_04_eredmenylap.cpp | Eredménylap: objektumtömb és kompozíció |
| P09_jegypenztar.cpp | Színházi helyfoglalás, hat lépésben |

A starterek önmagukban lefordulnak, de még nem oldják meg a feladatot. A kért osztályokat, konstruktorokat, feltételeket és ciklusokat neked kell megírnod. Inno előbb más problémát megoldó mintát és magyarázatot ad.

## A három blokk

1. Négy alapozó feladat: 45 perc, az indítással együtt.
2. Jegypénztár: 45 perc, egyetlen folyamatosan bővülő forrásban.
3. 20 kérdés: 10 feleletválasztós, 5 kimenetértési, 5 hibakeresési; visszajelzéssel 45 perc.

A szünetek ezen felül értendők. A lecke a fenti feladatokból áll; nincs külön kiegészítő feladatsor. Nincs házi feladat vagy automatikusan bejelentett következő ZH.

## Kísérőanyagok

- `LECKE_UTASITASOK.md`: az alapozó feladatok pontos követelményei.
- `MINTAKODOK.md`: eltérő problémájú, teljes analóg programok magyarázattal.
- `PROJEKT.md`: a jegypénztár lépései és ellenőrző esetei.
- `TANULOI_MUNKALAP.md`: rövid áttekintő; külön szerkesztened nem kell.
- `ZARO_TESZT.md`: rögzített kérdések, megoldókulcs nélkül.
- `HALADAS.json`: a tutor által vezetett folytatási állapot.
- `agent.md`: a tutor működését irányító útmutató.

Az oktatói megoldáscsomagot külön kell tartani. Ne másold a hallgatói munkamappába. A ZIP önmagában nem telepít és nem konfigurál InnoAgentet; a munkaterületi utasítások betöltése az alkalmazás beállításától függ.

RUN-hibánál vagy kérésre, az adott munkamappában nyitott terminálban:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G09_01_versenyzo.cpp -o G09_01 && ./G09_01
```

A `&&` miatt a program csak sikeres fordítás után indul. Ne fordítsd együtt az öt forrást: mindegyiknek saját `main` függvénye van.
