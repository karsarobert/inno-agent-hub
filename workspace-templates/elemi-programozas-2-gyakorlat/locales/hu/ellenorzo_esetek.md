# EP_02 – konkrét próbák a saját kódodhoz

A táblázatok ellenőrzési feltételek. **Írd meg a kódot, mentsd, futtasd, majd hasonlítsd össze az eredményt.** Nincs előzetes jóslási feladat. A tutor a tényleges programot is megnézi: önmagában az itt olvasható szám visszaküldése nem jelenti a feladat elkészítését.

Minden `.py` a `python_gyakorlat/` mappában van. A megfelelő fájl legyen megnyitva és elmentve; a Futtatás gomb használatához ne lépj be külön a gyakorlómappába, mert a gomb a munkatérhez viszonyított útvonalat kezeli. A szóközök vagy barátságos feliratok apró eltérései nem hibák, ha a kiírás jelentése egyértelmű, és az adott feladat nem kifejezetten pontos formát kér.

## F1 – egy definíció, két hívás

- Anna és Béla külön hívásban: a megfelelő név a megfelelő köszöntésben jelenik meg.
- A név a paraméterből kerüljön a szövegbe, ne egy beégetett „Anna” legyen a törzsben.

## F2 – valóban visszaadott szám

| Egységár | Darabszám | Visszaadott összeg |
|---:|---:|---:|
| 450 | 2 | 900 |
| 450 | 3 | 1350 |
| 890 | 2 | 1780 |

A függvény ne csak kiírja a számot. A hívó kapja meg és használja fel; a kimenet ne tartalmazzon váratlan None-t vagy a függvénybe rejtett plusz kiírást.

## B1 – változatlan működés az átszervezés után

| Név | Kávé | Szendvics | Alapösszeg |
|---|---:|---:|---:|
| Anna | 2 | 1 | 1790 Ft |
| Béla | 3 | 2 | 3130 Ft |

A `rendeles_osszege` a két darabszámot használja, belül a `tetel_ara` részszámításait hívja, és visszaadja az összeget. A bekérés és a kiírás a függvényen kívül marad.

## D1 – kedvezmény és a fizetési határ

| Alapösszeg | Diák? | Kedvezmény | Fizetendő |
|---:|---|---:|---:|
| 1790 | True | 179 | 1611 |
| 1790 | False | 0 | 1790 |

1611 Ft fizetendőnél 2000 Ft-ból 389 Ft visszajáró, 1611 Ft-ból 0 Ft visszajáró, 1610 Ft-nál 1 Ft hiány keletkezik.

**Külön próba, ha a kedvezményszabályt kell tisztázni:** 1795 Ft-nál a kedvezmény 1795 // 10 = 179 Ft, a fizetendő 1616 Ft. Ez megadott tanpéldaszabály. Az `int(osszeg * 0.9)` nem ugyanennek a szabálynak általánosan azonos megvalósítása.

## D2 – kategóriahatárok

1499 → Kis rendelés; 1500 → Közepes rendelés; 2999 → Közepes rendelés; 3000 → Nagy rendelés. Minden futás egyetlen kategóriát írjon ki.

## B2 – fő órai próbák

A sorrend: név, kávé, szendvics, igen/nem válasz, átadott pénz. A számok mellé nem gépelünk mértékegységet.

| Név | Kávé | Szendvics | Diák? | Pénz | Alapösszeg | Kedvezmény | Fizetendő | Eredmény |
|---|---:|---:|---|---:|---:|---:|---:|---|
| Anna | 2 | 1 | igen | 2000 | 1790 | 179 | 1611 | 389 Ft visszajáró |
| Béla | 2 | 1 | nem | 2000 | 1790 | 0 | 1790 | 210 Ft visszajáró |
| Anna | 2 | 1 | igen | 1611 | 1790 | 179 | 1611 | 0 Ft visszajáró |
| Anna | 2 | 1 | igen | 1610 | 1790 | 179 | 1611 | 1 Ft hiány |

Kiegészítő, célzott próbák: 3 kávé + 2 szendvics, igen, 3000 Ft → 3130 Ft alapösszeg, 313 Ft kedvezmény, 2817 Ft fizetendő, 183 Ft visszajáró. Nulla kávé + nulla szendvics, nem, 0 Ft → minden összeg 0; az üres rendelést ebben a tanpéldában elfogadjuk.

A fő változat megfelelő formájú, nemnegatív adatokat feltételez. A hibás „talan” válasz vagy negatív darabszám felismerése **csak K2 után követelmény**. `ketto` vagy `2.5` az egész számos inputnál ValueError-t okozhat; a fő útvonalon és K2-ben sem írunk még try/except-es javító bekérést.

## Z1 – szállítási díj

2499 Ft → 490 Ft; 2500 Ft → 0 Ft; 3000 Ft → 0 Ft. A függvény kapja meg az összeget paraméterként, döntés alapján adjon vissza számot, és a kiírás a hívóban történjen.

## K2 után – a kibővített bemeneti ellenőrzés

Negatív kávé, negatív szendvics, negatív pénz vagy az igen/nem-től eltérő válasz esetén hibaüzenet jelenjen meg, ne készüljön számított nyugta. Mind a négy hibatípust külön, egyetlen adatot megváltoztatva próbáld ki. Az egész számmá alakítható negatív számot meg tudjuk vizsgálni; a számmá sem alakítható szöveget itt továbbra sem kezeljük.
