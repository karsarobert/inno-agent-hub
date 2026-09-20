# Oktatói előkészítés

A hallgatók számára az egyetlen környezeti teendő a környezetellenőrző
Run-nal történő indítása. Ha csomag hiányzik, **az oktató segítségét kérik**.
A tutor nem ad telepítési parancsot, nem próbál önálló telepítést végezni.

## Környezet

A csomag Linux x86-64, Python 3.12 és CPU használatára készült. Az ellenőrzött
főcsomag-verziók a requirements.txt-ben vannak. Ez nem minden közvetett
függőség teljes zárolása. A programok tensorflow.keras API-t használnak.
Nincs szükség GPU-ra, Colabra, Jupyterre, pandasra vagy hálózati adatletöltésre.

Az oktató az intézményi eljárás szerint előre biztosítsa a csomagokat és a
megfelelő Python-értelmezőt az Innoagent Run számára. A telepítés nem az óra
része. A tananyag nem változtat az alkalmazás beállításain.

## Óra előtti ellenőrzés

1. Az agent.md és a G03-programok közvetlenül a munkaterület gyökerében vannak.
2. A helyi Innoagent-preset az új agent.md-t használja; új beszélgetés indul.
3. A Run-nal indított kornyezet_ellenorzes.py sikerrel lefut.
4. A G03_03 16 neuronos változata, majd az 50–50 modell 0.01 és 0.001
   rátával is lefut. Az utóbbi összevetés kötelező hallgatói kísérlet.
5. A képfájlok az eredmenyek alatt keletkeznek; a Nézet frissítése után
   az intézményi felületen megnyithatók. Ennek pontos gombja felületfüggő.
6. A G03_04 a kiválasztott mentett modellt be tudja tölteni, és készít tesztábrákat.
7. A hallgatók saját kísérleti példányt kapnak: a tanári próbaeredményeket
   és kitöltött választási mezőket ne osszuk ki kész hallgatói teljesítésként.

A 150 epoch több külön futásban is szerepel; az óra előtt mérjük meg a
helyi gépen. Ha indokolt, az oktató egységesen csökkentheti a négy spirálfutás
epochkeretét; ezt a forgatókönyvben és a jegyzetben is rögzítse. A záróteszt
15 percét ne a várakozási időből vegyük el. Egyszerre egy modellt futtassunk.

A csomagban a tanítást verbose=0 teszi csendessé, ezért a tutor előre elmondja,
hogy várni kell a futási összefoglalóra. A paraméterek, metrikák és kimeneti
mappa a futás végén együtt szerepelnek.

## Pedagógiai cél

A hallgató a modellrészben dolgozik: értelmezi a bemenetet és kimenetet,
megváltoztatja a neuronszámot, új Dense-réteget illeszt be, beállítja a tanítást,
összehasonlítja a validációt, majd indokolja a választását. A rajzolás
és az adat-előkészítés kész infrastruktúra. A konkrét API-k mellett az
adatszerepek és a műveletek közti különbség a fontos.

A záróteszt utolsó kötelező feladatrész. Inno egy kérdés után vár a válaszra,
magyaráz, pontoz, majd továbblép. A kulcs nincs technikailag elzárva,
így ez formatív ellenőrzés. Az oktató ne kezelje felügyelt vizsgaként.


## Rövid elfogadási próba az új tutorváltozathoz

Az új agent.md és óraterv az 1.1 változathoz tartozik. Új munkaterületet és
új beszélgetést használjunk a régi utasítások keveredésének elkerülésére.
A fő ellenőrzési pontok:

- G03_01-ben a tutor ténylegesen bemutatja mindkét gradiensképletet.
- Az első spirálfutás előtt közli a választási szabályt, és bemutatja
  a címkealakok, a fit argumentumai, valamint a predict/argmax különbségét.
- Négy spirálfutásra vezet végig, a kötelező R4-ben csak a ráta változik.
- Nem nevezi meg előre a nyertes futást, és nem diktál kész választási indokot.
- A grafikonokra konkrét, külön tanítási/validációs megfigyelést kér.
- A tesztmetrikák után megvárja az ábrák értelmezését is; csak utána indul a kvíz.
- A lezárásban a válaszokkal igazolt tudást nevezi meg, és elkülöníti az előzetes
  segítséget a szokásos, válasz utáni magyarázattól.

A korábbi tesztmásolatban eszköznevek és elrontott táblázatformázás is látszott.
Az agent.md a hallgatói szövegben tiltja a belső eszköznevek narrálását, és
szabályos egyszerű formázást kér. Az automatikus eszközpanel, illetve az export
megjelenítése alkalmazásoldali kérdés; ezt a tananyag nem tudja kikapcsolni.
Ellenőrizzük élőben, hogy a táblázat és a kódblokkok a felületen is olvashatók.
