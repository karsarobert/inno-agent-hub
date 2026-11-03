# T2 – EP_08 kódismereti teszt

10 kérdés, tervezetten 15 perc: KÓD1–KÓD5 kódértelmezés, KÓD6–KÓD10 hibakeresés. A rövid programok egymástól függetlenek, a munkamappa írható. Az első válaszadáskor ne futtasd a kódokat; a két rész teljes válaszadása után a javításhoz már futtathatsz. A kódkérdések saját teszt_ kezdetű fájlokat írnak, a tanulói naplót nem érintik. A KÓD6 csak a csomagolt ures.txt-t olvassa.

Kódértelmezésnél az eredményt és a kért rövid okot add meg. Hibakeresésnél nevezd meg az okot és a javítás elvét vagy érintett sorát. Teljes új programot nem kell írnod.

## KÓD1

Mi a négy kiírt sor? Az idézőjeles repr megjelenítést használd, hogy az üres sor és a fájlvég elkülönüljön.

```python
with open("teszt_sorok.txt", "w", encoding="utf-8") as fajl:
    fajl.write("alma\n\nkörte")

with open("teszt_sorok.txt", "r", encoding="utf-8") as fajl:
    print(repr(fajl.readline()))
    print(repr(fajl.readline()))
    print(repr(fajl.readline()))
    print(repr(fajl.readline()))
```

## KÓD2

Mi a három kiírt sor? Mi tette lehetővé az utolsó olvasást?

```python
with open("teszt_kurzor.txt", "w", encoding="utf-8") as fajl:
    fajl.write("A\nB")

with open("teszt_kurzor.txt", "r", encoding="utf-8") as fajl:
    elso = fajl.read()
    masodik = fajl.read()
    print(len(elso))
    print(len(masodik))
    fajl.seek(0)
    print(repr(fajl.readline()))
```

## KÓD3

Mi a három kiírt sor? A split itt nincs explicit elválasztóval meghívva.

```python
darabok = "gyors\tgyors  olcsó".split()
print(len(darabok))
print(len(set(darabok)))
print(" | ".join(darabok))
```

## KÓD4

Mi a végső kiírás, és miért nem marad benne az első két szó?

```python
with open("teszt_mod.txt", "w", encoding="utf-8") as fajl:
    fajl.write("egy\n")
with open("teszt_mod.txt", "a", encoding="utf-8") as fajl:
    fajl.write("kettő\n")
with open("teszt_mod.txt", "w", encoding="utf-8") as fajl:
    fajl.write("három\n")
with open("teszt_mod.txt", "r", encoding="utf-8") as fajl:
    print(repr(fajl.read()))
```

## KÓD5

Mi a három kiírt sor? Miben tér el az utolsó két művelet?

```python
nev, ar_szoveg = "tea;350\n".strip().split(";")
print(nev)
print(ar_szoveg + "5")
print(int(ar_szoveg) + 5)
```

## KÓD6

Az ures.txt létezik és 0 bájtos. Miért hibás a második művelet, milyen hibatípus várható, és hol legyen az olvasás?

```python
with open("ures.txt", "r", encoding="utf-8") as fajl:
    pass
print(fajl.read())
```

## KÓD7

Miért csak az alma jelenik meg, pedig a fájl később még tartalmaz adatot? Milyen feltételt vagy bejárást választanál, ha az üres sor nem fájlvég?

```python
with open("teszt_ures_sor.txt", "w", encoding="utf-8") as fajl:
    fajl.write("alma\n\nkörte\n")
with open("teszt_ures_sor.txt", "r", encoding="utf-8") as fajl:
    sor = fajl.readline().strip()
    while sor != "":
        print(sor)
        sor = fajl.readline().strip()
```

## KÓD8

A cél egy friss fájl, benne mindkét adattal külön sorban. Miért csak a kettő marad meg, és hogyan javítod úgy, hogy egy régi futás adatai se maradjanak benne?

```python
adatok = ["egy", "kettő"]
for adat in adatok:
    with open("teszt_friss.txt", "w", encoding="utf-8") as fajl:
        fajl.write(adat + "\n")
```

## KÓD9

Melyik sor és milyen hibatípussal akad meg? Hogyan legyen a fájlból már kinyert szöveges árak összege szám?

```python
osszeg = 0
ar_mezok = ["120", "80"]
for ar in ar_mezok:
    osszeg += ar
print(osszeg)
```

## KÓD10

Miért 100, majd None a kimenet? Hová kerüljön a return, hogy az első hívás 300-at, az üres lista pedig 0-t adjon?

```python
def arakat_osszegez(arak):
    osszeg = 0
    for ar in arak:
        osszeg += ar
        return osszeg

print(arakat_osszegez([100, 200, 0]))
print(arakat_osszegez([]))
```
