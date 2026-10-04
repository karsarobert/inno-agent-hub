# Rövid ismétlő lap – autoencoder és EKG

| Fogalom / kód | Mit jelent itt? |
|---|---|
| Egy jel | 140 skálázott érték, az időbeli sorrend megőrzésével. |
| `minta_index` | A megjelenített példa sorszáma, nullától. |
| Encoder | A 140 bemeneti értéket kisebb belső reprezentációvá alakító hálózatrész. |
| Bottleneck | Szűk keresztmetszet; az alapmodellben 8 érték. |
| Decoder | A belső reprezentációból 140 rekonstruált értéket állít elő. |
| `Dense` | Teljesen összekötött réteg; minden neuron az előző réteg összes kimenetét használja. |
| ReLU | A negatív összegzett bemenetből nulla lesz, a pozitív átjut. |
| Kimeneti sigmoid | 0–1 közötti amplitúdót ad minden mintapontra, nem osztályvalószínűségeket. |
| Bemenet = cél | Visszaállításra tanítunk, ezért ugyanazt a jelet szeretnénk visszakapni. |
| `compile` | Beállítja az optimalizálót és a veszteséget. |
| `fit` | A veszteség alapján módosítja a modell súlyait. |
| Epocha | A teljes tanítóhalmaz egyszeri bejárása. |
| Batch | Egy frissítéshez használt mintacsoport; itt 32 jel. |
| Validáció | Külön adatokon végzett mérés, súlyfrissítés nélkül. |
| MAE | Az eredeti és rekonstruált értékek abszolút eltéréseinek átlaga. |
| `axis=1` | A jel pontjainak tengelyén átlagolunk, jelenként külön hibát kapunk. |
| `hiba >= kuszob` | Riasztás, azaz rendellenesnek becsült jel. Az egyenlőség is riaszt. |
| TP | Valóban rendellenes, és riasztottunk. |
| FN | Valóban rendellenes, de nem riasztottunk. |
| FP | Valóban normál, de riasztottunk: téves riasztás. |
| TN | Valóban normál, és nem riasztottunk. |
| Precision | TP/(TP+FP): a riasztások közül valóban rendellenes. |
| Recall | TP/(TP+FN): a rendellenesek közül észlelt. |

## Három fontos különbség

**Hiba és döntés:** a rekonstrukció hibája folytonos szám. A küszöb alakítja döntéssé.
A határ módosítása nem tanítja újra és nem javítja meg a hálózatot.

**Saját futás és referencia:** G02 a saját futásban tanít; G03 és G04 a csomaghoz
mellékelt 30 epochás modell kimeneteit vizsgálja. A referencia eredete a futás elején látszik.

**Jó rekonstrukció és jó anomáliaészlelés:** ha a modell a rendellenes jeleket is
nagyon jól állítja vissza, a kis hiba önmagában nem segít őket megkülönböztetni.
Ezért a csoportok hibaeloszlásai és a téves döntések is számítanak.


## Két sor, két saját hiba

| Jel | Szemléltető abszolút eltérések | Saját átlag |
|---|---|---|
| 1. | 0,1; 0,1; 0,3; 0,3 | 0,2 |
| 2. | 0,4; 0,4; 0,4; 0,4 | 0,4 |

`axis=1` → [0.2, 0.4], tehát két külön hiba. `axis` nélkül → 0.3, egyetlen közös átlag.
A valódi 128 jelhez ugyanígy 128 külön MAE tartozik.

## Ugyanaz a helyes észlelés, más kiinduló csoport

A 0,06-os referenciafutásnál:
- Precision: **127 riasztás** = 121 jogos + 6 téves. 121/127 ≈ 95,3%.
- Recall: **128 valódi rendellenesség** = 121 észlelt + 7 elnézett. 121/128 ≈ 94,5%.

Először mindig nevezd meg, melyik csoportból indulsz! A számláló mindkettőnél a 121.
