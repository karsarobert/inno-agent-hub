# CPP_07 projekt – Érvényes mérési adatok elemzője

Egyetlen fájlt építünk tovább: **P07_meresek.cpp**. A starterben adott a Datum
és Meres típus, valamint hat mérés. A feldolgozó függvényeket, prototípusokat
és hívásokat te készíted el.

| Azonosító | Érték | Érvényes? | Dátum |
|---|---:|---|---|
| 101 | 18.5 | igen | 2026.10.17. |
| 102 | 26.0 | nem | 2026.10.17. |
| 103 | 21.0 | igen | 2026.10.17. |
| 104 | -2.0 | igen | 2026.10.17. |
| 105 | 30.5 | igen | 2026.10.17. |
| 106 | 21.0 | igen | 2026.10.17. |

A negatív érték is érvényes hőmérséklet lehet. Az érvényességet a külön
jelzőből olvassuk ki, nem az előjelből vagy a küszöbből vezetjük le.

## Munkamód és szerkezet

Minden lépés előtt Inno rövid, teljes analóg mintát magyaráz el. Utána te
alkalmazod az elvet. Egyszerre csak az aktuális rész készül.
A fájl sorrendje: típusok → prototípusok → main → függvénydefiníciók.
A main szervez; a részfeladatokat külön függvények végzik. A küszöb és az
elemszám maradjon a main helyi változója; szükség szerint add át őket.

## P1 – Egy mérés kiírása beágyazott dátummal

**Minta:** M6. Irányadó idő: 7 perc.

A `rogzitve` mező teljes Datum érték. Két egymást követő pont két szinten
választ mezőt. Készíts `meresKiirasa` void függvényt: egy mérést kapjon érték
szerint, és írja ki az azonosítót, értéket, érvényességet és a dátum három részét.
Hívd meg a tömb egy kiválasztott mérésével. Nem kell beolvasást készíteni.

Ellenőrzés az első mérésnél: 101, 18.5, igaz, 2026.10.17.
A formázás szabad; logikai `1` és szöveges „igen” egyaránt elfogadható.

## P2 – A teljes adatsor kiírása

**Minta:** M7. Irányadó idő: 6 perc.

Készíts `meresekKiirasa` függvényt, amely olvasható mérésekre mutató mutatót
és elemszámot kap. Ciklussal járja be a tömböt; minden elemnél a P1 kiíróját
hívja meg. A main a teljes adatsort kiíró függvényt hívja.

Ellenőrzés: hat rekord, az eredeti sorrendben, az érvénytelen is látszik.
A const-os mutatón keresztül nem módosítjuk az elemeket. A mutató nem árulja
el az elemszámot; ezért külön paraméter szükséges.

## P3 – Az érvényes mérések száma

**Minta:** M8, de most csak az érvényességi feltételt kell alkalmazni.
Irányadó idő: 6 perc.

Készíts `ervenyesDarab` függvényt: olvasható méréseket és elemszámot kapjon,
és az érvényes rekordok számával térjen vissza. A 102-es azonosítójú rekordot
ne számítsa bele, a -2.0 értékű érvényes rekordot viszont igen.

Ellenőrzés: 5.

## P4 – Az érvényes mérések átlaga

**Minta:** M9; használd a P3 eredményét is. Irányadó idő: 9 perc.

Készíts double eredményű `ervenyesAtlag` függvényt. Csak az érvényes rekordok
értékét összegezze; a nevező az érvényes darabszám legyen. A darabszámhoz
használd az `ervenyesDarab` függvényt, ne írd meg újra a számlálást.

Előfeltétel: legalább egy érvényes mérés van. A main ezt ellenőrizze hívás
előtt; ha nincs, ne hívja meg az átlagfüggvényt, hanem írjon érthető üzenetet.
Ne legyen nullával osztás és kitalált átlagérték.

Ellenőrzés: az érvényes összeg 89, az átlag 17.8.
Próbaképpen állítsd az összes jelzőt hamisra, és ellenőrizd a nincs-érvényes-mérés
ágat. Frissen fordíts. Ezután állítsd vissza az eredeti adatokat, és azokkal folytasd.

## P5 – Érvényes és szigorúan küszöb feletti

**Minta:** M8; csak az új különbséget kell ismét magyarázni. Irányadó idő: 7 perc.

Készíts `kuszobFelettiDarab` függvényt: méréseket, elemszámot és double küszöböt
kapjon. Csak az a rekord számítson, amely érvényes ÉS értéke **szigorúan nagyobb**
a küszöbnél. Ugyanazt a függvényt hívd 20-as és 21-es küszöbbel is.

Ellenőrzés: 20-nál 3, 21-nél 1. A küszöbbel egyenlő nem számít; az érvénytelen
26.0-s rekord egyik esetben sem számít.

## P6 – Eredeti mérés módosítása mutatóval

**Minta:** M3. Irányadó idő: 10 perc.

Készíts `ertekNovelese` void függvényt módosítható mérésre mutató mutatóval és
double növekménnyel. Csak a megmutatott mérés értékét növelje. Az azonosító,
érvényesség és dátum ne változzon.

Előfeltétel: a mutató létező mérésre mutat. A main az első tömbelem címét és 2.0
növekményt adjon át. Ne készíts második tömböt: az eredeti rekord változását
kell megfigyelni. Hívd újra a kiíró, átlagoló és számláló függvényeket.

Ellenőrzés: első érték 20.5; érvényes darabszám 5; átlag 18.2;
20 feletti érvényes darabszám 4; 21 feletti érvényes darabszám továbbra is 1.
Az első rekord azonosítója és dátuma változatlan.

## Projektzárás

Röviden magyarázd el: melyik függvény kap másolatot, melyik olvassa a tömböt,
melyik módosít eredeti rekordot? Miért külön adat az érvényesség?
Ez működésmagyarázat, nem új program és nem új kimenetjóslás.
