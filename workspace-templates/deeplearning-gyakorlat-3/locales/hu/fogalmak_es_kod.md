# Fogalmak és kód – gyors emlékeztető

| Fogalom | Kód / jelentés |
|---|---|
| Bemenet | `Input(shape=(2,))`: egy pont két koordinátája |
| Cél | Ismert osztály, például 2; one-hot alakban [0,0,1] |
| Súly és bias | A hálózat tanulható paraméterei |
| Rejtett réteg | `Dense(50, activation="relu")`: 50 tanult köztes jellemző |
| ReLU | Negatív bemenetből 0, nemnegatívból önmaga |
| Softmax | Három egymást kizáró osztályhoz három, 1-re összegződő becslés |
| Tanulási ráta | `Adam(learning_rate=0.01)`: az optimalizáló lépésskálája |
| Konfigurálás | `compile`: optimalizáló, veszteség, metrikák |
| Tanítás | `fit`: súlyok és biasok frissítése tanítópárokból |
| Epoch | A teljes tanítóhalmaz egyszeri feldolgozása |
| Batch | Egy frissítéshez felhasznált mintacsoport |
| Validáció | Ellenőrzés és beállításválasztás, közvetlen súlyfrissítés nélkül |
| Veszteség | A tanítással csökkentett eltérés; itt keresztentrópia |
| Pontosság | Helyesen osztályozott minták aránya |
| Becslés | `predict`: osztályonkénti értékek, súlyfrissítés nélkül |
| Osztályindex | `argmax(axis=1)`: a legnagyobb érték helye minden mintánál |
| Mérési eredmény | `evaluate`: veszteség és metrikák, súlyfrissítés nélkül |
| Teszt | A választás lezárása utáni ellenőrzés félretett adatokkal |
| Nézet frissítése | A már elkészült új fájlokat láthatóvá teszi a fájllistában |

360 minta és 32-es batch: 12 frissítés epochonként, az utolsó batch 8 minta.
A ráta/epoch/batch/neuronszám hiperparaméter, a súly/bias tanult paraméter.
Több epoch vagy nagyobb hálózat nem biztosít automatikusan jobb validációt.


A `[0,0,1]` one-hot célhoz categorical_crossentropy, a `2` egész címkéhez
sparse_categorical_crossentropy illik, mindkettő három softmax-kimenettel.
A loss a helyes osztály valószínűségét is figyelembe veszi; az accuracy a
helyes döntések aránya. Ezért a két mutató eltérően is rangsorolhat modelleket.
A 100% kizárólag az adott mért mintahalmazra vonatkozik, nem garancia minden új pontra.

A kötelező rátakísérletben az 50–50 hálózaton csak 0.01 → 0.001 változik.
Az összes R1–R4 futásból a kisebb validációs veszteség szabályával választunk;
pontos egyezésnél a kevesebb paraméter dönt. A saját indokot a teszt előtt írjuk le.
