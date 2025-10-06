"""
- Exercise 8: Generate a Python list of all the even numbers between 4 to 30

- Expected Output:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
"""

def main():
    l = []

    for i in range(4,30,2):
        l.append(i)
    
    print(l)