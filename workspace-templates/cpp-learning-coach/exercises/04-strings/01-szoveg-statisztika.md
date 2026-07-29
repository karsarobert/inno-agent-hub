# Szövegstatisztika

## Tanulási cél

`std::string`, `std::getline`, karakterenkénti bejárás és egyszerű szövegfeldolgozás.

## Előfeltétel

Ciklusok, feltételek és változók használata.

## Feladat

Olvass be egy teljes sort `std::getline` segítségével. Számold meg benne:

- az összes karaktert;
- a szóközöket;
- az angol ábécé kisbetűit és nagybetűit külön.

A program végül írja ki, hogy a beolvasott szöveg üres-e.

## Bemenet és kimenet

- Bemenet: egy teljes szövegsor, szóközökkel együtt.
- Kimenet: négy számláló és az ürességre vonatkozó jelzés.

## Utalások

- `std::getline(std::cin, szoveg)` a szóközöket is beolvassa.
- Használj range-based `for (char ch : szoveg)` ciklust.
- A betűvizsgálathoz biztonságosan használhatod a `<cctype>` eszközeit.

## Ellenőrzési szempontok

- A `Hello világ 2026` bemenetben a szóközök száma 2.
- Üres sor esetén nem omlik össze a program.
- A program nem tesz feltételezést a szöveg maximális hosszáról.

## Lehetséges bővítés

Készíts második függvényt, amely a szöveget megfordítva adja vissza. Beszéljétek meg, hogy ez még nem azonos a palindromvizsgálattal.
