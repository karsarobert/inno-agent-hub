# EP_07 – Inno-agent tanulói csomag

Magyar nyelvű, 2 × 45 perces Python-gyakorlat: tuple, halmazok és tudatos függvényhasználat. Módszertani alap: a csatolt EP_05 1.2.0 csomag. A 6. alkalom egész órás ZH volt; a tananyag az EP_05 után az EP_07-tel folytatódik.

A friss EP_07.html könyvtári mintáit itt a büfé rendelési adatain alkalmazzuk. Öt fő programozási feladat, egy feltételesen választható összetett bővítés és 10+10 kérdéses záró teszt tartozik hozzá. A csomag önmagában tartalmazza a szükséges kezdőadatokat; korábbi tanulói megoldásfájlok nem szükségesek.

## Indítás

1. A ZIP tartalmát új, üres Inno-agent munkatér **gyökerébe** bontsd ki. A preset.json, agent.md és a .py fájlok egymás mellett legyenek, közbeiktatott csomagmappa nélkül. A korábbi megoldásokat ne írd felül.
2. A Futtatás gomb terminálja a megnyitott .py fájl mappájában álljon. Itt a feladatváltás nem jár mappaváltással.
3. Kezdő üzenet: „Kezdjük a hetedik gyakorlatot.” A tutor röviden bemutatkozik, majd rögtön a tetelek.py A1 feladatával kezd. Nincs külön E0 vagy köszöntőátírás.
4. A tanuló szerkeszt, ment és futtat. A példák rögzített próbaadatokat használnak, nincs input-várakozás. A tutor magyaráz, olvas és visszajelez; nem írja és nem futtatja a célmegoldást a tanuló helyett.

A csomag helyi munkatérhez készült; nem kerül automatikusan hubra, és nem állítja át az alkalmazást. A preset.json a kapott alapcsomag mezőit követi. A feladatok.json és verzio.json tartalmi leírás, nem új alkalmazásséma.

## A 90 perces főút

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| Bemutatkozás és érdemi kezdés | 2 | B1.b – Halmaz módosítása | 6 |
| A1 – Rendelési tételek tuple-ben | 8 | Z1 – Önálló rendelésellenőrzés | 12 |
| A2 – Kosárstatisztika | 10 | T1 – Elméleti teszt | 10 |
| A3 – Kosarak összehasonlítása | 15 | T2 – Kódismereti teszt | 15 |
| B1.a – Új kosár, eredeti megőrzése | 8 | S2 – Értékelés és lezárás | 2 |
| S1 – Rövid összegzés | 2 |  |  |
| **Összesen** | **45** | **Összesen** | **45** |

Az időterv tömörített becslés, a szünet külön idő. A szükséges magyarázat, szerkesztés és futtatás része a keretnek. Kész eredményt csak ismert próbák alapján állítunk. Lassabb haladásnál a félbemaradt rész pontos folytatási pontot kap, nem kész megoldást vagy megalapozatlan teljesítésjelzést.

## Mit ír a tanuló?

| Feladat / fájl | Előkészített rész | Saját érdemi munka |
| --- | --- | --- |
| A1 / tetelek.py | Tuple-öket tartalmazó lista, fejléc és kezdeti egyben-kiírás. | Saját bejárás, kicsomagolás és részösszeg-számítás. |
| A2 / kosar_adatok.py | Függvényaláírás, (0,0,0) helykitöltő, próbahívás. | Háromféle darabszám, tuple-visszatérés, kicsomagolás és feliratok. |
| A3 / kosarak.py | Eredményszótár kulcsai, üres/False helykitöltők és kész megjelenítés. | Két helyi halmaz és hat valódi eredmény; a megjelenítés adott. |
| B1 / modositas.py | Eredetit módosító listafüggvény, helykitöltő halmazfüggvény és állapotkiírások. | Új lista az eredeti megőrzésével; tudatos set-módosítás True/False jelzéssel. |
| Z1 / onallo.py | Üres halmazt visszaadó helykitöltő és kezdeti próba. | Hiányzó termékek új halmaza és eredménytől függő hívói üzenet. |
| C1 / riport.py | Kezdőadatok és helykitöltő függvények. | Saját A2 újrahasználata, két kosárból új tuple-sorok és külön riport. |

A kezdőfájlok futtathatók, de nem teljesítik a célkövetelményt. A kezdeti hibás/hiányos eredmény magyarázott fejlesztési pont. A programozási feladatokhoz nincs kész célmegoldás a csomagban. A rövid analóg kódok más helyzetet szemléltetnek, majd a hallgató alkalmazza a módszert.

## Ellenőrzés és tesztek

A próbák az ellenorzo_esetek.md és a munkalap egyező táblázataiban vannak. Normál, üres, ismétlődő és megváltoztatott adat is szerepel. B1.b.2 egyetlen futásban, ugyanazon halmaz két hívásával ellenőrizhető. A bemenetmegőrzés és a visszatérési típus is követelmény.

T1: 10 rövid elméleti kérdés, 10 perc. T2: 5 kódértelmezési és 5 hibakeresési kérdés, 15 perc. Ötös kérdéscsoportok, kérésre egyesével. Az értékelés a teljes T2 után következik; a segített és az első önálló válasz külön marad. A megoldókulcs a munkatérben elérhető, ezért a teszt tanulási célú, nem titkos vizsga. Nem automatikus érdemjegy vagy mastery-mérés.

A programozási gyakorlatban nincs kötelező kimenetjóslás. A záró T2 szándékosan külön kódértelmezési szakasz. A teszt első válaszai után javításhoz már futtathat a tanuló.

## Az egyetlen választható bővítés

C1 egy összetett, 15 percre tervezett riport. Z1 után, T1 előtt indulhat, ha ténylegesen legalább 42 perc marad, így a két teszt és lezárás 27 perce biztosított. Bizonytalan időnél a tutor egyszer tisztáz. A teljes tervezett út C1-gyel 105 perc; a 90 perces órán csak megtakarított idővel férhet bele. Nincs automatikus második extra vagy kötelező házi feladat.

## Fájlok

- agent.md: a tutor teljes tanítási, segítségadási és értékelési szabályai.
- tanulo_lap.md: a főút céljai, mintái, saját módosításai és próbái.
- tutor_utmutato.md: feladatonkénti magyarázat, diagnózis és elfogadás.
- ellenorzo_esetek.md: normatív próbák, nem elvégzett tanulói futások.
- zaro_feladatok.md: a Z1 önálló feladat.
- bovites.md: C1, az egyetlen összetett bővítés.
- teszt_elmelet.md, teszt_kodismeret.md, teszt_megoldokulcs.md: 10+10 új kérdés és pontozás.
- memoria_utmutato.md: tényleges előrehaladás és ismétlésmentes folytatás.
- Hat .py: öt fő fájl és egy C1 kezdőprogram.
- EP_07.html: a legutóbbi, 27 kódpéldás offline tananyag.
- preset.json, feladatok.json, verzio.json: kártyaleírás, tartalmi térkép és verzió.
- futtatas.sh: opcionális kézi tartalék, például bash futtatas.sh tetelek.py. A Futtatás gomb terminálját nem állítja át.

## Oktatói kipróbálás

Új munkatérben ellenőrizd a bemutatkozást, az A1 program egészének magyarázatát és azt, hogy a tutor valódi saját kódírást kér. A kész jelzés után olvassa az aktuális kódot, és csak az ismeretlen próbát tisztázza. A3-nál külön kezelje a három szakaszt, B1.a után ne hibáztassa a még helykitöltő B1.b-t. Már igazolt próbát vagy saját módosítást ne ismételtessen.

A memória csak az alkalmazásban ténylegesen elérhető és engedélyezett eszközzel működhet. A csomag nem hoz létre automatikus haladas.md-t vagy eredményfájlt. Letiltásnál a beszélgetésben marad a folytatási pont. A technikai futtatási akadály nem fogalmi hiány.

A kezdőprogramok, analóg minták, tesztkódok és a feladatok megoldhatóságának helyi ellenőrzése nem helyettesíti az adott Inno-agent-modellel végzett élő tutori próbát. A valós segítségadás és párbeszéd modellfüggő.
