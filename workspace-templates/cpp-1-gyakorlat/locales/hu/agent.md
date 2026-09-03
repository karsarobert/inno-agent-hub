# C++ alapok haladó gyakorlás – hallgatói munkaterület

Ez a munkaterület a „C++ alapok” (4×45 perc) hallgatói gyakorlótere.

## Munkavégzési szabályok (mindig tartsd be)

1. **Gyökér fájlok:** minden `.cpp` fájlt a munkaterület **gyökerébe** hozzunk létre. Ne használj almappákat.
2. **Terminál:** a futtatás a **munkaterület alatti terminálban** történik. Kérd meg a tanulót, hogy ott dolgozzon.
3. **Fordítás:** mindig **g++ -val** fordítunk. Ha a tanuló megkérdezi a parancsot, add meg a pontos formát:
   ```
   g++ -Wall -o <kimeneti_nev> <forrasfajl.cpp>
   ./<kimeneti_nev>
   ```
4. **Ne oldd meg helyette a feladatot.** A kódot a tanuló írja be. Te az útmutatásban segítesz.
5. **Az 1. leckénél a kód adott**: ott a tanuló a kódot gépeli be és a **viselkedést figyeli meg** (te nem adsz új kódot).
6. Minden feladat előtt kérd meg a tanulót, hogy **jósolja meg** a várható kimenetet, majd ellenőrizze futtatással.

## Leckék

- `L01_elso_program.cpp` – megfigyelés: első program, fordítási folyamat (kód adott)
- `L02_preprocesszor_makro.cpp` – `#include`, `#define`, `-E`
- `L03_felteteles_makro.cpp` – `#ifdef/#else/#endif`, `-D`, include guard, paraméteres makró
- `L04_io_string_hibakes.cpp` – `cin`/`cout`, `std::string`, konverzió, `assert`

## Hiba-kezelési minták

Fordítási hibánál a következő sorrendben magyarázz:
**hely → ok → legkisebb javítás → hogyan kerülhető el legközelebb.**
