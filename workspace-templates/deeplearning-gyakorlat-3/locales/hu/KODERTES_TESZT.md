# Záró kódértési teszt – 10 kérdés

Minden kérdéshez egy helyes válasz tartozik. Válaszolj A, B, C vagy D betűvel.
Inno egyenként mutatja a kérdéseket, megvárja a válaszodat, és utána elmagyarázza
az eredményt. Az első válasz kérdésenként 1 vagy 0 pont; összesen 10 pont.
A teszt a hálózat létrehozására, beállítására, tanítására és értékelésére épül.
Az R1–R4 kísérletek, a saját modellválasztás és a végső tesztábrák
megbeszélése után kezdődik. A kérdésekben szereplő műveleteket előtte feldolgozzuk.

## 1. kérdés – A bemenet jelentése

```python
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

Mit jelent itt a `shape=(2,)`?

A. Egy futásban pontosan két mintát lehet feldolgozni.
B. Minden bemeneti minta két jellemzőt tartalmaz.
C. A modellnek két kimeneti osztálya van.
D. A hálózat két rejtett réteget tartalmaz.

## 2. kérdés – A hálózat rétegei

```python
modell = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(50, activation="relu"),
    layers.Dense(50, activation="relu"),
    layers.Dense(3, activation="softmax"),
])
```

Melyik leírás felel meg ennek a modellnek?

A. Egy rejtett réteg 100 neuronnal, majd 3 kimenet.
B. Három rejtett réteg, az utolsóban 3 neuron.
C. Két rejtett réteg, egyenként 50 neuronnal, majd 3 kimenet.
D. Két rejtett réteg, egyenként 3 neuronnal, majd 50 kimenet.

## 3. kérdés – Helyes cél–kimenet–veszteség párosítás

```python
tanito_cel = keras.utils.to_categorical(tanito_cimke, num_classes=3)
# Egy célvektor például: [0, 0, 1]
```

Három egymást kizáró osztályhoz melyik kimenet és veszteség illik közvetlenül
az így előállított célvektorokhoz?

A. `Dense(3, activation="softmax")` és `loss="categorical_crossentropy"`.
B. `Dense(3, activation="softmax")` és `loss="sparse_categorical_crossentropy"`.
C. `Dense(1, activation="sigmoid")` és `loss="binary_crossentropy"`.
D. `Dense(2, activation="softmax")` és `loss="categorical_crossentropy"`.

## 4. kérdés – Mikor tanul a modell?

```python
modell.compile(optimizer="adam", loss="categorical_crossentropy",
                metrics=["accuracy"])
tortenet = modell.fit(tanito_x, tanito_cel, epochs=10)
eredmeny = modell.evaluate(validacios_x, validacios_cel)
becsles = modell.predict(validacios_x[:5])
```

Melyik hívás végzi a tanulás során a súlyok és biasok frissítését?

A. A `compile`.
B. Az `evaluate`.
C. A `predict`.
D. A `fit`.

## 5. kérdés – Epoch és batch

```python
# tanito_x és tanito_cel pontosan 360 mintát tartalmaz.
modell.fit(tanito_x, tanito_cel, epochs=1, batch_size=32)
```

Alapértelmezett működés mellett, a rövid utolsó batch megtartásával hány
batch-et dolgoz fel ebben az egy epochban?

A. 11-et; az utolsó 8 minta kimarad.
B. 12-t; az utolsó batch 8 mintát tartalmaz.
C. 32-t; ezt írja elő a `batch_size`.
D. 360-at; minden minta önálló batch.

## 6. kérdés – A tanulási ráta hatása

```python
suly = 1.0
suly_gradiense = -4.0
TANULASI_RATA = 0.1
suly = suly - TANULASI_RATA * suly_gradiense
```

Mennyi lesz a súly az egyetlen kiírt frissítés után?

A. 0.6
B. -0.4
C. 1.1
D. 1.4

## 7. kérdés – Becsült osztályok

```python
valoszinusegek = np.array([
    [0.10, 0.70, 0.20],
    [0.80, 0.15, 0.05],
])
becsult = valoszinusegek.argmax(axis=1)
```

Mi a `becsult` tartalma, ha az osztályindexek 0-tól indulnak?

A. `[1, 0]`
B. `[0.70, 0.80]`
C. `[2, 1]`
D. `[1, 0, 0]`

## 8. kérdés – A validáció szerepe

```python
modell.fit(
    tanito_x, tanito_cel,
    validation_data=(validacios_x, validacios_cel),
    epochs=150,
)
```

Melyik állítás írja le helyesen a `validation_data` szerepét ebben a hívásban?

A. A tanítóadatokkal együtt közvetlen súlyfrissítésre szolgál.
B. Automatikusan lecseréli a kijelölt tanítóadatokat.
C. Epochonként ellenőrző mérést ad, közvetlen súlyfrissítés nélkül.
D. Automatikusan megállítja a tanítást az első rosszabb eredménynél.

## 9. kérdés – Veszteség és pontosság

```python
# Egy mintán, a cél: [0, 1, 0]
elso_becsles = np.array([0.10, 0.60, 0.30])
masodik_becsles = np.array([0.10, 0.80, 0.10])
```

Mi történik ezen az egy mintán a categorical crossentropy veszteséggel és
az argmax alapján számított helyes/hibás döntéssel a második becslésre váltva?

A. A veszteség nő, a döntés hibássá válik.
B. A veszteség csökken, a döntés mindkét esetben helyes.
C. A veszteség változatlan, a döntés hibásból helyessé válik.
D. A veszteség csökken, a döntés mindkét esetben hibás.

## 10. kérdés – A végső teszt

```python
modell = keras.models.load_model(mappa / "modell.keras")
eredmeny = modell.evaluate(teszt_x, teszt_cel, verbose=0, return_dict=True)
```

A modellt már a validáció alapján kiválasztottuk. Mit tesz ez a két sor?

A. Új véletlen súlyokkal újratanítja a modellt a tesztmintákon.
B. A tesztpontosság alapján automatikusan kiválasztja a legjobb futást.
C. Betölti a mentett modellt, majd súlyfrissítés nélkül méri a tesztadatokon.
D. Folytatja a tanítást a korábbi utolsó epochtól.
