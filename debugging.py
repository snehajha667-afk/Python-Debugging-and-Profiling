"""
Debugging Practice
Author: Sneha Jha

This file demonstrates common Python errors
and how to debug them using VS Code.
"""

print("========== Example 1 ==========")
# ZeroDivisionError

try:
    a = 100
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    print("Error:", e)


print("\n========== Example 2 ==========")
# NameError

try:
    name = "Sneha"
    print(nam)
except NameError as e:
    print("Error:", e)


print("\n========== Example 3 ==========")
# TypeError

try:
    age = 21
    print("Age: " + age)
except TypeError as e:
    print("Error:", e)


print("\n========== Example 4 ==========")
# IndexError

try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError as e:
    print("Error:", e)


print("\n========== Example 5 ==========")
# KeyError

try:
    student = {"name": "Sneha"}
    print(student["age"])
except KeyError as e:
    print("Error:", e)


print("\n========== Example 6 ==========")
# Logical Error

def add(a, b):
    return a - b

print("Expected: 15")
print("Actual:", add(10, 5))
