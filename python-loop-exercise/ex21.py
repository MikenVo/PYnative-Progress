"""
- Exercise 21: Flatten a nested list using loops
- Write a program to flatten a nested list using loops.

- Given:
'''
    nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

    # write function 'flatten_list' to flatten a nested list
    flattened = flatten_list(nested_list)
    print("Flattened list:", flattened)
'''

- Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
    
def main():
    nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

    flattened = flatten_list(nested_list)
    print("Flattened list:", flattened)  

def flatten_list(x):
    l = []
    for i in x:
        if type(i) == list:
            for j in i:
                l.append(j)
        else:
            l.append(i)

    return l