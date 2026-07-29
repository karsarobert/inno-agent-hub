---
name: cpp-compile-run
description: C++20-forrás biztonságos helyi fordítása és futtatása g++-szal, érthető diagnosztikával és elkülönített buildkönyvtárral.
---

# C++ fordítás és futtatás

## Biztonsági korlátok

- Csak a jelenlegi munkatérben lévő, a tanuló által kért forrást fordítsd.
- Ne futtass hálózati, jogosultság-módosító, fájltörlő vagy korlátlan erőforrást fogyasztó programot.
- Interaktív bemenethez előre rögzített, kis tesztbemenetet használj.
- A futást korlátozd időben; végtelen ciklus gyanújánál ne futtasd újra javítás nélkül.

## Egyetlen forrásfájl

Fordítás:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic -g source.cpp -o build/program
```

Futtatás:

```bash
./build/program
```

## CMake-projekt

```bash
cmake -S starter -B build
cmake --build build
./build/cpp_learning_coach
```

## Hibamagyarázat formátuma

Minden diagnosztikához add meg:

1. **Hely** — fájl és sor.
2. **Jelentés** — mit jelez a fordító közérthetően.
3. **Ok** — a C++ szabály vagy a kódbeli eltérés.
4. **Legkisebb javítás** — ne írj át fölösleges részeket.
5. **Megelőzés** — egy rövid szabály vagy ellenőrzési kérdés.

Sikeres futáskor hasonlítsd össze a tényleges és várt kimenetet. A tanulót kérd meg, hogy magyarázza meg az eredményt, mielőtt következő feladatra tértek.
