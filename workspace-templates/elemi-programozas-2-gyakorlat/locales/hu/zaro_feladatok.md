# Z1 – saját függvény a szállítási díjhoz

**Időkeret: 7 perc. Fájl: `python_gyakorlat/onallo.py`.** A cél a megismert paraméter, return és if–else önálló alkalmazása. Az instrukciókat és a próbaeredményeket megkapod; a megoldó kódot te írod. Nem kell futás előtt kimenetet jósolnod.

## Mi működik most?

A mintafájl minden hívásnál 490-et ad vissza:

```python
def szallitas_dija():
    return 490


print(szallitas_dija())
```

Ez teljes, futtatható kiinduló program. A függvény még nem kapja meg a rendelés összegét, ezért nem is tud attól függő döntést hozni.

## Írd át a szabály alapján

A szállítás legalább 2500 Ft-os rendelésnél ingyenes; kisebb, nemnegatív összegnél 490 Ft.

1. A `szallitas_dija` kapjon egy paramétert, amely a rendelés összegét jelöli.
2. Írj bele if–else elágazást a fenti szabályhoz. A függvény számot adjon vissza minden ágon, ne írjon ki.
3. A régi adat nélküli hívást cseréld három, adattal történő hívásra. Az eredményeket a függvényen kívül írasd ki, 2499, 2500 és 3000 Ft-tal dolgozva.
4. Ments és indítsd a Futtatás gombbal. A gombhoz nem kell külön belépned a gyakorlómappába.

| Rendelés összege | Visszaadandó szállítási díj |
|---:|---:|
| 2499 | 490 |
| 2500 | 0 |
| 3000 | 0 |

Ha eltérést látsz, a feltételt, az egyenlőség esetét és a két visszatérési utat ellenőrizd. Segítséget kérhetsz: a tutor elmagyarázza a szükséges részt, és jelöli, miben segített. Nem az eredmények fejben kiszámolása a feladat, hanem az ezekhez vezető kód megírása.

**Sikeres a próba, ha:** a függvény a paraméteréből dönt, mindkét ágon számot ad vissza, a pontos 2500 Ft elfogadott, és a külső hívások ténylegesen használják a függvény eredményét. Nem elég három állandó számot kiírni.

Az óra végén az el nem készült rész is rögzíthető folytatási pontként. Nem szükséges újabb kötelező feladatsor a 90 percen túl.
