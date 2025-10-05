"""
- Exercise 18: Print the following pattern
- Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

def main():
    for i in range(1, 6):
        print("* " * i)
    
    for i in range(4, 0,-1):
        print("* " * i)