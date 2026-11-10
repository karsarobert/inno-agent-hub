# B1: Csak az A3 két saját függvénydefinícióját hozd át, ne a főprogramot.
def eladast_ertelmez(sor):
    return "", 0, 0


def naplot_beolvas(fajlnev):
    return [], [], 0


# Az alábbi két segédfüggvény kész, működő támogatás. Nem kell újraírnod.

def naplo_adatait_osszesit(rekordok, hibak, ures_sorok):
    darab = 0
    bevetel = 0
    for termek, mennyiseg, egysegar in rekordok:
        darab += mennyiseg
        bevetel += mennyiseg * egysegar
    return {"rekordok": len(rekordok), "darab": darab, "bevetel": bevetel,
            "hibak": len(hibak), "ures_sorok": ures_sorok}


def osszesitest_ment(fajlnev, adatok):
    with open(fajlnev, "w", encoding="utf-8") as fajl:
        fajl.write(f"Érvényes rekordok: {adatok['rekordok']}\n")
        fajl.write(f"Eladott darab: {adatok['darab']}\n")
        fajl.write(f"Bevétel: {adatok['bevetel']} Ft\n")
        fajl.write(f"Hibás sorok: {adatok['hibak']}\n")
        fajl.write(f"Üres sorok: {adatok['ures_sorok']}\n")
        if adatok["rekordok"] == 0:
            fajl.write("Állapot: nincs feldolgozható eladás\n")
        elif adatok["hibak"] > 0:
            fajl.write("Állapot: részleges adatfeldolgozás\n")
        else:
            fajl.write("Állapot: minden nem üres sor feldolgozva\n")


# A fájlszintű hibakezelést és az összekapcsolást te készíted el.
def riportot_keszit(bemenet, kimenet):
    return False


siker = riportot_keszit("eladasok_vegyes.txt", "bufe_jelentes.txt")
print("A visszatérési érték:", siker)
# A főprogram riportkísérletét te egészíted ki finally lezáró üzenettel.
