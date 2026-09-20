# C++ 3. gyakorlat – vezérlési szerkezetek

Ez a csomag a **CPP_03 – Vezérlési szerkezetek** elméleti anyag gyakorlati folytatása.
Időkeret: **3 × 45 perc gyakorlat**, a szüneteken felül.

A fő cél most már nem csak kész programok módosítása. A hallgató **kis lépésekben
saját C++ kódrészleteket ír**, miközben az Inno tutor röviden elmagyarázza az új
szerkezetet, mintát mutat, majd visszalép és a hallgatót hagyja dolgozni.

A gyakorlat nem épül egyetlen nagy projekt köré. Rövid, különálló programokban
vizsgáljuk az `if`, `if–else`, `else if`, `switch`, `while`, `do–while` és `for`
szerkezeteket, majd két kisebb összekapcsoló feladatban több ismert elemet együtt
használunk.

## Fontos munkamegosztás

**A kódot a hallgató írja, szerkeszti és menti, a fordítást és futtatást is ő végzi.**
Inno a feladatot és az új fogalmat elmagyarázza, szükség esetén rövid analóg példát
mutat, segít hibát keresni, majd megvárja a hallgató próbáját.

A hallgató kétféleképpen futtathatja a programot:

- a kódszerkesztő ablak feletti **RUN** gombbal;
- vagy terminálból, például:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G03_01_if.cpp -o G03_01_if
./G03_01_if
```

A RUN gomb használatához nem kell könyvtárat váltani. Terminálos futtatásnál mindig
az aktuális fájl valódi nevét kell használni.

## A gyakorlat felépítése

### 1. blokk – döntések

- G03_01: egyszerű `if`
- G03_02: `if–else`
- G03_03: `else if` lánc
- G03_04: `switch`

### 2. blokk – ciklusok

- G03_05: `while`
- G03_06: `do–while`
- G03_07: `for`

### 3. blokk – kis összekapcsolások és zárás

- G03_08: `for` + `if` – páros számok megszámlálása
- G03_09: `for` + `if` + összegzés – 3-mal osztható számok összege
- záró feleletválasztós teszt
- záró kimenetjóslós teszt
- rövid tanulási összegzés és memóriamentés

## Mit nem tartalmaz a csomag?

- nincs házi feladat;
- nincs nagy, több részből álló alkalmazás;
- nincs saját függvény, tömb, pointer vagy osztály;
- nincs olyan elvárás, hogy a hallgató teljes programot emlékezetből írjon üres fájlból;
- nincs automatikus forrásfájl-javítás az agent részéről.

A gyakorlat végén Inno egyértelműen kimondja, hogy **a CPP_03 kötelező gyakorlat
véget ért**, jelzi, hogy nincs házi feladat, és a tényleges haladást, a támogatás
mértékét és a záróteszt eredményét az L1 tanulói memóriában rögzíti, ha ez a
környezetben elérhető. Ezután felajánlhat **egyetlen rövid opcionális plusz
gyakorlófeladatot** (`G03_PLUSZ_gyakorlas.cpp`), amely nem része a kötelező
teljesítésnek.
