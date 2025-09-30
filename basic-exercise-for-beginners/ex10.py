"""
- Exercise 10: Merge two lists using the following condition
- Given two lists of numbers, write Python code to create a new list
containing odd numbers from the first list and even numbers from the second list.
"""

def main():
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    new = []

    for i in list1:
        if i % 2 != 0:
            new.append(i)

    for j in list2:
        if j % 2 == 0:
            new.append(j)

    return f"Result list: {new}"