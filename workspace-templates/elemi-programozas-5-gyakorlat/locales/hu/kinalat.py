# A3: ez most mindent kiír. Szűréssel új listát kell visszaadnia.
def megfizetheto_termekek(arak, keret):
    for termek, ar in arak.items():
        print(f"{termek}: {ar} Ft")


arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
keret = 450
eredmeny = megfizetheto_termekek(arak, keret)
print(eredmeny)
