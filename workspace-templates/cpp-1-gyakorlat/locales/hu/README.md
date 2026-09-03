# C++ alapok – hallgatói gyakorló munkaterület

Ez a munkaterület a **„C++ alapok”** tananyaghoz készült önálló gyakorlótér
(4 × 45 perces lecke). Itt a kódokat **te magad** írod be, fordítod és futtatod.

## ⚠️ Legfontosabb tudnivaló a használathoz

- **A gyökérben dolgozzunk:** minden `.cpp` fájlt **ennek a munkaterületnek a gyökerébe** hozzunk létre (ne almappákba). Így egyből tudod futtatni, és az elérési út mindig egyszerű.
- **Használd a munkaterület alatti terminált:** a képernyőalján (vagy a jobb oldalon) található **Terminal** ablakban dolgozzunk — ott futtatjuk a `g++`-t. Minden leckénél megadom, hogy pontosan milyen paranccsal kell fordítani és futtatni.
- **Fordítás előtt mentsd a fájlt** (Ctrl+S), különben a régi verziót fordítod le.

## A leckék

| Fájl | Lecke | Mit gyakorolunk |
|------|-------|-----------------|
| `L01_elso_program.cpp` | 1. lecke | Első program, fordítás–futtatás **megfigyelése** (adott kód) |
| `L02_preprocesszor_makro.cpp` | 2. lecke | `#include`, `#define` makrók, `-E` kapcsoló |
| `L03_felteteles_makro.cpp` | 3. lecke | `#ifdef/#else/#endif`, `-D`, include guard, paraméteres makró |
| `L04_io_string_hibakes.cpp` | 4. lecke | `cin`/`cout`, `std::string`, konverzió, `assert` |

## A futtatás általános módja (g++)

```
g++ -Wall -o program neved_fajlod.cpp
./program
```

> Ha a munkaterület alatti terminálban vagy, és a fájl a gyökérben van, ez így működik — nem kell elérési utat írni.

Felkészülés a leckékre az óraterv alapján: `01..04_*.md` a tanári anyagban.
