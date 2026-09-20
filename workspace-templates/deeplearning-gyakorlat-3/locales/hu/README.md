# Deep Learning 2026 – 3. gyakorlat

**Javított 1.1 változat.** Magyar nyelvű Innoagent-csomag, **2 × 45 percre**. Téma: gradiensmódszer,
neuron és neurális hálózat felépítése, tanítási beállítások, spirálosztályozás,
validáció és végső teszt. A végén 10 feleletválasztós kódértési kérdés.

## Kezdés

1. Csomagold ki a ZIP-et egy új munkamappába. Az `agent.md` és a
   `G03_...py` fájlok közvetlenül a megnyitott munkamappában legyenek.
2. Az Innoagentben a korábban használt módon válaszd ki ezt a munkaterületet
   és a hozzá tartozó tutori utasítást. Indíts új beszélgetést.
3. Írd be: **„Kezdjük a 3. Deep Learning-gyakorlatot!”**
4. Inno bemutatkozik, ismerteti az óra célját, és végigvezet a feladatokon.

A ZIP a tananyagot és a munkaterületi utasításokat tartalmazza; a meglévő
Innoagent alkalmazást használja. Nem telepít vagy konfigurál önállóan alkalmazást.

**A programokat mentés után a Run gombbal futtasd.** A Run kezeli az útvonalat,
nem kell miatta `cd` parancsot kiadnod. A Python-fájlokat te szerkeszted;
Inno elmagyarázza a kódot és segít az eredmény értelmezésében.

**Ha Python-csomag hiányzik, kérd az oktató segítségét!** Ne kezdj önálló
telepítésbe. A csomag helyben működik, Colabot és Jupytert nem használunk.
Előkészített környezetben a programok futásához nincs szükség internetre vagy GPU-ra.

## Feladatok

| Fájl | Feladat |
|---|---|
| `kornyezet_ellenorzes.py` | Ellenőrizd a helyi környezetet; nem telepít semmit. |
| `G03_01_gradiens.py` | Kövesd egy súly és egy bias tanulását szintetikus adatokon. |
| `G03_02_spiral_alap.py` | Vizsgáld a háromosztályos, rejtett réteg nélküli alapmodellt. |
| `G03_03_spiral_halo.py` | Taníts 16 neuronos hálózatot, építs két 50-es réteget, majd külön futásban csökkentsd a rátát. |
| `G03_04_vegso_ertekeles.py` | A validáció alapján kiválasztott mentett modellt értékeld a teszten. |
| `KODERTES_TESZT.md` | Válaszolj Inno 10, egyenként feltett feleletválasztós kérdésére. |

A beállítások közül a tanulási ráta, az epoch és a batch jelentését is
feldolgozzuk. A **tanulásiráta-kísérlet kötelező**: az 50–50 hálózaton 0.01-ről
0.001-re változtatod a rátát, miközben minden más azonos marad.
Az adatkezelés és az összes értékelési ábra kódja kész a `segedletek.py` fájlban.
Az órai munka a modell építésére, beállítására és megértésére koncentrál.

Négy spirálfutást hasonlítasz össze: alapmodell, 16 rejtett neuron,
50–50 rejtett neuron 0.01 rátával, majd ugyanez 0.001 rátával. A választás
szabályát előre megismered: kisebb validációs loss; pontos egyezésnél
kevesebb paraméter. **A modellt te választod ki és te indoklod a döntésedet.**
A végső teszt ábráit is értelmezzük, mielőtt a tíz kérdés elkezdődik.

## Az új ábrák megnyitása

**Minden futás után frissítsd a Nézet mappát / fájllistát**, hogy az új
fájlok megjelenjenek! A kimenetben megadott, időbélyeges futási mappát
keresd az `eredmenyek` alatt. Innen nyisd meg például az új `loss.png` képet.
Ha korábbi kép maradt megnyitva, zárd be, és az új mappából nyisd meg a megfelelőt.

| Kimenet | Tartalom |
|---|---|
| `loss.png` | Tanítási és validációs veszteség |
| `accuracy.png` | Tanítási és validációs pontosság a spirálmodelleknél |
| `regresszio.png` | Szintetikus adatpontok és tanult egyenes az első feladatban |
| `dontesi_tartomanyok.png` | Valódi és becsült spirálcímkék, a modell döntési hátterével |
| `konfuzios_matrix.png` | Helyes és téves osztályozások osztályonként |
| `beallitasok.json` | A futás beállításai és validációs eredménye |
| `modell.keras` | A spirálmodell rétegei és megtanult paraméterei |
| `tanulasi_gorbek.csv` | A tanítási görbék számszerű adatai |

A végső teszt ábrái a kiválasztott futás `vegso_teszt` almappájában vannak.
Ott nincs új loss-görbe: a program a meglévő hálózatot méri, nem tanítja újra.
A régi futások megmaradnak. Az ábrák nem nyílnak meg automatikusan.

## Útmutatók

- `START-HERE.md`: rövid hallgatói indítás és hibaelhárítás.
- `agent.md`: a tutor bemutatkozása, működése, tesztvezetése és lezárása.
- `LECKE_UTASITASOK.md`: részletes óraterv és hallgatói lépések.
- `PROGRAM_BEMUTATOK.md`: programáttekintések és kódmagyarázatok.
- `KISERLETI_JEGYZET.md`: saját mérések és a modellválasztás indoka.
- `fogalmak_es_kod.md`: rövid fogalmi támasz.
- `OKTATOI_MEGOLDOKULCS.md`: tesztmegoldások indoklással, oktatói használatra.
- `OKTATOI_ELOKESZITES.md`, `requirements.txt`: környezet az oktató számára.
- `VALTOZASOK.md`: az 1.1 változat javításai és a frissítés menete.
- `FORRASOK.md`, `ELLENORZES.md`: eredet, szakmai pontosítások és ellenőrzések.

A csomagban szereplő megoldókulcs nincs technikailag elrejtve; ez tanulási
önellenőrzés, nem zárt vizsgarendszer. A tutor csak a válasz után adja meg a megoldást.
Az elméleti HTML és a forrásnotebookok külön anyagok, a futtatáshoz nem szükségesek.
A gyakorlat végén Inno kimondja: **„A 3. Deep Learning-gyakorlat véget ért.”**
