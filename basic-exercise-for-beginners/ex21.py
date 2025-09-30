"""
- Exercise 21: Check if a user-entered string contains any digits using a for loop
"""

def main():
    str = input("Enter a string: ").strip()
    is_digit = 0

    for i in str:
        try:
            int(i)
        except ValueError:
            pass
        else:
            is_digit += 1
            break
    
    if is_digit == 1:
        print("The string contains at least one digit.")
    else:
        print("The string does not contain any digits")

main()