# Az első futás előtti magyarázatok

Ezek tanári bemutatók az agent számára. A hallgatóval mondd el őket, ne ezek
elolvasását add feladatul. Minden blokk végén egy alapfuttatás következik.
A későbbi módosításoknál csak az új beállítást magyarázd, ne ismételd e teljes szöveget.

## Fájltérképek – mindig a kód megnyitásakor, a kulcssorok előtt

A hallgató lássa, hol jár a fájlban. A számozott kommentblokkokat röviden járd be:

| Fájl | A fő részek sorrendje |
|---|---|
| G05_01 | 1. Példaválasztás → 2. Betöltés → 3. Egy-egy sor kiemelése → 4. Ábra és kiírás. |
| G05_02 | 1. Epochszám → 2. Normál adatok → 3. Bemenet–cél párok → 4. Teljes modell → 5. Tanítás → 6. Mérés és ábrák. |
| G05_03 | 1. Példaválasztás → 2. Referencia → 3. Kétsoros szemléltetés → 4. MAE három lépésben → 5. Ábrák → 6. Összefoglaló. |
| G05_04 | 1. Küszöb → 2. Azonos MAE-k újraszámítása → 3. Riasztások → 4. Négy darabszám → 5. Precision → 6. Recall → 7. Kiírás → 8. Képek. |

Ez nem a teljes forrás felolvasása. Például: „A fájl elején választunk egy mintát.
Utána betöltjük a két csoportot, kiválasztjuk belőlük a megfelelő sorokat, végül
elmentjük a két görbét. Most nézzük meg a kiválasztást végző sorokat.”
Minden sikeres futásra adott válaszban szerepeljen a Nézet-frissítés, mielőtt
képet kérsz megnyitni. A program saját emlékeztetőjétől ez független.

## 1. EKG-adatok – még nincs hálózat

Most először megismerjük azt az adatot, amivel a hálózat dolgozni fog.
Egy EKG-példa itt egy 140 számból álló, már előfeldolgozott jelszakasz. A számok
sorrendje számít: a görbe egymás utáni pontjai. Nem 140 betegség vagy osztály.
A vízszintes tengely a pontok indexe, a függőleges skálázott jelérték.

A csomag normál és rendellenesnek címkézett példákat tartalmaz. A mostani
program nem tanul és nem dönti el, melyik jel rendellenes: a meglévő címke
alapján mutat meg egy-egy példát a két csoportból. Nem kell orvosi diagnózist adnod;
a görbék alakját fogjuk megfigyelni.

```python
minta_index = 0
normal_jel = normal_jelek[minta_index]
rendellenes_jel = rendellenes_jelek[minta_index]
```

A `minta_index` választja ki a megjelenített sort. A számozás nullától indul,
így 0 az első példa. A két csoport külön adathalmaz: ugyanaz az index nem azt
jelenti, hogy ugyanannak az embernek két mérését látjuk. A `normal_jel` egyetlen
140 elemű sor; a `normal_jelek` a teljes normál gyakorlócsoport.

A futás kiírja az egy jelhez tartozó alakot, és két görbét ment az `ekg_jelek.png`
képre. Először változtatás nélkül futtasd a `G05_01_ekg_adatok.py` fájlt.
Küldd el az „Egy jel 140 mintapontot tartalmaz” sort! A következő lépésben megnézzük a képet.

**Az indexváltás előtt, elmondandó:** „Most egy másik jelalakot vizsgálunk meg.
Állítsd a minta_index értékét 3-ra. Pythonban 0 az első, 1 a második, 2 a harmadik,
3 a negyedik példa. A normál csoport negyedik és a rendellenes csoport negyedik
jelét emeljük ki. Az értékeiket nem módosítjuk, csak másik példát választunk.”
A program 0–127 közötti egész indexet fogad el. Utána mentés, Run, Nézet-frissítés, új kép.

## 2. Autoencoder – mit tanítunk?

Most olyan hálózatot tanítunk, amely a kapott EKG-jelet próbálja visszaállítani.
512 normál jelet lát a tanításban. Nem a normál/rendellenes címkéket tanulja:
a kívánt kimenet ugyanaz a 140 jelérték, mint amit bemenetként kap.

A hálózat eleje fokozatosan csökkenti a belső értékek számát: 140 → 32 → 16 → 8.
Ez az encoder. A nyolc érték a szűk keresztmetszet: ezekből kell a decodernek
16 → 32 → 140 lépésekben visszaállítania a jelet. A nyolc szám tanult belső
reprezentáció, nem nyolc előre kijelölt EKG-pont. A rekonstrukció közelítő.

Mutasd meg a teljes hálózatot, az encoder/decoder megjegyzésekkel együtt:

```python
modell = keras.Sequential([
    keras.Input(shape=(140,)),
    # Encoder
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    # Szűk keresztmetszet
    layers.Dense(szuk_keresztmetszet, activation='relu', kernel_initializer='he_normal'),
    # Decoder
    layers.Dense(16, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(32, activation='relu', kernel_initializer='he_normal'),
    layers.Dense(140, activation='sigmoid'),
])
```

Ne mutass két távoli réteget közvetlenül egymás alá írva teljes modellként.
A Dense-neuron az előző réteg értékeinek súlyozott összegéből számol. A rejtett
ReLU nemlinearitást ad. Az utolsó szigmoid 0–1 közötti rekonstruált amplitúdókat
ad; ezek nem osztályvalószínűségek. A `he_normal` a kezdeti súlyok beállítása;
most nem ennek hangolása a feladat.

```python
tanito_csomag = adatcsomag(tanito_jelek, tanito_jelek, keveres=True)
modell.compile(optimizer='adam', loss='mae', jit_compile=False)
tortenet = modell.fit(tanito_csomag, validation_data=validacios_csomag,
                     epochs=epochok_szama, shuffle=False, verbose=0, callbacks=[RovidJelzes()])
```

Az első sorban ugyanaz a jel a bemenet és a cél. Ez felel meg a notebook
`fit(adatok, adatok)` gondolatának; a kész segéd 32 mintás csomagokat készít.
Az Adam frissíti a súlyokat, a MAE a rekonstrukció eltérését méri. A `compile`
beállítja a tanítást, a `fit` végzi el. Az adatok keverését az adatcsomag intézi,
ezért a fit-ben nincs újabb keverés. Egy epochában mind az 512 tanítójel sorra
kerül: 16 darab, 32 mintás frissítés történik.

A külön 128 normál validációs jel nem frissít súlyt. Segít követni, hogyan
rekonstruál a hálózat a tanításban nem használt normál jeleket. A mentett
rekonstrukciós kép egy további, külön gyakorlójelre mutat példát.

Először a `G05_02_autoencoder.py` alapváltozatát futtasd: 10 epocha és 8-as
szűk keresztmetszet. Várd meg a FUTÁS KÉSZ részt, és küldd el a végső normál
validációs MAE-t és a 0. normál gyakorlópélda MAE-ját!

**A 30 epochás futás előtt:** a hálózat ugyanazt az adathalmazt többször járja
be. Új Run új modellt hoz létre ugyanabból a rögzített kezdetből. 30 epocha itt
összesen 30, nem a korábbi 10 után további 30. A több tanítás nem garantál javulást.
A görbén az epochátlag, az összefoglalóban az utolsó súlyokkal újramért tanítási
hiba szerepel; ezek kismértékben eltérhetnek.

## 3. Rekonstrukciós hiba – egy jelhez egy szám

Az előbb láttuk, hogy a hálózat görbéje eltérhet az eredetitől. Most ezt az
eltérést számmal is leírjuk, és normál, illetve rendellenes jeleken hasonlítjuk össze.
Ebben a programban nem tanítunk. Egy korábban, valóban lefuttatott 30 epochás
modell mellékelt rekonstrukcióit olvassuk. Ez a rögzített referencia nem a te
legutóbbi futásod; akkor is használható, ha a tanítást nem tudtad elvégezni.

```python
elteresek = normal_jelek - normal_vissza
abszolut_elteresek = np.abs(elteresek)
normal_hibak = np.mean(abszolut_elteresek, axis=1)
```

A kivonás pontonként kiszámítja az eredeti és a visszaállított jel különbségét.
Az `np.abs` az abszolút értéket veszi, ezért a pozitív és negatív eltérések
nem oltják ki egymást. Az `np.mean(..., axis=1)` a 140 pont eltéréseit átlagolja,
minden jelre külön. Így 128 jelből 128 hibaszám keletkezik. Az összes tengely
átlagolásával viszont csak egyetlen közös számot kapnánk.

A program külön, kétsoros szemléltető példát is tartalmaz:

```python
szemlelteto_elteresek = np.array([
    [0.1, 0.1, 0.3, 0.3],
    [0.4, 0.4, 0.4, 0.4],
])
sajat_atlagok = np.mean(szemlelteto_elteresek, axis=1)
kozos_atlag = np.mean(szemlelteto_elteresek)
```

Az első sor négy eltérésének átlaga 0,2, a másodiké 0,4. Az axis=1 minden soron
belül átlagol: két külön jelhez két külön eredmény, [0.2, 0.4]. Az axis nélküli
átlag mind a nyolc számot együtt kezeli, eredménye egyetlen 0,3. Az axis=1 tehát
nem az első jel kiválasztása. Az axis_1.png képen külön sorok és külön eredmények
látszanak. Ez a kis tömb mesterséges szemléltetés, a valódi EKG-adatok külön számolódnak.
Ugyanez a szabály a valódi (128,140) tömbnél 128 saját MAE-t ad. A MAE nem százalék.

A `minta_index` kijelöli, melyik normál és rendellenes jelet emeljük ki.
A `rekonstrukciok.png` ezeket mutatja, a `hibaeloszlas.png` viszont a teljes
128+128 példacsoport hibáit. A hisztogram vízszintes tengelyén hiba, függőleges
irányban darabszám van. A csoportok eltérhetnek, de átfedhetnek is.

Futtasd a `G05_03_rekonstrukcios_hiba.py` fájlt változtatás nélkül, és küldd el
a kiemelt normál és rendellenes jel MAE-ját! Utána együtt vizsgáljuk a görbéket.

**Indexváltás előtt:** magyarázd el itt is, hogy 3 a negyedik normál és negyedik
rendellenes példát emeli ki külön vizsgálatra (0 az első). Csak a kiemelt jel változik, a teljes csoport és annak
hisztogramja nem. Ne várj új tanulást vagy új modellből származó hibákat.

## 4. Küszöb – mitől lesz egy hiba riasztás?

Eddig a rekonstrukció hibáját számoltuk ki. Most szabályt adunk arra, mikor
jelezzünk rendellenességet. A hálózat és a hibaértékek változatlanok maradnak:
csak a döntési határt mozgatjuk. Ugyanazt a mellékelt referenciát használjuk,
mint az előző programban.

```python
kuszob = 0.04
normal_riasztas = normal_hibak >= kuszob
rendellenes_riasztas = rendellenes_hibak >= kuszob
```

Minden jelet a saját hibájával hasonlítunk a küszöbhöz. A határt elérő hiba is
riasztást jelent. A két logikai tömb True értékei azt mondják: a szabály szerint
rendellenesnek becsüljük a jelet. Ettől a valódi címkéje nem változik.

```python
teves_riasztas = int(np.sum(normal_riasztas))
helyes_rendellenes = int(np.sum(rendellenes_riasztas))
```

Az első sor megszámolja, hány valóban normál jelet jelzett a szabály: ezek téves
riasztások. A második a valóban rendellenes csoporton számol: ezek a helyesen
felismert rendellenességek. Amelyik rendellenes jelre nem riasztunk, azt elnéztük.
A kimenet mind a négy eset darabszámát kiírja, a `dontesek.png` táblázatként is
megmutatja őket. A `hibaeloszlas.png` függőleges vonala a döntési határ.

Ebben a gyakorlatban a pozitív osztály a rendellenes. A 0,04 egy összehasonlítási
alapbeállítás, nem általános orvosi határérték vagy minden modellre jó küszöb.

Futtasd a `G05_04_kuszob.py` alapváltozatát, és küldd el a négy darabszámot!
Először ezeket értelmezzük, utána térünk át a százalékos mutatókra.

**Precision és recall – külön magyarázat, külön kérdés:**

A mostani `precision_recall.png` felső sávja az összes riasztást mutatja.
A 0,06-os referencián 127 jelre riasztottunk: 121 jogos, 6 téves.
„A precision azt kérdezi: a riasztásaink mekkora része jogos?”
Előbb a darabszámok, utána precision = 121 / (121+6) = 121/127 ≈ 95,3%.
Kérdés: „Miért 127-tel osztunk itt?” Várd meg a választ, és tisztázd.

Az alsó sáv a valóban rendellenes jeleket mutatja. 128 ilyen jel van: 121-et
észleltünk, 7-et elnéztünk. „A recall azt kérdezi: a rendellenességek mekkora
részét találtuk meg?” Recall = 121 / (121+7) = 121/128 ≈ 94,5%.
Kérdés: „A hét elnézett jel miért része a recall kiinduló csoportjának?” Várj választ.

Ugyanaz a számláló (helyes észlelések), más nevező (riasztások vagy valódi
rendellenességek). A két kép sávjai darabszámot mutatnak, nem eleve 100%-ra nyújtott
hosszúságúak. A kimenet szövegesen is leírja a bontást. A saját futás értékeit használd.
Riasztás nélkül a precision nem értelmezhető; a program és az ábra is jelzi.
A definíciók elmondása után ne ugorj rögtön a zárótesztre: a két rövid válasz is szükséges.
