# -*- coding: utf-8 -*-
"""
LESSON 2 - Text formatting (code + experimentation)
===================================================
Run:  python lecke2_formazas.py

In this lesson you observe three ways of formatting text:
1) %-formatting, 2) .format(), 3) f-strings.
Then YOU complete the code in a few places.
"""

# --- 1) %-formatting ---
name = "Alex"
age = 21
message = "Hello, I am %s and I am %d years old." % (name, age)
print(message)
# %s = string (text), %d = whole number (int)

# --- 2) the .format() method ---
message2 = "Hello, I am {} and I am {} years old.".format(name, age)
print(message2)

# We can also give names to the {} placeholders:
text = "The value of e is: {e}".format(e=2.718281)
print(text)

# --- 3) f-strings ---
message3 = f"Hello, I am {name} and I am {age} years old."
print(message3)

print()
print("=== TASK (develop it further) ===")
print("Rewrite the 'message3' f-string so that it contains YOUR name and age.")
print("To do that, change the values of 'name' and 'age' in the lines above,")
print("then write your own greeting into a variable called your_message:")
print()

# TODO: write your own variables and your own greeting
# your_name = ...
# your_age = ...
# your_message = f"..."
# print(your_message)

print("(When you are done, also try the .format() and the %-format with your own data.)")
