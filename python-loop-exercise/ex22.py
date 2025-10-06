"""
- Exercise 22: Find largest and smallest digit in a number
- Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.

- Input:
num1 = 9876543210
num2 = -5082

- Output:
Largest digit in 987654321: 9
Smallest digit in 987654321: 1

Largest digit in -5082: 8
Smallest digit in -5082: 0
"""

def main():
    num = input("Type a number: ").strip()
    print(find(num))

def find(n):
    l = list(n)
    try:
        int(l[0])
    except ValueError:
        l.remove(l[0])
        smallest = l[0]
        largest = l[0]
    else:
        smallest = l[0]
        largest = l[0]

    for i in l:
        if smallest > i:
            smallest = i
        
        if largest < i:
            largest = i
    
    return f"Largest digit in {n}: {largest}\nSmallest digit in {n}: {smallest}"

main()