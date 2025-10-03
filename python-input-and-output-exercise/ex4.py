"""
- Exercise 4: Display Float Number with 2 Decimal Places

- Given:
num = 458.541315

- Expected Output:
458.54
"""

def main():
    num = float(input("Type a rational number in decimal format: ").strip())

    print(round(num,2))