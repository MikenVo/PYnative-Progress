"""
- Exercise 2: Format Output String

- Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
- Use the print() function to format the given words in the specified format. Display the ** separator 
between each string.

- Given:
str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'
Expected Output:

- For example: print('your code') should display My**Name**Is**James
"""

def main():
    str1 = "My"
    str2 = "Name"
    str3 = "Is"
    str4 = "James"

    print(str1,str2,str3,str4,sep="**")