# EP_04 – szövegek és élő kosár, Inno-agent tanulói csomag

Magyar nyelvű Python-gyakorlat **2 × 45 percre**, az EP_04.html alapján és a végleges EP_03_innoagent 1.0.1 szerkezetét követve. Bemutatkozó, magyarázó tutor; rövid minták; saját tanulói kódírás, mentés és futtatás. Nincsenek jóslási feladatok.

## Indítás

1. A ZIP **tartalmát** új, üres Inno-agent munkatér gyökerébe bontsd ki. Ne maradjon közbeiktatott EP_04 almappa. Az agent.md, preset.json és a .py fájlok ugyanebben a gyökérben legyenek.
2. A Futtatás gombhoz a felület terminálja is ebben a mappában álljon. Minden .py itt van, ezért a feladatok között nincs mappaváltás. Ha korábban máshová léptettétek a terminált, a tényleges útvonal alapján térjetek vissza a munkatérbe.
3. Kezdő üzenet: „Kezdjük a negyedik gyakorlatot.” A tutor bemutatkozik, ismerteti a célt és rögtön a T1 szövegegységesítési feladattal indul.
4. A tanuló szerkeszt, ment és a Futtatás gombbal futtat. Inputra váró programnak a terminálban válaszol Enterrel.

A régi EP_03 tanulói megoldásokat ne írjuk felül. Ez új teljes munkatér, nem egy korábbi megoldáson automatikusan futtatandó javítás. A kártyaleírás mellé nem kerültek kitalált terminál- vagy memóriakonfigurációs kulcsok. A csomag nem töltődik fel automatikusan a hubra.

## Mi fér a 90 percbe?

| Első blokk | Perc | Második blokk | Perc |
|---|---:|---|---:|
| T1: szöveg egységesítése | 9 | B1: élő kosár, két belső lépés | 18 |
| T2: index és szelet | 7 | B2: fizetési kapcsolódás, két belső lépés | 12 |
| T3: karakterbejárás | 7 | Z1: önálló törlés név szerint | 12 |
| L1: listaműveletek | 9 | S2: lezárás | 3 |
| L2: split/join és szűrés | 10 | | |
| S1: összegzés | 3 | | |
| **Összesen** | **45** | **Összesen** | **45** |

A szünet külön idő. A keret a magyarázatot, kódírást és próbákat is tartalmazza. Ha lassabb a haladás, a pluszpróbák és K-részek kimaradnak; szükség esetén B2 összeépítése folytatásra maradhat. A tutor megőrzi a valós folytatási pontot, és nem nevezi késznek a hiányzó részt. A teljes HTML minden példája nem része a 90 perces főútnak.

## A fájlok szerepe

- agent.md: a tutor bemutatkozása, tanítási ritmusa, kódírási és értékelési szabályai.
- tanulo_lap.md: a fő feladatsor, minták és elvárt viselkedés.
- tutor_utmutato.md: feladatonkénti tanítási és hibakeresési támpontok.
- ellenorzo_esetek.md: tervezett próbák; nem előre igazolt eredmények.
- zaro_feladatok.md: Z1 önálló kódírás és saját próbahívások.
- tovabbi_gyakorlas.md: K1–K6 opcionális elmélyítés, nem házi feladat.
- memoria_utmutato.md: tanulási események az elérhető, engedélyezett L1 memóriában; nincs automatikus haladas.md.
- Nyolc .py: futtatható, hiányos kezdőminták. A 0 / [] / False törzsek nem végleges megoldások.
- EP_04.html: változatlan részletes tananyag, színezett kódokkal, bemutatókkal. A referenciakódok nem bemásolandó gyakorlati megoldások.
- feladatok.json és verzio.json: helyi tartalmi metaadatok; nem alkalmazáskonfiguráció.
- preset.json: az EP_03 formáját követő kártyaleírás.
- futtatas.sh: opcionális kézi futtatási segéd, például `bash futtatas.sh szoveg.py`. A segéd a saját munkakönyvtárát állítja be; a felület terminálját nem.

## Az élő kosár és a fizetés elkülönül

B1 a kosar_04.py fájlban fut. Csak terméket és vezérlőszót kér, majd kiírja a kész kosarat. B2 a bufe_04.py fájlban kerül elő. A tanuló ide viszi át saját két függvényét, átalakítja az egyszeri igen/nem mintát, majd kitölti a főprogram négy jelölt kezdőértékét és hozzáad egy fizetési hívást. A korábbi ár- és fizetési függvények készen rendelkezésre állnak. Nem kell az EP_03 teljes programját újragépelni.

## Oktatói ellenőrzés az első használat előtt

Új munkatérben próbáld ki a „kezdjük” üzenetet. A tutor mutatkozzon be és adjon saját szerkesztést; a működő indulást ne váltsa környezetvizsgára. Már a T1 kezdésekor ellenőrizd, hogy érdemi magyarázatot ad, de nem írja a tanuló helyett a függvényt. Egy „kész” jelzés után az aktuális kódot olvassa, ne ismételje meg az előző feladatot. B1-nél még ne kérjen pénzt. A tényleges tutorviselkedés az alkalmazásban használt modelltől is függ.

A memória beállítása oktatói feladat. Az EP_03 mintacsomag készítésekor ellenőrzött változatban kikapcsolt Simple Mode és engedélyezett L1 szükséges. Mindig a ténylegesen elérhető eszköz és sikerjelzés alapján használjuk; a csomag nem állítja át automatikusan. Kikapcsolt memória esetén a tanítás folytatható, a folytatási pont a beszélgetésben marad.

## Tartalmi alap

EP_04.html: sztringek, listametódusok, kosárépítés és büfés összekapcsolás; részletes források a HTML végén. Szerkezeti alap: EP_03_innoagent.zip 1.0.1, a külön blokkfeladatra és a tanuló saját kódírására épülő végleges csomag. A korábbi tesztelés tanulságai alapján hangsúlyos a teljes kimenet ellenőrzése, az üres kosár helyes kezelési sorrendje és a segítség pontos megnevezése.

## 1.1.0 – a kipróbálás alapján

- Kimaradt a köszöntés átírása; a bemutatkozás után rögtön T1 következik. A keret továbbra is 45 + 45 perc.
- B1-ben kész, futtatható ciklusvázat alakít át a tanuló. B2-ben kész szerkezetben dolgozik: nem kell újragépelni a főprogramot. A vázak szándékosan még nem teljesítik a végső követelményeket.
- Z1 megmaradt rövid önálló alkalmazásnak, így külön is látható, mi megy előkészített szerkezet nélkül.
- A tutor pontosabb feladatkövetési, visszajelzési és lezárási szabályokat kapott. A teljes fájl bemásoltatása és a már kész lépések ismétlése kerülendő.
- Az EP_04.html változatlan. A tanulói feladatok konkrét menetét az aktualizált tanulo_lap.md adja.

A ZIP új kezdőcsomag. Már kitöltött tanulói munkatérbe ne bontsd rá, mert a kezdőminták felülírhatnák a megoldásokat. Folyamatban lévő munkánál csak az útmutatókat frissítsd, a Python-fájlokból pedig a szükséges vázat külön mutasd meg.
