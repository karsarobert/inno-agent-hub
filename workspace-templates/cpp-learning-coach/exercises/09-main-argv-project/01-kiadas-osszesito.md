# Mini-projekt: kiadásösszesítő parancssori paraméterrel

## Tanulási cél

Parancssori argumentumok feldolgozása, több korábbi fogalom integrálása és önálló programdokumentálás.

## Előfeltétel

A kurzus 1–9. alkalmainak alapfogalmai.

## Feladat

Készíts programot, amely parancssori argumentumként kap egy szövegfájlnevet. A fájl minden sorában egy nem negatív kiadás szerepel. A program:

1. ellenőrzi, hogy pontosan egy fájlnevet kapott-e;
2. megnyitja a fájlt;
3. beolvassa az értékeket egy `std::vector<double>`-be;
4. kiírja a darabszámot, összeget, átlagot, minimumot és maximumot;
5. értelmes hibakódot ad vissza hibás használat vagy megnyitási hiba esetén.

Készíts `pelda-kiadasok.txt` tesztfájlt legalább öt értékkel, és írj rövid `README.md`-t a fordításról és futtatásról.

## Bemenet és kimenet

- Futtatás: `./kiadas-osszesito pelda-kiadasok.txt`
- Kimenet: rendezett, magyar összesítés.

## Utalások

- A `main` aláírása: `int main(int argc, char* argv[])`.
- Az `argv[0]` a program neve, az első saját paraméter az `argv[1]`.
- Az összegző és szélsőérték-számítást szervezd külön függvényekbe.

## Ellenőrzési szempontok

- Paraméter nélkül a program használati útmutatót ír és nem tekinti sikeres futásnak.
- Létező, öt értékes tesztfájlra helyes összesítést ad.
- Üres fájl esetén nem oszt nullával.
- A beadás tartalmazza a forráskódot, a tesztfájlt és a rövid futtatási leírást.

## Lehetséges bővítés

Egészítsd ki egy `--csv` kapcsolóval, amely az összesítést géppel feldolgozható CSV-sorban írja ki.
