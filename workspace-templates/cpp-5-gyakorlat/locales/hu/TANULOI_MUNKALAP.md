# CPP_05 – hallgatói munkalap

## Időkeret

A gyakorlat **3 × 45 perc**.

- 1. blokk: saját függvények alapjai és prototípus
- 2. blokk: Mérési adatok elemzőja – projekt
- 3. blokk: 20 kérdéses ZH-felkészítő teszt

## Munkamód

A kódot te írod, mented és futtatod. Elsődlegesen a szerkesztő feletti **RUN**
gombot használd. Terminálból például:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G05_01_elso_fuggveny.cpp -o G05_01
./G05_01
```

Fordítási hiba esetén az első lényeges hibaüzenetet küldd el Innónak. Sikertelen
fordítás után ne egy régi futtatható program eredményét ellenőrizd.

## 1. blokk

1. `G05_01_elso_fuggveny.cpp` – első saját függvény; két külön művelet
2. `G05_02_parameterek.cpp` – két paraméter; terület és kerület
3. `G05_03_void.cpp` – visszatérési érték nélküli függvények
4. `G05_04_prototipus.cpp` – prototípus és a definíció helye

A starterek szándékosan nem tartalmazzák a kész függvényfejléceket vagy `return`
sorokat. Ha elakadsz, Inno először magyarázattal és kisebb mintával segít.

## 2. blokk – projekt

Nyisd meg a `P05_meresi_adatok.cpp` fájlt és kövesd a `PROJEKT.md` P1–P7 lépéseit.
A projekt során **egy fájlt fejlesztesz tovább**. Új rész előtt Inno egy rövid,
hasonló mintakódot mutat, majd te alkalmazod a mintát a saját programodra.

A `MINTAKODOK.md` példái segítségre szolgálnak, de ne másold át őket változtatás
nélkül: más problémát és más neveket használnak.

## 3. blokk – ZH-felkészítés

A `ZARO_TESZT.md` 20 előre megírt kérdését Inno egyenként teszi fel:

- T1: 10 feleletválasztós elméleti kérdés a mai anyagból;
- T2: 10 kódértési feladat, amelyekben a korábbi C++-anyag is visszatér.

A T2-ben lesz kimenetjóslás és hibakeresés. A teszt célja nem új anyag tanítása,
hanem annak megmutatása, mely témákat érdemes még átismételned a következő órai ZH előtt.

Nincs házi feladat.
