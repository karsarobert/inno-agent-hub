# EP_03 – ciklusok és kosár, saját kódírással

Két 45 perces órán a második lecke büféprogramját fejleszted tovább. Először megismered az ismétlés működését, azután te írod meg a kijelölt kódrészt. A tutor rövid mintával, magyarázattal és hibakeresési támpontokkal segít.

**Cél → magyarázat és rövid minta → saját kódírás → mentés → Futtatás → ellenőrzés.** Nem kérünk előzetes kimenetjóslást. Az elvárt eredményt ellenőrzéshez kapod meg; a feladat a hozzá vezető kód elkészítése.

Az összes `.py` a munkamappa gyökerében van. Nyisd meg az aktuális fájlt, ments, és használd a Futtatás gombot. Alapesetben nincs mappaváltási teendő. A program `input()` kérdésére a **terminálban**, Enterrel válaszolj. Ne indíts újabb futást, amíg az előző válaszra vár. Elszabadult ciklust Ctrl+C-vel állíthatsz meg.

A mintafájlok futtatható **kiindulópontok**, nem kész megoldások. Az ideiglenes `return 0` vagy a még csak egy elemet feldolgozó rész kijelölt bővítési hely. Ne tekintsd a kezdeti lefutást a feladat teljesítésének. A saját kódodat később újra felhasználjuk; nem írjuk vissza a mintát a helyére.

| Szakasz | Fájl | Tervezett perc |
|---|---|---:|
| E0 – Mentett fájl és első futás | indulas.py | 3 |
| W1 – Ismétlés while ciklussal | sorszam.py | 8 |
| W2 – Újrakérés függvényben | bekeres.py | 9 |
| F1 – Sorszámok for és range segítségével | tartomany.py | 7 |
| B1 – Napi bevétel zárásig | napi_osszesito.py | 15 |
| S1 – Első óra lezárása | a saját fájlok | 3 |
| L1 – A kosár elemeinek bejárása | kosar.py | 8 |
| B2 – A kosár összegző függvénye | kosar.py | 9 |
| C1 – Blokk és ismeretlen termék kihagyása | blokk.py | 8 |
| B3 – A kosár és a fizetés összeépítése | bufe_03.py | 10 |
| Z1 – Önálló termékszámláló | onallo.py | 7 |
| S2 – Lezárás és folytatási pont | a saját fájlok | 3 |

S1 után ér véget az első 45 perc; S2 zárja a másodikat. A szünet nincs az időkeretben. A részletes [EP_03.html](EP_03.html) magyarázatai bármikor használhatók, de a teljes programjának bemásolása helyett az alábbi lépések saját módosításait végezd el. Nem kell az összes HTML-példát ezen az órán végigvenni.


## E0 – Mentett fájl és első futás

**Fájl:** `indulas.py`. **Keret:** 3 perc.

**Mire szolgál a program?** Egy már ismert print-utasítás szövegét módosítod. Ezzel ellenőrizzük, hogy valóban a megnyitott és elmentett fájl fut.

### Előbb értsük meg

A szerkesztőben Python-kódot írsz; a terminálban a futó program eredményét látod. A Futtatás mindig a megfelelő megnyitott fájlhoz tartozzon. Az összes gyakorlófájl a munkamappa gyökerében van, így itt ez egyben a Python-fájlok mappája is.

### Most te írd meg

1. Nyisd meg az `indulas.py` fájlt.
2. Cseréld a köszöntést erre: `Szia, kezdjük a harmadik gyakorlatot!` Az idézőjeleket és a print hívást tartsd meg.
3. Mentsd el, és nyomd meg a Futtatás gombot. Nincs szükség előzetes almappába lépésre.

### Próbák

- **E0.1** A köszöntés szövegét írd át. Nincs terminálbemenet. Ellenőrzés: Szia, kezdjük a harmadik gyakorlatot!

**Kész, ha:** Az elmentett saját szövegmódosítás megjelenik a megfelelő fájl futásakor.

**A futás után röviden:** Melyik fájlt futtattad? Csak bizonytalan célfájl esetén kérdezd.

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#kapcsolodas).

## W1 – Ismétlés while ciklussal

**Fájl:** `sorszam.py`. **Keret:** 8 perc.

**Mire szolgál a program?** A program rendelési sorszámokat ír ki. A kiinduló változat csak egyet mutat; te írod meg az ismétlést és a sorszám változtatását.

### Előbb értsük meg

A while minden kör előtt újra megvizsgálja a feltételt. A behúzott sorok a ciklus törzse. Az állapotnak változnia kell: a `+= 1` egész számnál ugyanazt jelenti, mint a régi értékhez egyet adó értékadás. A ciklus utáni, nem behúzott kiírás csak egyszer fut. Az alábbi minta visszaszámlál; a saját feladatod felfelé számoz.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
maradek = 2
while maradek > 0:
    print(f"Még {maradek} lépés.")
    maradek -= 1
```

### Most te írd meg

1. A `sorszam = 1` sort tartsd meg a ciklus előtt.
2. A rendelési sor kiírását tedd olyan while ciklusba, amely 1-től 3-ig kiírja a sorszámot. Te írd a feltételt, a behúzást és a növelést.
3. A lezáró üzenet maradjon a ciklus után. Ments és futtass.
4. Állítsd a felső határt 5-re, és próbáld ki. Ezután próbáld a kezdőérték 6-ra állítását ugyanazzal az 5-ös határral. Végül állítsd vissza 1-re a kezdést.

### Próbák

- **W1.1** Kezdés 1, felső határ 3. Nincs terminálbemenet. Ellenőrzés: Rendelés: 1; Rendelés: 2; Rendelés: 3; A sorszámok elkészültek.

- **W1.2** Kezdés 1, felső határ 5. Nincs terminálbemenet. Ellenőrzés: Öt sorszám, 1-től 5-ig; egy lezáró sor.

- **W1.3** Kezdés 6, felső határ 5. Nincs terminálbemenet. Ellenőrzés: Csak a lezáró sor; nincs rendelési sorszám.

**Kész, ha:** Valódi while ciklus, nem egymás alá írt kész kiírások. A növelés a törzsben, a lezárás azon kívül van. Az elsőre hamis feltétel esetén nulla kör történik.

**A futás után röviden:** Melyik sor miatt tud véget érni a ciklus? A saját kész kódjára mutasson.

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#while).

## W2 – Újrakérés függvényben

**Fájl:** `bekeres.py`. **Keret:** 9 perc.

**Mire szolgál a program?** Egy darabszámot bekérő függvényt egészítesz ki. A fejléc és a hívás már működik, de a függvény még a negatív számot is elfogadja.

### Előbb értsük meg

A kezdőértéket az első input adja. Amíg a szám negatív, figyelmeztetünk és új értéket kérünk. A return csak a ciklus után következhet: akkor már elfogadható számot adunk vissza. A 0 megengedett. Most egész számként leírható válaszokkal dolgozunk; a `ketto` és a `2.5` szöveg kezelését még nem tanultuk. A minta egy szöveges választ kér újra; a saját feladatban számmal és a negatív tartomány feltételével dolgozol.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
valasz = input("Kezdhetjük? (igen) ")
while valasz != "igen":
    valasz = input("A folytatáshoz írd be: igen ")
```

### Most te írd meg

1. Olvasd el a függvényt: az első bekérés és az utolsó return közé kerül az új rész.
2. Írj while ciklust, amely negatív számnál figyelmeztet, és ugyanazzal a `kerdes` paraméterrel új egész számot kér.
3. Tartsd a returnt a cikluson kívül, a függvény törzsében.
4. Ments, és próbáld ki a -2, -1, 2 sorozatot, majd egy új futásban rögtön a 0-t.

### Próbák

- **W2.1**  Bemenet sorrendben: `-2`, `-1`, `2`. Ellenőrzés: Két figyelmeztetés és újrakérés.; Elfogadott darabszám: 2

- **W2.2**  Bemenet sorrendben: `0`. Ellenőrzés: Elfogadott darabszám: 0; Nincs újrakérés.

**Kész, ha:** A negatív számnál tényleges új input történik. A paraméter kérdésszövegét használja. Az elfogadott számot adja vissza; nem csak kiírja.

**A futás után röviden:** Miért a while után van a return?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#ujrakeres).

## F1 – Sorszámok for és range segítségével

**Fájl:** `tartomany.py`. **Keret:** 7 perc.

**Mire szolgál a program?** A három ismétlődő print helyére egy ciklust írsz. A W1 megoldása a másik fájlban megmarad, így a két megoldást később összehasonlíthatod.

### Előbb értsük meg

A for sorban megkapja a range által megadott egész számokat. A kezdőérték benne van, a végpont nincs. A ciklusváltozót nem növeljük kézzel. A minta a 2, 4, 6 értékeket járja be; a harmadik argumentum a lépésköz.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
for szam in range(2, 7, 2):
    print(f"Páros érték: {szam}")
```

### Most te írd meg

1. A három külön rendelési kiírást cseréld egy for ciklusra. A cél sorszámok: 1, 2, 3. Te válaszd meg a range argumentumait.
2. Az egyszeri lezáró kiírást hagyd a ciklus után. Ments és futtass.
3. Alakítsd át a tartományt az 5, 6, 7, 8 értékekre, majd ellenőrizd. Ne írj külön növelést a törzsbe.

### Próbák

- **F1.1** Sorszámok 1–3. Nincs terminálbemenet. Ellenőrzés: Három rendelési sor és egy lezárás.

- **F1.2** Sorszámok 5–8. Nincs terminálbemenet. Ellenőrzés: Rendelés: 5; Rendelés: 6; Rendelés: 7; Rendelés: 8; A sorszámok elkészültek.

**Kész, ha:** For + range szerkezet, változót használó f-string. Kizárt végpont helyes, nincs felesleges kézi növelés.

**A futás után röviden:** Miért eggyel nagyobb a megadott végpont az utolsó kiírt számnál?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#for).

## B1 – Napi bevétel zárásig

**Fájl:** `napi_osszesito.py`. **Keret:** 15 perc.

**Mire szolgál a program?** A büfé kifizetett rendeléseinek összegeit rögzítjük, amíg 0-val le nem zárjuk a napot. Most a már kész rendelési értékeket adjuk meg, nem minden vendég teljes rendelését kérjük be.

### Előbb értsük meg

A napi bevétel és a rendelési darabszám a ciklus előtt indul 0-ról. A `while True` ismétel, a belső `break` ad neki kijáratot. A 0 itt végjel: nem rendelés. A negatív érték hibás, nem növeli egyik összesítőt sem. Az összegző az aktuális összeget, a számláló 1-et kap hozzá. A példa üzeneteket ismétel kilépésig; a saját programod számokat dolgoz fel.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
while True:
    uzenet = input("Üzenet (vege = kilépés): ")
    if uzenet == "vege":
        break
    print(f"Megkaptam: {uzenet}")
```

### Most te írd meg

1. A két összesítő kezdőértéke maradjon a ciklus előtt. Írj while True ciklust, amely körönként kér be egy rendelési összeget.
2. A bekérés után vizsgáld a 0-t, és breakkel zárj. A negatív érték figyelmeztetést kapjon; az eddigi if/elif ágat felhasználhatod.
3. Csak a pozitív összeg növelje a bevételt és a kifizetett rendelések számát. A két záró print kerüljön a ciklus után.
4. Ments és futtass a megadott sorozattal, majd azonnali zárással.

### Próbák

- **B1.1**  Bemenet sorrendben: `1611`, `-20`, `1790`, `450`, `0`. Ellenőrzés: A -20 figyelmeztetést kap, nem számít bele.; Kifizetett rendelések: 3; Napi bevétel: 3851 Ft

- **B1.2**  Bemenet sorrendben: `0`. Ellenőrzés: Kifizetett rendelések: 0; Napi bevétel: 0 Ft

**Kész, ha:** A bekérés a ciklusban van, a végjel vizsgálata a feldolgozás előtt. A negatív és a 0 nem növeli az összesítőket. Nincs cikluson belüli nullázás. A záró kiírás egyszer történik.

**A futás után röviden:** Mi veszne el, ha minden körben nulláznánk a napi bevételt?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#bufe-nap).

## S1 – Első óra lezárása

**Keret:** 3 perc.

**Mire szolgál a program?** Röviden rendezzük, mi készült el, és honnan folytatjuk.

### Előbb értsük meg

A fájlok a saját munkádat őrzik. A szünet után nem készítünk belőlük új, üres mintát.

### Teendő

1. Mentsd a módosított fájlokat.
2. A tutor röviden összegzi az elvégzett kódírást, a még hiányzó próbát és a következő lépést.
3. Szünet után L1 következik, vagy az első óra név szerint megjelölt hiányzó részének befejezése.

**Kész, ha:** A folytatási pont tényleges állapoton alapul.

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#osszegzes).

## L1 – A kosár elemeinek bejárása

**Fájl:** `kosar.py`. **Keret:** 8 perc.

**Mire szolgál a program?** A listában minden termék külön elem. Először a kosár adatát és kiírását változtatod; az összegző függvény csak a következő feladatban készül el.

### Előbb értsük meg

A lista szögletes zárójelben tárol elemeket. A kosárban ugyanaz a termék többször is szerepelhet. A for ciklusváltozó itt maga a szöveg, nem index. A fájlban már ott van az árlekérdező függvény; az ismeretlen termékre adott 0 később jelzés lesz. A `kosar_osszege` ideiglenes 0-ja még nem megoldás és nem a te hibád.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
nevek = ["Anna", "Béla"]
for nev in nevek:
    print(f"Szia, {nev}!")
```

### Most te írd meg

1. A kosár literálját alakítsd négy eleműre ebben a sorrendben: kávé, szendvics, kávé, üdítő. Ne használj most appendet.
2. Az első elem külön kiírása helyett írj közvetlen bejáró for ciklust; soronként jelenjen meg az aktuális termék.
3. Ments és futtass. Ideiglenesen állítsd a kosarat üres listára is, majd állítsd vissza a négy terméket. A 0-s összegző függvényt most még nem kell meghívnod.

### Próbák

- **L1.1** A megadott négy termék. Nincs terminálbemenet. Ellenőrzés: A kosárban: kávé; A kosárban: szendvics; A kosárban: kávé; A kosárban: üdítő

- **L1.2** kosar = [] Nincs terminálbemenet. Ellenőrzés: Nincs terméksor és nincs IndexError.

**Kész, ha:** A lista sorrendjében négy elem jelenik meg. Közvetlen bejárás; nincs beégetett négy print. Üres listán nem indexel nem létező elemet.

**A futás után röviden:** A termek változó az elem indexét vagy a termék nevét tartalmazza a saját ciklusodban?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#listak).

## B2 – A kosár összegző függvénye

**Fájl:** `kosar.py`. **Keret:** 9 perc.

**Mire szolgál a program?** A már működő árlekérdezést felhasználva saját kosárösszegzőt írsz. A függvény eredményére a büfé fizetési részének lesz szüksége.

### Előbb értsük meg

A `termek_ara` egyetlen termék árát adja vissza: kávé 450, szendvics 890, üdítő 390 Ft. A `kosar_osszege` minden elemnél ezt hívja, és a visszaadott értéket összeadja. A kiírás a hívónál marad. A rövid minta a felhalmozást mutatja szöveghosszakkal; a saját feladatod árakat számol, és függvényből tér vissza.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
hosszak_osszege = 0
for szo in ["alma", "tea"]:
    hosszak_osszege += len(szo)
print(hosszak_osszege)
```

### Most te írd meg

1. Az ideiglenes `return 0` helyett írd meg a kosar_osszege törzsét: induló összeg, a kosár bejárása, árlekérdezés és hozzáadás, majd visszatérés.
2. A függvényben ne legyen input vagy print. A termek_ara függvényben lévő árakat ne másold újra a ciklusba.
3. A fájl végén te írj hívást és f-stringes kiírást az eredmény megjelenítésére.
4. Próbáld ki a négy termékkel, egyetlen kávéval és üres listával. Végül állítsd vissza a négytermékes kosarat.

### Próbák

- **B2.1** kávé, szendvics, kávé, üdítő Nincs terminálbemenet. Ellenőrzés: Kosár összege: 2180 Ft

- **B2.2** csak kávé Nincs terminálbemenet. Ellenőrzés: Kosár összege: 450 Ft

- **B2.3** üres lista Nincs terminálbemenet. Ellenőrzés: Kosár összege: 0 Ft

**Kész, ha:** A függvény a paramétert járja be, nem a külső kosar változóra támaszkodik. A termek_ara függvényt hívja, és nem beégetett 2180-at ad vissza. A return a teljes ciklus után van; üres listán is 0 az eredmény.

**A futás után röviden:** Miért csak a bejárás után szabad visszaadni a teljes összeget?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#bejaras).

## C1 – Blokk és ismeretlen termék kihagyása

**Fájl:** `blokk.py`. **Keret:** 8 perc.

**Mire szolgál a program?** A blokk.py már tartalmazza az árlekérdező függvényt, a blokkfüggvény kezdetét és a próbakosarat. Most megírod a blokk megjelenítését. A program a blokk kiírásával véget ér; nincs terminálbemenet. A saját kész függvényedet B3-ban viszed át a büféprogramba.

### Előbb értsük meg

A blokk függvénye jogosan használ printet, mert megjelenítés a feladata. A 0 ár most ismeretlen terméket jelöl: minden eladható termékünk ára pozitív. A continue csak az adott kör hátralévő részét hagyja ki; a későbbi ismert termékeket továbbra is feldolgozzuk. A len(kosar) minden beírt elemet számolna, ezért az elfogadott tételekhez külön számláló kell.

Rövid szemléltető minta – a működés megértéséhez, nem a célfeladat kész megoldása:

```python
for szam in [2, -1, 3]:
    if szam < 0:
        print("Ezt kihagyjuk.")
        continue
    print(f"Elfogadott szám: {szam}")
```

### Most te írd meg

1. A blokkot_mutat fejlécét és a blokk címének kiírását tartsd meg. Írd bele a számláló induló értékét és a kosár bejárását.
2. Minden terméknél kérd le az árat. 0 esetén írj figyelmeztetést és continue-val hagyd ki a további feldolgozást.
3. Az elfogadott terméknél írd ki a nevet és az árat, és növeld a számlálót. A ciklus után egyszer írd ki az elfogadott tételek számát.
4. Mentsd el a blokk.py fájlt, és próbáld a kávé, pizza, üdítő listával. A blokk és a tételszám kiírása után a futás véget ér; nincs további kérdés.

### Próbák

- **C1.1** kosar = ["kávé", "pizza", "üdítő"] Nincs terminálbemenet. Ellenőrzés: kávé: 450 Ft; A pizza kihagyását jelző figyelmeztetés.; üdítő: 390 Ft; Elfogadott tételek: 2

**Kész, ha:** A pizza után az üdítő még megjelenik. Continue használata; az ismeretlen termék nem növeli a számlálót. A blokkfüggvény csak a kapott kosárral dolgozik.

**A futás után röviden:** Miért maradna ki az üdítő is, ha ezen a helyen break állna?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#ciklusvezerles).

## B3 – A kosár és a fizetés összeépítése

**Fájl:** `bufe_03.py`. **Keret:** 10 perc.

**Mire szolgál a program?** Most nyitod meg a bufe_03.py fájlt. A saját blokkmegjelenítő, összegző és bekérő függvényeidet viszed át és használod fel benne. A fizetés ismétlődik, amíg a teljes összeg össze nem gyűlik.

### Előbb értsük meg

A kosár alapösszege és a kedvezményes fizetendő külön adat. A kedvezmény az alapösszeg // 10 része, ha diák a vendég. A pótlás újonnan átadott pénz: hozzáadjuk a korábban befizetetthez. A nulla értékű kosárnál nincs fizetési kérdés. A számos kérdésekhez a W2 saját függvényét használjuk, a diáksághoz ezen a fő útvonalon pontos igen/nem választ kérünk.

### Most te írd meg

1. Nyisd meg a bufe_03.py fájlt. A benne lévő kezdő blokkot_mutat definíciót cseréld le a blokk.py-ban megírt saját függvényedre; ne maradjon két azonos nevű definíció. Csak a definíciót vidd át, a próbakosarat és a hívást ne. A kosar.py fájlból te másold át a saját kosar_osszege definíciódat a bufe_03.py elejére, a hívások elé. A termek_ara már ott van: ne duplázd. A próbahívásokat se másold.
2. Ugyanígy vidd át a bekeres.py saját nemnegativ_egesz_beker függvényét, csak a definíciót.
3. Az első termék árát használó mintaszámítást cseréld a saját kosárösszegző hívására. Nulla összegnél egy üzenet jelenjen meg; az egész diákság- és fizetési rész csak pozitív összegnél fusson.
4. Az első pénzbekérés használja a saját bekérő függvényedet. A régi fizetési if/else helyére írj while ciklust: amíg kevés a befizetés, írd ki a hiányt, kérj nemnegatív pótlást és add az összesen befizetett pénzhez. A visszajáró kiírása a ciklus után legyen.
5. A bufe_03.py négytermékes kosarával futtasd a két fizetési próbát; végül próbáld az üres kosarat. A blokk.py külön gyakorlófájl marad.

### Próbák

- **B3.1** kávé, szendvics, kávé, üdítő Bemenet sorrendben: `igen`, `2000`. Ellenőrzés: Rendelés: 2180 Ft; Kedvezmény: 218 Ft; Fizetendő: 1962 Ft; Visszajáró: 38 Ft

- **B3.2** Ugyanaz a kosár. Bemenet sorrendben: `igen`, `1900`, `62`. Ellenőrzés: Még hiányzik: 62 Ft; Visszajáró: 0 Ft

- **B3.3** kosar = [] Nincs terminálbemenet. Ellenőrzés: Elfogadott tételek: 0; Nincs fizetendő tétel.; Nem kér diákságot és pénzt.

**Kész, ha:** A teljes kosárra számol és a saját függvényeket hívja. A pótlást hozzáadja, nem lecseréli a befizetett összeget. Visszajárót csak elegendő pénznél ír, a ciklus után. Üres kosárnál nincs indexhiba, bekérés vagy fizetés.

**A futás után röviden:** Miben különbözik a pótlás a befizetett_osszesen értékétől?

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#bufe-kosar).

## Z1 – önálló termékszámláló

A 7 perces feladat részletes leírása: [zaro_feladatok.md](zaro_feladatok.md). Ezt te írod meg az `onallo.py` fájlban; a tutor szükség esetén segít, és ennek megfelelően értékeli az önállóságot.

## S2 – Lezárás és folytatási pont

**Keret:** 3 perc.

**Mire szolgál a program?** Összekapcsoljuk a ciklus, a függvény, a kosár és a pénzszámítás szerepét.

### Előbb értsük meg

A magyarázatodban a saját elkészült programrészekre támaszkodj. Ami még hiányzik, azt külön megnevezzük.

### Teendő

1. Mentsd a fájlokat.
2. Mondd el 2–3 mondatban: mit jár be a kosár ciklusa, miért a ciklus után van a return, és mitől ér véget a fizetési ismétlés. Ha az utóbbi még nem készült el, arról a megírt részből induljunk ki.
3. A tutor konkrétan összegzi az elkészült és támogatással elkészült részeket, a hiányzó próbákat és a következő teendőt.

**Kész, ha:** A lezárás nem állít többet a tényleges munkánál.

Referencia: [EP_03.html – kapcsolódó rész](EP_03.html#osszegzes).
