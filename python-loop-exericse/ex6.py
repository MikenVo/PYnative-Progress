"""
- Exercise 6: Count the total number of digits in a number
- Write a Python program to count the total number of digits in a number using a while loop.

- For example, the number is 75869, so the output should be 5.
"""

def main():
    num = list(input("Type the number: ").strip())

    total = 0
    n = 0

    while n < len(num):
        try:
            int(num[n])
        except ValueError:
            pass
        else:
            total += 1
        n += 1
    return total