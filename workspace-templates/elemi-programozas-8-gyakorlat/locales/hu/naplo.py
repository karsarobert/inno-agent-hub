# B1.a: Minden vásárolt darab külön sor, a vásárláskori árral.
def vasarlasokat_ment(fajlnev, kosar, arak):
    pass


# B1.b: A naplóban tárolt árakból készíts (darab, bevétel) tuple-t.
def naplot_osszesit(fajlnev):
    return 0, 0


arak = {"kávé": 450, "szendvics": 890, "üdítő": 390, "tea": 350, "víz": 0}
kosar = ["kávé", "tea"]
naplo_fajl = "eladasok.txt"
# B1.a alatt True. B1.b olvasási próbái előtt állítsd False-ra.
mentes_bekapcsolva = True
if mentes_bekapcsolva:
    vasarlasokat_ment(naplo_fajl, kosar, arak)

darab, bevetel = naplot_osszesit(naplo_fajl)
print("Eladott darab:", darab)
print("Bevétel:", bevetel, "Ft")
