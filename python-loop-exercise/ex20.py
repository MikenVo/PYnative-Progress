"""
- Exercise 20: Print the alternate numbers pattern

- Pattern:
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15
"""

def main():
    m = 1
    n = 2

    for i in range(2,7):
        for j in range(m,n):
            print(j, end=" ")
        print("\n", end="")

        m = n
        n = m + i