# A2: Csak a paraméterként megadott kulcsszavakat számold.
# Minden keresett szó szerepeljen az eredményben, találat nélkül is 0-val.
def kulcsszavak_gyakorisaga(fajlnev, kulcsszavak):
    return {}


kulcsszavak = {"finom", "gyors", "olcsó"}
eredmeny = kulcsszavak_gyakorisaga("velemenyek.txt", kulcsszavak)
print("Gyakoriság:", eredmeny)
