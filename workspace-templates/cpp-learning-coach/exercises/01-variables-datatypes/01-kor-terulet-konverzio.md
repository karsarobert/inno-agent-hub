# Hőmérséklet-átváltó és pontos kiírás

## Tanulási cél

Egész és lebegőpontos típus kiválasztása, beolvasás, aritmetikai művelet és értelmes formázott kiírás.

## Előfeltétel

Az 1. alkalom programvázának és a `std::cin`/`std::cout` alapjainak ismerete.

## Feladat

Írj programot, amely Celsius-fokban beolvas egy hőmérsékletet, majd Fahrenheitben kiírja az eredményt a következő képlet szerint:

`fahrenheit = celsius * 9 / 5 + 32`

A kimenet két tizedesjegyet mutasson. Ezután próbáld ki az 0, 20 és -40 bemenetekkel.

## Bemenet és kimenet

- Bemenet: egy valós szám Celsius-fokban.
- Kimenet például: `20.00 C = 68.00 F`.

## Utalások

- Miért nem `int` típusú a Celsius és Fahrenheit változó?
- A `9.0 / 5.0` más eredményt adhat, mint a csak egész számokkal végzett osztás.
- A tizedesjegyekhez keresd meg a `<iomanip>` és `std::setprecision` használatát.

## Ellenőrzési szempontok

- A program `double` vagy `float` típust használ a hőmérséklethez.
- `0` bemenetre 32 F jelenik meg.
- `-40` bemenetre -40 F jelenik meg.
- A hallgató meg tudja indokolni, miért nem biztonságos minden számításhoz ugyanazt a típust választani.

## Lehetséges bővítés

Írd ki azt is, hogy a víz a hétköznapi légköri nyomáson várhatóan jég, folyadék vagy gőz állapotú-e. A feltételeket csak a következő alkalom után valósítsd meg.
