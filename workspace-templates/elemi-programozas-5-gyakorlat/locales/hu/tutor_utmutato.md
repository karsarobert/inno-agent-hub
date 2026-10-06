# EP_05 – tutorútmutató

Belső tanítási támpont, nem felolvasandó adminisztráció. A tanuló kész, de a célt még nem teljesítő kis programokat alakít át. A feladat és a HTML példája között tudatos eltérés van. Az új fájl egészének bemutatása után a változó adatra, feltételre és visszatérési értékre irányítsd a figyelmet.

A főút 45 + 45 tervezett perc. A feladatsor első lépése rögtön A1; nincs külön köszöntőátírás. A B1 és B2 külön fájl marad, hogy a későbbi fizetés ne terhelje a korai összegzést. A részletes viselkedési szabályokat az agent.md tartalmazza.

## A1 – Árkeresés egységesített névvel

**Fájl:** arkereses.py. **Keret:** 8 perc.

**Nagy kép:** A termék nevét egységesíted, és megkülönbözteted az ismert árat a hiányzó terméktől.

**Magyarázd el:** A szótár kulcsa a terméknév, értéke az ár. A get hiányzó kulcsnál None-t ad; ez nem 0 és nem a "None" szöveg. Az arat_keres már lekérdez, de még a nyers nevet használja. A hívó rész egyelőre magyarázat nélkül írja ki az eredményt. A számot visszaadó keresés és az üzenet megjelenítése külön feladat.

**Segítség és hibakeresés:** A None hiányjelzés, az is None vizsgálat új: magyarázd meg a minta alapján. Ne készíttess felesleges kulcsellenőrzést a get mellé. Az ékezeteket a lower nem pótolja. A minta hívó elágazását átalakíthatja; ez még nem a függvény és főprogram teljes kész megoldása.

**Elfogadás:** A függvény a paraméter szövegét egységesíti, és a paraméter árjegyzékből kérdez le. Hiány és 0 nem keveredik: a hívó None-t vizsgál, nem az ár igazságértékét. Az árjegyzék változatlan; a függvény visszaad, a hívó kiír.

## A2 – Meglévő ár ellenőrzött frissítése

**Fájl:** arfrissites.py. **Keret:** 8 perc.

**Nagy kép:** Csak létező termék pozitív egész próbaárát írod át, és jelzed, hogy megtörtént-e a módosítás.

**Magyarázd el:** A kezdőminta minden kulcsot beállít: új kulcsot is felvesz, és hibás árat is elfogad. Ezt ellenőrzött frissítéssé alakítod. A szótár paraméterként átadása nem készít másolatot, ezért a függvény a hívó szótárát módosítja. A frissítés eredménye logikai érték, nem az új ár.

**Segítség és hibakeresés:** A példában az értékadás lehet hozzáadás vagy módosítás; a feladatban csak módosítás megengedett. Most egész számként adjuk az uj_ar próbákat: nincs szükség típusellenőrzésre vagy try/exceptre. A 0 elutasítása itt feladatszabály; nem mond ellent annak, hogy A1 keresőként érvényes 0-t is visszaadhat.

**Elfogadás:** Csak meglévő kulcs pozitív egész próbaárát módosítja. Elutasításkor nem hoz létre új kulcsot, és a régi árat sem írja felül. Egységesít és True/False értéket ad vissza; nem printtel jelzi a függvény eredményét.

## A3 – Megfizethető termékek listája

**Fájl:** kinalat.py. **Keret:** 8 perc.

**Nagy kép:** A kiíró bejárásból szűrő függvényt alakítasz: új listát kapsz a keretből megfizethető terméknevekkel.

**Magyarázd el:** A kezdő függvény már items() segítségével bejárja a párokat, de minden terméket kiír, és nincs hasznos visszatérési értéke. A két ciklusváltozó a kulcsot és az árat kapja. A te feladatod a feltétel és az új eredménylista hozzáadása. A keretbe pontosan beleférő termék is megfelelő.

**Segítség és hibakeresés:** Fejtsd ki, hogy a név és érték egy párból érkezik. A mintához képest nemcsak változónevet cserélünk: megfordul a feltétel iránya, és kiírás helyett visszaadott lista készül. Az üres eredmény kezdő lista, nem a függvény sikertelenségét jelző None.

**Elfogadás:** A keret paramétert használja, <= feltétellel; a határértéket is elfogadja. Új listát épít nevekkel, a return a teljes bejárás után van. Nincs kiírás a függvényben és nem változtatja az arak szótárat.

## B1 – Kosárból összeg, fizetés nélkül

**Fájl:** osszegzes.py. **Keret:** 10 perc.

**Nagy kép:** A kosár minden tételéhez árat keresel, és a darabszámot számoló kezdőmintát pénzösszegzéssé alakítod.

**Magyarázd el:** A kosár a feldolgozandó terméknevek listája. Az árjegyzék névhez árat rendel. A kezdő kosar_osszege még minden tétel után csak 1-et ad hozzá: tehát most darabot számol, nem forintot. A blokkot_mutat egyelőre csak a termékneveket írja. Ebben a fájlban kizárólag rögzített kosár és számítás van, nincs input és fizetés.

**Segítség és hibakeresés:** Egy összetartozó változtatás az összegzés és a blokk adatforrásának módosítása. Ne diktáld a teljes ciklust. Előfeltétel: minden kosártétel érvényes árjegyzékkulcs. Ezért a közvetlen lekérdezés helyes; ne javasolj get(termek, 0)-t, és ne add feladatul ismeretlen nevű kosár csendes feldolgozását. A későbbi B2 bekérő ezt az előfeltételt biztosítja.

**Elfogadás:** A kosár listáját járja be, nem az összes kínált terméket. Az árat a paraméter szótárból kéri, nincs beégetett árlánc vagy visszatérés az első körben. Ismétlődő termék minden alkalommal számít; üres kosárra 0. A blokk az adott árjegyzékből mutat árat; ebben a fájlban nincs fizetés.

## S1 – Rövid összegzés

**Fájl:** beszélgetés. **Keret:** 2 perc.

**Nagy kép:** Röviden összekapcsolod a lista, a szótár és a függvény szerepét.

**Magyarázd el:** A kosár kiválasztja, mit számolunk; az árjegyzék megadja az árat. A számoló függvény visszaad, a blokkfüggvény megjelenít.

**Segítség és hibakeresés:** Ne kérj új programot vagy ismétlő vizsgát. A 45 perc tervezett idő, nem mért adat; a szünet ezen kívül van.

**Elfogadás:** Valós folytatási pont; részleges válasz esetén rövid pontosítás.

## B2 – A szótáras árjegyzék bekapcsolása a büfébe

**Fájl:** bufe_05.py. **Keret:** 17 perc.

**Nagy kép:** A saját számoló és blokkfüggvényt összekapcsolod a korábbi, előkészített kosárbekéréssel és fizetéssel.

**Magyarázd el:** A fájl első része az EP_04-ből ismert kész segédkód: szövegegységesítés, kosárbekérés, igen/nem bekérés, kedvezmény és pénzpótlás. Ezeket most nem kell újragépelni. A kosarat_beker kinalat paraméteréhez szótárat is adhatunk: az in és a bejárás annak kulcsait használja. A főprogram végén az üres és nem üres ág készen van, de a kosár és összeg kezdőértékei még nem kapcsolódnak a saját függvényeidhez.

**Segítség és hibakeresés:** A teljes fájl helyett a másolás helyét és a jelölt főprogramot olvasd célzottan. Az előre adott segédfüggvényeket csak releváns hiba esetén nézd részletesen. Ne követelj egész fájlos chatbemásolást. B2.a 9 perc, B2.b 8 perc próbákkal együtt. Az árjegyzék csak futás előtt változik: menet közbeni árváltozás nem mai követelmény. A számoló és blokkoló függvények saját munkák, a fizetési algoritmus most előkészített.

**Elfogadás:** Az árjegyzék az egyetlen kézzel karbantartott kínálati és áradat a bufe_05.py-ban. Saját B1-függvényeket hív, mindkettőnek átadja az árjegyzéket. Az ürességet a kosár alapján ellenőrzi; üres kosárnál nincs diákkérdés vagy pénzkérdés. Ismeretlen és üres bevitel nem kerül a kosárba; a mégse biztonságosan visszavon. Az új ár és termék megjelenik a blokkban és a számításban. A pénzpótlás előtt nincs visszajárós sor.

## Z1 – Önálló átalakítás: drága tételek száma

**Fájl:** onallo.py. **Keret:** 10 perc.

**Nagy kép:** A kosár olyan tételeit számolod, amelyek ára szigorúan nagyobb a megadott határnál.

**Magyarázd el:** A kezdő függvény a teljes kosár hosszát adja, ezért még nem válogat ár alapján. Az új eredmény egész darabszám legyen. A kétszer vásárolt szendvics két tételnek számít. A forrás a kosár; az összehasonlítandó ár a paraméter szótárból jön.

**Segítség és hibakeresés:** Első próbálkozásra csak a feladatszabályt és az adatokat add, ne add át a kész számláló algoritmust. Az EP_05 HTML mérési példája analóg segítségként felidézhető valódi elakadásnál: a tanulónak hozzá kell kapcsolnia a név szerinti árkeresést és a függvényes visszatérést. A starter próbahívása előre adott; az önállóság a függvény átalakítására és a tesztadatok alkalmazására vonatkozik.

**Elfogadás:** Saját feltételes számláló ciklust ír a kosárra, az árakat a paraméter szótárból olvassa. Szigorúan >, nem >=; ismétlődések is külön tételként számítanak. Üres listára 0; nincs input, print vagy bemenetmódosítás a függvényben.

## Új büfébővítések: C1 → C2 → C3, valamint K5

A C1 és C2 a gyorsan végzők elsőként választandó, összetartozó bővítése. C1-ben a tanuló új szótárat épít a kosárból, C2-ben a darabszámokat az árjegyzékkel kapcsolja össze. C3 a legnagyobb részösszeget keresi; K5 új árjegyzéket készít az eredeti módosítása nélkül. A részletes feladat, analóg minta és próba a bufe_bovitesek.md fájlban van. Ne kérd újra a teljes büfé megírását.

Az alapút tervezett ideje továbbra is 90 perc, ebből a T1–T2 teszt 25 perc, S2 2 perc. Z1 után, a tesztek előtt a ténylegesen fennmaradó idő alapján válassz bővítést. Ha a két teszt és lezárás 27 percén felül legalább 25 perc marad, indítsd C1-et, majd C2-t. Ha ezen felül is marad 10 perc, jöhet C3; újabb 10 percben K5. Ha csak 10–24 szabad perc van a tesztekre fenntartott időn felül, C1 önmagában is elvégezhető, C2 kimondott folytatási ponttal marad későbbre. Előbb mindig a függőséget teljesítsd. Minden bővítés végén az aktuálisan hátralévő idővel számolj; ha a tervezettnél tovább tartott, a következő bővítést halaszd el, ne a tesztek idejét vedd el.

A gyorsaságot tényleges időadat vagy tanulói közlés alapján állapítsd meg, ne az üzenetek számából. Ha nincs időadat, egyszer kérdezd meg: „A két záró tesztre körülbelül 25 perc kell. Mennyi időnk maradt még?” Ha a tanuló az összes bővítést kéri, haladjatok C1 → C2 → C3 → K5 sorrendben, és mondd ki, hogy a teljes tervezett út 135 perc. Az alapút C1–C2-vel 115 perc. A gyorsabb tényleges haladás rövidítheti ezt; kezdőknél nem garantált a 90 perc.

A tesztek mindig a kiválasztott programozási feladatok után következnek: Z1 → [kiválasztott bővítések] → T1 → T2 → S2. A T1–T2 kérdései változatlanok, nem vizsgáztatnak a ki nem választott bővítésekből. Ne nyiss új programozási feladatot a tesztek két része között vagy az óra lezárása után automatikusan.

Minden új fájlnál előbb mondd el 2–4 mondatban a teljes célt, az adott részeket és a tanuló feladatát. Utána magyarázd el a rövid analóg mintát. Csak egy összetartozó szerkesztést kérj egyszerre. C2 külön két lépés: saját C1-definíció és számoló függvény; ezután a blokk sorainak kibővítése. A tanuló ír, ment és futtat; a tutor nem szerkeszti és nem futtatja helyette a kódot.

Az analóg mintát mutathatod, de ne alakítsd át kész célmegoldássá. A saját C1-definíció átvétele rendben van; a főprogram és a próbaadatok átvétele nem kell. Késznek csak az elfogadási pontok és az ismert próbaeredmények alapján nevezd a feladatot. A kért, de még ismeretlen határesetet egy rövid kérdéssel tisztázd; korábbi igazolt próbát ne ismételtess.

A korábbi K3 összevontblokk-feladat helyét C1–C2 veszi át, ezért K3-at ne add új feladatként. K1 és K2 meglévő azonosítója megmarad; az új árkorrekció neve K5. C3 összes részösszeget vizsgál, K2 viszont egységárat: a kettőt ne keverd össze.

## Kötelező záró tesztek: T1 és T2

Z1 után még ne zárd le az órát: előbb az idő alapján kiválasztott bővítések, majd T1 → T2 → S2 következik. T1 a teszt_elmelet.md 10 kérdése (10 perc), T2 a teszt_kodismeret.md 10 kérdése (15 perc). A teszt_megoldokulcs.md csak az értékeléshez való. Minden kérdést az eredeti azonosítóval és változatlan kóddal adj; a B2-ben átírt árak nem írják felül a teszt saját adatait.

1. Röviden mondd el, hogy a tanuló előbb önállóan válaszol, aztán közösen megbeszélitek. Nincs szükség új fájl szerkesztésére. A tesztben kimenetértelmezés is van; ez szándékos kivétel a programozási gyakorlatok jóslásmentes menete alól.
2. Alapértelmezetten öt kérdést küldj egyszerre: E1–E5, E6–E10, KÓD1–KÓD5, KÓD6–KÓD10. Kódkérdésnél a teljes rövid kódot mutasd. Kérésre egyesével is haladhattok. Várd meg a konkrét válaszokat; a „kész” vagy „minden jó” nem tesztválasz.
3. A válaszokat fogadd, de a helyességet és a megoldást a teljes T2 válaszaiig ne áruld el: a korábbi magyarázatok más kérdésre is súgnának. Egyértelműen mondd: „Megkaptam a válaszaidat, az értékelés a két rész után következik.” Ha hiányzik azonosító, csak azt pontosítsd. Ne mondd közben, hogy helyes.
4. Kérésre segíts, de a még meg nem válaszolt érintett kérdéseket támogatottnak jelöld; ne számítsd a segítséggel kialakult választ önálló teljesítménynek. Ne futtass a tanuló helyett a teszt során sem.
5. A 20 válasz (vagy kimondott kihagyás) után értékelj a kulcs alapján. Add meg külön a T1 /10, T2 /10 és összesen /20 eredményt, és jelezd a támogatott vagy kihagyott kérdéseket. Ne találj ki választ, futást vagy megértést.
6. A hibás és részleges válaszoknál a konkrét félreértést magyarázd el, majd kérj rövid javítást. A tanuló most futtathat is. A hibátlan válaszokat ne magyarázd újra hosszan. A részletes pótlás időigénye szükség szerint külön folytatás.
7. Az eredményt és az utolsó megválaszolt azonosítót a beszélgetésben, illetve engedélyezett L1-ben őrizd a memoria_utmutato.md szerint. Ne írj eredmény.md-t vagy új naplófájlt, és ne módosítsd a kérdéslapokat. A pontszám nem automatikus mastery-érték vagy érdemjegy.

A végső lezárásban a programozási feladatok állapotát és a tesztek eredményét külön mondd ki. Ha Z1 kész, de T1/T2 még nem, csak a programozási rész készült el. Részleges vagy elhalasztott tesztet ne minősíts sikeresen teljesítettnek.

## S2 – Lezárás és folytatási pont

**Fájl:** beszélgetés. **Keret:** 2 perc.

**Nagy kép:** Összefoglalod, hogyan függ össze a kosár, az árjegyzék és a saját függvényed.

**Magyarázd el:** A feladatokban különböző eredmény készült: ár vagy None, módosítási sikerjelzés, új lista, pénzösszeg és darabszám. Ezeket az eredmények jelentése különbözteti meg.

**Segítség és hibakeresés:** Ha a Z1-ben csak egy próba ismert, tisztázd a maradékot, vagy nevezd részlegesnek. A végső fájlban nem kell minden korábbi próba egyszerre szerepeljen; a korábbi ismert futást vedd figyelembe.

**Elfogadás:** Nincs megalapozatlan teljesítésállítás; a segítség és a saját átalakítás megnevezése pontos. Az óra vége egyértelmű; nincs automatikusan indított kötelező pluszfeladat vagy házi feladat.

## Mi előkészített, és mi saját munka?

| Fájl | Adott minta | A tanuló érdemi módosítása |
|---|---|---|
| arkereses.py | get lekérdezés, egy próbahívás | Egységesítés, None szerinti megjelenítés. |
| arfrissites.py | Ellenőrizetlen értékadás | Kulcs- és árkorlát, egységesítés, sikertelen eredmény. |
| kinalat.py | items bejárás és kiírás | <= feltétel, eredménylista, függvényes visszatérés. |
| osszegzes.py | Számláló ciklus és névlista kiírása | Kulcsalapú árkeresés és összegzés, ár a blokkban. |
| bufe_05.py | Régi beviteli/fizetési segédek és főprogramszerkezet | Saját B1-definíciók újrahasználata, három kapcsolódás és új adatok alkalmazása. |
| onallo.py | len alapú kezdőfüggvény, egy próbahívás | Saját feltételes számlálás árjegyzék alapján, határesetek kipróbálása. |

A kód több helyen már elindul és nyomtat valamit, de ettől még nem kész. A1 nyers nevet keres; A2 mindent beír; A3 None-t is nyomtat; B1 darabot ír ki Ft-ként; B2 még üres kosárral zár; Z1 minden elemet számol. Ezek előre megnevezett fejlesztési pontok. Ne javítsd át őket automatikusan a tanuló helyett.

## A korábbi tesztelésből megtartott szabályok

- Egy aktív feladatot adj; ha eredményt vársz, ne kezdj egyúttal a következőbe.
- A már kész módosítást és már közölt tesztet ne kérd újra.
- A teljes fájl bemásolása helyett olvass célzottan; hozzáférés hiányában kérj kis részletet.
- A kiírás jelentése is számít: ismeretlen termékre ne legyen másik termékről szóló hamis üzenet.
- Az aktuális fájlban nem látható régi próba attól még megtörténhetett. Nézd a beszélgetés eredményeit; csak a valóban ismeretlen esetet kérdezd.
- A teljes főút sikerét ne állítsd, ha a záró feladatnak csak az üres esete ismert.
- A technikai Run/útvonalhibát ne fogalmi hiányként könyveld el.
