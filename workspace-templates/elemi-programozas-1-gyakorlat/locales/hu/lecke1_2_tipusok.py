# -*- coding: utf-8 -*-
"""
LECKE 1 - 2. FAJL: Alapvető adattípusok + type() (kód + viselkedés)
====================================================================
Futtasd a terminálból:
    python lecke1_2_tipusok.py

Feladat: figyeld meg, MIT ír ki, és MIÉRT. A program a type() függvényt
használja, hogy megmutassa egy-egy adat típusát.
"""

print("=== bool (logikai) ===")
# A logikai típus értéke True vagy False (nagybetűkkel!)
print(True)
print(False)

print()
print("=== int (egész szám) ===")
print(42)
print(-7)

print()
print("=== float (lebegőpontos / valós szám) ===")
# Figyeld: tizedespontot használunk, és a kimenet is .0-át tar egyenlő
print(3.14)
print(5 / 2)   # az osztás eredménye lebegőpontos lesz

print()
print("=== str (szöveg / string) ===")
print("Ez egy szöveg")
print('Ez is szöveg, csak aposztróffal')

print()
print("=== type(): mi a típusa? ===")
print(type(42))        # várod: int
print(type(3.14))      # várod: float
print(type("42"))      # várod: ?? (idézőjel van!)
print(type(True))      # várod: bool
print(type(False))

print()
print("=== FIGYELEM: True vs \"True\" ===")
print(True)          # ez bool típusú
print("True")        # ez STRING típusú (idézőjelben!)
# A kettő NEM ugyanaz! Nézd meg a típusukat:
print(type(True))
print(type("True"))

print()
print("=== Kisbetűs true / false NEM működik ===")
print("Spoiler: a 'true' és 'false' (kisbetűvel) hiba lenne.")
print("A Python ezt a két értéket csak nagybetűvel ismeri: True / False")
