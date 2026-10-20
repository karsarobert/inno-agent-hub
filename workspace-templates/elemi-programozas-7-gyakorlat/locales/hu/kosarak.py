# A3 – Két kosár termékfajtáinak összehasonlítása.
# A szótár kulcsai és a kiírások előkészítettek.
# A helykitöltő értékek helyére te számítod ki a megfelelő eredményeket.
def kosarakat_hasonlit(elso_kosar, masodik_kosar):
    return {
        "osszes": set(),
        "kozos": set(),
        "csak_elso": set(),
        "csak_masodik": set(),
        "csak_egyik": set(),
        "elso_reszhalmaz": False,
    }


elso_kosar = ["kávé", "üdítő", "kávé"]
masodik_kosar = ["üdítő", "szendvics"]
eredmeny = kosarakat_hasonlit(elso_kosar, masodik_kosar)

print("Összes termékfajta:", sorted(eredmeny["osszes"]))
print("Közös termékfajták:", sorted(eredmeny["kozos"]))
print("Csak az elsőben:", sorted(eredmeny["csak_elso"]))
print("Csak a másodikban:", sorted(eredmeny["csak_masodik"]))
print("Pontosan az egyikben:", sorted(eredmeny["csak_egyik"]))
print("Az első termékfajtái mind a másodikban:", eredmeny["elso_reszhalmaz"])
print("Eredeti első kosár:", elso_kosar)
print("Eredeti második kosár:", masodik_kosar)
