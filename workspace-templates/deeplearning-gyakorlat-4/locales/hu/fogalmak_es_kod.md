# Rövid fogalmi támasz

| Fogalom | Jelentés a példákban |
|---|---|
| Gradiens | A veszteség érzékenysége az aktuális paraméterre; a frissítéshez használjuk. |
| Tanulási ráta | A gradiensből képzett lépés nagyságát szabályozó beállítás. |
| Momentum | A korábbi frissítések hatásának megőrzése egy sebességváltozóban. |
| Aktiváció | A neuron súlyozott összegét átalakító függvény. |
| Lokális derivált | Megmutatja, hogyan változik az aktiváció kimenete a bemenet kis változására. |
| ReLU | `max(0, z)`; pozitív oldalon továbbad, negatív oldalon nulláz. |
| Leaky ReLU | Negatív oldalon is van rögzített, általában kicsi meredekség. |
| Epocha | A teljes tanítóhalmaz egyszeri bejárása. |
| Batch | Az egy súlyfrissítéshez közösen felhasznált minták csoportja. |
| MAE | A cél és becslés abszolút eltéréseinek átlaga. Nem osztályozási hibaarány. |
| Validáció | Mérés a tanítás beállításainak vizsgálatához; nem közvetlen súlyfrissítés. |
| L2-büntetés | λ szorozva a kijelölt súlyok négyzetösszegével. |
| Dropout | Tanítási módban véletlen aktivációnullázás, a megmaradó értékek skálázásával. |

**Az összehasonlítás szabálya:** egy vizsgált tényező változzon; ugyanazt a feladatot,
adatfelosztást és megfelelő mérőszámot használd. A gyakorlatban a modellméretet,
az epochaszámot és az L2-erősséget külön kísérletekben változtatjuk.

**A tanítási hiba nem elég:** új mintákon más lehet a teljesítmény. A validációs
eredmények alapján végzett ismételt hangolás után független végső teszt kellene
egy lezárt modell minősítéséhez. Ebben a rövid szemléltetésben ilyen teszt nincs.

**Értelmezd a kimenetet:** melyik beállítást módosítottad, melyik mutató változott,
mekkora volt a különbség, és a képen mi támasztja alá a következtetésedet?
