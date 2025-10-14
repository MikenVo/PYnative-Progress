"""
- Exercise 1B: Create a string made of the middle three characters
- Write a program to create a new string made of the middle three characters of an input string.

- Given:
Case 1
str1 = "JhonDipPeta"

Output
Dip

Case 2
str2 = "JaSonAy"

Output
Son
"""

def main(str1):
    out = str1[((len(str1)-1)//2)-1] + str1[(len(str1)-1)//2] + str1[((len(str1)-1)//2)+1]
    print(out)