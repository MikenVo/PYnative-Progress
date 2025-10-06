"""
- Exercise 5: Create an inner function
- Create a program with nested functions to perform an addition calculation as follows:
1. Define an outer function that accepts two parameters, a and b.
2. Inside this outer function, define an inner function that calculates the sum of a and b.
3. The outer function should then add 5 to this sum.
4. Finally, the outer function should return the resulting value.”
"""

def main(num1, num2):
    def addition(f, s):
        return f + s
    
    return f"{5 + addition(num1, num2):g}"

a = float(input("Type the first number: ").strip())
b = float(input("Type the second number: ").strip())