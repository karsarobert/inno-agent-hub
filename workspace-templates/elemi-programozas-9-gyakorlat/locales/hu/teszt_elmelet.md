# T1 – EP_09 elméleti teszt

10 kérdés, tervezetten 10 perc. Mindegyiknél egy helyes válasz van; add meg az azonosítót és betűt, például E1: A. A teljes két tesztrész végéig nincs helyességi visszajelzés. Elsőre önállóan válaszolj, a kulcs megnyitása nélkül. A kérdésekhez a főút elég; C1 nem előfeltétel.

## E1

Melyik helyzet okoz itt ValueError-t?

- A) int("alma") konverzió.
- B) 800 Ft-hoz 500 egész forint felajánlása önmagában.
- C) 0 árú víz három darabjának helyes összegzése.
- D) Létező üres fájl for ciklusos bejárása önmagában.

## E2

A naplot_beolvas nem találja a fájlt. Mi felel meg az A3.b szerződésének?

- A) Csendben ([],[],0)-t ad, így nincs hiba.
- B) Létrehoz egy üres bemeneti fájlt.
- C) A FileNotFoundError-t továbbengedi a B1 hívójának.
- D) A hibás fájlnév helyett másik naplót választ.

## E3

A későbbi jó sorokat is fel akarjuk dolgozni. Hol kezeljük az adott sor ValueError-ját?

- A) A teljes ciklus után, új ciklus nélkül.
- B) A cikluson belül, az adott sor értelmező hívása körül.
- C) Csak a program legvégén, csupasz excepttel.
- D) A finally blokkban, a hibás rekordot 0-val pótolva.

## E4

Mi a tetel_osszege és a hívó szereposztása?

- A) A függvény csak hibaszöveget printel, a hívó kitalálja, történt-e hiba.
- B) A függvény ismeretlen termékre 0-t ad, a hívó 0-nál hibát állít.
- C) A függvény minden hibát elnyel, mert máskülönben nem hibatűrő.
- D) A függvény tiltott értékre ValueError-t jelez, a hívó célzottan kezeli és közli.

## E5

Melyik eladási sor érvényes a feladat szerint?

- A) víz;3;0
- B) tea;0;350
- C) tea;1;-50
- D) ;1;100

## E6

A fájl első sora jó, a második üres, a harmadik hibás. Melyik hibasorszám helyes?

- A) 2, mert az üres sort nem tekintjük sornak.
- B) 1, mert a hibaszámláló most lett egy.
- C) 3, mert az eredeti fizikai sorszámot őrizzük.
- D) 0, mert a Python minden számlálót így kezd.

## E7

Mikor helyes a B1 Mentett jelentés sikerüzenete?

- A) A függvény legelején, mert a fájlnév adott.
- B) A mentő rendes befejezése után, ha a with lezárása is sikerült.
- C) A finally-ban, mert az biztos lezárást jelent.
- D) Bármikor, ha már létezik régebbi jelentésfájl.

## E8

Melyik állítás helyes a finally-ról a bemutatott rendes vezérlési esetekben?

- A) Csak akkor fut, ha az except talált hibát.
- B) Ha return van a try-ban, a finally mindig kimarad.
- C) A finally-beli return nem módosíthatja a korábbi eredményt.
- D) A try szerkezet elhagyásakor siker, kezelt/terjedő kivétel és return esetén is lefut.

## E9

Mit jelent a kávé;2;450 rekord a riportban?

- A) Egy rekord, két eladott darab és 900 Ft tárolt bevétel.
- B) Két rekord, egy darab és 450 Ft bevétel.
- C) Egy rekord, 450 darab, mai áron számított bevétel.
- D) Egy rekord, két darab, de az árat kötelező a mai árjegyzékből kikeresni.

## E10

A Z1 kosarában van jó és hibás tétel is. Mi a helyes első visszatérési érték?

- A) A jó tételek összege, hogy legalább részfizetés történjen.
- B) 0, mert minden hiba nulla összegnek számít.
- C) None, mert a teljes kosár ellenőrzése nem sikerült.
- D) A ValueError szövege az összeg helyén.
