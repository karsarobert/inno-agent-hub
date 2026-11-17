# Tutorsegédlet

## Rövid analóg példa

Szükség esetén mutasd ezt a más tárgyú mintát:

```python
class Pontgyujto:
    def __init__(self):
        self.pont = 0

    def novel(self, mennyivel):
        self.pont += mennyivel

    def aktualis(self):
        return self.pont
```

A self.pont az adott példány állapota; a novel módosít, az aktualis
visszaad. A büfés feladat elad metódusa módosít és összeget is visszaad.
Ne tanítsd azt, hogy egy módosító metódus mindig None-t ad vissza.

## Célzott segítség

A1: „A nev helyi paraméter vagy példányon tárolt adat?”
„Hány lista jön létre, ha a class törzsébe írod?”
„Az értékadás lemásolja a szótárat?”

A2: „A kulcsot vagy az árat vizsgálod?”
„A 0 ár hiányzó terméket jelent?”
„Ettől a számítástól változnia kell a bevételnek?”

A3: „Melyik saját metódusod ellenőrzött már?”
„Módosítasz az érvényesség ellenőrzése előtt?”
„Egy rekord egy termékdarabot vagy egy eladást jelent?”

B1: „Volt új példányosítás a második név létrehozásakor?”
„Melyik példányt éri el most a self?”
„A __str__ visszaad vagy csak kiír?”

Z1: „Már egész számot kapsz, vagy szöveget?”
„Melyik hiba egy soré, és melyik az egész fájlé?”
„Hiányzó bemenetnél eljutunk a jelentésírásig?”

Ha összekeverednek a nevek és objektumok, használj rövid táblázatot:
név | melyik példány | bevétel | értékesítések száma.
Ne kérj memóriacímeket. Az is azonos objektumot vizsgál, nem
általános tartalmi egyenlőséget.

Ne elégedj meg azzal, hogy „lefutott”: a változatlanul maradó
állapotot is nézzétek meg. Ha az eredmény már megvan, fogadd el.
Az ellenőrzőkód feltételeket vizsgál, nem kész Bufe-megoldás.
