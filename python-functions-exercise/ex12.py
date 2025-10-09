"""
- Exercise 12: Modifies global variable
- Define a global variable global_var = 10. Write a function that modifies a global variable value.
"""

global_var = 10

def main():
    global global_var
    n = int(input("Type a number: ").strip())
    global_var += n
    return global_var