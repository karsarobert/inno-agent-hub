def termek_ara(termek):
    if termek == "kávé":
        return 450
    elif termek == "szendvics":
        return 890
    elif termek == "üdítő":
        return 390
    else:
        return 0


# C1: a fejléc után te írod meg a tételek bejárását és a számlálást.
def blokkot_mutat(kosar):
    print("--- Büféblokk ---")


kosar = ["kávé", "szendvics", "kávé", "üdítő"]
blokkot_mutat(kosar)

