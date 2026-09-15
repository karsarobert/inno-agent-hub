# EP_02 – külön folytatás a fő óra után

Ezek a feladatok nem részei automatikusan a két 45 perces órai útvonalnak. A fő gyakorlat befejezésének nem feltételei. Válassz a tutorral egy feladatot, magyarázat és minta után írd meg a saját kódot, ments és futtass. Az eredményeket ellenőrzéshez adjuk meg.

## K1 – elhagyható argumentumok

**Fájl:** `alapertek.py`. **Becsült idő:** 10 perc. **Előfeltétel:** F1 és F2.

A meglévő `koszont(nev)` csak akkor hívható meg helyesen, ha átadod a nevet. Az alapértelmezett paraméterérték lehetővé teszi, hogy a hívó bizonyos adatot elhagyjon.

Külön, teljes függvénydefiníció a mintához:

```python
def cimke(szoveg="Mai ajánlat"):
    return szoveg
```

A `szoveg="Mai ajánlat"` a fejlécben alapértéket ad. A `cimke()` ezt a szöveget adja vissza; a `cimke("Ebédmenü")` a kapott argumentumot. A híváskor megadott adat felülírja az adott hívásban használt alapértéket. Az egyszerű paraméterlistában a kötelező paraméterek az alapértékesek előtt állnak.

**Írd át a saját mintafájlt:**

1. A köszöntő függvény `nev` paramétere alapértelmezetten `"Vendég"` legyen.
2. Adj hozzá `uzenet` paramétert `"Jó étvágyat!"` alapértékkel, és ezt is helyezd a kiírt szövegbe.
3. Írj egy adat nélküli hívást, majd egy csak Annát megadó hívást.
4. A harmadik hívásnál kizárólag az üzenetet add meg, **név szerint**: a hívásban `uzenet="Ma is várunk!"` álljon. A név szerinti argumentum a paraméter nevével azonosítja, melyik adatot adod át; így az első paraméter az alapértékén maradhat.

**Ellenőrzés:** Vendég + Jó étvágyat!; Anna + Jó étvágyat!; Vendég + Ma is várunk!. A fájl három köszöntést adjon, a függvény továbbra is egyetlen definíció legyen.

## K2 – elfogadható adatokkal dolgozzon a büfé

**Fájl:** a saját, kész B2-es `bufe_02.py`. **Becsült idő:** 15 perc. **Előfeltétel:** B2 és az alábbi új fogalmak magyarázata.

A fő program megfelelően beírt adatokat feltételezett. Most külön vizsgáljuk a már számmá alakított darabszámokat és a pénzt, valamint az igen/nem választ. Nem kezdünk ciklust vagy kivételkezelést tanulni.

### Új eszközök: and, or, not

Az `and` két logikai feltétel együtt teljesülését írja le. Az `or` legalább egy igaz részfeltételt kér. A `not` megfordítja a logikai értéket. A részfeltételeknek nevet adhatunk, így az elágazás a feladat nyelvén is olvasható lesz.

Külön szemléltető program, amelyet a tutor elmagyaráz:

```python
eletkor = 20
idoszak = "reggel"

kor_jo = eletkor >= 0 and eletkor <= 120
idoszak_jo = idoszak == "reggel" or idoszak == "delutan"

if not (kor_jo and idoszak_jo):
    print("Javítsd az adatot.")
else:
    print("Az adatok elfogadhatók.")
```

Mindkét életkorhatárnak teljesülnie kell. Az időszaknál az egyik elfogadott szöveggel való egyezés elég. A zárójel összefogja a két adatcsoport együttes megfelelőségét, a `not` ennek hibás esetét jelöli. A minta nem a büfé teljes megoldása: a saját adatcsoportjaidra írd meg a feltételeket.

### Most egészítsd ki a büfét

1. A bemenetek után készíts logikai változót annak jelölésére, hogy mindkét darabszám nemnegatív.
2. Egy másik változó azt jelezze, hogy a válasz pontosan `"igen"` vagy `"nem"`. Mindkét oldalon teljes összehasonlítást írj; az `or "nem"` önmagában nem azt jelenti, hogy a válasz nemet tartalmaz.
3. Külön vizsgáld a fizetett összeg nemnegativitását.
4. Ha bármely adatcsoport hibás, írj rövid, javítást kérő üzenetet. A számítás és a teljes nyugta kizárólag az elfogadó ágban fusson.

A meglévő sorok megfelelő blokkba mozgatásakor a behúzás változik. Ne töröld a saját függvényeidet. A főprogram érvényes ága négy szóközzel, az azon belüli fizetési elágazás törzse további négy szóközzel lesz beljebb. A nulla darabszám továbbra is megengedett.

**Ellenőrzés:** a korábbi jó B2-próbák továbbra is működjenek. Ezután külön-külön írj negatív kávédarabszámot, negatív szendvicsdarabszámot, negatív pénzt, illetve `talan` választ. Mindegyiknél hibaüzenetet várunk, kiszámított nyugtát nem.

**Korlát:** a `ketto` vagy `2.5` szöveget az `int` nem tudja egész számmá alakítani, ezért a program még a most írt ellenőrzés előtt hibázhat. Ezt a K2 nem oldja meg. A hibás futás után indíts újra és adj megfelelő bemenetet; a hibákból visszatérő ismételt bekérés későbbi téma.

## K3 – logikai értéket visszaadó függvény

**Fájl:** `parossag.py`. **Becsült idő:** 7 perc. **Előfeltétel:** return és összehasonlítás.

A kiinduló program a `darabszam % 2` értékét írja ki. A `%` osztási maradékot számol. Páros egész számnál a kettővel való osztás maradéka nulla, ezt a `== 0` összehasonlítás ellenőrzi. Az összehasonlítás eredménye maga is visszaadható logikai érték.

Rövid, külön minta egy másik tulajdonság visszaadására:

```python
def pozitiv_e(szam):
    return szam > 0
```

Ez nem ír ki; a hívó True vagy False értéket kap a paramétertől függően.

**Írd meg** a `paros_e` függvényt, amely egy egész számot kap és annak párosságát adja vissza. A fájl jelenlegi kiírását cseréld a függvény eredményének kiírására. Próbáld ki 6-tal, 7-tel és 0-val: az eredmény True, False, True legyen. A nulla is páros.

Ha ez kész, a hívás eredményére építs if–else ágat: logikai szavak helyett „Páros” vagy „Páratlan” jelenjen meg. A döntési szabály maradjon a függvényben, a szöveges megjelenítés a hívóban.
