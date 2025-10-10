"""
- Exercise 18: Create Higher-Order Function
- Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and returns the result of calling func(x, y).
- Demonstrate its use with different functions (e.g., addition, subtraction).

- The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.
"""

def apply_operation(func, x, y):
    print(func(x,y))

def calculate(x, y):
    operator = input("Type an operator (+, -, /, *): ").strip()

    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        if y != 0:
            return f"{x / y:g}"
        else:
            return "ERROR!!!"
    elif operator == "*":
        return x * y

def main():
    x = int(input("Type the first number: ").strip())
    y = int(input("Type the second number: ").strip())

    apply_operation(calculate, x, y)