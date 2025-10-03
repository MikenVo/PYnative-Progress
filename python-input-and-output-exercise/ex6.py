"""
- Exercise 6: Write all content of a file into a new file by skipping line number 5

- Create a test.txt file and add the below content to it.

- Given test.txt file:
line1
line2
line3
line4
line5
line6
line7

- Expected Output: new_file.txt
line1
line2
line3
line4
line6
line7
"""

counter = 0

with open("ex6.py", "r") as file:
   lines = file.readlines()

with open("ex6_new_file.txt", "w") as fw:
    for line in lines:
        if counter == 4:
            counter += 1
            continue
        else:
            fw.write(f"Line{counter}\n")
            print(f"Line{counter}")
            counter += 1        
    