"""
- Exercise 10: Read Line Number 4 from File

- Create a test.txt file and add the below content to it.
- test.txt file:
line1
line2
line3
line4
line5
line6
line7
"""

def main():
    with open("ex10_test.txt", "r") as fr:
        lines = fr.readlines()
        print(lines[4-1], end="")