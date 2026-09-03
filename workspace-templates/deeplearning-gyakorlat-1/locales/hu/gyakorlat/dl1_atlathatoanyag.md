# DL 1 — Kulcsfogalmak áttekintése (1 oldal)

## A neurális hálózat képben

```
Bemenet (adat)           Réteg                Kimenet (osztály)
┌──────────────┐  súlyok →  ┌──────────────┐  →  ┌──────────────┐
│ 28×28 kép    │   w, b     │ Dense(10)    │     │ 0,1,2,…,9    │
│ = 784 vektor │  ──────►   │ softmax      │ ──► │ (valószínűség)│
└──────────────┘            └──────────────┘     └──────────────┘
```

## A történet rövid íve

- **1958 — Perceptron** (Rosenblatt): az első egyszerű egység, súlyokkal tanul.
- **MLP (többrétegű hálózat)**: több réteg összekapcsolása → bonyolultabb feladatok.
- **A mély tanulás újjászületése**: több rejtett réteg, nagy számítási kapacitás.
- **Napjaink**: a képek, szövegek, hang feldolgozása — erre épül a kurzus többi része.

## Az alapfogalmak

| Fogalom | Mit jelent, az MNIST példán |
|---|---|
| **Adat** | a példák halmaza (60 000 tanuló + 10 000 teszt kép) |
| **Jellemző** | amiből a modell tanul (a 784 pixelérték mint vektor) |
| **Felügyelet** | ismerjük a helyes címkét (a számjegy 0-9) a tanításnál |
| **Modell** | a rétegek + súlyok együttese (a `Sequential` háló) |
| **Tanítás** | a `fit` során a súlyok igazítása a hiba alapján |
| **Osztályozás** | a modell kimenete: a 10 számjegy osztálya |

## Az adat-előkészítés lépései (a kódban)

```
betöltés → reshape(60000,784) → astype(float32) → /255 → to_categorical
```

| Lépés | Kód | Miért? |
|---|---|---|
| Betöltés | `mnist.load_data()` | 60 000 tanuló + 10 000 teszt kép (28×28) |
| Alakítás | `reshape(60000, 784)` | a Dense-réteg **vektort** vár, nem 2D képet |
| Típusváltás | `astype('float32')` | folytonos számok, jobb számítás |
| Normalizálás | `X /= 255` | értékek 0.0–1.0-ba; stabilabb tanulás |
| One-hot | `to_categorical(Y, 10)` | a címke vektorrá válik az osztályozáshoz |

## Kulcsfogalmak

- **Epoch**: hányszor megy a modell a **teljes** adathalmazon keresztül.
- **Batch**: hány minta egy „lépésben", mielőtt a súly frissül (pl. 128).
- **Softmax**: a kimenő réteg aktivációja → 10 valószínűség, összeg 1.
- **Veszteség (loss)**: mennyire rosszul tippel a modell; a tanulás ezt csökkenti.
- **Adam**: optimalizáló, amely a súlyokat igazítja a veszteség alapján.

> A **túltanulást** (és a tanulási görbék alapos elemzését) a kurzus későbbi
> tematikája tárgyalja — az 1. alkalommal csak a fő lépéseket látjuk.

*Segédanyag a Deep Learning 1. gyakorlathoz — a `dl1_megoldott.py` mellett.*