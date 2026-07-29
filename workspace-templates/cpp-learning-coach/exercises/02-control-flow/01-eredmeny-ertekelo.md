# Eredményértékelő

## Tanulási cél

`if` / `else if` / `else` lánc és számlálós `for` ciklus használata világos feltételekkel.

## Előfeltétel

Változók, aritmetikai operátorok és billentyűzetes bemenet használata.

## Feladat

A program kérjen be egy 0 és 100 közötti pontszámot. Írja ki az értékelést:

- 0–49: `elégtelen`
- 50–62: `elégséges`
- 63–75: `közepes`
- 76–88: `jó`
- 89–100: `jeles`

A tartományon kívüli értékre írjon hibajelzést. Ezután egy `for` ciklussal írd ki az összes határértéket és a hozzá tartozó kategóriát.

## Bemenet és kimenet

- Bemenet: egy egész pontszám.
- Kimenet: egyetlen magyar értékelés vagy `Hibás pontszám`.

## Utalások

- A hibás érték ellenőrzése legyen a legelső döntés.
- A feltételek sorrendje számít.
- Írd le tesztesetként a 49, 50, 62, 63, 88, 89, 100 és 101 értékeket.

## Ellenőrzési szempontok

- Minden határérték a megfelelő kategóriába kerül.
- A kód nem keveri össze az `=` értékadást és a `==` összehasonlítást.
- A ciklus nem végtelen és minden felsorolt tesztértéket feldolgoz.

## Lehetséges bővítés

Kérj be addig pontszámokat, amíg a felhasználó `-1` értéket nem ad. Számold ki az érvényes pontszámok átlagát.
