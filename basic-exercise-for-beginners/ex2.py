"""
- Exercise 2: Print the Sum of a Current Number and a Previous number
- Write Python code to iterate through the first 10 numbers and, in each iteration,
print the sum of the current and previous number.
"""

def main():
    print("Printing current and previous number sum in a range(10)")
    for i in range(10):
        if i == 0:
            print(f"Current Number {i} Previous Number {i} Sum: {i}")
        else:
            print(f"Current Number {i} Previous Number {i-1} Sum: {i+i-1}")