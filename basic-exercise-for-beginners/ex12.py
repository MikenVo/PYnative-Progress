"""
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the income is 45000, and the income tax payable is
"""

def main():
    income = int(input("Type your income: ").strip())

    if 0 <= income <= 10000:
        return f"Tax: {round(income*(0/100))}"
    elif 10000 < income <= 20000:
        return f"Tax: {round(10000*(0/100)+(income-10000)*(10/100))}"
    else:
        return f"Tax: {round(10000*(0//100)+10000*(10/100)+(income-20000)*(20/100))}"

print(main())