# -*- coding: utf-8 -*-
"""
LESSON 4 - Type conversion and input()
=====================================
Run:  python lecke4_konverzio_input.py

The program asks for data in the terminal. Type a name and two whole
numbers. Observe what happens after input(), and then after the
conversion.
"""

print("=== Type conversions ===")
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(42), type(str(42)))

print()
print("=== Interactive program ===")
name = input("What is your name? ")
print(f"Hi, {name}!")

print()
print("=== The sum of two numbers ===")
# Important: the result of input() is always str.
# That is why we convert the read text with int():
a = int(input("First whole number: "))
b = int(input("Second whole number: "))
total = a + b
print(f"The sum is: {total}")

print()
print("=== Observation questions ===")
print("1. What would happen if we left out the int() conversion?")
print("2. What does the operation '3' + '4' do if both are strings?")
print("3. Why do we need to turn a number into str() to join it to text with '+'?")
