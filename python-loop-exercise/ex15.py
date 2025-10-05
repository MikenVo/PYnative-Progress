"""
- Exercise 15: Print elements from a given list present at odd index positions

- Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

- Expected output:
20 40 60 80 100
"""

def main():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for i in range(len(my_list)):
        if i % 2 != 0:
            print(my_list[i], end=" ")