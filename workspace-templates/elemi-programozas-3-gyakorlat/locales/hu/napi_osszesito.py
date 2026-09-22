# B1: a kiinduló változat egyetlen rendelési összeget kezel.
napi_bevetel = 0
rendelesek_szama = 0
osszeg = int(input("Rendelés összege (0 = zárás): "))

if osszeg < 0:
    print("Negatív összeg nem fogadható el.")
elif osszeg > 0:
    napi_bevetel += osszeg
    rendelesek_szama += 1

print(f"Kifizetett rendelések: {rendelesek_szama}")
print(f"Napi bevétel: {napi_bevetel} Ft")
