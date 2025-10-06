"""
- Exercise 9: Find the largest item from list

- Given:
x = [4, 6, 8, 24, 12, 2]

- Expected Output:
24
"""

def main():
    x = [4, 6, 8, 24, 12, 2]
    largest = x[0]

    for i in x:
        if largest < i:
            largest = i
    print(largest)