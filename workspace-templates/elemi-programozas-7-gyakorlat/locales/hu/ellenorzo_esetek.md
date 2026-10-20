# EP_07 – Ellenőrző esetek

Ezek elvárt eredmények, nem elvégzett tanulói futások. A próbákat a tanuló mentés után futtatja. A tutor a kódváltozathoz és a tényleges adatállapothoz köti az ismert eredményt. A halmazok sorrendje nem követelmény; a főprogram sorted megjelenítése listát ad. Szóközök, idézőjeltípusok és egyenértékű feliratok eltérhetnek, az adatok jelentése maradjon helyes.

## A1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | Az előkészített két tétel. | Kávé: 2 db × 450 Ft = 900 Ft; szendvics: 1 db × 890 Ft = 890 Ft. Mindkét tétel külön sor. |
| A1.2 | Csak a kávé tételét állítsd erre: ("kávé", 3, 500). | Kávé részösszege 1500 Ft; szendvicsé továbbra is 890 Ft. A feldolgozó kód nem változik. |
| A1.3 | tetelek = []. | A fejléc megjelenhet; tételsor nincs, és nincs hiba. |
| A1.4 | tetelek = [("víz", 2, 0)]. | Egy sor: 2 db, 0 Ft egységár, 0 Ft részösszeg. A nulla ár itt érvényes próbaadat. |

## A2

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | Az előkészített ötelemű kosár; keresett_termek = "kávé". | A visszakapott tuple (5, 3, 3). A főprogram a három értéket jelentésének megfelelő felirattal mutatja. |
| A2.2 | Ugyanez a kosár; keresett_termek = "tea". | (5, 3, 0). Hiányzó termékből nulla van. |
| A2.3 | kosar = []; keresett_termek = "kávé". | (0, 0, 0), hiba nélkül. |
| A2.4 | kosar = ["tea", "tea", "tea"]; keresett_termek = "tea". | (3, 1, 3). Az eredeti kosár minden próbában változatlan. |

## A3

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.1 | első: ["kávé", "üdítő", "kávé"]; második: ["üdítő", "szendvics"]. | Összes: {kávé, szendvics, üdítő}; közös: {üdítő}; csak első: {kávé}; csak második: {szendvics}; pontosan egyik: {kávé, szendvics}; részhalmaz: False. |
| A3.2 | első: ["kávé", "kávé"]; második: ["kávé"]. | Összes és közös: {kávé}; mindkét irányú és szimmetrikus különbség üres; részhalmaz: True. Darabszámot itt nem ellenőrzünk. |
| A3.3 | első: []; második: ["tea"]. | Összes: {tea}; közös és csak első üres; csak második és pontosan egyik: {tea}; részhalmaz: True. |
| A3.4 | első: ["tea"]; második: []. | Összes, csak első és pontosan egyik: {tea}; közös és csak második üres; részhalmaz: False. |
| A3.5 | Mindkét kosár üres. | Mind az öt halmazeredmény üres; részhalmaz: True. A bemeneti listák mindegyik próbában változatlanok. |

## B1.a

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.a.1 | kosar = ["kávé", "üdítő"]; uj_termek = "tea". | Az eredeti ["kávé", "üdítő"]; az új ["kávé", "üdítő", "tea"]. Az is összehasonlítás False. |
| B1.a.2 | kosar = []; uj_termek = "tea". | Az eredeti []; az új ["tea"]. Két külön lista. |
| B1.a.3 | kosar = ["kávé", "kávé"]; uj_termek = "kávé". | Az eredetiben két, az újban három kávé. A sorrend és az ismétlődés megmarad. |

## B1.b

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.b.1 | Új futás: {"anna", "bela"}, név: "csilla". | True; a halmazban anna, bela és csilla. A kapott halmaz helyben módosul. |
| B1.b.2 | Ugyanazon halmazzal, újraindítás nélkül hívd még egyszer ugyanazzal a csilla névvel. | False; továbbra is három név. A meglévő bejegyzések megmaradnak. |
| B1.b.3 | Üres halmaz, név: "anna". | True; a halmaz egyetlen eleme anna. |

## Z1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | Alapárjegyzék; kosár: ["kávé", "üdítő"]. | Üres halmaz; a hívó jelzi, hogy a rendelés teljesíthető. |
| Z1.2 | Alapárjegyzék; kosár: ["kávé", "tea"]. | A hiányzó halmaz egyetlen eleme tea; a hívó a hiányt és a termék nevét mutatja. |
| Z1.3 | Alapárjegyzék; kosár: ["tea", "tea", "pizza"]. | A hiányzó halmaz elemei tea és pizza, mindkettő egyszer. |
| Z1.4 | Alapárjegyzék; üres kosár. | Üres halmaz, hiba nélkül. A program szabálya szerint teljesíthető: nincs hiányzó termék. |
| Z1.5 | A Z1.2 adataihoz futás előtt vedd fel a "tea": 350 bejegyzést az árjegyzékbe. | Üres hiányzó halmaz, teljesíthető rendelés. Csak a próbaadat változik, a függvény nem. A függvény mindegyik próbában változatlanul hagyja a bemeneteket. |

## C1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | Az előkészített két kosár és árjegyzék. | Rendezett tétel-tuple-ök: ("kávé", 2, 450, 900), ("szendvics", 1, 890, 890), ("üdítő", 2, 390, 780). Összesen 2570 Ft. |
| C1.2 | Mindkét kosár üres. | Új üres lista; nincs terméksor; összesen 0 Ft. |
| C1.3 | arak = {"tea": 350, "kakaó": 350}; első kosár ["tea", "kakaó"], második ["tea"]. | Két sor: kakaó 1 db, 350 Ft részösszeg; tea 2 db, 700 Ft részösszeg; összesen 1050 Ft. Azonos egységár miatt nem olvad össze két termék. |
| C1.4 | A C1.1 adatai; csak a kávé ára legyen 500. | Kávé részösszege 1000 Ft; a teljes összeg 2670 Ft. A kosarak és az árjegyzék minden hívás során változatlanok. |
