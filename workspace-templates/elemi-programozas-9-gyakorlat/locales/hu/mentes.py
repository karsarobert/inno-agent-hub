# C1: A saját A2- és Z1-definíciókat hozd át, ne a korábbi főprogramokat.
def tetel_osszege(termek, darab, arak):
    return 0


def kosarat_ellenoriz(kosar, arak):
    return 0, []


# Előbb teljes adatellenőrzés; csak utána engedélyezett a hozzáfűzés.
def kosarat_ment(fajlnev, kosar, arak):
    return False


arak = {"kávé": 450, "tea": 350, "szendvics": 890, "víz": 0}
kosar = [("kávé", 2), ("víz", 3)]
siker = kosarat_ment("uj_eladasok.txt", kosar, arak)
print("Siker:", siker)
