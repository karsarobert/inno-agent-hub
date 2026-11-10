# Z1: Az A2 saját függvénydefiníciójával váltsd ki ezt a helykitöltőt.
def tetel_osszege(termek, darab, arak):
    return 0


# Hibás kosárhoz (None, hibalista), hibátlanhoz (összeg, []) tartozzon.
def kosarat_ellenoriz(kosar, arak):
    return 0, []


arak = {"kávé": 450, "tea": 350, "szendvics": 890, "víz": 0}
kosar = [("kávé", 2), ("víz", 3)]
osszeg, hibak = kosarat_ellenoriz(kosar, arak)
print("Kezdeti eredmény:", osszeg, hibak)
# A nyers kiírást te alakítod a követelmény szerinti döntéssé és visszajelzéssé.
