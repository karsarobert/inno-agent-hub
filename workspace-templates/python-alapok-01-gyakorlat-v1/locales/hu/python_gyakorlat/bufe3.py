# BEMENET: ebben a változatban a kódba írt adatok
kave_egysegar = 450
szendvics_egysegar = 890
kave_darabszam = 2
szendvics_darabszam = 1

# FELDOLGOZÁS: részösszegek és végösszeg
kave_osszeg = kave_darabszam * kave_egysegar
szendvics_osszeg = szendvics_darabszam * szendvics_egysegar
fizetendo = kave_osszeg + szendvics_osszeg

# KIMENET: a kiszámított összeg megjelenítése
print("Fizetendő:", fizetendo, "Ft")
