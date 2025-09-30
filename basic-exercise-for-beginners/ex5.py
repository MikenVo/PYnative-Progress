"""
- Exercise 5: Check if the first and last numbers of a list are the same
- Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.
"""

def main():
    x = list(map(int, input("Type a list of numbers: ").strip().split(" ")))

    for i in range(len(x)):
        if x[0] == x[len(x)-1]:
            return True
        else:
            return False