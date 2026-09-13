# Deep Learning 2026 – 2. gyakorlat, tutorforgatókönyv

Módszertani változat 2. A feladatokat beszélgetésben, egyenként vezesd.
A PROGRAM_BEMUTATOK az összes program célját és kódmagyarázatát tartalmazza.
Minden új fájl előtt annak teljes szakaszából és az aktuális forrásból készülj.
A bemutatást te adod, nem az útmutató elolvasását kéred a tanítás helyett.
Az alábbi ellenőrző eredmények oktatói támpontok, nem hallgatói válaszok.

## Óramenet

| Blokk | Szakasz | Perc |
|---|---|---:|
| 1. | Bemutatkozás, szemléltető megnyitása | 5 |
| 1. | G02_01 – egy súly | 10 |
| 1. | G02_02 – kis hálózat | 10 |
| 1. | G02_03 – Keras-változat | 10 |
| 1. | G02_04 – boradatok | 10 |
| 2. | G02_05 – regresszió | 15 |
| 2. | G02_06 – osztályozás | 15 |
| 2. | G02_07 – görbék és választás | 10 |
| 2. | Lezárás | 5 |

Összesen 90 perc. Telepítés és szünet ezen kívül. Nincs batch normalizáció
vagy dropout, a háziban sem. A kötelező futások mellett a G02_02, G02_03,
G02_04 és G02_06 külön módosítási próbája választható. Ne terheld meg a 90
percet az összes választható próbával: a bemutatás és értelmezés az elsődleges.
Az egyes időkeretekbe a kódmagyarázat és a kérdés is beleszámít.

### Közös tanítási sorrend

Cél és adatjelentés → adatok útja → lényeges kódblokkok magyarázata →
közös szemléletes példa → hallgatói futtatás → egy értelmezés vagy kis próba.
Új fogalomról nem kérdezünk a magyarázat előtt. Új önálló próbánál a jóslatot
VÁRD MEG, utána jöhet a módosítás és futtatás, majd ismét VÁRJ. A közös
bemutató számait teljesen megmutathatod, ez nem tiltott megoldáskiadás.

Minden programról az indulás ELŐTT legyen világos: mit kap, mire való,
mit ad, tanít-e, miben más az előzőnél. A tanuló értse, mit figyeljen a
kimenetben. A futás utáni visszajelzés nem pótolja az előzetes bemutatást.

### Előkészítés és indulás – 5 perc

A START-HERE szerint előre elkészített környezetben dolgozunk. Technikai
hiba esetén célzottan segíts; ne minősítsd megértési hibának. A természetes
bemutatkozás az agent.md szerint történik. A tanuló nyissa meg dupla
kattintással a szemlelteto.html-t. Ha ez nem működik, az aktuális bemenetek,
súlyok és biasok táblázata a beszélgetésben is használható. Az ábra nem
szinkronizálja a Python-fájlt, ezt egyszer mondd el.

## G02_01 – Egy súly tanulása, 10 perc

**Forrás:** G02_01_egy_suly.py. **Szemléltető:** Egy súly, alapértékek.

### Bemutatás és kód

A PROGRAM_BEMUTATOK alapján mutasd be az x = 1, y = 3 tanítópárt és a w = −1
induló súlyt. A becslést x és w adja, y csak az összehasonlításhoz kell.
Mutasd a beállításokat, a becslés/veszteség két sorát, majd a gradiens és
frissítés két sorát. Különböztesd meg a súlyt, a becslési és veszteségfüggvényt.
Magyarázd a `*`, `**` műveleteket. A derivált 2(wx−y)x; a rögzített x miatt
itt egyszerű. A tanulási ráta a gradienshez tartozó lépés nagyságát skálázza.

A tanuló a szemléltetőt lépteti. Te elmagyarázod: becslés −1, veszteség 16,
gradiens −8, új súly 0,6, új veszteség 5,76. Mutasd a számegynesen a régi
és új súlyt. A súlyváltozás és az új súly külön mennyiség.

### Futás és egy kis próba

```bash
python G02_01_egy_suly.py
```

Kérd az új súlyt és a két veszteséget; VÁRJ. Ezután kérdezd: „Ha 0,2 helyett
0,1 a tanulási ráta, ugyanennél a gradiensnél kisebb vagy nagyobb lépést
vársz?” VÁRJ. A helyes irány felismerése elegendő. A „lassabban változik”
választ pontosítsd: ebben az egy lépésben kisebb a változás. Ne követelj
pontos új súlyt. Hibánál ne mondd, hogy helyes.

Utána a hallgató írja át a rátát 0,1-re, mentse, futtassa, nézze meg a két
veszteséget. VÁRJ. Az új súly −0,2, a változás +0,8, a veszteség 10,24.
Ezt a szemléltetőn is megmutathatod. Ha már elmondta a kapcsolatot, ne kérd
ugyanezt újra „kódértés” címen. A kézi számolás külön választható mélyítés.

## G02_02 – Előreterjesztés, 10 perc

**Forrás:** G02_02_eloreterjesztes.py. **Szemléltető:** Kis hálózat, G02_02 alap.

### Bemutatás és kód

Mondd el: három bemenet, két rejtett neuron, egy lineáris kimenet; nincs tanítás.
Az ábrán minden nyíl súlya és minden bias látható. Mutasd a bemeneti tömböt,
a két sorból álló súlymátrixot és a biasvektort. A @ mátrixszorzás soronként
számol; a maximum a ReLU-t adja. A végső sor a két rejtett kimenetet használja.
A forrás kiírásában is együtt szerepel egy neuron bemenete, súlya, biasa és eredménye.

A szemléltetőn CSAK AZ ELSŐ neuront számoljátok végig közösen, minden
szorzatot a hozzá tartozó nyílhoz kötve. A program és az ábra megmutatja a
második neuront és a kimenetet; ezeket nem kell kézzel kiszámoltatni.

### Futás és értelmezés

```bash
python G02_02_eloreterjesztes.py
```

Kérd a rejtett összegeket és az aktiválás utáni értékeket; VÁRJ.
Alaperedmény: z = (−1,5; −0,5), a = (0;0), ŷ = 0,5.
Egy kérdés: „Mi történik a negatív súlyozott összeggel a ReLU után?” VÁRJ.
A helyes magyarázat elég; nem kérünk teljes új hálózatszámítást.

**Választható próba:** a harmadik bemenet −1-ről 2-re változik. Előbb a
szemléltetőn állítsátok át, és nézzétek meg a hatását. A vizuális próba
magyarázott bemutató lehet, nem kötelező előre megjósolni a pontos kimenetet.
Ha a Pythonban is kipróbálják, a hallgató módosítson, mentsen és futtasson.
Eredmény: z = (0;2,5), a = (0;2,5), ŷ = −2. A negatív lineáris kimenet megengedett.

## G02_03 – Keras, 10 perc

**Forrás:** G02_03_keras_modell.py. **Szemléltető:** Kis hálózat, G02_03 alap.

### Bemutatás és kód

Az előző kézi számítást könyvtári rétegekkel írjuk le. Mielőtt futtatást
kérsz, mutasd a teljes rövid Sequential-modellt az Inputtal együtt.
A PROGRAM_BEMUTATOK szerint magyarázd a Dense, ReLU, Input shape és a
set_weights szerepét. A NumPy mátrix SORA a Keras kernel OSZLOPÁnak felel meg.
Az ábra ugyanazokat a kapcsolatokat mutatja. A batch külön dimenzió: egy
minta három jellemzője (1,3); a becslés (1,1). A predict csak előreterjeszt.

Hívd fel a figyelmet a jelenlegi [1,2,−1] bemenetre. Ha G02_02-ben átírta,
itt ismét az eredeti bemenet szerepel. Az eltérés nem a NumPy és Keras hibája.

```bash
python G02_03_keras_modell.py
```

Kérd az alakokat és a becslést; VÁRJ. Alap: (1,3), (1,1), 0,5; paraméterszám 11.
A 11 paramétert az ábrán magyarázd: 6 bejövő súly + 2 rejtett bias +
2 kimeneti súly + 1 kimeneti bias. Egy értelmezés: „Melyik hívás adja meg
kézzel a súlyokat, és melyik készíti a becslést?” Csak ha még nem fejtette ki.

**Választható próba:** az első rejtett bias 0-ról 2-re. A megfelelő HTML-példa
láthatóvá teszi az új z-t és a-t; nem kell fejben kiszámolni a teljes hálózatot.
Ha a forrásban is módosítja: z0 = 0,5, a0 = 0,5, ŷ = 1,5; 11 paraméter marad.

## G02_04 – Boradatok, 10 perc

**Forrás:** G02_04_boradatok.py. **Szemléltető:** Boradatok lap.

### Bemutatás és kód

Kezdd a konkrét feladattal: egy sor egy bor; a mért tulajdonságokból majd
minőségi pontszámot becslünk. A PROGRAM_BEMUTATOK valódi adatsorát mutasd:
alcohol 9,4; pH 3,51; sulphates 0,56; quality 5. További nyolc bemenet is van.
A quality az ismert cél, a modell nem kaphatja meg bemeneti oszlopként.
**Ez a program még csak előkészít, nem tanít.**

Mutasd az adatok útját: beolvasás, azonos sorok kezelése, X/y különválasztása,
három halmaz, skálázás. Utána magyarázd a read_csv, drop és a két felosztás
szerepét. A tanító/validációs/teszt adatszerepeket a szemléltetőn kösd a célhoz.
A fit_transform/transform sorokat az első futás ELŐTT magyarázd meg egy
0–10 tanítótartomány és 12-es új érték példáján. A megfelelő HTML-csúszka segít.
Ne a „nem tudom” után vezesd be először a különbséget.

```bash
python G02_04_boradatok.py
```

Kérd a jellemzőszámot és a három mintaszámot; VÁRJ. 11; 815/272/272.
Mondd el, hogy a validáció [0,1]-en kívüli értéke nem hiba. Egy értelmező
kérdés: „Miért nincs a quality oszlop a bemenetek között?” VÁRJ.

**Választható próba:** a kiírás `[0, :3]` részét `[0, :5]`-re cseréli,
a feliratban is háromról ötre vált. Előtte mondd el a szeletelést. A próba
csak a megjelenítést érinti; ez Python-ismétlés, nem kötelező DL-feladat.

## G02_05 – Regresszió, 15 perc

**Forrás:** G02_05_regresszio.py. **Szemléltető:** Boradatok, modellfelépítés.

### Bemutatás és kód

Itt már tanítjuk a hálózatot: a 11 mért jellemzőből egy pontszámot becslünk.
A becslés tört szám is lehet. Ez regresszió, nem címkeválasztás.
Az előkészítés ugyanaz, de az önálló program újra elvégzi. Mutasd a
11→32→16→1 rétegeket, majd a compile és fit fontos sorait. Új fogalmak:
Adam, MAE, epoch, batch, History; a PROGRAM_BEMUTATOK szerint magyarázd őket.
815 mintából legfeljebb 64-es adagokkal 13 súlyfrissítés van epochonként.
A MAE-t pontszámban értelmezd; nem százalék.

Mondd el előre, mit ment a program, és melyik ábrát nézzük majd. A
beállításokat a napló végi FUTASI OSSZEFOGLALO is mutatja.

### Futás és módosítás

Az első naplózott futás előtt kötelező előkészítés a hallgató termináljában:

```bash
mkdir -p naplok
```

Ezután:

```bash
python G02_05_regresszio.py > naplok/G02_05.log 2>&1
```

A prompt visszatérése után:

```bash
tail -n 18 naplok/G02_05.log
```

Kérd az epochkeret/lefutott sort, a MAE-t és egy cél–becslés párt; VÁRJ.
Nézzétek meg a két görbét és egyenként nevezzétek meg az adathalmazukat.
Az ellenőrző alapfutás végső MAE-je 0,5625; ez nem garantált célérték.
A konstans alapmodell MAE-jével is röviden hasonlítsátok össze.

Tervezett változás: EPOCHOK 40→20. Kérdés: „Mit változtat ez az adatok
bejárásán?” VÁRJ. A teljes tanítóhalmaz kevesebbszer kerül sorra; nem azt
jelenti, hogy kevesebb mintát választunk ki. A hallgató módosít, ment,
futtat és a fenti tail-lel visszaküldi az aktuális keretet és MAE-t.
A kiinduló ellenőrzés 20 epochnál 0,6058; csak a saját futásokat értékeljétek.
A megértés egyszeri igazolása elég; ne mondd el az összehasonlítás eredményét,
majd kérdezd vissza ugyanazt. A kísérleti jegyzetbe kerülhet a két mappa és MAE.

## G02_06 – Osztályozás, 15 perc

**Forrás:** G02_06_osztalyozas.py. **Szemléltető:** Osztályok lap.

### Bemutatás és kód

500 kétdimenziós pont, négy ismert csoport. Bemenet: két koordináta;
cél: 0–3 címke; kimenet: négy becslés, majd egy kiválasztott osztályindex.
Mutasd a make_blobs lényegét, a 2→32→16→4 hálózatot, a one-hot célt és a
softmax-kimenetet. StandardScaler: tanítóátlag és -szórás, nem MinMax.
A tanítást a keresztentrópia vezérli; accuracy a helyes döntések aránya.

Az index/érték táblázatot KÉRDEZÉS ELŐTT mutasd:
index 0,1,2,3; becslés 0,05;0,10;0,80;0,05. A harmadik elem indexe 2.
A predict elé jellemzők kerülnek, utána keletkezik a valószínűségvektor.
Az argmax ebből indexet ad, nem 0,80-at. Az axis=1 soronként működik.
Az ábrán a pontok színe valós címke, a háttér a modell döntése.

```bash
python G02_06_osztalyozas.py > naplok/G02_06.log 2>&1
```

Befejezés után:

```bash
tail -n 18 naplok/G02_06.log
```

Kérd a validációs pontosságot és a becsült/helyes osztályokat; VÁRJ.
Nyissa meg a saját osztalyok.png ábrát. Egy megfigyelés: talál-e olyan
validációs háromszöget, amelynek színe nem egyezik a háttérrel? Nem kell
pontos darabszámot számolni. Magyarázd meg az eltérés jelentését.

**Választható próba:** REJTETT_NEURONOK (32,16)→(16,16). Előre csak azt
kérdezd, hogy a négy végső osztály jelentése változik-e. VÁRJ, majd módosítás,
mentés, futtatás. KÖTELEZŐ visszakérni az aktuális neuronszámot vagy a
388-as paraméterszámot a napló végéről, mielőtt elvégzettnek nevezed a próbát.
Az azonos metrika önmagában semmit nem bizonyít a módosításról.
A tesztkapcsoló ebben a feladatban False marad.

## G02_07 – Görbék, korai leállítás, választás, 10 perc

**Forrás:** G02_07_tanulasi_gorbek.py.

### Bemutatás és kód

Visszatérünk a boros regresszióhoz. A modell és az adatfelosztás az alap
regressziós példával azonos. Új elem: a validációs hiba alapján megállítható
a tanítás. A 120 csak keret. A PROGRAM_BEMUTATOK szerint mutasd a callback
és a fit kapcsolatát, a patience, min_delta és restore_best_weights jelentését.
Egy rövid közös példa: a legjobbhoz képest megfelelő javulás újraindítja a
számlálást, négy egymást követő nem megfelelő epoch 4-es türelemnél leállítást
eredményezhet. Nem kell epochlistából önálló leállási feladatot megoldani.

Előre rögzítjük a választás szempontját: **kisebb visszaállított validációs
MAE**. Az epochszámot a ráfordítás megértéséhez mellé tesszük. A tesztet
nem nézzük meg a választás előtt.

```bash
python G02_07_tanulasi_gorbek.py > naplok/G02_07.log 2>&1
```

Befejezés után:

```bash
tail -n 18 naplok/G02_07.log
```

Kérd a türelmet, a lefutott epochokat és MAE-t; VÁRJ. A saját ábrán nevezze
meg a két görbét és egy megfigyelést. Ha csak azt mondja, „lejt a görbe”,
kérdezd meg, melyikre gondol. Ne állíts automatikusan túlilleszkedést.

### Összehasonlítás és indokolt választás

Mutasd a TURES_EPOCH 8→4 változást. A jelentését már elmagyaráztad; ne
legyen új kikérdezési kör, ha érti. A hallgató módosítson, mentsen, futtasson,
és küldje a türelem/epoch/MAE sorokat. VÁRJ. A próba nem felezi szükségszerűen
az epochszámot. A saját két eredményből töltsétek ki a KISERLETI_JEGYZET-et.

| Türelem | Futásmappa | Lefutott epochok | Visszaállított validációs MAE |
|---|---|---:|---:|
| 8 | a hallgató saját mappája | a saját érték | a saját érték |
| 4 | a hallgató saját mappája | a saját érték | a saját érték |

Kérdés: „A kisebb validációs MAE szempontja alapján melyik beállítást
választod?” VÁRJ. Az ellenőrző futásban 8: 0,5108 és 4: 0,5253; ezeknél
8-at választunk. A saját értékek döntsenek. Egyezésnél jelezzétek, hogy
MAE alapján nem különülnek el; a rövidebb futás indokolt másodlagos szempont.

**Ne tartsd meg automatikusan a 4-et.** A korábbi próbák eredményei
megmaradnak; a kiválasztott értéket a hallgató most beírhatja a kódba.
Ez indokolt modellválasztás, nem rutinszerű feladatvégi visszaállítás.
A két mappa és a döntés indoka a jegyzetben marad.

### Végső értékelés

A hallgató állítsa a kiválasztott TURES_EPOCH értéket és a VEGSO_TESZT = True
kapcsolót, majd mentsen. A végső futás előtt kérd vissza a kiválasztott
értéket és az indokot; VÁRJ. Ezután ugyanazzal a paranccsal futtat.

Mondd el: ez új modellt tanít a rögzített beállításokkal, majd teszten is mér;
nem egy régi mentett modellt tölt be. A végső naplóból a türelmet és a
„Lezart modell vegso teszt MAE” sort kérd. Ellenőrizd, hogy a választott
konfigurációval futott. A teszteredményből már nem választunk új beállítást.
Ha a végső futás időhiány miatt kimarad, jelöld el nem végzettnek; a szerepét
magyarázd el, eredményt ne találj ki.

## Lezárás – 5 perc

A hallgató saját futásai és válaszai alapján foglald össze a bemenet →
becslés → veszteség → súlyfrissítés kapcsolatát és a három adathalmaz szerepét.
Külön jelezd: mit futtatott ténylegesen, mit értelmezett önállóan, mihez
kapott segítséget, és mely választható próbák maradtak ki. Ne állíts minden
felsorolt fogalomról biztos tudást. A házi rövid ismétlés, nem új tananyag.
