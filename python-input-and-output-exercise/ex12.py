"""
- Exercise 12: Interactive Menu
- Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”.
- Based on the user’s input, perform the corresponding action
"""

def main():
    while True:
        print("--------------------------------------","\nWelcome to my interactive menu!!!")
        print("Please choose one of these services.")
        print("1. Say Hello","2. Calculate Square","3. Exit",sep="\n",end="")

        try:
            n = int(input("\nInput: ").strip())
        except ValueError:
            print("ERROR!!!")
            main()
        else:
            if n == 1:
                print(sayhello())
            elif n == 2:
                print(calsquare())
            elif n == 3:
                print("Goodbye!!!")
                break
            else:
                print("ERROR!!!")

def sayhello():
    print("--------------------------------------")
    name = input("What is your name? ").strip()
    
    return f"Hello {name}!!!"

def calsquare():
    print("--------------------------------------")
    try:
        s = float(input("Enter the length of the square side (meter): ").strip())
        cal = input("Do you want to calculate 'perimeter' or 'area'? ").strip().lower()
    except ValueError:
        return "ERROR!!!"
    else:
        if cal == "perimeter":
            if 4*s == 1:
                return f"Result: {4*s} meter"
            else:
                return f"Result: {4*s} meters"
        elif cal == "area":
            return f"Result: {s**2} square meters"
        else:
            return "ERROR!!!"
main()