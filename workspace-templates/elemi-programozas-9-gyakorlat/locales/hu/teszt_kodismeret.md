# T2 – EP_09 kódismereti teszt

10 kérdés, tervezetten 15 perc. KÓD1–KÓD5 kódértelmezés, KÓD6–KÓD10 hibakeresés. Az első önálló válaszadáskor ne futtasd a kódokat és ne nyisd meg a kulcsot; a teljes T2 utáni javításhoz már futtathatsz. A kódok különállóak. A KÓD9 saját teszt_jelentes.txt-t ír, a csomagolt bemeneteket és a saját büfés naplót nem érinti.

Add meg a kért kimenetet és rövid indokot; hibakeresésnél az okot és a javítás elvét vagy érintett sorát. Teljes új programot nem kell írni. C1 nem előfeltétel.

## KÓD1

Mi a három kiírt sor? Melyik bemenetnél fut az except ág?

```python
for szoveg in ["4", "alma", "0"]:
    try:
        szam = int(szoveg)
    except ValueError:
        print("hibás szöveg")
    else:
        print(szam + 1)
```

## KÓD2

Mi íródik ki? Miért nem a második except ág fut?

```python
try:
    raise FileNotFoundError("szándékos próba")
except OSError:
    print("általános fájlhiba")
except FileNotFoundError:
    print("hiányzó fájl")
```

## KÓD3

Mi a kiírás pontos sorrendje? Mi történik a finally-val a két hívásban?

```python
def keretet_vizsgal(ertek):
    try:
        if ertek < 0:
            raise ValueError("negatív keret")
        return ertek + 1
    finally:
        print("lezárva")

for ertek in [2, -1]:
    try:
        print(keretet_vizsgal(ertek))
    except ValueError:
        print("elutasítva")
```

## KÓD4

Mi a három kiírt szám, és melyik mit jelent?

```python
rekordok = [("víz", 2, 0), ("tea", 3, 100)]
darab = 0
bevetel = 0
for nev, mennyiseg, egysegar in rekordok:
    darab += mennyiseg
    bevetel += mennyiseg * egysegar
print(len(rekordok))
print(darab)
print(bevetel)
```

## KÓD5

Mi a három logikai eredmény? Melyik vizsgálat különíti el a 0 összeget a None hiányjelzéstől?

```python
osszeg = 0
hibak = []
print(osszeg is None)
print(bool(osszeg))
print(hibak == [])
```

## KÓD6

Miért félrevezető az Elfogadott felirat? Hogyan legyen sikertelen konverzió után új kérés vagy célzott hibajelzés, sikeresnek látszó régi érték nélkül?

```python
darab = 5
try:
    darab = int("alma")
except ValueError:
    pass
print("Elfogadott:", darab)
```

## KÓD7

Miért 10 az összeg, és hogyan kapjuk meg a későbbi jó 20-at is, a hibás adat jelzett kihagyásával?

```python
osszeg = 0
try:
    for szoveg in ["10", "hibás", "20"]:
        osszeg += int(szoveg)
except ValueError:
    print("Egy hibás adatot kihagytunk.")
print(osszeg)
```

## KÓD8

Miért nincs látható ValueError, és miért 0 a kiírás? Hogyan ne fedje el a befejező blokk az eredeti hibát?

```python
def proba():
    try:
        raise ValueError("érvénytelen adat")
    finally:
        return 0

print(proba())
```

## KÓD9

Miért vész el a korábbi jelentés, ha az új adat hibás? Hogyan legyen a validáció sorrendje, hogy konverziós hiba miatt ne nyíljon meg írásra a cél?

```python
with open("teszt_jelentes.txt", "w", encoding="utf-8") as fajl:
    fajl.write("korábbi jelentés\n")

with open("teszt_jelentes.txt", "w", encoding="utf-8") as fajl:
    ertek = int("hibás")
    fajl.write(str(ertek) + "\n")
```

## KÓD10

Miért nem kezeli a második except a nullával osztást? Milyen kivétel jut ki, és hol kell a hibás kezelőt javítani vagy az új hibát külön kezelni?

```python
try:
    int("hibás")
except ValueError:
    print(1 / 0)
except ZeroDivisionError:
    print("Kezelt osztási hiba.")
```
