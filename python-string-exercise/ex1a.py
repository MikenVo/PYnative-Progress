"""
- Exercise 1A: Create a string made of the first, middle and last character
- Write a program to create a new string made of an input string’s first, middle, and last character.

- Given:
str1 = "James"

- Expected Output:
Jms
"""

def main():
    str1 = "James"
    print(str1[0] + str1[(len(str1)-1)//2] + str1[len(str1)-1])