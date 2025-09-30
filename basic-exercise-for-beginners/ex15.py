"""
- Exercise 15: Get an int value of base raises to the power of exponent
- Write a function called exponent(base, exp) that returns an int value of base
raises to the power of exp.

- Note here exp is a non-negative integer, and the base is an integer.
"""

def main():
    base = int(input("Type a number for the base (integer): ").strip())
    exponent = int(input("Type a number for the exponent (non-negative integer): ").strip())

    if exponent >= 0:
        return base**exponent
    else:
        return "ERROR!!!"