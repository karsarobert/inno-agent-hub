# Források és tudatos egyszerűsítések

## A felhasználó anyagai

- PTE_DL5_ECG.ipynb: a Dense-autoencoder és az EKG-rekonstrukciós feladat alapja.
- DL_05.html: az autoencoderrel kezdődő elméleti tananyag; nem futási függőség.
- A korábbi DL04 Innoagent-csomag: a tutori menet, az rövid, sorszámozott ábramentés,
  CPU-s adagszervezés és záróteszt formátuma.

## Adatforrás

Az ECG5000-adatcsalád TensorFlow-tananyaghoz előkészített binárisan címkézett CSV-je:
https://storage.googleapis.com/download.tensorflow.org/data/ecg.csv

Leírás és kapcsolódó bemutató:
https://www.tensorflow.org/tutorials/generative/autoencoder

Eredeti adatgyűjtemény:
https://www.timeseriesclassification.com/description.php?Dataset=ECG5000

A csomagkészítéskor letöltött CSV ténylegesen 4998 sorból és 141 oszlopból állt
(a család neve ECG5000). 140 jelérték után a címke következik: 1 normál, 0 rendellenes.
A CSV ellenőrzőösszege és a kiválasztás adatai az `adatok/adatleiras.json` fájlban vannak.
A nyers CSV nincs a csomagban; csak a 896 kiválasztott, skálázott jel és azok forrássor-indexei.

Kiválasztás: NumPy `default_rng(2026)`, a normál és rendellenes sorindexek külön
permutációja. Normál: első 512 tanító, következő 128 validációs, következő 128
megfigyelési; rendellenes: első 128 megfigyelési. A különböző részek sorindexei
diszjunktak. Ez nem jelent külön betegeken végzett klinikai validációt: a CSV-ből
ilyen betegszintű felosztást nem igazolunk.

Skálázás: a 512 normál tanítójel közös minimuma és maximuma; ugyanaz a lineáris
transzformáció minden részhalmazon. Float32, nincs levágás. Az új jelek kilóghatnak
0–1-ből, miközben a modell szigmoidja csak ezen belül ad kimenetet.

## Eltérések a teljes notebooktól

Kisebb helyi adathalmaz, rövidebb CPU-s tanítás, külön normál validáció, kész ábramentés.
A modell felépítése megmarad: 140–32–16–8–16–32–140; rejtett ReLU + he_normal,
kimeneti sigmoid, Adam (alap tanulási ráta 0.001), MAE. A tömböket egy kész segéd
32-es, egy háttérszálas adatcsomagokra bontja; ettől a bemenet=cél tanítás nem változik.

A küszöbös feladat kézzel állítható határral dolgozik, hogy a döntési kompromisszum
látható legyen. Nem számít automatikusan átlag+2 szórás küszöböt. A referencia
rekonstrukciói valódi 30 epochás futásból származnak, nem mesterségesen tervezett hibák.
G03/G04 függetlenül használható, de mindig ezt a referenciát olvassa.

## Dokumentáció

- Keras tanítási API: https://keras.io/api/models/model_training_apis/
- TensorFlow adathalmazok: https://www.tensorflow.org/api_docs/python/tf/data/Dataset
- NumPy átlag: https://numpy.org/doc/stable/reference/generated/numpy.mean.html

Az adatok forrását a fenti hivatkozások őrzik; nem állítunk saját szerzőséget az
EKG-adatokra, és nem rendelünk hozzájuk a forrástól eltérő új licencet.
A TensorFlow oktatókódjának licenchivatkozása: Apache License 2.0.
A kapcsolódó licencszöveg `oktatoi/APACHE-2.0.txt`; a programok a feladathoz
átdolgozott, magyar változatok. A kódbeli módosításokat és a paramétereket fent rögzítettük.
