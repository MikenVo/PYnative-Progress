"""
- Exercise 16: Check Palindrome Number
- A palindrome number is a number that remains the same when its digits are reversed.
- In simpler terms, it reads the same forwards and backward. For example 121, 5005.
"""

def main():
    num = input("Type a number: ").strip()
    n = []

    for i in num:
        n.append(i)
    
    n.reverse()
    new = "".join(n)

    if num == new:
        return f"{num} is a palindrome number"
    else:
        return f"{num} is not a palindrome number"