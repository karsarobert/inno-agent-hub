# BEMENET: rögzített rendelés
kave_egysegar = 450
szendvics_egysegar = 890
kave_darabszam = 2
szendvics_darabszam = 1

# FELDOLGOZÁS
kave_osszeg = kave_darabszam * kave_egysegar
szendvics_osszeg = szendvics_darabszam * szendvics_egysegar
fizetendo = kave_osszeg + szendvics_osszeg

# KIMENET: formázott sorok
print(f"Kávé: {kave_darabszam} db, {kave_osszeg} Ft")
print(f"Szendvics: {szendvics_darabszam} db, {szendvics_osszeg} Ft")
print(f"Fizetendő: {fizetendo} Ft")
