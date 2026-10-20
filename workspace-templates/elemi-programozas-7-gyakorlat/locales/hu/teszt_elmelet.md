# T1 – EP_07 elméleti teszt

10 rövid kérdés, 10 pont, tervezetten 10 perc. Saját szavaiddal, E1–E10 jelöléssel válaszolj. Az első válaszadás előtt ne nyisd meg a tananyagot vagy a megoldókulcsot. Segítséget kérhetsz; azt külön jelöljük. A helyességet a T2 teljes válaszadása után beszéljük meg, hogy a magyarázatok ne súgjanak másik kérdéshez.

## E1 – Tuple mezői

A `tetel = ("tea", 2, 350)` milyen adatszerkezet, és mit jelent a három mező a rendelési példában?

## E2 – Az egyelemű tuple

Mi a különbség az `(5)` és az `(5,)` között? Melyik írásjel dönt, és miért?

## E3 – Információvesztés

Mely két fontos információ nem állítható vissza általában a látogatási vagy kosárlistából készített halmazból?

## E4 – Index és bejárás

Miért hibás a `halmaz[0]`, miközben a halmaz bejárható? Milyen típusú értéket ad a `sorted(halmaz)`?

## E5 – Halmaz módosítása

Mi történik meglévő elem újabb add hívásakor? Mi a különbség a remove és a discard között hiányzó elemnél?

## E6 – Különbség és szimmetrikus különbség

Milyen elemek vannak az `elso - masodik`, és milyenek az `elso ^ masodik` eredményében?

## E7 – Részhalmaz

Mit vizsgál az `elso <= masodik` halmazoknál, és miért True a `set() <= masodik`?

## E8 – Háromféle darabszám

Mit számol a `len(kosar)`, a `len(set(kosar))` és a `kosar.count(keresett_termek)`?

## E9 – Módosíthatóság és paraméterátadás

A list, dict, set, int, str és tuple közül melyek módosíthatók? Más átadási módra vált-e a Python szám és lista esetén, vagy mi magyarázza az eltérő hatást?

## E10 – Értékadás vagy helyben módosítás

Egy függvényben miben tér el a paramétert jelölő `lista = ["tea"]` és a `lista.append("tea")` hatása a hívó eredeti listájára?
