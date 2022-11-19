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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Create a list to hold all the numbers called by people in Bangalore
#  that starts with (0...)
all_nums_called = []
# Create a set to hold the area codes
unique_codes = set()
i = 0

# While loop to loop over the doc, until the end of it
# Find the numbers that starts with (080) in the first column
# Then append to the all_codes list the number called by it (second column)
while i < len(calls):
    if '(080)' in calls[i][0]:
        all_nums_called.append(calls[i][1])
        # If the number start with a code '(0', then split to get just the code,
        # add to the end of the code ')', once we lost it during split
        if '(0' in calls[i][1]:
            code = (calls[i][1].split(')')[0]) + ')'
            # Once unique_codes is a set, it will add the code only when it is not there already
            unique_codes.add(code)
    i += 1

print("The numbers called by people in Bangalore have codes:"
      + '\n' + '\n'.join(sorted(unique_codes)))

# To find how many times a person from Bangalore calls some one in Bangalore:
# For each number in all_nums_called check if has '(080)' (Bangalore)
# If does adds 1 to count
count = 0
for num in all_nums_called:
    if '(080)' in num:
        count += 1

# To find the percentage, get the count variable, and divide by the len of all_nums_called
# Use round to get just the two first decimals
percent = round((count * 100)/len(all_nums_called), 2)

print(f"{percent} percent of calls from fixed lines in Bangalore are calls "
      "to other fixed lines in Bangalore.")
