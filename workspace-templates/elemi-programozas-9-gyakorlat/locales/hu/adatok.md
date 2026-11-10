# EP_09 – A változatlan bemeneti adatok

Öt UTF-8 fájl van a gyökérben; nincs BOM vagy fejléc. A repr jelölésben a \n egyetlen valódi sortörésnek felel meg. Minden nem üres naplósor a termék;darab;egységár szerkezetet követi, vagy szándékos hibát tartalmaz.

## eladasok_jo.txt

```text
'kávé;2;450\ntea;1;350\nvíz;3;0\nkávé;1;500'
```

A végén nincs sortörés.

## eladasok_vegyes.txt

```text
'kávé;2;450\nhibas sor\n\ntea;1;350\nvíz;3;0\nszendvics;0;890\nkávé;1;500\ntea;ketto;350\n;1;100\nüdítő;1;-50\n'
```

A végén van sortörés.

## eladasok_hibas.txt

```text
'hibas sor\ntea;-1;350\nkávé;1;drága\n'
```

A végén van sortörés.

## eladasok_valtott.txt

```text
'tea;2;320\nkávé;3;500\nvíz;1;0\n'
```

A végén van sortörés.

## ures.txt

```text
''
```

0 bájt, nincs benne szóköz és sortörés sem.


## Kézi összesítések

- Jó fájl: 4 rekord, de 7 eladott darab. Bevétel: 2×450 + 1×350 + 3×0 + 1×500 = 1750 Ft.
- Vegyes fájl: ugyanaz a 4 jó rekord, 5 hibás sor (2, 6, 8, 9, 10), 1 üres sor (3). Nem minden fizikai sor egy eladott darab.
- Csak hibás fájl: 0 jó rekord, 3 hiba, 0 üres sor.
- Váltott fájl: 3 rekord, 6 darab, 2×320 + 3×500 + 1×0 = 2140 Ft.

A naplók történeti eladási árai eltérhetnek a program mai árjegyzékétől. A riport nem árazza át a múltbeli rekordokat.

## Hiányzó fájl és saját kimenetek

Az ep09_nincs_naplo.txt szándékosan nincs a csomagban. Ne hozd létre a hibapróbához; ha véletlenül létezik ilyen saját fájlod, válassz másik, biztosan hiányzó nevet.

A bufe_jelentes.txt és az opcionális uj_eladasok.txt szintén nincs a ZIP-ben. Az elsőt a saját riportprogram hozza létre/frissíti, a másodikat csak C1-ben a saját naplómentő. Az írási hiba próbájához ures.txt/jelentes.txt szerepel: az ures.txt létező fájl, ezért nem lehet szülőmappa. A cél hibája nem indok az ures.txt törlésére vagy átnevezésére.

A forrásokhoz nem kell hozzáírnod. A próbákat fájlnév, keresett adat vagy paraméter váltásával végzed. A ZIP-et ne bontsd újra a már használt munkatérbe: felülírhatná a saját kódot.

Minden szöveges bemenet UTF-8. Sérült kódolás, idézőjeles CSV, párhuzamos módosítás és általános típusellenőrzés nem része a feladatnak. A fájlmentés nem atomi: írás közbeni OSError után a cél lehet hiányos; erre nem adhatunk sikerüzenetet. A hiányzó forrás miatt viszont el sem indulhat a mentés.
