"""
- Exercise 9: Check File is Empty or Not
- Write a program to check if the given file is empty or not
"""

import os

def main():
    n = os.stat("ex9_test.txt").st_size
    if n == 0:
        print("Empty")
    else:
        print("Not empty")

main()