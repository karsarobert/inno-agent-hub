# EP_08 – Tutori útmutató

A tanulói csomagban nincs kész célmegoldás. A tutor feladata magyarázni, diagnosztizálni és a saját kódot értékelni. A források belső szervezését nem kell a tanulónak felsorolni. A 90 perces főút és az egyező normatív tesztek a tanulo_lap.md / ellenorzo_esetek.md fájlban szerepelnek.

## A HTML-hez képest szükséges önálló átvitel

| HTML-ben látott módszer | A gyakorlat új követelménye |
| --- | --- |
| Mérési sorok számlistája | Terméknevek listája, a rendelés sorrendjének és ismétlődésének megtartásával. |
| Minden szó gyakorisága | Csak paraméterben kapott kulcsok; hiányzó keresett szóhoz is 0. |
| Összegző mérési jelentés | Darabonkénti blokk az árjegyzék csatlakoztatásával; aktuális rendelési adatokból. |
| Egyszámos napló | Kétmezős eladási rekord: név és vásárláskori ár. |
| Teljes napló aggregálása | Paraméter szerinti termékszűrés, külön számítás és friss jelentés. |

A HTML mintájának változtatás nélküli bemásolása nem teljesíti ezeket. A módszer és a tanuló saját korábbi beolvasójának újrahasználata viszont kívánatos.

## A1 – Rendelés a szövegfájlból

**Program egészének bemutatása:** A fájl egy sora egy megrendelt darab. A rendelest_beolvas függvény listát ad vissza; a hívó a listát és darabszámát mutatja. Az ismétlődés itt többszöri vásárlást jelent.

**Adott / saját rész:** A függvény neve, fájlnévparamétere és a próbahívás adott. A return [] helykitöltő; még egyetlen sort sem olvas. A rendelesek.txt-ben szélső szóköz, üres sor és sortörés nélküli utolsó sor is van. Minden nem üres, tisztított név szerepel az alapárjegyzékben.

**Magyarázati hangsúly:** Az open szöveges fájlobjektumot ad, a readline egy szöveget. A valóban üres ures.txt első olvasásának eredménye "", vagyis már fájlvég van. Egy üres sor viszont "\n" lenne. A with a blokk végén lezárja a fájlt. A saját feladatban minden sort bejársz, a név szélét tisztítod és a nem üreseket összegyűjtöd.

**Tipikus hiba és diagnózis:** A set elveszítené a rendelési darabokat. A cikluson belüli return csak az első elemet adná. A read eredménye nem sorlista. A relatív fájlnevet a munkamappához viszonyítjuk.

**Elfogadás:**

- Új lista az eredmény; a sorrend és az ismétlődő kávé megmarad.
- A szélső whitespace és az üres sor a kimondott szabály szerint eltűnik.
- Fájlnévparaméterből dolgozik; üres fájlt is kezel; minden szükséges próba ismert.

**Kötelező próbák:** A1.1, A1.2, A1.3.

## A2 – Csak a keresett kulcsszavak gyakorisága

**Program egészének bemutatása:** A büfé szöveges visszajelzéseiből csak a paraméterként megadott szavakat számolod. Az eredmény minden keresett szóhoz egész darabszámot rendel, találat nélkül is nullát.

**Adott / saját rész:** A kulcsszóhalmaz már kisbetűs, nem üres, írásjel nélküli neveket tartalmaz. A return {} most helykitöltő. A szó itt whitespace mentén kapott darab, kisbetűsítve, majd a szélein a . , ! ? ; : " ( ) karakterektől megtisztítva. Belső karaktert nem törlünk; teljes nyelvi elemzés nem cél.

**Magyarázati hangsúly:** A lower új, kisbetűs szöveget ad. A strip argumentuma levágható karakterek gyűjteménye, nem egyben keresett részszöveg. A minta csak egy darabot tisztít és tagságot vizsgál. A saját feladatban fájlsorokat darabolsz split()-tel, és a keresett kulcsok számlálóját frissíted.

**Tipikus hiba és diagnózis:** Az üres fájlnál {} hibás eredmény, ha nem üres a kulcsszóhalmaz. A split(" ") nem ugyanaz, mint a split(). A get/ellenőrzés nem helyettesíti a visszatérési értéket. A lower() önmagában nem távolítja el a vesszőt.

**Elfogadás:**

- Pontosan a paraméterként kapott kulcsok szerepelnek az eredményben, egész értékkel; a hiányzó is 0.
- A kis-/nagybetű és a megadott szélső írásjelek kezelése helyes.
- Nem az összes szó gyakoriságát adja; nem égeti be a finom/gyors/olcsó neveket. A bemenetek megmaradnak.

**Kötelező próbák:** A2.1, A2.2, A2.3, A2.4.

## A3.a – Blokk tételsorai

**Program egészének bemutatása:** Az A1 saját beolvasójának eredményéből friss blokkot készítesz. Egy rendelési darab egy tételsor, névvel és az árjegyzékből vett árral. A blokk nem az eredeti rendelési fájl.

**Adott / saját rész:** A két függvény aláírása, az árjegyzék és a főprogram adott. A beolvasó [] és a mentő pass része még helykitöltő. Az A1-ben már megírt saját beolvasó definícióját hozd át; a főprogramját ne. Az árak egész, nemnegatív forintértékek. A kosár minden neve ismert kulcs; a 0 ár érvényes.

**Magyarázati hangsúly:** A w a megnyitáskor kiüríti a meglévő célt, vagy létrehozza. A write nem ad hozzá automatikusan sortörést, ezért a mintában mindkét szöveg végén szerepel a \n. A saját blokk sorait a kosárból és az árjegyzékből állítod elő; ezt nem végzi el helyetted a minta.

**Tipikus hiba és diagnózis:** A kosár helyett az árjegyzék összes kulcsának bejárása nem a rendelést listázza. Az összesítő sora még nem feltétel ebben a részben. Az A1-eredmény [] helykitöltőjének bent hagyása üres blokkot adna.

**Elfogadás:**

- Az A1 saját beolvasója dolgozik; négy, helyes sorrendű tételsor készül.
- A mentő a kapott kosárból és árjegyzékből dolgozik, a bemeneteket nem módosítja.
- Külön célfájlt ír, minden tételsor végén van sortörés.

**Kötelező próbák:** A3.a.1.

## A3.b – Blokkösszeg és felülírás ellenőrzése

**Program egészének bemutatása:** A tételsorok után egy összesítő sort mentesz. A második futás új blokkot készít, ezért a régi rendelés sorai nem maradhatnak a fájlban.

**Adott / saját rész:** Az A3.a saját tételkiírásod már megvan. Ugyanabban a mentő függvényben kell az aktuális árak összegét számítani. Nincs mennyiségmező: egy kosárelem egy darab, ezért a két kávé kétszer ad árat.

**Magyarázati hangsúly:** A w a fájl megnyitásakor hat, nem csak akkor, amikor az első nem üres tételt kiírjuk. Ezért üres kosárnál is friss cél készül. A 0 kezdőösszeg az üres kosárhoz is helyes.

**Tipikus hiba és diagnózis:** A w cikluson belüli újranyitása mindig törölné az előző tételt. A return korán lezárná a függvényt. A 2180 állandó beírása nem számítás. Az a mód duplázó blokkot eredményezne.

**Elfogadás:**

- Az összeg az aktuális kosár minden darabjának aktuális árából készül.
- A végső összesítő mindig pontosan egy sor; üres kosárnál is elkészül 0 Ft-tal.
- Az ismételt futás nem dupláz, új rendelés után nem marad régi sor. A normatív próbák ismertek.

**Kötelező próbák:** A3.b.1, A3.b.2, A3.b.3, A3.b.4.

## B1.a – Eladási események hozzáfűzése

**Program egészének bemutatása:** A blokk friss eredményt mutatott; a napló több programfutás eladásait őrzi. Minden eladott darabhoz eltárolod a nevét és az akkori árát, pontosvesszővel elválasztva.

**Adott / saját rész:** A mentő és a még nem kész B1.b-összesítő aláírása adott. A főprogramban a mentes_bekapcsolva True, a kosár két darab: kávé és tea. Az eladasok.txt nincs a csomagban: a saját mentőd első helyes futása hozza létre. A két helykitöltő kezdetben 0, 0 kiírást eredményez, fájlírás nélkül.

**Magyarázati hangsúly:** Az a megőrzi a korábbi tartalmat, és a végére ír. A pontosvesszős rekordban a terméknév és az ár külön mező. A saját fájl első sorának például kávé;450 alakúnak kell lennie, nem blokkfeliratnak. A terméknevek nem tartalmaznak pontosvesszőt vagy sortörést; az ár érvényes, nemnegatív egész.

**Tipikus hiba és diagnózis:** A w elveszítené a régi vásárlást. A forráslistát/árjegyzéket nem kell átírni. Egy rekordban az egész árat írjuk, Ft felirat nélkül. A naplófájlt ne írd felül újabb ZIP-kibontással vagy alaphelyzetbe állító kóddal.

**Elfogadás:**

- Első futáskor létrehozza a naplót; minden darab saját, kétmezős, sortöréssel lezárt rekord.
- A második futás megőrzi a korábbi sorokat és még kettőt hozzáfűz.
- A bemeneti kosár és árjegyzék változatlan; a B1.b kiírása még nem kész eredmény.

**Kötelező próbák:** B1.a.1, B1.a.2.

## B1.b – A napló saját árai alapján összesítünk

**Program egészének bemutatása:** A kétmezős sorból nevet és tárolt árat olvasol. Minden rekord egy darab; a bevételt a fájlban rögzített árakból számítod. A mai árjegyzék később változhat, a régi eladás bevétele ettől nem változik.

**Adott / saját rész:** A B1.a saját mentője megmarad. Mielőtt olvasási próbát futtatsz, állítsd False-ra a mentes_bekapcsolva változót, így a próba nem fűz hozzá új adatot. A naplo_proba.txt és naplo_regi_arak.txt változatlan tesztbemenet, nem a saját eladasok.txt naplód. A fájlok minden nem üres sora pontosan két mező; az ár egész és nemnegatív.

**Magyarázati hangsúly:** A strip a sor szélét tisztítja, a split(";") két szöveges mezőt készít, a kicsomagolás nevet ad nekik. A második mező int után számként összegezhető. Ez kötött formátumú szöveg, nem teljes CSV-kezelés. A saját függvény nem keresi újra az árat az arak szótárban.

**Tipikus hiba és diagnózis:** Az int("kávé;450") hibás, előbb mezőkre kell bontani. A mai arak[nev] újraárazná a múltat. A mentési kapcsoló True értéke észrevétlenül hozzáfűzne a próba előtt. Az üres fájlt nem kell megjavítani vagy 0 sorral feltölteni.

**Elfogadás:**

- A darabszám minden rekordot számol, a nulla árút is; a bevétel a tárolt árak összege.
- (0,0) az üres eredmény; általánosan két egészből álló tuple tér vissza.
- A függvény csak olvas; nem használ globális árjegyzéket; a kötelező próbák nem változtatják a tesztfájlokat.

**Kötelező próbák:** B1.b.1, B1.b.2, B1.b.3.

## B1 állapot: ne a futások számát találgassuk

A tiszta munkatér első két mentőfutása két, majd négy rekordot ad. Ha már többször futott a program, attól nem hibás a napló, hogy több sor van benne. A tényleges állapotot olvasd; a következő mentés előtt rögzítsd, hány és milyen korábbi sor van. Az új futásnak pontosan a kosár új rekordjait kell a végéhez tennie. Ne töröld a naplót, és ne kérj újabb mentőfutást csak azért, mert a fájlnézet nem frissült.

B1.b állapotfüggetlen próbákat használ: False kapcsoló + naplo_proba.txt, naplo_regi_arak.txt, ures.txt. A naplo_fajl egyszerre a mentő és olvasó fájlneve a főprogramban, ezért a kapcsoló False értéke előfeltétel e három bemenet kiválasztásakor. Az első, kétfutásos saját eladasok.txt továbbra is megmarad. A ma átírt 999-es ár semmilyen régi naplóbejegyzést nem áraz át.

## Z1 – Önálló termékjelentés

A zaro_feladatok.md szerint először követelmény és teszt, nem előre megadott algoritmus. A saját függvény a kiválasztott termék két aggregátumát adja; a főprogram ment. Elakadásnál külön vizsgáld a mezők olvasását, az egyenlőség szerinti termékszűrést, a darab és bevétel eltérő jelentését, végül a mentést. A fájlban tárolt ár 0-ja valós adat. A keresett szó nem részszöveg-keresés: a név pontosan egyezzen.

Az eladas_minta.txt végén nincs sortörés; a szendvics sora ettől még olvasható. A hiányzó termék nem hibás fájl: 0,0 eredménye és rendes jelentése van. A jelentés minden új próba után frissüljön, a forrás változatlan maradjon. A terminálkimenet önmagában nem bizonyítja a fájlmentést. Kötelező próbák: Z1.1–Z1.5.

## C1 – Egyetlen összetett bővítés

A bovites.md szerinti 15 perc, legalább 42 ismert hátralévő perccel Z1 után. Előbb összesítő szótár, aztán külön mentő; a tuple frissítése új tuple hozzárendelése. Egy termék többféle eladási árral is egy kulcshoz gyűlik. Az üres riportban is van fejléc. A sorted a Python rendezése; magyar nyelvi kolláció nem feladat. A ki nem választott bővítést a két záróteszt nem feltételezi.

## Tesztek és lezárás

A két teszt teljes válaszadása után értékelj. A tesztkódok minden állományt külön teszt_ kezdetű névvel hoznak létre, vagy a változatlan ures.txt-t csak olvassák; a tanuló naplóját nem érintik. Kérdés és válaszazonosító maradjon változatlan. Az eredmény tanulási visszajelzés, nem titkos vizsga vagy automatikus érdemjegy.

Ne indíts automatikusan újabb feladatot a tesztek után. A hiányos programozási rész és a részleges teszt külön folytatási pontot kap. Élő InnoAgent-párbeszédben a tutor következetességét az aktuális modell és eszközök is befolyásolják; a csomag helyi kódellenőrzése nem élő tutori próba.
