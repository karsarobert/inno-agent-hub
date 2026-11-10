# EP_09 – Gyakorló tesztek megoldókulcsa

Tutori/oktatói értékeléshez, a teljes önálló válaszadás után. A munkatérben elérhető, ezért a teszt nem titkos vizsga. A fájl nem tartalmaz kész A1–C1 célprogramot.

## Pontozás és bizonyíték

T1: egy helyes válasz 1 pont, legfeljebb 10. Ellentmondó betű/magyarázat vagy több betű esetén egyszer tisztázz, ne találj ki választ. Kihagyás 0.

T2 KÓD1–KÓD5: a teljes helyes eredmény és a kért rövid indok együtt 1 pont; helyes eredmény lényegi magyarázat nélkül vagy egy lényegi rész hiányával 0,5; félreértett működés 0. A jelentést nem változtató idézőjel/szóköz nem hiba. KÓD4-nél a három mennyiség jelentését is meg kell nevezni; KÓD5-nél a None-vizsgálat szerepét is.

T2 KÓD6–KÓD10: 0,5 pont a lényegi ok, 0,5 a helyes javítási irány. Egyenértékű javítás elfogadott; teljes új kód nem kell. Kihagyás 0. T2 legfeljebb 10.

Az első önálló választ, a segítséggel kialakult választ és a későbbi javítást külön kezeld. Segítség előtti választ ne írd felül utólag; az első válasz előtt támogatott kérdést azonosítóval jelöld a /10–/10–/20 összpont mellett. Ezt ne nevezd tisztán önálló eredménynek. Hiányzó/nem feltett kérdés nem teljesített; részleges tesztnél a megválaszolt darabszámot is közöld.

A teljes T2 után értékelj, majd a tényleges félreértéseket beszéljétek meg. Javításkor már futtathat a hallgató. A programozási állapot és a tesztpont külön marad; a pontszám nem automatikus jegy vagy elsajátítási százalék.

## T1

| Azonosító | Válasz | Indoklás |
| --- | --- | --- |
| E1 | A | A hibás szöveg nem alakítható egésszé. A kevés pénz sikeres konverzió után ellenőrizhető feltétel. |
| E2 | C | A hiány nem sikeres üres beolvasás; az egész fájl problémájáról a hívó dönt. |
| E3 | B | A cikluson belüli kezelés után folytatható a következő sor; a kihagyást jelezni kell. |
| E4 | D | A számító függvény adatot ad vagy hibát jelez; a kommunikáció a hívó dolga. |
| E5 | A | Pozitív darabszám és nemnegatív egységár kell. A 0 ár megengedett, a 0 darab és üres terméknév nem. |
| E6 | C | A visszakereséshez a fizikai sorszám kell; az üres sor is növeli. |
| E7 | B | A korábbi fájl és a finally futása nem bizonyítja az új mentés sikerét. |
| E8 | D | Befejező művelet, nem sikerbizonyíték. A finally-beli return elfedhet eredményt/kivételt, ezért nem ezt a mintát használjuk. |
| E9 | A | A rekord mennyiséget és történeti egységárat őriz; a bevétel ezek szorzata. |
| E10 | C | A Z1 üzleti szabálya hibás kosárnál nem enged részösszeg fizetését. A 0 ettől különböző, valós összeg is lehet. |

## T2

### KÓD1

```text
5
hibás szöveg
1
```

Csak az alma konverziója hibás. A 0 is érvényes szám, ezért az else ott is fut.

### KÓD2

```text
általános fájlhiba
```

A FileNotFoundError az OSError speciális esete; az első illeszkedő kezelő fut. A konkrét esethez a sorrendet meg kellene fordítani.

### KÓD3

```text
lezárva
3
lezárva
elutasítva
```

A finally a sikeres return előtt és a ValueError továbbadása előtt is lefut.

### KÓD4

```text
2
5
300
```

Két rekord, öt eladott darab, háromszáz Ft. Az ingyenes víz is növeli a darabszámot.

### KÓD5

```text
False
False
True
```

A 0 nem None, de hamis igazságértékű. A hiányhoz az is None vizsgálat megfelelő, nem a puszta bool(osszeg).

### KÓD6

A ValueError elnyelődik, a darab régi 5 értéke marad, és a program ezt tévesen sikernek nevezi. Az except adjon jelzést/újrapróbálkozást, a sikeres kiírás csak sikeres konverzió után fusson, például else ágban. Ciklusban a hibás eset continue-val kérhet új adatot.

A pass nem javítja a hibás adatot, és nem hoz létre új sikeres eredményt.

### KÓD7

A kivétel elhagyja a teljes ciklust, így a 20-hoz nem jutunk el. Az adott elem konverziójának ValueError-ját a cikluson belül kell kezelni, jelezni/gyűjteni a hibát, majd a következő elemmel folytatni. Így az összeg 30.

A kezelő után nem térünk automatikusan vissza a megszakított ciklusba.

### KÓD8

A finally-beli return 0 elnyomja az eredeti kivételt és ezt adja vissza. A finally-ból el kell hagyni a return-t; ott legfeljebb a valódi befejező művelet maradjon. A ValueError-t megfelelő hívói except kezelheti.

A finally nem alkalmas minden ágon sikeresnek látszó alapérték visszaadására.

### KÓD9

A második w megnyitás már kiüríti a régi célt, aztán az int ValueError-t jelez. A bemenet konverziója/ellenőrzése az írási megnyitás előtt történjen; hibánál ne induljon mentés. Az OSError kezelés önmagában nem teszi atomivá az írást.

Az adatellenőrzési hiba előtti fájlvédelem a műveletek sorrendjétől függ.

### KÓD10

A ZeroDivisionError az except ValueError ág belsejében keletkezik, nem az eredeti try blokkban. Ugyanennek a szerkezetnek másik except ága nem kapja el. A hibás kezelőből el kell távolítani/javítani az osztást, vagy az új művelethez saját/külső megfelelő kezelő szükséges.

A try-hoz tartozó except ágak nem egymás hibáinak kezelői.
