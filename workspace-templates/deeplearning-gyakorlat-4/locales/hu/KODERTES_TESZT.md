# Záró kódértési teszt – 10 kérdés

Mindegyik kérdésnél egy helyes válasz van. Válaszolj A, B, C vagy D betűvel.
Inno egyenként teszi fel a kérdéseket, megvárja az első válaszodat, majd
elmagyarázza a megoldást. Egy kérdés 1 vagy 0 pont, összesen 10 pont.
A későbbi javítás tanulás, nem változtatja meg az első válasz pontját.
Ha előzetes segítséget kérsz, azt külön jelezzük az értékelésben.

A kódrészleteknél a használt könyvtárak importját adottnak tekintjük.
Nem kell programot futtatni vagy pontos saját tanítási eredményeket felidézni.
Ez fogalmi önellenőrzés, nem a hálózat teszthalmazának értékelése.

## 1. kérdés – Egy súlyfrissítés

```python
suly = -1.0
tanulasi_rata = 0.1
gradiens = 2 * (suly - 3)
suly = suly - tanulasi_rata * gradiens
```

Mennyi a suly értéke a frissítés után?

A. −1,8
B. −0,2
C. 0,8
D. 3,0

## 2. kérdés – Momentum nélkül

```python
sebesseg = beta * sebesseg - tanulasi_rata * gradiens
hely = hely + sebesseg
```

Mi történik beta = 0 esetén?

A. A program nem változtatja a helyet.
B. A tanulási ráta automatikusan nulla lesz.
C. Minden korábbi gradiens azonos súllyal megmarad.
D. A korábbi sebesség hatása eltűnik; egyszerű gradienslépést kapunk.

## 3. kérdés – A ReLU kimenete

```python
bemenetek = np.array([-2.0, 0.0, 3.0])
kimenetek = np.maximum(0, bemenetek)
```

Mi lesz a kimenetek tartalma?

A. [0.0, 0.0, 3.0]
B. [-2.0, 0.0, 3.0]
C. [2.0, 0.0, 3.0]
D. [0.0, 0.0, 1.0]

## 4. kérdés – Sigmoid: kimenet és derivált

```python
z = 0.0
ertek = 1 / (1 + np.exp(-z))
derivalt = ertek * (1 - ertek)
```

Mennyi lesz a derivalt értéke?

A. 0,0
B. 0,5
C. 0,25
D. 1,0

## 5. kérdés – A regressziós hálózat

```python
modell = keras.Sequential([
    keras.Input(shape=(1,)),
    layers.Dense(64, activation="relu"),
    layers.Dense(1),
])
```

Melyik leírás helyes?

A. 64 bemeneti minta, majd egy osztályvalószínűség.
B. Mintánként egy bemeneti jellemző, 64 rejtett ReLU-neuron, egy lineáris kimenet.
C. Egy rejtett réteg 1 neuronnal és 64 kimeneti osztály.
D. 64 rejtett réteg, majd szigmoid kimenet.

## 6. kérdés – Hány tanítási frissítés?

```python
# A tanítóhalmaz 64 mintát tartalmaz.
# Az adatcsomag 16 mintás batch-eket ad.
# A fit egy epochát futtat végig.
```

Hány tanítási batch, így hány súlyfrissítés történik ebben az epochában?

A. 1
B. 16
C. 64
D. 4

## 7. kérdés – L2 és teljes veszteség

```python
sulyok = np.array([2.0, -1.0])
l2_erosseg = 0.01
mae = 0.12
buntetes = l2_erosseg * np.sum(sulyok ** 2)
teljes_loss = mae + buntetes
```

Mennyi lesz a teljes_loss?

A. 0,12
B. 0,05
C. 0,17
D. 0,62

## 8. kérdés – Mit hasonlítsunk össze?

```python
# Azonos validációs halmazon mért eredmények:
# A modell: val_loss = 0.21, val_mae = 0.21
# B modell: val_loss = 0.27, val_mae = 0.19
# A B modell vesztesége L2-büntetést is tartalmaz.
```

Melyik állítás helyes a becslési hibáról ezen a validációs halmazon?

A. B becslési hibája kisebb, mert a validációs MAE-je kisebb.
B. A becslési hibája biztosan kisebb, mert kisebb a teljes loss.
C. B-nek 27% az osztályozási hibaaránya.
D. A büntetés miatt a két modell MAE-je nem hasonlítható össze.

## 9. kérdés – Egy megtartott dropout-aktiváció

```python
bemenet = 0.8
maszk = 1
kiesesi_arany = 0.5
kimenet = bemenet * maszk / (1 - kiesesi_arany)
```

Mennyi a kimenet tanítási módban, ennél a megtartott elemnél?

A. 0,4
B. 1,6
C. 0,8
D. 0,0

## 10. kérdés – Dropout kiértékeléskor

```python
tanitasi_mod = False
bemenetek = np.array([0.2, 0.8, 1.0])

if tanitasi_mod:
    kimenetek = bemenetek * maszk / (1 - kiesesi_arany)
else:
    kimenetek = bemenetek.copy()
```

Mi történik az itt mutatott futásban?

A. A program minden elemet megkétszerez.
B. A program véletlenül nullázza a bemenetek felét.
C. A program új súlyokat tanít.
D. A kimenet [0.2, 0.8, 1.0], külön maszkolás és skálázás nélkül.
