# Elméleti záróteszt

10 perc. Kérdésenként egy helyes válasz.

## E01

Melyik állítás helyes?

A. Az osztály egyetlen konkrét büfé bevétele.
B. Egy osztályból több külön példány készíthető.
C. Minden példány automatikusan ugyanazt a listát használja.
D. A példány nem tárolhat adatot.

## E02

Mit ér el a self egy szokásos példánymetódusban?

A. Mindig az elsőként létrehozott példányt.
B. Egy automatikusan készített másolatot.
C. Az aktuális hívás példányát.
D. A főprogram összes változóját.

## E03

Mi az __init__ szerepe?

A. Beállítja a példány kezdeti állapotát.
B. Kötelezően visszaadja a kész példányt.
C. Minden metódushívás előtt újraindul.
D. Csak szöveget jeleníthet meg.

## E04

Mi történik a masik = bufe értékadáskor?

A. Új Bufe példány készül.
B. Csak az attribútumok másolódnak.
C. Új árlista és értékesítési lista készül.
D. A két név ugyanazt az objektumot éri el.

## E05

Hová kerüljön a külön büfék saját üres értékesítési listája?

A. Egyetlen globális változóba.
B. Az __init__-ben a self.eladasok attribútumhoz.
C. Kizárólag a __str__ helyi változójába.
D. Mindig a class törzsébe, közös listaként.

## E06

Miért elegendő itt az árlista sekély másolata?

A. A szótárhoz eleve nem tartozhat módosítható érték.
B. A sekély másolat minden beágyazott objektumot is lemásol.
C. Új külső szótár kell, az értékek pedig nem módosítható egészek.
D. Mert a másolás után nem változhat a szótár.

## E07

Mit jelent az elad 0 visszatérési értéke ebben a feladatban?

A. Sikeres, ingyenes értékesítés is lehet.
B. Mindig ismeretlen terméket.
C. A metódus nem futott le.
D. Az értékesítési lista biztosan üres.

## E08

Mikor változhat az állapot az elad metódusban?

A. A bemenet ellenőrzése előtt.
B. Minden kérésnél, a hibást is beleszámítva.
C. Csak pozitív összegnél.
D. Az érvényesség ellenőrzése és a számítás után.

## E09

Mit kell a __str__ metódusnak adnia?

A. Egy kiíratás nélkül is tovább használható szöveget.
B. Mindig None-t.
C. Egy tetszőleges listát.
D. Kötelezően közvetlen konzolos kiírást.

## E10

Mi történjen hiányzó bemeneti fájlnál?

A. Üres, sikeres jelentés készüljön.
B. Az árlistát törölni kell.
C. Hibajelzés után ne induljon jelentésmentés.
D. A fájlt automatikusan eladásokkal kell feltölteni.
