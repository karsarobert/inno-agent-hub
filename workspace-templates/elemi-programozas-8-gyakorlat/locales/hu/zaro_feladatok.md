# Z1 – Önálló termékjelentés

**Fájl:** onallo.py. **Tervezett idő:** 12 perc. Előfeltétel: A1–A3 és B1.b fő gondolatai. Az eladas_minta.txt előkészített adat, így Z1 nem függ a saját naplód korábbi futásszámától.

## A teljes cél

Egy kiválasztott termékről készítesz jelentést a mentett eladások alapján. A termek_adatai(fajlnev, keresett) függvény a termék eladott darabszámát és tárolt bevételét adja vissza két egészből álló tuple-ben, ebben a sorrendben. A főprogram háromsoros, friss szövegfájlt ment.

Adott a függvény aláírása, a (0,0) helykitöltő, a fájlnevek és a próbahívás. A helyes számító függvényt és a főprogram mentését te írod. A fájl minden nem üres sora terméknév;ár. A név már tisztított, a tárolt ár érvényes, nemnegatív egész. A fájl végső sortörése nem előfeltétel. A fizikai üres/whitespace sorokat kihagyjuk.

## Követelmények

1. A számító függvény csak a paraméterben megadott fájlt és pontosan egyező terméknevet használja. Nem kérdez és nem ír ki, nem ír fájlt, nincs benne globális árjegyzék.
2. Minden egyező rekord egy eladott darab. A bevételt a hozzá tartozó, fájlban rögzített ár adja. A nulla árú egyezés is növeli a darabot. Hiányzó termékhez és üres fájlhoz (0,0) tartozik.
3. A főprogram a kimenet változóban megadott fájlba, UTF-8 kódolással, minden futáskor friss jelentést ír. A keresett név és a két eredmény a változókból származzon. A bemeneti fájlt nem változtatja meg.
4. A jelentés sorai alapadattal, végükön sortöréssel:

```text
Termék: kávé
Eladott darab: 2
Bevétel: 850 Ft
```

5. Végezd el a Z1.1–Z1.5 próbát. A következő futás jelentésében csak az aktuális próba adatai legyenek. A terminál három megfelelő sora mellett a mentett fájlt is ellenőrizd, szükség esetén frissített nézettel.

## Elfogadás

- A függvény új tuple-t ad két helyes egész értékkel; az adat jelentése és a nulla ár kezelése helyes.
- A keresett név és a fájlnév valódi paraméter, a megoldás nem kávéra vagy az alapfájl adataira beégetett.
- A főprogram ír, a számító függvény számol; a forrás változatlan, a jelentés friss és háromsoros.
- Minden kötelező próba ismert. A tesztlista elvárás, nem automatikus teljesítésigazolás.

## Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | `eladas_minta.txt`; keresett="kávé" | Tuple `(2, 850)`; jelentés: Termék: kávé / Eladott darab: 2 / Bevétel: 850 Ft, három külön sorban. |
| Z1.2 | Ugyanaz a fájl; keresett="víz" | `(1, 0)`; a nulla árú eladás is egy darab. A jelentés az új adatot tartalmazza. |
| Z1.3 | Ugyanaz a fájl; keresett="kakaó" | `(0, 0)`; a jelentés a keresett kakaó nevét és a két nullát tartalmazza. |
| Z1.4 | `ures.txt`; keresett="kávé" | `(0, 0)`, nincs hiba; háromsoros friss jelentés készül. |
| Z1.5 | `eladas_valtott.txt`; keresett="kávé" | `(3, 1050)`; a jelentésben 3 és 1050 Ft. Csak a bemenet és a keresett paraméter változik. |

## Segítség elakadáskor

Az első próbálkozás előtt a tutor csak a követelményt, formátumot és példakimenetet tisztázza. Elakadáskor előbb azt vizsgálja, hogy a beolvasás, a termékfeltétel, a két számláló vagy a mentés lépése bizonytalan-e. Szükség esetén egy kapcsolódó korábbi analóg mintára utal, majd a konkrét hibás részhez ad fokozatos segítséget. Kész célfüggvényt vagy teljes mentőblokkot nem ad előre.
