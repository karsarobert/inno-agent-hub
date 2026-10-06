# B1: rögzített kosár feldolgozása; még nincs input vagy fizetés.
# A kezdő ciklus darabot számol. Alakítsd pénzösszegzéssé.
def kosar_osszege(kosar, arak):
    osszeg = 0
    for termek in kosar:
        osszeg += 1  # MODOSITSD: az adott tétel ára növelje az összeget
    return osszeg


def blokkot_mutat(kosar, arak):
    print("--- Büféblokk ---")
    for termek in kosar:
        print(termek)  # MODOSITSD: a termék ára és Ft is jelenjen meg
    print(f"Tételek száma: {len(kosar)}")


arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
kosar = ["kávé", "üdítő", "kávé"]
blokkot_mutat(kosar, arak)
rendeles_osszeg = kosar_osszege(kosar, arak)
print(f"Rendelés: {rendeles_osszeg} Ft")
