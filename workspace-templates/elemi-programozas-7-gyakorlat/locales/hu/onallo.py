# Z1 – Mely kosártermékek hiányoznak az árjegyzékből?
# A helykitöltő függvény még minden kosárhoz üres halmazt ad.
# A keresést és az eredménytől függő megjelenítést te készíted el.
def hianyzo_termekek(kosar, arak):
    return set()


arak = {"kávé": 450, "üdítő": 390, "szendvics": 890}
kosar = ["kávé", "tea", "tea"]
hianyzo = hianyzo_termekek(kosar, arak)

print("Keresés eredménye:", hianyzo)
print("Eredeti kosár:", kosar)
print("Eredeti árjegyzék:", arak)
