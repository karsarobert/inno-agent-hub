# EP_04 – szövegek és élő kosár, saját kódírással

Az EP_03 folytatása. Az egyes fájlok futtatható, de még hiányos kezdőminták: a feladat célját megvalósító kódot te írod. A visszaadott 0, [] vagy False önmagában még nem kész megoldás. A B2 régi ár- és fizetési függvényei újrahasznált, kész részek; a bekérés és az összekapcsolás rövid kezdőmintáit te alakítod át. B1-ben kész ciklusvázat, B2-ben kész főprogramszerkezetet kapsz. Z1-ben rövid önálló alkalmazás következik.

Munka: megnyitás → a cél megértése → saját szerkesztés → mentés → Futtatás → eredmény ellenőrzése. A Futtatás gomb terminálja a megnyitott .py fájl mappájában álljon. Ebben a csomagban ez mindig a munkatér gyökere. Nem kell python_gyakorlat almappába lépni. Az input kérdéseire a terminálban válaszolj; egy futás befejezése előtt ne indíts új példányt.

Nincs kimenetjóslás: a tanultakat programírással és futtatással próbálod ki. A szöveges feliratok kisebb eltérése elfogadható, ha az adat és a működés helyes. A lenyitható HTML-magyarázat segítség; a célfeladat teljes referenciamegoldása nem helyettesíti a saját munkát.

## Időterv

| Lépés | Fájl | Perc |
|---|---|---:|
| T1 – Terméknév egységesítése | szoveg.py | 9 |
| T2 – Rendelési kód és szelet | kodresz.py | 7 |
| T3 – Feltételes számlálás szövegen | karakterszam.py | 7 |
| L1 – Kosár módosítása metódusokkal | listamuveletek.py | 9 |
| L2 – Rendelési sor feldolgozása | feldolgozas.py | 10 |
| S1 – Az első blokk lezárása | beszélgetés | 3 |
| B1 – Élő kosár, fizetés nélkül | kosar_04.py | 18 |
| B2 – Összekapcsolás a fizetéssel | bufe_04.py | 12 |
| Z1 – Önálló törlés név szerint | onallo.py | 12 |
| S2 – Lezárás és folytatási pont | beszélgetés | 3 |

T1–S1: **45 perc**. B1–S2: **45 perc**. A szünet külön idő. A magyarázat és a próbák is a keret részei. A K-feladatok opcionálisak, a kereten kívüliek.

## T1 – Terméknév egységesítése

**Fájl:** `szoveg.py`. **Tervezett idő:** 9 perc.

### Mire szolgál ez a rész?

A nyers terméknevet számításhoz használható szöveggé alakítod.

### Előbb értsük meg

A strip() a két szélről távolítja el a whitespace karaktereket, a lower() kisbetűsít. A sztring megváltoztathatatlan: a visszakapott értéket el kell tárolni vagy vissza kell adni. A belső szóközt és az ékezeteket nem töröljük. A függvény feldolgoz, a hívó rész jelenít meg.

Rövid analóg minta, amelynek működését a saját feladatodhoz használhatod:

```python
cim = "mai ajánlat"
kiemelt_cim = cim.upper()
print(kiemelt_cim)
print(cim)
```

### Most te írd meg

1. A szoveget_egysegesit(szoveg) most változtatás nélkül adja vissza a szöveget. Alakítsd át: a szélek levágása után kisbetűs szöveget adjon vissza.
2. A függvényben ne legyen input vagy print. A fájl alján a kapott eredményt írasd ki szögletes zárójelek között, hogy látszódjanak a szélső szóközök.
3. Mentsd és futtasd a két kötelező próbával; a nyers_termek értékét te módosítsd.

### Kész, ha

- A paramétert dolgozza fel, nem egy beégetett kávé szót ad vissza.
- A return a feldolgozott szöveget adja. Az eredeti változó és az új érték szerepe világos.

### Próbák

### T1.1

nyers_termek = "  KÁVÉ  "

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- [kávé]


### T1.2

nyers_termek = "   "

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- [] – üres szöveg a kiírás zárójelei között


### T1.3 – választható pluszpróba

nyers_termek = " JEGES KÁVÉ "

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- [jeges kávé]


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#metodusok). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## T2 – Rendelési kód és szelet

**Fájl:** `kodresz.py`. **Tervezett idő:** 7 perc.

### Mire szolgál ez a rész?

Szöveg egy karakterét és egy részét olvasod ki; üres bemenettel is működő programot készítesz.

### Előbb értsük meg

Az indexek 0-tól indulnak. A [0] egyetlen karaktert kér, az [1:] a második karaktertől a végéig tartó szöveget. A szelet nem alakít számmá: a vezető nulla megmarad. Az üres szövegen nincs első karakter, ezért az indexelést meg kell előznie az ellenőrzésnek.

Rövid analóg minta, amelynek működését a saját feladatodhoz használhatod:

```python
felirat = "MENÜ"
print(felirat[-1])
print(felirat[:2])
```

### Most te írd meg

1. A jelenlegi egyszerű kiírás helyére írj if–else elágazást: nem üres kod esetén jelenjen meg külön az első karakter és az első karakter utáni rész.
2. Az utótagot szövegként kezeld; ne alakítsd int-té. Üres kódra a Nincs rendelési kód. üzenetet írd.
3. Te állítsd át a kod változót és futtasd mindhárom esetet.

### Kész, ha

- A nem üres ág használ indexelést és szeletelést.
- Az üres esetben nincs IndexError; a 042 megőrzi a vezető nullát.

### Próbák

### T2.1

kod = "B042"

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Első karakter: B
- Utótag: [042]


### T2.2

kod = ""

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Nincs rendelési kód.


### T2.3

kod = "B"

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Első karakter: B
- Utótag: []


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#indexeles). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## T3 – Feltételes számlálás szövegen

**Fájl:** `karakterszam.py`. **Tervezett idő:** 7 perc.

### Mire szolgál ez a rész?

Saját ciklussal megszámolod egy szöveg magánhangzóit.

### Előbb értsük meg

A for egy sztringen karaktereket kap, listán listaelemeket. A számláló a ciklus előtt indul, csak egyezéskor nő, a return a teljes bejárás után áll. A kisbetűs változaton elég a magyar kisbetűs magánhangzókat vizsgálni.

Rövid analóg minta, amelynek működését a saját feladatodhoz használhatod:

```python
for karakter in "B12":
    print(f"Karakter: {karakter}")
```

### Most te írd meg

1. A maganhangzok_szama(szoveg) ideiglenes return 0 törzsét írd át saját for ciklusos számlálásra. A vizsgált betűk: aáeéiíoóöőuúüű.
2. Ne a kávé szó konkrét eredményét add vissza. A függvény nem ír ki; a hívó rész megjeleníti a visszakapott számot.
3. A két megadott teszthez te módosítsd a szoveg értékét, ments és futtass.

### Kész, ha

- A paraméter szövegét járja be, nagybetűt is kezel.
- A számláló nem nullázódik minden körben, üres szövegre 0 tér vissza.
- Ebben a feladatban valódi feltételes ciklus kell, nem beépített count hívások összege.

### Próbák

### T3.1

szoveg = "KÁVÉ"

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Magánhangzók száma: 2


### T3.2

szoveg = ""

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Magánhangzók száma: 0


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#bejaras). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## L1 – Kosár módosítása metódusokkal

**Fájl:** `listamuveletek.py`. **Tervezett idő:** 9 perc.

### Mire szolgál ez a rész?

Hozzáadod és visszavonod az utolsó tételt, majd biztonságosan törölsz egy terméknevet.

### Előbb értsük meg

Az append helyben módosít és None-t ad vissza. A pop kivesz és visszaad egy elemet. A remove az első egyező értéket törli; hiánynál hibás lenne. A listán az in teljes elemeket keres. A kosár egyetlen elemét a különböző műveletek eltérően azonosítják.

Rövid analóg minta, amelynek működését a saját feladatodhoz használhatod:

```python
sor = ["Anna"]
sor.append("Béla")
utolso_nev = sor.pop()
print(utolso_nev)
print(sor)
```

### Most te írd meg

1. A két kávét és egy üdítőt tartalmazó kosárhoz append-del adj croissant-t. Írasd ki a listát.
2. Ha a kosár nem üres, pop()-pal vedd ki az utolsó elemet, tedd a torolt_termek változóba és írasd ki. Üres kosárnál legyen figyelmeztetés.
3. A keresett_termek első előfordulását csak akkor remove-old, ha benne van a kosárban. Különben jelezd a hiányt.
4. A végén írasd ki a kosarat és count()-tal a kávék számát. A második próbához csak a keresett_termek értékét változtasd.

### Kész, ha

- Az append visszatérési értékét nem rendeli a kosar névhez.
- A pop és remove előtt megfelelő ellenőrzés áll.
- A remove csak egy kávét töröl; itt a count használata kifejezetten cél.
- A hiányüzenet a tényleges keresett termékről szól: tea keresésekor nem állíthatja, hogy nincs kávé.

### Próbák

### L1.1

Kezdő kosár: ["kávé", "üdítő", "kávé"], keresett_termek = "kávé".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Hozzáadás után 4 tétel.
- A kivett utolsó tétel croissant.
- Végső kosár: ["üdítő", "kávé"]. Kávék száma: 1.


### L1.2

Minden futás az eredeti 3 tétellel indul; keresett_termek = "tea".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- A tea hiányát jelzi.
- Végső kosár: ["kávé", "üdítő", "kávé"]. Kávék száma: 2.
- A hiányjelzés a teára utal, nem a kávéra.


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#listamuveletek). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## L2 – Rendelési sor feldolgozása

**Fájl:** `feldolgozas.py`. **Tervezett idő:** 10 perc.

### Mire szolgál ez a rész?

Egy vesszővel elválasztott szövegből új, érvényes termékeket tartalmazó listát készítesz.

### Előbb értsük meg

A split(",") listát ad, amelyben üres sztringek is lehetnek. Minden darabon külön végezz strip és lower műveletet. Csak a kínálatban lévő elemet add az új kosárhoz; az eredeti darablistából ne törölj bejárás közben. A join a kapott sztringelemeket egy kiírható felirattá kapcsolja.

Rövid analóg minta, amelynek működését a saját feladatodhoz használhatod:

```python
nevek = "Anna;Béla".split(";")
print(" / ".join(nevek))
```

### Most te írd meg

1. A termekeket_feldolgoz(szoveg, kinalat) return [] kezdő törzsét alakítsd át: új üres kosár, split utáni bejárás, darabonkénti egységesítés, ellenőrzés és append, végül return.
2. A feladat szabálya szerint az üres és ismeretlen részt kihagyjuk. A függvény ne írjon ki. Azonos terméket többször is tartson meg.
3. A hívó kódban a kiírást egészítsd ki join használatával, hogy a termékek között vessző és szóköz legyen. Saját próbahívással ellenőrizd az üres bemenetet is.

### Kész, ha

- A paraméterként kapott kínálatot használja, nem egy külön beégetett listát.
- Új listát épít, minden darabot egységesít, ismétlődést megtart, return a ciklus után.
- A sztring visszaalakítása és a lista tárolása külön művelet.
- A hívó rész join segítségével Rendelés: feliratú szöveget is kiír; a lista kiírása önmagában nem elég.

### Próbák

### L2.1

szoveg = " KÁVÉ, , pizza, ÜDÍTŐ, kávé "; adott kínálat.

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Eredménylista: ["kávé", "üdítő", "kávé"]
- Rendelés: kávé, üdítő, kávé


### L2.2

szoveg = ""; adott kínálat.

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- Eredménylista: []
- A Rendelés: felirat után nincs termék.


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#split-join). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## S1 – Az első blokk lezárása

**Fájl:** nincs új fájl. **Tervezett idő:** 3 perc.

### Mire szolgál ez a rész?

Röviden megnevezed, milyen szöveg- és listaműveletet használtál; megőrizzük a folytatási pontot.

### Előbb értsük meg

A sztringmetódus új adatot adhat, a listaművelet a meglévő listát módosíthatja. A megírt függvények később újra használhatók.

### Most te írd meg

1. A saját kódodból mutass egy példát a visszakapott érték felhasználására és egy listát módosító műveletre.
2. A tutor összegzi a ténylegesen kész és még hiányzó részeket. Következő lépés a külön kosar_04.py fájl.

### Kész, ha

- Rövid, valós folytatási pont; nincs új feladat vagy kimenetjóslás.

Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#osszegzes). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## B1 – Élő kosár, fizetés nélkül

**Fájl:** `kosar_04.py`. **Tervezett idő:** 18 perc.

### Mire szolgál ez a rész?

A felhasználó termékeket ad a kosárhoz, visszavonhatja az utolsót, majd lezárhatja a rendelést.

### Előbb értsük meg

A kosarat_beker(kinalat) párbeszédet folytat és listát ad vissza. A kosár a ciklus előtt jön létre. Minden bevitelt egységesítünk. A fizetek és a mégse vezérlőszó, ezért nem termékként kezeljük. A fájl a kosár összefoglalásával véget ér; nincs benne diákság, ár- vagy pénzbekérés. A kezdőminta már tartalmazza a ciklust, a listát és a visszaadást. Jelenleg minden nyers szöveget felvesz, és a vége szóra zár: ezt alakítod a büfé szabályaihoz.

### Most te írd meg

1. B1.a: a szoveg.py saját szoveget_egysegesit definíciójával cseréld le a kezdő definíciót. Csak ezt a függvényt vidd át.
2. B1.a: a kész ciklusban a bekért szöveget a saját függvényeddel egységesítsd. A vége lezáró szót és a kérdés szövegét cseréld fizetek-re. A listát és a while szerkezetét tartsd meg.
3. B1.a: a feltétel nélküli append és tételszám-kiírás köré te írj ellenőrzést: csak a kínálatbeli termék kerüljön be. Üres vagy ismeretlen bevitelre érthető üzenetet adj, majd folytatódjon a bekérés. Ments és végezd el a B1.1 próbát.
4. B1.b: a lezárás vizsgálata után, a termékellenőrzés elé tegyél külön mégse ágat. Az L1-ben már megírt pop-részletet alakítsd ehhez: ellenőrizd az ürességet, töröld és nevezd meg az utolsó elemet. Ezután a ciklus kérdezzen újra; a parancs ne fusson tovább ismeretlen termékként. Ments és végezd el a B1.2–B1.3 próbát.

**Belső lépések:** B1.a – ismételt bekérés és hozzáadás (11 perc); B1.b – visszavonás és üres kosár (7 perc).

### Kész, ha

- A ciklus valóban új inputot kér, a lista nem nullázódik minden körben.
- Csak egységesített, kínálatbeli termék jut a kosárba; a parancsok nem.
- Üres kosáron a mégse nem okoz hibát.
- A kész kosarat visszaadja, és nincs fizetési kérdés ebben a fájlban.

### Próbák

### B1.1

Az a rész után: alapvető kosárépítés.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `" KÁVÉ "`
2. `""` – csak Enter
3. `"pizza"`
4. `"ÜDÍTŐ"`
5. `" FIZETEK "`

Elvárt viselkedés:

- Üres bevitelre és pizzára figyelmeztetés.
- Végső kosár: ["kávé", "üdítő"], 2 tétel.
- Nincs pénz- vagy diákságkérdés.


### B1.2

A b rész után: utolsó tétel visszavonása.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `"kávé"`
2. `"croissant"`
3. `"mégse"`
4. `"üdítő"`
5. `"fizetek"`

Elvárt viselkedés:

- Törölve: croissant
- Végső kosár: ["kávé", "üdítő"], 2 tétel.


### B1.3

Üres kosár és azonnali lezárás.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `"mégse"`
2. `"fizetek"`

Elvárt viselkedés:

- Üres a kosár, nincs mit törölni.
- Üres kosár, 0 tétel. Nincs pénzkérdés.


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#elo-kosar). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## B2 – Összekapcsolás a fizetéssel

**Fájl:** `bufe_04.py`. **Tervezett idő:** 12 perc.

### Mire szolgál ez a rész?

A saját kosárkezelődet a korábbi ár- és fizetési függvényekhez kapcsolod. Új elem az egységesített, ellenőrzött igen/nem bekérés.

### Előbb értsük meg

Az EP_03-ból ismert árlekérdezés, összegzés, blokk, kedvezmény és pénzpótlás előkészített segédkód. Nem kell ezeket újra megírni. Az új igen/nem függvény logikai értéket ad vissza: a bool("nem") igaz lenne, ezért konkrét szöveget vizsgálunk. A kosárösszeg ellenőrzése megelőzi a diákság és pénz bekérését. A fájl végén már kész a főprogram szerkezete, az üres kosár ága és a kiírások. A MODOSITSD jelöléseknél négy kezdőértéket cserélsz saját függvényhívásra vagy számításra, és hozzáadsz egy fizetési hívást.

### Most te írd meg

1. B2.a: vidd át a kosar_04.py két saját definícióját (szoveget_egysegesit, kosarat_beker) a jelölt helyre; a régi főprogramot ne. Ha már ott vannak, ezt ne ismételd meg.
2. B2.a: az igen_nem_beker jelenleg egyszer kérdez, és a pontos igen szövegre ad True-t. Ezt a rövid mintát alakítsd át: a bekérés kerüljön ciklusba, minden választ egységesíts, csak igen vagy nem esetén térj vissza. Más válasznál figyelmeztess és kérdezz újra. Az összehasonlítás logikai értéket ad; a bool(valasz) nem alkalmas erre.
3. B2.b: a főprogram MODOSITSD 1 sorában az üres lista helyén hívd a saját kosárbekérőt a kinalat-tal. A kosár kiírása, összegzése és az üres ág már kész; ezeket ne gépeld újra.
4. A MODOSITSD 2–4 sorokban a False helyére az igen/nem bekérő hívása, a 0 helyére a kedvezményfüggvény hívása, a fizetendő kezdőértékének helyére pedig az alapösszeg és a kedvezmény különbsége kerüljön. A meglévő kiírások után, az else ágon belül a HOZZAAD sor helyére hívd a fizetest_ker függvényt a fizetendővel.
5. Ments és végezd el a három fő próbát. A régi segédfüggvényeket nem kell újraírni. Az átalakított főprogramot a tesztek alapján ellenőrizd, ne a HTML teljes programjának bemásolásával helyettesítsd a célzott módosításokat.

**Belső lépések:** B2.a – saját definíciók és igen/nem bekérés (5 perc); B2.b – főprogram és próbák (7 perc).

### Kész, ha

- A saját kosárfüggvényt használja; nem egy rögzített lista kerül a helyére.
- Az igen/nem bekérés minden új választ egységesít, megfelelő bool értéket ad.
- Üres kosárnál nincs diákság- vagy pénzkérdés.
- A teljes kosárra számol, és visszajárót csak elégséges összeg után ír.

### Próbák

### B2.1

Szokásos diák rendelés; nagybetű és szélső szóköz.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `" KÁVÉ "`
2. `"szendvics"`
3. `"kávé"`
4. `"üdítő"`
5. `"fizetek"`
6. `" IGEN "`
7. `"2000"`

Elvárt viselkedés:

- Rendelés: 2180 Ft
- Kedvezmény: 218 Ft
- Fizetendő: 1962 Ft
- Visszajáró: 38 Ft


### B2.2

Hibás igen/nem után nem diák, pénzpótlással.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `"kávé"`
2. `"üdítő"`
3. `"fizetek"`
4. `"talán"`
5. `" NEM "`
6. `"800"`
7. `"40"`

Elvárt viselkedés:

- A talán után új kérdés.
- Fizetendő: 840 Ft
- Még hiányzik: 40 Ft
- A 40 Ft pótlás után Visszajáró: 0 Ft; korábban nincs visszajárós sor.


### B2.3

Rögtön fizetek.

Terminálbemenetek sorban, egyenként Enterrel. Az üres idézőjel üres sort jelent; az idézőjelek nem begépelendők.

1. `"fizetek"`

Elvárt viselkedés:

- Tételek száma: 0
- Nincs fizetendő tétel.
- Nem kér diákságot vagy pénzt.


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#bufe). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.


## Z1 – Önálló törlés név szerint

12 perc, `onallo.py`. A részletes feladat és a négy próba: [zaro_feladatok.md](zaro_feladatok.md). A függvényt és a próbahívásokat is te írod meg.

## S2 – Lezárás és folytatási pont

**Fájl:** nincs új fájl. **Tervezett idő:** 3 perc.

### Mire szolgál ez a rész?

Röviden összefoglalod, hogyan jut a program a nyers terméknévtől a kosárig és a fizetésig.

### Előbb értsük meg

A szövegfeldolgozás új szöveget állít elő, a listaműveletek módosítják a kosarat, a régi számító függvények a kész listát dolgozzák fel.

### Most te írd meg

1. A saját programodra hivatkozva mondd el röviden a szöveg egységesítésének, az append/pop műveletnek és az üres kosár ellenőrzésének szerepét.
2. A tutor lezárja a foglalkozást: elkészült részek, segítséggel kész részek, és ha szükséges, a későbbre maradt konkrét teendő.

### Kész, ha

- A lezárás a tényleges eredményen alapul, és egyértelműen kimondja, hogy az óra véget ért.

Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#osszegzes). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.
