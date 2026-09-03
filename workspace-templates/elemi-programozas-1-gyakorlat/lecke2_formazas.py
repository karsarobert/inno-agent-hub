# -*- coding: utf-8 -*-
"""
LECKE 2 - Szöveg formázás (kód + kipróbálás)
=============================================
Futtasd:  python lecke2_formazas.py

Ebben a leckében a szövegformázás három módját figyeled meg:
1) %-os formázás, 2) .format(), 3) f-string.
Aztán néhány helyen TE egészítesz ki kódot.
"""

# --- 1) %-os formázás ---
nev = "Béla"
eletkor = 21
uzenet = "Hello, %s vagyok, %d éves." % (nev, eletkor)
print(uzenet)
# %s = string (szöveg), %d = egész szám (int)

# --- 2) .format() metódus ---
uzenet2 = "Hello, {} vagyok, {} éves.".format(nev, eletkor)
print(uzenet2)

# A {} belsejébe nevet is adhatunk:
text = "Az e értéke: {e}".format(e=2.718281)
print(text)

# --- 3) f-string ---
uzenet3 = f"Hello, {nev} vagyok, {eletkor} éves."
print(uzenet3)

print()
print("=== FELADAT (fejleszd tovább) ===")
print("Írd át az 'uzenet3' f-stringet úgy, hogy a neved és az életkorod legyen benne.")
print("Ehhez módosítsd az alábbi sorokban a 'nev' és 'eletkor' értékeit,")
print("majd a saját köszöntésedet írd az uzenet_sajat nevű változóba:")
print()

# TODO: írd meg a saját változóidat és a saját köszöntésedet
# nev_sajat = ...
# eletkor_sajat = ...
# uzenet_sajat = f"..."
# print(uzenet_sajat)

print("(Aki kész, próbálja ki a .format() és a %-os formát is a saját adataival.)")
