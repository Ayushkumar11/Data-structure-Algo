"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calls_dict = defaultdict(int)
output = "{} spent the longest time, {} seconds, on the phone during September 2016."

for caller, callee, timestamp, duration in calls:
    calls_dict[caller] += int(duration)
    calls_dict[callee] += int(duration)

max_time = 0
phone_number = ""

for key,value in calls_dict.items():
    if value > max_time:
        phone_number = key
        max_time = value

print(output.format(phone_number, max_time))