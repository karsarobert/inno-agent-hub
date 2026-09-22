# EP_03 – külön időben végezhető kiegészítők

Ezek nem a 90 perces főút rejtett befejezési feltételei. A tanuló itt is maga írja és futtatja a kódot; a tutor elmagyarázza az új fogalmat, rövid analóg mintát mutat, majd egy módosítást kér. A HTML megfelelő kiegészítő fejezete használható referenciaként. A működő saját változatot ne állítsuk vissza az eredeti mintára.

## K1 – több vendég, napi bevétel (15 perc)

**Fájl:** `bufe_03.py`, a kész B3 után. A főút előre megadott kosarat dolgozott fel. Most ugyanennek a kosárnak a kiszolgálását ismételjük több vendégre; a kosár futás közbeni összeállítása későbbi téma.

A meglévő, egy vásárlást kezelő műveleteket szervezd `egy_rendeles(kosar)` függvénybe. Csak a befejezett fizetés után adja vissza a fizetendő összeget; üres kosárra 0-t. A főprogram kérjen vendégnevet q végjelig, hívja meg a függvényt, és halmozza a visszaadott értékeket. Csak a pozitív bevételű rendelés növelje a kifizetett rendelések számát. A napi számlálók a külső ciklus előtt legyenek.

Próbák: azonnali q → 0 rendelés, 0 Ft. A négytermékes kosárral Anna/igen/2000, majd Béla/nem/2500, végül q → 2 rendelés, 4142 Ft bevétel. A visszajáró nem bevétel. A belső fizetési ciklus befejezése még nem a napi külső ciklus vége.

## K2 – visszaszámlálás és üres tartomány (8 perc)

**Fájl:** `tartomany.py`. Írd át a for ciklust, hogy 5-től 1-ig számoljon vissza, majd egyszer írja ki: Indulhatunk! Használj negatív lépésközt. Ezután próbáld az azonos kezdő- és végértéket: csak a ciklus utáni sor jelenjen meg. A lépésköz 0-val hibás, nem üres tartomány.

Ha a ciklusváltozó értékére nincs szükség, a `for _ in range(...)` alakban az `_` szokásos, nem használt értéket jelző változónév. Írj vele három azonos köszöntést.

## K3 – a diákság válaszának újrakérése (10 perc)

**Fájl:** `bufe_03.py`. A főút pontos igen/nem választ feltételezett. Írj `igen_nem_beker(kerdes)` függvényt, amely más válasz esetén újra kérdez, majd logikai értéket ad vissza. A hibás válasz egyszerre nem igen és nem nem; ehhez a két egyenlőtlenség között and szükséges. A bool(valasz) nem helyettesíti az igen szöveggel való összehasonlítást.

Előbb a függvényt készítsd el és próbáld, majd a büfé régi bekérését váltsd a hívására. Próbák: talan, igen → újrakérés után kedvezmény; nem → nincs újrakérés és nincs kedvezmény. A kis/nagybetű és a környező szóköz normalizálása most nem követelmény.

## K4 – indexelés és szeletelés (8 perc)

**Fájl:** `kosar.py`. A meglévő bejárást tartsd meg. A négytermékes listán írj külön kiírásokat az első elemre, az utolsó elemre, az első két elemre és a középső két elemre. Az utolsó elemet negatív indexszel módosítsd teára, majd járd be újra a listát. A módosítás nem bővíti a listát.

Az index 0-tól indul. A szelet végpontja kizárt, és a szeletelés új listát ad. Üres listán a [0] és a [-1] hibás; ezt ne keverd össze az üres listán biztonságosan végigfutó, nulla kört végző forral. A 350 Ft-os tea árát külön bővítésként kell hozzáadni a termek_ara függvényhez, ha számolni is szeretnél vele.

## K5 – keresés és a ciklus else ága (10 perc)

**Fájl:** `kosar.py`. Írj külön keresést üdítőre. Találatnál írj egy üzenetet és lépj ki breakkel; ha a bejárás végéig nem találtál, a ciklus else ága jelezze a hiányt. Az else a for sorával azonos behúzású.

Próbáld: üdítőt tartalmazó lista, üdítő nélküli lista és üres lista. A hiányjelzés az utolsó két esetben jelenik meg. Az else nem az if hamis ága, hanem a break nélküli szabályos ciklusbefejezéshez tartozik; return vagy kivétel is megakadályozhatja az elérését.

## K6 – teknőcgrafika (10 perc, csak megfelelő helyi környezetben)

Előbb magyarázd el a modul és az import szerepét. A tanuló hozzon létre `rajz.py` fájlt ugyanabban a munkamappában. A HTML teknőcgrafikai mintájából indulva írjon háromszöget rajzoló saját függvényt, három ismétléssel és 120 fokos fordulattal. `import turtle` és `turtle.` előtag legyen, ne csillagos import.

A turtle.done() az eseménykezelést indítja és nyitva tartja az ablakot, nem azonnal bezárja. Grafikus környezet nélküli távoli futtatásban a példa nem feltétlenül használható. Környezeti akadály esetén ne telepítsünk csomagot automatikusan; a feladat kihagyható, a főút ettől teljes marad.
