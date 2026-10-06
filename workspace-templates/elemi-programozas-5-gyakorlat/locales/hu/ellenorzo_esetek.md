# EP_05 – ellenőrző esetek

Ezek tervezett próbák, nem igazolt tanulói futások. A1.4 opcionális; a többi felsorolt eset szükséges a teljes feladatigazoláshoz. A kódot, a tesztadatot, a tényleges eredményt és a bizonyíték forrását különböztesd meg.

Az arfrissites.py módosítja az árjegyzéket: a próbákat új, alapáras futásból indítsd. A3 és Z1 határfeltétele különböző: A3 <= keret, Z1 > határ. B1 minden kosárneve érvényes kulcs; a B2 bekérő szűri az ismeretlen neveket.

A kiírások tartalma számít. A listák egyszeres/kettős idézőjele vagy a szokásos szóközeltérés nem hiba. A téves terméknév, hiányzó összeg, rossz pénznem vagy hibás műveleti sorrend viszont érdemi eltérés.

## A1 – `arkereses.py`

### A1.1

Alapárjegyzék; keresett_termek = "  KÁVÉ  ".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Ár: 450 Ft


### A1.2

Alapárjegyzék; keresett_termek = "pizza".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Nincs ilyen termék.
- A pizza nem kerül bele az árjegyzékbe.


### A1.3

Alapárjegyzék; keresett_termek = "   ".

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Nincs ilyen termék.


### A1.4 – választható pluszpróba

Pluszpróba: ideiglenesen vedd fel a "víz": 0 bejegyzést; keresd a vizet.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Ár: 0 Ft; nem hiányjelzés.


## A2 – `arfrissites.py`

### A2.1

Új futás az alapárakkal; " KÁVÉ ", 500.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- True; a kávé ára 500 Ft.
- Továbbra is négy kulcs van; a többi ár változatlan.


### A2.2

Új futás az alapárakkal; "pizza", 700.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; nincs pizza kulcs; az árjegyzék teljesen változatlan.


### A2.3

Új futás az alapárakkal; "kávé", 0.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; a kávé ára 450 marad.


### A2.4

Új futás az alapárakkal; "kávé", -50.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- False; a kávé ára 450 marad.


## A3 – `kinalat.py`

### A3.1

Alapárjegyzék; keret = 450.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- ["kávé", "üdítő"]; a megadott beszúrási sorrendben.


### A3.2

Alapárjegyzék; keret = 389.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- []


### A3.3

Alapárjegyzék; keret = 890.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- ["kávé", "szendvics", "üdítő", "croissant"]


### A3.4

arak = {}; keret = 450.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- []; hiba nélkül.


## B1 – `osszegzes.py`

### B1.1

Alapárjegyzék; kosar = ["kávé", "üdítő", "kávé"].

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Blokksorok: kávé 450 Ft; üdítő 390 Ft; kávé 450 Ft.
- Tételek száma: 3; rendelés: 1290 Ft.


### B1.2

Ugyanez a kosár; csak a kávé árát állítsd 500-ra.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- A két kávés sorban 500 Ft; rendelés: 1390 Ft.


### B1.3

kosar = []; bármelyik fenti árjegyzék.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Tételek száma: 0; rendelés: 0 Ft.


### B1.4

Kávé ismét 450; az árjegyzékbe vedd fel a "tea": 350 párt; kosar = ["tea", "kávé"].

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Két tétel; rendelés: 800 Ft.
- Az új termékhez nem kellett új elágazás a függvénybe.


## B2 – `bufe_05.py`

### B2.1

A négy alapár szerepeljen; a kávé 450 Ft.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

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

Alapárjegyzék; hibás igen/nem után nem diák.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `"kávé"`
2. `"üdítő"`
3. `"fizetek"`
4. `"talán"`
5. `" NEM "`
6. `"800"`
7. `"40"`

Elvárt viselkedés:

- A talán után újra kérdez.
- Fizetendő: 840 Ft
- Még hiányzik: 40 Ft
- Csak a pótlás után: Visszajáró: 0 Ft.


### B2.3

Új futás, üres kosár.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `"mégse"`
2. `"fizetek"`

Elvárt viselkedés:

- Üres a kosár, nincs mit törölni.
- Tételek száma: 0; Nincs fizetendő tétel.
- Nincs diákság- és pénzbekérés.


### B2.4

Alapárjegyzék; érvénytelen bevitel és visszavonás.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `""` – csak Enter
2. `"pizza"`
3. `"kávé"`
4. `"croissant"`
5. `"mégse"`
6. `"ÜDÍTŐ"`
7. `"fizetek"`
8. `"nem"`
9. `"1000"`

Elvárt viselkedés:

- Az üres szövegre és pizzára figyelmeztetés.
- Törölve: croissant
- A végső kosár kávé és üdítő, két tétel.
- Fizetendő: 840 Ft; visszajáró: 160 Ft.


### B2.5

Csak a bufe_05.py egyetlen árjegyzékében: kávé 500, új tea 350. A többi ár változatlan.

Terminálbemenetek sorban, mindegyik után Enter. Az idézőjelek nem begépelendők; az üres szöveg csak Entert jelent.

1. `" TEA "`
2. `"kávé"`
3. `"fizetek"`
4. `"nem"`
5. `"1000"`

Elvárt viselkedés:

- A tea elfogadott termék.
- Blokk: tea 350 Ft, kávé 500 Ft.
- Fizetendő: 850 Ft; visszajáró: 150 Ft.


## Z1 – `onallo.py`

### Z1.1

Alapárjegyzék; kosar = ["kávé", "szendvics", "szendvics"]; hatar = 500.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Drága tételek száma: 2


### Z1.2

Ugyanez a kosár és árjegyzék; hatar = 890.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Drága tételek száma: 0; a pontos határ nem számít.


### Z1.3

Ugyanez a kosár és árjegyzék; hatar = 449.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Drága tételek száma: 3


### Z1.4

kosar = []; hatar = 500.

A tesztadatokat a fájlban vagy a saját próbahívásban állítsd át, majd ments és futtass.

Elvárt viselkedés:

- Drága tételek száma: 0


## C1–C3 és K5 ellenőrzése

Az új feladatok teljes esetei a [bufe_bovitesek.md](bufe_bovitesek.md) megfelelő táblázataiban szerepelnek: C1.1–C1.4, C2.1–C2.4, C3.1–C3.5, K5.1–K5.4. Ezek próbaelőírások, nem elvégzett futások. Csak a kiválasztott bővítések teljesítéséhez szükségesek; a ki nem választott bővítések nem teszik hiányossá az alaputat.
