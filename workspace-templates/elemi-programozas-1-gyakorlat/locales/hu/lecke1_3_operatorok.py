# -*- coding: utf-8 -*-
"""
LECKE 1 - 3. FAJL: Operátorok viselkedése (kód + viselkedés)
=============================================================
Futtasd a terminálból:
    python lecke1_3_operatorok.py

Feladat: figyeld meg a KIEMELT sorok viselkedését. Több meglepő
eredmény van - gondold át, miért viselkedik így a Python.
"""

print("=== Osztás: / és // (dupla per) ===")
print("5 / 2  =", 5 / 2)    # lebegőpontos (valós) osztás -> 2.5
print("5 // 2 =", 5 // 2)   # egész osztás -> 2
print("A '/' lebegőpontos, a '//' egész osztást végez.")

print()
print("=== Maradékos osztás és hatványozás ===")
print("5 % 2  =", 5 % 2)    # a maradék -> 1
print("5 ** 2 =", 5 ** 2)   # hatványozás -> 25

print()
print("=== Meglepetés: szöveg szorozva számmal ===")
print("'ha' * 5 =", "ha" * 5)
print("5 * 'ha' =", 5 * "ha")
print("('Na' * 10) + ' BATMAN' =", ("Na" * 10) + " BATMAN")
print("A '*' a szöveggél 'többszörözés': megismétli a szöveget.")

print()
print("=== Hozzárendelő operátorok += / -= ===")
szam = 10
print("eredeti szam =", szam)
szam += 1
print("szam += 1 ->", szam)
szam -= 1
print("szam -= 1 ->", szam)

print()
print("=== FONTOS: a ++ és -- NEM létezik Pythonban ===")
print("A 'szam++' és 'szam--' hiba (SyntaxError) lenne.")
print("Helyette: 'szam += 1' és 'szam -= 1' a helyes.")

print()
print("Megfigyelési kérdés: miért ad '5 / 2' 2.5-öt, de '5 // 2' 2-t?")
