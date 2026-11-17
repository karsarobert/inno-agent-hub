# Saját büfé objektumokkal

## Teljes cél

Egy Bufe osztályt készítesz, majd előkészített fájlos alkalmazásban
használod. A számítás, az állapotváltozás és a megjelenítés szerepét
külön figyeld meg.

A bufe.py fájlban ugyanazt az osztályt bővítsd; ne másolj egymás alá
több teljes Bufe-definíciót.

Az induló árlista:

    {"tea": 300, "szendvics": 700, "viz": 0}

A terméknevek kis- és nagybetűérzékenyek. A viz ingyenes, érvényes termék.
Előfeltétel: a név szöveg; az árlista nem üres terméknevekhez nem negatív
egész árakat rendel; a mennyiségi paraméter egész szám.
Most nem készítünk általános típusellenőrzést.

## A1 – A büfé kezdeti állapota

Készítsd el az __init__(self, nev, arak) metódust.

- A név elejéről és végéről tűnjenek el a szóközök.
- Az üresre tisztított név ValueError-t okozzon.
- self.nev a megtisztított név.
- self.arak az induló szótár saját másolata.
- self.bevetel kezdetben 0.
- self.eladasok kezdetben saját üres lista.

Két példány ne ugyanazt a módosítható tárolót használja.
Az eredeti árlista későbbi átírása ne módosítsa a büfé árlistáját.

Próba: python3 probak.py A1

Magyarázd el röviden, miért nem elegendő az önálló belső állapothoz
önmagában az, hogy két külön Bufe(...) hívást írtál.

## A2 – Számítás állapotváltoztatás nélkül

Készítsd el a tetel_osszege(self, termek, darab) metódust.
Előbb ellenőrizd a pozitív darabszámot, majd a termék jelenlétét.
Hibát ValueError jelezzen érthető üzenettel.
Érvényes kérésnél add vissza a teljes árat.

A metódus nem növeli a bevételt, nem rögzít értékesítést,
nem módosítja az árlistát, nem ír ki és nem kér be adatot.

- tea, 2 → 600
- viz, 3 → 0
- tea, 0 → ValueError
- kave, 1 → ValueError

Próba: python3 probak.py A2

## A3 – Sikeres értékesítés rögzítése

Készítsd el az elad(self, termek, darab) metódust.
A számításhoz használd a saját tetel_osszege metódusodat.
A feltételeket ne másold át még egyszer.

Siker esetén növeld a bevételt, fűzd az eladasok listához a
(termek, darab, osszeg) tuple-t, és add vissza az összeget.
Hibás kérésnél sem a bevétel, sem az értékesítési lista nem változhat.

A 0 Ft-os eladás is bekerül a listába. Az eladás sikerét nem
vizsgálhatod az összeg egyszerű igazságértékével.

Próba: python3 probak.py A3

## B1 – Két büfé és egy második név

A peldanyok.py fájlban írj főprogramot:

1. Hozz létre két külön büfét ugyanabból az induló árlistából.
2. Csak az elsőn adj el két teát.
3. Ellenőrizd mindkét büfé bevételét és értékesítési listáját.
4. A masik névhez rendeld hozzá az első büfét.
5. A masik néven keresztül adj el egy szendvicset.
6. Ellenőrizd, melyik büfé változott.
7. Az is segítségével is vizsgáld az objektumazonosságot.

Az első bevétele ekkor 1300 Ft, a másodiké 0 Ft.
A masik és az első büfé ugyanaz az objektum.

A bufe.py fájlban készíts __str__ metódust. A pontos formátum:

    Iskolai büfé: 2 értékesítés, 1300 Ft bevétel

A név, a darabszám és a bevétel az aktuális objektumból jöjjön.
Az „értékesítés” egy sikeres elad hívás, nem a termékdarabok összege.
A __str__ szöveget adjon vissza, és ne változtasson állapotot.

Futtasd külön a kozos_lista.py fájlt. Keresd meg, miért közös benne
a lista, és javítsd úgy, hogy példányonként külön lista jöjjön létre.
Ez külön hibakeresési példa, nem új Bufe-változat.

Próbák:

    python3 peldanyok.py
    python3 kozos_lista.py
    python3 probak.py B1

## Z1 – A saját osztályod a teljes programban

Nyisd meg a feldolgozas.py fájlt. Készen kapod a beolvasást,
a sorok szerkezeti ellenőrzését, a jelentésírást, a fájlhibák
kezelését és a munkamenet szervezését.

A te részed: ertekesiteseket_vegrehajt(bufe, tetelek, hibak).
A tetelek elemei: (sorszam, termek, darab).

Minden tételnél hívd a kapott bufe elad metódusát.
ValueError esetén a hibak listához kerüljön (sorszam, str(hiba)).
Egy hibás tétel után folytasd a következővel. A kapott büfét
módosítod, nem hozol létre minden sorhoz új példányt.
A függvénynek nem kell visszatérési értéket megadnia.

A sorok külön értékesítések, nem egy közös, csak egyben elfogadható kosár.

Futtasd a programot a jó, vegyes és üres fájllal: ehhez a főprogram
bemenet változóját módosítsd. A jelentést minden futás után nyisd meg;
szükség esetén frissítsd a nézetet.
Hiányzó fájlnál a régi jelentésnek változatlanul kell maradnia.
A bemenetet ne add meg jelentési célként.

Próbák:

    python3 feldolgozas.py
    python3 probak.py Z1
