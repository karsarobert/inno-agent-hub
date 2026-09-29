# B1.a: cseréld a saját T1-függvényedre.
def szoveget_egysegesit(szoveg):
    return szoveg


# Kezdőminta: ismételt bekérés, még szűrés és visszavonás nélkül.
# B1.a: egységesítés, fizetek parancs, kínálatellenőrzés.
# B1.b: csak az a rész próbája után add hozzá a mégse ágat.
def kosarat_beker(kinalat):
    kosar = []
    print("Kínálat: " + ", ".join(kinalat))
    while True:
        termek = input("Mit kérsz? (vége = lezárás) ")  # MODOSITSD
        if termek == "vége":  # MODOSITSD: a büfé lezáró parancsa
            return kosar
        # MODOSITSD: csak kínálatbeli terméket adjunk hozzá.
        kosar.append(termek)
        print(f"Kosárban: {len(kosar)} tétel")


kinalat = ["kávé", "szendvics", "üdítő", "croissant"]
kosar = kosarat_beker(kinalat)
print("Kosár: " + ", ".join(kosar))
print(f"Tételek száma: {len(kosar)}")
