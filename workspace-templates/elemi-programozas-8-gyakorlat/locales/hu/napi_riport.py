# C1: Az egyetlen választható összetett bővítés.
# Eredmény: terméknév -> (darabszám, tárolt árak összege).
def termekenkenti_osszesites(fajlnev):
    return {}


def napi_riportot_ment(fajlnev, osszesites):
    pass


adatok = termekenkenti_osszesites("eladas_minta.txt")
napi_riportot_ment("napi_riport.txt", adatok)
print("Ellenőrizd a napi_riport.txt tartalmát a fájlnézetben.")
