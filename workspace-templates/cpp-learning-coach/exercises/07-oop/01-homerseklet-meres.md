# Hőmérsékletmérés osztállyal

## Tanulási cél

Osztály, privát adat, publikus metódus, konstruktor és egyszerű érvényességvizsgálat használata.

## Előfeltétel

Struktúrák, függvények és feltételek.

## Feladat

Készíts `HomersekletMeres` osztályt. Privát tagja legyen a Celsius-fok. A konstruktor kapjon Celsius-értéket. Készíts publikus metódusokat:

- `celsius()` – visszaadja az értéket;
- `fahrenheit()` – átváltja Fahrenheitre;
- `allapot()` – `jég`, `folyadék` vagy `gőz` szöveget ad vissza egyszerű határértékekkel.

A `main` hozzon létre két példányt és írja ki mindkettő állapotát.

## Bemenet és kimenet

- Kezdetben a hőmérsékletek lehetnek a programban rögzítettek.
- Kimenet: Celsius, Fahrenheit és az állapot szövegesen.

## Utalások

- Osztályban az adatok alapértelmezetten privátak.
- A nem módosító lekérdező metódusok legyenek `const` metódusok.
- A konstruktor neve azonos az osztály nevével, nincs visszatérési típusa.

## Ellenőrzési szempontok

- A Celsius-adat nem írható közvetlenül a `main`-ből.
- `0` Celsiusra a Fahrenheit érték 32.
- A metódusok felelőssége elkülönül.
- A hallgató elmagyarázza az adatrejtés célját.

## Lehetséges bővítés

Készíts származtatott osztályt, amely a méréshez helyszínnevet is tárol, és saját formátumban írja ki az adatot.
