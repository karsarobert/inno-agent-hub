# A2: a kezdőminta még bármilyen kulcsot és árat beállít.
# Te adod hozzá az egységesítést és az ellenőrzéseket.
def arat_frissit(arak, termek, uj_ar):
    arak[termek] = uj_ar
    return True


arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
keresett_termek = "kávé"
uj_ar = 500
sikerult = arat_frissit(arak, keresett_termek, uj_ar)
print(sikerult)
print(arak)
