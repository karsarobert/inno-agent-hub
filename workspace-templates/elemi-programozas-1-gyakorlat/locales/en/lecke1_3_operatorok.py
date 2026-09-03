# -*- coding: utf-8 -*-
"""
LESSON 1 - FILE 3: How operators behave (code + behaviour)
==========================================================
Run from the terminal:
    python lecke1_3_operatorok.py

Task: observe the behaviour of the HIGHLIGHTED lines. There are several
surprising results - think about why Python behaves this way.
"""

print("=== Division: / and // (double slash) ===")
print("5 / 2  =", 5 / 2)    # floating point (real) division -> 2.5
print("5 // 2 =", 5 // 2)   # integer division -> 2
print("'/' does floating-point division, '//' does integer division.")

print()
print("=== Remainder and exponentiation ===")
print("5 % 2  =", 5 % 2)    # the remainder -> 1
print("5 ** 2 =", 5 ** 2)   # exponentiation -> 25

print()
print("=== Surprise: text multiplied by a number ===")
print("'ha' * 5 =", "ha" * 5)
print("5 * 'ha' =", 5 * "ha")
print("('Na' * 10) + ' BATMAN' =", ("Na" * 10) + " BATMAN")
print("'*' with text means 'repetition': it repeats the text.")

print()
print("=== Assignment operators += / -= ===")
number = 10
print("original number =", number)
number += 1
print("number += 1 ->", number)
number -= 1
print("number -= 1 ->", number)

print()
print("=== IMPORTANT: ++ and -- do NOT exist in Python ===")
print("'number++' and 'number--' would be an error (SyntaxError).")
print("Instead, use: 'number += 1' and 'number -= 1'.")

print()
print("Observation question: why does '5 / 2' give 2.5 but '5 // 2' give 2?")
