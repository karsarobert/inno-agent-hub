# C2: saját C1-függvény, külön számítás, majd összevont megjelenítés.
# Az árjegyzék és a darabszámok kulcsa egyaránt a termék neve.

# Ezt a definíciót cseréld a C1-ben elkészített saját függvényedre.
def darabszamokat_szamol(kosar):
    return {}


def osszesitett_ar(darabszamok, arak):
    # Termékenként darabszám * egységár; a részösszegek összege térjen vissza.
    return 0


def osszevont_blokkot_mutat(darabszamok, arak):
    print("--- Összevont büféblokk ---")
    for termek, darab in darabszamok.items():
        # Egészítsd ki egységárral és részösszeggel a sort.
        print(f"{termek}: {darab} db")
    # Ide írj egy hívást az összegződre, és jelenítsd meg a teljes összeget.


arak = {"kávé": 450, "szendvics": 890, "üdítő": 390, "croissant": 520}
kosar = ["kávé", "szendvics", "kávé", "üdítő", "szendvics"]
darabszamok = darabszamokat_szamol(kosar)
osszevont_blokkot_mutat(darabszamok, arak)
