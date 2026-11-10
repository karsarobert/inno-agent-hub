# EP_09 – Kivételkezelés a büfés alkalmazásban

Két 45 perces magyar nyelvű Python-gyakorlat az EP_09.html után. A HTML mérési és kölcsönzési példáinak módszerét most fizetésre, eladási rekordokra és kosárellenőrzésre alkalmazod. A csomag önálló: korábbi megoldásfájlok nem szükségesek, a most megírt saját függvényeidet használod újra.

A tutor új fájl előtt bemutatja a teljes célt, az adatokat és az adott/saját részeket. Rövid analóg mintát magyaráz, majd egy összetartozó szerkesztést kér. Te szerkesztesz, mentesz és a Futtatás gombbal futtatsz. A programozási részben nincs előzetes kimenetjóslás; a záró kódismereti teszt külön szakasz.

A kezdőfájlok futtatható helykitöltők. A return 0, a ("",0,0), az üres listák és a False nem célmegoldások. A hibamentes indulás önmagában nem kész feladat. A2/A3.a után a saját ValueError-t a hívóban kezeled; a hiányzó teljes napló FileNotFoundError-ját A3.b továbbengedi a B1 hívójához.

## Munkamappa és futtatás

A ZIP tartalmát új, üres InnoAgent-munkatér gyökerébe bontsd ki. A preset.json, agent.md, .py és .txt fájlok egymás mellett legyenek. A Futtatás gomb terminálja a megnyitott program mappájában álljon. A relatív fájlnév a munkamappához viszonyul, nem automatikusan a .py fájl helyéhez. Nincs feladatonkénti mappaváltás.

A1 megírása után a program inputra vár: a válaszokat a terminálba írd. Futó bekérésbe ne írj shellparancsot és ne indíts második példányt. Ctrl+C megszakít; >>> Python-promptból exit() léptet ki. Ha nincs Python vagy technikai akadály van, kérj oktatói segítséget.

Írási futás után a tényleges célfájlt is nyisd meg. Ha a változás nem látszik, frissítsd a fájlnézetet vagy nyisd újra a fájlt. A régi jelentés megléte nem a mostani futás sikerének bizonyítéka.

## Időterv

| Első 45 perc | Perc | Második 45 perc | Perc |
| --- | --- | --- | --- |
| START – Bemutatkozás és érdemi kezdés | 2 | B1 – Fájlszintű hibakezelés | 6 |
| A1 – Fizetés újrakérése | 8 | Z1 – Önálló kosárellenőrzés | 12 |
| A2 – Érvénytelen tétel és raise | 10 | T1 – Elméleti teszt | 10 |
| A3.a – Rekord értelmezése | 9 | T2 – Kódismereti teszt | 15 |
| A3.b – Sérült napló beolvasása | 14 | S2 – Értékelés és lezárás | 2 |
| S1 – Rövid összegzés | 2 | | |
| **Összesen** | **45** | **Összesen** | **45** |

Tömörített tervezett keret, nem hallgatókkal mért teljesítési idő. A magyarázat, szerkesztés és próba része, a szünet külön idő. Lassabb haladásnál a félbemaradt rész pontos folytatási pontot kap; nem kész célkódot. A tesztek és lezárás 27 percét fenntartjuk.

C1 egyetlen 15 perces összetett bővítés. Z1 után, T1 előtt választható, legalább 42 ténylegesen fennmaradó perccel. A teljes tervezett út C1-gyel 105 perc, ezért 90 percbe csak megtakarított idővel fér. Nincs automatikus második extra vagy kötelező házi.

## Adatformátum

A naplósor **termék;darab;egységár**. Egy rekord több eladott darabot is jelenthet. A terméknév nem üres, a darab pozitív egész, az egységár nemnegatív egész. A 0 ár érvényes, a 0 darab tiltott. A történeti árakat a naplóból vesszük, nem a mai árjegyzékből. A pontosvessző nem szerepelhet mezőn belül; ez egyszerű kötött szövegformátum, nem teljes CSV-kezelés.

A kilencedik lecke formátuma szándékosan hárommezős, az EP_08 kétmezős naplóját nem másoljuk át változtatás nélkül. Az öt csomagolt adatfájl változatlan bemenet. Pontos tartalom: adatok.md. Az üres sor külön kategória, a hibás sor nem helyettesíthető jó 0 értékkel.

## A1 – Fizetés újrakérése hibás összeg után

**Fájl:** `fizetes.py`. **Tervezett idő:** 8 perc.

### Mit csinál majd a program?

A fizetest_beker(fizetendo) addig kér egész forintösszeget, amíg az adott önálló felajánlás legalább a fizetendő. A függvény az átadott összeget adja vissza; a főprogram a különbséget mutatja.

### Mi adott, mit írsz te?

Adott a függvény aláírása és a főprogram. A return 0 helykitöltő még nem kér adatot, ezért az induló -800 Ft nem helyes visszajáró, hanem hiányos programjelzés. A fizetendo paraméterről feltételezzük, hogy nemnegatív egész. Minden új válasz új, önálló felajánlás: az összegek nem halmozódnak.

### Rövid analóg minta

```python
while True:
    try:
        emelet = int(input("Hányadik emelet?\n"))
    except ValueError:
        print("Egész számmal add meg.")
        continue
    break
print("Megadott emelet:", emelet)
```

Az input szöveget ad. A ValueError csak a sikertelen egész konverziót jelzi; az 500 sikeresen egész lehet, de 800 Ft-hoz kevés. A saját függvényben a ciklust a sikeres return zárja le. Az analóg minta csak konvertál, a fizetési feltételt neked kell hozzáadnod.

### Most te alakítsd át

1. A függvényben ciklussal kérj be egész összeget. Csak a konverzió várható ValueError-ját kezeld, érthető újrakérő üzenettel.
2. Sikeres konverzió után ellenőrizd a fizetendo paraméterhez képest az összeget. Kevés pénznél jelezz és kérj új választ, ne add hozzá az előzőhöz.
3. Elég pénznél térj vissza az egész összeggel. A főprogram meglévő kivonása számolja a visszajárót.
4. Ments és futtass. A válaszokat a terminálba írd; futó inputhoz ne küldj shellparancsot. Végezd el a három próbát.

### Kész, ha

- Konverziós és elégtelen összeghez eltérő, értelmes üzenet tartozik.
- Csak megfelelő egész összeg tér vissza; a pontos összeg és a 0 fizetendő is helyes.
- A fizetendő valódi paraméter; nincs beégetett 800 vagy rejtett részfizetés.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | fizetendo=800; terminálválaszok egymás után: alma, -10, 500, 1000 | Az alma konverziós hiba; -10 és 500 kevés. Az utolsó önálló felajánlás 1000, visszajáró 200 Ft. Nem adódnak össze a felajánlások. |
| A1.2 | fizetendo=800; terminálválasz: 800 | Visszatérés 800, visszajáró 0 Ft; nem kér újra. |
| A1.3 | fizetendo=0; terminálválaszok: -1, 0 | -1 elutasított; 0 elfogadott, visszajáró 0. Csak a paraméter változik. |

Kapcsolódó háttér: [EP_09.html](EP_09.html#bekeres).

## A2 – Érvénytelen tétel jelzése raise segítségével

**Fájl:** `tetel.py`. **Tervezett idő:** 10 perc.

### Mit csinál majd a program?

A tetel_osszege(termek, darab, arak) ismert termék és pozitív darabszám esetén a tétel összegét adja. Ismeretlen termék vagy nem pozitív darab esetén ValueError-t jelez. A hívó kezeli és közli a hibát.

### Mi adott, mit írsz te?

Az aláírás, az árjegyzék és a próbaadat adott. A return 0 helykitöltő. A darab egész szám, a termék már tisztított, nem üres szöveg; az árjegyzék értékei nemnegatív egész forintárak. A függvény nem kérdez, nem ír ki és nem módosít adatot.

### Rövid analóg minta

```python
def terem_ellenoriz(ferohely):
    if ferohely < 1:
        raise ValueError("A férőhely legyen pozitív.")
    return ferohely

try:
    terem_ellenoriz(0)
except ValueError as hiba:
    print("Nem foglalható terem:", hiba)
```

A függvény ismeri a megengedett értéket, ezért ott jelez raise-zel. Az except a hívóban van; az as hiba a konkrét kivétel üzenetéhez ad nevet. A célfüggvény kétféle hibás értéket vizsgál, és helyes esetben az árjegyzékből számol.

### Most te alakítsd át

1. A függvényben ismeretlen termékre és nem pozitív darabra külön, érthető ValueError üzenetet adj.
2. Érvényes adatra a paraméterben kapott árjegyzék megfelelő árának és a darabszámnak a szorzatát add vissza. A nulla ár érvényes.
3. A főprogram hívását egészítsd ki ValueError kezeléssel. Sikeres összeg csak sikeres hívás után jelenjen meg; hibánál ne használj korábbról megmaradt eredményt.
4. A főprogram próbaadatait módosítva végezd el az A2-próbákat. A későbbi Z1-be a saját függvénydefiníciódat viszed tovább.

### Kész, ha

- Érvényes adatra egész összeget ad, tiltott értékre ValueError-t jelez; nincs hibajelző szöveg vagy 0-ra álcázott hiba.
- A hívó érthető üzenetet ad, és nem állít sikeres tételösszeget hiba után.
- Az árjegyzékparamétert használja, az adatokat megőrzi; a 0 ár helyes.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | termek="kávé", darab=2, alapárjegyzék | 900 egész érték; a főprogram sikerüzenete ezt mutatja. |
| A2.2 | termek="víz", darab=3 | 0 egész érték; nem hiba. |
| A2.3 | termek="kakaó", darab=1 | ValueError, az üzenet az ismeretlen termékre utal. A főprogram közli a hibát, nincs Tételösszeg sikerüzenet. |
| A2.4 | Ismert termék; darab=0, majd külön próbában -2 | Mindkét eset ValueError, pozitív darabszámra utaló üzenettel. |
| A2.5 | A kávé árát a próba előtt 500-ra változtatod; termek="kávé", darab=2 | 1000; a függvény csak a paraméterben kapott szótárat használja, a bemeneteket nem módosítja. |

Kapcsolódó háttér: [EP_09.html](EP_09.html#raise).

## A3.a – Hárommezős eladási sor értelmezése

**Fájl:** `naplo.py`. **Tervezett idő:** 9 perc.

### Mit csinál majd a program?

Az eladast_ertelmez(sor) egy nem üres termék;darab;egységár sorból (termek, darab, egysegar) tuple-t készít, vagy ValueError-t jelez. A rekord eladási mennyiséget őriz, ezért nem minden sor egyetlen darab.

### Mi adott, mit írsz te?

A naplo.py két függvénye még helykitöltő; most csak az első készül. A közvetlen sorpróbát vizsgáljuk, a beolvasó ([],[],0) eredménye ebben a szakaszban szándékosan hiányos. Minden sor szöveg; a termék nem tartalmaz pontosvesszőt vagy sortörést. Ez kötött elválasztott szöveg, nem teljes CSV.

### Rövid analóg minta

```python
sor = "R12;7\n"
azonosito, szam_szoveg = sor.strip().split(";")
print(azonosito, int(szam_szoveg))
```

A split szövegmezőket ad, az int külön alakít számmá. A saját formátumban három mező van: a számukat a kicsomagolás előtt ellenőrizd. A név szélei tisztítandók, a darab pozitív, az egységár nemnegatív egész. Hibánál nem adunk kitalált jó rekordot.

### Most te alakítsd át

1. A függvény követeljen pontosan három mezőt; hibás mezőszámra raise ValueError jelezze a formátumot.
2. A terméknevet tisztítsd, üres névre jelezz. A második és harmadik mezőt alakítsd egésszé.
3. A darab legfeljebb 0, illetve a negatív egységár ValueError-t jelentsen. Egyébként a szöveg és a két egész tuple-je térjen vissza.
4. A közvetlen főprogrambeli sorpróbához adj ValueError kezelést. Végezd el a próbákat; A3.b előtt a közvetlen sort érvényes adatra állítsd vissza, vagy a sorpróbát kommenteld ki.

### Kész, ha

- Három mező jelentése és típusa helyes; a whitespace és a hiányzó végső sortörés megfelelően kezelt.
- Mezőszám, üres név, hibás konverzió és tiltott számtartomány ValueError-t okoz.
- A 0 egységár megengedett, a 0 darab tiltott; a függvény nem ír ki.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.a.1 | sor=" kávé ; 2 ; 450\n" (a \n itt valódi sortörés) | ("kávé", 2, 450): szöveg és két egész, a szélső whitespace eltűnik. |
| A3.a.2 | sor="víz;3;0", végső sortörés nélkül | ("víz", 3, 0); a nulla egységár érvényes. |
| A3.a.3 | Külön próbák: `hibas sor`, `kávé;1;450;extra`, `;1;100` | Mindhárom ValueError: hibás mezőszám vagy üres terméknév; a hívó kezeli a jelzést. |
| A3.a.4 | Külön próbák: `tea;ketto;350`, `tea;0;350`, `tea;1;-50` | Mindhárom ValueError: konverzió, nem pozitív darab, illetve negatív egységár. |

Kapcsolódó háttér: [EP_09.html](EP_09.html#rekordok).

## A3.b – Sérült napló feldolgozása sorszámos hibákkal

**Fájl:** `naplo.py`. **Tervezett idő:** 14 perc.

### Mit csinál majd a program?

A naplot_beolvas(fajlnev) a teljes fájlból érvényes rekordlistát, (fizikai_sorszám, hibaüzenet) hibalistát és az üres sorok számát adja vissza. A jó sorokat a hibásak után is feldolgozza.

### Mi adott, mit írsz te?

Az A3.a saját sorértelmeződ megmarad; a második függvényt most írod meg. Minden fájl UTF-8. Az eladasok_jo.txt utolsó sora sortörés nélkül zárul. A hibás nem üres sor és az üres/whitespace sor eltérő kategória. Az egész fájlt érintő I/O-hibát a függvény nem nyeli el.

### Rövid analóg minta

```python
ertekek = []
hibak = []
for szoveg in ["10", "alma", "0"]:
    try:
        ertek = int(szoveg)
    except ValueError as hiba:
        hibak.append(str(hiba))
        continue
    ertekek.append(ertek)
print(ertekek, len(hibak))
```

A konverzió a cikluson belül kap kezelőt. A continue után a következő elemmel folytatunk; a 0 jó érték marad. A saját feladatban int helyett a saját eladast_ertelmez függvényedet hívod, és az eredeti fájl fizikai sorszámát is megőrzöd. A str(hiba) szöveget tároljuk, nem az except utáni hiba változóra hagyatkozunk.

### Most te alakítsd át

1. with/open segítségével a paraméterben kapott fájlt olvasd. A sorszám minden fizikai sornál nőjön, az üresnél is.
2. A tisztítás után üres sort külön számláld és hagyd ki. A többi sorra hívd meg a saját eladast_ertelmez függvényedet.
3. Az adott sor ValueError-ját a cikluson belül kezeld: sorszámot és nem üres hibaüzenetet gyűjts, majd folytasd. Jó eredmény új rekordként kerüljön a listába.
4. A végén (rekordok, hibak, ures_sorok) térjen vissza. Ne kérdezz, ne írj ki, ne módosítsd a forrást. FileNotFoundError/OSError továbbterjed; nem tér vissza helyettük üres sikeres adat.
5. A jó, vegyes, üres és csak hibás bemenettel végezd el a próbákat. A hiányzó fájl esetét a következő B1 hívójában, egyszer célzottan fejezzük be.

### Kész, ha

- Az érvényes rekordok sorrendje, ismétlődése és eladási mennyisége megmarad.
- A hibák fizikai sorszáma és nem üres oka megvan, az üres sor külön kategória.
- Hiányzó fájl hibája továbbterjed; nincs kitalált jó 0 árú rekord vagy csendes except: pass.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.b.1 | eladasok_jo.txt | Rekordok sorrendben: (kávé,2,450), (tea,1,350), (víz,3,0), (kávé,1,500); hibák=[]; üres sorok=0. |
| A3.b.2 | eladasok_vegyes.txt | Ugyanaz a 4 jó rekord; hibalista 5 elemmel, sorszámok 2,6,8,9,10 és értelmes ok; üres sorok=1. |
| A3.b.3 | ures.txt | ([], [], 0). Az üres fájl sikeres, üres beolvasás. |
| A3.b.4 | eladasok_hibas.txt | ([], [(1,ok),(2,ok),(3,ok)], 0), az okok nem üresek. Nem keletkezik kitalált 0 árú jó rekord. |
| A3.b.5 | ep09_nincs_naplo.txt (nem létezik) | FileNotFoundError továbbterjed a hívóhoz; nem tér vissza álcázott ([],[],0). Ezt a próbát a B1 főprogramjával fejezzük be, a fájlt nem hozzuk létre. |

Kapcsolódó háttér: [EP_09.html](EP_09.html#hibas-sorok).

## S1 – Rövid összegzés

2 perc, új program nélkül. A saját kódodon mutasd meg röviden: melyik hibát jelzi a függvény, melyiket kezeli a sorbejáró, és miért különbözik a rekordok száma az eladott darabtól. Ez nem új kötelező szóbeli vizsga. A folytatás B1; a két saját A3-függvény maradjon meg.

## B1 – Fájlszintű hibák és őszinte riportüzenetek

**Fájl:** `riport.py`. **Tervezett idő:** 6 perc.

### Mit csinál majd a program?

A riportot_keszit(bemenet,kimenet) a saját A3 beolvasód, a kész összesítő és a kész mentő együttműködését szervezi. Fájlszintű hibánál False-t, befejezett mentés után True-t ad. A főprogram finally üzenete csak lezárást jelent.

### Mi adott, mit írsz te?

Az A3 két saját függvénydefinícióját át kell hoznod a helykitöltők helyére. A naplo_adatait_osszesit és osszesitest_ment már kész, nem új feladat. Az összesítő a mennyiségeket adja össze, a bevételt darab*egységár alapján számolja. A mentő külön w célfájlt ír. A mai árjegyzék nem forrása a történeti bevételnek.

### Rövid analóg minta

```python
try:
    with open("ep09_nincs_naplo.txt", "r", encoding="utf-8") as fajl:
        print(fajl.read())
except FileNotFoundError:
    print("A kért bemenet nem található.")
finally:
    print("A beolvasási kísérlet véget ért.")
```

A finally a kezelt hibánál is lefut, ezért nem lehet benne sikerüzenet. A saját riportban különüljön el a beolvasás és a mentés hibája. Hiányzó bemenet után a mentő nem hívható: különben egy régi riport üres sikeres adattal felülíródna.

### Most te alakítsd át

1. Csak az A3 két függvénydefinícióját hozd át; a korábbi főprogram ne kerüljön ide. A két kész segédfüggvényt olvasd át a tutorral, de ne írd újra.
2. A riportot_keszit előbb a beolvasást próbálja. FileNotFoundError esetén külön hiányjelzés és korai False, más OSError esetén beolvasási hibajelzés és False legyen.
3. Sikeres beolvasás után add az eredményeket a kész összesítőnek, majd a mentőnek. A mentő OSError-ját külön jelezd; a sikeres mentés után legyen sikerüzenet és True.
4. A főprogram riportkísérletét egészítsd ki try–finally szerkezettel és egy semleges lezáró üzenettel. A fájllezárás továbbra is a kész with blokkok dolga.
5. Írás után nyisd meg/frissítsd a célt. Végezd el az öt B1-próbát; sikertelen beolvasás után a megmaradó régi riport nem a mostani futás eredménye.

### Kész, ha

- A fájlhibák és a sorhibák eltérő szinten kezeltek. Hiányzó/olvashatatlan forrás után nem indul mentés.
- Mentési hiba False és célzott üzenet; sikerüzenet csak rendes mentés után van.
- A finally nem állít sikert, a régi cél hiányzó bemenet után változatlan.
- A jó rekordok száma nem azonos az eladott darabszámmal; az előkészített segítők szerepét felismeri.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.1 | A3 saját függvényei; bemenet=eladasok_vegyes.txt, cél=bufe_jelentes.txt | True; 4 érvényes rekord, 7 darab, 1750 Ft, 5 hiba, 1 üres sor, részleges állapot. Mentett jelentés sikerüzenet és végül a finally lezáró üzenete. |
| B1.2 | A B1.1 célját megtartva bemenet=ep09_nincs_naplo.txt | False és hiányzó bemenetet jelző üzenet; a korábbi cél bájtra változatlan, nincs sikerüzenet. A finally lefut. |
| B1.3 | bemenet=ures.txt, cél=bufe_jelentes.txt | True; 0 rekord/darab/bevétel/hiba/üres sor; nincs feldolgozható eladás. A korábbi sorok eltűnnek. |
| B1.4 | bemenet=eladasok_jo.txt, cél=ures.txt/jelentes.txt; az ures.txt változatlanul 0 bájtos fájl | False és mentési OSError-üzenet; nincs sikerüzenet, a finally lefut, az ures.txt és a forrás megmarad. |
| B1.5 | bemenet=eladasok_valtott.txt, rendes külön cél; majd ugyanaz még egyszer | Mindkét futás True; a riport 3 rekord, 6 darab, 2140 Ft. A második mentés nem dupláz. |

Kapcsolódó háttér: [EP_09.html](EP_09.html#meresi-alkalmazas).

## Z1 – Önálló kosárellenőrzés

12 perc. Követelmények és próbák: [zaro_feladatok.md](zaro_feladatok.md). Itt a hibás tétel mellett **nem** adunk engedélyt részösszeg fizetésére. A tutor elsőre a célt és a próbákat adja, kész algoritmust nem.

## C1 – Egyetlen választható bővítés

15 perc. Csak teljesen ellenőrzött kosár kerüljön a naplóba; adatellenőrzési hiba ne okozzon részleges hozzáfűzést. Feltételek és részletek: [bovites.md](bovites.md).

## T1 és T2 – Zárótesztek

T1: 10 feleletválasztós elméleti kérdés, 10 perc. T2: 5 kódértelmezési és 5 hibakeresési kérdés, 15 perc. Alapból ötös csoportokban, kérésre egyesével. Először önállóan válaszolsz, a tesztkódok futtatása és a kulcs megnyitása nélkül. A teljes T2 után közösen értékeltek; javításkor már futtathatsz. A kulcs a munkatérben elérhető, így ez tanulási célú teszt, nem titkos vizsga.

## S2 – Lezárás

2 perc. Külön összegzés a programozási munka állapotáról, a T1/T2 pontjairól és a támogatással javított részekről. Hiánynál pontos folytatási pont. Az óra véget ér, új feladat nem indul automatikusan.
