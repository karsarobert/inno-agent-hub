# EP_03 – ellenőrző esetek

Ezek a tanuló saját futásaihoz tartozó próbaadatok. Az elvárt kimenet ismerete nem helyettesíti a kódírást. A próbák itt **tervezettek**; a dokumentum nem állítja, hogy a tanuló elvégezte őket.

Az adatok a lépés kész változatára vonatkoznak. C1 a külön blokk.py fájlt vizsgálja, terminálbemenet nélkül. Az üres kosár teljes büféprogramos próbája B3 végén esedékes, a bufe_03.py összeépítése után. A rövid kódolvasás, az aktuális fájl és az adott próba eredménye együtt ad bizonyítékot.

## E0 – `indulas.py`

### E0.1

A köszöntés szövegét írd át.

Nincs terminálbemenet.

Elvárt viselkedés:

- Szia, kezdjük a harmadik gyakorlatot!

## W1 – `sorszam.py`

### W1.1

Kezdés 1, felső határ 3.

Nincs terminálbemenet.

Elvárt viselkedés:

- Rendelés: 1
- Rendelés: 2
- Rendelés: 3
- A sorszámok elkészültek.

### W1.2

Kezdés 1, felső határ 5.

Nincs terminálbemenet.

Elvárt viselkedés:

- Öt sorszám, 1-től 5-ig; egy lezáró sor.

### W1.3

Kezdés 6, felső határ 5.

Nincs terminálbemenet.

Elvárt viselkedés:

- Csak a lezáró sor; nincs rendelési sorszám.

## W2 – `bekeres.py`

### W2.1



Bemenetek sorban (egyenként Enter):

```text
-2
-1
2
```

Elvárt viselkedés:

- Két figyelmeztetés és újrakérés.
- Elfogadott darabszám: 2

### W2.2



Bemenetek sorban (egyenként Enter):

```text
0
```

Elvárt viselkedés:

- Elfogadott darabszám: 0
- Nincs újrakérés.

## F1 – `tartomany.py`

### F1.1

Sorszámok 1–3.

Nincs terminálbemenet.

Elvárt viselkedés:

- Három rendelési sor és egy lezárás.

### F1.2

Sorszámok 5–8.

Nincs terminálbemenet.

Elvárt viselkedés:

- Rendelés: 5
- Rendelés: 6
- Rendelés: 7
- Rendelés: 8
- A sorszámok elkészültek.

## B1 – `napi_osszesito.py`

### B1.1



Bemenetek sorban (egyenként Enter):

```text
1611
-20
1790
450
0
```

Elvárt viselkedés:

- A -20 figyelmeztetést kap, nem számít bele.
- Kifizetett rendelések: 3
- Napi bevétel: 3851 Ft

### B1.2



Bemenetek sorban (egyenként Enter):

```text
0
```

Elvárt viselkedés:

- Kifizetett rendelések: 0
- Napi bevétel: 0 Ft

## L1 – `kosar.py`

### L1.1

A megadott négy termék.

Nincs terminálbemenet.

Elvárt viselkedés:

- A kosárban: kávé
- A kosárban: szendvics
- A kosárban: kávé
- A kosárban: üdítő

### L1.2

kosar = []

Nincs terminálbemenet.

Elvárt viselkedés:

- Nincs terméksor és nincs IndexError.

## B2 – `kosar.py`

### B2.1

kávé, szendvics, kávé, üdítő

Nincs terminálbemenet.

Elvárt viselkedés:

- Kosár összege: 2180 Ft

### B2.2

csak kávé

Nincs terminálbemenet.

Elvárt viselkedés:

- Kosár összege: 450 Ft

### B2.3

üres lista

Nincs terminálbemenet.

Elvárt viselkedés:

- Kosár összege: 0 Ft

## C1 – `blokk.py`

### C1.1

kosar = ["kávé", "pizza", "üdítő"]

Nincs terminálbemenet. A blokk és a tételszám kiírása után a program véget ér.

Elvárt viselkedés:

- kávé: 450 Ft
- A pizza kihagyását jelző figyelmeztetés.
- üdítő: 390 Ft
- Elfogadott tételek: 2

## B3 – `bufe_03.py`

### B3.1

kávé, szendvics, kávé, üdítő

Bemenetek sorban (egyenként Enter):

```text
igen
2000
```

Elvárt viselkedés:

- Rendelés: 2180 Ft
- Kedvezmény: 218 Ft
- Fizetendő: 1962 Ft
- Visszajáró: 38 Ft

### B3.2

Ugyanaz a kosár.

Bemenetek sorban (egyenként Enter):

```text
igen
1900
62
```

Elvárt viselkedés:

- Még hiányzik: 62 Ft
- Visszajáró: 0 Ft

### B3.3

kosar = []

Nincs terminálbemenet.

Elvárt viselkedés:

- Elfogadott tételek: 0
- Nincs fizetendő tétel.
- Nem kér diákságot és pénzt.

## Z1 – `onallo.py`

### Z1.1

["kávé", "üdítő", "kávé"], keresett termékek: kávé, üdítő, tea; végül üres lista és kávé.

Nincs terminálbemenet.

Elvárt viselkedés:

- A négy eredmény rendre: 2, 1, 0, 0.

## További próba B3 után, ha marad idő

- Alapkosár, `nem`, `2500`: 2180 Ft fizetendő, 320 Ft visszajáró.
- Alapkosár, `igen`, `1962`: 0 Ft visszajáró, nincs pótláskérés.
- Alapkosár, `igen`, `1900`, `0`, `62`: a nulla pótlás után továbbra is 62 Ft hiányzik, majd 0 Ft visszajáró.
- Alapkosár, `igen`, `-1`, `1962`: a saját bekérő új pénzadatot kér a negatív helyett.
- `["kávé", "pizza", "üdítő"]`, `nem`, `1000`: 2 elfogadott tétel, 840 Ft fizetendő, 160 Ft visszajáró.
- `["pizza"]`: figyelmeztetés, 0 elfogadott tétel, nincs diákság- vagy pénzbekérés.

Ezek kiegészítő ellenőrzések, nem rejtett pluszfeladatok a 90 perc után. A `ketto`, a `2.5`, az EOF és egyéb nem egész alakú bemenet kezelése nem része a fő útnak.
