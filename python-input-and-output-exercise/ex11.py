"""
- Exercise 11: Percentage Display
- Ask the user for a numerator and a denominator. 
- Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).
"""

def main():
    try:
        numerator = float(input("Type a numerator: ").strip())
        denominator = float(input("Type a denominator: ").strip())

        if denominator != 0:
            result = round((numerator/denominator) * 100,2)
            print(f"Result: {result:.2f}%")
        else:
            print("ERROR!!!")
            main()
    except ValueError:
        print("ERRROR!!!")
        main()