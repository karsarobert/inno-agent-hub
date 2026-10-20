# T2 – EP_07 kódismereti teszt

10 kérdés, 10 pont, tervezetten 15 perc. KÓD1–KÓD5: pontos kimenet és rövid indoklás. KÓD6–KÓD10: hiba/ok és működő javítás. A hibanevet nem kell pontosan megnevezned, ha az okot helyesen leírod.

Minden kódrészlet külön új program. Az előző kérdés adatait nem viszi tovább. A listakiírásban egyszeres és kettős idézőjel egyaránt elfogadható. A rendezés minden sorrendre kérdező halmazpéldában explicit szerepel.

Elsőre ne futtasd a kódokat és ne nyisd meg a megoldókulcsot. A két teszt válaszai után javítunk, ekkor már futtathatsz. A programozási gyakorlatok során továbbra is saját szerkesztés és futtatás a feladat; ez külön kódértelmezési szakasz.

## KÓD1 – Tuple kicsomagolása

Mi a kiírt sor, és melyik két mezőből származik a számított részösszeg?

```python
tetel = ("tea", 3, 200)
termek, darab, egysegar = tetel
print(f"{termek}: {darab * egysegar} Ft")
```

## KÓD2 – Összes darab és termékfajta

Mi a három kiírt szám? Röviden különböztesd meg, mit számolnak.

```python
kosar = ["tea", "keksz", "tea", "víz", "keksz"]
print(len(kosar))
print(len(set(kosar)))
print(kosar.count("keksz"))
```

## KÓD3 – Halmazműveletek

Mi jelenik meg a három sorban? Röviden indokold a két logikai eredményt.

```python
elso = {"alma", "körte"}
masodik = {"körte", "szilva"}
print(sorted(elso ^ masodik))
print(elso <= masodik)
print(set() <= masodik)
```

## KÓD4 – Helyi név és visszatérés

Mi a két kiírt szám? Miért nem változik meg a külső szam a függvényben lévő értékadástól?

```python
def novel(szam):
    szam = szam + 1
    return szam

szam = 10
print(novel(szam))
print(szam)
```

## KÓD5 – Módosítás és hiányzó return

Mi a két kiírt sor? Miért változik a kosár, és miért ez a függvény visszatérési értéke?

```python
def bovit(lista):
    lista.append("tea")

kosar = ["kávé"]
eredmeny = bovit(kosar)
print(kosar)
print(eredmeny)
```

## KÓD6 – Halmaz indexelése

Az összes termékfajtát szeretnénk rendezett sorokban megjeleníteni. Miért hibás a kiírás, és hogyan javítanád bejárással?

```python
termekfajtak = {"tea", "keksz"}
print(termekfajtak[0])
```

## KÓD7 – Üres halmaz létrehozása

Üres halmazhoz szeretnénk teát hozzáadni. Mi a hiba oka, és mi legyen a létrehozó sor?

```python
termekfajtak = {}
termekfajtak.add("tea")
print(sorted(termekfajtak))
```

## KÓD8 – Elveszett ismétlődések

A megvásárolt darabokat kell számolni, ismétlődésekkel együtt. Miért hibás az eredmény, és hogyan őriznéd meg a szükséges adatot?

```python
kosar = ["tea", "tea", "keksz"]
kosar = set(kosar)
print(len(kosar))
```

## KÓD9 – Másik név vagy másolat?

Az eredeti kosárnak változatlanul kellene maradnia. Miért nem teljesül ez, és hogyan javítanád a függvényt?

```python
def bovitett_kosar(kosar):
    uj = kosar
    uj.append("tea")
    return uj

kosar = ["kávé"]
masik = bovitett_kosar(kosar)
print(kosar)
print(masik)
```

## KÓD10 – Túl korai visszatérés

Minden termék darabszámát vissza kellene adni, üres kosárnál pedig üres szótárat. Hol a hiba, mit okoz, és hova kerüljön a return?

```python
def darabszamokat_ad(kosar):
    eredmeny = {}
    for termek in kosar:
        eredmeny[termek] = kosar.count(termek)
        return eredmeny

print(darabszamokat_ad(["tea", "keksz"]))
print(darabszamokat_ad([]))
```
