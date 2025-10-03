"""
- Exercise 3: Display Decimal Number to Octal using print() function
- Given:
num = 8

- Expected Output:
The octal representation of the decimal number 8 is 10.
"""

def main():
    num = int(input("Type an integer number: ").strip())
    print(f"Octal to Decimal: {'%o' % num}")