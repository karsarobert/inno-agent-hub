---
name: cpp-progress-tracker
description: Helyi, adatminimalizáló C++ tanulási haladásnapló vezetése a progress.json fájlban bizonyítékokkal és tanulói ellenőrzéssel.
---

# C++ haladáskövető

## Adatkezelési alapelv

A `progress.json` kizárólag a tanuló munkaterében marad. Ne küldd sehova, ne kérj teljes nevet, e-mail-címet vagy intézményi azonosítót. A `studentAlias` csak akkor tölthető ki, ha a tanuló azt kifejezetten kéri.

## Mikor frissítsd

Feladat vagy diagnosztikai beszélgetés végén ajánld fel a frissítést. Csak a tanuló jóváhagyásával írd át a fájlt.

## Mit rögzíts

- teljesített vagy folyamatban lévő modul;
- feladat relatív útvonala és rövid bizonyíték: például sikeres fordítás, tesztkimenet vagy a tanuló saját magyarázata;
- kompetenciaszint: `not_started`, `developing`, `secure` vagy `needs_review`;
- visszatérő, oktatásilag hasznos nehézség;
- következő kis, konkrét lépés.

## Amit ne rögzíts

- teljes beszélgetési átiratot;
- szükségtelen személyes adatot;
- érzékeny információt;
- modell által feltételezett diagnózist vagy címkét bizonyíték nélkül.

## Frissítési eljárás

1. Foglald össze egy mondatban, mit ért el a tanuló.
2. Kérdezd meg, egyetért-e az összesítéssel.
3. A meglévő JSON-sémát őrizd meg; ne töröld a korábbi bizonyítékot.
4. Mentsd a relatív fájlnevet és tömör bizonyítékot.
5. Mondd el, hogy a jelentés helyben marad, és bármikor szerkeszthető vagy törölhető.
