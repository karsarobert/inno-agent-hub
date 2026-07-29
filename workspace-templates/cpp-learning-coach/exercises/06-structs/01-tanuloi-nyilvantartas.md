# Tanulói nyilvántartás struktúrákkal

## Tanulási cél

Összetartozó adatok `struct` típusban való tárolása és `std::vector` használata.

## Előfeltétel

`std::string`, vektorok, ciklusok és függvények alapjai.

## Feladat

Hozz létre `Tanulo` struktúrát a következő tagokkal:

- `nev` (`std::string`);
- `azonosito` (`int`);
- `pontszam` (`int`).

Olvass be három tanulót egy vektorba. Készíts függvényt, amely megkeresi és visszaadja a legmagasabb pontszámú tanuló indexét. A `main` írja ki a nevét és pontszámát.

## Bemenet és kimenet

- Bemenet: három név, azonosító és 0–100 közötti pontszám.
- Kimenet: a legjobb eredményű tanuló neve és pontszáma.

## Utalások

- A struktúra tagjaihoz pont operátorral férsz hozzá: `tanulo.nev`.
- A kereső függvény üres vektorra is adjon egyértelmű választ vagy kapjon nem üres vektort előfeltételként.
- Ne tárolj valódi személyes adatot a példában; használj fiktív neveket.

## Ellenőrzési szempontok

- A program külön `Tanulo` típust használ.
- A legmagasabb pontszámot helyesen keresi meg.
- Azonos legjobb eredmény esetén a választott szabály dokumentált.
- A hallgató meg tudja indokolni, miért jobb a kapcsolódó adatokat egy struktúrában tárolni.

## Lehetséges bővítés

A pontszám alapján készíts értékelő függvényt, és minden tanulóhoz írd ki a szöveges minősítést.
