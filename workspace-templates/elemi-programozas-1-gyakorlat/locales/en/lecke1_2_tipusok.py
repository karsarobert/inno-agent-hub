# -*- coding: utf-8 -*-
"""
LESSON 1 - FILE 2: Basic data types + type() (code + behaviour)
================================================================
Run from the terminal:
    python lecke1_2_tipusok.py

Task: observe WHAT it prints and WHY. The program uses the type()
function to show the type of each piece of data.
"""

print("=== bool (boolean) ===")
# The boolean type has the values True or False (capitalized!)
print(True)
print(False)

print()
print("=== int (whole number) ===")
print(42)
print(-7)

print()
print("=== float (floating point / real number) ===")
# Note: we use a decimal point, and the result of division keeps a .0
print(3.14)
print(5 / 2)   # the result of division will be a float

print()
print("=== str (text / string) ===")
print("This is a text")
print('This is also text, just with apostrophes')

print()
print("=== type(): what is its type? ===")
print(type(42))        # expect: int
print(type(3.14))      # expect: float
print(type("42"))      # expect: ?? (there are quotes!)
print(type(True))      # expect: bool
print(type(False))

print()
print('=== WARNING: True vs "True" ===')
print(True)          # this one is of type bool
print("True")        # this one is of type STRING (in quotes!)
# The two are NOT the same! Look at their types:
print(type(True))
print(type("True"))

print()
print("=== Lowercase true / false does NOT work ===")
print("Spoiler: 'true' and 'false' (lowercase) would be an error.")
print("Python knows these two values only capitalized: True / False")
