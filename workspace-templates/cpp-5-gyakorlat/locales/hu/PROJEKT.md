# CPP_05 projekt – Mérési adatok elemzője

A második 45 perces blokkban egyetlen programot fejlesztesz tovább:

`P05_meresi_adatok.cpp`

A kiinduló program hat mérési értéket tartalmaz:

```text
18, 24, 11, 29, 21, 17
```

A cél nem az, hogy minden számítást a `main()` végezzen. A programot kisebb,
névvel ellátott függvényekre bontjuk. Minden új rész előtt Inno mutat egy rövid,
hasonló mintakódot más változónevekkel, majd neked kell azt a projektre alkalmaznod.

## P1 – Adatok kiírása

Készíts `void` függvényt, amely megkapja a mérési tömb első elemének címét és az
elemszámot, majd ciklussal kiírja az összes mérést.

A projekten belül használd a prototípus → hívás → definíció szerkezetet.

## P2 – Összeg

Készíts függvényt, amely végigjárja a tömböt és visszaadja a mérési értékek összegét.
A `main()` csak hívja meg és írja ki az eredményt.

## P3 – Átlag

Készíts `double` eredményű függvényt az átlaghoz. Ne másold be újra az összegző
ciklust: az átlagfüggvény használja fel a P2-ben elkészített saját összegző függvényt.
Ügyelj arra, hogy az osztás ne veszítse el a tört részt.

## P4 – Maximum

Készíts függvényt, amely visszaadja a legnagyobb mérési értéket. Feltételezheted,
hogy a tömb nem üres.

## P5 – Küszöb feletti értékek száma

Készíts függvényt három paraméterrel: a mérési adatok, az elemszám és egy küszöb.
A függvény adja vissza, hány mérés **szigorúan nagyobb** a küszöbnél.

Elsőként használd a `riasztasiKuszob` kezdeti, 20-as értékét.

## P6 – Korábbi mutatós tudás alkalmazása

Készíts `void` függvényt, amely egy egész változó címét kapja és 1-gyel megnöveli
az ott tárolt értéket. Hívd meg a `riasztasiKuszob` címével. Ezután ismét használd
a P5 függvényét az új küszöbértékkel.

## P7 – `<cmath>` a projektben

Készíts két `double` paramétert fogadó `tavolsag` függvényt. A függvény az origótól
mért euklideszi távolságot számolja ki:

```text
gyök(x*x + y*y)
```

A négyzetgyököt a `<cmath>` könyvtár `sqrt` függvényével számítsd. A kiinduló
koordináták 3.0 és 4.0.

## Várt ellenőrző eredmények

Ha minden rész elkészült, ezekkel az értékekkel ellenőrizheted a programodat:

- összeg: `120`
- átlag: `20`
- maximum: `29`
- 20-nál nagyobb mérések száma: `3`
- a küszöb növelés után: `21`
- 21-nél nagyobb mérések száma: `2`
- a mérőállomás távolsága az origótól: `5`

A pontos kiírás formátuma eltérhet; a számított értékeknek kell egyezniük.
