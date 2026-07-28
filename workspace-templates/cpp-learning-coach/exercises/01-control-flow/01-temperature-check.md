# Hőmérséklet-ellenőrző

## Tanulási cél

Használj `if` / `else if` / `else` szerkezetet egy számszerű bemenet kategorizálására.

## Előfeltétel

Változók, összehasonlító operátorok és `std::cin`.

## Feladat

Olvass be egy Celsius-fokban megadott hőmérsékletet. Írd ki, hogy az érték `fagy`, `hűvös`, `kellemes` vagy `meleg` kategóriába esik. Te magad határozd meg és dokumentáld a határokat.

## Utalások

- Írd fel először a kategóriák intervallumait.
- A feltételeket a legszűkebb vagy legalsó tartománytól következetesen rendezd.
- Figyelj arra, mi történik pontosan a határértékeken.

## Ellenőrzési szempontok

- Teszteld legalább egy negatív, egy határérték és egy magas hőmérséklettel.
- Minden lehetséges egész hőmérséklet pontosan egy kategóriát kap.
- A program C++20 módban figyelmeztetés nélkül fordul.

## Lehetséges bővítés

Egészítsd ki a programot egy `while` ciklussal, amely addig kér új értéket, amíg a felhasználó egy előre megadott kilépési értéket nem ad.
