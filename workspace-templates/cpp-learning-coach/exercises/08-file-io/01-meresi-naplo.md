# Mérési napló mentése fájlba

## Tanulási cél

Szövegfájl megnyitása, ellenőrzése, írása és visszaolvasása C++ stream-ekkel.

## Előfeltétel

Függvények, `std::string`, ciklusok és alapvető hibakezelés.

## Feladat

Írj programot, amely három hőmérsékletértéket kér be, majd soronként elmenti őket `meresek.txt` fájlba. Ezután zárja le, nyissa meg olvasásra, és számolja ki a mentett értékek átlagát.

A fájl megnyitásának sikertelenségét kezeld hibaüzenettel.

## Bemenet és kimenet

- Bemenet: három valós hőmérséklet.
- Fájl: `meresek.txt`, soronként egy érték.
- Kimenet: a visszaolvasott értékek átlaga.

## Utalások

- Íráshoz `std::ofstream`, olvasáshoz `std::ifstream` használható.
- Minden megnyitás után ellenőrizd a stream állapotát.
- Az olvasási ciklust a sikeres beolvasás vezérelje, ne a fájl vége előzetes vizsgálata.

## Ellenőrzési szempontok

- A fájl létrejön és három sor adatot tartalmaz.
- A program a fájlból olvassa vissza az átlaghoz szükséges értékeket.
- Hibás megnyitás esetén érthető hibaüzenetet ad.
- A hallgató meg tudja különböztetni a szövegfájlt és a bináris fájlt.

## Lehetséges bővítés

Mentsd a méréseket a 6. alkalom függvényével formázottan, majd készíts opcionális bináris mentést is.
