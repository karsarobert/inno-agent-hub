# EP_08 – Bemeneti fájlok és állapotuk

Az alábbi kilenc fájl változatlan próbabemenet. A tartalmuk UTF-8; nincs rejtett fejléc vagy BOM. A megadott repr megjelenítésben a \n egyetlen sortörést jelöl; a fájlokban valódi sortörések vannak. A kezdő és végső szóközök az A1 adataihoz tartoznak.

## rendelesek.txt

```text
' kávé \n\nszendvics\nkávé\n  üdítő  '
```

A végén nincs sortörés.

## rendeles_valtott.txt

```text
'tea\nvíz\ntea\n'
```

A végén van sortörés.

## velemenyek.txt

```text
'Finom a kávé, gyors a kiszolgálás.\n\nGYORS, de drága! A kávé finom.\nCsak jel: !!!\n'
```

A végén van sortörés.

## velemeny_rovid.txt

```text
'OLCSÓ! Gyors, gyors. finom?\n!!! ()\n'
```

A végén van sortörés.

## eladas_minta.txt

```text
'kávé;400\ntea;350\nkávé;450\nvíz;0\nszendvics;890'
```

A végén nincs sortörés.

## eladas_valtott.txt

```text
'tea;320\nkávé;500\ntea;350\nkávé;550\nkávé;0\n'
```

A végén van sortörés.

## naplo_proba.txt

```text
'kávé;450\ntea;350\nkávé;450\ntea;350\n'
```

A végén van sortörés.

## naplo_regi_arak.txt

```text
'kávé;400\nkávé;450\ntea;300\n'
```

A végén van sortörés.

## ures.txt

```text
''
```

0 bájt, nincs benne sem szóköz, sem sortörés.


## Saját kimenetek

Az eladasok.txt, blokk.txt, termek_jelentes.txt és napi_riport.txt szándékosan nincs a ZIP-ben. Ezeket a saját program készíti. A blokk és a jelentések w móddal frissülnek; az eladasok.txt a módban gyűlik. Ne bontsd újra a kezdőcsomagot a már használt munkatérbe: felülírná a saját kódodat, és félreérthető állapotot okozhatna.

B1.a ismételt futása valódi új eseményeket ment, akkor is, ha ugyanazok a nevek és árak. B1.b-ben ezért False a mentési kapcsoló. A naplo_proba.txt az első két sikeres B1.a futás tartalmával egyezik, de önálló, változatlan tesztfájl. Az eladas_minta.txt korábbi, eltérő árakat tartalmaz; a Z1 bevétele a tárolt árakból származik.

A naplóformátum minden nem üres sorában pontosan egy pontosvessző van: terméknév;egész_ár. A terméknév nem üres, belsejében nincs pontosvessző vagy sortörés. Az ár nemnegatív egész. A fizikai üres/whitespace sorokat a naplóolvasók kihagyják. Hiányzó fájl, hibás mezőszám, nem egész ár és idézőjeles CSV kezelése nem célkövetelmény; a következő lecke a hibakezelést bővíti.
