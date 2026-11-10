# C1 – Csak teljesen ellenőrzött kosár kerüljön a naplóba

**Fájl:** mentes.py. **Tervezett idő:** 15 perc. Az egyetlen választható programozási bővítés. Z1 után, T1 előtt indulhat, ha legalább 42 ténylegesen fennmaradó perc ismert: 15 perc munka + 27 perc teszt/lezárás. A teljes tervezett út 105 perc, ezért a 90 perces órába csak időnyereséggel fér. Bizonytalan időnél a tutor egyszer tisztáz.

## Mit csinál majd a program?

A kosarat_ment(fajlnev,kosar,arak) csak akkor nyitja meg hozzáfűzésre a naplót, ha a saját Z1-függvény szerint az egész kosár érvényes. Egyetlen hibás tétel esetén semmi nem kerül a fájlba, még a korábban vizsgált jó tétel sem. Ez az adatellenőrzés előtti és az írás előtti döntés összekapcsolása.

A saját A2 és Z1 függvénydefinícióidat hozd át a helykitöltők helyére. A főprogramokat ne másold át. A napló új sora termék;darab;aktuális_egységár, a végén sortöréssel. Minden kosártétel külön rekord; a sorok nem vonódnak össze. A 0 egységár érvényes.

## Rövid analóg minta

```python
engedelyezett = False
if not engedelyezett:
    print("Nem indítjuk el a műveletet.")
else:
    print("Most következhetne a művelet.")
```

A minta csak a döntés és a későbbi művelet sorrendjét szemlélteti. A saját ellenőrzést a korábbi Z1 végzi, a művelet pedig valódi, célzottan kezelt fájlírás lesz.

## Követelmények

- Előbb a teljes kosár Z1-ellenőrzése történjen. Hibás kosárnál értelmes jelzés és False; a fájlt megnyitni sem szabad. A meglévő cél változatlan, hiányzó cél nem jön létre.
- Üres, hibátlan kosárnál True, Nincs mentendő tétel jelzés, de nincs fájlmegnyitás és új fájl sem keletkezik.
- Nem üres, érvényes kosárnál a/UTF-8 megnyitás és az előírt hárommezős rekordok hozzáfűzése következik. A korábbi sorok megmaradnak. Előfeltétel: a meglévő saját napló minden korábbi rekordja sortöréssel lezárt.
- Írási OSError esetén False és hibaüzenet; True/siker csak a with rendes lezárása után. A paraméterek megmaradnak.
- A kész célfájlt nyisd meg, szükség esetén frissítsd a nézetet. Ugyanaz a program második futása új mentésnek számít.

Az adatellenőrzési hiba előtti fájlvédelem nem atomi fájlművelet. Írás közbeni OSError után a cél lehet részben módosult; a feladat nem kér tranzakciót, visszagörgetést vagy biztonsági másolatos cserét. Ezt nem állítjuk sikernek.

## Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | Új, még nem létező uj_eladasok.txt; kosár [("kávé",2),("víz",3)]; alapárak | True; két rekord: kávé;2;450 és víz;3;0, mindkettő sortöréssel. Második futás után négy sor, a korábbi két sor megmarad. |
| C1.2 | Meglévő cél tartalmát megtartva kosár [("kávé",1),("tea",0)]; utána ugyanez másik, még nem létező célra | False; meglévő cél bájtra változatlan, hiányzó cél nem jön létre. A valid kávé sem kerül részlegesen a naplóba. |
| C1.3 | Üres kosár, még nem létező cél | True, nincs mentendő tétel; a cél nem jön létre. |
| C1.4 | Érvényes kosár, cél=ures.txt/naplo.txt | False és OSError-visszajelzés; nincs sikerüzenet, a források és az ures.txt változatlanok. |

Egy már használt saját naplót ne törölj a próba kedvéért. A két-/négysoros elvárás új fájlra vonatkozik; meglévőnél a pontos új rekordok hozzáfűzését vizsgáld, vagy válassz új saját célnevet. A csomagolt bemeneteket ne használd mentési célnak.

C1 után a két záróteszt következik; nem indul automatikusan újabb extra vagy kötelező házi feladat.
