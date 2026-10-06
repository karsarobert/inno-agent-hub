# EP_05 – választható elmélyítés

Az alábbi régi K-feladatok nem a 90 perces főút kötelező részei, nem házi feladatok. A gyorsan végzők új, elsődleges bővítése a [C1–C2 feladatsor](bufe_bovitesek.md); C3 és K5 ugyanott található. Csak külön választásra vagy a tanuló kérésére induljanak. A tutor itt is rövid mintát magyaráz, a tanuló módosít és futtat. Az elkészült főfeladatot ne írjátok felül: a tanuló külön saját másolatban is dolgozhat; a futtatóterminál és a fájl mappája egyezzen.

## K1 – Árjegyzék törlése és frissítése (10 perc)

Fájl: arfrissites.py. Kapcsolódó HTML-rész: modositas.

Készíts eltávolító függvényt, amely egységesített név alapján csak meglévő terméket töröl. A kivett árat adja vissza; hiánynál None legyen, és ne történjen módosítás. A HTML terem-törlési mintáját alakítsd paraméteres függvénnyé, megjelenítés nélkül.

Próbák: kávé kivétele → 450, a kulcs megszűnik; újabb kávékivétel → None, változatlan szótár; üres szótár → None. Itt a pop visszatérési értéke az ár, nem a termék neve. A clear és update külön, másolt tesztadatokon is kipróbálható; az update helyben változtat és None-t ad.

## K2 – Legdrágább kosártétel (12 perc)

Fájl: onallo.py. Kapcsolódó HTML-rész: elmelyites.

A legnagyobbterem-példát alakítsd olyan függvénnyé, amely kosarat és árjegyzéket kap. Csak a megvásárolt tételek közül adja vissza a legdrágább termék nevét. Üres kosárra None; azonos árnál az első kosárbeli tétel maradjon. A kosár minden eleme ismert kulcs.

Próbák: [kávé, üdítő] → kávé; [croissant, szendvics] → szendvics; [] → None. Pluszpróba: külön tesztárjegyzékben két külön termék azonos árral, fordított kosársorrenddel. Az árjegyzék drágább, de meg nem vásárolt terméke ne legyen eredmény.

## A korábbi K3 helyett: C1 és C2

Az összevont blokk most részletes, kétlépéses feladat külön kezdőfájlokkal: [bufe_bovitesek.md](bufe_bovitesek.md). Aki C1–C2-t megoldotta, annak ez nem újabb feladat.

## K4 – Napi forgalom több kosárból (20 perc)

Fájl: onallo.py. Kapcsolódó HTML-rész: beagyazott.

Rendelésazonosító → kosárlista szótárt dolgozz fel. Használd a saját B1 összegződet a rendelésekhez. A napi alapösszeget és a tételek összes darabszámát add meg; most nincs diákkedvezmény vagy fizetésfeldolgozás.

Próba: R1 → [kávé, kávé], R2 → [üdítő], R3 → []; alapárakkal 1290 Ft és 3 tétel. Üres napi szótárra mindkettő 0. A megrendelések számát ne keverd össze a tételek számával.
