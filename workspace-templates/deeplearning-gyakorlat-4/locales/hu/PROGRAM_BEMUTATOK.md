# Rövid programbemutatók és kódmagyarázatok

Minden szakasz első része közvetlenül elmondható tanulói bemutató. Az agent
ezt az első futás ELŐTT mondja el, a kódrészletekkel és azok magyarázatával
együtt. Ne rövidítse puszta célmegjelölésre, és ne adja fel olvasnivalónak.
A bevezető végén egyetlen futási feladatot adjon, majd várja meg az eredményt.
A „További magyarázat” az ismétlés és az elakadás támogatása; nem kell az
egész háttéranyagot egyszerre elmondani. A konkrét forrást mindig ellenőrizze:
az alábbi minták a kiinduló változatok, a tanuló már módosíthatta őket.
A kódblokkok a meglévő program részletei, nem bemásolandó új programok.

## G04_01 – hogyan lesz a gradiensből súlyfrissítés?

### Első futás előtt elmondandó bemutató

Most a `G04_01_tanulasi_rata.py` példában azt nézzük meg, hogyan változik
egy súly a tanulási ráta hatására. Egyetlen számot, a `suly` értékét módosítjuk;
a cél a 3. A veszteség `(suly - 3) ** 2`: a céltól való eltérés négyzete,
amely pontosan a célnál nulla. Itt a súlyfrissítést külön vizsgáljuk, adathalmaz
és teljes neurális hálózat nélkül.

Az induló beállítások:

```python
tanulasi_rata = 0.1
lepesek_szama = 8
kezdo_suly = -1.0
```

A kezdő súly megadja, honnan indulunk. A tanulási ráta a frissítés méretét
szabályozza, a lépésszám pedig azt, hányszor hajtjuk végre. A program ciklusában
minden alkalommal ez a három sor számol:

```python
gradiens = 2 * (suly - 3)
suly = suly - tanulasi_rata * gradiens
veszteseg = (suly - 3) ** 2
```

A gradiens a veszteség helyi meredeksége; a képlete itt készen adott.
Az előjele jelzi a növekedés irányát, ezért a második sor kivonja a rátával
szorzott gradienst. A harmadik már az új súly hibáját számolja.
Nézzünk egy közös lépést: −1-nél a gradiens −8, így az új súly
−1 − 0,1·(−8) = −0,2. A negatív szám kivonása itt növelte a súlyt.
Az új veszteség (−0,2−3)² = 10,24.

A kimenet három oszlopa a lépésszám, a súly és a veszteség; a 0. sor az indulás.
A `tanulasi_lepesek.png` ezek változását mutatja. Később a rátát és a lépésszámot
fogod külön-külön módosítani. Most futtasd változtatás nélkül a fájlt a Run
gombbal, és küldd el az utolsó sort. Ebből vizsgáljuk majd, hová jutott a súly.

### További magyarázat – kérdés vagy ismétlés esetére

Egyetlen súly van. A 3 a kívánt érték, a `suly` a jelenlegi állapot.
A `tanulasi_rata` a frissítés méretét szabályozza; a ciklus ismétli a lépést.

```python
gradiens = 2 * (suly - 3)
suly = suly - tanulasi_rata * gradiens
veszteseg = (suly - 3) ** 2
```

Az első sor a régi súlyhoz tartozó érzékenységet számolja. A második sor
ezt használja a súly megváltoztatásához. A harmadik már az **új súllyal**
számol veszteséget. Negatív gradiens kivonása növeli a súlyt.
Nem kell fejből több lépést kiszámolni. Az elsőt közösen követjük,
a továbbiakat a program és a kép teszi láthatóvá.

A `range(lepesek_szama)` ismétlésszámot ad; a `round` vagy a formázás csak
a kiírt tizedesjegyek számát szabályozza, a számítás pontosságát nem állítja át.
A CSV minden lépést megőriz, a hosszabb terminálkimenet rövidített.

## G04_02 – a momentum két sora

### Első futás előtt elmondandó bemutató

Az előző példában minden lépés csak az aktuális gradiensre támaszkodott.
A `G04_02_momentum.py` azt mutatja meg, mi történik, ha a korábbi elmozdulásból
is megőrzünk valamennyit. Most két paraméterünk van: x és y. A veszteség
`x*x/20 + y*y`, minimuma a (0, 0) pont. Ez az egyik irányban laposabb,
a másikban meredekebb felszín; itt sincs adathalmaz vagy teljes hálózat.

A számítás indulása az `utvonal(beta)` függvényben:

```python
hely = np.array([-7.0, 2.0])
sebesseg = np.zeros(2)
```

A `hely` a két paramétert tartalmazó tömb. A `hely[0]` az első, a `hely[1]`
a második érték. A sebesség is két szám, kezdetben mindkettő nulla. A ciklusban:

```python
gradiens = np.array([hely[0] / 10, 2 * hely[1]])
sebesseg = beta * sebesseg - tanulasi_rata * gradiens
hely = hely + sebesseg
```

Az első sor megadja a veszteség meredekségét a két irányban. A második sor
az előző sebesség `beta`-szorosát összekapcsolja az aktuális gradienslépéssel.
Az utolsó sor ezzel a sebességgel mozdítja el a pontot. A tömbműveletek mindkét
koordinátán elvégzik ugyanezt. A `momentum = 0.9` a függvény `beta` paraméterébe
kerül: az előző sebesség 90%-a szerepel a következő frissítésben.

A program ugyanonnan két útvonalat számol: `utvonal(0.0)` és `utvonal(momentum)`.
A ráta mindkettőnél 0,1, a lépésszám 40. A kiírás a végpontot és a végső
veszteséget adja; az `utvonalak.png` a bejárt utakat mutatja. A szintvonalak
azonos veszteségű pontokat kötnek össze. Később csak a momentumot változtatod.
Most futtasd változtatás nélkül a fájlt, és küldd el a két végpontot a
veszteségekkel; ezek alapján hasonlítjuk össze az eredményeket.

### További magyarázat – kérdés vagy ismétlés esetére

Ugyanazon tál alakú függvény minimumát keressük két szabállyal. A veszteség
`x*x/20 + y*y`, így a gradiens két komponense `x/10` és `2*y`.

```python
gradiens = np.array([hely[0] / 10, 2 * hely[1]])
sebesseg = beta * sebesseg - tanulasi_rata * gradiens
hely = hely + sebesseg
```

A `hely` egy kétértékű tömb; az első elem x, a második y. A `sebesseg`
ugyanilyen tömb, kezdetben [0,0]. A beta megőrzi a korábbi sebesség egy részét,
ehhez adódik az aktuális gradiensből képzett lépés. Utána elmozdítjuk a helyet.
A `copy()` a lépés állapotát külön másolatban őrzi meg az ábrához.
Beta=0 esetén a régi sebesség nem számít; egyszerű gradienslépés marad.

A szintvonal ugyanakkora veszteséget jelentő pontokat köt össze. Az ábrán
a zöld pont a kezdet, a narancs az utolsó lépés, a fekete kereszt a minimum.
A két panel azonos tengelytartományt használ, ezért az útvonalak összevethetők.

## G04_03 – a neuron kimenete és a derivált nem ugyanaz

### Első futás előtt elmondandó bemutató

A `G04_03_aktivaciok.py` egy neuron működésének másik részét emeli ki:
az aktivációt és annak szerepét a gradiens továbbításában. A bemeneti öt szám
−6, −1, 0, 1 és 6. Ezeket most úgy kezeljük, mint a neuron már kiszámolt
súlyozott összegeit. Nem tanítunk hálózatot, csak átalakítjuk a számokat.
Az `aktivacio = "sigmoid"` választja ki az első függvényt; később ReLU-t és
Leaky ReLU-t is kipróbálsz.

A `fuggveny(z)` sigmoid ága:

```python
if aktivacio == "sigmoid":
    return 1 / (1 + np.exp(-z))
```

A `z` a bemenet, az `np.exp` az exponenciális függvényt számolja. A sigmoid
0 és 1 közötti kimenetet készít. A külön `derivalt(z)` függvény azt adja meg,
mennyire érzékeny ez a kimenet a bemenet kis változására. Sigmoidnál az ottani
`ertek * (1 - ertek)` képletet használjuk; nem kell levezetned.

A program ezután három külön tömböt állít elő:

```python
kimenetek = fuggveny(bemenetek)
lokalis_derivaltak = derivalt(bemenetek)
visszaadott_gradiensek = beerkezo_gradiens * lokalis_derivaltak
```

Az első az előre számolt aktiváció. A második a helyi meredekség.
A harmadik a visszafelé továbbított gradiens: a hálózat későbbi részéből
érkező jelet a helyi deriválttal szorozzuk. Itt a beérkező gradiens kész,
2-es érték; ez külön mennyiség a bemenettől. Közös mintapontként z=0 esetén
a sigmoid 0,5, deriváltja 0,25, a visszaadott gradiens pedig 2·0,25 = 0,5.

A táblázat négy oszlopa: bemenet, kimenet, lokális derivált, visszaadott
gradiens. Az ábra külön mutatja a függvényt és a deriváltját. Később a bemeneti
értékeket, majd az aktivációt módosítod. Most futtasd változtatás nélkül a
fájlt, és küldd el a 0 és a 6 bemenet sorát; a két helyi deriváltat fogjuk összevetni.

### További magyarázat – kérdés vagy ismétlés esetére

A bemenet itt a neuron már kiszámolt súlyozott összege, z. A példában nem
számítunk súlyozott összeget, csak a nemlineáris átalakítást vizsgáljuk.

```python
ertek = 1 / (1 + np.exp(-z))
lokalis_derivalt = ertek * (1 - ertek)
```

Sigmoidnál z=0 → kimenet=0,5 → derivált=0,25. Nagy abszolút bemenetnél
a kimenet telítődik, a derivált kicsi. A kimenet nem lehet negatív,
de ettől még egy teljes hálózat súlyainak gradiense lehet negatív.

```python
np.maximum(0, z)
np.where(z > 0, z, negativ_meredekseg * z)
```

Az első sor a ReLU: elemenként a 0 és a z közül a nagyobbat választja.
A második a Leaky ReLU: pozitív bemenetnél z, egyébként a meredekséggel
szorzott z. A `np.where` feltétel, igaz ág, hamis ág sorrendben kap argumentumokat.
A deriváltfüggvény a megfelelő ág meredekségét adja vissza.

```python
visszaadott_gradiensek = beerkezo_gradiens * lokalis_derivaltak
```

Ez a láncszabály helyi lépése. A példában 2 a beérkező gradiens, nem a bemeneti
aktiváció. A 0 pontbeli ReLU-deriváltnál a program 0-t választ. Leaky ReLU-nál
a bal oldali meredekséget választjuk. Ez a töréspontban számítási konvenció,
nem két különböző oldali meredekség matematikai egyenlősége.

## G04_04 – egy kis regressziós hálózat

### Első futás előtt elmondandó bemutató

A `G04_04_kis_halozat.py` már egy valódi, CPU-n tanuló neurális hálózat.
Egyetlen x számból egy folytonos y értéket becslünk: ez regresszió.
A program 192 mesterséges pontot készít egy hullámos függvényből, kis zajjal.
64 pont a tanításhoz, 128 a validációs méréshez tartozik. A validációs pontokat
nem használjuk a súlyok frissítésére. A kész adat-előkészítés most a háttérben marad.

Először felépítjük a modellt:

```python
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(REJTETT_NEURONOK, activation="relu"),
    layers.Dense(1),
])
```

A `Sequential` egymás után kapcsolja a rétegeket. Az `Input(shape=(1,))`
mintánként egy bemeneti jellemzőt jelent. A rejtett Dense-réteg kezdetben
8 neuront tartalmaz: mindegyik súlyozott összeget és tanulható eltolást képez,
majd ReLU-t alkalmaz. A végső `Dense(1)` ezekből egyetlen számot becsül.
Nincs rajta sigmoid: a kimenetnek nem kell 0 és 1 közé esnie.

Az utána következő `modell.compile(...)` beállítja a tanítás szabályait.
Az Adam optimalizáló rátája 0,01; a `loss="mae"` átlagos abszolút hibát jelent.
Ha például a cél 0,7, a becslés 0,5, ennek a mintának az abszolút hibája 0,2.
A MAE ezeket átlagolja, a célváltozó egységében; nem százalék. A compile még
nem tanít. A tényleges tanítás itt kezdődik:

```python
tortenet = modell.fit(
    tanito_adatok,
    validation_data=validacios_adatok,
    epochs=EPOCHOK,
    shuffle=False,  # Az előkészített adatcsomag már keveri a tanítómintákat.
    verbose=0,
    callbacks=[RovidJelzes(EPOCHOK)],
)
```

A `tanito_adatok` tartalmazza a bemenet–cél párokat. Egy epocha a 64 tanítóminta
egyszeri bejárása; 16-os adagokkal ez 4 súlyfrissítés. Az `EPOCHOK = 120`
120 ilyen bejárást jelent. A `validation_data` minden epocha végén mér.
A keverést az előkészített adatcsomag végzi, a `verbose` és az állapotjelző
csak a kiírást szabályozza. A `tortenet` az epochák mérési adatait őrzi.

A végén tanítási és validációs MAE-t kapsz az utolsó modellállapotra.
A `becsles.png` a pontokat és a hálózat becslését, a `tanulasi_gorbek.png`
a hibák alakulását mutatja. Később a neuronszámot és az epochaszámot módosítod,
mindig friss modellt tanítva. Most futtasd változtatás nélkül a fájlt, várd meg
a FUTÁSI ÖSSZEFOGLALÓ és FUTÁS KÉSZ részt, majd küldd el a két végső MAE-t.

### További magyarázat – kérdés vagy ismétlés esetére

**Minta:** egy x bemenet és egy y cél. Az x −3 és 3 közötti szám, a cél
egy hullámos függvény zajos értéke. A zaj nem külön bemenet. A program
ugyanazokat a 64/128 mintákat generálja minden futásban.

```python
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(REJTETT_NEURONOK, activation="relu"),
    layers.Dense(1),
])
```

A `shape=(1,)` egyetlen jellemzőt jelent mintánként, nem egyetlen mintát.
A rejtett réteg több különböző súlyozott és ReLU-val átalakított értéket készít.
A végső Dense ezekből egy lineáris becslést ad. A bias a réteg tanulható eltolása.
A tanuló most a neuronszámot változtatja, nem kell új réteget építenie.
8 rejtett neuron esetén 25, 64 esetén 193 tanulható paraméter van; a program kiírja.

```python
modell.compile(
    optimizer=keras.optimizers.Adam(learning_rate=TANULASI_RATA),
    loss="mae",
    metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
    jit_compile=False,
)
```

A compile konfigurál; még nem tanít. Az Adam a gradiensekből számol frissítést.
A ráta itt 0,01 és a kötelező hálózatos kísérletekben állandó.
A `loss="mae"` abszolút hibát ad a cél és a becslés között, majd átlagol.
Ugyanezt külön metrikaként is követjük, ami a későbbi L2-példában lesz fontos.
A `jit_compile=False` technikai beállítás; nem tanulási feladat, ne változtassátok.

```python
tortenet = modell.fit(
    tanito_adatok,
    validation_data=validacios_adatok,
    epochs=EPOCHOK,
    shuffle=False,
    verbose=0,
    callbacks=[RovidJelzes(EPOCHOK)],
)
```

Itt tanul a hálózat. A tanító-adatcsomag már tartalmazza a bemenet–cél párokat,
16-os adagokba szervezve és reprodukálhatóan keverve. Ezért a fit-ben nem adjuk
meg újra a `batch_size`-t és a keverést. A `shuffle=False` **nem** azt jelenti,
hogy soha nincs keverés: azt a kész adatcsomag végzi.
A validáció az epocha végén mér, súlyt nem frissít. A rövid állapotjelző
csak kiír néhány epochaszámot, nem állítja le a tanítást és nem állít vissza súlyokat.

**Mérés a kész segédben:**

```python
validacios_becsles = modell(validacios_x, training=False).numpy()
validacios_mae = np.mean(np.abs(validacios_y - validacios_becsles))
```

A `training=False` kiértékelési viselkedést kér. Ebben a két Dense-réteges
modellben nincs dropout vagy batch normalization; a jelölés mégis egyértelművé
teszi, hogy most becslést készítünk. A hívás nem tanít. A `.numpy()` a tensor
értékeit NumPy-tömbként adja vissza a méréshez és rajzoláshoz.

**A három kép értelmezése:**

- `becsles.png`: pontok és a hálózat folytonos becslése. A szürke szaggatott
  görbe a szintetikus adatgenerátor ismert, zaj nélküli függvénye, nem teszteredmény.
- `tanulasi_gorbek.png`: tanítási és validációs MAE epochánként. A tanítási
  görbe az epochán belül változó súlyokkal mért átlag, a validáció az epocha végi állapot.
- `loss_es_mae.png`: büntetés nélkül a két validációs mennyiség egybeesik;
  a következő programban különválnak.

A 400 epochás futás azonos kezdeti állapotból újratanul; nem a 120-as modell folytatása.
Nem az ábra legkisebb értékét írjuk ki végső eredményként, hanem az utolsó súlyok mérését.

## G04_05 – az L2 beépítése

### Első futás előtt elmondandó bemutató

A `G04_05_l2_regularizacio.py` az előző hálózathoz súlybüntetést ad.
Ugyanazokat a tanító- és validációs adatokat használjuk. Ebben az önálló fájlban
64 rejtett neuron és 120 epocha szerepel: a korábbi 64 neuronos, 120 epochás
kísérlethez kapcsolódunk, új modellt tanítva. Most az `L2_EROSSEG` lesz az
egyetlen vizsgált beállítás; kezdetben 0,0, vagyis még nincs büntetés.

A modellben itt jelenik meg az új elem:

```python
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(REJTETT_NEURONOK, activation="relu",
                 kernel_regularizer=regularizers.l2(L2_EROSSEG)),
    layers.Dense(1, kernel_regularizer=regularizers.l2(L2_EROSSEG)),
])
```

A `kernel_regularizer` az adott réteg súlymátrixához rendel büntetést.
Az L2-erősség, más néven λ, megszorozza a súlyok négyzeteinek összegét.
Ezt a Keras hozzáadja a becslési hibához, így a tanítás során a nagy súlyoknak
is ára van. Itt mindkét Dense-réteg súlymátrixa kap büntetést, az eltolások
nem. A kapcsolódó HTML/Spotify-példában csak a rejtett rétegek kapnak ilyet.

A compile-ban két külön szerepet látsz:

```python
loss="mae",
metrics=[keras.metrics.MeanAbsoluteError(name="mae")],
```

Ezek a meglévő függvényhívás argumentumai. A `loss` becslési tagja MAE,
ehhez a Keras hozzáadja az L2-büntetést. A külön `mae` metrika csak a
becslési hibát méri. Közös számpélda, nem mért kimenet: [2, −1] súlyok és
λ=0,01 mellett a büntetés 0,01·(4+1)=0,05. Ha a MAE 0,12, a teljes loss 0,17.

A kiírás külön közli a MAE-t, a büntetést, a teljes loss-t és a súlyok
négyzetösszegét. A `loss_es_mae.png` a két validációs mennyiséget mutatja.
A becslések minőségét a validációs MAE alapján fogjuk összevetni. Most
futtasd az alapváltozatot 0,0-s L2-erősséggel és 120 epochával, majd küldd el
a két végső MAE-t és a validációs teljes loss-t.

### További magyarázat – kérdés vagy ismétlés esetére

A modell, az adatok, a ráta és a 120 epocha rögzített. Csak λ változik.
Az egyszerűség kedvéért mindkét Dense-kernelre alkalmazzuk a büntetést.
A HTML/Spotify-példa rejtett rétegekre alkalmazott regularizálásához képest
itt a kimeneti kernel is regularizált; a biasokat továbbra sem büntetjük.

```python
layers.Dense(REJTETT_NEURONOK, activation="relu",
             kernel_regularizer=regularizers.l2(L2_EROSSEG))
layers.Dense(1, kernel_regularizer=regularizers.l2(L2_EROSSEG))
```

Ez két réteg konstruktorhívásának szemléltető részlete; a fájlban a Sequential
listájában szerepelnek, vesszővel elválasztva. A `kernel_regularizer` a réteg
súlymátrixára vonatkozik. A regularizer számértéke λ-szor a kernel négyzetösszege.

```python
teljes_veszteseg = becslesi_mae + l2_buntetes
```

Ez a jelentését mutató képlet, a tanítás során az összeadást a Keras végzi.
A külön MAE-metrika nem tartalmaz büntetést. Az eltérő λ-val tanított modellek
előrejelzését azonos validációs MAE alapján hasonlítjuk.
A súlymátrixok négyzetösszege nem az L2-norma: a normához még négyzetgyök kellene.
Nagyobb λ mellett kisebb súlyok sem garantálnak jobb becslést.

## G04_06 – dropout rövid tömbön

### Első futás előtt elmondandó bemutató

A `G04_06_dropout.py` a dropout működését teszi láthatóvá nyolc pozitív
számon. Ezek egy réteg képzeletbeli aktivációi. Most nem tanítunk újabb
hálózatot: azt figyeljük, mely értékek jutnak tovább, és hogyan változik a
nagyságuk. A `tanitasi_mod = True` az átalakítás üzemmódját jelenti.
A kezdeti `kiesesi_arany = 0.5` minden elemnél 50%-os kiesési valószínűséget ad.

A tanítási ág:

```python
if tanitasi_mod:
    maszk = veletlen.random(len(bemenetek)) >= kiesesi_arany
    kimenetek = bemenetek * maszk / (1 - kiesesi_arany)
```

Az első számítás minden bemenethez egy 0 és 1 közötti véletlen számot készít.
A feltétel igaz értéke megtartást, hamis értéke kiesést jelent. A maszk
szorzáskor 1 és 0 értékként működik. A következő sor lenullázza az eldobott
elemeket, a megmaradókat pedig elosztja a megtartási valószínűséggel.
0,5-ös kiesésnél ez kétszerezés: például egy megtartott 0,8-ból 1,6 lesz.
Ez egy lehetséges elem magyarázata, nem a még nem látott maszk eredménye.
A skálázás az értékek várható nagyságát őrzi meg; egy rövid vektorban sem
pontos feleződés, sem pontosan változatlan átlag nem garantált.

A másik ág:

```python
else:
    maszk = np.ones(len(bemenetek), dtype=bool)
    kimenetek = bemenetek.copy()
```

Kiértékelési módban minden érték továbbjut. A `copy()` ugyanazokat az értékeket
teszi egy új tömbbe; nincs további skálázás. A nulla itt nem törölt neuront jelent.
A `veletlen_mag = 42` miatt azonos beállításokkal újrafuttatva ugyanazt a mintát
kapod. Később külön módosítod a kiesési arányt, a magot és az üzemmódot.

A kiírás a bemenetet, a maszkot és a kimenetet mutatja; a `dropout.png`
a bemeneti és kimeneti értékeket hasonlítja össze. Most futtasd változtatás
nélkül a fájlt, és küldd el a maszkot és a kimenetet. A saját számaidon nézzük
majd meg, hogyan működött a nullázás és a skálázás.

### További magyarázat – kérdés vagy ismétlés esetére

Nyolc pozitív aktivációt használunk, hogy a véletlen nullázás jól látszódjon.
A bool maszk számtani műveletben 0/1-ként működik.

```python
maszk = veletlen.random(len(bemenetek)) >= kiesesi_arany
kimenetek = bemenetek * maszk / (1 - kiesesi_arany)
```

A random 0 és 1 közötti értékeket mintáz. A `>= p` az 1−p valószínűségű
megtartást jelöli. Maszk=0 mellett a kimenet 0. Maszk=1 mellett a megmaradó
értéket 1/(1−p)-vel szorozzuk. p=0,5 esetén ez kétszerezés.
Az aktiváció várható értékét őrizzük, nem az egyetlen rövid vektor tényleges átlagát.

```python
kimenetek = bemenetek.copy()
```

Ez a kiértékelési ág: nincs nullázás és külön skálázás. Itt a `.copy()` egy
külön tömböt készít ugyanazokkal az értékekkel. A szemléltetés nem állítja,
hogy a dropout biztosan javítaná az előző regressziós modell pontosságát.

## K04_01 – opcionális softmax: első futás előtti bemutató

Ezt csak külön kérésre használd. A `K04_01_softmax.py` három osztály
pontszámából, azaz logitjából közösen normalizált valószínűségeket készít.
A kiinduló pontszámok 2, 1 és 0; ezek még nem valószínűségek. Nincs tanítás.

```python
eltolt_logitok = logitok + kozos_eltolas
exponencialisak = np.exp(eltolt_logitok - np.max(eltolt_logitok))
valoszinusegek = exponencialisak / np.sum(exponencialisak)
```

Az első sor mindhárom ponthoz ugyanazt a számot adja. A második a maximum
kivonása után exponenciálist számol: így elkerülhető a nagy pozitív értékek
exponenciális túlcsordulása. A harmadik elosztja a pozitív értékeket az összegükkel,
így az eredmény összege 1. Az elemek egymástól is függenek, mert közös a nevező.
A program kiírja a pontszámokat, a valószínűségeket és az összegüket, majd
oszlopábrát ment. Később a közös eltolást változtatod meg. Most futtasd az
alapváltozatot, és küldd el a három valószínűséget és az összegüket.

## K04_02 – opcionális batch normalization: első futás előtti bemutató

Ezt csak külön kérésre használd. A `K04_02_batch_normalization.py` az 1, 2, 3,
4 értékeken mutatja meg a normalizálást, majd a skálázást és eltolást.
Itt a gamma és beta kézzel állítható; egy valódi rétegben tanulható paraméterek.
Ebben a példában nincs hálózattanítás.

```python
if tanitasi_mod:
    atlag = np.mean(bemenetek)
    variancia = np.mean((bemenetek - atlag) ** 2)
else:
    atlag = tarolt_atlag
    variancia = tarolt_variancia
```

Tanítási módban az aktuális négy számból számítunk átlagot és varianciát,
vagyis átlagos négyzetes eltérést. A másik ág előre megadott, tárolt adatokat
használ. Ezek itt szemléltető értékek, nem egy korábbi tanítás mérései.

```python
normalizalt = (bemenetek - atlag) / np.sqrt(variancia + epszilon)
kimenetek = gamma * normalizalt + beta
```

Először kivonjuk az átlagot és elosztjuk a szóráshoz közeli mennyiséggel;
a kis epszilon stabilizálja az osztást. A gamma szoroz, a beta eltol.
Kezdetben gamma=1, beta=0. A kiírás külön mutatja a használt statisztikákat,
a normalizált értékeket és a végső kimenetet; a kép a bemenettel hasonlít össze.
Később külön változtatod a gammát, a betát és az üzemmódot. Most futtasd az
alapváltozatot, és küldd el a normalizált értékeket és a végső kimenetet.
