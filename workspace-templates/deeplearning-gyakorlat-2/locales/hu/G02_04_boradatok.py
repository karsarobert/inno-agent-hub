"""A borminőség becslésének adat-előkészítése.

Egy sor egy borminta. A 11 mért tulajdonság a bemenet, a quality a cél.
Beolvasás → azonos sorok egyszer → három halmaz → skálázás.
Ez a program még nem épít és nem tanít hálózatot.
Részletes kódbemutatás: PROGRAM_BEMUTATOK.md.
Szemléltetés: szemlelteto.html (böngészőben megnyitható).
"""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

print('A borminőség becslésének adat-előkészítése.')
print('Egy sor egy borminta. A 11 mért tulajdonság a bemenet, a quality a cél.\nBeolvasás → azonos sorok egyszer → három halmaz → skálázás.\nEz a program még nem épít és nem tanít hálózatot.')

VELETLEN_MAG = 42
adatfajl = Path(__file__).resolve().parent / "adatok" / "red-wine.csv"
nyers_adatok = pd.read_csv(adatfajl)

# Azonos teljes sorokat ebben az oktatási példában egyszer szerepeltetünk.
adatok = nyers_adatok.drop_duplicates().reset_index(drop=True)
# Egy valódi sor rövid bemutatása: a pontszámot nem tesszük a bemenetbe.
print("Egy borminta nehany bemenete es az ismert cel:")
print(adatok.loc[[0], ["alcohol", "pH", "sulphates", "quality"]].to_string(index=False))
print("A harom bemutatott jellemzon kivul meg nyolc bemenetet hasznalunk.")
jellemzok = adatok.drop(columns=["quality"])
celertekek = adatok["quality"]

tanulo_resz, teszt_jellemzok, tanulo_cel, teszt_cel = train_test_split(
    jellemzok, celertekek, test_size=0.2, random_state=VELETLEN_MAG
)
tanito_jellemzok, validacios_jellemzok, tanito_cel, validacios_cel = train_test_split(
    tanulo_resz, tanulo_cel, test_size=0.25, random_state=VELETLEN_MAG
)

# A minimumot és maximumot kizárólag a tanítóadatokból tanuljuk meg.
skalazo = MinMaxScaler()
tanito_skala = skalazo.fit_transform(tanito_jellemzok)
validacios_skala = skalazo.transform(validacios_jellemzok)
teszt_skala = skalazo.transform(teszt_jellemzok)

print("Nyers adatok alakja:", nyers_adatok.shape)
print("Kihagyott azonos sorok:", len(nyers_adatok) - len(adatok))
print("Elso ket adatsor:")
print(adatok.head(2).to_string(index=False))
print("Jellemzok szama:", jellemzok.shape[1])
print("Tanito / validacios / teszt mintak:",
      len(tanito_cel), len(validacios_cel), len(teszt_cel))
print("Tanito bemenet alakja:", tanito_skala.shape)
print("Elso tanitominta elso harom skalazott jellemzoje:", tanito_skala[0, :3])
print("Ehhez tartozo cel:", tanito_cel.iloc[0])
print(f"Tanito tartomany: {tanito_skala.min():.4f} .. {tanito_skala.max():.4f}")
print(f"Validacios tartomany: {validacios_skala.min():.4f} .. {validacios_skala.max():.4f}")
print("A teszthalmazon most nem ertekelunk modellt.")
