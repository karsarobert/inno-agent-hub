# CPP_07 – Leckeutasítások

## Menet

| Blokk | Részek | Irányadó idő |
|---|---|---|
| 1. | G07_01: 12, G07_02: 12, G07_03: 10, G07_04: 11 perc | 45 perc |
| 2. | A PROJEKT P1–P6 lépései | 45 perc |
| 3. | T1: 15, T2: 25, visszajelzés: 5 perc | 45 perc |

Az idők támpontok, nem automatikus teljesítési feltételek. Minden új rész előtt:
nagy kép → analóg minta → kulcssorok magyarázata → egy teendő → RUN → értelmezés.

## G07_01 – Saját struktúra és önálló másolat

**Fájl:** G07_01_struktura.cpp. **Minta:** M1.

### A – egy mérés adatai

Nagy kép: három összetartozó adatból egyetlen összetett értéket készítünk.
A hallgató a main előtt definiáljon `Meres` típust. Mezői: egész `azonosito`,
`double ertek`, logikai `ervenyes`. A main-ben hozzon létre `eredeti` nevű
objektumot a starter kezdőadataiból, és írja ki mindhárom mezőt.

Ne add oda elsőre a konkrét típusdefiníciót a feladat saját neveivel.
Ellenőrzés: 101, 23.5, igaz; az `1` logikai kiírás is helyes.
Egy rövid megértési kérdés: melyik rész a típust, melyik a konkrét objektumot hozza létre?

### B – másolat és értékadás

Az eredeti alapján hozzon létre `masolat` nevű új objektumot, annak értékét
állítsa 30-ra. Írja ki az eredeti és a másolat értékét. Egy külön lépésben másolja
az eredetit a már létező másolatba, és írja ki újra mindkettőt.

Ellenőrzés: előbb `23.5 30`, utána `23.5 23.5`.
Nevezd nevén: másoló inicializálás, majd másoló értékadás.
Magyarázd meg a helyi inicializálatlan objektum és az üres kapcsos zárójellel
inicializált egyszerű struktúra különbségét; inicializálatlan mezőt ne olvassatok ki.

## G07_02 – Érték szerint kapott struktúra és mutató

**Fájl:** G07_02_masolas.cpp. **Minták:** M2, majd M3.
Itt a típus és egy eredeti mérés adott, hogy az új műveletekre koncentrálhassunk.

### A – módosított másolat visszaadása

M2 után készítsen `emeltMasolat` függvényt. Egy mérést érték szerint és egy
double növekményt kapjon, növelje a saját paraméterének mért értékét, majd adja
vissza a teljes módosított struktúrát. A többi mező ne változzon.
Hívja meg az eredetivel és 2.0 növekménnyel; az eredményt új változóban tárolja.

Ellenőrzés: eredeti 10.5, új 12.5; mindkét azonosító 201, a jelző igaz.
Magyarázd el a visszatérési típust, a saját paraméterobjektumot és a return szerepét.

### B – az eredeti elérése mutatóval

M3 után hozzon létre mutatót az eredetire, majd ezen keresztül növelje annak
értékét 1.5-del. Ehhez még nem kell új függvény. Írja ki az eredeti és az A részben
kapott másolat értékét.

Ellenőrzés: eredeti 12, másolat 12.5. A mutató címet tárol, az eredeti objektumot
éri el; nem készül újabb másolat. Magyarázd el a nyíl és a zárójeles dereferálás
egyenértékűségét, de a konkrét hallgatói értékadó sort ne írd be helyette.

## G07_03 – Unió és a változat nyilvántartása

**Fájl:** G07_03_unio.cpp. **Minta:** M4.
Nagy kép: az eredmény egész darabszám VAGY tört érték; a két alternatívát nem
tároljuk egyszerre, ezért nyilvántartjuk, melyik olvasható.

### A – egész eredmény

Definiáljon `SzamAdat` uniót `egesz` (int) és `tort` (double) mezőkkel. Egy
`Eredmeny` struktúra fogjon össze `egeszTipusu` logikai jelzőt és `adat` nevű
SzamAdat mezőt. Hozzon létre objektumot, állítsa be az egész kezdőértéket és a
hozzá tartozó jelzőt. If alapján csak a jelzőnek megfelelő mezőt írja ki.

Ellenőrzés: 7, egész mező aktív, jelző igaz.

### B – váltás tört értékre

Ugyanennek az objektumnak állítsa be a tört mezőjét 2.5-re, frissítse a jelzőt,
és a jelző alapján írja ki a tört eredményt. A kiírást kiszervezheti void
függvénybe, de ez itt nem kötelező.

Ellenőrzés: 2.5. A korábbi egész mezőt ekkor nem olvassuk ki.
Rövid kérdés: ki tartja összhangban a jelzőt és az uniót? A program, nem automatikusan a fordító.
Ha sizeof-ot is használ, ne követelj konkrét méretet; az igazítás is számít.

## G07_04 – Blokk, névelrejtés és ciklusváltozó

**Fájl:** G07_04_hatokor.cpp. **Minta:** M5.

### A – három külön objektum ugyanazzal a névvel

Adott a globális `szam`, értéke 5. A main-ben hozzon létre azonos nevű helyi
változót 10 értékkel, majd egy külön belső blokkban ismét ilyen nevűt 20 értékkel.
Írja ki a belső értéket, a blokk után a main helyi értékét, végül a globálisat
minősített névvel.

Ellenőrzés: 20, 10, 5. Ugyanabban a blokkban nem lehet két ilyen lokális
változódefiníció. A külső objektum a belső blokkban is létezik, csak a neve rejtett.

### B – a függvény nem a hívó helyi változóját látja

Hívja meg a starter `globalisKiirasa()` függvényét a main-ből.
Ellenőrzés: 5. A main helyi 10-es értéke változatlan. A névkeresést a függvény
kódjának helye alapján értelmezzétek, ne a hívás pillanatnyi blokkja alapján.

### C – a ciklus fejlécében deklarált változó

Külső összegváltozóba, for ciklussal összegezze az 1, 2, 3 értékeket.
Az index a ciklus fejlécében legyen deklarálva. A ciklus után írja ki az összeget.
Ellenőrzés: 6. Ezután egyszer próbálja a ciklus után kiírni az indexet is:
ennek a névnek a használata fordítási hibát okoz. Távolítsa el a hibás kiírást,
és fordítson/futtasson újra. Sikertelen fordítás után ne fusson régi bináris.

Zárásként különítsd el a név hatókörét és az objektum élettartamát. Az itteni
automatikus belső változó a blokk elhagyásakor megszűnik.

## A következő két blokk

Vezesd a PROJEKT P1–P6 lépéseit a megjelölt analóg mintákkal. Az ellenőrző
adatok a TUTOR_KULCS-ban találhatók. Ezután a ZARO_TESZT húsz kérdése
következik, egyenként, változatlan sorrendben; ne rögtönözz helyettük új feladatokat.
