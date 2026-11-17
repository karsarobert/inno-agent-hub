"""Z1: csak az ertekesiteseket_vegrehajt függvényt kell megírnod.
A főprogramban a bemeneti és kimeneti próbanév módosítható.
"""
from bufe import Bufe

ARAK = {"tea": 300, "szendvics": 700, "viz": 0}


def tetelek_beolvas(fajlnev):
    """(tételek, hibák, üres sorok száma).

    Tétel: (sorszám, termék, egész darabszám).
    Pozitivitást és terméklétezést a Bufe ellenőriz.
    A teljes fájlt érintő OSError a hívóhoz jut.
    """
    tetelek = []
    hibak = []
    ures = 0
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        for sorszam, sor in enumerate(fajl, start=1):
            tiszta = sor.strip()
            if tiszta == "":
                ures += 1
                continue
            mezok = tiszta.split(";")
            if len(mezok) != 2:
                hibak.append((sorszam, "Két mező szükséges: termek;darab"))
                continue
            termek = mezok[0].strip()
            if termek == "":
                hibak.append((sorszam, "Üres terméknév"))
                continue
            try:
                darab = int(mezok[1].strip())
            except ValueError:
                hibak.append((sorszam, "A darabszám nem egész szám"))
                continue
            tetelek.append((sorszam, termek, darab))
    return tetelek, hibak, ures


def ertekesiteseket_vegrehajt(bufe, tetelek, hibak):
    """HALLGATÓI RÉSZ.

    Minden tétel külön értékesítés. Hívd az elad metódust;
    ValueError esetén gyűjts sorszámos hibát, majd folytasd.
    A kapott bufe és hibak objektumokat módosítod.
    Visszatérési érték nem szükséges.
    """
    pass


def jelentest_ment(fajlnev, bufe, hibak, ures):
    """Friss jelentés írása. Az OSError-t a hívó kezeli."""
    eladott_darab = 0
    for termek, darab, osszeg in bufe.eladasok:
        eladott_darab += darab
    allapot = "Részleges" if hibak else "Teljes"
    with open(fajlnev, "w", encoding="utf-8") as fajl:
        fajl.write(f"Büfé: {bufe.nev}\n")
        fajl.write(f"Állapot: {allapot}\n")
        fajl.write(f"Értékesítések: {len(bufe.eladasok)}\n")
        fajl.write(f"Eladott darab: {eladott_darab}\n")
        fajl.write(f"Bevétel: {bufe.bevetel} Ft\n")
        fajl.write(f"Hibás sorok: {len(hibak)}\n")
        fajl.write(f"Üres sorok: {ures}\n")
        fajl.write("Értékesítések részletei:\n")
        for termek, darab, osszeg in bufe.eladasok:
            fajl.write(f"{termek};{darab};{osszeg}\n")
        fajl.write("Hibák:\n")
        for sorszam, uzenet in sorted(hibak):
            fajl.write(f"{sorszam}. sor: {uzenet}\n")


def munkamenetet_futtat(bemenet, kimenet, nev="Iskolai büfé"):
    """Érvényes név, UTF-8 bemenet és külön célfájl az előfeltétel."""
    try:
        tetelek, hibak, ures = tetelek_beolvas(bemenet)
    except FileNotFoundError:
        print("Hiányzó bemenet; nem készül új jelentés.")
        return False
    except OSError as hiba:
        print(f"Beolvasási hiba: {hiba}")
        return False
    bufe = Bufe(nev, ARAK)
    ertekesiteseket_vegrehajt(bufe, tetelek, hibak)
    try:
        jelentest_ment(kimenet, bufe, hibak, ures)
    except OSError as hiba:
        print(f"Mentési hiba: {hiba}")
        return False
    print(bufe)
    print(f"Elutasított sorok: {len(hibak)}")
    print(f"Jelentés elkészült: {kimenet}")
    return True


if __name__ == "__main__":
    bemenet = "eladasok_vegyes.txt"
    kimenet = "jelentes.txt"
    munkamenetet_futtat(bemenet, kimenet)
