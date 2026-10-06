# T1 – Elméleti teszt: szótáras büfé

10 kérdés, összesen 10 pont. Javasolt idő: 10 perc.
Válaszolj röviden, saját szavaiddal, az E1–E10 azonosítókkal. Nem kell tankönyvi definíció.
Elsőre a tananyag és a megoldókulcs megnyitása nélkül dolgozz. Ha segítséget kérsz, azt a tutor jelzi az értékelésben.
Az értékelés a T2 válaszai után következik, hogy a magyarázatok ne súgják meg a kódfeladatokat.

## E1 – Kulcs és érték

Az `arak = {"tea": 320}` szótárban mi a kulcs, és mi az érték?

## E2 – Hiányzó kulcs

Mi a különbség az `arak[termek]` és az `arak.get(termek)` között, ha a `termek` nincs a szótárban?

## E3 – Tagságvizsgálat

Mit vizsgál a `termek in arak`: a kulcsok vagy az értékek között keres?

## E4 – Egy pár bejárása

A `for termek, ar in arak.items():` sorban mit kap a `termek`, és mit kap az `ar` változó?

## E5 – Frissítés vagy hozzáadás

Mikor módosít meglévő bejegyzést, és mikor vesz fel új bejegyzést az `arak[termek] = uj_ar` sor?

## E6 – Hiány vagy nulla

Miért az `ar is None` feltételt használjuk a hiányzó ár jelzésére az `if not ar` helyett?

## E7 – Visszaadás és kiírás

Miért célszerű a `kosar_osszege` függvénynek visszaadnia az összeget ahelyett, hogy csak kiírná?

## E8 – Lista és szótár együtt

Miért a kosárlistát járjuk be a rendelés összegzéséhez, és nem az árjegyzék összes kulcsát?

## E9 – Egyetlen árforrás

Miért adjuk át ugyanazt az árjegyzéket a blokkmegjelenítő és az összegző függvénynek?

## E10 – Határértékpróba

A szabály: a keretbe pontosan beleférő termék is megfizethető. Egy 600 Ft-os keretnél milyen három, közvetlenül a határ körüli árral tesztelnél, és melyiket fogadnád el?
