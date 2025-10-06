"""
- Exercise 6: Create a recursive function
- Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

*A recursive function is a function that calls itself repeatedly.

- Expected Output:
55
"""

def main():
    print(add(0))

def add(n):
    if n < 10:
        return n + add(n+1)
    else:
        return 10