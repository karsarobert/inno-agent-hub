# Deep Learning 2026 – Programbemutatások és kódmagyarázatok

Ez olvasható hallgatói segédlet és a tutor bemutatásainak alapja. A tutor minden
új fájl előtt bemutatja a célt és az adatok útját, majd a fontos kódrészleteket.
Az olvasást nem adja ki a beszélgetésbeli magyarázat helyett. Az idézetek a
kiinduló programokat követik; módosítás után az aktuális forrásból kell idézni.

A `szemlelteto.html` dupla kattintással, internet nélkül megnyitható. A benne
állított számok csak a szemléltetést módosítják: a Python-fájlba kézzel kell
átírni a kívánt változtatást. Nem olvassa automatikusan az aktuális forrást.

## G02_01 – Mit jelent egyetlen súly tanulása?

**A program célja.** Van egy ismert tanítópárunk: x = 1 és y = 3. Egy nagyon
egyszerű modell a bemenetet megszorozza egy w súllyal. A súly induló értékét
mi választjuk −1-nek. Megvizsgáljuk a becslés hibáját, majd egyetlen lépéssel
módosítjuk a súlyt. A program nem egy teljes adathalmazt tanít.

**Az adatok útja.** x és w alapján ŷ keletkezik; ŷ és az ismert y alapján
veszteséget számolunk; ebből gradiens és új w készül. Az új w-vel új becslést
és új veszteséget kapunk. A bemenet és a cél változatlan marad.

```python
bemenet = 1.0
celertek = 3.0
suly = -1.0
TANULASI_RATA = 0.2
```

Az első két szám az ismert példa. A `suly` a tanulható paraméter. A tanulási
ráta a súlyfrissítés nagyságát szabályozza. A súly nem külön „súlyfüggvény”:
a becslési függvény és a veszteségfüggvény függ a súly értékétől.

```python
becsles = suly * bemenet
veszteseg = (becsles - celertek) ** 2
```

A `*` szorzás, a `** 2` négyzetre emelés. ŷ = wx = −1; L = (−1 − 3)² = 16.
A becslés elkészítéséhez a modell nem használja y-t. A cél csak az
összehasonlításhoz kell. ŷ = w itt az x = 1 miatt igaz, nem általánosan.

```python
gradiens = 2 * (becsles - celertek) * bemenet
uj_suly = suly - TANULASI_RATA * gradiens
```

A gradiens a veszteség súly szerinti helyi meredeksége. A képlet a
L(w) = (wx − y)² deriváltja: 2(wx − y)x. Most −8. A frissítés
−1 − 0,2 · (−8) = 0,6: pozitív irányban lépünk, mert a gradiens negatív.
Az új veszteség 5,76. A `uj_suly` külön változóban őrzi az eredményt;
nincs rejtett ismétlődő tanítási ciklus.

**Mit figyelj?** A szemléltető „Egy súly” lapján haladj lépésenként. Kisebb
rátánál ugyanebben a helyzetben kisebb a lépés. Nem kell fejben újraszámolnod
minden értéket. A túl nagy ráta akár növelheti is a veszteséget.

## G02_02 – Hogyan halad át az adat a kis hálózaton?

**A program célja.** Három számot vezetünk át két rejtett neuronon és egy
kimeneti neuronon. Minden súlyt és biast kézzel adunk meg; nincs tanítás.
A rejtett neuronok súlyozott összeget számolnak, majd ReLU-t alkalmaznak.
A kimeneti neuron lineárisan számol a két rejtett kimenetből.

**Az adatok útja.** Három bemenet → két súlyozott összeg → két ReLU-kimenet
→ egy végső becslés. Nyisd meg a szemléltető „Kis hálózat” lapját; válaszd
az aktuális példát. A w[h0,x0] jelölés az x0-ból h0-ba vezető nyíl súlya.

```python
bemenetek = np.array([1.0, 2.0, -1.0], dtype=np.float32)
rejtett_sulyok = np.array([[1.0, -1.0, 0.5],
                          [-0.5, 1.0, 1.0]], dtype=np.float32)
rejtett_bias = np.array([0.0, -1.0], dtype=np.float32)
```

A `np.array` számtömböt hoz létre; a `float32` a tárolás számtípusa. A
súlymátrix alakja (2, 3): két neuron, neurononként három bejövő súly.
A bias külön paraméter, nem negyedik bemenet. Az x0 valódi bemenet.

```python
sulyozott_osszegek = rejtett_sulyok @ bemenetek + rejtett_bias
rejtett_kimenetek = np.maximum(0.0, sulyozott_osszegek)
```

A `@` minden mátrixsort összeszoroz a bemeneti vektorral, majd összegez.
Az első neuron: 1 · 1 + (−1) · 2 + 0,5 · (−1) + 0 = −1,5.
A ReLU ebből 0-t ad. A második összeg −0,5, aktiválás után szintén 0.
A `maximum` elemenként választja a nagyobbat a nulla és az adott érték közül.

```python
becsles = kimeneti_sulyok @ rejtett_kimenetek + kimeneti_bias
```

A kimeneti súlyok (2; −1), a bias 0,5: 2 · 0 − 1 · 0 + 0,5 = 0,5.
Itt nincs ReLU, így más bemenetnél a végső becslés negatív is lehet.
A kimeneti tömb egy elemet tartalmaz; a `[0]` ezt választja ki a kiíráshoz.

**Mit figyelj?** Az ábra előbb az első, majd a második neuron kapcsolatait,
végül a kimeneti kapcsolatokat emeli ki. Egy neuron számítását közösen nézzük
meg. A teljes hálózat kézi újraszámolása választható mélyítés.

## G02_03 – Ugyanaz a számítás Kerasban

**A program célja.** Az előző kézi NumPy-számítást Keras-rétegekkel írjuk le.
Ez még mindig rögzített súlyú előreterjesztés. A Keras olyan könyvtári felület,
amellyel a rétegeket és később a tanítást is megadhatjuk.

**Az adatok útja.** Egy sorba tett három bemenet → Dense(2), ReLU → Dense(1)
→ egy becslés. A kiinduló bemenet itt [1, 2, −1]. Ha a másik fájlban már
megváltoztattad, az ide nem kerül át: az összehasonlításhoz nézd meg az értékeket.

```python
modell = keras.Sequential([
    keras.Input(shape=(3,)),
    layers.Dense(2, activation="relu", name="rejtett"),
    layers.Dense(1, name="kimenet"),
])
```

A `Sequential` egymás utáni rétegeket jelent. A `shape=(3,)` mintánként három
jellemzőt mond; nem három mintát. A vessző egyelemű Python-tuple-t jelöl.
A `Dense(2)` két teljesen összekapcsolt neuront készít: mindkettő megkapja
mindhárom bemenetet. Az utolsó rétegben nincs megadott aktiválás, ezért lineáris.

```python
modell.layers[0].set_weights([
    np.array([[1.0, -0.5], [-1.0, 1.0], [0.5, 1.0]], dtype=np.float32),
    np.array([0.0, -1.0], dtype=np.float32),
])
```

A lista első tagja a kernel, a második a biasvektor. A Keras kernel alakja
(bemenetek, neuronok), tehát (3, 2). Itt egy OSZLOP tartozik egy neuronhoz;
a G02_02-ben egy SOR. Ugyanazokat a nyilakat írjuk le transzponált elrendezésben.
A `set_weights` kézzel rögzít paramétereket; nem keres jó súlyokat.

```python
becslesek = modell.predict(bemenetek, verbose=0)
```

A `bemenetek` alakja (1, 3), a visszakapott tömbé (1, 1): egy mintához egy
becslés tartozik. A `[0, 0]` az első minta első kimenetét választja. A
`verbose=0` a folyamatjelzést kapcsolja ki. A `predict` nem módosít súlyokat.
Ehhez a bemutatóhoz nem kell `compile`. A `summary` 11 paramétert mutat:
3 · 2 + 2 bias, majd 2 · 1 + 1 bias. A kiírt `None` a változó batchméret helye.

**Mit figyelj?** A NumPy-kód és a Keras-kód ugyanazt a hálózatot valósítja meg.
A szemléltető mellett keresd meg, melyik kódsor írja le a rejtett réteget.
A bias módosítása választható próba; a teljes számítás nem kötelező.

## G02_04 – Mit tartalmaznak a boradatok, és miért készítjük elő őket?

**A program célja.** Minden sor egy bormintáról tartalmaz mért adatokat.
A 11 bemenet például az alkoholtartalom, a pH és a szulfáttartalom. A
`quality` az ismert minőségi pontszám. A következő program ezt próbálja
megbecsülni. Most csak adatot készítünk elő, hálózatot még nem építünk.

Egy valódi sor rövid részlete a mellékelt CSV-ből:

| alcohol – bemenet | pH – bemenet | sulphates – bemenet | quality – cél |
|---:|---:|---:|---:|
| 9.4 | 3.51 | 0.56 | 5 |

További nyolc bemeneti jellemző is van. A táblázat szűkítése itt kizárólag
szemléltetés. Új bor becslésekor a mért tulajdonságokat ismerjük, a keresett
pontszámot nem adjuk be a modellnek.

**Az adatok útja.** Helyi CSV → ismétlődő sorok kezelése → X és y külön →
tanító/validációs/teszthalmaz → tanítóadatból meghatározott skálázás.

```python
nyers_adatok = pd.read_csv(adatfajl)
adatok = nyers_adatok.drop_duplicates().reset_index(drop=True)
jellemzok = adatok.drop(columns=["quality"])
celertekek = adatok["quality"]
```

A `read_csv` táblázatot, DataFrame-et olvas be. Az 1599 sorból 240 teljes
sor ismétlődik; ebben a példában mindegyiket egyszer használjuk. A `reset_index`
folytonos sorindexet készít. Ez oktatási döntés, nem minden ismétlődés hibás.
A `drop(columns=...)` elhagyja a célt a bemenetekből. Így X-nek 11 oszlopa,
y-nak egy pontszáma van mintánként.

A két `train_test_split` hívás előbb 20% tesztadatot választ le, majd a maradék
25%-át validációnak: összesen körülbelül 60/20/20% a felosztás. A seed 42
mellett 815/272/272 minta keletkezik. A tanítóadat a súlyfrissítéshez kell;
a validáció a beállítások összehasonlításához; a teszt a lezárt választás
végső értékeléséhez. A `random_state` a felosztás ismételhetőségét segíti.

```python
skalazo = MinMaxScaler()
tanito_skala = skalazo.fit_transform(tanito_jellemzok)
validacios_skala = skalazo.transform(validacios_jellemzok)
```

Miért skálázunk? A jellemzők eltérő mértékegységűek és nagyságrendűek;
az átalakítás segítheti az optimalizálást. A `fit` oszloponként meghatározza
a tanítóminimumot és maximumot. A `transform` kiszámítja:
(érték − minimum) / (maximum − minimum). A validációhoz ugyanazt a szabályt
használjuk, nem számítunk új szélsőértékeket. Tanítóminimum 0, maximum 10
esetén 5-ből 0,5, egy új 12-es értékből 1,2 lesz. A validáció tehát kiléphet
[0,1]-ből. A scikit-learn az állandó oszlop külön esetét is kezeli.

**Mit figyelj?** A (815, 11) alak sorokat és jellemzőket jelent. A
`tanito_skala[0, :3]` az első sor első három értékét választja ki kiírásra;
a `:5` csak a megjelenített részletet bővíti, nem alakítja át X-et.

## G02_05 – Hogyan tanulja meg a hálózat a borminőség becslését?

**A program célja.** Most már ténylegesen tanítunk. A 11 mért tulajdonságból
egy minőségi pontszámot becslünk. Bár az adatbeli pontszám egész szám,
ezt itt regresszióként kezeljük: a becslés például 6,2 is lehet. Nem kell
kerekíteni a veszteségszámításhoz.

**Az adatok útja.** A G02_04 előkészítését ez az önálló program újra elvégzi.
Utána hálózatot épít, beállítja a tanítást, súlyokat tanul, validációs hibát
számol, majd ábrát és eredményeket ment. Nem folytat egy előző fájlban élő modellt.

```python
keras.Input(shape=(tanito_skala.shape[1],)),
layers.Dense(REJTETT_NEURONOK[0], activation="relu"),
layers.Dense(REJTETT_NEURONOK[1], activation="relu"),
layers.Dense(1),
```

Az alapfelépítés 11 → 32 → 16 → 1. A rejtett rétegek tanulható átalakításokat
végeznek, a lineáris kimenet egy pontszámot ad. A rejtett értékek nem kézzel
megnevezett bortulajdonságok. A modell 929 paraméterrel indul.

```python
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="mae",
)
```

A `compile` a tanítás módját állítja be, nem végez tanítást. Az Adam a
gradiensek alapján módosítja a paramétereket; nem azonos az első példánk
egyszerű frissítési képletével. A MAE az abszolút hibák átlaga. Ha a cél 6,
a becslés 6,2, ennek a mintának az abszolút hibája 0,2 pont. A 0,56 MAE
átlagosan 0,56 pont eltérést jelent, nem 56%-os hibát vagy 44%-os pontosságot.

```python
tortenet = modell.fit(
    tanito_skala, tanito_cel,
    validation_data=(validacios_skala, validacios_cel),
    epochs=EPOCHOK, batch_size=BATCH_MERET, verbose=2,
)
```

A `fit` végzi a tanítást. Egy epoch a teljes tanítóhalmaz egyszeri bejárása.
A batch egy súlyfrissítéshez együtt feldolgozott adag: itt legfeljebb 64 minta.
815 mintából 13 adag keletkezik; az utolsóban 47 minta van. A validáció
kiértékelés, nem gradiensből végzett súlyfrissítés. A `History` objektum
`history` szótára az epochonkénti metrikákat tárolja.

Az `evaluate` a validáció egészén mér; a `predict` néhány mintára konkrét
becslést ad. A tanítócélok mediánját mindig jósló alapmodell egyszerű
összehasonlítás: érdemes-e a tanult hálózatot használni? Itt az utolsó epoch
modelljét értékeljük; nincs automatikus legjobb súly-visszaállítás.

**Mit figyelj?** A cél–becslés párt és a MAE jelentését. A görbe két vonala
más adathalmazból származik. Az epochszám csökkentése kevesebb bejárás;
az eredményt mérjük, a pontosság változását nem garantáljuk.

## G02_06 – Hogyan lesz két koordinátából osztály?

**A program célja.** 500 mesterségesen létrehozott pont négy csoportját
vizsgáljuk. Egy pont két koordinátája a bemenet, a generátor által adott
0, 1, 2 vagy 3 címke a cél. A csoportok átfedhetnek, ezért nem várunk
mindenáron hibátlan osztályozást.

**Az adatok útja.** Pontgenerálás → három halmaz → skálázás → one-hot cél →
2–32–16–4 hálózat tanítása → négy becslés → osztályindex → ábra.

```python
jellemzok, cimkek = make_blobs(
    n_samples=500, n_features=2, centers=OSZTALYOK_SZAMA,
    cluster_std=2.0, random_state=2,
)
```

A `make_blobs` ismert csoportokhoz tartozó pontokat készít. A `cluster_std`
a szóródást szabályozza. A felosztás `stratify` argumentuma az osztályarányokat
őrzi meg. 300/100/100 minta lesz. Itt StandardScaler-t használunk: a tanítóátlagot
vonjuk ki, és a tanítószórással osztunk; ez nem [0,1]-re skálázás.

```python
tanito_cel = keras.utils.to_categorical(tanito_cimkek, OSZTALYOK_SZAMA)
layers.Dense(OSZTALYOK_SZAMA, activation="softmax")
```

A `to_categorical` az ismert címkéből one-hot célvektort készít. A 2-es
osztály célja [0, 0, 1, 0]. A softmax a modell négy kimenetét nemnegatív,
egyre összegződő becslésekké alakítja. A cél és a becslés két külön adat.
A softmax önmagában nem garantál kalibrált valószínűségeket.

| Osztályindex | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| Ismert one-hot cél | 0 | 0 | 1 | 0 |
| Szemléltető modellbecslés | 0,05 | 0,10 | 0,80 | 0,05 |

```python
valoszinusegek = modell.predict(validacios_skala[:5], verbose=0)
becsult_osztalyok = valoszinusegek.argmax(axis=1)
```

A `predict` BEMENETE öt minta két-két skálázott koordinátája, alakja (5, 2).
A VISSZATÉRÉSI ÉRTÉKE öt darab négyes becslési vektor, alakja (5, 4).
Az `argmax(axis=1)` soronként a legnagyobb érték indexét választja. A példa
eredménye 2, mert a harmadik elem indexe 2: Pythonban nullától indexelünk.
Az eredmény nem a 0,80 érték, hanem az osztályindex. Öt mintánál alakja (5,).

A `categorical_crossentropy` a tanítás vesztesége. One-hot célnál mintánként
−log(a helyes osztály becsült valószínűsége); nagyobb helyes becsléshez kisebb
veszteség tartozik. Az `accuracy` a helyesen választott osztályok aránya.
A két szám más jelentésű, és a boros MAE-vel sem hasonlítjuk össze őket.

**Mit figyelj?** Az ábra pontszíne a valódi címke, háttere a modell osztálydöntése.
A háromszögek validációs pontok. Az ábrakészítés rácspontokat skáláz és jósol;
ezek nem új tanítópontok. A rejtett neuronszám módosítása nem változtatja meg
a négy kimenet jelentését. A napló végén a tényleges neuronszám és paraméterszám
ellenőrizhető: alapból 692, (16,16) esetén 388. A tesztkapcsoló most False marad.

## G02_07 – Tanulási görbék, korai leállítás és indokolt választás

**A program célja.** A már ismert boros feladatot tanítjuk, de nem feltétlenül
használjuk el a teljes epochkeretet. Megfigyeljük, hogy a validációs hiba
javul-e még, és ez alapján állítjuk le a tanítást. A kimenet továbbra is
egy minőségi pontszám, nem osztálycímke.

**Az adatok útja.** Boradatok → ugyanaz a regressziós alapmodell → epochonkénti
tanítás és validáció → leállási döntés → követett legjobb súlyok visszaállítása
→ eredmények összehasonlítása → kiválasztott beállítás végső tesztje.

```python
korai_leallitas = keras.callbacks.EarlyStopping(
    monitor="val_loss", mode="min", min_delta=MIN_JAVULAS,
    patience=TURES_EPOCH, restore_best_weights=True,
)
```

A callback a tanítás kijelölt pontjain meghívott objektum. A `val_loss` a
`validation_data` adataiból számított veszteség. A `mode="min"` kisebb értéket
keres. A `min_delta=0.001` abszolút javulási küszöb: ezt meghaladó javulás
számít érdeminek a követett legjobb értékhez képest. Nem százalék.
A `patience=8` nyolc egymást követő, ilyen javulás nélküli epochot enged;
egy érdemi javulás újraindítja a számlálást. A `restore_best_weights=True`
a követett legjobb pont súlyait állítja vissza. A nyers naplóminimum a
küszöb miatt kissé eltérhet a visszaállított modell eredményétől.

```python
# A fit híváson belül:
validation_data=(validacios_skala, validacios_cel),
callbacks=[korai_leallitas],
```

A `validation_data` adja a mérés adatait, a `callbacks` kapcsolja be a
leállítás figyelését. A callback létrehozása önmagában nem elég. A 120 epoch
felső keret; a teljes keret lefutása is lehetséges.

**Mit figyelj?** Előbb a görbéket értelmezzük. Melyik tanítási és melyik
validációs? Látszik tartós szétválás, vagy mindkettő ellaposodik? Egyetlen
rosszabb pont nem bizonyít túlilleszkedést. Ha nem világos, melyik görbéről
beszélsz, a tutor ezt tisztázza, nem találja ki.

Ezután 8-as és 4-es türelemmel összehasonlítható futás készül. A választás
előre rögzített szempontja itt a kisebb visszaállított validációs MAE; az
epochszámot a ráfordítás megértéséhez mellé tesszük. Nem automatikusan az
utoljára kipróbált beállítást választjuk. A korábbi próba eredménymappája
megmarad akkor is, ha visszaírjuk a jobbnak talált beállítást.

A kiválasztott `TURES_EPOCH` értéket állítsd be, majd `VEGSO_TESZT = True`.
Az új futás ugyanazzal a kiválasztott eljárással új modellt tanít, és a
visszaállított súlyokat teszten értékeli. Nem korábban mentett modellt tölt be.
A teszteredmény alapján már nem választunk másik türelmet. A választás
indokát és a két összehasonlított futás nevét írd a `KISERLETI_JEGYZET.md`-be.

## Közös technikai részek

A CPU-t beállító környezeti változók a TensorFlow importja előtt szerepelnek.
Az importok a használt könyvtárakat töltik be. A `Path(__file__).resolve().parent`
a program mappáját adja: innen érjük el a CSV-t és ide mentjük az eredményeket.
Az f-sztring kapcsos zárójelei értékeket helyettesítenek be; a `:.4f` négy
kiírt tizedesjegyet jelent, nem módosítja a számítás pontosságát.

A tanítóprogramok új időbélyeges mappát készítenek. A Matplotlib `Agg` módja
PNG-fájlt ment felugró ablak helyett. A `to_csv` táblázatot ment; a JSON a
beállításokat rögzíti; a `shutil.copyfile` megőrzi a futtatott forrást.
E részek szerepét érdemes ismerni; minden mentési sor kikérdezése nem cél.
