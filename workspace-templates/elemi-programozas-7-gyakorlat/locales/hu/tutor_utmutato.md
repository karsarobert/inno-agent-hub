# EP_07 – Tutorútmutató

Belső tanítási támpont. A kezdőminták futnak, de a célkövetelményt még nem teljesítik. A hallgató a saját érdemi módosításait írja, menti és futtatja. Az agent.md szabályai érvényesek; ez a fájl a feladatonkénti magyarázatot és diagnózist részletezi.

Minden új fájlnál előbb a nagy képet mondd el: bemenet, feldolgozás, kimenet, mi adott és mi saját. Utána egy rövid analóg minta, majd egy összetartozó szerkesztés és konkrét próba következzen. A kész célalgoritmust ne add át. Z1-nél elsőre követelmény és teszt jár; analóg irány csak elakadásnál.

A valós kód, a megtekintett futás és a tanulói beszámoló eltérő bizonyíték. Csak a még hiányzó esetet kérd. A normatív eredménytábla nem tanulói futás. Az A3 és B1 szakaszait külön tartsd számon.

## A1 – Rendelési tételek tuple-ben

**Fájl:** tetelek.py; **keret:** 8 perc.

**Nagy kép:** A tétellista minden adat-hármasából terméknevet, darabszámot és egységárat kapsz, majd tételsoronként részösszeget számolsz.

**Adott és saját rész:** Adott a tétellista és a fejléc. Egy tuple pontosan három mezőt tartalmaz ebben a sorrendben: terméknév, darabszám, egységár. A kezdőprogram csak egyben írja ki a listát. Darabszám pozitív egész, egységár nemnegatív egész; típusellenőrzés nem feladat.

**Magyarázd el:** A rövid mintában egy listaelem egy könyv két mezője; a ciklus ezeket kicsomagolja. A saját tételben három mező van, és két számból részösszeget is számolsz. A mezők pozícióját a jelentésükkel együtt figyeld.

**Fokozatos segítség:** A ciklus minden menetben egy teljes tuple-t ad. Hány nevet kell a kicsomagolás bal oldalára írnod? A kiírás előtt mely két mező szorzatára van szükség?

**Tipikus hiba:** Felcserélt darab/ár; az egész lista kicsomagolása egy tétel helyett; beégetett részösszeg. A pontos szóközök és a × vagy * megjelenítés eltérése elfogadható.

**Elfogadás:**
- Minden tétel külön sorban szerepel, a három mező jelentése helyes.
- A részösszeg az aktuális adatokból származik, nem beírt állandó.
- Üres listánál nincs tételsor; a bemenet nem módosul.

**Kötelező próbák:** A1.1, A1.2, A1.3, A1.4.

## A2 – Mit mond el a kosár?

**Fájl:** kosar_adatok.py; **keret:** 10 perc.

**Nagy kép:** Egy függvény visszaadja az összes tétel számát, a különböző termékfajták számát és egy keresett termék darabszámát, ebben a sorrendben.

**Adott és saját rész:** A kosar_adatai paraméterei és az induló próbaadatok adottak. A visszatérés még (0, 0, 0), ezért nem valódi számítás. A főprogram egyelőre csak egyben mutatja ezt a tuple-t. A terméknevek már egységesített szövegek.

**Magyarázd el:** A len az összes eseményt számolja. A set egyedi azonosítókat készít, ennek hossza más kérdésre felel. A lista count metódusa egy megadott érték előfordulásait adja; nem a teljes lista hossza és nem halmazművelet.

**Fokozatos segítség:** A három kérdéshez három külön kifejezés tartozik. Ha a kosarat halmazzá alakítod, az eredetit külön őrizd meg: a count a listán működik.

**Tipikus hiba:** A kosar név halmazra átírása információvesztést okoz; count hívása halmazon; print a return helyett; tuple visszaadása után a főprogram nem csomagol ki. Egy kiválasztott termék count-ja egy bejárás; itt nem teljes gyakorisági szótárat kérünk.

**Elfogadás:**
- A visszatérési érték három egész számot tartalmazó tuple, a rögzített sorrendben.
- Külön kezeli az összes darabot, a termékfajtákat és a keresett terméket.
- Az eredeti kosár megőrzi sorrendjét és ismétlődéseit. A hívó jelenít meg.

**Kötelező próbák:** A2.1, A2.2, A2.3, A2.4.

## A3 – Két kosár termékfajtáinak összehasonlítása

**Fájl:** kosarak.py; **keret:** 15 perc.

**Nagy kép:** Két kosárlistából halmazalapú összehasonlítást készítesz. A kimutatás öt halmazt és egy logikai értéket ad vissza az előkészített eredményszótárban.

**Adott és saját rész:** A függvény paraméterei, a szótár kulcsai és az eredmények megjelenítése adott. Az üres halmazok és a False egyelőre helykitöltők. Egy kosárban ugyanaz a termék többször szerepelhet; itt csak a termékfajtákat hasonlítjuk össze.

**Magyarázd el:** A metszet új halmazt ad. A részhalmazvizsgálat logikai értéket ad: minden bal oldali elem szerepel-e a jobb oldalon? Az eredmény típusát is figyeld. A darabszámok összehasonlítása ettől külön feladat lenne.

**Fokozatos segítség:** Előbb fogalmazd meg a kérdést: mindkettőben, legalább az egyikben, csak az elsőben, csak a másodikban, pontosan az egyikben, vagy minden elsőbeli a másodikban? Ezután válassz műveletet.

**Tipikus hiba:** or/and használata halmazképzés helyett; két különbség azonos iránnyal; elemszám összehasonlítása részhalmaz helyett; <= listákon; a logikai érték sorted-ba adása. A szótár keretét szabad megtartani, csak a helykitöltő kifejezéseket kell lecserélni.

**Elfogadás:**
- Az első öt eredmény set; az elso_reszhalmaz bool.
- A különbség irányai és a szimmetrikus különbség jelentése helyes.
- Azonos termékfajták eltérő darabszámmal is részhalmazviszonyt adhatnak.
- Az üres bal oldali halmaz részhalmaz; minden kötelező próba ismert, a bemenetek változatlanok.

**Kötelező próbák:** A3.1, A3.2, A3.3, A3.4, A3.5.

## B1.a – Új kosár az eredeti megőrzésével

**Fájl:** modositas.py; **keret:** 8 perc.

**Nagy kép:** A bovitett_kosarat_keszit új, egy termékkel bővített listát adjon vissza, miközben a hívó eredeti kosara változatlan.

**Adott és saját rész:** A kezdő függvény az append miatt még az eredeti kosarat bővíti, és ugyanazt a listát adja vissza. A főprogram megmutatja a hívás előtti és utáni állapotot, valamint az is összehasonlítást. A B1.b függvénye még szándékosan helykitöltő; most nem azt javítjuk.

**Magyarázd el:** A másolat külön szótár; ebben a mintában egész értékeket tartalmaz. Listának is van copy metódusa. A paraméterhez kötött objektum automatikusan nem másolódik: a saját feladatban tudatosan kell külön listát készítened a bővítéshez.

**Fokozatos segítség:** A másik név önmagában még nem másolat. Melyik objektumon fut le az append, és melyik objektumot adod vissza?

**Tipikus hiba:** uj = kosar csak másik nevet ad ugyanahhoz az objektumhoz; return kosar a másolat helyett; return lista.append(...) None-t adna; set-tel elvesznek az ismétlődések. A feladat sekély, szövegeket tároló listát használ.

**Elfogadás:**
- Új lista tér vissza; az eredeti tartalma és objektuma megmarad.
- Az új termék az új lista végére kerül; az ismétlődés megengedett.
- Az is összehasonlítás False; minden előírt próba ismert.

**Kötelező próbák:** B1.a.1, B1.a.2, B1.a.3.

## B1.b – Törzsvásárló szándékos felvétele

**Fájl:** modositas.py; **keret:** 6 perc.

**Nagy kép:** A torzsvevot_felvesz a kapott halmazt szándékosan módosítsa új névnél. Adjon True-t új név, False-t már meglévő név esetén.

**Adott és saját rész:** A második függvény most mindig False-t ad, és nem módosít. A nevek már egységesített, nem üres szövegek; nincs külön input vagy névtisztítási feladat. Az első függvény korábban elkészített változata maradjon meg.

**Magyarázd el:** Az add a meglévő halmazt módosítja, és az ismételt elem nem növeli az elemszámot. A te függvényednek emellett azt is jeleznie kell, hogy most került-e be új név, ezért a hívás előtti jelenlét is számít.

**Fokozatos segítség:** A korai return lezárhatja a már meglévő név ágát. Az add visszatérési értéke nem a te True/False sikerjelzésed.

**Tipikus hiba:** A halmaz helyett másolaton dolgozik, így a hívó nem változik; mindkét esetben True-t ad; egyik ágban hiányzik a return; visszaadja az add None eredményét; két külön futást ismételt hívásnak tekint.

**Elfogadás:**
- Új névnél a hívó halmaza bővül és True tér vissza.
- Meglévő névnél semmilyen név nem vész el, az elemszám nem nő és False tér vissza.
- A működés megkülönböztethető a B1.a új listát készítő működésétől.

**Kötelező próbák:** B1.b.1, B1.b.2, B1.b.3.

## Z1 – Teljesíthető-e a rendelés?

**Fájl:** onallo.py; **keret:** 12 perc.

**Nagy kép:** A kosárlistából és az árjegyzékszótárból új halmazban visszaadod a hiányzó termékfajtákat. A hívó a hiány alapján érthető üzenetet jelenít meg.

**Adott és saját rész:** A függvény jelenlegi üres halmaza csak helykitöltő. A próbaadatok és a visszatérés tárolása adott. A terméknevek már egységesítettek. Az árjegyzékben a kulcsok a terméknevek; itt elérhetőséget, nem készletdarabszámot vizsgálunk.

**Magyarázd el:** Első próbálkozáskor a követelményt és a teszteket kapod, kész algoritmust nem. A korábbi feladatokban már használtál egyedivé alakítást, csoportkülönbséget és függvényes visszatérést.

**Fokozatos segítség:** Valódi elakadásnál előbb kérdezd meg: melyik adatforrás őrzi a kért termékeket, és melyik az elérhető neveket? A szótár bejárása a kulcsokat adja. Ezután az A3-ból egyetlen kapcsolódó műveletre utalj, teljes célfüggvény nélkül.

**Tipikus hiba:** Fordított különbség; csak elemszámok összehasonlítása; az összes kapható termék visszaadása; a kosár módosítása; a hiányzó termék felvétele az árjegyzékbe; árakból képzett halmaz; beégetett tea/pizza nevek.

**Elfogadás:**
- Új set az eredmény, a hiányzó termékfajták helyesek és egyediek.
- A függvény paraméterekből dolgozik, nem globális kosárból/árjegyzékből.
- A két bemenet változatlan; a döntés és megjelenítés a hívóban van.
- Az összes előírt próba eredménye ismert; az üres eredmény nem None.

**Kötelező próbák:** Z1.1, Z1.2, Z1.3, Z1.4, Z1.5.

## A3 szakaszhatárok és a részhalmaz jelentése

A3.a-ban csak az osszes és kozos mezőt vizsgáljuk az A3.1 adataival. A3.b-ben az öt halmazmező készül; ugyanazon A3.1 még ismeretlen mezőit nézzük. A3.c-ben a bool és az üres/azonos esetek jönnek. Csak a végső A3-értékelés követeli mind az öt eset teljes eredményét.

A <= itt nem darabszámot és nem elemszámot hasonlít. Az első kosár két kávéja és a második egy kávéja termékfajta alapján részhalmazviszony. Ha a tanuló jogosan jelzi, hogy ez nem elég valódi készletellenőrzésre, fogadd el: a feladat elérhetőségi kimutatás. A Z1 is csak kínálati kulcsokat vizsgál.

## B1 – Név és objektum

A B1.a induló kódjának appendje szándékosan módosít. Nem technikai hibát javítunk, hanem új követelményt teljesítünk. Az uj = kosar után az is True lenne: ugyanaz az objektum. Másolattal új lista készül, a hívói lista változatlan. Az is False önmagában nem elég: az új lista tartalmát és az eredetit is ellenőrizni kell.

A B1.b-ben épp szándékos helyben módosítás a cél. A visszatérési érték sikerjelzés, nem maga a halmaz és nem az add eredménye. A már jelen lévő név ága False; új név True. A paraméterátadás mechanizmusa a két feladatban azonos, a függvény művelete eltér.

A tuple elemei nem cserélhetők, de beágyazott listája módosulhat. A mai B1-lista csak szövegeket tartalmaz, ezért a sekély copy elég. Ne magyarázd úgy, hogy számnál tartalommásolatot kap, listánál pedig automatikusan más átadási módra vált a Python.

## C1 – Az egyetlen összetett bővítés

A bovites.md szerint, 15 tervezett perc. Z1 után legalább 42 ténylegesen fennmaradó perc kell hozzá, a tesztek és lezárás 27 percét megtartva. Bizonytalan időnél egyszer tisztázz. A teljes tervezett út C1-gyel 105 perc; a megtakarított idő teszi lehetővé a 90 percen belüli választást.

Saját A2-definíció átvétele, majd C1.a soradatok előállítása és C1.b megjelenítés. A kezdeti kosar_adatai is helykitöltő; ne maradjon benne a saját változat helyett. Minden termék ismert árjegyzékkulcs, ezért közvetlen árlekérdezés megfelelő. Ne csendesíts ismeretlen nevet get(..., 0)-val.

A tuple-ök négyeleműek, a visszakapott lista új és rendezett. Két külön termék azonos áron is külön sor. A listák + művelete új listát készít; az elso_kosar.extend(...) átírná az első bemenetet. Nem kell ezt a célkódot előre diktálnod; a tényleges változtatásnál diagnosztizáld.

## S1, záró tesztek, S2

S1 kétperces, a már kész saját kódhoz kapcsolódó összegzés és a B1.b folytatási pontja. Nem új kör és nem kötelező szóbeli vizsga.

T1 10, T2 15 perc. A kérdéseket eredeti azonosítóval, változatlan adatokkal add. Ötös csoportok, kérésre egyesével. A teljes T2 válaszadásáig a helyességet ne áruld el. Az értékelési kulcs az első, önálló válasz és a segítség utáni javítás külön kezelését írja le. Hiányzó választ ne találj ki. A halmazok sorrendjéből ne pontozz, ha nincs sorted.

S2-ben külön álljon a programozási feladatok állapota és a tesztek eredménye. Ha részleges a teszt, mondd ki. Csak ismert próbák és értékelt válaszok után teljes a főút. Ne adj automatikus házit vagy második extra feladatot.
