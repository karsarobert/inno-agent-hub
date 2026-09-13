# A red-wine.csv eredete

A mellékelt fájl a kurzus nyilvános adattárából származik:
[DeepLearning2026 – red-wine.csv](https://raw.githubusercontent.com/karsarobert/DeepLearning2026/main/red-wine.csv).
Letöltés: 2026. szeptember 13. A mellékelt CSV-t nem módosítottuk.

Az eredeti adatforrás: **Cortez, P., Cerdeira, A., Almeida, F., Matos, T.,
& Reis, J. (2009). Wine Quality. UCI Machine Learning Repository.**
DOI: [10.24432/C56S3T](https://doi.org/10.24432/C56S3T).

[UCI adatlap](https://archive.ics.uci.edu/dataset/186/wine+quality).
Az adatlap licence: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
Az adatok portugál vörös- és fehérbor-vizsgálatokból származnak; ez a fájl
az **1599 vörösboros megfigyelést** tartalmazza. A 11 fizikai-kémiai
jellemzőből a `quality` minőségi pontszámot becsüljük.

## A példákban végzett előkészítés

- Az eredeti fájl 1599 sort és 12 oszlopot tartalmaz; nincs hiányzó érték.
- A programok a 240 ismétlődő teljes sort eltávolítják: 1359 különböző sor marad.
- A választott seed mellett 815 tanító-, 272 validációs és 272 tesztminta keletkezik.
- Az azonos sorok egyszeri felhasználása oktatási döntés: így ugyanaz a teljes
  megfigyelés nem kerül több halmazba. Ez nem jelenti azt, hogy minden valós
  adatfeladatban minden ismétlődő sor hibás lenne.
- A skálázó paramétereit csak a tanítóhalmazból számítjuk.

Fájlméret: 100951 bájt. SHA-256:

```text
d6a0d9bd24806944818795f22500c46cb6424cbff517aacda36595d3ed9b2daa
```
