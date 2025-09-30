"""
- Exercise 1: Calculate the multiplication and sum of two numbers
- Given two integer numbers, write a Python program to return their product only 
if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

def main():
    number1 = int(input("Number 1: ").strip())
    number2 = int(input("Number 2: ").strip())

    if number1 * number2 <= 1000:
        return number1 * number2
    else:
        return number1 + number2