# Fogalmi és kódmagyarázati támasz a tutor számára

Csak az aktuális cellához szükséges részletet tanítsd. Ne olvasd fel ezt a fájlt.

## Adat és alak

- `(N, F)`: Nmintát, mintánként Fjellemzőt tárolunk. A shape nem magyarázza meg önmagában az oszlopok jelentését.
- `X[i]`egy sort 1Dvé tehet; `X[i: i+1]`megtartja az egymintás 2Dalakot. Az indexelés 0 alapú.
- `float 32`lebegőpontos adattípus. A skálázást és a típusváltást ne nevezd ugyanannak.
- `reshape(-1, F)`a teljes elemszám megőrzésével új alakot készít; a-1 a hiányzó méret kiszámítását kéri.
- `np.mean(..., axis=1)`kétdimenziós tömbben soronként átlagol, az oszlopok dimenzióját összegezve.
  Ha rekonstrukciós különbségünkN×F, a kimenetNelemű hibasorozat lesz.

## Skálázás és elkülönítés

MinMaxScaler minden jellemzőhöz saját minimumot/maximumot tanul. Fit_transform csak a tanítóadaton;
transform a többi adaton ugyanazzal az objektummal. Az új adat kilóghat 0..1-ből.
Az előre ismert 255-tel osztás nem ugyanaz, mint teljes adathalmazból becsült maximum használata.
A tanító adat közvetlen súlyfrissítést ad, a validáció beállítás/kiválasztás eszköze, a teszt végső mérés.
A kalibráció a küszöb rögzítésére szolgál; nem a teszt optimalizálására.

## A három modell

| Feladat | Bemenet | Cél | Kimenet | Veszteség |
|---|---|---|---|---|
| Lakásérték |13 jellemző|1 valós szám|1 lineáris|MAE|
| MNIST |784 képpont|10 elemű one-hot|10 softmax|categorical_crossentropy|
| Autoencoder |5 szám|ugyanaz az 5 szám|5 sigmoid|MSE|

Compile konfigurál, fit tanít, evaluate mér, predict kimenetet készít. Predict önmagában nem számít
hibát, mert nem adunk hozzá célértéket. Softmax-kimenetből argmaxszal lesz osztályindex.
Az autoencoder outputja nem csalási valószínűség; hibájából később bináris döntést készítünk.

## Tanulás

Batch=egy frissítés mintacsoportja; epoch=egy teljes áthaladás. A maxepochs felső korlát.
Az EarlyStopping monitorja a val_loss. Patience egymást követő javulás nélküli epochokat számol;
restore_best_weights a kiválasztott állapotot állítja vissza. A legkisebb nyers val_loss és a
min_delta alapján kiválasztott legjobb epoch nem feltétlenül pontosan ugyanaz.
Egy másodikfit ugyanazon modellen folytatódik; friss összehasonlításhoz új modellt építünk.
Dropout tanítás közben aktív, értékeléskor és jóslatkor nem. A görbék helyzetéből önmagában ne
állíts adatszivárgást vagy garantált túlilleszkedést; konkrét mintázatot vizsgálj.

## Metrikák

MAE: abszolút eltérések átlaga, a cél egységében. Nem százalék és nem minden egyes minta hibája.
Accuracy: a helyes osztálydöntések aránya. A keresztentrópia a helyes címkére jutó kimeneti értékre is érzékeny.
Bináris mátrix`[[TN, FP], [FN, TP]]`, ha a címkesorrend[0, 1]. Itt pozitív az anomália 1.
Precision=TP/(TP+FP): a riasztások közül mennyi valódi. Recall=TP/(TP+FN): a valódiakból mennyi lett megtalálva.
Nulla nevezőnél a report 0 értéke formázási/definiálási döntés, nem bizonyított modellminőség.
A kis anomáliateszt miatt a becslések bizonytalanok; konkrét általánosíthatósági ígéretet ne tegyél.

## Ábrák tanítása

Előbb mondd el a tengelyeket és a görbék jelentését, majd egy konkrét megfigyelést kérj.
Tévesztési mátrixnál valódi címke+becsült címke+darabszám a válasz. Hibaeloszlásnál a
normál/anomália átfedést és a rögzített küszöb jelentését értelmeztesd. Nem látott ábráról
csak a hallgató konkrét leírására támaszkodhatsz. Az oldalfrissítés nem számol új adatot.
