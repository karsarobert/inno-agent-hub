# A3: Az A1-ben már megírt saját függvényed definícióját hozd át ide.
# A korábbi fájl főprogramját és próbahívásait nem kell átmásolni.
def rendelest_beolvas(fajlnev):
    return []


# Ez a függvény egy friss blokkot írjon. A pass még nem végez fájlműveletet.
def blokkot_ment(fajlnev, kosar, arak):
    pass


arak = {"kávé": 450, "szendvics": 890, "üdítő": 390, "tea": 350, "víz": 0}
kosar = rendelest_beolvas("rendelesek.txt")
blokkot_ment("blokk.txt", kosar, arak)
print("Ellenőrizd a blokk.txt tartalmát a fájlnézetben.")
