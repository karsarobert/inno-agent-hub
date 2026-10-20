# C1 – Két kosárból összesített rendelési riport

Egyetlen választható, összetett pluszfeladat, tervezetten 15 perc. A fő programozási rész után, T1 előtt indulhat, ha ténylegesen legalább 42 perc marad: 15 perc C1 és 27 perc teszt/lezárás. Ha az idő nem ismert, a tutor egyszer tisztázza. Az alapút C1-gyel tervezetten 105 perc; a 90 perces keretben csak tényleges korábbi időnyereséggel férhet el. A C1 nem kötelező házi feladat.

**Fájl:** `riport.py`. **Előfeltétel:** A1, A2, A3 és Z1 elkészült, vagy az oktató kifejezetten ezt a bővítést választja ismert előismeretekkel.

## Mit készítesz?

Két kosár és egy árjegyzék alapján termékenként egy riportsort. Minden sor tuple: terméknév, összes darabszám, egységár, részösszeg. A számító függvény új listában, terméknév szerint rendezve adja ezeket. A külön megjelenítő függvény soronként mutatja a mezőket és a végösszeget.

Minden kosártétel ismert kulcs az árjegyzékben; ezt most előfeltételként adjuk. A hiányzó termék kezelését a Z1 már gyakoroltatta. Itt ne bővítsd a feladatot fájlkezeléssel, kivételkezeléssel vagy készletdarabszámokkal.

## Mi adott, mit írsz te?

A próbaadatok és a függvénynevek adottak, a számítások helykitöltők. A saját `kosar_adatai` definíciódat az A2-ből használd újra. Csak a definíciót másold, a korábbi főprogramot és próbaadatokat ne. Az összesítés és a megjelenítés új saját munka.

## Rövid analóg minta

```python
meresi_sorok = [("reggel", 3, 4), ("este", 2, 5)]
for napszak, darab, egysegertek in meresi_sorok:
    reszertek = darab * egysegertek
    print(f"{napszak}: {reszertek}")
```

Itt az adat-hármasok már készen vannak, és csak a részértéket számoljuk. A saját feladatodban a két kosárból előbb elő kell állítanod a termékenkénti összes darabszámot; az eredmény már négyelemű tuple-öket tartalmaz. A két kosár összevonása közben az eredetieket őrizd meg.

## C1.a – Adatok előállítása, kb. 9 perc

1. Vidd át a saját A2-függvényed definícióját a megjelölt helyre.
2. A `rendeleseket_osszesit` készítsen a két kosárból új közös feldolgozási adatot. Az eredeti listákat ne bővítse és ne törölje.
3. Minden különböző termék egyszer szerepeljen. A saját A2-függvényeddel kérd le az adott termék összes darabszámát az összesített kosárban; használd a visszatérő tuple megfelelő elemét vagy kicsomagolását.
4. A paraméter árjegyzékből olvasd az egységárat, számíts részösszeget, és új tuple-ként vedd fel az eredménylistába. A lista legyen terméknév szerint rendezett. A számító függvény ne írjon ki.
5. Egy rövid saját próbahívással ellenőrizd a visszakapott sorokat, mielőtt a megjelenítést készíted.

## C1.b – Megjelenítés, kb. 6 perc

1. A `riportot_megjelenit` a kapott sorokat járja be, és csomagolja ki a négy mezőt.
2. A sorok mutassák a terméket, a darabszámot, az egységárat és a részösszeget.
3. A részösszegekből számíts végösszeget, és a teljes bejárás után jelenítsd meg. Üres sorlistánál 0 Ft legyen.
4. A megjelenítés ne módosítsa a kapott listát. A pontos szorzásjel és szóköz nem követelmény; a számítás igen.

## Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | Az előkészített két kosár és árjegyzék. | Rendezett tétel-tuple-ök: ("kávé", 2, 450, 900), ("szendvics", 1, 890, 890), ("üdítő", 2, 390, 780). Összesen 2570 Ft. |
| C1.2 | Mindkét kosár üres. | Új üres lista; nincs terméksor; összesen 0 Ft. |
| C1.3 | arak = {"tea": 350, "kakaó": 350}; első kosár ["tea", "kakaó"], második ["tea"]. | Két sor: kakaó 1 db, 350 Ft részösszeg; tea 2 db, 700 Ft részösszeg; összesen 1050 Ft. Azonos egységár miatt nem olvad össze két termék. |
| C1.4 | A C1.1 adatai; csak a kávé ára legyen 500. | Kávé részösszege 1000 Ft; a teljes összeg 2670 Ft. A kosarak és az árjegyzék minden hívás során változatlanok. |

## Kész, ha

- A saját A2-függvényt használod, és nem cseréled át a korábbi jelentését.
- Új lista tér vissza, rendezett négyelemű tuple-ökkel, termékenként egyszer.
- Minden darab szerepel a számításban; a két azonos árú, különböző termék nem olvad össze.
- A megjelenítés külön működik, a bemenetek változatlanok, az előírt próbák eredménye ismert.

Ezután T1 → T2 → S2 következik; újabb pluszfeladatot nem indítunk automatikusan.
