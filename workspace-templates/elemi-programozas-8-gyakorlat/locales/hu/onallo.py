# Z1: Egy kiválasztott termék darabszámát és tárolt bevételét keresd.
def termek_adatai(fajlnev, keresett):
    return 0, 0


keresett = "kávé"
bemenet = "eladas_minta.txt"
kimenet = "termek_jelentes.txt"
darab, bevetel = termek_adatai(bemenet, keresett)
print("Termék:", keresett)
print("Eladott darab:", darab)
print("Bevétel:", bevetel, "Ft")
# A friss jelentés mentését is te írod meg a főprogramban.
