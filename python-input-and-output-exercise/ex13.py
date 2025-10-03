"""
- Exercise 13: Display Right-Aligned Output
- Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.

- Expected Output:
Enter a word:  PYnative
Enter a number:  29
            PYnative29
"""

def main():
    word = input("Enter a word: ").strip()
    number = input("Enter a number: ").strip()

    print(f"{word:>20}{number}")