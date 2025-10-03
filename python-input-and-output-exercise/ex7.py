"""
- Exercise 7: Accept any three string from one input() call
- Write a program to take three names as input from the user in a single call to the input() function.

- Expected Output
Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
"""

def main():
    names = input("Enter three names: ").strip().split(" ")
    for i in range(1, len(names)+1):
        print(f"Name{i}: {names[i-1]}")