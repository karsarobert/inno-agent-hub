# Kezdjük az autoencoder-gyakorlatot!

A kicsomagolt munkamappában írd az Innónak:

> Kezdjük az 5. Deep Learning-gyakorlatot!

Először bemutatja az óra célját és kéri a `kornyezet_ellenorzes.py` futtatását.
Utána minden új program előtt elmagyarázza a példát és a fontos kódsorokat.
Te szerkesztesz, mentesz és a Run gombbal futtatsz. Nem kell `cd` parancs.

Minden példát először változtatás nélkül futtass. Csak az aktuálisan kért értéket
módosítsd. Pythonban a tizedesjel pont: például `0.025`, nem `0,025`.

## Képek és eredmények

Várd meg a **FUTÁS KÉSZ** sort. A program kiírja az új, rövid, sorszámozott mappát.
Frissítsd a Nézet mappát / fájllistát, és ebből az új mappából nyisd meg a képet.
A régebbi futások képei megmaradnak; összehasonlításhoz hasznosak.
Az `eredmeny.json` a beállításokat és számokat tartalmazza, nem kell szerkesztened.

## Ha elakadsz

- Hiányzó csomagnál kérd az oktató segítségét, és mutasd meg az utolsó hibasorokat.
- Hiányzó adatfájlnál ellenőrizd, hogy a teljes csomagot kicsomagoltad-e.
- A tanítás első indulásakor néhány másodperc csend normális lehet.
  Ne indíts ugyanabból több példányt.
- Ha régi beállítást ír ki a program, ellenőrizd, melyik fájlt mentetted és futtattad.
- Az `index` egész szám, 0 és 127 közötti; a 0. sor az első példa.
- A 3. és 4. program rögzített referenciát használ, ezért nem változik az eredményük
  attól, hogy a 2. programot más epochszámmal futtattad. Ez szándékos.

A jelalakok összehasonlításához nem kell orvosi ismeret. Ez gépi tanulási példa.
A végén tíz rövid kérdés és összegzés következik. Nincs házi feladat.


## Az új képek

- `axis_1.png`: két jel → két saját átlag; nem a valódi EKG-mérés.
- `precision_recall.png`: riasztások és valódi rendellenességek külön csoportként.
- `osszehasonlitas.png`: a saját 10 és 30 epochás rekonstrukció közös ábrája.
  Előbb az alap 10 epochát, majd a 30 epochát futtasd; a program csak megfelelő
  saját előzmény esetén készíti el a képet. A számok és görbék együtt értelmezendők.
