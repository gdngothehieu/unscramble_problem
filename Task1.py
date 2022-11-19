"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# First create a set to hold all the unique numbers
nums = set()


def get_nums(list):
    # For loop in text, to go throw each row in the doc
    # Then, select the numbers in the first and second columns
    # If it is not in nums adds to it, if it is ignore and continue
    for row in list:
        for num in row[0], row[1]:
            nums.add(num)
    return nums


get_nums(texts)
get_nums(calls)

# Get the len of nums to know how many unique numbers in the two documents
count = len(nums)
print(f"There are {count} different telephone numbers in the records.")
