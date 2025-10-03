"""
- Exercise 14: Tabular Output from Lists
- You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
- Print these lists as a simple table with columns “Name” and “Score”.

- Expected Output:
Name       Score
---------------
Alice      85   
Bob        92   
Charlie    78  
"""

def main():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]

    print(f"{'Names'}{'Scores':>12}")
    print("-" * 17)

    for i in range(len(scores)):
        print(f"{names[i]:<10}{scores[i]:>3}")