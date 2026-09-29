# EP_04 – önálló alkalmazás

A Z1 a 90 perces főút része. Nem házi feladat és nem újabb vizsga.

## Z1 – Önálló törlés név szerint

**Fájl:** `onallo.py`. **Tervezett idő:** 12 perc.

### Mire szolgál ez a rész?

Új függvényben kapcsolod össze a szöveg egységesítését, a listatagságot és a törlést.

### Előbb értsük meg

A tetelt_torol(kosar, keresett_termek) a paraméterben kapott listát módosítja. Az egységesített terméknév első előfordulását törli. Siker esetén True, hiány esetén False az eredmény. A függvény nem kérdez és nem ír ki. A főprogram mutatja meg az eredményt és a listát.

### Most te írd meg

1. A kezdő függvényt te írd meg a fenti követelmény szerint. Használhatod a saját T1 segédfüggvényedet, vagy a tanult metódusokat közvetlenül.
2. Te írd meg a próbahívásokat és a kiírásokat. Minden próba új, az adott sorban megadott kezdőlistából induljon; ne keverd össze a bemeneti adatot a keresett termékkel.
3. Az első három próbánál ugyanaz a háromelemű tesztkosár: ["kávé", "üdítő", "kávé"]. A negyediknél []. Az alábbi négy eset eredményét és a megmaradt listát is ellenőrizd.

### Kész, ha

- Az első egyezést törli; a kávé ismétlődése megmaradhat.
- A paramétereket használja, a keresést egységesíti, bool értéket ad.
- Hiányzó terméknél és üres listán nincs kivétel és nem módosul a lista.
- A tanuló saját próbahívásai és a lista utóállapotai is ismertek.

### Próbák

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


Referencia: [EP_04.html – kapcsolódó rész](EP_04.html#feladatok). A teljes célprogram bemásolása helyett a kért módosítást te készítsd el.
