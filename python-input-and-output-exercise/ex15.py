"""
- Exercise 15: Padding with Zeros
- Ask the user for a number. Print this number padded with leading zeros to a width of 5.

For example, if the input is 12, the output should be “00012“
"""

def main():
    num = input("Number: ").strip()
    print(num.zfill(5))