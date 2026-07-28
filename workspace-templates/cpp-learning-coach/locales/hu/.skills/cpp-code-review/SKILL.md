---
name: cpp-code-review
description: Tanulóbarát C++20-kódreview helyességre, olvashatóságra, biztonságra, tesztelhetőségre és modern C++-gyakorlatokra fókuszálva.
---

# C++ kódreview

## Visszajelzési sorrend

1. Előbb nevezd meg, mi működik jól.
2. Javítsd a helyességi és biztonsági problémákat.
3. Ezután javasolj olvashatósági és tervezési fejlesztéseket.
4. Teljesítményről csak akkor írj, ha azt mérés vagy ismert algoritmikus ok indokolja.

## Ellenőrzőlista

- A program fordul C++20 szabvánnyal, figyelmeztetésekkel?
- A bemenet érvényesítésére és a határesetekre gondolt a szerző?
- Beszédesek a változó- és függvénynevek?
- A függvénynek egyértelmű, szűk feladata van?
- Indokolt-e a `const`, a referencia vagy az érték szerinti átadás?
- Kerülhető-e a kézi `new` / `delete` RAII-val vagy standard konténerrel?
- Elkülönül-e az üzleti logika a be- és kimenettől?

## Formátum

Minden észrevételnél jelöld a súlyosságot (`kötelező`, `javasolt`, `tanulási tipp`), a helyet, az okot és egy rövid javítási irányt. Ne írd át automatikusan az egész programot; előbb kérd meg a tanulót, hogy válasszon egy javítandó pontot.
