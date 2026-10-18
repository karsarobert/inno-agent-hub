# 7. gyakorlat · részletes tutori forgatókönyv

Ez nem helyi futtatási tananyag: az agent beszélget, a hallgató Colabban szerkeszt és futtat.
Az agent.md szabályai kötelezőek. Az egyetlen aktív cella ritmusát a kész cellákra is alkalmazni kell.
A nagy lépésszám miatt tilos a teljes óratervet egyetlen hallgatói üzenetben felsorolni.

## Órai ütemezés

Kiinduló tervezés: két 45 perces blokk. Az elsőben indulás+regresszió+MNIST előkészítés,
a másodikban MNIST értékelés+anomáliák+zárás. Ez célzott, tutorral segített feldolgozás;
az előzetes tudás, párbeszéd és futtatókörnyezet miatt hosszabb is lehet. Időhiánynál
ne hagyj ki észrevétlenül értelmezést, és ne állíts teljes teljesítést. A következő órára
megőrzött folytatási állapot pontosabb, mint egy elkapkodott, bizonyíték nélküli lezárás.

## Minden új blokk bevezetése

- R01 előtt: történeti körzetadatok, 13 jellemző, egy valós cél, ezer korabeli USD; regresszió.
- M01 előtt: 28×28 képek, 10 számjegy, vektorrá alakítás, one-hot, softmax; osztályozás.
- A01 előtt: 5 mesterséges tranzakciós jellemző, normál 0/anomália 1; normál adatok rekonstrukciója,
  majd külön küszöb és végső vegyes teszt. Nem közvetlen 0/1 hálózatot tanítunk.

## Összefoglaló térkép

| Cella | Munkamód | Cél |
|---|---|---|
| E01 | kész | Környezet és munkamód |
| R01 | kész | Lakásadatok betöltése |
| R02 | kész | Az adatok ellenőrzése |
| R03 | kész | Tanító-, validációs és teszthalmaz |
| R04 | önálló | Skálázás adatszivárgás nélkül |
| R05 | önálló | Regressziós modell |
| R06 | önálló | Veszteség és korai leállítás |
| R07 | kész | Regresszió tanítása |
| R08 | kész | Tanulási görbék értelmezése |
| R09 | kész | Végső teszt és alapbecslés |
| R10 | önálló | Új adat és ugyanaz a skálázó |
| M01 | kész | MNIST és egy gyorsabb tanító részhalmaz |
| M02 | kész | Egy kép és a valódi címkéje |
| M03 | önálló | Normalizálás és kilapítás |
| M04 | önálló | One-hot célvektorok |
| M05 | önálló | Számjegyosztályozó hálózat |
| M06 | önálló | Osztályozási veszteség |
| M07 | kész | Az osztályozó tanítása |
| M08 | kész | Veszteség és accuracy külön ábrán |
| M09 | önálló | Teszteredmény és egyetlen számjegy jóslata |
| M10 | kész | Tévesztések vizsgálata |
| A01 | kész | Szintetikus tranzakciók és a címkék |
| A02 | kész | Felosztás a skálázás előtt |
| A03 | önálló | Csak normál tanítóadat és külön kalibráció |
| A04 | önálló | A normál működés skálázása |
| A05 | önálló | Autoencoder szűk keresztmetszettel |
| A06 | kész | A bemenet tanítása önmagára |
| A07 | önálló | Mintánkénti kalibrációs hiba |
| A08 | önálló | Küszöb meghatározása a teszt előtt |
| A09 | önálló | Vegyes teszt: döntések és metrikák |
| A10 | kész | Hibaeloszlás és tévesztések |
| Z01 | kész | Eredmények mentése és lezárás |

## A cellák vezetése

### [E01] Környezet és munkamód

**Cél:** A Colab futtatókörnyezete használható, a hallgató ismeri a visszajelzés módját.

**Futtatás/szerkesztés előtti magyarázat:** Ez a cella betölti a könyvtárakat és megadja a véletlenmagot. Nem tanít modellt. Az Innoagent beszélgetésre szolgál, a kód szerkesztése és futtatása a saját Colab-notebookodban történik. A külön R_, M_ és A_ változónevek megőrzik a három feladat eredményeit.

**Egyetlen aktuális teendő:** Futtasd az importáló cellát a Colabban. Másold vissza a verziókat és a készenléti sort.

**Várt bizonyíték:** TensorFlow- és NumPy-verzió, valamint az E01 készenléti sor.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Nincs importhiba; a készenléti sor megjelent. Nem szükséges konkrét verzióegyezés vagy GPU.

**Elakadás esetén:** Hiányzó TensorFlow esetén ellenőrizze, hogy valóban Colab Python-futtatókörnyezetben van-e. Ne induljon helyi pip-telepítés.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R01] Lakásadatok betöltése

**Cél:** A hallgató különbséget tesz jellemzők és célérték között.

**Futtatás/szerkesztés előtti magyarázat:** A történeti Boston-adatokban egy sor egy körzetet ír le, 13 jellemzővel. A cél a körzet lakásainak mediánértéke, ezer korabeli amerikai dollárban. A hivatalos NPZ-fájl betöltése után a következő lépésben saját, független felosztást készítünk. A helyi NPZ-fájl ellenőrzése csak letöltési tartalék: nem kell fájlt feltöltened, ha a Keras-letöltés működik.

**Egyetlen aktuális teendő:** Futtasd a cellát. Írd meg a bemenet és a cél alakját, és mondd el, mi a célérték.

**Várt bizonyíték:** A két shape és a célérték saját szavas jelentése.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (506, 13) és (506, ); körzetenkénti medián lakásérték ezer korabeli USD-ban. A 13 a jellemzők száma.

**Elakadás esetén:** A shape első eleme a mintaszám. A cél nem az egyes házak mai, tényleges eladási ára.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R02] Az adatok ellenőrzése

**Cél:** A hallgató felismeri a jellemzők eltérő skáláját.

**Futtatás/szerkesztés előtti magyarázat:** A DataFrame áttekinthető táblázatot készít. Az oszlopok minimuma és maximuma megmutatja az eltérő számtartományokat. Az isfinite azt ellenőrzi, hogy nincs-e NaN vagy végtelen érték.

**Egyetlen aktuális teendő:** Futtasd a cellát. Nevezd meg két oszlop eltérő tartományát, és indokold, miért lesz hasznos a skálázás.

**Várt bizonyíték:** Két tényleges oszloptartomány és rövid indoklás.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Valós kimenetre támaszkodó skálakülönbség; a cél a bemenetek összehasonlíthatóbb számtartománya, nem az ár megváltoztatása.

**Elakadás esetén:** A TAX és a NOX például más nagyságrendű; a konkrét értékeket a saját kimenetéből olvassa le.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R03] Tanító-, validációs és teszthalmaz

**Cél:** A három halmaz szerepének elkülönítése.

**Futtatás/szerkesztés előtti magyarázat:** Először 60% tanítóadatot választunk, majd a maradékot felezzük. A validáció a korai leállításban segít, a végső tesztet a tanítás befejezése után értékeljük. A kerekítés miatt nem teljesen azonos a validációs és tesztdarabszám.

**Egyetlen aktuális teendő:** Futtasd a cellát. Küldd el a három darabszámot, és nevezd meg, melyik halmaz alapján állítjuk le a tanítást.

**Várt bizonyíték:** Három darabszám és a validáció szerepe.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 303, 101, 102; a validációs veszteséget követjük, nem a végső tesztet.

**Elakadás esetén:** A tanítóhalmazból frissülnek a súlyok; a validáció ettől külön, a kiválasztást befolyásolja.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R04] Skálázás adatszivárgás nélkül

**Cél:** A fit_transform és a transform helyes használata.

**Futtatás/szerkesztés előtti magyarázat:** A skálázó oszloponként tanul minimumot és maximumot. Ezt csak a tanítóbemenetből szabad meghatározni. A célérték most eredeti egységben marad.

**Egyetlen aktuális teendő:** Hozz létre R_scaler néven MinMaxScaler objektumot. Készítsd el R_X_train_s, R_X_val_s és R_X_test_s tömböket. Csak a tanítón használj fit_transform műveletet, a többi halmazon transformot. Írasd ki mindhárom shape-et és a skálázó n_samples_seen_ értékét.

**Várt bizonyíték:** A saját skálázó kódod, a három shape és az illesztési mintaszám.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (303, 13), (101, 13), (102, 13); n_samples_seen_=303; a kódban csak a tanítón történik illesztés.

**Elakadás esetén:** A HTML MinMaxScaler példájának munkafolyamatát alkalmazza a saját R_ változóira. A külön fit a validáción hibás.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R05] Regressziós modell

**Cél:** A kimeneti réteg megválasztása.

**Futtatás/szerkesztés előtti magyarázat:** A hálózat 13 jellemzőből egy valós értéket becsül. A rejtett rétegek ReLU aktivációt használnak. A lineáris kimenet nem korlátozza 0 és 1 közé az árbecslést.

**Egyetlen aktuális teendő:** Építs R_model nevű Sequential modellt: a bemenetet a skálázott tanítóadat jellemzőszáma határozza meg; utána 64, majd 32 ReLU-neuron következzen, végül egy lineáris kimenet. Jelenítsd meg a summary-t.

**Várt bizonyíték:** Modellkód és a summary utolsó rétegének alakja; miért egy kimenet?

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 13→64→32→1, utolsó alak (None, 1), lineáris aktiváció. Az ár egy szám; nem osztály.

**Elakadás esetén:** Egy Dense-réteg szintaxisát más, például 8 neuronos esettel mutasd; a teljes saját hálózatot először a tanuló írja.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R06] Veszteség és korai leállítás

**Cél:** A compile és a korai leállítás jelentése.

**Futtatás/szerkesztés előtti magyarázat:** A compile nem tanít, hanem beállítja az optimalizálót és a veszteséget. A MAE az abszolút eltérések átlaga. A korai leállítás a validációs veszteség alapján a tanulás megfelelő állapotát választja.

**Egyetlen aktuális teendő:** Fordítsd R_model-t adam optimalizálóval és mae veszteséggel. Hozz létre R_stop EarlyStopping objektumot: val_loss figyelése, min_delta=0.001, patience=12, legjobb súlyok visszaállítása. Írd ki a loss-t és a monitor nevét.

**Várt bizonyíték:** Compile- és callback-kód; mi történik 12 javulás nélküli epoch után?

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** MAE, val_loss, patience 12, restore_best_weights=True. Tizenkét egymást követő érdemi javulás nélküli epoch után leállhat.

**Elakadás esetén:** A patience nem az összes epoch száma. A min_delta a megfigyelt javulás minimális nagysága.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R07] Regresszió tanítása

**Cél:** Tanítás megfigyelése és befejezésének igazolása.

**Futtatás/szerkesztés előtti magyarázat:** A fit a tanítómintákból és áraikból módosítja a súlyokat. A validáció nem kap közvetlen súlyfrissítést. A 150 epoch felső korlát; a callback ennél korábban is leállíthat.

**Egyetlen aktuális teendő:** Futtasd a tanítást, várd meg a végét. Küldd el a lefutott epochok számát és a legkisebb validációs veszteséget.

**Várt bizonyíték:** Az R07 összefoglaló két száma a tanítás befejeződése után.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 1..150 epoch, véges validációs MAE. Nem szükséges adott hibahatár vagy early-stop bekövetkezése.

**Elakadás esetén:** Futó cellánál várjon; ne indítson új fit-et ugyanarra a modellre. Új kísérlethez az R05-től kell friss modellt létrehozni.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R08] Tanulási görbék értelmezése

**Cél:** A két görbét konkrét megfigyeléssel tudja értelmezni.

**Futtatás/szerkesztés előtti magyarázat:** A grafikon a tanító és validációs MAE-t mutatja. A görbék közös csökkenése és tartós szétválása más tanulási helyzetre utal. Pontos epochszám helyett az irány és a kapcsolat felismerése a fontos.

**Egyetlen aktuális teendő:** Futtasd a rajzolást. Írj le egy konkrét megfigyelést a tanító- és validációs görbe kapcsolatáról.

**Várt bizonyíték:** Képernyőkép vagy saját szavas, konkrét görbeleírás.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Mindkét görbe azonosítva; legalább egy alátámasztott megfigyelés. A nem látott görbe trendjét nem szabad kitalálni.

**Elakadás esetén:** Ha csak annyit mond: jó, kérd, hogy nevezze meg, együtt csökkennek-e vagy eltérnek. Ha már konkrét, ne kérdezd újra.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R09] Végső teszt és alapbecslés

**Cél:** A MAE mértékegységének és érvényességi körének értelmezése.

**Futtatás/szerkesztés előtti magyarázat:** A tesztet most használjuk először eredményértékelésre. Összevetjük a hálózatot egy állandó alapbecsléssel, amely mindig a tanítócélok mediánját tippeli. MAE-nél ez természetes kiindulás.

**Egyetlen aktuális teendő:** Futtasd a cellát. Küldd el a két MAE-t, és mondd el a hálózat hibájának jelentését a megfelelő egységben.

**Várt bizonyíték:** Hálózati MAE, alap-MAE, és a hálózati szám jelentése.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Átlagos abszolút tévedés ezer korabeli USD-ban; a saját két eredményből következtet. Gyengébb hálózat sem automatikus feladathiba.

**Elakadás esetén:** 2.5 MAE kb. 2500 korabeli USD átlagos abszolút eltérést jelent, nem 2.5%-ot. A példaszám nem elvárt eredmény.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [R10] Új adat és ugyanaz a skálázó

**Cél:** Új mintát azonos előfeldolgozással tud átadni.

**Futtatás/szerkesztés előtti magyarázat:** A teszthalmaz egy nyers mintáján szemléltetjük az új adat útját. Ez nem új független teszt; az egyedi becslés lépéseit nézzük meg. A mintaszám dimenzióját egyetlen sornál is megtartjuk.

**Egyetlen aktuális teendő:** Válaszd az R_X_test első sorát kétdimenziós szelettel R_uj néven. A már illesztett R_scaler segítségével készítsd el R_uj_s-t, majd számíts becslést R_model-lel. Írd ki a bemenet és a kimenet alakját és a becslést.

**Várt bizonyíték:** Kód, a két alak és annak indoklása, miért nem fit_transform szerepel.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (1, 13), (1, 1); transform ugyanazzal a skálázóval; helyes oszlopsorrend és mintaszám-dimenzió.

**Elakadás esetén:** Az első sor kiválasztásánál a 0 index és a 0: 1 szelet eltérő alakot ad.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M01] MNIST és egy gyorsabb tanító részhalmaz

**Cél:** Külön kezeli a képeket, címkéket, validációt és tesztet.

**Futtatás/szerkesztés előtti magyarázat:** Az MNIST kézzel írt számjegyek 28×28-as képeit tartalmazza. A gyorsabb órai munka érdekében a 60000 tanítómintából 12000-et választunk osztályarányt tartó véletlen részhalmazként: 10000 tanító és 2000 validációs képet. Az eredeti 10000 tesztképet elkülönítve hagyjuk.

**Egyetlen aktuális teendő:** Futtasd a betöltést. Küldd el a három képhalmaz alakját és a címkék értéktartományát.

**Várt bizonyíték:** Három shape és a címkék tartománya.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (10000, 28, 28), (2000, 28, 28), (10000, 28, 28), címkék 0..9; az első szám képszám.

**Elakadás esetén:** A teszt 10000 képe nem a 12000-es részhalmazból keletkezett.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M02] Egy kép és a valódi címkéje

**Cél:** Az indexelés és a képi minta kapcsolatának megértése.

**Futtatás/szerkesztés előtti magyarázat:** A 3-as index a negyedik képet jelenti. M_y_test még egész osztályindexeket tárol. A címke azt jelzi, milyen számjegyet ábrázol a kép az adatkészlet szerint.

**Egyetlen aktuális teendő:** Futtasd a cellát. Mondd meg, melyik sorszámú képet nézzük, és mi a valódi címkéje.

**Várt bizonyíték:** A kép sorszáma és a saját kimenetében látható egész címke.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Negyedik kép; a tényleges kiírt címke. Nem kell előre a modell jóslatát találgatni.

**Elakadás esetén:** A lista 0. eleme az első, ezért a 3. index a negyedik.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M03] Normalizálás és kilapítás

**Cél:** A kép méretének átfordítása modellbemenetté.

**Futtatás/szerkesztés előtti magyarázat:** A képpontok uint 8 értékei 0 és 255 közöttiek. Float 32-re alakítva és 255-tel osztva 0–1 tartományt kapunk. A 28×28 kép 784 eleme a reshape során ugyanaz marad, csak vektorba rendezzük.

**Egyetlen aktuális teendő:** A nyers M_train_kepek, M_val_kepek és M_test_kepek tömbökből készíts M_X_train, M_X_val és M_X_test float 32 tömböket. Oszd az értékeket 255-tel, és alakítsd mindegyik képet 784 elemű vektorrá. Írd ki a három shape-et, valamint a tanítóbemenet minimumát és maximumát.

**Várt bizonyíték:** A kód, a három shape, a tartomány és a -1 jelentése.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (10000, 784), (2000, 784), (10000, 784); float 32, 0..1; a -1 a mintaszám kiszámítását kéri.

**Elakadás esetén:** A HTML 6×6-os példájának elvét alkalmazza. A nyers _kepek tömböket használja, így újrafuttatáskor sem oszt már skálázott adatot ismét.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M04] One-hot célvektorok

**Cél:** Megőrzi az egész címkéket és megfelelő célvektorokat készít.

**Futtatás/szerkesztés előtti magyarázat:** A one-hot vektor hossza az osztályok száma. A helyes osztály helyén 1, a többi helyen 0 van. Az eredeti M_y_train, M_y_val és M_y_test tömböket nem írjuk felül.

**Egyetlen aktuális teendő:** A keras.utils.to_categorical segítségével készíts M_y_train_oh, M_y_val_oh és M_y_test_oh tömböket tíz osztállyal. Írd ki a tanítócél alakját és az első egész címkét a hozzá tartozó one-hot vektorral.

**Várt bizonyíték:** A kód, (10000, 10) alak és egy összetartozó címkepár.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Helyes tízosztályos one-hot, eredeti egész címkék megőrizve. Az egyetlen 1 helye a címke indexe.

**Elakadás esetén:** Ne végezze el újra a kódolást az _oh tömbön; mindig az eredeti egész címkét használja.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M05] Számjegyosztályozó hálózat

**Cél:** A bemenet, dropout és softmax helyes összekapcsolása.

**Futtatás/szerkesztés előtti magyarázat:** A 784 bemeneti számhoz két sűrű rejtett réteg kapcsolódik. A dropout tanításkor egyes aktivációkat véletlenszerűen nulláz. A tíz softmax-kimenet a tíz számjegyhez tartozik.

**Egyetlen aktuális teendő:** Építs M_model néven hálózatot 784 bemenettel, 128 ReLU-neuronnal, 0.3 dropouttal, 64 ReLU-neuronnal, újabb 0.3 dropouttal és tíz softmax-kimenettel. Jelenítsd meg a summary-t.

**Várt bizonyíték:** Modellkód és a summary utolsó alakja; a tíz kimenet indoka.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (None, 10), két dropout és megfelelő Dense-rétegek. A kimeneti számok nem közvetlen egész számjegyek.

**Elakadás esetén:** Először csak a hibás rétegsort javíttasd. Dropout a predict alatt nem véletlenszerűen dob el aktivációkat.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M06] Osztályozási veszteség

**Cél:** A one-hot és a categorical_crossentropy összekapcsolása.

**Futtatás/szerkesztés előtti magyarázat:** A címkék one-hot alakúak, a modell softmax-kimenetet ad. Ehhez categorical_crossentropy illik. Az accuracy a helyes osztályválasztások aránya, és nem azonos a veszteséggel.

**Egyetlen aktuális teendő:** Fordítsd M_model-t adam optimalizálóval, a one-hot címkékhez megfelelő veszteséggel és accuracy metrikával. Hozd létre M_stop callbacket val_loss figyeléssel, patience=4 és a legjobb súlyok visszaállításával. Írd ki a veszteség nevét.

**Várt bizonyíték:** Compile- és callback-kód; a választott veszteség indoklása.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** categorical_crossentropy one-hot címkékkel; sparse változat csak következetesen egész célokra átállva fogadható el, a kész későbbi cellákat is igazítani kell.

**Elakadás esetén:** A one-hot és a sparse veszteség közötti különbséget a konkrét célalakból vezesse le.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M07] Az osztályozó tanítása

**Cél:** A tanítás lefutása és a metrikák követése.

**Futtatás/szerkesztés előtti magyarázat:** Legfeljebb húsz epochot engedünk, 256-os batchmérettel. A validációs képek és célvektorok külön halmazban vannak. A verbose=1 mutatja az előrehaladást; a végső teszt még nem vesz részt.

**Egyetlen aktuális teendő:** Futtasd a tanítást, várd meg a végét. Küldd el az epochok számát és a legnagyobb validációs accuracy-t.

**Várt bizonyíték:** Epochszám és a validációs accuracy saját kimenetből.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 1..20 epoch, accuracy 0..1. Nem kérünk konkrét minimumot; sikert nem garantálunk.

**Elakadás esetén:** A 0.94-es érték 94%-ot jelent, nem 0.94%-ot. Futás közben ne indítsa el még egyszer a cellát.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M08] Veszteség és accuracy külön ábrán

**Cél:** Megkülönbözteti a két mérőszámot és a dropout hatását.

**Futtatás/szerkesztés előtti magyarázat:** Balra a keresztentrópia, jobbra a találati arány látható. A dropout tanításkor aktív, validációnál nem, ezért a validációs görbe helyzete önmagában nem mutat hibát.

**Egyetlen aktuális teendő:** Futtasd az ábrázolást, és a két ábra közül egyen írj le konkrét tanító–validációs megfigyelést.

**Várt bizonyíték:** Kép vagy konkrét, a saját ábrára vonatkozó leírás.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Azonosítja, melyik ábrát értelmezi. Nem állítja, hogy az accuracy és a loss ugyanaz.

**Elakadás esetén:** A magasabb val_accuracy dropout mellett önmagában nem adatszivárgás bizonyítéka.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M09] Teszteredmény és egyetlen számjegy jóslata

**Cél:** A predict-kimenetből osztályt készít és összeveti a valódi címkével.

**Futtatás/szerkesztés előtti magyarázat:** A predict egy képre tíz kimeneti számot ad. Ezek maximumának helye a becsült számjegy. A valódi címke az eredeti egész M_y_test tömbből olvasható ki.

**Egyetlen aktuális teendő:** Értékeld M_model-t M_X_test és M_y_test_oh alapján; tárold az eredményt M_loss és M_acc néven. A korábban választott M_index képét kétdimenziós szelettel add a predictnek, majd np.argmax segítségével válaszd ki a becsült számjegyet M_josolt néven. Írd ki az accuracy-t, a tíz kimenetet, a becsült és a valódi címkét.

**Várt bizonyíték:** Kód; accuracy; kimeneti vektor; becsült és valódi számjegy.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Egy mintához tíz kimenet, argmax eredménye 0..9, egész valódi címke. A döntés lehet hibás, ez nem önmagában kódhiba.

**Elakadás esetén:** A one-hot címke vektort ne írja ki számjegyként. A predict nem maga az osztályindex.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [M10] Tévesztések vizsgálata

**Cél:** A teljes teszt teljesítményének korlátozott értelmezése.

**Futtatás/szerkesztés előtti magyarázat:** A teljes teszt kimenete 10000×10. Az argmax(axis=1) soronként, azaz képenként választ osztályt. A mátrix sorai valós, oszlopai becsült címkék. A kód egy hibás példát mutat, ha van ilyen.

**Egyetlen aktuális teendő:** Futtasd a cellát. Értelmezz egy tévesztési mátrixcellát valódi címkével, becsült címkével és darabszámmal.

**Várt bizonyíték:** Egy tényleges mátrixcella jelentése vagy egy hibás kép címkepárja; teljes teszt hibaszáma.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Sor=valós, oszlop=becsült; konkrét adat. Hibátlan futásnál egy átlócella értelmezése elegendő, ne kérjen nem létező hibát.

**Elakadás esetén:** Egyetlen jóslat nem helyettesíti a teljes tesztet. A teszteredmény alapján nem kezdünk új konfigurációkeresést.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A01] Szintetikus tranzakciók és a címkék

**Cél:** A normál és rendellenes címke jelentése, aránytalanság felismerése.

**Futtatás/szerkesztés előtti magyarázat:** A kiinduló notebookhoz hasonlóan 1000 normál és 50 eltolással képzett rendellenes, öt jellemzőjű mintát generálunk. A jellemzők itt mesterséges számok, nem valós tranzakciós mezők. A címke 0 normál, az 1 rendellenes. Ez az egyszerű adatkészlet nem reprezentálja a valós banki csalások összetettségét.

**Egyetlen aktuális teendő:** Futtasd a cellát. Írd le a két osztály darabszámát, és nevezd meg, melyik címke jelenti az anomáliát.

**Várt bizonyíték:** Címkejelentés, darabszámok és bemeneti shape.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 0: 1000 normál, 1: 50 anomália, (1050, 5). Nem 5% az összesből, hanem 50/1050≈4.76%.

**Elakadás esetén:** A normálhoz viszonyítva 5%, az összes mintához viszonyítva kb.4.76% az anomáliaarány.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A02] Felosztás a skálázás előtt

**Cél:** A tesztet még bármilyen illesztés előtt elkülöníti.

**Futtatás/szerkesztés előtti magyarázat:** A stratify megőrzi az osztályarányokat. Még nyers adatokkal dolgozunk: nincs a teljes adatra illesztett skálázó. A normál mintákat csak a felosztás után választjuk ki.

**Egyetlen aktuális teendő:** Futtasd a felosztást. Küldd el a három elemszámot és a teszt két osztályának darabszámát.

**Várt bizonyíték:** 630/210/210 és a teszt címkeeloszlása.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Teszten 200 normál és 10 anomália. Még nincs adatból számolt előfeldolgozási paraméter.

**Elakadás esetén:** A ritka anomáliák kis tesztmintaszáma miatt egyetlen tévesztés is 10 százalékponttal módosítja az anomália recallját.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A03] Csak normál tanítóadat és külön kalibráció

**Cél:** Helyes logikai maszk és elkülönített küszöbmeghatározás.

**Futtatás/szerkesztés előtti magyarázat:** A 0 címke alapján választjuk ki a normál sorokat. A normál validációs adatot két részre bontjuk: az egyik a korai leállításhoz, a másik a küszöb kalibrálásához szolgál. Így a küszöb még a validáció tanulást irányító részétől is elkülönül.

**Egyetlen aktuális teendő:** Készíts A_normal_train és A_normal_val tömböket a 0 címkéjű tanító-, illetve validációs sorokból. A_normal_val-t train_test_split segítségével felezd A_normal_stop és A_normal_cal tömbre, random_state=42 mellett. Írd ki a három felhasznált rész alakját.

**Várt bizonyíték:** Saját szűrőkód és a három shape.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** (600, 5), (100, 5), (100, 5); helyes 0-s maszk; a vegyes teszt változatlan.

**Elakadás esetén:** Az astype(bool) itt az 1-hez adTrue-t, így önmagában az anomáliákat választaná. A feltételes maszkot írja ki egyértelműen.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A04] A normál működés skálázása

**Cél:** A skálázó paraméterei csak normál tanítóadatból származnak.

**Futtatás/szerkesztés előtti magyarázat:** Ugyanazt a skálázót alkalmazzuk a normál stop-, normál kalibrációs és vegyes tesztadatokra. Az anomáliák skálázott értékei túlléphetnek az 1-en: ezt nem vágjuk le, mert az eltérés információt hordozhat.

**Egyetlen aktuális teendő:** Hozz létre A_scaler MinMaxScaler objektumot, és készítsd el az A_train_s, A_stop_s, A_cal_s, A_test_s tömböket. Az illesztés csak A_normal_train-en történjen. Írd ki a skálázó illesztési mintaszámát és a négy shape-et.

**Várt bizonyíték:** Kód, 600-as illesztési mintaszám és négy shape.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Csak normál tanítóra fit; (600, 5), (100, 5), (100, 5), (210, 5). A teszten nincs új illesztés.

**Elakadás esetén:** A scaler nem tanulhat a kalibrációból vagy a tesztből sem. Nem szükséges minden új értéknek 0..1 között lennie.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A05] Autoencoder szűk keresztmetszettel

**Cél:** A rekonstrukciós modell bemenetének és kimenetének felismerése.

**Futtatás/szerkesztés előtti magyarázat:** Öt jellemzőt próbálunk visszaállítani. A középső három érték kisebb dimenziójú, mint a bemenet. Az eredeti mesterséges normál adatok nem eleve alacsony dimenziósak, ezért a tömörítés a normál adatoknál is okozhat hibát. Az öt sigmoid kimenet a normál tanítóadat 0–1 tartományához illik; a tartományon kívüli bemenetet ezért nem tudja hibátlanul visszaadni.

**Egyetlen aktuális teendő:** Építs A_model nevű autoencodert: 5 bemenet → 16 ReLU → 3 lineáris → 16 ReLU → 5 sigmoid kimenet. Fordítsd adam optimalizálóval és mse veszteséggel. Jelenítsd meg a summary-t.

**Várt bizonyíték:** Modellkód; az öt kimenet és a háromelemű középső réteg jelentése.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 5→16→3→16→5; öt sigmoid kimenet, nem egyetlen bináris kimenet; a modell a bemenetet rekonstruálja, nem közvetlen címkét tanul.

**Elakadás esetén:** A csalás 0/1 döntése később a hibaküszöbből keletkezik. A hálózat kimenete most öt szám.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A06] A bemenet tanítása önmagára

**Cél:** A fit célértékének megértése.

**Futtatás/szerkesztés előtti magyarázat:** A tanító bemenet és cél ugyanaz a normál tömb. A stop-halmaz is csak normál adatot tartalmaz. A kalibrációs adat még nem szerepel a fit-ben, a teszt sem.

**Egyetlen aktuális teendő:** Futtasd a tanítást. Küldd el az epochszámot, és mondd el, miért szerepel ugyanaz a tömb a fit első két argumentumában.

**Várt bizonyíték:** Epochszám és a bemenet=cél magyarázata.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Rekonstrukciót tanul normál adatokon; nem az 0/1 címkéket kapja célként.

**Elakadás esetén:** Ha címkét adott második argumentumnak, ne folytassátok hibás modellel: A05 új modell, majdA06.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A07] Mintánkénti kalibrációs hiba

**Cél:** Az axis=1 és a rekonstrukciós MSE tudatos használata.

**Futtatás/szerkesztés előtti magyarázat:** Először a külön normál kalibrációs mintákat rekonstruáljuk. Az öt jellemző négyzetes eltérését soronként átlagoljuk, így egy mintához egy hibaszám tartozik. A teljes tömb egyetlen átlaga nem alkalmas mintánkénti döntésre.

**Egyetlen aktuális teendő:** Számítsd ki A_cal_rek-et A_model.predict-tel az A_cal_s-ből. Ezután készíts A_cal_hiba néven mintánkénti MSE-t np.mean segítségével, a megfelelő tengely mentén. Írd ki a rekonstrukció és a hibatömb alakját, valamint az első öt hibát.

**Várt bizonyíték:** Kód és(100, 5)rekonstrukció, (100, )hiba, axisindoklás.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Nemnegatív, véges 100 hibaszám; axis=1 az öt jellemző mentén átlagol.

**Elakadás esetén:** Egy másik 2 mintás, 3 jellemzős példán magyarázd a tengelyt, majd a hallgató javítsa a saját sorát.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A08] Küszöb meghatározása a teszt előtt

**Cél:** A küszöbszabályt a teszt ismerete nélkül rögzíti.

**Futtatás/szerkesztés előtti magyarázat:** A normál kalibrációs hibák 97%-os kvantilisét választjuk. Ez előre rögzített oktatási szabály, nem biztosít minden új halmazon pontosan 3% téves riasztást. Az átlag+2 szórás másik lehetséges heurisztika, nem kötelező matematikai törvény.

**Egyetlen aktuális teendő:** Készíts A_kuszob változót az A_cal_hiba 97%-os kvantiliseként np.quantile segítségével. Írd ki a küszöböt és a kalibrációs hibák számát; mondd el, miért nem a teszthibákat használjuk.

**Várt bizonyíték:** Kód, küszöb, 100 kalibrációs minta; a teszt függetlenségének indoka.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** np.quantile(A_cal_hiba, .97), véges küszöb; nem tesztfüggő hangolás. Most rögzítsük a küszöböt.

**Elakadás esetén:** A 97% nem a detektálás elvárt accuracy-je. A tesztet nem használjuk beállításválasztásra.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A09] Vegyes teszt: döntések és metrikák

**Cél:** Elválasztja a modellkimenetet, hibát és bináris döntést.

**Futtatás/szerkesztés előtti magyarázat:** A210 tesztminta között normál és rendellenes adat is van. A rögzített küszöbnél nagyobb hiba 1-es döntést ad. A címkéket csak az eredményértékelésben hasonlítjuk a döntésekhez.

**Egyetlen aktuális teendő:** Rekonstruáld A_test_s-t A_test_rek néven, számíts A_test_hiba mintánkénti MSE-t, majd készíts A_pred 0/1 egész döntéseket a rögzített A_kuszob segítségével. Írasd ki classification_report-tal a Normál és Anomália osztályok eredményét, labels=[0, 1], zero_division=0 mellett.

**Várt bizonyíték:** Kód, classification_report, az Anomália sor precisionje és recallja.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** 210 hibaszám és döntés, helyes irányú > küszöb; positiveclass 1. Nulla detektált anomália esetén is a tényleges eredményt kell értelmezni.

**Elakadás esetén:** A precision a riasztások pontossága, a recall a megtalált anomáliák aránya. A0-s osztály recallja nem a csalások megtalálási aránya.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [A10] Hibaeloszlás és tévesztések

**Cél:** A riasztásokat valódi darabszámokból tudja értelmezni.

**Futtatás/szerkesztés előtti magyarázat:** A mátrix összefoglalja a helyes és hibás döntéseket. A hibaeloszlás a két valódi osztály rekonstrukciós hibáit mutatja, a függőleges vonal pedig a korábban rögzített küszöb. Itt már nem állítunk a küszöbön.

**Egyetlen aktuális teendő:** Futtasd a cellát. Küldd vissza a TN, FP, FN, TP értékeket, és magyarázd el egy téves riasztás vagy elmulasztott anomália jelentését.

**Várt bizonyíték:** Négy darabszám és konkrét értelmezés; a küszöb nem változott.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Összeg 210, TN+FP=200, FN+TP=10. Nem kell nem létező hibát találni; hibátlannál a nulla cella jelentése is megfelelő.

**Elakadás esetén:** FP normál mintán riasztás, FN valódi anomália jelzés nélkül. A teszteredmény alapján ne válasszon új küszöböt.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.

### [Z01] Eredmények mentése és lezárás

**Cél:** Az elvégzett munkát saját eredményekkel összefoglalja és elmenti.

**Futtatás/szerkesztés előtti magyarázat:** A három feladat eltérő célértéket és metrikát használ. A rövid összefoglaló segít a saját futási eredményeket egy helyen áttekinteni. A kitöltött notebookot a Colab mentési vagy letöltési lehetőségével őrizd meg.

**Egyetlen aktuális teendő:** Futtasd a cellát, küldd el az összefoglalót, és mentsd a saját kitöltött notebookodat.

**Várt bizonyíték:** A három feladat saját eredményeinek összesítése és a mentés jelzése.

**Elfogadási szempont – ezt ne előre felmondandó válaszként add:** Három eredménycsoport csak valóban elvégzett futás után. Az agent három rövid szóbeli zárókérdést egyenként kérdez ezután.

**Elakadás esetén:** Ha valami kimaradt vagy nem futott le, a lezárásban tételesen jelezni kell; ne állítsatok teljes teljesítést.

**Ezután:** várd meg a hallgató kimenetét és szükséges értelmezését. Csak igazolt állapot után következhet a következő cella.
