"""
- Exercise 4: Arrange string characters such that lowercase letters should come first
- Given string contains a combination of the lower and upper case letters.
- Write a program to arrange the characters of a string so that all lowercase letters should come first.

- Given:
str1 = PyNaTive

- Expected Output:
yaivePNT
"""

def main():
    str1 = "PyNaTive"
    out = []

    for i in str1:
        if i.istitle() == False:
            out.append(i)
    
    for j in str1:
        if j.istitle() == True:
            out.append(j)
    print("".join(out))

main()