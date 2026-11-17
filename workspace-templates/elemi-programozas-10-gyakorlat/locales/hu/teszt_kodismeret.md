# Kódértelmezés és hibakeresés

15 perc. K01–K05: értelmezés. K06–K10: hibakeresés.
A K05 a saját helyes bufe.py fájlodat használja; a többi kódrészlet önálló.

## K01 – Kódértelmezés

Mi a két kiírt szám? Hány példány készült?

```python
class Pont:
    def __init__(self):
        self.ertek = 2

elso = Pont()
masodik = Pont()
elso.ertek += 3
print(elso.ertek, masodik.ertek)
```

## K02 – Kódértelmezés

Mi a kimenet? Miért?

```python
class Doboz:
    def __init__(self):
        self.elemek = []

elso = Doboz()
masik = elso
masik.elemek.append(0)
print(elso.elemek)
print(elso is masik)
```

## K03 – Kódértelmezés

Mi jelenik meg? Hol jött létre a lista?

```python
class Doboz:
    elemek = []

elso = Doboz()
masodik = Doboz()
elso.elemek.append("x")
print(masodik.elemek)
```

## K04 – Kódértelmezés

Mi jelenik meg, és mi változott?

```python
class Szamlalo:
    def __init__(self):
        self.ertek = 0

    def novel(self):
        self.ertek += 1

szamlalo = Szamlalo()
eredmeny = szamlalo.novel()
print(eredmeny, szamlalo.ertek)
```

## K05 – Kódértelmezés

A saját, A3 szerint helyesen elkészült osztályoddal mi a kimenet?

```python
from bufe import Bufe

bufe = Bufe("Próba", {"viz": 0})
osszeg = bufe.elad("viz", 2)
print(osszeg, bufe.bevetel, len(bufe.eladasok))
```

## K06 – Hibakeresés

Mi a hiba oka, és mit kell javítani?

```python
class Cimke:
    def __init__(self, nev):
        nev = nev

cimke = Cimke("Próba")
print(cimke.nev)
```

## K07 – Hibakeresés

Miért hibás a hívás, és mi a javítás?

```python
class Koszonto:
    def szoveg():
        return "Szia!"

koszonto = Koszonto()
print(koszonto.szoveg())
```

## K08 – Hibakeresés

Miért nem megfelelő a __str__, és hogyan javítanád?

```python
class Cimke:
    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
        print(self.nev)

print(Cimke("Próba"))
```

## K09 – Hibakeresés

Miért veszik el a példány elérése a pontok néven?

```python
class Pontgyujto:
    def __init__(self):
        self.pont = 0

    def hozzaad(self, mennyivel):
        self.pont += mennyivel

pontok = Pontgyujto()
pontok = pontok.hozzaad(5)
print(pontok.pont)
```

## K10 – Hibakeresés

Mi marad hibás állapotban, és hogyan változtatnád meg a sorrendet?

```python
class Keszlet:
    def __init__(self):
        self.darab = 10

    def kivesz(self, mennyit):
        self.darab -= mennyit
        if mennyit <= 0 or self.darab < 0:
            raise ValueError("Érvénytelen kivét")

keszlet = Keszlet()
try:
    keszlet.kivesz(12)
except ValueError:
    print(keszlet.darab)
```
