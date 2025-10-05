"""
- Exercise 8: Print list in reverse order using a loop

- Given:
list1 = [10, 20, 30, 40, 50]

- Expected output:
50
40
30
20
10
"""

def main():
    list1 = [10, 20, 30, 40, 50]

    for i in range(len(list1)):
        swapped = False

        for j in range(len(list1) - i - 1):
            if list1[j] < list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapped = True
        
        if not swapped:
            return list1