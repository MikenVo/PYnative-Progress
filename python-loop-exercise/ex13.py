"""
- Exercise 13: Find the factorial of a given number
- Write a Python program to use for loop to find the factorial of a given number.

- The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.

- For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120

- Expected output:
120
"""

def main():
    n = int(input("Type a number: ").strip())
    total = factorial(n)

    print(total)

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)