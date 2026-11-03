# EP_08 – InnoAgent tanulói csomag

Magyar nyelvű, 2 × 45 perces Python-gyakorlat az EP_08.html fájlkezelési és szövegfeldolgozási anyagához. Módszertani alap: EP_05 1.2.0 és EP_07 1.0.0. Az elméleti HTML aktuális változatát a csomag tartalmazza; a feladatok más adatot és követelményt használnak, ezért a HTML teljes mintái változtatás nélkül nem célmegoldások.

## Indítás

1. A ZIP tartalmát új, üres InnoAgent-munkatér gyökerébe bontsd ki, közbeiktatott csomagmappa nélkül. A preset.json, agent.md, .py és .txt fájlok egymás mellett legyenek. Meglévő munkát ne írj felül.
2. Kezdő üzenet: „Kezdjük a nyolcadik gyakorlatot.” A tutor bemutatkozik, ismerteti a célt, és rögtön az A1 magyarázatával kezd.
3. A tanuló megnyitja, szerkeszti, menti és a Futtatás gombbal próbálja a programot. A gomb terminálja a megnyitott program mappájában álljon. Nincs python_gyakorlat almappa, feladatonkénti cd vagy inputra váró kezdőprogram.
4. Írási futás után az eredményfájlt is megnyitja; ha nem frissült a nézet, frissíti vagy újranyitja. A tutor emlékeztet erre, különösen az eladási naplónál, ahol egy újabb futás új eladást jelentene.

A csomag helyi munkatérhez készült; nem telepít a hubra és nem változtat alkalmazásbeállítást. A preset.json az EP_07 mezőit követi. A feladatok.json és verzio.json helyi tartalmi dokumentáció, nem új alkalmazásséma.

## Az öt fő feladat

| Feladat / fájl | Mi adott? | Mi a saját munka? |
| --- | --- | --- |
| A1 / rendeles.py | Aláírás, üreslista-helykitöltő, próbahívás és fájl. | Soronkénti beolvasás, tisztítás, üres sor kihagyása; sorrendtartó, ismétlődő lista. |
| A2 / velemeny.py | Aláírás, üresszótár-helykitöltő, kulcsszóhalmaz, visszajelzések. | Kisbetűsítés, szélső írásjel-kezelés, csak a keresett szavak számlálása, hiánynál is 0. |
| A3.a/b / blokk.py | Árjegyzék és hívások; két helykitöltő. | Saját A1-definíció átvétele; tételsorok és összeg friss célfájlba, két szakaszban. |
| B1.a/b / naplo.py | Árjegyzék, kapcsoló, két aláírás és hívások. | Eseményenként név;ár rekord hozzáfűzése, majd a tárolt árak beolvasása és összesítése. |
| Z1 / onallo.py | Aláírás, (0,0), keresett érték és fájlnevek. | Paraméter szerinti termékstatisztika és a főprogramban háromsoros, friss jelentés. |
| C1 / napi_riport.py | Két aláírás és hívások. | Választható: termékenkénti (darab,bevétel) szótár, rendezett napi riport. |

Hat futtatható kezdőprogram van; nem teljesítik a célkövetelményt. Nincs kész célmegoldás vagy kitöltendő kész ciklusváz a programozási feladatokhoz. A rövid analóg minták a módszert mutatják, a saját programot a hallgató készíti. A tutor nem szerkeszt és nem futtat helyette.

## A 90 perces főút

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| START | 2 | B1.b | 6 |
| A1 | 8 | Z1 | 12 |
| A2 | 12 | T1 | 10 |
| A3.a/b | 13 | T2 | 15 |
| B1.a | 8 | S2 | 2 |
| S1 | 2 | | |
| **Összesen** | **45** | **Összesen** | **45** |

Tömörített becslés, a szünet külön idő. Lassabb haladásnál pontos, valós folytatási pont marad; nincs késznek nevezett félmegoldás. C1 15 perc, kizárólag Z1 után és T1 előtt, legalább 42 ténylegesen fennmaradó perc esetén. A tesztek és lezárás 27 perce megmarad. C1-gyel a teljes tervezett út 105 perc; 90 percbe csak gyorsabb tényleges haladással fér. Nincs automatikus további extra vagy kötelező házi.

## Bemenet, kimenet, fájlállapot

Kilenc változatlan, UTF-8 bemeneti .txt található a gyökérben; pontos tartalom és formátum: adatok.md. Az ures.txt 0 bájtos, két adatfájlból hiányzik a végső sortörés, és a rendelés üres sort/szélső szóközöket is tartalmaz. Az eladási árak tárolt történeti adatok.

A blokk.txt, eladasok.txt, termek_jelentes.txt és napi_riport.txt nincs a csomagban, saját program hozza létre. A blokk/jelentés w móddal frissül; a napló a módban gyűlik. B1.a friss munkatérben azonos naplón két futást kér. B1.b előtt a mentési kapcsolót False-ra kell állítani; az olvasási próbák változatlan fájlokkal mennek. Így a javítás ismételt futtatása nem ad hozzá véletlenül új eseményt.

## Tesztek és értékelés

A főfeladatokhoz 22 kötelező normatív próba tartozik, a C1-hez további 3. Az elvárt táblázat nem végrehajtási bizonyíték. A tutor külön kezeli a látott kódot, a látott/azonosítható futást vagy kimeneti fájlt, és a tanulói beszámolót. Az ismert próbát csak érintő változás/ellentmondás esetén ismételteti.

T1 10 MCQ (10 perc), T2 5 kódértelmezés és 5 hibakeresés (15 perc). A teljes T2 után közös értékelés: külön /10, /10, összesen /20; első önálló válasz, segítség és későbbi javítás külön. A kulcs elérhető a munkatérben, ezért gyakorló teszt, nem titkos vizsga. Nem automatikus jegy vagy elsajátítási százalék.

## Fájlok

- agent.md: teljes tutori szerep, menet, segítség, fájlállapot és lezárás.
- tanulo_lap.md: lépésenkénti tanulói munka, analógiák és egyező próbák.
- tutor_utmutato.md: adott/saját részek, hangsúlyok, diagnózis és elfogadás.
- adatok.md, ellenorzo_esetek.md: bemenetek és normatív esetek.
- zaro_feladatok.md, bovites.md: Z1 és az egyetlen választható C1.
- teszt_elmelet.md, teszt_kodismeret.md, teszt_megoldokulcs.md: 20 kérdés és értékelés.
- memoria_utmutato.md: elérhető/engedélyezett memória, ismétlésmentes folytatás.
- Hat .py kezdőprogram, kilenc .txt bemenet; EP_08.html az elméleti háttérrel.
- preset.json, feladatok.json, verzio.json: kártyaleírás, helyi tartalmi térkép és verzió.
- futtatas.sh: opcionális kézi tartalék, például bash futtatas.sh rendeles.py; a gomb munkamappáját nem állítja át.

## Oktatói kipróbálás és ellenőrzési korlát

Új munkatérben ellenőrizd a bemutatkozást, az A1 egészének és analógiájának magyarázatát, majd a saját szerkesztés kérését. A2-nél ne fogadjon el minden szót tartalmazó szótárat; A3.a-nál ne kérje előre az összesítőt; B1.a-nál a mentett fájlt vizsgálja a helykitöltő nullák helyett. B1.b előtt mondja ki a False kapcsolót. Írási futás után szükség esetén kérjen nézetfrissítést, ne új mentőfutást. Z1-hez ne adjon előre kész algoritmust.

A kezdőprogramokat, az analóg kódokat és a tesztkódok eredményét helyi Pythonban ellenőriztük. A normatív esetek megoldhatóságát külön, a csomagba nem kerülő referenciafüggvényeken is vizsgáltuk, a fájlok bájttartalmával és az ismételt futással együtt. Ez nem az aktuális InnoAgent-modellel végzett élő tutori próba és nem automatikus hub-importteszt. A párbeszéd és eszközhasználat modell-/alkalmazásfüggő.

A memória csak valóban elérhető és engedélyezett eszközzel működhet. A csomag nem készít automatikus haladas.md-t vagy eredmeny.md-t; hiba/tiltás esetén a beszélgetés őrzi a valós folytatási pontot. A tanulói eladási napló nem tutori adminisztrációs fájl.
