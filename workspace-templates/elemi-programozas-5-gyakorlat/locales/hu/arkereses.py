# A1: a keresés még a nyers nevet használja.
# A függvénybe egységesítést, a főprogramba hiánykezelést írsz.
def arat_keres(arak, termek):
    return arak.get(termek)


arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
keresett_termek = "  KÁVÉ  "
talalt_ar = arat_keres(arak, keresett_termek)
print(talalt_ar)  # MODOSITSD: értelmes ár- vagy hiányjelzés
