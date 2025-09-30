"""
- Exercise 22: Capitalize the first letter of each word in a string

- Expected Output:
str1 = "pynative.com is for python lovers"
# Output Pynative.com Is For Python Lovers
"""

def main():
    str1 = input("Type your string: ").strip()
    new = []

    for i in str1.split(" "):
        new.append(i.capitalize())

    print(" ".join(new))

main()