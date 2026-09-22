def termek_ara(termek):
    if termek == "kávé":
        return 450
    elif termek == "szendvics":
        return 890
    elif termek == "üdítő":
        return 390
    else:
        return 0


def kedvezmeny_osszege(rendeles_osszeg, diak_e):
    if diak_e:
        return rendeles_osszeg // 10
    else:
        return 0


# B3: ezt a kezdő definíciót cseréld le a blokk.py-ban megírt
# saját blokkot_mutat függvényedre. Csak a definíciót vidd át.
def blokkot_mutat(kosar):
    print("--- Büféblokk ---")


kosar = ["kávé", "szendvics", "kávé", "üdítő"]
blokkot_mutat(kosar)

# B3-ban ezt a mintaszámítást cseréled a saját kosar_osszege hívására.
# Most még csak az első termék árát használja, nem a teljes kosarat!
rendeles_osszeg = termek_ara(kosar[0])
diak_valasz = input("Diák vagy? (igen/nem) ")
diak_e = diak_valasz == "igen"
kedvezmeny = kedvezmeny_osszege(rendeles_osszeg, diak_e)
fizetendo = rendeles_osszeg - kedvezmeny

print(f"Rendelés: {rendeles_osszeg} Ft")
print(f"Kedvezmény: {kedvezmeny} Ft")
print(f"Fizetendő: {fizetendo} Ft")

befizetett_osszesen = int(input("Átadott pénz (Ft): "))
if befizetett_osszesen >= fizetendo:
    print(f"Visszajáró: {befizetett_osszesen - fizetendo} Ft")
else:
    print(f"Még hiányzik: {fizetendo - befizetett_osszesen} Ft")
