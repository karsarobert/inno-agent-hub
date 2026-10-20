# C1 – Egyetlen választható, összetett bővítés.
# Csak tényleges időnyereség és tutori egyeztetés után kezdd.

# Ide a saját A2-függvényed definícióját vidd át.
# A régi próbaadatokat és a főprogramot ne másold ide.
def kosar_adatai(kosar, keresett_termek):
    return 0, 0, 0


def rendeleseket_osszesit(elso_kosar, masodik_kosar, arak):
    # Készíts új, terméknév szerint rendezett listát tétel-tuple-ökkel.
    # Használd a saját kosar_adatai függvényed eredményét is.
    return []


def riportot_megjelenit(sorok):
    # Írj saját bejárást, mezőkicsomagolást és végösszegzést.
    print("A riport még nincs elkészítve.")


arak = {"kávé": 450, "üdítő": 390, "szendvics": 890}
elso_kosar = ["kávé", "üdítő", "kávé"]
masodik_kosar = ["szendvics", "üdítő"]
sorok = rendeleseket_osszesit(elso_kosar, masodik_kosar, arak)
riportot_megjelenit(sorok)
print("Eredeti első kosár:", elso_kosar)
print("Eredeti második kosár:", masodik_kosar)
