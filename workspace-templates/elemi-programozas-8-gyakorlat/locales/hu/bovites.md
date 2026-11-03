# C1 – Összes termék napi riportja

**Fájl:** napi_riport.py. **Tervezett idő:** 15 perc. Ez az egyetlen választható programozási bővítés. Z1 után, T1 előtt kezdhető, ha legalább 42 ténylegesen fennmaradó perc ismert: 15 perc feladat + 27 perc teszt és lezárás. A teljes tervezett út 105 perc; 90 percbe csak megtakarított idővel fér. Bizonytalan időnél a tutor egyszer tisztáz. A bővítés nem kötelező házi feladat.

## Mit csinál majd a program?

A napló minden termékéhez eladott darabszámot és tárolt bevételt rendelsz. A termekenkenti_osszesites(fajlnev) eredménye új szótár, amelynek kulcsa a terméknév, értéke (darab, bevetel) tuple. A napi_riportot_ment(fajlnev, osszesites) külön, friss szövegfájlt ír.

Adott a két aláírás, a helykitöltők és a hívások. A beolvasás, csoportosítás és mentés a te feladatod. A formátum és a kihagyott üres sorok szabálya ugyanaz, mint B1-ben. Nem a jelenlegi árjegyzéket használod.

## Rövid analóg minta

```python
foglalasok = {"R1": (2, 30)}
darab, perc = foglalasok["R1"]
foglalasok["R1"] = (darab + 1, perc + 15)
print(foglalasok)
```

A tuple elemeit nem írjuk át; a kulcshoz új, frissített tuple kerül. A saját feladatban az első termékelőfordulás kezdőállapotát is kezelned kell. A számok itt teremfoglalást jelentenek, nem eladást.

## Két lépés

C1.a: készítsd el az összesítő szótárat. Egy termék többszöri előfordulása egy kulcshoz gyűljön; az árak akár eltérhetnek. Üres fájlból üres szótár legyen.

C1.b: a mentő w/UTF-8 móddal először írja a termek;darab;bevetel fejlécet. Utána a kulcsok sorted sorrendjében egy termék egy sorba kerüljön, például kávé;2;850. Minden sor végén legyen sortörés. A sorted itt a Python szövegrendezése, nem magyar szótári rendezést állítunk be. A mentő ne módosítsa a kapott szótárat.

## Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | `eladas_minta.txt` | Az adatszótár: kávé → (2,850), tea → (1,350), víz → (1,0), szendvics → (1,890). A riport első sora `termek;darab;bevetel`, majd a kulcsok `sorted` sorrendjében kávé, szendvics, tea, víz. |
| C1.2 | `ures.txt` | Üres szótár; a riport csak a sortöréssel lezárt fejlécet tartalmazza. |
| C1.3 | `eladas_valtott.txt` | kávé → (3,1050), tea → (2,670); két adatsor a fejléc után. Korábbi riportsor nem marad meg. |

Kész, ha mindkét függvény teljesíti a fenti szerepét, minden kiválasztott próba ismert és a bemenetek változatlanok. Ezután T1 következik; nincs újabb automatikus extra.
