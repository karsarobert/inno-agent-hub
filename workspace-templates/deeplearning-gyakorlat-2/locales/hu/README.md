# Deep Learning 2026

## 2. gyakorlat – A súlyoktól a tanítható hálózatokig

**Módszertani változat: 2 – programbemutatás és szemléltetés.**

**Időkeret: 2 × 45 perc.** Magyar nyelvű, Innoagentben használható
gyakorlati munkaterület, helyben futtatható kész Python-programokkal.
A felépítés a második óra HTML-anyagára és a PTE_DL2 notebookra épül.
A tanulási módszer a C++-gyakorlat magyarázó tutoros menetét követi.

Kész programokat olvasol, futtatsz és kis lépésekben módosítasz. Inno minden
új fájl előtt bemutatja a program célját, az adatok jelentését és útját,
majd elmagyarázza a fontos kódrészleteket. Ezután megvizsgálod
a működést, kipróbálsz egy módosítást, és saját szavaiddal értelmezed az eredményt.
Nem kell üres fájlból programot írnod. A kész kódokban nincs kitöltendő rész.

## Kezdés

1. Csomagold ki a ZIP-et egy új mappába. Az első DL- vagy a C++-gyakorlat
   munkamappáját hagyd meg külön.
2. A `DL_02_Innoagent` mappát nyisd meg munkaterületként: ebben közvetlenül
   megtalálható az `agent.md` és a hét `G02_...py` fájl.
3. Az óra előtt készítsd elő a helyi Python-környezetet a `START-HERE.md` alapján.
4. Nyisd meg a `szemlelteto.html` fájlt dupla kattintással a böngészőben.
   Internet nélkül mutatja az egy súly és a kis hálózat számítását, a
   boradatok szerepét és az osztályindexek jelentését.
5. Indíts új tutorbeszélgetést, és írd: **„Kezdjük a 2. Deep Learning-gyakorlatot!”**

A csomag a korábban használt Innoagent-beállításodhoz készült. A ZIP önmagában
nem telepít vagy konfigurál Innoagentet; a munkaterületi utasítások betöltése
az alkalmazás beállításától függ. A korábbi beszélgetés utasításainak
keveredését külön munkamappával és új beszélgetéssel kerülheted el.

## Munkamegosztás

**A kódot te szerkeszted és mented, a programot te futtatod a terminálban.**
Ez az első közös bemutatóra és a hibajavításra is igaz. Inno megadja a szükséges
kódrészletet és parancsot, megvárja az eredményedet, majd segít értelmezni.

Egy-egy fontos részletet saját szavaiddal is elmagyarázol. Nem tankönyvi
megfogalmazást várunk: az számít, hogy értsd, milyen adatból milyen eredmény
keletkezik. A sikeres futtatás és a megértés két külön dolog.

A módosított, működő programok megmaradnak; a feladat végén nem kell
visszaállítanod a kiinduló állapotot. A végső modellválasztásnál viszont
indokoltan visszaírhatod egy korábbi, jobb validációs eredményű próba
beállítását; az eredménymappák megmaradnak. A külön programok külön indulnak,
így másik fájlban elvégzett módosítás nem változtatja meg őket automatikusan.

## A hét feladat

| Fájl | Mit vizsgálunk? | Idő |
|---|---|---:|
| `G02_01_egy_suly.py` | Ismert cél, becslés, veszteség és egy gradienslépés | 10 perc |
| `G02_02_eloreterjesztes.py` | Egy 3 → 2 → 1 hálózat számítása NumPy-jal | 10 perc |
| `G02_03_keras_modell.py` | Ugyanaz a kis hálózat Kerasban, rögzített súlyokkal | 10 perc |
| `G02_04_boradatok.py` | Jellemzők, célváltozó, felosztás és skálázás | 10 perc |
| `G02_05_regresszio.py` | Minőségi pontszám becslése tanítható modellel | 15 perc |
| `G02_06_osztalyozas.py` | Négy pontcsoport, one-hot cél és softmax-kimenet | 15 perc |
| `G02_07_tanulasi_gorbek.py` | Tanulási görbék, korai leállítás és végső teszt | 10 perc |

A teljes hálózat kézi újraszámítása nem kötelező. A G02_02, G02_03, G02_04
és G02_06 külön módosítási próbája választható; a közös bemutatás és az
alapfuttatás ezeknél is az óra része.

Ráhangolás és lezárás: 5–5 perc. A telepítés és a szünet nem része a 90 percnek.
Dropoutot és batch normalizációt ezen az alkalmon nem dolgozunk fel.

## Futtatás és eredmények

Az aktivált virtuális környezetben, a munkamappa termináljában:

```bash
python G02_01_egy_suly.py
```

A későbbi programok parancsát Inno adja. Python esetén mentés után közvetlenül
futtatsz; nincs külön C++-szerű fordítási parancs. A programok nem kérnek futás
közbeni billentyűzetes adatbevitelt: a vizsgált beállításokat a forrásban módosítod.

A három tanítóprogram sok sort írhat. A naplózás előkészítése:

```bash
mkdir -p naplok
```

Példa tanításra és a befejezés utáni kivonatra:

```bash
python G02_05_regresszio.py > naplok/G02_05.log 2>&1
```

Amikor visszakaptad a terminálpromptot:

```bash
tail -n 18 naplok/G02_05.log
```

Inno csak a kérdéshez kapcsolódó sorokat vagy megfigyelést kéri. Nem kell
az összes epochot bemásolnod. Hiba esetén a kivétel nevét és az érintett sort küldd el.

Minden tanítófutás új mappát készít az `eredmenyek/` alatt. Az elérési út a
kimenet végén látható. A mappa tartalmazza a tanulási görbék PNG-képét és
CSV-adatait, a beállításokat és a futtatott program másolatát. A regressziós
programok egyedi becsléseket is mentenek, az osztályozó pedig `osztalyok.png`
néven a döntési tartományokat. A képeket a fájlkezelőből nyisd meg.
Nem jelenik meg automatikusan grafikus ablak. A korábbi futási mappák megmaradnak.

## Kapcsolódó anyagok

| Fájl | Kinek és mire szolgál? |
|---|---|
| `szemlelteto.html` | Offline, léptethető ábrák és módosítható paraméterek |
| `PROGRAM_BEMUTATOK.md` | A hét program célja, adatfolyamata és részletes kódmagyarázata |
| `KISERLETI_JEGYZET.md` | Saját futások összevetése és a végső választás indoklása |
| `VALTOZASOK.md` | A tesztbeszélgetés alapján elvégzett javítások |
| `START-HERE.md` | Hallgatói és oktatói helyi környezetbeállítás |
| `fogalmak_es_kod.md` | Képletek és Python-kódrészletek összekapcsolása |
| `hazifeladat.md` | Rövid, kész kódokra és meglévő eredményekre épülő ismétlés |
| `agent.md` | A tutor szerepe, munkamegosztása és kommunikációs szabályai |
| `LECKE_UTASITASOK.md` | Részletes oktatói forgatókönyv és ellenőrző támpontok |
| `FORRASOK.md` | A felhasznált oktatási és technikai források |
| `adatok/FORRAS.md` | A mellékelt CSV eredete és licence |
| `ELLENORZES.md` | Az elkészítéskor végzett próbafuttatások oktatói feljegyzése |

Az elméleti `DL_02.html` és az eredeti notebook külön tananyag; a programok
futtatásához nincs szükség a fájljaikra. A notebook logikáját a kész `.py`
programok tartalmazzák. A telepítés után a csomag példái internet nélkül futnak.

## Mit hasonlítunk össze?

A kísérletekben a validációs eredményt vizsgáljuk. A teszthalmazt a végső,
rögzített beállítású értékeléshez tartjuk fenn. A `VEGSO_TESZT` kapcsolót
az alapórán a hetedik feladat lezárásakor használjuk; ezután már nem hangolunk
a teszteredmény alapján. Az első hat feladatban a tesztből nem választunk modellt.

A fix seed segít az ismételhetőségben, de különböző gépeken vagy verziókkal
kisebb eltérések lehetnek. A pontos elméleti számpéldákat és az esetenként
változó tanítási mutatókat ezért külön kezeljük.

## Áttérés az előző csomagról

Az új ZIP-et külön mappába csomagold ki; ne írd felül vele a saját kísérleti
forrásaidat és eredményeidet. Az Innoagentben az új mappához tartozó agent.md
legyen az aktív utasítás. Indíts új beszélgetést. Ha a régi presetet használod,
annak fájljai nem frissülnek pusztán az új ZIP letöltésétől. Az alkalmazás
munkaterület-választását a nálatok használt felületen végezd el.

A szemléltető nem olvassa a Python-fájlokat. Az ábra példaválasztóját vagy
számmezőit az aktuális kódhoz kell igazítani. A teljes kézi számolás helyett
az adat útját és a változás hatását figyeljük.
