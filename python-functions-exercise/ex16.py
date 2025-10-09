"""
- Exercise 16: Use a lambda with the map() function to double each element in a list

- Given:
numbers = [1, 2, 3, 4, 5]

- Expected Output:
The doubled numbers are: [2, 4, 6, 8, 10]
"""

def main():
    numbers = [1, 2, 3, 4, 5]
    n = list(map(lambda x: x*2, numbers))

    print(f"The doubled numbers are: {n}")