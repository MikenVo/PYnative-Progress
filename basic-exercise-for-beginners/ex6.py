"""
- Exercise 6: Display numbers divisible by 5
- Write a Python code to display numbers from a list divisible by 5
"""

def main():
    x = list(map(int, input("Type a list of numbers: ").strip().split(" ")))
    print(f"Given list is {x}")
    print("Divisible by 5")
    for i in x:
        if i % 5 == 0:
            print(i)