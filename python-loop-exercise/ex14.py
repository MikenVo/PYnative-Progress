"""
- Exercise 14: Reverse a integer number

- Given:
76542

- Expected output:
24567
"""

def main():
    n = input("Type a number: ").strip()

    l = list(n)
    l.reverse()

    print("".join(l))