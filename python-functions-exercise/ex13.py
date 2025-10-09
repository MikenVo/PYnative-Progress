"""
- Exercise 13: Write a recursive function to calculate the factorial
- Write a recursive function to calculate the factorial of a non-negative integer.
"""

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

def main():
    num = int(input("Type a number: ").strip())
    print(factorial(num))