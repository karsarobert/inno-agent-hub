# EP_04 – tutorútmutató

Ez a fájl a tanítás támpontja, nem a tanulónak felolvasandó háttérszabály. Új fájlnál előbb egészében mutasd be a célt, utána a kódrész szerepét. A tanuló a célkódot maga módosítja; B1/B2-ben előkészített szerkezetből dolgozik. A B2 régi segédfüggvényei szándékosan készen vannak, a szöveg- és kosárkezelés végleges megoldásai és a Z1 megoldása nem.

## Idő és segítség

Az első blokk T1–S1 összesen 45 perc, a második B1–S2 szintén 45. Egy fájl nem feltétlenül egyetlen üzenet, de ne adj külön mikrolépést minden sorra. B1 a/b és B2 a/b önállóan ellenőrizhető szakasz. A részfeladat megadása után várj a tanuló kódjára, ne folytasd magadtól a kész megoldás további sorainak kiadását.

A rutinszerű állapotmentés ne indítson új tanítási kört. A megadott teszt nem elvégzett teszt. Aktuális kód, futási bizonyíték, segítségszint és következő lépés együtt ad folytatási pontot. Nem kell minden körben az összes útmutatót újra felolvasni vagy minden korábbi példát újra ellenőrizni.

## T1 – Terméknév egységesítése

**Fájl:** szoveg.py. **Keret:** 9 perc.

**A program célja:** A nyers terméknevet számításhoz használható szöveggé alakítod.

**Tanítási hangsúly:** A strip() a két szélről távolítja el a whitespace karaktereket, a lower() kisbetűsít. A sztring megváltoztathatatlan: a visszakapott értéket el kell tárolni vagy vissza kell adni. A belső szóközt és az ékezeteket nem töröljük. A függvény feldolgoz, a hívó rész jelenít meg.

**Segítség és hibakeresés:** A minta új szöveget adó metódust mutat, nem a célfüggvény kész megoldását. Ne diktáld rögtön a strip().lower() teljes return sorát. Egységesítés nem helyesírás-javítás: a kave továbbra sem kávé.

**Elfogadás:** A paramétert dolgozza fel, nem egy beégetett kávé szót ad vissza. A return a feldolgozott szöveget adja. Az eredeti változó és az új érték szerepe világos.

## T2 – Rendelési kód és szelet

**Fájl:** kodresz.py. **Keret:** 7 perc.

**A program célja:** Szöveg egy karakterét és egy részét olvasod ki; üres bemenettel is működő programot készítesz.

**Tanítási hangsúly:** Az indexek 0-tól indulnak. A [0] egyetlen karaktert kér, az [1:] a második karaktertől a végéig tartó szöveget. A szelet nem alakít számmá: a vezető nulla megmarad. Az üres szövegen nincs első karakter, ezért az indexelést meg kell előznie az ellenőrzésnek.

**Segítség és hibakeresés:** A mintát bontsd ki: utolsó karakter, első két karakter, kizárt végpont. Ha a feltétel jó, de az üres ág hiányzik, csak azt kérd javítani. A szögletes zárójelek a kimeneti felirat részei.

**Elfogadás:** A nem üres ág használ indexelést és szeletelést. Az üres esetben nincs IndexError; a 042 megőrzi a vezető nullát.

## T3 – Feltételes számlálás szövegen

**Fájl:** karakterszam.py. **Keret:** 7 perc.

**A program célja:** Saját ciklussal megszámolod egy szöveg magánhangzóit.

**Tanítási hangsúly:** A for egy sztringen karaktereket kap, listán listaelemeket. A számláló a ciklus előtt indul, csak egyezéskor nő, a return a teljes bejárás után áll. A kisbetűs változaton elég a magyar kisbetűs magánhangzókat vizsgálni.

**Segítség és hibakeresés:** A ciklus vázát már ismeri; először természetes nyelven kapja a célt. Segítségnél a számláló és return helyére mutass rá, ne írj helyette kész függvényt.

**Elfogadás:** A paraméter szövegét járja be, nagybetűt is kezel. A számláló nem nullázódik minden körben, üres szövegre 0 tér vissza. Ebben a feladatban valódi feltételes ciklus kell, nem beépített count hívások összege.

## L1 – Kosár módosítása metódusokkal

**Fájl:** listamuveletek.py. **Keret:** 9 perc.

**A program célja:** Hozzáadod és visszavonod az utolsó tételt, majd biztonságosan törölsz egy terméknevet.

**Tanítási hangsúly:** Az append helyben módosít és None-t ad vissza. A pop kivesz és visszaad egy elemet. A remove az első egyező értéket törli; hiánynál hibás lenne. A listán az in teljes elemeket keres. A kosár egyetlen elemét a különböző műveletek eltérően azonosítják.

**Segítség és hibakeresés:** Az ürességvédelmet kódolvasással is ellenőrizd; a két fő próba az előző append miatt nem éri el az üres ágat. Ne állítsd, hogy az üres pop-ág futással igazolt. A tényleges üres törlés B1.3 és Z1.4 része. Egy append+pop+remove összetartozó módosítás; ne kérj minden sor után kész választ.

**Elfogadás:** Az append visszatérési értékét nem rendeli a kosar névhez. A pop és remove előtt megfelelő ellenőrzés áll. A remove csak egy kávét töröl; itt a count használata kifejezetten cél. A hiányüzenet a tényleges keresett termékről szól: tea keresésekor nem állíthatja, hogy nincs kávé.

## L2 – Rendelési sor feldolgozása

**Fájl:** feldolgozas.py. **Keret:** 10 perc.

**A program célja:** Egy vesszővel elválasztott szövegből új, érvényes termékeket tartalmazó listát készítesz.

**Tanítási hangsúly:** A split(",") listát ad, amelyben üres sztringek is lehetnek. Minden darabon külön végezz strip és lower műveletet. Csak a kínálatban lévő elemet add az új kosárhoz; az eredeti darablistából ne törölj bejárás közben. A join a kapott sztringelemeket egy kiírható felirattá kapcsolja.

**Segítség és hibakeresés:** A minta a két metódus kapcsolatát mutatja; a szűrő ciklust a tanuló írja. A L2 kihagyja az ismeretlent; B1 viszont párbeszédben figyelmeztet rá. Ne mosd össze e két feladat különböző szabályát.

**Elfogadás:** A paraméterként kapott kínálatot használja, nem egy külön beégetett listát. Új listát épít, minden darabot egységesít, ismétlődést megtart, return a ciklus után. A sztring visszaalakítása és a lista tárolása külön művelet. A hívó rész join segítségével Rendelés: feliratú szöveget is kiír; a lista kiírása önmagában nem elég.

## S1 – Az első blokk lezárása

**Fájl:** beszélgetés. **Keret:** 3 perc.

**A program célja:** Röviden megnevezed, milyen szöveg- és listaműveletet használtál; megőrizzük a folytatási pontot.

**Tanítási hangsúly:** A sztringmetódus új adatot adhat, a listaművelet a meglévő listát módosíthatja. A megírt függvények később újra használhatók.

**Segítség és hibakeresés:** Részleges választ pontosíts egy rövid magyarázattal; ne nyilváníts mindent bizonyítottnak. A szünet nem része a 90 percnek.

**Elfogadás:** Rövid, valós folytatási pont; nincs új feladat vagy kimenetjóslás.

## B1 – Élő kosár, fizetés nélkül

**Fájl:** kosar_04.py. **Keret:** 18 perc.

**A program célja:** A felhasználó termékeket ad a kosárhoz, visszavonhatja az utolsót, majd lezárhatja a rendelést.

**Tanítási hangsúly:** A kosarat_beker(kinalat) párbeszédet folytat és listát ad vissza. A kosár a ciklus előtt jön létre. Minden bevitelt egységesítünk. A fizetek és a mégse vezérlőszó, ezért nem termékként kezeljük. A fájl a kosár összefoglalásával véget ér; nincs benne diákság, ár- vagy pénzbekérés. A kezdőminta már tartalmazza a ciklust, a listát és a visszaadást. Jelenleg minden nyers szöveget felvesz, és a vége szóra zár: ezt alakítod a büfé szabályaihoz.

**Segítség és hibakeresés:** A fájlban adott ciklusvázat magyarázd, ne írasd újra. B1.a három módosítás: egységesítés, lezáró szó, tagságellenőrzés. B1.b külön, az a próba után következik. A saját L1 pop-részlet újrahasználható; a mégse ág után continue vagy kizáró elif szerkezet is jó. Az adott váz nem a tanuló most önállóan megírt ciklusa.

**Elfogadás:** A ciklus valóban új inputot kér, a lista nem nullázódik minden körben. Csak egységesített, kínálatbeli termék jut a kosárba; a parancsok nem. Üres kosáron a mégse nem okoz hibát. A kész kosarat visszaadja, és nincs fizetési kérdés ebben a fájlban.

## B2 – Összekapcsolás a fizetéssel

**Fájl:** bufe_04.py. **Keret:** 12 perc.

**A program célja:** A saját kosárkezelődet a korábbi ár- és fizetési függvényekhez kapcsolod. Új elem az egységesített, ellenőrzött igen/nem bekérés.

**Tanítási hangsúly:** Az EP_03-ból ismert árlekérdezés, összegzés, blokk, kedvezmény és pénzpótlás előkészített segédkód. Nem kell ezeket újra megírni. Az új igen/nem függvény logikai értéket ad vissza: a bool("nem") igaz lenne, ezért konkrét szöveget vizsgálunk. A kosárösszeg ellenőrzése megelőzi a diákság és pénz bekérését. A fájl végén már kész a főprogram szerkezete, az üres kosár ága és a kiírások. A MODOSITSD jelöléseknél négy kezdőértéket cserélsz saját függvényhívásra vagy számításra, és hozzáadsz egy fizetési hívást.

**Segítség és hibakeresés:** Olvasd célzottan az átvitt két definíciót, az igen/nem függvényt és a jelölt főprogramrészt. Az előkészített ár- és fizetési részeket csak hiba esetén kell részletesen vizsgálni. Ne kérd a teljes fájl bemásolását, ha olvasni tudod. A négy kezdőérték és az egy hívás módosítása egy összetartozó lépés; ne várj minden sor után kész választ. Az ellenőrzött működés nem bizonyítja a kész váz önálló megírását.

**Elfogadás:** A saját kosárfüggvényt használja; nem egy rögzített lista kerül a helyére. Az igen/nem bekérés minden új választ egységesít, megfelelő bool értéket ad. Üres kosárnál nincs diákság- vagy pénzkérdés. A teljes kosárra számol, és visszajárót csak elégséges összeg után ír.

## Z1 – Önálló törlés név szerint

**Fájl:** onallo.py. **Keret:** 12 perc.

**A program célja:** Új függvényben kapcsolod össze a szöveg egységesítését, a listatagságot és a törlést.

**Tanítási hangsúly:** A tetelt_torol(kosar, keresett_termek) a paraméterben kapott listát módosítja. Az egységesített terméknév első előfordulását törli. Siker esetén True, hiány esetén False az eredmény. A függvény nem kérdez és nem ír ki. A főprogram mutatja meg az eredményt és a listát.

**Segítség és hibakeresés:** Első próbálkozás előtt csak cél, szabály és teszttábla; ne adj kész algoritmust vagy próbahívásokat. Valós elakadáskor fokozatosan segíts. Az algoritmus és a teszthívások önállóságát külön értékeld; ne legyen a tesztelő segítségből megalapozatlan teljes önállóság.

**Elfogadás:** Az első egyezést törli; a kávé ismétlődése megmaradhat. A paramétereket használja, a keresést egységesíti, bool értéket ad. Hiányzó terméknél és üres listán nincs kivétel és nem módosul a lista. A tanuló saját próbahívásai és a lista utóállapotai is ismertek.

## S2 – Lezárás és folytatási pont

**Fájl:** beszélgetés. **Keret:** 3 perc.

**A program célja:** Röviden összefoglalod, hogyan jut a program a nyers terméknévtől a kosárig és a fizetésig.

**Tanítási hangsúly:** A szövegfeldolgozás új szöveget állít elő, a listaműveletek módosítják a kosarat, a régi számító függvények a kész listát dolgozzák fel.

**Segítség és hibakeresés:** Nincs kötelező házi feladat, új záróvizsga vagy kimenetjóslás. Ha részfeladat maradt, attól az óra lezárható, de nem nevezhető az egész főút teljesítettnek.

**Elfogadás:** A lezárás a tényleges eredményen alapul, és egyértelműen kimondja, hogy az óra véget ért.

## A korábbi teszt tanulságai itt kötelező ellenőrzési pontok

- B1-ben semmilyen későbbi pénzkérdés nincs. Ha a tanuló pénzkérdést lát, ellenőrizd, melyik fájlt futtatja; ne kérj fiktív adatokat csak azért, hogy átugorjátok a későbbi részt.
- B2-ben a kosár alapösszegét vizsgáljuk a diákság és fizetés előtt. Az üres ág kiír, az else ág kérdez és fizettet. Ezt az egy sorrendet használd következetesen.
- A visszajáró sor időzítése ugyanúgy a működés része, mint az értéke. Korai visszajáró, kétszeri végösszeg vagy kevert futáskimenet esetén célzott ellenőrzés kell.
- Z1-ben a tesztek külön új listákkal indulnak. A keresett tea nincs a listában, ettől a próba helyes. Ne változtass a tesztadaton azért, hogy találat legyen.
- Ha egy függvény saját munka, de a teszteket konkrét segítséggel írta meg, a visszajelzés például: „A függvényt önállóan, a próbahívásokat segítséggel készítetted el.”
- A záró szóbeli összefoglalóban egy hiányzó elemre röviden térj vissza. A tutor által kimondott magyarázat nem a tanuló önálló magyarázata.

## Futtatás és technikai akadály

A .py fájlok egyetlen gyökérmappában vannak, a Futtatás gomb terminálja is ott álljon. Ne kérj általános cd-t, és ne nyiss új alkönyvtárat. Hiba esetén a valódi parancs, az aktuális fájl és a tényleges futtatóterminál alapján diagnosztizálj. Az agent.md részletes szabályai érvényesek. A technikai akadályt ne könyveld el fogalmi hiánynak.

## A kezdőminták értelmezése

A T1 függvény változatlan szöveget, T3 nullát, L2 üres listát, Z1 False értéket ad. Ez a futtatható kiinduló állapot; az elvárt viselkedést még nem valósítja meg. Egy helyesnek tűnő üres próba ezért nem elég: a nem üres pozitív eset és a kód szerkezete is szükséges. B1 kész ciklusa még minden szöveget hozzáad és vége szóra zár; az ellenőrzéseket a tanuló írja hozzá. B2 igen/nem mintája csak egyszer kérdez, főprogramja üres kezdőlistával fut. Ezek szándékos hiányok, nem kész megoldások.

B2 kész segédfüggvényeinek elfogadható használata nem bizonyítja, hogy a tanuló most újra önállóan megírta a teljes fizetési ciklust. A mai teljesítmény: saját EP_04 részek, helyes összeépítés és ellenőrzött működés.
