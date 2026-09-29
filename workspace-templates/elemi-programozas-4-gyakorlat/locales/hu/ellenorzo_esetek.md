# EP_04 – ellenőrző esetek

Ezek tervezett próbák, nem a tanuló elvégzett futásai. Csak az aktuális fájlhoz és aktuális módosításhoz tartozó, ténylegesen ismert eredményt jelöld igazoltnak. A fájlbeli tesztadatokat és próbahívásokat a tanuló írja át. A T1.3 választható, minden más itt felsorolt fő próba kötelező a teljes feladatigazoláshoz.

A B1 csak kosárépítés: a futás a lista kiírásával véget ér. A B2 pénzösszegei a kész, összekapcsolt programra vonatkoznak. A starter változatok nem teljesítik automatikusan ezeket a próbákat.

## T1 – `szoveg.py`

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


## T2 – `kodresz.py`

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


## T3 – `karakterszam.py`

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


## L1 – `listamuveletek.py`

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


## L2 – `feldolgozas.py`

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


## B1 – `kosar_04.py`

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


## B2 – `bufe_04.py`

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


## Z1 – `onallo.py`

### Z1.1

Új tesztkosár ["kávé", "üdítő", "kávé"]; keresett = " KÁVÉ ".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- True
- Megmaradt lista: ["üdítő", "kávé"]


### Z1.2

Új tesztkosár ["kávé", "üdítő", "kávé"]; keresett = "üdítő".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- True
- Megmaradt lista: ["kávé", "kávé"]


### Z1.3

Új tesztkosár ["kávé", "üdítő", "kávé"]; keresett = "tea".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- False
- Változatlan lista: ["kávé", "üdítő", "kávé"]


### Z1.4

Új üres kosár []; keresett = "kávé".

Nincs interaktív terminálbemenet; a tesztadatokat a fájlban vagy saját próbahívással módosítod.

Elvárt viselkedés:

- False
- Változatlan lista: []
