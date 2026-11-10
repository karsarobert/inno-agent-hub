# EP_09 – InnoAgent tanulói csomag

Magyar nyelvű, 2 × 45 perces Python-gyakorlat az EP_09.html kivételkezelési anyagához. Módszertani alap: EP_08/EP_07 és az EP_05 magyarázó, saját kódírásra építő menete. Az aktuális HTML a csomagban van; a büfés adatok és üzleti követelmények eltérnek a HTML mérési/kölcsönzési példáitól. Változtatás nélküli másolás nem célmegoldás.

## Indítás

1. A ZIP tartalmát új, üres InnoAgent-munkatér gyökerébe bontsd ki, közbeiktatott csomagmappa nélkül. A preset.json, agent.md, .py és .txt fájlok egymás mellett legyenek. Korábbi megoldást ne írj felül.
2. Kezdő üzenet: „Kezdjük a kilencedik gyakorlatot.” A tutor röviden bemutatkozik, ismerteti a célt, és az A1 magyarázatával rögtön érdemi munkát kér.
3. A tanuló szerkeszt, ment és a Futtatás gombbal futtat. A gomb terminálja a megnyitott program mappájában álljon; a relatív adatnevek a munkamappához viszonyulnak. Nincs python_gyakorlat almappa vagy feladatonkénti cd.
4. A1 megírása után inputra vár a program, a válaszokat a terminálba kell írni. A többi kezdőprogram rögzített próbaadatokkal dolgozik. Írás után a valódi célfájlt is meg kell nyitni, szükség esetén frissített nézettel.

Helyi munkatéri csomag: nem telepít a hubra, nem változtat alkalmazásbeállítást. A preset mezői a korábbi csomagot követik. A feladatok.json és verzio.json helyi tartalmi dokumentáció, nem új importséma. Korábbi hallgatói megoldásfájl nem szükséges.

## Öt fő feladat, hat kezdőprogram

| Feladat / fájl | Adott | Saját érdemi munka |
| --- | --- | --- |
| A1 / fizetes.py | Aláírás, return 0, fizetendő és próbahívás. | Egész összeg újrakérése; elégtelen önálló felajánlás elutasítása, megfelelő érték visszaadása. |
| A2 / tetel.py | Aláírás, árjegyzék és próbaadat. | ValueError az ismeretlen termék/nem pozitív darab miatt; rendes összeg, hívói kezelés. |
| A3.a/b / naplo.py | Két aláírás, helykitöltők és hívások. | Hárommezős rekord validálása, majd soronkénti feldolgozás sorszámos hibalistával. |
| B1 / riport.py | Két helykitöltő A3-definíció, kész összesítő és kész mentő. | Saját A3 átvétele, fájlszintű hibakezelés és összekapcsolás; főprogram finally lezárás. |
| Z1 / onallo.py | A2/Z1 helykitöltők és próbakosár. | Saját A2 átvétele; minden tételhiba gyűjtése, hibás kosárhoz None, részfizetés tiltása. |
| C1 / mentes.py | Két korábbi helykitöltő és mentőaláírás. | Választható: saját A2/Z1 átvétele, hozzáfűzés csak teljes validáció után. |

A hat kezdőprogram fut, de nem teljesíti a követelményt. Nincs kész A1–C1 célmegoldás vagy kitöltendő kész célciklus. A riport két előkészített segítője tudatosan adott támogatás: használatukat meg kell érteni, újraírásuk nem feladat. Az analógiák rövid, más helyzetben működő minták; a tanuló maga alakítja a saját programját.

## A 90 perces főút

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| START | 2 | B1 | 6 |
| A1 | 8 | Z1 | 12 |
| A2 | 10 | T1 | 10 |
| A3.a | 9 | T2 | 15 |
| A3.b | 14 | S2 | 2 |
| S1 | 2 | | |
| **Összesen** | **45** | **Összesen** | **45** |

Ez tömörített becslés, nem hallgatókkal mért idő. Magyarázat, szerkesztés és próba is része, szünet külön. Lassabb haladásnál pontos folytatási pont, nem kész megoldás vagy megalapozatlan teljesítésjelzés. C1 15 perc, Z1 után/T1 előtt, legalább 42 ténylegesen fennmaradó perccel. A tesztek és lezárás 27 perce megmarad. C1-gyel a teljes tervezett út 105 perc; 90-be csak gyorsabb tényleges haladással fér. Nincs automatikus második extra vagy házi.

## Adatok és döntések

Öt változatlan UTF-8 bemenet; pontos tartalmuk az adatok.md-ben. A termék;darab;egységár rekord nem az EP_08 kétmezős adata. Jó alap: 4 rekord, 7 darab, 1750 Ft. A 0 egységár valós adat, a 0 darab tiltott. A fizikai üres sor külön kategória, a hibás nem üres sor sorszámos hibát ad. A fájl hiánya nem válhat sikeres üres beolvasássá.

B1 jelzett részleges riportot készíthet jó naplósorokból. Z1 más szabályt kér: hibás kosárnál semmilyen részösszeg nem fizethető. C1 csak az egész kosár ellenőrzése után nyithatja a naplót. Az adatellenőrzési sorrend nem atomi I/O-mentés: írási hiba után a cél lehet hiányos.

A bufe_jelentes.txt és opcionális uj_eladasok.txt nincs a ZIP-ben, a saját program hozza létre. Hiányzó forrás után a régi jelentés megmaradhat, de nem új sikeres eredmény. C1 ismételt futása új hozzáfűzés; nézetfrissítés helyett ne indíts felesleges új mentést. A forrásokat nem kell javítani/felülírni.

## Próbák és tesztek

27 főúti normatív próbaazonosító, C1-hez további 4. Néhány azonosító több rövid alpróbát foglal össze. A3.b.5 a B1.2 ismert viselkedésével is igazolható, azonos saját beolvasó esetén. Az elvárás nem végrehajtási bizonyíték. Az aktuális kód, az azonosítható futás/fájl és a tanulói beszámoló külön marad; ismert próbát csak érintő változás/ellentmondás esetén ismételünk.

T1: 10 MCQ, 10 perc. T2: 5 kódértelmezés és 5 hibakeresés, 15 perc. A teljes T2 után közös pontozás: /10, /10, /20, segítség és későbbi javítás külön. A kulcs a munkatérben van: tanulási célú teszt, nem titkos vizsga. Nem automatikus jegy vagy elsajátítási százalék.

## Fájlok

- agent.md: tutori szerep, tanítás, segítség, bizonyíték és lezárás.
- tanulo_lap.md: teljes célok, adott/saját részek, analógiák, lépések és próbák.
- tutor_utmutato.md: magyarázati hangsúly, diagnózis, szakaszhatárok.
- adatok.md és ellenorzo_esetek.md: pontos bemenet és normatív ellenőrzés.
- zaro_feladatok.md és bovites.md: önálló Z1 és egyetlen választható C1.
- teszt_elmelet.md, teszt_kodismeret.md, teszt_megoldokulcs.md: 20 új kérdés és értékelés.
- memoria_utmutato.md: engedélyezett memória és ismétlésmentes folytatás.
- Hat .py, öt .txt; aktuális EP_09.html.
- preset.json, feladatok.json, verzio.json: kártya, helyi feladattérkép és verzió.
- futtatas.sh: opcionális kézi tartalék, például bash futtatas.sh fizetes.py. A felületi Futtatás gomb mappáját nem állítja át.
- ellenorzesi_jelentes.md: a helyi ellenőrzés köre és korlátja.

## Oktatói próba és korlát

Próbáld ki új munkatérben a bemutatkozást, a teljes A1-cél és az analóg minta magyarázatát, a saját szerkesztés kérését és a terminál-input helyes kezelését. A2-nél a 0 ár elfogadott; A3.a alatt a még helykitöltő beolvasó nem hiba. B1 hiányzó forrás után nem nyúl a célhoz, a finally-t nem nevezi sikernek. Z1 elején nem ad kész algoritmust és nem enged részfizetést. Írás után emlékeztet a nézetfrissítésre és a céltartalom vizsgálatára.

A kezdőprogramokat, rövid analógiákat, tesztkódokat és normatív elvárásokat helyi Pythonban ellenőriztük, külön referencia-megoldásokkal és valós fájlműveletekkel is. A referencia-megoldások nem kerültek a ZIP-be. Ez nem élő InnoAgent-párbeszéd vagy az aktuális hub-import automatizált tesztje. A tutori viselkedés a választott modelltől, alkalmazástól és eszközöktől is függ.

A memória csak valóban elérhető és engedélyezett eszközzel működhet. A csomag nem hoz létre automatikus haladas.md-t vagy eredmeny.md-t. Hiba/tiltás után a beszélgetésben marad a valódi folytatási pont; a jelentés és üzleti napló nem tutori adminisztrációs fájl.
