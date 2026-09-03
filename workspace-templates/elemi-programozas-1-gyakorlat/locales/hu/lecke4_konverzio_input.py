# -*- coding: utf-8 -*-
"""
LECKE 4 - Típuskonverzió és input()
===================================
Futtasd:  python lecke4_konverzio_input.py

A program adatot kér a terminálban. Írj be egy nevet és két egész számot.
Figyeld meg, mi történik az input() után, majd a konverzió után.
"""

print("=== Típuskonverziók ===")
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(42), type(str(42)))

print()
print("=== Interaktív program ===")
nev = input("Hogy hívnak? ")
print(f"Szia, {nev}!")

print()
print("=== Két szám összege ===")
# Fontos: az input() eredménye mindig str.
# Ezért alakítjuk int-té a beolvasott szöveget:
a = int(input("Első egész szám: "))
b = int(input("Második egész szám: "))
osszeg = a + b
print(f"Az összeg: {osszeg}")

print()
print("=== Megfigyelési kérdések ===")
print("1. Mi lenne, ha az int() konverziót kihagynánk?")
print("2. Mi történik a '3' + '4' művelettel, ha mindkettő string?")
print("3. Miért kell a számot str()-ré alakítani, ha '+' jellel szöveghez fűznénk?")
