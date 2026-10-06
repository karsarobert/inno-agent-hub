# B2: az EP_04 ismert beviteli és fizetési részei készen állnak.
# Először a jelölt másolási helyet és a fájl végi főprogramot szerkeszd.
# Az új számoló- és blokkfüggvény az osszegzes.py-ból kerül ide.

def szoveget_egysegesit(szoveg):
    return szoveg.strip().lower()


def kosarat_beker(kinalat):
    kosar = []
    print("Kínálat: " + ", ".join(kinalat))
    print("Parancsok: mégse = utolsó tétel törlése; fizetek = lezárás.")
    while True:
        termek = szoveget_egysegesit(input("Mit kérsz? "))
        if termek == "fizetek":
            return kosar
        if termek == "":
            print("Írj be terméknevet vagy parancsot.")
            continue
        if termek == "mégse":
            if len(kosar) == 0:
                print("Üres a kosár, nincs mit törölni.")
            else:
                torolt_termek = kosar.pop()
                print(f"Törölve: {torolt_termek}")
        elif termek in kinalat:
            kosar.append(termek)
            print(f"Kosárban: {len(kosar)} tétel")
        else:
            print(f"Nincs a kínálatban: {termek}")


def kedvezmeny_osszege(rendeles_osszeg, diak_e):
    if diak_e:
        return rendeles_osszeg // 10
    else:
        return 0


def igen_nem_beker(kerdes):
    while True:
        valasz = szoveget_egysegesit(input(kerdes))
        if valasz == "igen":
            return True
        if valasz == "nem":
            return False
        print("Kérlek, igen vagy nem legyen a válasz.")


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


# B2.a: ide másold át a saját kosar_osszege és blokkot_mutat definícióidat.
# Mindkettő kosar és arak paramétert kapjon.
# A régi főprogramot és az árjegyzéket ne másold át.


# B2 főprogram: egyetlen árjegyzék, már előkészített fizetési szerkezet.
arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
kosar = []  # MODOSITSD 1: a kosárbekérő hívása az árjegyzékkel
# HOZZAAD: a saját blokkfüggvényed hívása a két szükséges adattal

if len(kosar) == 0:
    print("Nincs fizetendő tétel.")
else:
    rendeles_osszeg = 0  # MODOSITSD 2: a saját összegződ hívása
    print(f"Rendelés: {rendeles_osszeg} Ft")
    diak_e = igen_nem_beker("Diák vagy? (igen/nem) ")
    kedvezmeny = kedvezmeny_osszege(rendeles_osszeg, diak_e)
    fizetendo = rendeles_osszeg - kedvezmeny
    print(f"Kedvezmény: {kedvezmeny} Ft")
    print(f"Fizetendő: {fizetendo} Ft")
    fizetest_ker(fizetendo)
