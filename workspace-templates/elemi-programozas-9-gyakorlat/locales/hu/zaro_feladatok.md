# Z1 – Önálló kosárellenőrzés részfizetés nélkül

**Fájl:** onallo.py. **Tervezett idő:** 12 perc.

## A teljes cél

A kosar lista (terméknév, darabszám) tuple-öket tartalmaz. A kosarat_ellenoriz(kosar, arak) az összes tételt megvizsgálja, és két értéket ad vissza:

- Ha minden tétel érvényes: (teljes_egész_összeg, []).
- Ha akár egy tétel hibás: (None, hibalista). A hibalista (1-től_számozott_tétel, értelmes_üzenet) tuple-öket tartalmaz minden hibás tételhez.

Ez a feladat a részleges naplóösszesítéstől eltérő szabályt alkalmaz. A jó tételek részösszege hibás kosárnál nem kerül fizetendőként visszaadásra. Egy fizetési döntéshez teljesen ellenőrzött rendelés kell. A 0 összeg lehet helyes, a None tiltást jelent.

## Mi adott?

Az A2-függvény aláírása, a Z1 aláírása, a kezdőárjegyzék és próbakosár. A helykitöltő A2-definíciót a saját tetel_osszege függvényeddel váltsd ki, a főprogramját ne másold át. A kosár minden eleme eleve kételemű tuple; a darab egész, a terméknév már tisztított szöveg. A tétel üzleti érvényességét a saját A2-függvényed jelzi. A paraméterek és előfeltételek nem kérnek új típusellenőrző keretrendszert.

## Követelmények

1. Az összes tétel ellenőrzésekor a saját A2-függvényedet használd. Ha egy tétel ValueError-t jelez, a többi vizsgálatát is végezd el, és minden hibás tétel sorszámát/okát add vissza.
2. Hibátlan kosárhoz a teljes összeg, hibás kosárhoz None legyen az első visszatérési érték. Üres kosárhoz (0, []) tartozik.
3. A függvény nem kérdez, nem ír ki, nem ír fájlt és nem változtatja a kosarat vagy az árjegyzéket. A kulcsok és árak a paraméterből származnak.
4. A főprogram a nyers kezdeti kiírás helyett érthető döntést adjon. Hiba esetén közölje, hogy a fizetés nem indítható, és sorolja fel a hibás tételszámokat/okokat. Ne mutasson Fizetendő: … sikerüzenetet vagy részösszeget. Hibátlan esetben a teljes Fizetendő: … Ft jelenjen meg. Üres kosárnál külön Nincs rendelés üzenet is elfogadott.
5. Nem kell inputot vagy fájlírást hozzáadnod: a feladat az ellenőrzési döntésről szól. A már ismert A1-bekérést ne indítsd el a próbák közben.

## Elfogadás

- Minden tételt vizsgál, minden ValueError-t a hozzá tartozó tételsorszámmal gyűjt.
- Hibánál az első eredmény None; a jó 0 összeg ettől különbözik.
- Az összeg valódi árakból és mennyiségekből készül; az ismétlődő tétel is számít.
- A hívó üzenete a visszaadott döntést követi, a paraméterek változatlanok; a szükséges próbák ismertek.

## Próbák

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | kosar=[("kávé",2),("víz",3)]; alapárjegyzék | (900, []); a főprogram Fizetendő: 900 Ft üzenetet ad. |
| Z1.2 | kosar=[("víz",3)] | (0, []); a 0 valós fizetendő összeg, nem hibajelzés. |
| Z1.3 | kosar=[("kávé",1),("kakaó",1),("tea",0),("víz",2)] | (None, hibalista), két hiba a 2. és 3. tételhez. Nincs Fizetendő sikerüzenet és nincs 450 Ft-os részfizetés. |
| Z1.4 | kosar=[] | (0, []), hiba nélkül; a főprogram közölheti, hogy nincs rendelés. Nem kér fizetési inputot. |
| Z1.5 | kosar=[("tea",2),("tea",1)]; az árjegyzék tea ára előbb 400 | (1200, []); az ismétlődő tételek mind számítanak. Minden Z1-próbában a kosár és árjegyzék változatlan. |

## Tutori segítség

Elsőre csak a követelményt, a kétféle visszatérést és a próbákat tisztázd. Ne add előre a ciklust, a try helyét vagy kész célkifejezést. Valódi elakadáskor külön vizsgáld: tételösszeg, több hiba összegyűjtése, összesített döntés vagy hívói üzenet. Csak az érintett fogalomhoz adj fokozatos segítséget. A kész célmegoldást ne diktáld le egymás utáni darabokban.
