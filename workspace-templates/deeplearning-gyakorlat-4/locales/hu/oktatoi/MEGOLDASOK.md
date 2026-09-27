# Tanári megoldások és értelmezési támpontok

A hallgatói fájlok működő alapváltozatok. A megoldás a kijelölt beállítás
átírása, az új futás és a tényleges eredmény értelmezése. Az alábbi értékeket
nem kell egyetlen nagy blokkban a hallgató elé tenni. Az agent mindig csak
az aktuális kísérlethez adjon segítséget.

## 1. Tanulási ráta

| Futás | tanulasi_rata | lepesek_szama | Mihez hasonlítjuk? |
|---|---:|---:|---|
| R1 | 0.1 | 8 | Kezdőállapothoz |
| R2 | 0.8 | 8 | R1-hez |
| R3 | 1.1 | 8 | R1/R2-höz |
| R4 | 0.1 | 25 | R1-hez, azonos ráta mellett |

R1-ben egy oldalról közelítünk a minimumhoz. R2-ben az eltérés előjele váltakozik,
de a nagysága csökken. R3-ban a kilengés nő. R4 azt mutatja, hogy a korábbi
kis lépéssel több frissítés után közelebb jutunk.

Ellenőrző összefüggés az oktatónak: `w_t - 3 = (w_0 - 3) * (1 - 2*eta)**t`.
Ez a konkrét másodfokú függvényre igaz, nem tetszőleges hálózat tanulási garanciája.
A program számai és a kézi első lépés ezzel ellenőrizhetők.

## 2. Momentum

Az alapérték `momentum = 0.9`, a módosított érték `momentum = 0.0`.
A ráta 0.1, a lépésszám 40 marad. Nulla momentum mellett a két útvonal,
végpont és veszteség egyezik, mert a két frissítési szabály azonossá válik.
A 0.9-es útvonal átléphet a minimum túloldalára. Az oszcilláció önmagában
nem jelent hibás algoritmust, és a momentum nem garantáltan jobb minden helyzetben.

## 3. Aktivációk

| Futás | Aktiváció | Bemeneti szélek | Negatív meredekség |
|---|---|---|---:|
| A1 | `sigmoid` | −6 és 6 | nincs szerepe |
| A2 | `sigmoid` | −8 és 8 | nincs szerepe |
| A3 | `relu` | visszaállítva −6 és 6 | nincs szerepe |
| A4 | `leaky_relu` | −6 és 6 | 0.1 |
| A5 | `leaky_relu` | −6 és 6 | 0.2 |

A középső bemenetek mindenütt −1, 0 és 1. A sigmoid kimenete 0-nál 0,5,
deriváltja 0,25; a beérkező 2-es gradiensből így 0,5 halad tovább.
6-nál a sigmoid deriváltja kb. 0,00247, 8-nál kb. 0,000335: a telítődésben
kicsi helyi változás jut vissza. A sigmoid kimenete itt közelebb kerül 1-hez,
miközben a deriváltja csökken; a két mennyiség nem azonos.

−1 bemenetnél ReLU: kimenet 0, derivált 0. Leaky ReLU 0,1-es meredekséggel:
kimenet −0,1, derivált 0,1, visszaadott gradiens 0,2. 0,2-es meredekséggel:
kimenet −0,2, derivált 0,2, visszaadott gradiens 0,4.
A nullabeli töréspont konvencióját röviden jelezzük, de nem vizsgáztatjuk a szubgradiens fogalmát.

## 4. Kis hálózat

```python
# H1: kiinduló állapot
REJTETT_NEURONOK = 8
EPOCHOK = 120

# H2: csak a neuronszám változik H1-hez képest
REJTETT_NEURONOK = 64
EPOCHOK = 120

# H3: csak a tanítási idő változik H2-höz képest
REJTETT_NEURONOK = 64
EPOCHOK = 400
```

Ezek külön futások beállításai, nem egymás alá bemásolandó teljes kód.
A ráta 0.01, batch=16, mag=42 marad. A képen az adatgenerátor zaj nélküli
görbéje referencia, a hálózat a zajos tanítócélokat kapta.

A tanuló a két végső MAE-t és a görbéket hasonlítja. A 64 neuronos hálózatnak
193 paramétere van a 8 neuronos 25 paraméterével szemben, de ettől a validáció
nem feltétlenül lesz jobb. A hosszabb tanítás után kisebb tanítási és nagyobb
validációs hiba túlillesztésre utalhat; egyetlen kis különbségből nem állítunk általános törvényt.

A tanítási görbe epochátlaga és a tanítás végén az utolsó súlyokkal újramért
MAE nem kötelezően egyezik. A validációs görbe minimuma nem a megtartott állapot,
mert nincs korai leállítás vagy legjobbállapot-visszaállítás.

## 5. L2

| Futás | L2_EROSSEG | Rejtett neuron | Epocha |
|---|---:|---:|---:|
| REG0 – büntetés nélkül | 0.0 | 64 | 120 |
| REG1 – enyhe büntetés | 0.001 | 64 | 120 |
| REG2 – erős büntetés | 0.05 | 64 | 120 |

A hálózat nem a 400 epochás H3-at folytatja. Minden futás újraindul azonos
kezdeti súlyokról; a kiírt kezdeti azonosító ugyanaz H2/H3/REG0/REG1/REG2 esetén.
REG0 azonos adatkezelés és környezet mellett reprodukálja a H2 eredményét.

Mindkét Dense-kernelre `kernel_regularizer=regularizers.l2(L2_EROSSEG)` kerül.
A biasok nem regularizáltak. A kiírt kernel-négyzetösszeg λ-szorosa a büntetés,
és `validacios_loss_vegso = validacios_mae_vegso + l2_buntetes`.
λ=0 esetén a két mennyiség egybeesik.

A nagyobb λ csökkentheti a súlyok méretét, de túl erősen korlátozhatja a modellt.
Az eltérő λ-val számolt loss nem azonos mérce a becslési minőség összehasonlítására;
erre az ugyanazon adatokon mért MAE-t használjuk. A képen a növekvő büntetési
különbség és a javuló MAE egyszerre is megjelenhet.

## 6. Dropout

| Futás | kiesesi_arany | veletlen_mag | tanitasi_mod |
|---|---:|---:|---|
| D1 | 0.5 | 42 | `True` |
| D2 | 0.25 | 42 | `True` |
| D3 | 0.25 | 43 | `True` |
| D4 | 0.25 | 43 | `False` |

D1-ben a megtartott értékek kétszeresek, D2/D3-ban 4/3-szorosak.
D2 ugyanazokat a véletlen számokat használja kisebb küszöbbel: az előzőleg
megtartott elemek megmaradnak, és további elemek is megmaradhatnak.
D3 új mintát készít; ugyanazon arány nem ír elő azonos kieső helyeket vagy darabszámot.
D4 minden bemeneti értéket változatlanul továbbad. A maszkolás nem súlytörlés.

Egy véletlen maszk mintájának átlaga nem kötelezően egyezik a bemeneti átlaggal.
Az inverted dropout az egyes aktivációk várható értékét őrzi meg. A fix mag
miatt ugyanaz a program ugyanabban a környezetben ismételve ugyanazt adja;
ez nem a valódi tanítás minden batch-én újraindított véletlengenerátort jelent.

## Opcionális fájlok

Softmax: `[2,1,0]` esetén kb. `[0.665241,0.244728,0.090031]`.
`kozos_eltolas = 1000.0` mellett az arányok ugyanazok, a stabil számítás nem csordul túl.
A kimenetek összege 1. Egyetlen logit változtatása ezzel szemben általában minden arányt módosít.

BN: `[1,2,3,4]` átlaga 2,5, a `1/m` szerinti variancia 1,25.
ε=0,001 mellett a normalizált értékek kb. `[−1.3411,−0.4470,0.4470,1.3411]`.
gamma=2, beta=1 ezeket skálázza és eltolja. Az ε miatt a variancia nem pontosan 1.
Kiértékelési módban a tárolt átlag és variancia marad használatban akkor is,
ha a bemenetet például `[2,3,4,5]`-re cseréljük. A statisztikák itt szemléltető értékek.

## A tutor értékelése

Elfogadható a „nem javult”, „alig változott” vagy „nem egyértelmű” válasz,
ha a hallgató a saját kimenetével alátámasztja. Ne várjunk pontos tanári
referenciaszámokat, és ne vezessük a tanulót előre eldöntött győzteshez.
A teszt részletes kulcsa az OKTATOI_MEGOLDOKULCS.md fájlban van.
