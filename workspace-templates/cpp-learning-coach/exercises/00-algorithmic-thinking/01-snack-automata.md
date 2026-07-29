# Uzsonnaautomata: algoritmusból C++ program

## Tanulási cél

A feladat megfogalmazása, bemenet–feldolgozás–kimenet bontása, majd az algoritmus C++20-programmá alakítása.

## Előfeltétel

Nincs. Ismerd meg a `main`, a `std::cout` és a `std::cin` szerepét az órán.

## Feladat

Tervezd meg pszeudokóddal, majd írd meg azt a programot, amely bekéri egy uzsonna árát és a fizetett összeget. A program írja ki a visszajáró összeget.

Előbb írj legalább három lépésből álló pszeudokódot. Csak utána kezdd el a C++-kódot.

## Bemenet és kimenet

- Bemenet: két nem negatív egész szám, `ar` és `fizetett`.
- Kimenet: `Visszajáró: X Ft`.
- Kezdetben feltételezheted, hogy a fizetett összeg legalább az ár.

## Utalások

- A program kiindulópontja: `int main() { ... }`.
- A változó deklarációja és értékadása külön lépés.
- A visszajáró: fizetett összeg mínusz ár.

## Ellenőrzési szempontok

- A pszeudokód tartalmazza a bemenetet, a számítást és a kiírást.
- A kód C++20-ban fordul.
- `ar=650`, `fizetett=1000` esetén a kimenet 350 Ft-ot jelez.
- A hallgató el tudja mondani, miért a `main`-ből indul a program.

## Lehetséges bővítés

Jelezd külön üzenettel, ha a fizetett összeg kisebb az árnál. Ezt még csak tervezd meg pszeudokódban; a feltételt a 3. alkalmon valósítsd meg.
