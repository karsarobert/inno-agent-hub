# B1.a – A kezdő függvény még az eredeti kosarat módosítja.
# Alakítsd át úgy, hogy külön bővített listát adjon vissza.
def bovitett_kosarat_keszit(kosar, uj_termek):
    kosar.append(uj_termek)
    return kosar


# B1.b – Ezzel a résszel csak a B1.a után foglalkozz.
# A függvény egyelőre nem vesz fel új nevet: helykitöltő eredményt ad.
def torzsvevot_felvesz(torzsvevok, nev):
    return False


print("--- B1.a: kosárbővítés ---")
kosar = ["kávé", "üdítő"]
print("Hívás előtt:", kosar)
bovitett = bovitett_kosarat_keszit(kosar, "tea")
print("Eredeti a hívás után:", kosar)
print("Visszakapott kosár:", bovitett)
print("Ugyanaz az objektum:", kosar is bovitett)

print("--- B1.b: törzsvásárló ---")
torzsvevok = {"anna", "bela"}
nev = "csilla"
sikerult = torzsvevot_felvesz(torzsvevok, nev)
print("Új név került be:", sikerult)
print("Nyilvántartás:", sorted(torzsvevok))
