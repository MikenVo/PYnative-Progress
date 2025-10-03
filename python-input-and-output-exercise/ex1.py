"""
- Exercise 1: Accept Numbers From User

- Write a program to accept two integer numbers from the user and calculate their product.
"""

def main():
    n1 = int(input("Type an integer: ").strip())
    n2 = int(input("Type a second integer: ").strip())

    return f"The product: {n1*n2}"