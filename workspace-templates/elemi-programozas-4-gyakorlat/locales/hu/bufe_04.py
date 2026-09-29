# B2: ismert segédfüggvények az EP_03 és az EP_04 tananyagból.
# Árak: kávé 450, szendvics 890, üdítő 390, croissant 520 Ft.
# A kosár csak kínálatbeli, egységesített termékneveket tartalmazhat.
def termek_ara(termek):
    if termek == "kávé":
        return 450
    elif termek == "szendvics":
        return 890
    elif termek == "üdítő":
        return 390
    elif termek == "croissant":
        return 520
    else:
        return 0


def kosar_osszege(kosar):
    osszeg = 0
    for termek in kosar:
        osszeg += termek_ara(termek)
    return osszeg


def blokkot_mutat(kosar):
    print("--- Büféblokk ---")
    for termek in kosar:
        print(f"{termek}: {termek_ara(termek)} Ft")
    print(f"Tételek száma: {len(kosar)}")
    print(f"Ebből kávé: {kosar.count('kávé')} db")


def kedvezmeny_osszege(rendeles_osszeg, diak_e):
    if diak_e:
        return rendeles_osszeg // 10
    else:
        return 0


def nemnegativ_egesz_beker(kerdes):
    # Ebben a változatban egész számmá alakítható bemenetet várunk.
    szam = int(input(kerdes))
    while szam < 0:
        print("Nemnegatív egész számot adj meg.")
        szam = int(input(kerdes))
    return szam


def fizetest_ker(fizetendo):
    befizetett_osszesen = nemnegativ_egesz_beker("Átadott pénz (Ft): ")
    while befizetett_osszesen < fizetendo:
        hianyzo = fizetendo - befizetett_osszesen
        print(f"Még hiányzik: {hianyzo} Ft")
        potlas = nemnegativ_egesz_beker("Mennyit adsz még hozzá? (Ft): ")
        befizetett_osszesen += potlas
    print(f"Visszajáró: {befizetett_osszesen - fizetendo} Ft")


# B2.a: ide vidd át a kosar_04.py két saját függvénydefinícióját.
# A próbahívásokat és a főprogramot ne másold át.


# B2.a: egyszeri pontos összehasonlításból ellenőrzött bekérés.
# MODOSITSD: ciklus, egységesítés, igen/nem ellenőrzés, újrakérdezés.
def igen_nem_beker(kerdes):
    valasz = input(kerdes)
    return valasz == "igen"


# B2.b: a szerkezet készen van. Négy kezdőértéket és egy hívást módosítasz.
# A kiinduló program üres kosarat mutat: ez még nem a teljes megoldás.
kinalat = ["kávé", "szendvics", "üdítő", "croissant"]
kosar = []  # MODOSITSD 1: a saját kosárbekérőd hívása
blokkot_mutat(kosar)
rendeles_osszeg = kosar_osszege(kosar)
print(f"Rendelés: {rendeles_osszeg} Ft")
if rendeles_osszeg == 0:
    print("Nincs fizetendő tétel.")
else:
    diak_e = False  # MODOSITSD 2: az igen/nem bekérő hívása
    kedvezmeny = 0  # MODOSITSD 3: a kedvezményfüggvény hívása
    fizetendo = rendeles_osszeg  # MODOSITSD 4: vond le a kedvezményt
    print(f"Kedvezmény: {kedvezmeny} Ft")
    print(f"Fizetendő: {fizetendo} Ft")
    # HOZZAAD: a fizetést kezelő függvény hívása ebben az ágban
