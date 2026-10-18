# X1 – Egyetlen kiegészítés gyors haladás esetére

Csak akkor adható, ha a kötelező kódolás mért nettó ideje 90 perc alatti, és
a teszt megtartásával legalább 15 perc marad. Ismeretlen időnél ne feltételezz
gyors haladást. Az extra_assigned állapotot egyszer állítsd igazra; második extra nincs.

## Napi összesítés struktúrában

Ugyanabban a projektben készíts `Osszesites` típust és függvényt, amely a
keresett dátumhoz tartozó érvényes mérések darabszámát, legkisebb és legnagyobb
értékét adja vissza egyetlen struktúrában. Külön logikai mező jelezze, van-e találat.

A függvény olvasható mérésekre mutató mutatót, elemszámot és keresett dátumot
kapjon. Az évnek, hónapnak és napnak is egyeznie kell. A minimumot és maximumot
az első megfelelő értékből indítsd; ne feltételezd, hogy az értékek pozitívak.
Ha nincs találat, a hívó ezt jelezze, és ne írjon ki hamis minimumot/maximumot.

Ellenőrzés a P6 utáni adatokkal:
- 2026.10.17.: 5 találat, minimum -2.0, maximum 30.5.
- 2026.10.18.: nincs találat; a jelző hamis, a darabszám 0.

Ezután a rögzített teszt következik, nem újabb feladatsor.
