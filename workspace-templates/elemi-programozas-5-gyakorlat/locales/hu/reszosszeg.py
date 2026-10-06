# C3: a legnagyobb darabszám * egységár értékhez tartozó termék neve kell.
# A darabszámok pozitív egészek, minden név ismert árjegyzékkulcs.
def legtobb_bevetelt_ado_termek(darabszamok, arak):
    # Üres szótárnál None; holtversenynél az elsőként bejárt termék maradjon.
    return None


arak = {"kávé": 450, "szendvics": 890, "üdítő": 390, "croissant": 520}
darabszamok = {"kávé": 3, "szendvics": 1}
termek = legtobb_bevetelt_ado_termek(darabszamok, arak)
if termek is None:
    print("Nincs rendelési tétel.")
else:
    print(f"Erre költöttünk a legtöbbet: {termek}")
