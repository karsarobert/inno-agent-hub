# EP_07 – Önálló alkalmazás

A Z1 első próbálkozásakor a követelmény és a tesztek járnak; kész célalgoritmus nem. Elakadásnál fokozatos tutori segítség kérhető.

## Z1 – Teljesíthető-e a rendelés?

**Fájl:** `onallo.py`. **Tervezett idő:** 12 perc.

### Mit csinál majd a program?

A kosárlistából és az árjegyzékszótárból új halmazban visszaadod a hiányzó termékfajtákat. A hívó a hiány alapján érthető üzenetet jelenít meg.

### Mi van előkészítve?

A függvény jelenlegi üres halmaza csak helykitöltő. A próbaadatok és a visszatérés tárolása adott. A terméknevek már egységesítettek. Az árjegyzékben a kulcsok a terméknevek; itt elérhetőséget, nem készletdarabszámot vizsgálunk.

Első próbálkozáskor a követelményt és a teszteket kapod, kész algoritmust nem. A korábbi feladatokban már használtál egyedivé alakítást, csoportkülönbséget és függvényes visszatérést.

### Most te alakítsd át

1. Alakítsd át a hianyzo_termekek függvényt úgy, hogy a paraméterként kapott adatokból új halmazban adja vissza az árjegyzékben nem szereplő termékfajtákat. Ismételt hiányzó termék egyszer legyen benne.
2. A főprogram nyers eredménykiírását alakítsd érthető döntéssé. Ha nincs hiányzó elem, jelezze, hogy teljesíthető; egyébként mutassa meg a hiányzó termékeket rendezett megjelenítéssel.
3. A függvény ne kérdezzen, ne írjon ki, és ne módosítsa a kosarat vagy az árjegyzéket. Üres kosárból üres hiányzó halmaz készüljön.
4. Végezd el a Z1.1–Z1.5 próbákat. A kódot általánosítsd: az újonnan kínálatba vett tea miatt csak az adatot kelljen megváltoztatnod.

### Kész, ha

- Új set az eredmény, a hiányzó termékfajták helyesek és egyediek.
- A függvény paraméterekből dolgozik, nem globális kosárból/árjegyzékből.
- A két bemenet változatlan; a döntés és megjelenítés a hívóban van.
- Az összes előírt próba eredménye ismert; az üres eredmény nem None.

### Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | Alapárjegyzék; kosár: ["kávé", "üdítő"]. | Üres halmaz; a hívó jelzi, hogy a rendelés teljesíthető. |
| Z1.2 | Alapárjegyzék; kosár: ["kávé", "tea"]. | A hiányzó halmaz egyetlen eleme tea; a hívó a hiányt és a termék nevét mutatja. |
| Z1.3 | Alapárjegyzék; kosár: ["tea", "tea", "pizza"]. | A hiányzó halmaz elemei tea és pizza, mindkettő egyszer. |
| Z1.4 | Alapárjegyzék; üres kosár. | Üres halmaz, hiba nélkül. A program szabálya szerint teljesíthető: nincs hiányzó termék. |
| Z1.5 | A Z1.2 adataihoz futás előtt vedd fel a "tea": 350 bejegyzést az árjegyzékbe. | Üres hiányzó halmaz, teljesíthető rendelés. Csak a próbaadat változik, a függvény nem. A függvény mindegyik próbában változatlanul hagyja a bemeneteket. |

Kapcsolódó magyarázat: [EP_07.html](EP_07.html#atvitel).
