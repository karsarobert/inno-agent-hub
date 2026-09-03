# -*- coding: utf-8 -*-
"""
LECKE 3 - Változók és dinamikus típusosság
==========================================
Futtasd:  python lecke3_valtozok.py

Ebben a leckében a VÁLTOZÓK viselkedését figyeled meg, főleg a
dinamikus típusosságot: ugyanaz a változó más-más típusú adatot
is tárolhat.
"""

print("=== Változó létrehozása és egyszerű típus ===")
az_en_valtozom = "valami szöveg"
print(az_en_valtozom)
print(type(az_en_valtozom))

print()
print("=== Dinamikus típusosság: a változó TÍPUST IS cserélhet ===")
val = 42
print("val = 42   ->", type(val), "érték:", val)

val = 12.345
print("val = 12.345 ->", type(val), "érték:", val)

val = "sajt"
print("val = 'sajt' ->", type(val), "érték:", val)

print()
print("A 'val' változó előbb int, aztán float, végül str lett!")
print("Ezt hívjuk dinamikus típusosságnak.")

print()
print("=== Elemzés: típus lekérdezése type() segítségével ===")
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("szöveg")) # <class 'str'>
print(type(True))     # <class 'bool'>

print()
print("=== FELADAT ===")
print("Nézd meg, mit ad a type() az alábbi két változónál:")
e = 3.5
nev2 = "Anna"
print(type(e))
print(type(nev2))
