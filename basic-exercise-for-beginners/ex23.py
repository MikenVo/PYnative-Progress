"""
Exercise 23: Create a simple countdown timer using a while loop.
Write a code to create a simple countdown timer of 5 seconds using a while loop.

Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
"""

def main():
    i = 5
    while i <= 5:
        print(f"Time remaining: {i} seconds")
        if i == 0:
            print("Time's up!")
            break
        i -= 1

main()