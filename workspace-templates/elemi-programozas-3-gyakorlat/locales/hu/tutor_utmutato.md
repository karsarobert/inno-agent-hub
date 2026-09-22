# EP_03 – tanítási terv és segítségadási támpontok

A tanuló a célkódot maga írja. Ez a fájl a tutor munkáját szervezi; nem felolvasandó szöveg, és nem kész megoldókulcs. Először az aktuális munkalaprész és a tényleges forrásfájl tartalmát olvasd, csak utána adj következő szerkesztést.

## A 90 perc felosztása

| Első blokk | Perc | Második blokk | Perc |
|---|---:|---|---:|
| E0 – első mentett futás | 3 | L1 – lista és bejárás | 8 |
| W1 – while | 8 | B2 – kosárösszegző | 9 |
| W2 – újrakérés | 9 | C1 – blokk, continue | 8 |
| F1 – for/range | 7 | B3 – összeépítés, fizetési ciklus | 10 |
| B1 – napi összesítés, break | 15 | Z1 – önálló termékszámláló | 7 |
| S1 – folytatási pont | 3 | S2 – lezárás | 3 |
| **Összesen** | **45** | **Összesen** | **45** |

Az időkeret rugalmas terv, nem a tanuló teljesítményének mért adata. A magyarázat, a szerkesztés és a próbák is ebbe tartoznak. A listák és ciklusok teljes HTML-fejezetsorát nem olvassuk fel. A részletes referenciát célzottan használjuk.

Két büfés nézőpont van: B1 már kifizetett rendelési összegekből készít napi összesítőt; B2–B3 egy előre megadott kosár tételeiből állít elő fizetendőt. A teljes vendégkezelő főciklus K1-ben kapcsolja össze a kettőt. A két program célját mondd el, ne sugallj több funkcionalitást, mint ami elkészült.

B3 szűk keretű összeépítés: a tanuló saját W2/B2 függvényét újra használja, nem újraírja. Ha ez még lassan megy, a pénzpótlási bővítés későbbre tehető; a hiány legyen kimondva. Z1 és a lezárás idejét ne fogyaszd el teljesen. A kész célkód bemásolása nem időgazdálkodási megoldás.

## Minden új fájl előtt

Mondd el három összefüggő mondatban vagy rövid bekezdésben: mit csinál a kiinduló program, milyen adatot használ, és milyen új képességet ír hozzá a tanuló. Ezután magyarázd a kijelölt sorok jelentését. Az induló helyőrzőket ismertesd: például B2 return 0-ja tervezett bővítési hely, nem korábbi tanulói tévedés.

A munkalap rövid mintáit magyarázd el, ne csak illeszd a beszélgetésbe. A feladatra vonatkozó pontos próbaadat átadható. Nem kérünk előzetes eredményjóslást.


## E0 – Mentett fájl és első futás

**A program célja:** Egy már ismert print-utasítás szövegét módosítod. Ezzel ellenőrizzük, hogy valóban a megnyitott és elmentett fájl fut.

**Tanítási hangsúly:** A szerkesztőben Python-kódot írsz; a terminálban a futó program eredményét látod. A Futtatás mindig a megfelelő megnyitott fájlhoz tartozzon. Az összes gyakorlófájl a munkamappa gyökerében van, így itt ez egyben a Python-fájlok mappája is.

**Segítség és gyakori elakadás:**

- Ne indulj pwd/ls verzióellenőrző kérdéssorral, ha a Run működik.
- Régi szövegnél előbb a mentést és az aktív fájlt vizsgáld. Ez technikai lépés, nem ciklusismeret.

**Elfogadási szempont:** Az elmentett saját szövegmódosítás megjelenik a megfelelő fájl futásakor.

**Futás utáni megértésellenőrzés:** Melyik fájlt futtattad? Csak bizonytalan célfájl esetén kérdezd.

## W1 – Ismétlés while ciklussal

**A program célja:** A program rendelési sorszámokat ír ki. A kiinduló változat csak egyet mutat; te írod meg az ismétlést és a sorszám változtatását.

**Tanítási hangsúly:** A while minden kör előtt újra megvizsgálja a feltételt. A behúzott sorok a ciklus törzse. Az állapotnak változnia kell: a `+= 1` egész számnál ugyanazt jelenti, mint a régi értékhez egyet adó értékadás. A ciklus utáni, nem behúzott kiírás csak egyszer fut. Az alábbi minta visszaszámlál; a saját feladatod felfelé számoz.

**Segítség és gyakori elakadás:**

- A mintában csökken a maradék, a feladatban növekszik a sorszám: ezt magyarázd el.
- Végtelen futásnál Ctrl+C, majd feltétel és növelés vizsgálata; ne javíts a fájlban.

**Elfogadási szempont:** Valódi while ciklus, nem egymás alá írt kész kiírások. A növelés a törzsben, a lezárás azon kívül van. Az elsőre hamis feltétel esetén nulla kör történik.

**Futás utáni megértésellenőrzés:** Melyik sor miatt tud véget érni a ciklus? A saját kész kódjára mutasson.

## W2 – Újrakérés függvényben

**A program célja:** Egy darabszámot bekérő függvényt egészítesz ki. A fejléc és a hívás már működik, de a függvény még a negatív számot is elfogadja.

**Tanítási hangsúly:** A kezdőértéket az első input adja. Amíg a szám negatív, figyelmeztetünk és új értéket kérünk. A return csak a ciklus után következhet: akkor már elfogadható számot adunk vissza. A 0 megengedett. Most egész számként leírható válaszokkal dolgozunk; a `ketto` és a `2.5` szöveg kezelését még nem tanultuk. A minta egy szöveges választ kér újra; a saját feladatban számmal és a negatív tartomány feltételével dolgozol.

**Segítség és gyakori elakadás:**

- Ha az új input eredményét nem rendeli a szamhoz, a feltétel nem változik.
- Ha a tanuló nem alakítható szöveget ír be, ne minősítsd a tartományellenőrzését hibásnak; nevezd meg a feladat korlátját.

**Elfogadási szempont:** A negatív számnál tényleges új input történik. A paraméter kérdésszövegét használja. Az elfogadott számot adja vissza; nem csak kiírja.

**Futás utáni megértésellenőrzés:** Miért a while után van a return?

## F1 – Sorszámok for és range segítségével

**A program célja:** A három ismétlődő print helyére egy ciklust írsz. A W1 megoldása a másik fájlban megmarad, így a két megoldást később összehasonlíthatod.

**Tanítási hangsúly:** A for sorban megkapja a range által megadott egész számokat. A kezdőérték benne van, a végpont nincs. A ciklusváltozót nem növeljük kézzel. A minta a 2, 4, 6 értékeket járja be; a harmadik argumentum a lépésköz.

**Segítség és gyakori elakadás:**

- A tanuló írja a range-et, ne írd helyette azonnal a célbeli sort.
- A negatív lépés és a nulla ismétlés a kiegészítő gyakorlásban elérhető, ne növeld kötelezően az időigényt.

**Elfogadási szempont:** For + range szerkezet, változót használó f-string. Kizárt végpont helyes, nincs felesleges kézi növelés.

**Futás utáni megértésellenőrzés:** Miért eggyel nagyobb a megadott végpont az utolsó kiírt számnál?

## B1 – Napi bevétel zárásig

**A program célja:** A büfé kifizetett rendeléseinek összegeit rögzítjük, amíg 0-val le nem zárjuk a napot. Most a már kész rendelési értékeket adjuk meg, nem minden vendég teljes rendelését kérjük be.

**Tanítási hangsúly:** A napi bevétel és a rendelési darabszám a ciklus előtt indul 0-ról. A `while True` ismétel, a belső `break` ad neki kijáratot. A 0 itt végjel: nem rendelés. A negatív érték hibás, nem növeli egyik összesítőt sem. Az összegző az aktuális összeget, a számláló 1-et kap hozzá. A példa üzeneteket ismétel kilépésig; a saját programod számokat dolgoz fel.

**Segítség és gyakori elakadás:**

- Oszd B1.a: ismételt bekérés és 0/break; B1.b: helyes összegzők; B1.c: két próba.
- Ne add meg egyetlen üzenetben a teljes célprogramot.
- Ez kifizetett összegek nyilvántartása: a 2000 Ft-os készpénzátadás helyett a tényleges 1611 Ft-os rendelési érték kerülne bele.

**Elfogadási szempont:** A bekérés a ciklusban van, a végjel vizsgálata a feldolgozás előtt. A negatív és a 0 nem növeli az összesítőket. Nincs cikluson belüli nullázás. A záró kiírás egyszer történik.

**Futás utáni megértésellenőrzés:** Mi veszne el, ha minden körben nulláznánk a napi bevételt?

## S1 – Első óra lezárása

**A program célja:** Röviden rendezzük, mi készült el, és honnan folytatjuk.

**Tanítási hangsúly:** A fájlok a saját munkádat őrzik. A szünet után nem készítünk belőlük új, üres mintát.

**Segítség és gyakori elakadás:**

- Ne minősíts teljesítettnek olyan W/B feladatot, amelyet nem írt meg vagy nem próbált ki a tanuló.

**Elfogadási szempont:** A folytatási pont tényleges állapoton alapul.

## L1 – A kosár elemeinek bejárása

**A program célja:** A listában minden termék külön elem. Először a kosár adatát és kiírását változtatod; az összegző függvény csak a következő feladatban készül el.

**Tanítási hangsúly:** A lista szögletes zárójelben tárol elemeket. A kosárban ugyanaz a termék többször is szerepelhet. A for ciklusváltozó itt maga a szöveg, nem index. A fájlban már ott van az árlekérdező függvény; az ismeretlen termékre adott 0 később jelzés lesz. A `kosar_osszege` ideiglenes 0-ja még nem megoldás és nem a te hibád.

**Segítség és gyakori elakadás:**

- A szögletes és a kerek zárójel szerepét különítsd el.
- Az üres listán nem futó törzs érvényes működés, nem hiányzó eredmény.

**Elfogadási szempont:** A lista sorrendjében négy elem jelenik meg. Közvetlen bejárás; nincs beégetett négy print. Üres listán nem indexel nem létező elemet.

**Futás utáni megértésellenőrzés:** A termek változó az elem indexét vagy a termék nevét tartalmazza a saját ciklusodban?

## B2 – A kosár összegző függvénye

**A program célja:** A már működő árlekérdezést felhasználva saját kosárösszegzőt írsz. A függvény eredményére a büfé fizetési részének lesz szüksége.

**Tanítási hangsúly:** A `termek_ara` egyetlen termék árát adja vissza: kávé 450, szendvics 890, üdítő 390 Ft. A `kosar_osszege` minden elemnél ezt hívja, és a visszaadott értéket összeadja. A kiírás a hívónál marad. A rövid minta a felhalmozást mutatja szöveghosszakkal; a saját feladatod árakat számol, és függvényből tér vissza.

**Segítség és gyakori elakadás:**

- Ha csak 450 az eredmény, először a return behúzását nézd.
- A len mintában magyarázd meg: szöveghosszt ad; ne váljon külön szövegfeldolgozási feladattá.

**Elfogadási szempont:** A függvény a paramétert járja be, nem a külső kosar változóra támaszkodik. A termek_ara függvényt hívja, és nem beégetett 2180-at ad vissza. A return a teljes ciklus után van; üres listán is 0 az eredmény.

**Futás utáni megértésellenőrzés:** Miért csak a bejárás után szabad visszaadni a teljes összeget?

## C1 – Blokk és ismeretlen termék kihagyása

**A program célja:** A blokk.py már tartalmazza az árlekérdező függvényt, a blokkfüggvény kezdetét és a próbakosarat. Most megírod a blokk megjelenítését. A program a blokk kiírásával véget ér; nincs terminálbemenet. A saját kész függvényedet B3-ban viszed át a büféprogramba.

**Tanítási hangsúly:** A blokk függvénye jogosan használ printet, mert megjelenítés a feladata. A 0 ár most ismeretlen terméket jelöl: minden eladható termékünk ára pozitív. A continue csak az adott kör hátralévő részét hagyja ki; a későbbi ismert termékeket továbbra is feldolgozzuk. A len(kosar) minden beírt elemet számolna, ezért az elfogadott tételekhez külön számláló kell.

**Segítség és gyakori elakadás:**

- C1 kizárólag a blokk.py fájlban zajlik. A futás végén nincs diákság- vagy pénzkérdés; a bufe_03.py csak B3-ban kerül elő.
- A program közvetlenül a blokkot_mutat(kosar) hívás után véget ér. B3 elején a tanuló a saját kész függvénydefinícióját viszi át, a tesztadatokat és a próbahívást nem.

**Elfogadási szempont:** A pizza után az üdítő még megjelenik. Continue használata; az ismeretlen termék nem növeli a számlálót. A blokkfüggvény csak a kapott kosárral dolgozik.

**Futás utáni megértésellenőrzés:** Miért maradna ki az üdítő is, ha ezen a helyen break állna?

## B3 – A kosár és a fizetés összeépítése

**A program célja:** Most nyitod meg a bufe_03.py fájlt. A saját blokkmegjelenítő, összegző és bekérő függvényeidet viszed át és használod fel benne. A fizetés ismétlődik, amíg a teljes összeg össze nem gyűlik.

**Tanítási hangsúly:** A kosár alapösszege és a kedvezményes fizetendő külön adat. A kedvezmény az alapösszeg // 10 része, ha diák a vendég. A pótlás újonnan átadott pénz: hozzáadjuk a korábban befizetetthez. A nulla értékű kosárnál nincs fizetési kérdés. A számos kérdésekhez a W2 saját függvényét használjuk, a diáksághoz ezen a fő útvonalon pontos igen/nem választ kérünk.

**Segítség és gyakori elakadás:**

- B3.a: a saját blokkot_mutat definíció átvitele a blokk.py-ból a kezdő definíció helyére, majd a saját összegző és bekérő definíció átvitele és az összeg; B3.b: nulla ág; B3.c: fizetési ciklus. Ezeket külön üzenetekben vezesd.
- Ha időszűke van, B3.c külön folytatásra tehető, de ilyenkor csak az EP_02-féle egyszeri fizetésellenőrzés kész.
- A pontos igen/nem a főút bemeneti szerződése; talan-t nem tekintünk megbízhatóan kezelt esetnek. Az igen/nem újrakérés K3.

**Elfogadási szempont:** A teljes kosárra számol és a saját függvényeket hívja. A pótlást hozzáadja, nem lecseréli a befizetett összeget. Visszajárót csak elegendő pénznél ír, a ciklus után. Üres kosárnál nincs indexhiba, bekérés vagy fizetés.

**Futás utáni megértésellenőrzés:** Miben különbözik a pótlás a befizetett_osszesen értékétől?

## Z1 – Önálló termékszámláló

**A program célja:** Egy önálló függvényt írsz, amely tetszőleges megadott terméket számol meg a kosárban.

**Tanítási hangsúly:** A feladat a már ismert paramétert, bejáró ciklust, feltételt és returnt kapcsolja össze. Nincs új nyelvi eszköz. A függvény csak számot adjon vissza; a próbahívások eredményét kívül írd ki.

**Segítség és gyakori elakadás:**

- Ne másold be a három-négy kész próbahívást sem a kész vagyok válaszra. Nevezd meg a hiányzó esetet, a tanuló írja a hívást.
- Konkrét célkódsegítség után támogatással megoldott állapot jár. Nincs kötelező újabb vizsga az óra végén.

**Elfogadási szempont:** A keresett termék paraméterét használja, nem beégetett kávét. Feltételes számlálás és ciklus utáni return. A saját próbahívásai megvannak, üres listára is.

**Futás utáni megértésellenőrzés:** Miért nem ugyanaz a lista hossza és a keresett termék darabszáma?

## S2 – Lezárás és folytatási pont

**A program célja:** Összekapcsoljuk a ciklus, a függvény, a kosár és a pénzszámítás szerepét.

**Tanítási hangsúly:** A magyarázatodban a saját elkészült programrészekre támaszkodj. Ami még hiányzik, azt külön megnevezzük.

**Segítség és gyakori elakadás:**

- A kihagyott feladat nem teljesített. Egy hiányos szóbeli válasz után röviden egészítsd ki a megértést; ne jelents teljes fogalmi bizonyítást.

**Elfogadási szempont:** A lezárás nem állít többet a tényleges munkánál.

## Az önállóság értelmezése

A mikropélda elmagyarázása nem oldja meg automatikusan a másik feladatot. A tanuló elvégzett kódváltoztatása, ismert próbái és a megoldáshoz adott konkrét segítség alapján értékelj. Ha te mutattad meg a célfeladat teljes ciklusát és hívásait, nem önálló megoldásról van szó attól, hogy a tanuló bemásolta.

B3-ban a saját korábbi függvény átvitele megengedett önálló alkalmazás, de az eredeti W2/B2 segítségigényét ne töröld a feladattörténetből. Ha egy korábbi függvény támogatással készült, ezt ott tartsd meg. Az összeépítés saját részének segítségigényét külön rögzítsd.

A „sikerült” válaszra olvass kódot és ellenőrizd az ismert futási adatot. A kód helyességét és a futás bizonyítékát külön kezeld: például „A ciklus a fájlban helyes. Az üres listás próba eredményét még nem látom; futtasd le ezt az egy esetet.” Ne mondd, hogy minden határérték lefutott, ha csak a legutolsó értéket látod.

## Haladás és folytatás

A memória szabályai a memoria_utmutato.md-ban szerepelnek. Nincs automatikusan szerkesztett haladási lap. S1/S2-nél egyszer rögzíts érdemi összefoglalót, majd természetes nyelven röviden vezesd tovább vagy zárd le az órát. Letiltott memória esetén a beszélgetésben legyen folytatási pont; az alkalmazás beállítását nem változtatjuk meg automatikusan.
