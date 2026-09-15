# EP_02 – tanítási terv a magyarázó tutorhoz

A feladat előtt a munkalap megfelelő részét és a tanuló tényleges fájlját olvasd. A teljes útvonalat ez a csomag határozza meg: a HTML jóslási felszólításait nem vesszük át. A minták tanításra valók; a kijelölt kódot a tanuló szerkeszti. Ez az útmutató nem felolvasandó tanulói szöveg és nem teljes megoldókulcs.

## A két óra súlypontja

Az első 45 percben a függvény adatot kap, eredményt ad vissza, és másik függvényre épül. A másodikban a visszaadott értéket feltétel szabályozza, majd a saját részprogramokból összeáll a büfé. Egy feladathoz csak annyi új nyelvi eszközt adj, amennyi a következő szerkesztéshez kell. A helyi neveket F2-nél röviden értelmezzük, de nem nyitunk külön globálisváltozó-témakört.

A percértékek tervezési keretek. A szünetet nem számoljuk bele. Ha a tényleges időt nem látod, ne mondd biztosan, hogy „még 12 perc van”; az oktató vagy a tanuló jelzése alapján alkalmazkodj. Az órablokk végén egyetlen rövid időre vonatkozó kérdés megengedett, ha a folytatásról kell dönteni, de ne kérdezz minden feladatnál órát.

| Első óra | Keret | Második óra | Keret |
|---|---:|---|---:|
| E0 | 5 | D1 | 12 |
| F1 | 10 | D2 | 7 |
| F2 | 15 | B2 | 16 |
| B1 | 12 | Z1 | 7 |
| S1 | 3 | S2 | 3 |

Késéskor D2 áttehető a folytatásba, így 7 perc szabadulhat fel a korábbi alapokra vagy a B2-re. Ez ne legyen csendes „teljesítés”: a kategorizálást későbbre tettként rögzítsd. Ha még így sem fér bele, a ténylegesen elkészült programrészt zárd le, és jelöld a következő lépést. Nem kell a tanuló helyett beírni a hiányzó kódot, hogy papíron meglegyen a teljes program.

## E0 – működő, mentett fájl a megfelelő terminálból

A bemutatkozás és tartalmi áttekintés után mondd el az E0 célját. A tanuló nyissa meg és mentse a megfelelő `.py` fájlt, majd használja a Run gombot. Ne kérj előzetes belépést a `python_gyakorlat` mappába, és ne indíts kötelező `pwd`/`ls` vizsgálattal: a gomb munkatérrelatív útvonalat ad a programhoz. A gomb ugyanahhoz a `.py` fájlhoz tartozzon, amelyet a tanuló mentett.

Először egy ismert print-szöveget módosít a tanuló; a def szerkezet részletes tárgyalását F1-re hagyjuk. Ez nem új ismeretből kért vizsga. Az átírt mondat tényleges megjelenése egyszerre ellenőrzi a mentést és a célfájlt.

**Hiba esetén:** régi üzenet → mentés/aktív fájl; file not found → a gomb által indított útvonal és szükség esetén `pwd`/`ls`; python hiányzik → helyi Python 3-parancs ellenőrzése; inputot váró terminál → a kérdésre kell válaszolni. A tesztben a Run `python python_gyakorlat/koszontes.py` parancsot adott, miközben a korábbi tutorutasítás miatt a terminál már a gyakorlómappában állt. Ez a kettőzés oka; nem kézzel elrontott tanulói parancs. Ha a terminál igazoltan a munkatér közvetlen `python_gyakorlat` almappájában áll, `cd ..`, majd újabb Run a helyreállítás. A saját eszközöd könyvtárváltása nem mozgatja a tanuló terminálját. Kézi tartalék a munkatér gyökeréből: `python3 python_gyakorlat/koszontes.py`, más fájlnál annak tényleges nevével.

## F1 – függvénydefiníció, paraméter, hívás

**Egész feladat:** egy köszöntő műveletet szeretnénk több vendégre használni. A minta már működik, a tanuló az adatátadást írja hozzá.

**Magyarázat:** a def létrehoz, a zárójeles hívás végrehajt. A paraméter neve a törzsben a híváskor adott értéket jelöli. A behúzás a blokk határa. A munkalap termékes mikropéldájában soronként mutasd meg a kapcsolatot, nem kell kimenetet kérdésként kitaláltatni.

**Első kérés:** „Alakítsd át a koszont függvényt úgy, hogy egy nevet kapjon, és a kapott nevet írja a köszöntésbe. Annával próbáld ki, mentés után a Futtatás gombbal.” Ha ez még sok, külön a fejléc és a kiírás módosítását vezesd, de ne szerkeszd te a fájlt.

**Következő kis lépés:** a második névvel írt hívás. Ellenőrizd, hogy nem született két, eltérő névre beégetett függvény.

**Gyakori hibák:** zárójel nélküli név nem hívás; a fejléc új paramétere után a régi adat nélküli hívás hibázik; az f-stringből kihagyott f a kapcsos zárójeles nevet írhatja ki. A konkrét okot magyarázd, ne ismételtesd öncélúan az egész feladatot.

**Átvezetés:** az adatátadás már működik; most egy függvény eredményét szeretnénk tovább használni.

## F2 – return, print és a hívó változója

**Egész feladat:** a termék árát később a rendelés összesítéséhez is fel akarjuk használni. A terminálra írt szám ehhez nem elég, vissza kell kerülnie a hívóhoz.

**Közös magyarázat:** a téglalapos mintán kövesd a konkrét értékeket: 4 és 5 → helyi terulet = 20 → return → külső eredmeny = 20 → print. Ez magyarázat, nem tanulói előrejelzés. Az eredményt megmutathatod.

**Szerkesztési sorrend:** először a szám visszaadása és a függvény átnevezése; utána a hívó oldali értékadás és a kiírás; végül második adatpár. Az alapeset után a következő próba legyen új adatokkal végzett alkalmazás, ne ugyanannak az eredménynek újraküldése.

**Értékelés:** a `tetel_ara` paraméterekből számoljon, ne legyen benne print vagy input. A kiírásra szánt `koszont`-ban a print helyes volt; ne tanítsd, hogy minden függvényből tilos kiírni. Az itt elvárt visszatérés oka a további számítás.

**Ha None jelenik meg:** olvasd a függvényt. Van-e return? A print kifejezését adja-e vissza? Nem az elnevezés a baj. A print visszatérési értéke None; a szorzatot kell visszaadni. Rövid utalás után, ha szükséges, mutass egy konkrét sort másik szorzásos példán. A saját fájl javítását a tanuló végezze el.

**Helyi név:** a függvény belső neve és a hívó külső neve nem kell azonos legyen. A függvénybe írt `osszeg` későbbi, külső használata NameError-t okozhat; a visszaadott értéket kell egy külső névhez rendelni. Ne indíts külön global-os kitérőt.

## B1 – a már ismert büfé átszervezése

**Egész fájl először:** név + két darabszám bekérése → a két termék részösszege → rendelés összege → kiírás. A kód most még függvények nélkül végzi a számítást, ez az induló állapot, nem tanulói hiba.

**Kapcsolat:** F2-ben egy tétel árát neveztük meg. Most a két tételből álló rendelés összesítését nevezzük meg. A munkalap két egymást hívó függvényének mintáját magyarázd el, utána a tanuló a saját kódját alkalmazza.

**Lépések:** saját tetel_ara definíció átvitele → rendeles_osszege megírása helyi árakkal és két részszámítással → a régi három számoló sor leváltása a hívással. Mindig az elkészült rész után lépj tovább. A meghatározott árak átkerülnek az összesítő függvénybe; a mostani kis programnál nincs szükség globális beállításra vagy új konfigurációfájlra.

**Ne kérd:** a teljes bufe_02.py törlését és a HTML teljes kész megoldásának beillesztését. Ezzel éppen a tanuló önálló függvényírása maradna el.

**Ellenőrzés:** Anna 2/1 → 1790; Béla 3/2 → 3130. A kiírás egyezése mellett a tényleges függvényhívásokat és a paraméterek használatát is nézd meg. Fogadd el a más nevű, de egyértelmű megfelelő változókat. Az árakat a főprogramból véletlenül olvasó rejtett függőség helyett segíts a helyi adatok használatában.

## S1 – nem új feladat, hanem rendezett folytatási pont

Röviden foglald össze: adat átadása → helyi számítás → visszaadott érték → összetett rendelés. A megírt fájlok maradjanak meg. L1 haladási esemény csak tényleges kód és ismert futás alapján készüljön; a `haladas.md` ne legyen automatikusan frissítve. Ha egy próba még nem történt meg, azt ne pipáld ki. Szünet után a D1 következik, vagy a konkrétan megnevezett hiányzó B1-rész.

## D1 – egy döntés külön, azután újabb döntés

**Egész feladat:** a rögzített rendelésből feltétellel kedvezményt számolunk, majd a kiszámított fizetendőhöz képest értelmezzük a pénzt. Nem kell egyszerre az inputtal is foglalkozni.

**Előbb D1.a:** a munkalap gyerekbelépős függvénye alapján magyarázd el a logikai paramétert, az if/else ágakat, a kétszintű behúzást a függvényben és a két visszatérést. Az ár és a kedvezmény szerepe eltér: a saját függvény a kedvezmény ÖSSZEGÉT adja vissza. A return minden ágon számot adjon.

A `//` műveletet itt röviden idézd fel. A kedvezmény a nemnegatív összeg tízzel való egész hányadosa. Példa: 1790 // 10 = 179; fizetendő 1790 - 179 = 1611. Ha szükséges, 1795-nél is vezesd végig: 179 kedvezmény és 1616 fizetendő. Ne cseréld a szabályt int(osszeg * 0.9)-re.

**Utána D1.b:** a fizetett >= fizetendo összehasonlítás logikai eredményét használd. Tanítsd meg, miért fontos az egyenlőség. A két kivonás sorrendje a kiírt összeg jelentését követi: visszajáró vagy hiány. A tanuló írja meg a saját ágait, és a megadott adatokkal futtasson.

**Tipikus javítás:** csak True ágon van return → False esetben None; `>` → a pontos fizetés téves elutasítása; mindkét helyen ugyanaz a kivonás → negatív „hiány”. Egyetlen hibát vegyetek egyszerre célba, utána térjetek vissza az érintett másik ágra is.

## D2 – if-ek helyett kategóriát választó lánc

**Először a célkülönbség:** a kiinduló két if két igaz állítást is kiírhat. Ez a mintában nem szintaktikai hiba. A tanuló új célja egyetlen kategória kiválasztása.

**Új fogalom:** elif az előző feltételek hamis esete után vizsgál. Az első igaz ág után a lánc többi része kimarad. A konkrét >= küszöböket ezért nagyobbtól kisebbig rendezzük; ne általánosítsd minden lehetséges feltételláncra.

**Kérés:** a teljes kis kategorizáló részt a tanuló írja át. Nem szükséges függvényt is létrehozatni erre a hétperces feladatra. A 1499/1500 és 2999/3000 párok a határátlépést ellenőrzik. 3500-nál a kis küszöb előre helyezése fedi fel a sorrendhibát, ha célzott javítás kell.

Időhiányban ez a külön feladat későbbre tehető; ettől B2 if–else működése még összeépíthető. Az elif teljesítését ilyenkor nem igazoljuk.

## B2 – összeépítés, nem újraírás

**Egész program áttekintése:** a B1 számításához két új bemenet kapcsolódik, a D1 kedvezménye és fizetési döntése pedig a kapott adatokat használja. Mondd el az új program egész célját, mielőtt bemeneti sorokat vagy kivonást kérsz írni.

**Darabolás:** saját kedvezményfüggvény átvitele → két új input és a válasz összehasonlítása → kedvezmény és fizetendő → nyugta és fizetési ág → négy próba. A köszöntő függvény használata megengedett, de nem új kötelező követelmény. Az integrációban a jó nevek és a meglévő munkája használata a fő cél.

**Magyarázat:** az input szöveg, az int számot ad; a diákságot nem int-tel, hanem == összehasonlítással állítjuk elő. A bool("nem") nem magyar jelentést vizsgál, ezért nem jó ide. A fő útvonalon megfelelő bemenetet feltételezünk; ne minősítsd a K2 nélküli programot általánosan hibásnak, mert nem vizsgál minden negatív számot vagy elírt választ. A tanuló tudjon erről a feltételezésről.

**Fájlhasználat:** a dontes.py állandó tesztadatai nem kerülhetnek át a bekért értékek helyére. Ha véletlenül a 2000 maradt az input után, olvasd együtt vele az adat útját: a későbbi értékadás felülírja a bekért értéket. Ne kényszerítsd teljes fájlcserére.

**Ellenőrzés:** a munkalap négy B2-próbája elég a fő célhoz. Új hiba vagy eltérő számítás esetén további konkrét eset indokolt. A nulla rendelés elfogadott ebben a tanpéldában. A forrásban megírt függvényeket és a hívásban adott adatokat is ellenőrizd, ne csak a számokat.

## Z1 – rövid önálló alkalmazás, támogatás továbbra is elérhető

A tanuló a meglévő, állandó díjat adó függvényt alakítja adatfüggővé. A paraméter, a két visszatérési út és a >= már szerepelt a tanításban. A feladat nem kíván új nyelvi eszközt, és nem kér kimenetjóslást.

A konkrét cél: legalább 2500 Ft-nál 0, alatta 490. A megadott tesztek nem kész kódok. Ne diktáld le előre az egész függvényt, majd jelöld önállónak a bemásolását. A tényleges forrásban ellenőrizd, hogy paraméterből dönt, nem kiírt állandó eredményekkel kerüli meg a feladatot.

Ha elakad, először a hiba helyét kérdezd vagy mutasd meg a hiányzó fogalom analóg példáját. Ha rövid kész részlet kell, add meg, de az érintett munka támogatott. Időn belül egy új határértékre végzett kis módosítás megerősítheti a megértést; ez nem újabb kötelező vizsgakör.

## Kiegészítők csak külön időben

K1: alapértelmezett paraméter, majd név szerinti argumentum; mindkét fogalom magyarázata megelőzi a saját átírást. K2: and/or/not, majd az adatellenőrzés és a számítás elkülönítése. Az int átalakítás hibáját ez nem kezeli. K3: a maradékból összehasonlítás, annak logikai visszatérési értékéből megjelenítési döntés. Mindháromhoz van kiinduló minta a munkalapon és/vagy fájlban.

## S2 – tanulási összegzés

A saját programjára hivatkozva kösd össze a részeket: a paraméterek az adatokat viszik a függvényhez, a return a számítás eredményét hozza vissza, az elágazás egy feltétel alapján választ végrehajtandó kódot. A bemenet, a számítás és a megjelenítés szerepe látható marad. A határeseteket valós futásokkal próbáljuk ki.

Ezután röviden jelöld, mely fájlrészt írta saját maga, mihez kapott konkrét segítséget, és mi a folytatás. Ne keverd össze a természetes fogalommagyarázatot az adott feladat kódjának lediktálásával. A haladási állapothoz a kód és a futás forrása is tartozzon, az L1 eseményben rögzítve, automatikus munkatérfájl-írás nélkül. Az összegzés nem helyettesíthető puszta „kész, 100%” adminisztrációval.


## A haladás rögzítésének helye

A `record_learning_event` a strukturált részfeladat-/próbaeseményhez való. A `payload.topic` röviden azonosítsa az EP_02-t, az aktuális részt és a következő lépést; a szabad `payload` tartalmazza az állapotot, konkrét módosítást, próbát, eredményforrást és segítséget. Az esemény a profilt is frissíti, ezért ugyanazt nem kell még `patch_learner_profile`-lal és egy Markdown-szerkesztéssel megismételni. Puszta haladásadminisztrációnál a `derived_signals.mastery_delta` legyen 0. A részletes hívási szabályt az agent.md memóriafejezete írja le.

S1/S2-nél a rövid eseményösszegzésből is derüljön ki, mely részek készültek el, hol volt konkrét kódsegítség és mi maradt. Ne állítsd az egész feladatot önállónak azért, mert a támogatással javított rész fut. Ez a korábbi értékelési elv változatlan alkalmazása az új tárolási helyen.

A `haladas.md` megmarad kézzel használható lapnak. Nem írjuk át automatikusan, nem nyitjuk meg minden részfeladat után, és nem cseréljük másik munkatérbeli háttérfájlra. Külön kért megtekintés/export esetén használható. Letiltott L1 vagy Egyszerű mód esetén nincs sikeres memóriamentés: a chatben adj folytatási pontot, ne szerkeszd a lapot kerülőútként. Beállítást csak az oktató változtat; az agent nem kapcsolja át magától.
