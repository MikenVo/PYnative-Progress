"""
- Exercise 10: Display a message “Done” after the successful execution of the for loop
- For example, the following loop will execute without any error.

- Given:
    for i in range(5):
        print(i)

- Expected output:
0
1
2
3
4
Done!
"""

def main():
    for i in range(5):
        print(i)
        if i >= 4:
            print("Done!")