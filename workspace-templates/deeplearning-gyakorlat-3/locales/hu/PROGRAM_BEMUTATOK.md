# Programbemutatók – Inno magyarázó támasza

Az áttekintést a tutor mondja el, nem helyettesíti „olvasd el ezt a fájlt” kéréssel.
A példák a csomag kezdeti kódját mutatják; módosítás után mindig az aktuális
forrást magyarázd. A segedletek.py rajzolását nem kell soronként megtanulni.

## Kötelező bemutatási minimum – 1.1

A következő táblázat a tutor felkészülését segíti; a hallgatónak ténylegesen
mutasd meg az érintett kódot a futtatás ELŐTT. Nem elég, hogy itt le van írva.
Legfeljebb két rövid blokk egy üzenetben, köztük egy célzott hallgatói lépés.

| Program | Bemutatandó részletek |
|---|---|
| G03_01 | Becslés/hiba; mindkét np.mean gradiens; súly és bias frissítése |
| G03_02 | One-hot és egész címke; Input/Dense; compile; teljes fit; evaluate és predict/argmax |
| G03_03 | Új rejtett réteg; önálló 50–50 építés; a ráta 0.01 → 0.001 módosítása |
| G03_04 | Saját választás és indok; load_model/evaluate; tesztábra értelmezése |

## G03_01 – Egyetlen lineáris neuron, látható súlyfrissítéssel

**Mi a program célja?** Egy elképzelt tanuló tanulási idejéből becsülünk
pontszámot. Minden sor egy idő–pontszám pár; mind a 100 pár mesterséges.
A kapcsolat nagyjából egyenes, némi zajjal. A neuronnak egyetlen bemenete,
egy súlya és egy biasa van; lineáris kimenetet ad. A súlyt és biast a 80
kijelölt tanítópárból tanulja, a 20 validációs pár csak az ellenőrzésre szolgál.
Ez a notebook kézi gradiensmódszerét teszi önálló programban követhetővé.

**Adatút:** adatok előállítása → becslés → eltérés és gradiens →
súly/bias módosítása → veszteség és ábrák. Nincs fájlletöltés.

```python
becsles = suly * tanito_x + bias
hiba = becsles - tanito_y
```

A tanito_x egyszerre 80 időértéket tartalmaz, így a szorzás 80 becslést ad.
A tanito_y az ismert cél, a hiba a becslés mínusz cél. A pozitív hiba
felülbecslést, a negatív alulbecslést jelent. A bias a bemenettől független
eltolás: nulla tanulási időnél a becslés bias. Nem tudunk ok-okozati
összefüggést vagy valódi hallgatói teljesítményt igazolni szintetikus adatokból.

```python
suly_gradiense = np.mean(hiba * tanito_x)
bias_gradiense = np.mean(hiba)
```

A np.mean átlagol a tanítópárokon. A súly a bemenettel szorzódik,
ezért gradiense tartalmazza tanito_x-et; a biasé nem. A két szám azt jelzi,
hogyan változna az átlagos veszteség az adott paraméter kis változtatására.
L = átlag((becslés − cél)²) / 2. A felezés eltünteti a deriválásból adódó 2-t.
A képlet értelmét kell látni, nem önállóan levezetni.

```python
suly = suly - TANULASI_RATA * suly_gradiense
bias = bias - TANULASI_RATA * bias_gradiense
```

A gradienssel ellentétes irányba lépünk. A ráta a lépés nagyságát skálázza;
nem a hálózat tanult súlya. Negatív gradiens kivonása növeli a paramétert.
Itt minden frissítés a teljes 80 mintát használja: egy epoch egy súlyfrissítés.
A tanítás 120 alkalommal ismétli ezt. Az ábrák a frissítés UTÁNI veszteséget
mutatják; az első pont már az első lépés eredménye.

**Értékelés:** loss.png: két görbe; regresszio.png: tanult egyenes és pontok.
A zaj miatt az egyenesnek nem kell minden ponton átmennie. Az alacsonyabb
veszteség ugyanebben a feladatban kisebb átlagos négyzetes hibát jelent.
Minden képmegnyitás előtt frissíteni kell a Nézet fájllistáját.

## G03_02 – Három spirálosztály, egyszerű alapmodell

**Mi a probléma?** Egy síkbeli pont két koordinátájából meg kell mondani,
melyik spirálág osztályához tartozik. A címkék 0, 1, 2; nem minőségi
sorrendet jelentenek. 600 pontot állítunk elő a notebook elvét követve,
reprodukálható véletlen zajjal. A két koordinátából a hálózat három
osztályhoz ad valószínűségi becslést. Ez osztályozás, szemben az előző
program egyetlen folytonos pontszámával.

**Adatút:** spirálpontok → 360/120/120 felosztás → one-hot célok →
modell és tanítás → validációs görbék, döntési kép, mentett modell.
A koordináták itt eleve körülbelül −1 és 1 közöttiek, ezért nincs külön skálázó.
A tesztet most csak félretesszük, nem használjuk az architektúra kiválasztásához.

```python
tanito_cel = keras.utils.to_categorical(tanito_cimke, num_classes=3)
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(3, activation="softmax"),
])
```

A címke 2 one-hot alakja [0,0,1]. A tanito_cel alakja (360,3), a tanito_x-é
(360,2): a cél nem egy harmadik bemeneti koordináta. A shape=(2,) egy mintán
belüli két jellemzőt ír le, a vessző egyelemű Python-tuple-t képez. A Dense
minden kimeneti neuront minden bemenethez kapcsol. A három softmax-érték
nemnegatív és összegük numerikusan közel 1. Az osztálybecslés nem bizonyosság.
Ebben a modellben nincs rejtett réteg: páronként egyenes döntési határokat kapunk.

**Két címkeábrázolás, ugyanaz az osztály:** ezt a különbséget a teszt előtt tanítsd.

| Cél egy mintához | Az egész célhalmaz alakja | A három softmax-kimenethez illő loss |
|---|---|---|
| `[0,0,1]` | `(N,3)` | `categorical_crossentropy` |
| `2` | `(N,)` | `sparse_categorical_crossentropy` |

A to_categorical az egész címkéből one-hot alakot készít. A két veszteség
ugyanazt a többosztályos problémát kezeli eltérő célábrázolással; nem azt
jelenti, hogy a sparse eleve jobb vagy rosszabb. Itt one-hot cél marad,
ezért categorical_crossentropy-t használunk. A hallgatónak ezt a párosítást
kell felismernie, nem kell új loss-t implementálnia.

```python
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
```

Az Adam a gradiensek alapján frissíti a paramétereket, saját adaptív
lépésszabállyal. A learning_rate továbbra is fontos skálázási beállítás.
A keresztentrópia az ismert one-hot cél és a softmax-eloszlás eltérését bünteti;
a helyes osztályhoz rendelt kis valószínűség nagy büntetést ad.
Az accuracy a helyesen osztályozott minták aránya; mérőszám, nem itt
minimalizált veszteség. A compile csak előkészít, még nem tanít.

```python
tortenet = modell.fit(
    tanito_x, tanito_cel,
    validation_data=(validacios_x, validacios_cel),
    epochs=EPOCHOK, batch_size=BATCH_MERET, verbose=0,
)
```

A fit első két argumentuma a bemeneti koordinátatömb és a hozzá soronként
illeszkedő céltömb. A validation_data zárójelében külön ellenőrző bemenet–cél
pár van. A return érték, tortenet, a tanítás mérési történetét tartalmazza.
Az evaluate ezzel szemben az aktuális modell mutatóit méri a megadott adatokon.
A fit végzi a tanítást. Az epoch a teljes tanítóhalmaz egyszeri feldolgozása;
32-es batch esetén egy lépés legfeljebb 32 mintán számolt gradienst használ.
360 minta: 11 teljes 32-es batch és egy 8-as, összesen 12 frissítés epochonként.
A validációs adatokon epochonként mérünk, de azokból nincs súlyfrissítés.
A verbose=0 az epochonkénti képernyőszöveget kapcsolja ki, nem a tanítást.
A tortenet.history tartalmazza a loss, val_loss, accuracy és val_accuracy sorozatokat.

```python
valoszinusegek = modell.predict(validacios_x[:5], verbose=0)
becsult_osztalyok = valoszinusegek.argmax(axis=1)
```

A [:5] az első öt mintát választja ki. A predict eredménye 5 × 3-as tömb,
nem öt címke. Az argmax soronként kiválasztja a legnagyobb érték indexét.
Például [0.10,0.75,0.15] → 1. A 0.75 a valószínűségi becslés,
az 1 az osztályindex. A predict nem tanít. A kész ábrázoló ugyanezt az
átalakítást használja a pontok színezésére; a teljes 3-os vektort nem adja
RGB-színként a szórásdiagramnak.

**Mit figyeljünk?** A spirál egyenesekkel nehezen választható szét.
A gyenge eredmény itt az egyszerű modellosztály korlátjára is utalhat.
A loss változhat akkor is, ha az argmax-osztályok és az accuracy nem változnak.

## G03_03 – Rejtett réteg létrehozása és bővítése

**Mi változik?** Ugyanazokat a pontokat osztályozzuk, de a modell köztes
jellemzőket is tanul. A kezdeti hálózat 16 ReLU-neuronnal rendelkezik.
A bemenet két koordináta, a kimenet változatlanul három osztálybecslés.
A hallgató utána két 50 neuronos rejtett réteget épít. A rajzoló kód ugyanaz,
így a figyelem a modell létrehozásán és az eredményén marad.

```python
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

Az első Dense 16 súlyozott összeget számít a két koordinátából és 16 biasból.
A ReLU a negatív összeg helyére nullát tesz, a pozitívat meghagyja.
A kimeneti réteg ezután 16 tanult köztes értékből számít három softmax-értéket.
A rejtett rétegekben alkalmazott nemlinearitás hajlítható, szakaszonként
lineáris osztályhatárokat tesz lehetővé. Több lineáris réteg aktiválás nélkül
nem adna ilyen új nemlineáris kifejezőerőt.

| Hálózat | Paraméterek | Számolási támpont |
|---|---:|---|
| 2 → 3 | 9 | 2×3 + 3 |
| 2 → 16 → 3 | 99 | (2×16+16) + (16×3+3) |
| 2 → 50 → 50 → 3 | 2853 | (2×50+50) + (50×50+50) + (50×3+3) |

A számokat a model.summary / count_params is megadja; nem kell fejből
vizsgáztatni a hallgatót. A nagyobb modell több tanulható paramétert jelent,
nem automatikusan jobb általánosítást. A tanulási ráta, epoch és batch
ugyanaz marad a kötelező architektúra-összevetésben.

**A négy kész ábra értelmezése:**

- loss.png: tanítási és validációs keresztentrópia; az alacsonyabb kedvezőbb.
- accuracy.png: helyes osztályozások aránya mindkét halmazon; a magasabb kedvezőbb.
- dontesi_tartomanyok.png: háttér a döntés, két panelen valódi / becsült pontszín.
  Az osztályok színe mindkét panelen azonos: 0 kék, 1 narancs, 2 zöld.
- konfuzios_matrix.png: sor a valódi, oszlop a becsült osztály. A (0,2) cella
  például olyan 0-s pontokat számol, amelyeket a modell 2-esnek jelölt.

Ha a tanítási veszteség csökken, a validációs tartósan romlik, az túlilleszkedésre
utalhat. Ha mindkettő rossz, kevés tanítás, nehéz optimalizálás vagy túl egyszerű
modell is lehet az ok. A görbe önmagában nem bizonyít egyetlen diagnózist.
A futások azonos seedje segít összevetni őket, de más architektúra más
paraméterkészlettel indul, és egyetlen seed nem ad statisztikai bizonyítékot.

### Miért térhet el a pontosság és a veszteség szerinti sorrend?

A hallgató először értelmezze a saját futások metrikáit. Ne áruld el előre
az önálló összehasonlítás válaszát. Ha segítség kell, használd ezt a külön
tanítópéldát, amely nem a hallgató futásának eredménye:

A valódi címke 1. Két becslés: `[0.20,0.65,0.15]` és `[0.05,0.90,0.05]`.
Mindkettő az 1-es osztályt választja, ezért a pontosság szempontjából mindkettő
helyes. A második több valószínűséget rendel a valódi osztályhoz, ezért kisebb
a keresztentrópiája: `-ln(0.65)` körülbelül 0.431, `-ln(0.90)` körülbelül 0.105.
Nem kell logaritmust számoltatni. Több mintán az átlagos veszteség úgy is
javulhat, hogy közben egy mintán rosszabb lesz az argmax-döntés. Ez magyarázza,
miért lehetséges kevesebb helyes címke mellett kisebb átlagos veszteség.

A rangsor nem bizonyítja, hogy az egyik modell minden szempontból jobb.
A gyakorlat ELŐRE közölt szabálya a kisebb validációs loss-t választja;
a nagyobb hálózat több paraméterét és a pontosságát külön értelmezzük.
A 100% csak a mért adathalmazra vonatkozik, nem minden jövőbeli pontra.

### Kötelező R4 – ugyanaz a hálózat más tanulási rátával

**Áttekintés:** R3-ban már elkészült az 50–50 rejtett rétegű hálózat 0.01
rátával. Most azt vizsgáljuk, hogyan változik a tanítás menete azonos
adatokon és epochkerettel, ha kizárólag a rátát csökkentjük. Nem írunk új
programot és nem folytatjuk a korábbi súlyok tanítását. Új futás készül,
a meglévő ábrázoló kód mindkét futás görbéit külön mappába menti.

```python
TANULASI_RATA = 0.001
```

A hallgató ezt az egy beállítást módosítja. Az Adam konstruktora ezt kapja
learning_rate-ként. A két 50-es réteg, a 150 epoch (vagy előzetesen kijelölt
közös keret), a 32-es batch, a seed és a pontok változatlanok. Az azonos
architektúra és seed támogatja az összevethető inicializálást.
A kisebb ráta más optimalizálási utat eredményezhet; nem biztosít jobb
végső eredményt, és az Adam adaptív frissítései miatt a teljes tanítás minden
lépését nem egyszerűen tizedeljük. Nincs előírt „helyes” görbealak.

Run után a napló végén a tényleges 0.001 rátát és az 50–50–3 rétegeket is
ellenőrizni kell. A hallgató frissíti a Nézetet, összeveti R3 és R4 loss.png
képeit, és külön nevezi meg a tanítási és validációs görbe viselkedését.
Mit lát a kezdeti csökkenésben, későbbi ingadozásban vagy ellaposodásban,
és melyik futásnak kisebb a végső validációs vesztesége? Először ő válaszol,
a tutor csak utána kapcsolja a megfigyelést a beállításhoz.

R4 is bekerül a végső, négy futást tartalmazó összevetésbe. Nem feltétlenül
a legutóbb futtatott modell lesz a választás. A korábbi mentések miatt
nem kell a kódot visszaállítani a G03_04 indítása előtt.

## G03_04 – A kiválasztott modell független tesztje

**Mi a cél?** A tanulás és a validációs összevetés már megtörtént. Most a
korábban félretett pontokon ellenőrizzük a kiválasztott hálózatot. A program
nem tanít új modellt, a korábbi futás .keras fájlját tölti vissza. A hallgató
az R1–R4 összevetése után saját szavaival megadja a futási mappa nevét
és az előzetes választás indokát. A tutor ne adjon neki előre kész indoklást. Az ábrák és
metrikák az adott futás vegso_teszt almappájába kerülnek.

```python
modell = keras.models.load_model(mappa / 'modell.keras')
teszt_cel = keras.utils.to_categorical(teszt_cimke, num_classes=3)
eredmeny = modell.evaluate(teszt_x, teszt_cel, verbose=0, return_dict=True)
```

A load_model a rétegeket és a megtanult súlyokat helyreállítja. Az evaluate
az adatból veszteséget és pontosságot számol; return_dict=True esetén ezek
név szerint érhetők el az eredményben. Nincs fit, ezért a súlyok nem változnak,
és nincs új epochgörbe. A teszt eredménye az előre kiválasztott eljárás
értékelése. Ha utólag ezen kezdenénk másik modellt választani, többé nem
tekinthetnénk érintetlen végső ellenőrzésnek.

**A metrikák után még ábraértelmezés következik.** Nézet frissítése, majd
vegso_teszt/dontesi_tartomanyok.png és konfuzios_matrix.png. A hallgató
értelmez egy valódi/becsült címkepárt és annak darabszámát. Hibátlan esetben
az átló és a nullák jelentését mondja el, illetve hogy a pontosság a 120
vizsgált tesztpontra érvényes. A tutor ezt a választ megvárja, mielőtt a
záró kódértési tesztet elkezdené. A nagy, 1-hez közeli softmax-kimenet
önmagában nem bizonyít garantált helyességet vagy megfelelő kalibráltságot.

## Előkészített technikai háttér – röviden

A segedletek.py egységesen előállítja és osztja fel az adatokat, készíti az
ábrákat és menti a kísérleteket. Az `Agg` rajzolási mód fájlt készít felugró
ablak helyett. Az útvonalak a .py fájl helyéhez igazodnak, nem a terminál
véletlen munkakönyvtárához. Minden tanítás külön időbélyeges mappát kap,
benne a forrásmásolattal, a beállításokkal, a modellfájllal és a görbék CSV-jével.
A forrásmásolat dokumentáció, nem onnan kell a programot újraindítani.
A Nézet frissítése csak megjeleníti az újonnan létrehozott fájlokat.
