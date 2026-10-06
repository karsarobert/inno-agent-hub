# T2 – Kódismereti teszt: kimenet és hibakeresés

10 kérdés, összesen 10 pont. Javasolt idő: 15 perc.
KÓD1–KÓD5: add meg a pontos kimenetet és a kért rövid indoklást.
KÓD6–KÓD10: nevezd meg a hibát vagy okát, és add meg a javítást. Nem kell az egész programot újra leírni.
Minden kódrészlet külön, új programként értendő; az előző kérdés változóit nem viszi tovább.
Szokásos Python 3-kódok, nincs verziófüggő idézőjeles trükk. A listák kiírásában az egyszeres és kettős idézőjel egyaránt elfogadható.
Első válaszaid előtt ne futtasd a kódokat. A teszt végén a hibás vagy bizonytalan válaszaidat futtatással is ellenőrizheted.
A programozási gyakorlatok során továbbra is saját kódírás és futtatás a feladat; ez a záró teszt külön kódértelmezési szakasz.

## KÓD1 – Egységesített keresés

Írd le a három kiírt sort, és röviden indokold az utolsó két eredményt.

```python
arak = {"tea": 320, "víz": 0}
termek = "  TEA  ".strip().lower()
print(arak.get(termek))
print(arak.get("kakaó"))
print(arak.get("víz") is None)
```

## KÓD2 – Módosítás és hozzáadás

Mi jelenik meg a három sorban? Miért változott a szótár elemszáma?

```python
arak = {"tea": 320, "keksz": 180}
arak["tea"] = 350
arak["víz"] = 200
print(len(arak))
print(arak["tea"])
print(arak["víz"])
```

## KÓD3 – Szűrés a határértéken

Melyik lista jelenik meg? Röviden indokold, miért kerül bele vagy marad ki a tea.

```python
arak = {"tea": 320, "keksz": 180, "kakaó": 480}
eredmeny = []
for termek, ar in arak.items():
    if ar <= 320:
        eredmeny.append(termek)
print(eredmeny)
```

## KÓD4 – Ismétlődő kosártétel

Milyen számot ír ki? Mutasd meg röviden a számítást.

```python
arak = {"tea": 320, "keksz": 180}
kosar = ["tea", "keksz", "tea"]
osszeg = 0
for termek in kosar:
    osszeg += arak[termek]
print(osszeg)
```

## KÓD5 – Szótár módosítása függvényben

Mi a két kiírt érték? Miért változik vagy marad változatlan a főprogram szótára?

```python
def arat_emel(arak, termek):
    arak[termek] += 20
    return arak[termek]

arak = {"tea": 320}
print(arat_emel(arak, "tea"))
print(arak["tea"])
```

## KÓD6 – Az ingyenes termék hibás jelzése

A víz szerepel a kínálatban, és ingyenes. Melyik feltétel hibás, miért, és hogyan javítanád?

```python
arak = {"víz": 0}
ar = arak.get("víz")
if not ar:
    print("Nincs ilyen termék.")
else:
    print(f"Ár: {ar} Ft")
```

## KÓD7 – Túl korai visszatérés

A cél a teljes kosár összegének visszaadása. Hol a hiba, mit okoz, és hogyan javítanád?

```python
def kosar_osszege(kosar, arak):
    osszeg = 0
    for termek in kosar:
        osszeg += arak[termek]
        return osszeg

print(kosar_osszege(["tea", "keksz"], {"tea": 320, "keksz": 180}))
```

## KÓD8 – Új kulcs véletlen felvétele

A függvény csak meglévő termék pozitív árát módosíthatná. Az ár egész szám, a terméknév már egységesített. Melyik ellenőrzés hiányzik? Írd le a javított feltételt.

```python
def arat_frissit(arak, termek, uj_ar):
    if uj_ar > 0:
        arak[termek] = uj_ar
        return True
    return False

arak = {"tea": 320}
print(arat_frissit(arak, "kakaó", 480))
print("kakaó" in arak)
```

## KÓD9 – Felcserélt kulcs és érték

Termékneveket és árakat szeretnénk kapni, majd a legfeljebb 400 Ft-os árakat vizsgálni. Mi a hiba a for sorában, mit okoz, és hogyan javítanád?

```python
arak = {"tea": 320, "kakaó": 480}
for ar, termek in arak.items():
    if ar <= 400:
        print(termek)
```

## KÓD10 – Szigorú árhatár

Csak a 320 Ft-nál szigorúan drágább kosártételeket kell megszámolni. Melyik sor hibás, és mi legyen a helyes feltétel és eredmény?

```python
arak = {"tea": 320, "kakaó": 480}
kosar = ["tea", "kakaó", "tea"]
darab = 0
for termek in kosar:
    if arak[termek] >= 320:
        darab += 1
print(darab)
```
