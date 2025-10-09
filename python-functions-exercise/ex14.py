"""
- Exercise 14: Create a lambda function that squares a given number
- A lambda function in Python is a small anonymous function defined using the lambda keyword.
- The syntax is lambda arguments: expression. The expression is evaluated and returned.
"""

def main():
    b = int(input("Type a number: ").strip())
    n = lambda b: b**2
    
    print(n(b))