# A3.a: Egy nem üres sort értelmezünk: termék;darab;egységár.
def eladast_ertelmez(sor):
    return "", 0, 0


# A3.b: A teljes fájlból érvényes rekordok, sorszámos hibák, üres sorok.
def naplot_beolvas(fajlnev):
    return [], [], 0


# A3.a alatt ezt a sort vizsgáljuk. A kivétel kezelését a hívóba te írod.
sor = " kávé ; 2 ; 450\n"
rekord = eladast_ertelmez(sor)
print("Sorpróba:", rekord)

# A3.b előtt a fenti közvetlen sorpróbát érvényes adatra állítsd vissza.
rekordok, hibak, ures_sorok = naplot_beolvas("eladasok_vegyes.txt")
print("Rekordok:", rekordok)
print("Hibák:", hibak)
print("Üres sorok:", ures_sorok)
