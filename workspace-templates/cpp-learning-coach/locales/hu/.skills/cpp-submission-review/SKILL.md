---
name: cpp-submission-review
description: C++ beadandók tanulóbarát, átlátható értékelése szabványos bizonyítékkal, rubrikával és a helyi haladásnaplóhoz illeszkedő összegzéssel.
---

# C++ beadandó értékelése

## Munkafolyamat

1. Azonosítsd a beadott feladatot és annak tanulási célját.
2. Fordítsd le C++20 módban a `cpp-compile-run` készséggel, ha a tanuló ezt kéri vagy a feladat ezt megengedi.
3. Ellenőrizd a megfigyelhető viselkedést kis, releváns tesztesetekkel.
4. Értékeld a rubrika szerint.
5. Adj egy javítandó, konkrét következő lépést.
6. Kérdezd meg a tanulót, hogy kerüljön-e tömör összesítés a `progress.json` fájlba.

## Rubrika

| Szempont | Szint | Bizonyíték |
|---|---|---|
| Helyesség | még nem teljes / részben jó / megfelelő | teszt vagy konkrét eset |
| C++20 használat | fejlesztendő / megfelelő / tudatos | kódhely |
| Olvashatóság | fejlesztendő / megfelelő / kiemelkedő | név, szerkezet, megjegyzés |
| Hibakezelés és határeset | hiányzik / részleges / megfelelő | vizsgált eset |
| Önálló indoklás | hiányzik / részleges / világos | a tanuló magyarázata |

## Kimenetek

A részletes értékelést `feedback/<feladat-azonosító>.md` fájlba mentsd. A tanulói beadandó vagy forrásfájl ne legyen automatikusan megosztva; a tanuló dönt a leadásról.
