"""
- Exercise 5: Accept a list of 5 float numbers as an input from the user

- Expected Output:
[78.6, 78.6, 85.3, 1.2, 3.5]
"""

def main():
    l = list(map(float, input("Type a list of float numbers: ").strip().split(" ")))

    print(l)

main()