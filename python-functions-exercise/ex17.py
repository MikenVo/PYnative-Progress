"""
- Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element

- Given:
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

- Expected Output:
The sorted list of tuples based on the second element is: [('date', 1), ('banana', 2), ('apple', 5), ('cherry', 8)]
"""

def main():
    data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

    sdata = sorted(data, key=lambda x: x[1])
    print(sdata)