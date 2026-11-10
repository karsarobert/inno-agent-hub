# A2: Ismert termék és pozitív egész darabszám esetén számot adj.
# A tiltott értékeket ValueError kivétellel jelezd.
def tetel_osszege(termek, darab, arak):
    return 0


arak = {"kávé": 450, "tea": 350, "szendvics": 890, "víz": 0}
termek = "kávé"
darab = 2
eredmeny = tetel_osszege(termek, darab, arak)
print("Tételösszeg:", eredmeny, "Ft")
