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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Create set to hold the possible telemarketers numbers
possible_nums = set()
# Create a set to hold numbers with outgoing calls, incoming calls and numbers that sent or received texts
texts_nums = set()
outgoing_nums = set()
incoming_nums = set()

# For each row in calls, get the number which made the call and add to outgoing_nums
# Then get the number which received the call and add to incoming_nums
for row in calls:
    num1 = row[0]
    num2 = row[1]
    outgoing_nums.add(num1)
    incoming_nums.add(num2)

# Add the phone numbers which sent text or received text, and add to text_nums
for row in texts:
    num1 = row[0]
    num2 = row[1]
    texts_nums.add(num1)
    texts_nums.add(num2)

# Compare each of the outgoing_nums number to the other list
# If the number is not in incoming_nums, or texts_nums means the number did only calls
# So it is a possible telemarketers
for num in outgoing_nums:
    if num not in incoming_nums:
        if num not in texts_nums:
            possible_nums.add(num)


print("These numbers could be telemarketers: "
      + '\n' + '\n'.join(sorted(possible_nums)))
