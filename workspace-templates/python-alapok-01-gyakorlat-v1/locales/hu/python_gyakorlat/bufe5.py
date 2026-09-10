# RÖGZÍTETT ADATOK: egységárak forintban
kave_egysegar = 450
szendvics_egysegar = 890

# BEMENET: a vásárló válaszai
vasarlo_neve = input("Mi a neved? ")
kave_szoveg = input("Hány kávét kérsz? ")
szendvics_szoveg = input("Hány szendvicset kérsz? ")

# FELDOLGOZÁS: előbb átalakítunk, utána számolunk
kave_darabszam = int(kave_szoveg)
szendvics_darabszam = int(szendvics_szoveg)
kave_osszeg = kave_darabszam * kave_egysegar
szendvics_osszeg = szendvics_darabszam * szendvics_egysegar
fizetendo = kave_osszeg + szendvics_osszeg

# KIMENET: az elkészült rendelés
print(f"Köszönjük, {vasarlo_neve}!")
print(f"Kávé: {kave_darabszam} db, {kave_osszeg} Ft")
print(f"Szendvics: {szendvics_darabszam} db, {szendvics_osszeg} Ft")
print(f"Fizetendő: {fizetendo} Ft")
