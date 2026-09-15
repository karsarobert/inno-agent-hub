# B1, majd B2: az EP_01-ről ismert, még függvények nélküli alap.
kave_egysegar = 450
szendvics_egysegar = 890

vendeg_neve = input("Hogy hívnak? ")
kave_darabszam = int(input("Hány kávét kérsz? "))
szendvics_darabszam = int(input("Hány szendvicset kérsz? "))

kave_osszeg = kave_egysegar * kave_darabszam
szendvics_osszeg = szendvics_egysegar * szendvics_darabszam
rendeles_osszeg = kave_osszeg + szendvics_osszeg

print(f"Szia, {vendeg_neve}!")
print(f"A rendelés összege: {rendeles_osszeg} Ft")
