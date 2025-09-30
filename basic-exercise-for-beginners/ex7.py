"""
- Exercise 7: Find the number of occurrences of a substring in a string
- Write a Python code to find how often the substring “Emma” appears
in the given string.
"""

def main():
    str_x = "Emma is good developer. Emma is a writer"
    new = {}

    for i in str_x.split(" "):
        new[i] = str_x.split(" ").count(i)
    
    return f"Emma appeared {new['Emma']} times"
    
