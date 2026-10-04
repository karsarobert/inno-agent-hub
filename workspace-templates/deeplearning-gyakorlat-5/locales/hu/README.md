# Deep Learning 2026 – 5. gyakorlat

**1.1 változat · Autoencoder és EKG-alapú anomáliaészlelés · magyar Innoagent-csomag · 2 × 45 perc · CPU**

Négy rövid, működő Python-példa: jelek megfigyelése, valódi autoencoder-tanítás,
rekonstrukciós hiba, majd a döntési küszöb hatása. A hallgató egyszerre egy
beállítást módosít. Minden új program előtt az agent bemutatja a célt és a fontos
kódrészleteket. A gyakorlatot tíz magyarázatos tesztkérdés zárja.
A CNN a következő gyakorlat témája; ebben a csomagban nem szerepel.

## Indítás

1. Csomagold ki a ZIP-et egy új munkamappába. Az `agent.md` és a négy `G05_...py`
   közvetlenül a megnyitott munkamappában legyen; az `adatok` almappa maradjon mellettük.
2. Az Innoagentben a megszokott módon válaszd ki a munkaterületet és a tutori
   utasítást. A csomag nem telepíti vagy konfigurálja át magát az alkalmazást.
3. Indíts új beszélgetést: **„Kezdjük az 5. Deep Learning-gyakorlatot!”**
4. A tanuló a Run gombbal futtat. A programok nem telepítenek és nem töltenek le semmit.

## Programok

| Fájl | Cél | Módosítás | Fő ábra |
|---|---|---|---|
| `kornyezet_ellenorzes.py` | Helyi adatok, CPU és ábramentés | Nincs | `ellenorzes.png` |
| `G05_01_ekg_adatok.py` | Normál és rendellenes jelalak | `minta_index`: 0 → 3 | `ekg_jelek.png` |
| `G05_02_autoencoder.py` | Tanulás és rekonstrukció | `epochok_szama`: 10 → 30 | `rekonstrukcio.png`, `tanulasi_gorbek.png`, `osszehasonlitas.png` |
| `G05_03_rekonstrukcios_hiba.py` | Jelenkénti MAE és hibák eloszlása | `minta_index`: 0 → 3 | `axis_1.png`, `rekonstrukciok.png`, `hibaeloszlas.png` |
| `G05_04_kuszob.py` | Riasztások és téves döntések | `kuszob`: 0.04 → 0.025 → 0.06 | `dontesek.png`, `hibaeloszlas.png`, `precision_recall.png` |

Csak gyors haladáskor: G02-ben 30 epocha mellett bottleneck 8 → 16.
Az alapóra nem igényel saját osztályt, új függvényt, kézi gradienst vagy üres fájlból kódírást.

## Helyi adatok és a referencia

- 512 normál tanítójel; 128 külön normál validációs jel.
- Külön 128 normál és 128 rendellenes gyakorlójel, mindegyik 140 pontból áll.
- A minimum és maximum kizárólag a tanítóadatokból származik. A többi részhalmaz
  is ezt a skálázást kapja. Nincs címke a 140 bemeneti érték között.
- G02 valóban tanít, és minden Run új modellt épít, rögzített maggal.
- G03 és G04 **mindig a mellékelt referencia-rekonstrukciókat használja**,
  nem a saját G02 legutóbbi eredményeit. A referencia egy valóban lefuttatott,
  30 epochás, nyolcértékű bottleneckkel készült modellből származik.
- A megfigyelt és küszöbhangolásra használt gyakorlóhalmaz nem érintetlen végső
  teszthalmaz. A gyakorlat végén szereplő „teszt” fogalmi kérdéssort jelent.

A címkék a forrásban 1=normál, 0=rendellenes jelentésűek. A küszöbös programban
viszont **pozitív = rendellenes**; ehhez tartozik minden TP/FP/FN/TN és precision/recall.

## Eredmények

Minden futás saját rövid, sorszámozott almappát készít a `nezet` alatt, és kiírja a helyét.
Például: `01_adatok_01`, `02_halo_01`, `02_halo_02`, `03_hiba_01`, `04_kuszob_01`.
A korábbi eredmények megmaradnak; a pontos mentési idő az eredmeny.json fájlban van. Frissítsd a Nézet mappát / fájllistát minden futás után!
A PNG-k mellett az `eredmeny.json` a beállításokat és összegző számokat is megőrzi.
G02 a saját rekonstrukcióit NPZ-ben, a görbéket CSV-ben is menti; ezek nem írják felül a referenciát.

## Új szemléltetések

Az `axis_1.png` két rövid, mesterséges hibasoron mutatja meg a jelenkénti és a
közös átlag különbségét. Az EKG-eredmények ettől elkülönülnek.
A `precision_recall.png` két darabszámsávval mutatja, hogy a precision a riasztásokból,
a recall a valódi rendellenességekből indul.

A 30 epochás G02 a jelenlegi formátumú saját 10 epochás futások közül a legutóbbi,
azonos adatú, architektúrájú, tanítási beállítású és kezdősúlyú futást választja.
Ha van ilyen, `osszehasonlitas.png` készül: két rekonstrukció azonos tengelyekkel,
alul abszolút eltérések. A képen a két futás neve is látszik. Ha nincs előzmény,
a program ezt kiírja; nem tanít rejtetten és nem mutat helyette referenciát.
A régi csomag hosszú mappanevű futásai megmaradhatnak, de ebbe az új összehasonlításba
nem kerülnek be. Az új órához új munkamappába csomagolj ki, és futtasd a 10 → 30 menetet.

## Útmutatók

- `START-HERE.md`: hallgatói kezdés és hibaelhárítás.
- `agent.md`: tutorviselkedés, egyszeri bemutatás, haladás, ismétlés elkerülése.
- `LECKE_UTASITASOK.md`: lépésenkénti óraterv és várakozási pontok.
- `PROGRAM_BEMUTATOK.md`: részletes első-futtatás előtti magyarázatok.
- `KODERTES_TESZT.md`: tíz előre elkészített kérdés.
- `fogalmak_es_kod.md`: hallgatói ismétlő lap.
- `oktatoi/`: előkészítés, kulcsok, mért futások, ellenőrzés és mintaábrák.
- `FORRASOK.md`, `adatok/adatleiras.json`, `adatok/referencia_leiras.json`: eredet és előfeldolgozás.

## Működési feltételek

A Python-programok előkészített környezetben GPU és internet nélkül futnak.
G01/G03/G04 NumPy-t és Matplotlibet használ; G02 és a teljes környezetellenőrzés
TensorFlow/Keras csomagot is igényel. A telepítés oktatói feladat, nem órai hallgatói teendő.
Az Innoagent szolgáltatás internetigénye ettől különálló.

A referenciaértékek nem kötelezően reprodukálandó hallgatói eredmények: tanításnál
más környezet kisebb eltéréseket adhat. A rögzített referencia döntési darabszámai ellenőrizhetők.
A tutorutasítások önmagukban nem tudják megszüntetni az alkalmazás esetleges technikai
kettős üzenetmegjelenítését; az oktatói ellenőrzés erre külön próbát javasol.
A megoldókulcs olvasható a csomagban; ez vezetett tanulás, nem elzárt vizsgarendszer.
Nincs házi feladat. A példák nem klinikai diagnosztikai eszközök.
