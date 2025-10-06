"""
- Exercise 1: Create a function in Python
- Write a program to create a function that takes two arguments, name and age, and prints their values.
"""

def main():
    nm = input("Type a name: ").strip()
    age = int(input("Type an age: ").strip())
    print(perinfo(nm, age))

def perinfo(name, age):
    return f"Name: {name} - Age: {age}"