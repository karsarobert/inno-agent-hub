# Saját kísérleti jegyzet – 3. gyakorlat, 1.1

Az első spirálfutás ELŐTT megismert szabály: kisebb teljes validációs
keresztentrópia alapján választok; pontos egyezésnél kevesebb paraméter dönt.
A pontosságot és a képeket is értelmezem. A tesztet csak a döntés után nézem meg.
A gradiensprogram MSE/2 értékét nem hasonlítom a spirálmodellek veszteségéhez.

## Négy kötelező spirálfutás

| Futás | Rejtett neuronok | Ráta | Epoch | Batch | Paraméterek |
|---|---|---:|---:|---:|---:|
| R1 | nincs | 0.01 | 150 | 32 | 9 |
| R2 | 16 | 0.01 | 150 | 32 | 99 |
| R3 | 50, 50 | 0.01 | 150 | 32 | 2853 |
| R4 | 50, 50 | 0.001 | 150 | 32 | 2853 |

Ha az oktató előzetesen más egységes epochkeretet választott, a ténylegeset írd be.

| Futás | Pontos futási mappanév | Validációs loss | Validációs accuracy |
|---|---|---:|---:|
| R1 | | | |
| R2 | | | |
| R3 | | | |
| R4 | | | |

A teljes kiírt/mentett loss alapján hasonlítok, nem csak a kerekített szám alapján.
Az adatokat és az értelmezést én írom; a tutor nem tölti ki helyettem.

## Saját megfigyelések

- R1 → R2: mi változott a döntési határban és a validációs metrikákban?
- R2 → R3: ugyanazt a modellt részesíti előnyben a loss és az accuracy?
  Miért térhet el a két mutató szerinti rangsor?
- R3 → R4: hogyan változik külön a tanítási és a validációs loss-görbe?
  Milyen különbséget látok a kezdeti haladásban és a futás végén?
- Mi maradt azonos a rátakísérletben, és mi változott?
- Egy validációs mátrixcella: valódi címke → becsült címke, darabszám.
  Ha csak a főátlóban vannak értékek, mit jelent ez?

## Döntés – a teszt megtekintése ELŐTT

- Az R1–R4 közül ezt a futást választom:
- Pontos futási mappaneve:
- Az összehasonlított validációs értékek:
- Saját szavaimmal az indoklás:

Csak ezután töltöm ki a G03_04 két üres szövegét. A korábbi mentett modell
betölthető, nem kell hozzá a G03_03 aktuális kódját visszaállítanom.

## Végső teszt és az ábrák értelmezése

- Tesztpontosság:
- Tesztveszteség:
- Egy tévesztés: valódi címke → becsült címke és darabszám.
  Hibátlan esetben a főátló és az átlón kívüli nullák jelentése:
- Mely adatokra vonatkozik a mért pontosság, és mit nem garantál új pontokra?

A Nézetet frissítettem, és a kiválasztott futás vegso_teszt mappáját néztem.
A teszteredmény alapján már nem választok új modellt. Az ábrák megbeszélése
után következik Inno tíz feleletválasztós kérdése.
