# Z1: ez még minden kosártételt számol, az árakat nem vizsgálja.
# A függvény törzsét te alakítod át saját feltételes számláló ciklussá.
def draga_tetelek_szama(kosar, arak, hatar):
    return len(kosar)


arak = {
    "kávé": 450,
    "szendvics": 890,
    "üdítő": 390,
    "croissant": 520,
}
kosar = ["kávé", "szendvics", "szendvics"]
hatar = 500
eredmeny = draga_tetelek_szama(kosar, arak, hatar)
print(f"Drága tételek száma: {eredmeny}")
