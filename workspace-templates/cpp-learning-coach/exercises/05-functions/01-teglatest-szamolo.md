# Téglatest-számoló függvényekkel

## Tanulási cél

Feladat bontása kis függvényekre, paraméterátadás és visszatérési érték használata.

## Előfeltétel

Változók, képletek, bemenet és kiírás.

## Feladat

Írj programot, amely három pozitív oldalhosszt kér be egy téglatesthez. Külön függvény számítsa ki:

- a térfogatot;
- a felszínt;
- azt, hogy minden oldalhossz pozitív-e.

A `main` csak a beolvasást, a függvényhívást és a kiírást végezze.

## Bemenet és kimenet

- Bemenet: `a`, `b`, `c` valós oldalhosszak.
- Kimenet: felszín és térfogat, vagy hibaüzenet.

## Utalások

- A térfogat: `a * b * c`.
- A felszín: `2 * (a*b + a*c + b*c)`.
- Válassz beszédes függvényneveket és `const` paramétereket, ha a függvény nem módosítja őket.

## Ellenőrzési szempontok

- A programban legalább három saját függvény van.
- `2, 3, 4` esetén a térfogat 24, a felszín 52.
- Nulla vagy negatív oldalhossz esetén nem számol tovább.
- A hallgató el tudja mondani, melyik adat paraméter és melyik visszatérési érték.

## Lehetséges bővítés

Írj rekurzív függvényt, amely kiszámítja egy nem negatív egész szám faktoriálisát, majd hasonlítsd össze ciklusos változattal.
