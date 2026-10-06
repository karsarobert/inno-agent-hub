# EP_05 – önálló alkalmazás

A Z1 a 90 perces főút része. A kezdő fájl rövid próbahívást ad; a saját munka a függvény átalakítása és a különböző tesztadatok alkalmazása.

## Z1 – Önálló átalakítás: drága tételek száma

**Fájl:** `onallo.py`. **Időkeret:** 10 perc.

### A program célja

A kosár olyan tételeit számolod, amelyek ára szigorúan nagyobb a megadott határnál.

### Értsük meg a kezdőmintát

A kezdő függvény a teljes kosár hosszát adja, ezért még nem válogat ár alapján. Az új eredmény egész darabszám legyen. A kétszer vásárolt szendvics két tételnek számít. A forrás a kosár; az összehasonlítandó ár a paraméter szótárból jön.

### Most te alakítsd át

1. A draga_tetelek_szama(kosar, arak, hatar) függvény jelenlegi törzsét alakítsd feltételes megszámlálássá saját ciklussal. A paraméter határt használd, ne beégetett 500-at.
2. A függvény csak eredményt adjon, ne írjon ki és ne módosítsa a bemeneteket. A főprogram már egy próbahívást tartalmaz; annak adatait te írd át a további esetekhez.
3. Ments és futtasd a négy próbát. Minden próbában csak érvényes terméknevek szerepelnek; az árjegyzék alapárai 450, 890, 390 és 520 Ft.

### Kész, ha

- Saját feltételes számláló ciklust ír a kosárra, az árakat a paraméter szótárból olvassa.
- Szigorúan >, nem >=; ismétlődések is külön tételként számítanak.
- Üres listára 0; nincs input, print vagy bemenetmódosítás a függvényben.

### Próbák

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


Kapcsolódó magyarázat: [EP_05.html](EP_05.html#onallo). A minta eszközeit a saját feladatodhoz alakítod; a teljes célmegoldást te készíted el.
