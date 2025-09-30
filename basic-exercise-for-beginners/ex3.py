"""
- Exercise 3: Print characters present at an even index number
- Write a Python code to accept a string from the user and display characters 
present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
"""

def main():
    str = input("Type string: ").strip()
    print(f"Original String is {str}")
    print("Printing only even index chars")

    for i in range(len(str)):
        if i % 2 == 0:
            print(str[i])