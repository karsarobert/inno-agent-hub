# -*- coding: utf-8 -*-
"""
LESSON 3 - Variables and dynamic typing
=======================================
Run:  python lecke3_valtozok.py

In this lesson you observe how VARIABLES behave, especially dynamic
typing: the same variable can store data of different types.
"""

print("=== Creating a variable and its simple type ===")
my_variable = "some text"
print(my_variable)
print(type(my_variable))

print()
print("=== Dynamic typing: a variable can CHANGE its type too ===")
val = 42
print("val = 42   ->", type(val), "value:", val)

val = 12.345
print("val = 12.345 ->", type(val), "value:", val)

val = "cheese"
print("val = 'cheese' ->", type(val), "value:", val)

print()
print("The 'val' variable was int first, then float, and finally str!")
print("This is what we call dynamic typing.")

print()
print("=== Analysis: asking for the type with type() ===")
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("text"))   # <class 'str'>
print(type(True))     # <class 'bool'>

print()
print("=== TASK ===")
print("Look at what type() gives for the two variables below:")
e = 3.5
name2 = "Ann"
print(type(e))
print(type(name2))
