# Rövid ismétlő feladat – Deep Learning 2026, 2. gyakorlat

A már elkészült kódokra és az elmentett eredményeidre építs. Nem kell új
programot írnod, új témát feldolgoznod vagy a teszthalmaz alapján modellt hangolnod.
Irányadó idő: 15–20 perc. Ha egy órai rész kimaradt, ezt jelezd a válaszban.

## 1. Egy súly, saját szavakkal

Nyisd meg a saját `G02_01_egy_suly.py` fájlodat. Ne állítsd vissza a beállításokat.
Négy rövid mondatban írd le a `bemenet`, `celertek`, `suly`, `becsles` szerepét.
A szemléltetőben állítsd be a saját számaidat, és figyeld meg egy lépés
hatását. Egy futtatással vesd össze az eredményt. Írd le, mi változott és
mi maradt ugyanaz. A pontos új súly kézi kiszámítása választható mélyítés.

## 2. Egy kódrészlet magyarázata

Válassz az alábbiak közül egyet, és 3–5 mondatban magyarázd el:

- A saját G02_02 programod `np.maximum` sora: mit kap és mit ad vissza?
- A G02_03 programod `set_weights` és `predict` hívása: melyik mire szolgál?
- A G02_06 programod `argmax(axis=1)` sora: hogyan változik az adat jelentése?

A puszta sorbemásolás helyett az adat és az eredmény kapcsolatát írd le.
Új tanítást ehhez nem kell indítanod.

## 3. Egy valódi futás értelmezése

Válassz egy már elkészült regressziós eredménymappát. Add meg:

- a mappa nevét, a neuronszámokat és a ténylegesen lefutott epochok számát;
- a validációs MAE-t és annak jelentését;
- egy megfigyelést a `tanulasi_gorbek.png` két görbéjéről;
- használtál-e végső tesztet, és az mikor történt a modellválasztáshoz képest.

Ne találj ki túlilleszkedést, ha a görbén nincs erre utaló tartós mintázat.
Ha a saját futásodban a callback nem állt le az epochkeret előtt, ezt az
eredményt írd le. A pontos megfigyelés fontosabb egy elvárt történetnél.

## Beadás

Egy rövid szöveg vagy Markdown-fájl és a választott futás görbéje elegendő.
Nem kell teljes napló, virtuális környezet vagy minden eredménymappa.
Ha már lefutott a végső teszt, az eredménye alapján ne módosítsd a beállításokat. A további munka itt a meglévő eredmények magyarázata.

A modellválasztást a `KISERLETI_JEGYZET.md` segíti: a validáció alapján
hozott döntést indokold, ne pusztán a legutolsó kipróbált értéket írd le.
