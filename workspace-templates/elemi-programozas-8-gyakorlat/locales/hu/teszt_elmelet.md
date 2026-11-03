# T1 – EP_08 elméleti teszt

10 kérdés, tervezetten 10 perc. Mindegyik kérdésnél egy helyes válasz van: add meg az azonosítót és a betűt, például E1: B. A teljes két tesztrész végéig nincs helyességi visszajelzés. Önálló válaszadáskor ne nyisd meg a megoldókulcsot. A tananyagban és főúton használt fogalmak szerepelnek; C1 vagy bináris fájlkezelés nem előfeltétel.

## E1

Mihez viszonyítja a Python az open("rendelesek.txt", ...) relatív fájlnevet?

- A) Mindig a megnyitott .py fájl könyvtárához.
- B) A program aktuális munkamappájához.
- C) Mindig a Letöltések mappához.
- D) A böngészőben megnyitott HTML helyéhez.

## E2

Mit biztosít a with open(...) as fajl szerkezet a blokk elhagyásakor?

- A) Az összes adat automatikus listává alakítását.
- B) A kurzor automatikus visszaállítását a fájl elejére.
- C) Minden üres sor automatikus kihagyását.
- D) A fájl automatikus lezárását, akkor is, ha a blokkban kivétel történik.

## E3

Mit jelent a readline eredménye: "\n", illetve ""?

- A) Az első lehet üres sor sortöréssel, a második fájlvég.
- B) Mindkettő fájlvég, tehát felcserélhetők.
- C) Az első fájlvég, a második mindig üres fájlsor.
- D) Mindkettő None.

## E4

Melyik állítás helyes szöveges fájlnál?

- A) A readlines egyetlen str értéket ad.
- B) A read mindig számokat ad, ha számokat lát a fájlban.
- C) A read str értéket, a readlines sorokat tartalmazó listát ad.
- D) A for fajl bejárás minden bájtot külön int-ként ad.

## E5

Melyik állítás írja le helyesen a split() és split(";") szerepét?

- A) Mindkettő kizárólag szóköznél bont.
- B) A split() whitespace mentén bont; a split(";") a pontosvessző mezőelválasztót használja.
- C) A split(";") az ármezőt automatikusan egész számmá alakítja.
- D) Mindkettő szótárat ad.

## E6

Mit tesz a szo.strip(".,!?")?

- A) A szó minden belső pontját és vesszőjét is eltávolítja.
- B) Csak a pontosan ".,!?" alakú teljes részszöveget törli.
- C) Kisbetűsíti a teljes szót.
- D) A szó két széléről levágja a felsorolt karaktereket, amíg ilyeneket talál.

## E7

A keresett szavak {"finom", "gyors"}, a bemeneti fájl üres. Mi az A2 előírt eredménye?

- A) {"finom": 0, "gyors": 0}, tetszőleges kulcssorrenddel.
- B) {} minden esetben.
- C) None, mert nincs értelmezhető eredmény.
- D) {"finom": 1, "gyors": 1}, mert két keresett szó van.

## E8

Mikor ürül ki egy már létező fájl, ha sikeresen w módban megnyitjuk?

- A) Csak az első nem üres write híváskor.
- B) Csak a with blokk végén.
- C) Már a megnyitáskor.
- D) Soha; a w hozzáfűz.

## E9

Mi igaz az a módra és a write műveletre?

- A) Az a automatikusan eltávolítja az azonos régi sorokat.
- B) Az a hozzáfűz, a write pedig nem ad automatikusan sortörést.
- C) Az a minden futáskor üres naplót készít.
- D) A write mindig tesz sortörést az új rekord elé és mögé.

## E10

A naplóban kávé;400 szerepel, a mai árjegyzékben a kávé ára 500. Milyen árral számol a B1.b?

- A) 500-zal, mert mindig a legfrissebb ár a helyes.
- B) 0-val, mert az eltérő ár hibás adat.
- C) A kettő átlagával, 450-nel.
- D) A fájlban tárolt 400-zal, egész számmá alakítás után.
