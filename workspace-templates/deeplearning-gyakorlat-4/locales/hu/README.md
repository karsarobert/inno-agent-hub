# Deep Learning 2026 – 4. gyakorlat

**Magyar nyelvű innoagent-csomag · 2 × 45 perc · CPU · 1.1 változat**

Az agent minden új példa előtt bemutatja a feladatot, a fontos kódrészleteket
és a kimenet jelentését. Ezután működő példát futtatsz, egy beállítást
módosítasz, majd a kimenetből és az
ábrából megvizsgálod a változás hatását. Nem kell üres fájlból programot írnod.
A hat fő téma: tanulási ráta, momentum, aktivációk, kis neurális hálózat,
L2-regularizáció és dropout. A gyakorlat végén tíz rögzített tesztkérdés következik.

## Kezdés

1. Csomagold ki a ZIP-et egy új munkamappába. Az `agent.md` és a `G04_...py`
   fájlok közvetlenül ebben a mappában legyenek.
2. Az Innoagentben a megszokott módon válaszd ki a munkaterületet és a hozzá
   tartozó tutori utasítást. A csomag a meglévő alkalmazáshoz készült, nem telepít alkalmazást.
3. Indíts új beszélgetést ezzel: **„Kezdjük a 4. Deep Learning-gyakorlatot!”**
4. Inno bemutatkozik, elmondja az óra célját, majd kéri a környezetellenőrző program futtatását.

**Te szerkesztesz, mentesz és a Run gombbal futtatsz.** A Run kezeli a
futtatási útvonalat; nem kell hozzá `cd`. Ha hiányzik egy Python-csomag,
kérd az oktató segítségét. A hallgatói programok semmit nem telepítenek és nem töltenek le.

## Programok

| Fájl | Mit vizsgálunk? | Legfontosabb kép |
|---|---|---|
| `kornyezet_ellenorzes.py` | Helyi Python, CPU-s számítás, ábramentés | `ellenorzes.png` |
| `G04_01_tanulasi_rata.py` | Egy súly közeledése a minimumhoz | `tanulasi_lepesek.png` |
| `G04_02_momentum.py` | Két frissítési szabály útvonala | `utvonalak.png` |
| `G04_03_aktivaciok.py` | Kimenet és lokális derivált | `aktivacio_es_derivalt.png` |
| `G04_04_kis_halozat.py` | A neuronszám és a tanítási idő hatása | `becsles.png`, `tanulasi_gorbek.png` |
| `G04_05_l2_regularizacio.py` | Súlybüntetés, loss és MAE | `loss_es_mae.png`, `becsles.png` |
| `G04_06_dropout.py` | Véletlen maszk és a két üzemmód | `dropout.png` |

A `K04_01_softmax.py` és `K04_02_batch_normalization.py` **opcionális**
kiegészítés; nem része a kötelező 90 percnek vagy a zárótesztnek.
Inicializálási feladat nincs. AdaGradot és Adamot nem kell kézzel megvalósítani;
a kis hálózat tanításához a kész Adam optimalizálót használjuk.

## Hol vannak az eredmények?

Minden futás saját, időbélyeges almappát készít a `nezet` alatt. A mappa
pontos útvonalát a program a végén kiírja. A korábbi futások megmaradnak.

**Minden futás után frissítsd a Nézet mappát / fájllistát**, és az új mappából
nyisd meg a képet. Ha régi kép maradt nyitva, nyisd meg az új futásét.
A képek nem nyílnak meg maguktól. A számadatok `ertekek.csv`, a beállítások
és összegző értékek `eredmeny.json` néven maradnak meg.

## A kis hálózat feladata

Egy mesterséges x értékből egy zajos, folytonos y értéket becslünk.
64 tanító- és 128 validációs mintát használunk, minden futásban ugyanazokat.
Az adatgenerátor: `y = sin(1.5*x) + 0.3*x + zaj`.
Ez szemléltető regresszió, nem Spotify-előrejelzés és nem osztályozás.
A pontszám helyett itt tetszőleges mértékegységű szám a cél; a MAE-t nem szorozzuk 100-zal.

A validációval kísérletezünk; a csomagban **nincs független végső tesztmérés**.
Ezért az eredményből nem állítunk végleges általánosítási teljesítményt.
A meglévő Spotify-notebook külön, összetettebb alkalmazás, nem szükséges a futtatáshoz.
A HTML elméleti tananyag sem futási függőség.

## Útmutatók

- `START-HERE.md`: rövid hallgatói indítás és hibaelhárítás.
- `agent.md`: a tutor működése és a haladás kezelése.
- `LECKE_UTASITASOK.md`: lépésenkénti óraterv.
- `PROGRAM_BEMUTATOK.md`: az agent által elmagyarázandó kódrészletek.
- `KODERTES_TESZT.md`: tíz előre megírt, egyválaszos kérdés.
- `fogalmak_es_kod.md`: rövid ismétlő lap.
- `oktatoi/`: előkészítés, megoldások, tesztkulcs és mért ellenőrzési eredmények.

Az agent a haladást a beszélgetési állapotában / az alkalmazás elérhető memóriájában
követi. Nem ír új haladási fájlt, nem nyitogatja folyamatosan a fájlfát.
A zárómondat: **„A 4. Deep Learning-gyakorlat véget ért.”** Nincs házi feladat.

## Működési feltételek

A példaprogramok előkészített környezetben helyben, internet és GPU nélkül
futnak. A neurális hálózatot tanító fájlok kifejezetten kikapcsolják a GPU használatát.
A NumPy-példákhoz NumPy és Matplotlib, a környezetellenőrzéshez és a két
hálózatos programhoz TensorFlow/Keras is kell. Az Innoagent szolgáltatás
kapcsolati igénye ettől különálló; a csomag nem teszi az agentet offline alkalmazássá.

Az oktatói megoldások a ZIP részei és olvashatók. Ez vezetett tanulás és
önellenőrzés, nem technikailag elzárt vizsgarendszer.
