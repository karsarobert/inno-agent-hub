# EP_05 – szótáras árjegyzék, Inno-agent tanulói csomag

Magyar nyelvű Python-gyakorlat **2 × 45 percre**, az EP_05.html alapján, a végleges EP_04_innoagent 1.1.0 szerkezetét és tesztelési tanulságait követve. Bemutatkozó, magyarázó tutor; saját tanulói szerkesztés és futtatás, a gyakorlásban kimenetjóslás nélkül. A végén új, 10 + 10 kérdéses elméleti és kódismereti teszt következik.

## Indítás

1. A ZIP tartalmát új, üres Inno-agent munkatér **gyökerébe** bontsd ki. Ne maradjon közbeiktatott EP_05 almappa. A preset.json, agent.md és minden .py ugyanitt van.
2. A Futtatás gomb terminálja a megnyitott .py fájl mappájában álljon. Itt ez minden feladatnál a munkatér gyökere; feladatváltáskor nem kell cd.
3. Kezdő üzenet: „Kezdjük az ötödik gyakorlatot.” A tutor bemutatkozik és rögtön az A1 árkeresési feladattal kezd.
4. A tanuló megnyit, módosít, ment és futtat. A B2 interaktív kérdéseire a terminálban válaszol Enterrel. Inputra váró program mellett ne indítson új futást.

A korábbi megoldásokat ne írjuk felül ezzel a kezdőcsomaggal. A csomag nem kerül automatikusan a hubra, és nem módosít alkalmazásbeállításokat. A kártyaleírás a korábbi preset.json mezőit követi.

## A 90 perces főút

| Első 45 perc | Perc | Második 45 perc | Perc |
|---|---:|---|---:|
| A1 – Árkeresés | 8 | B2.b – Próbák és új termék | 8 |
| A2 – Ellenőrzött árfrissítés | 8 | Z1 – Önálló kódátalakítás | 10 |
| A3 – Kínálatszűrés | 8 | T1 – 10 elméleti kérdés | 10 |
| B1 – Kosárösszeg és blokk | 10 | T2 – 10 kódismereti kérdés | 15 |
| S1 – Rövid összegzés | 2 | S2 – Eredmény és lezárás | 2 |
| B2.a – Függvények összekapcsolása | 9 | | |
| **Összesen** | **45** | **Összesen** | **45** |

Ez a gyorsabban haladó csoportnak szánt, tömörített 90 perces terv; a két teszt együtt 25 perc. A szünet külön idő. A B2.a az első blokk végére kerül, a B2.b a második elejére. Az idő becslés: a szükséges próbákat nem szabad igazolás nélkül késznek nevezni. Lassabb haladásnál a félbemaradt programozás vagy teszt kimondott folytatási ponttal kerül későbbre. A tesztet sem teljesítjük kész válaszok átadásával. Az új C1–C3 és K5 bővítések tényleges időnyereség esetén, a régi K-feladatok külön választásra indulnak; nem férnek automatikusan ebbe a keretbe.

## Tartalom

- agent.md: bemutatkozás, magyarázat, kódírási és értékelési szabályok.
- tanulo_lap.md: fő feladatsor, rövid minták, saját módosítások és próbák.
- tutor_utmutato.md: feladatonkénti magyarázat és hibakeresés; adott és saját részek.
- ellenorzo_esetek.md: szükséges tesztadatok és elvárt viselkedés.
- zaro_feladatok.md: Z1 önálló átalakítás.
- teszt_elmelet.md: 10 rövid elméleti kérdés.
- teszt_kodismeret.md: 5 kimenetértelmezés és 5 hibakeresés.
- teszt_megoldokulcs.md: pontozás és magyarázat; válaszadás előtt nem mutatandó meg. A munkatérben hozzáférhető, ezért a teszt tanulási célú, nem titkos vizsga.
- bufe_bovitesek.md: C1–C3 és K5, részletes minták és ellenőrző esetek.
- tovabbi_gyakorlas.md: a régi K1, K2, K4 elmélyítések; a régi K3 helyett C1–C2.
- memoria_utmutato.md: haladás az elérhető, engedélyezett L1-ben; nincs haladas.md.
- Tíz .py: a korábbi hat és négy új, futtatható, még átalakítandó kezdőminta.
- EP_05.html: a legfrissebb offline tananyag, a 8–10. fejezet kiegészítő példáival.
- feladatok.json, verzio.json: helyi tartalmi térkép és verzióadatok, nem alkalmazáskonfiguráció.
- preset.json: kártyaleírás a korábbi csomag formájában.
- futtatas.sh: opcionális kézi tartalék, például `bash futtatas.sh arkereses.py`. Nem állítja át a felület termináljának mappáját.

## Mit alakít át a tanuló?

A minták futnak, de a követelményt még nem teljesítik. A nyers lekérdezésből egységesített keresés, ellenőrizetlen értékadásból ellenőrzött frissítés, kiíró ciklusból listát visszaadó szűrés, darabszámlálásból árösszegzés lesz. A záró feladatban önállóan kapcsolja össze a kosarat, az árjegyzéket és a feltételes számlálást.

B1 külön rövid fájl, benne nincs későbbi fizetési kód. B2-ben a régi, már tanult beviteli és fizetési segédek készen szerepelnek. A tanuló saját B1-függvényeit viszi át, majd a három jelölt kapcsolódást készíti el. A programozási feladatokhoz nincs kész célmegoldás. A záró tesztekhez külön, nyíltan elérhető értékelési segéd tartozik. A tutor a tanuló helyett nem szerkeszt és nem futtat.

A HTML telefonkönyves, termes és mérési mintái magyarázó források. A büfés feladatokhoz az adatforrást, a feltételt vagy az eredmény típusát is át kell alakítani. Az ár- és újtermék-próbák segítenek ellenőrizni, hogy az algoritmus valóban a kapott adatokat használja.

## Oktatói kipróbálás

Új munkatérben ellenőrizd a bemutatkozást, az A1 magyarázatát és azt, hogy a tutor tényleges saját szerkesztést kér. A „kész” után olvassa az aktuális kódot, és csak a hiányzó futási eredményt tisztázza. B1-nél ne kérjen pénzt; B2-nél ne másoltassa be az egész fájlt a chatbe. A Z1 végén ne jelentse teljesnek a főutat ismeretlen próbák mellett.

A memória használata a tényleges alkalmazásbeállítástól és az elérhető eszközöktől függ. Az alapul használt EP_04-csomag dokumentált feltételeit a memoria_utmutato.md őrzi; ezek történeti támpontok, nem automatikus alkalmazáskonfiguráció. Letiltott memória mellett a tutor a beszélgetésben ad folytatási pontot.

A kezdőminták és a feladatok megoldhatóságának helyi ellenőrzése nem helyettesíti az adott Inno-agent-modellel végzett élő tesztet. A tanulási út és a követelmények készültek el; a tényleges tutorviselkedés modellfüggő.


## 1.1.0 változásai

A fő programozási feladatok és a hat kezdő .py fájl változatlanok. Új a 20 kérdéses záró teszt, a megoldókulcs, a válaszadás és pontozás tutorutasítása, valamint a hozzáigazított 90 perces időterv. Az EP_05.html legutóbbi, 8–10. fejezettel bővített változata került a ZIP-be. Az 1.1.0 verzió még nem tartalmazta a C-feladatokat; az 1.2.0 már beépíti őket.


## 1.2.0 – Beépített büfébővítések

| Feladat | Kezdőfájl | Becsült idő |
|---|---|---:|
| C1 – Darabszámok szótárban | darabszamok.py | 10 perc |
| C2 – Összevont blokk, saját C1-függvénnyel | osszevont_blokk.py | 15 perc |
| C3 – Legnagyobb részösszeg | reszosszeg.py | 10 perc |
| K5 – Új árjegyzék árkorrekcióval | arkorrekcio.py | 10 perc |

C1–C2 a gyorsan végzők elsődleges bővítése. A korábbi K3 feladatot váltják ki, ezért nincs kétszeri összevontblokk-feladat. C3 összes részösszeget keres, a régi K2 egységárat; az új árkorrekció K5, hogy a meglévő K1 ne kapjon más jelentést.

Az alapút 90 perc, C1–C2-vel 115, mind a négy új feladattal 135 perc tervezett idő. A ténylegesen gyorsabban haladó tanuló a megtakarított időben végzi a bővítéseket. A tutor 27 percet tart fenn a két tesztre és lezárásra; bizonytalan időadatnál egyszer tisztázza, mennyi idő maradt. A tesztek a kiválasztott programozási feladatok után jönnek. Az összes bővítés egy 90 perces órába nem garantálható.

Az új kódfájlok megjegyzésekkel tagolt kezdőminták; kész célmegoldást nem tartalmaznak. A tutor rövid analóg mintát magyaráz, a tanuló írja meg és futtatja a saját változatot. A korábbi hat kezdőprogram, a HTML és a 20 tesztkérdés változatlan.
