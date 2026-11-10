# EP_09 – Tutori magyarázat és diagnózis

Módszertani alap: EP_08/EP_07, az EP_05 magyarázó, saját kódírásra építő menetével. Nincs kész A1–C1 célmegoldás a csomagban. A tutor a valódi kódot olvassa, magyaráz és a hallgató futásait értékeli. Nem írja és nem futtatja helyette a programot.

## Miért nem elég a HTML kész mintája?

| HTML-ben látott módszer | A gyakorlat új követelménye |
| --- | --- |
| Egész vagy pozitív érték bekérése | Paraméter szerinti elégséges önálló pénzfelajánlás, pontos/0 összeggel is. |
| Kölcsönzési értékellenőrzés | Árjegyzékkulcs és darabszám ellenőrzése, hívói döntéssel. |
| Kétmezős mérési rekord | Hárommezős eladás, pozitív darab és nemnegatív történeti egységár. |
| Számlista összesítése | Rekordszám, mennyiség és darab×egységár szerinti bevétel elkülönítése. |
| Jelzett kihagyásos mérési riport | Hibás kosárnál fizetés tiltása, az összes tételhiba összegyűjtésével. |

A módszer és a saját függvény újrahasználata kívánatos; a HTML programjának változtatás nélküli bemásolása nem teljesíti a követelményt.

## A1 – Fizetés újrakérése hibás összeg után

**Az egész bemutatása:** A fizetest_beker(fizetendo) addig kér egész forintösszeget, amíg az adott önálló felajánlás legalább a fizetendő. A függvény az átadott összeget adja vissza; a főprogram a különbséget mutatja.

**Adott/saját rész:** Adott a függvény aláírása és a főprogram. A return 0 helykitöltő még nem kér adatot, ezért az induló -800 Ft nem helyes visszajáró, hanem hiányos programjelzés. A fizetendo paraméterről feltételezzük, hogy nemnegatív egész. Minden új válasz új, önálló felajánlás: az összegek nem halmozódnak.

**Magyarázati hangsúly:** Az input szöveget ad. A ValueError csak a sikertelen egész konverziót jelzi; az 500 sikeresen egész lehet, de 800 Ft-hoz kevés. A saját függvényben a ciklust a sikeres return zárja le. Az analóg minta csak konvertál, a fizetési feltételt neked kell hozzáadnod.

**Tipikus hiba:** Csupasz except elnyelné a megszakítást is; a kevés pénz nem konverziós hiba. Az input bekérésének a cikluson belül kell ismétlődnie. A -10-et nem kell külön másik hibatípussá alakítani: nem éri el a nemnegatív fizetendőt.

**Elfogadás:**

- Konverziós és elégtelen összeghez eltérő, értelmes üzenet tartozik.
- Csak megfelelő egész összeg tér vissza; a pontos összeg és a 0 fizetendő is helyes.
- A fizetendő valódi paraméter; nincs beégetett 800 vagy rejtett részfizetés.

**Kötelező próbák:** A1.1, A1.2, A1.3.

## A2 – Érvénytelen tétel jelzése raise segítségével

**Az egész bemutatása:** A tetel_osszege(termek, darab, arak) ismert termék és pozitív darabszám esetén a tétel összegét adja. Ismeretlen termék vagy nem pozitív darab esetén ValueError-t jelez. A hívó kezeli és közli a hibát.

**Adott/saját rész:** Az aláírás, az árjegyzék és a próbaadat adott. A return 0 helykitöltő. A darab egész szám, a termék már tisztított, nem üres szöveg; az árjegyzék értékei nemnegatív egész forintárak. A függvény nem kérdez, nem ír ki és nem módosít adatot.

**Magyarázati hangsúly:** A függvény ismeri a megengedett értéket, ezért ott jelez raise-zel. Az except a hívóban van; az as hiba a konkrét kivétel üzenetéhez ad nevet. A célfüggvény kétféle hibás értéket vizsgál, és helyes esetben az árjegyzékből számol.

**Tipikus hiba:** A 0 eredmény nem bizonyít hibát, mert ingyenes termék létezik. A ValueError-t ne ugyanott nyeld le, ahol dobod: a függvény hívója kezeli. Az arak.get(termek,0) elrejtené az ismeretlen terméket.

**Elfogadás:**

- Érvényes adatra egész összeget ad, tiltott értékre ValueError-t jelez; nincs hibajelző szöveg vagy 0-ra álcázott hiba.
- A hívó érthető üzenetet ad, és nem állít sikeres tételösszeget hiba után.
- Az árjegyzékparamétert használja, az adatokat megőrzi; a 0 ár helyes.

**Kötelező próbák:** A2.1, A2.2, A2.3, A2.4, A2.5.

## A3.a – Hárommezős eladási sor értelmezése

**Az egész bemutatása:** Az eladast_ertelmez(sor) egy nem üres termék;darab;egységár sorból (termek, darab, egysegar) tuple-t készít, vagy ValueError-t jelez. A rekord eladási mennyiséget őriz, ezért nem minden sor egyetlen darab.

**Adott/saját rész:** A naplo.py két függvénye még helykitöltő; most csak az első készül. A közvetlen sorpróbát vizsgáljuk, a beolvasó ([],[],0) eredménye ebben a szakaszban szándékosan hiányos. Minden sor szöveg; a termék nem tartalmaz pontosvesszőt vagy sortörést. Ez kötött elválasztott szöveg, nem teljes CSV.

**Magyarázati hangsúly:** A split szövegmezőket ad, az int külön alakít számmá. A saját formátumban három mező van: a számukat a kicsomagolás előtt ellenőrizd. A név szélei tisztítandók, a darab pozitív, az egységár nemnegatív egész. Hibánál nem adunk kitalált jó rekordot.

**Tipikus hiba:** Az int-et nem a teljes pontosvesszős sorra alkalmazzuk. A negatív mérés a HTML-ben lehetett érvényes; itt a negatív egységár tiltott üzleti adat. A három tuple-mező nem felcserélhető.

**Elfogadás:**

- Három mező jelentése és típusa helyes; a whitespace és a hiányzó végső sortörés megfelelően kezelt.
- Mezőszám, üres név, hibás konverzió és tiltott számtartomány ValueError-t okoz.
- A 0 egységár megengedett, a 0 darab tiltott; a függvény nem ír ki.

**Kötelező próbák:** A3.a.1, A3.a.2, A3.a.3, A3.a.4.

## A3.b – Sérült napló feldolgozása sorszámos hibákkal

**Az egész bemutatása:** A naplot_beolvas(fajlnev) a teljes fájlból érvényes rekordlistát, (fizikai_sorszám, hibaüzenet) hibalistát és az üres sorok számát adja vissza. A jó sorokat a hibásak után is feldolgozza.

**Adott/saját rész:** Az A3.a saját sorértelmeződ megmarad; a második függvényt most írod meg. Minden fájl UTF-8. Az eladasok_jo.txt utolsó sora sortörés nélkül zárul. A hibás nem üres sor és az üres/whitespace sor eltérő kategória. Az egész fájlt érintő I/O-hibát a függvény nem nyeli el.

**Magyarázati hangsúly:** A konverzió a cikluson belül kap kezelőt. A continue után a következő elemmel folytatunk; a 0 jó érték marad. A saját feladatban int helyett a saját eladast_ertelmez függvényedet hívod, és az eredeti fájl fizikai sorszámát is megőrzöd. A str(hiba) szöveget tároljuk, nem az except utáni hiba változóra hagyatkozunk.

**Tipikus hiba:** A ciklus körüli ValueError-kezelő az első hibánál megszakítaná a bejárást. A hiba listájába az excepten belül tedd a str(hiba) szöveget. A return a teljes ciklus után legyen, különben a későbbi jó sorok elvesznek.

**Elfogadás:**

- Az érvényes rekordok sorrendje, ismétlődése és eladási mennyisége megmarad.
- A hibák fizikai sorszáma és nem üres oka megvan, az üres sor külön kategória.
- Hiányzó fájl hibája továbbterjed; nincs kitalált jó 0 árú rekord vagy csendes except: pass.

**Kötelező próbák:** A3.b.1, A3.b.2, A3.b.3, A3.b.4, A3.b.5.

## B1 – Fájlszintű hibák és őszinte riportüzenetek

**Az egész bemutatása:** A riportot_keszit(bemenet,kimenet) a saját A3 beolvasód, a kész összesítő és a kész mentő együttműködését szervezi. Fájlszintű hibánál False-t, befejezett mentés után True-t ad. A főprogram finally üzenete csak lezárást jelent.

**Adott/saját rész:** Az A3 két saját függvénydefinícióját át kell hoznod a helykitöltők helyére. A naplo_adatait_osszesit és osszesitest_ment már kész, nem új feladat. Az összesítő a mennyiségeket adja össze, a bevételt darab*egységár alapján számolja. A mentő külön w célfájlt ír. A mai árjegyzék nem forrása a történeti bevételnek.

**Magyarázati hangsúly:** A finally a kezelt hibánál is lefut, ezért nem lehet benne sikerüzenet. A saját riportban különüljön el a beolvasás és a mentés hibája. Hiányzó bemenet után a mentő nem hívható: különben egy régi riport üres sikeres adattal felülíródna.

**Tipikus hiba:** A FileNotFoundError a mentésnél is előfordulhat, ezért ne egy nagy try-ból írj mindkettőre Nincs bemenet üzenetet. OSError kezelő elé kerüljön a speciális FileNotFoundError. A True/False visszatérés nem írhatja felül a hibát egy finally-beli return-nel.

**Elfogadás:**

- A fájlhibák és a sorhibák eltérő szinten kezeltek. Hiányzó/olvashatatlan forrás után nem indul mentés.
- Mentési hiba False és célzott üzenet; sikerüzenet csak rendes mentés után van.
- A finally nem állít sikert, a régi cél hiányzó bemenet után változatlan.
- A jó rekordok száma nem azonos az eladott darabszámmal; az előkészített segítők szerepét felismeri.

**Kötelező próbák:** B1.1, B1.2, B1.3, B1.4, B1.5.

## A3 és B1 határai

A3.a alatt a fájlbejáró még ([],[],0). A3.b előtt a közvetlen sorpróbát állítsa vissza jó sorra vagy kommentelje ki, különben egy szándékosan rossz tesztsor akadályozhatná a fájlpróbát. A sorfüggvény és beolvasó nem printel; a főprogram mutatja az adatokat. Az excepthez kötött hiba objektumot nem szabad a blokk után tárolóként használni; a str(hiba) üzenet az excepten belül kerüljön a listába.

A3.b.5 továbbterjedő FileNotFoundError-ját a B1.2 hiányzó forráspróbája is bizonyítja, ha ugyanaz a saját A3-definíció dolgozik ott. Ezt nem kell még egyszer szándékosan kezeletlen hibával futtatni. Egy normatív tábla önmagában nem bizonyít végrehajtást.

B1-ben a két kész segédfüggvényt előbb röviden mutasd be: az egyik rekordokat összesít, a másik kapott adatot ment. A kézzel összeadható jó alap 4 rekord/7 darab/1750 Ft, a vegyesben 5 hibás és 1 üres sor. A mentő a hibák számát és a részleges állapotot tárolja; a sorszámos okok az A3 visszatérési hibalistájában megmaradnak. Nem kérünk B1-ben újabb részletes hibajegyzék-mentést.

A finally a B1 főprogram riportkísérletét fogja körül: a lezáró üzenet siker és kezelt hiba után is jön. A rendes True/False döntés a riportot_keszit feladata. A beolvasó és mentő saját with blokkjai zárnak, nem új kézi close/finally kombináció.

## Z1 – Önálló döntés a teljes kosárról

Először csak a követelményt és a próbákat add. A Z1 a korábbi függvényre épít, de a részleges összeg helyett teljes ellenőrzési döntést kér. Minden hibát gyűjteni kell; az első hibánál return nem felel meg. Ugyanakkor hiba esetén a jó tételek összege sem engedély fizetésre. A None és a 0 megkülönböztetése kulcsfontosságú.

Elakadásnál külön nézd meg, hogy a tételfüggvény hívása, a hibagyűjtés, a végső döntés vagy a hívói üzenet bizonytalan. Kész célciklust elsőre ne adj. A kosár struktúrája és az árjegyzék típusai előfeltételek, nem kell általános adatvalidáló keretrendszert építeni.

## C1 – Írás csak teljes adatellenőrzés után

15 perc, legalább 42 ismert fennmaradó perccel, Z1 után/T1 előtt. Saját A2 és Z1 definíció, utána a kosarat_ment. A cél megnyitása előtt legyen végleges döntés. Egy jó első tétel után fellépő második tételhiba sem engedély részleges írásra. Üres kosár nem hiba és nem készít fájlt.

Ez az adatellenőrzési hibák miatti részleges hozzáfűzést akadályozza meg, nem atomi I/O-tranzakció. Írás közbeni OSError után a fájl lehet részben változott, erre False és hibaüzenet jár. A régi napló sortöréses lezárása előfeltétel. C1 ismételt futás új esemény; nézetfrissítés helyett ne kérj felesleges új mentést.

## Kipróbálási fókuszok

Új munkatér: bemutatkozás, A1 egészének magyarázata és önálló szerkesztés kérése. Valódi inputnál a tutor a terminálhoz irányít. A2 nulla árát elfogadja. A3.a alatt a még helykitöltő beolvasót nem kéri számon. A3.b jó soraiban 4 rekord és 7 darab szerepel. B1 hiányzó forrásnál nem nyitja meg a célt, a finally üzenetből nem következtet sikerre. Z1-nél előre nem ad kész algoritmust, és hibás kosárnál nem engedélyez részfizetést. A már ismert próbát nem ismételteti.

Tesztek: eredeti kérdésazonosítók, teljes kódok, a teljes T2 után visszajelzés. A külön kódértelmezési szakasz nem új programozási feladat. A pontozás és a programozási állapot külön marad. A tanuló megoldását a tutor nem futtatja és nem írja át.

A csomag helyi kód- és tartalomellenőrzése nem élő InnoAgent-párbeszéd. A valódi tutori következetesség az aktuális modelltől, alkalmazástól és engedélyezett eszközöktől is függ.
