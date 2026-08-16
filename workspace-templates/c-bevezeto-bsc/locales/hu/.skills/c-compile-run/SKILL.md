---
name: c-compile-run
description: C17-forrás biztonságos helyi fordítása és futtatása gcc-vel, érthető diagnosztikával.
---

# C fordítás és futtatás

## Biztonsági korlátok

- Csak a jelenlegi munkatérben lévő, a hallgató által kért forrást fordítsd.
- Ne futtass hálózati, jogosultság-módosító, fájltörlő vagy korlátlan erőforrást fogyasztó programot.
- Interaktív bemenethez előre rögzített, kis tesztbemenetet használj.
- A futást korlátozd időben; végtelen ciklus gyanújánál ne futtasd újra javítás nélkül.

## Egyetlen forrásfájl

Fordítás:

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -g forras.c -o build/program
```

Futtatás:

```bash
./build/program
```

## Hibamagyarázat formátuma

Minden diagnosztikához add meg:

1. **Hely** — fájl és sor.
2. **Jelentés** — mit jelez a fordító közérthetően.
3. **Ok** — a C szabály vagy a kódbeli eltérés.
4. **Legkisebb javítás** — ne írj át fölösleges részeket.
5. **Megelőzés** — egy rövid szabály vagy ellenőrzési kérdés.

Sikeres futáskor hasonlítsd össze a tényleges és várt kimenetet. A hallgatót kérd meg, hogy magyarázza meg az eredményt, mielőtt következő feladatra tértek.
