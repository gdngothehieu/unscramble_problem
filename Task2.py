"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# First, creating a dictionary to hold the numbers and the counting num
num_dict = {}

# For loop in calls, to go throw each row in the doc
# Then, select the numbers in the first and second columns
# And add the num as a key for the dictionary
# and set the value as the time spent in the call - column D (row[3])
# If num already int he dictionary increases the value by the time in the call
for row in calls:
    for num in row[0], row[1]:
        num_dict[num] = num_dict.get(num, 0) + int(row[3])

# Find the key with the greater value in the dictionary
# And storage in a variable
greater_key = max(num_dict, key=num_dict.get)

# To get the value (time spent in the call) for the variable greater_key
# use the function get passing the greater_key as argument
print(f"{greater_key} spent the longest time, {num_dict.get(greater_key)} seconds, "
      f"on the phone during September 2016.")