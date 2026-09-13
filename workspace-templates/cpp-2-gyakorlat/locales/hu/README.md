# C++ – 2. gyakorlat: változók, típusok és számábrázolás

A csomag a javított **CPP_02.html** elméleti anyag gyakorlati folytatása.
Az elméleti HTML külön fájl; a gyakorlat futtatásához nem szükséges.
Időkeret: **3 × 45 perc gyakorlat**, a szüneteken felül.

Kész, rövid programokból indulunk. A tutor magyarázata után kis változtatásokat
végzel, megfigyeled a működést, és elmondod az eredmény okát. Az utolsó feladatban
már egy számítási sort is önállóan javíthatsz. Nem kell programot írnod üres fájlból.

## Munkamegosztás a gyakorlaton

**A kódot te szerkeszted és mented, a fordítást és futtatást is te végzed.**
Ez az első bemutatóprogramra, minden módosításra és a hibakeresésre is vonatkozik. Inno elmagyarázza a feladatot, szükség
esetén megmutatja a cserélendő sort és a terminálparancsokat, majd megvárja az
eredményedet. A helyes jóslat után következik a saját próbád.

Elegendő a kért kimeneti sort vagy a megfigyelésedet elküldened. Fordítási
hiba esetén ne indíts régi programot: az első lényeges hibaüzenetet küldd el.
Inno segít értelmezni és javítani a hibát, de a javítást is te írod be.

A feladatok végén a módosított kód megmarad: nem kell az eredeti állapotot
visszaállítanod. A következő próba az előző eredményére épül. Csak a szándékos
hibapróba hibáját javítod ki, hogy a programmal tovább lehessen dolgozni.

Ha a korábbi csomagot már használod, az `agent.md` és a `LECKE_UTASITASOK.md`
fájlt cseréld le a munkamappában, majd indíts új tutorbeszélgetést, hogy az új
utasítások érvényesüljenek. A `.cpp` fájlok ehhez a pontosításhoz nem változtak;
a saját, már módosított forrásaidat ne írd felül a csomag kiinduló példáival.
Külön letöltésnél az útmutatók neve pontosan a fenti legyen; az esetleges
`(1)` utótagot távolítsd el a fájlnévből.

## A kód megértésének ellenőrzése

A bitmintás feladat kivételével minden alapfeladatban egy rövid kódrészlet
működését is elmagyarázod a saját szavaiddal. Inno a sikeres próba után
1–3 lényeges sort emel ki: azt beszélitek meg, mit végeznek és mit jelent
az eredmény. Nem kell tankönyvi megfogalmazás vagy minden sor részletes elemzése.
Ha ezt már elmagyaráztad, nem kell megismételned. Elakadáskor segítséget és
rövid gondolati példát kapsz; ehhez nem kell újra szerkeszteni vagy fordítani.

Ezek a beszélgetések a meglévő időkeretbe tartoznak, és az ismétlő kérdéseket
váltják fel. A helyes kimenet és a kód megértése külön visszajelzést kap.
Eltérő számítási eredménynél előbb az aktuális adatokat és kódsorokat tisztázzátok,
akkor is, ha a végső igaz/hamis eredmény a vártnak megfelel.

## Kezdés Innoagentben

1. Csomagold ki a ZIP tartalmát egy új, a második gyakorlathoz tartozó mappába.
   A fájlok közvetlenül ennek a munkaterületnek a gyökerébe kerüljenek.
   Ne másold rá az első gyakorlat mappájára: mindkét csomagban van `agent.md`.
2. Nyisd meg ezt a mappát az Innoagent munkaterületeként, a korábbi beállításoddal.
3. Írd a beszélgetésbe: **„Kezdjük a 2. C++-gyakorlatot!”**
4. A `.cpp` fájlokat szövegszerkesztőben módosítsd, a fordítási és futtatási
   parancsokat pedig az adott mappában nyitott Linux-terminálban add ki.

A csomag a korábbi gyakorlat fájlszerkezetét követi. A munkaterülethez kapcsolt
utasítások betöltése az Innoagent beállításától függ; a ZIP önmagában nem telepít
vagy konfigurál alkalmazást. Az `agent.md` és a `LECKE_UTASITASOK.md` a tutor
irányítását szolgálja; a gyakorláshoz a kijelölt forrásfájlt nyisd meg.

## Feladatsorrend

| Fájl | Téma | Irányadó idő |
|---|---|---:|
| `G02_01_tipusok.cpp` | Tárméret és típushatárok | 15 perc |
| `G02_02_inicializalas.cpp` | Kezdőérték, értékadás, konstans | 10 perc |
| `G02_03_bitmintak.cpp` | Nyolc bit kétféle értelmezése | 15 perc |
| `G02_04_osztas.cpp` | Osztás és a konverzió helye | 15 perc |
| `G02_05_tartomanyok.cpp` | Előjel nélküli körbefordulás és nagy szorzás | 15 perc |
| `G02_06_pontossag.cpp` | Lebegőpontos közelítés és értékes számjegyek | 15 perc |
| `G02_07_formazas.cpp` | Tárolás és kimenetformázás | 10 perc |
| `G02_08_tures.cpp` | Összehasonlítás abszolút tűréssel | 10 perc |
| `G02_09_pontszamok.cpp` | Összekapcsoló javítási feladat | 15 perc |

A ráhangolásra 5, a lezárásra 10 perc jut: összesen 135 perc.
Az időkeret rugalmas; a további próbák és a kiegészítők nem kötelezők.

A `G02_K01_tulcsordulas.cpp` külön, választható bemutató. Kiinduló állapotában
helyes program. Csak tutorral, az előírt futásidejű ellenőrzéssel alakítjuk át
hibás változatra. Ez nem része a 135 perces alapútvonalnak.

## Fordítás és futtatás

C++20-at támogató GCC szükséges. Ellenőrzés: `g++ --version`.
Az első feladat fordítása:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_01_tipusok.cpp -o G02_01
```

Sikeres fordítás után:

```bash
./G02_01
```

A következő feladatok konkrét parancsait a tutor adja. A `-o` utáni név
az elkészülő program neve; ezt kell futtatni. Módosítás után mindig ments és
fordíts újra. Sikertelen fordítás után ne indíts el régi programot az új kód
ellenőrzéseként. Az alapfeladatokban nincs begépelendő futásidejű bemenet:
a vizsgált adatokat a forrásban módosítjuk.

## Clean code a kezdő gyakorlatban

- Beszédes, ékezet nélküli magyar azonosítók, következetes `snake_case` írással.
- A mértékegység szerepel a névben, ha az értelmezéshez fontos, például
  `mert_hossz_meter`. A név elsősorban a jelentést, nem a típust írja le.
- A beállításokat és feladatszabályokat megnevezett állandók fejezik ki.
  `constexpr` a fordításkor ismert beállításhoz, `const` a később nem módosított
  számítási eredményhez. A megfigyelésben módosítandó változók változtathatók.
- Négy szóközös behúzás, egyértelmű blokkok, következetes `std::` előtag.
- A megjegyzés indokol vagy fontos korlátot jelez, nem mondja vissza a kódot,
  és nem árulja el az önálló próbák eredményét.
- Egy fájl egy tanulási témát szolgál. A bitmodell ismétlődő része tudatosan
  egyszerű: a tömböket és függvényeket még nem tanultuk. Az elnevezések és a
  közös részszámítás kiemelése így is javítja az olvashatóságot.
- Az `elso_atlag` jellegű név az összehasonlított változatot azonosítja;
  a zárófeladat már a jelentést hordozó `atlag_pontszam` nevet használja.

A 9. feladat egy világosan megjelölt **logikai hibát** tartalmaz. A rendezett,
jól elnevezett kód is lehet hibás; ezt a számítás ellenőrzésével javítjuk.
A szándékos hibapróbák után kizárólag a hibát javítod ki. A többi kipróbált
módosítás megmarad; nincs feladatvégi visszaállítás vagy külön takarítási kör.

## Környezeti különbségek

A típusméreteket a saját gépen kérdezzük le. A részletes lebegőpontos példák
szokásos IEEE 754 binary32 (`float`) és binary64 (`double`) környezetre,
a szokásos kerekítésre vonatkoznak. Az eltérés nem automatikusan hallgatói hiba.
A számokban nincs aposztrófos tagolás. A forráskód tizedesjele pont.
A magyarázatok magyarul, a terminálüzenetek és azonosítók ékezet nélkül szerepelnek.
