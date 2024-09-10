# How to extract the substring between two markers?

# Let's say I have a string 'gfgfdAAA1234ZZZuijk' and I want to extract just the '1234' part

# 1: using slicing function with markers
text = 'gfgfdAAA1234ZZZuijk'

# Define the markers
start_marker = 'AAA'
end_marker = 'ZZZ'

# Find the start and end positions
start_pos = text.find(start_marker) + len(start_marker)
end_pos = text.find(end_marker)

# Extract the substring
substring = text[start_pos:end_pos]

print(substring)

# 2: Use a regex pattern to find a sequence of digits
import re

string = 'gfgfdAAA1234ZZZuijk'

numbers = re.search(r'\d+', string)

if numbers:
    print(numbers.group())
else:
    print("No numbers found")

# Notes for re module

# The Regular Expression Pattern: r'\d+':
# r'' (raw string): When you use r'',
# it treats the string as a "raw string," meaning special characters like \ are not escaped.
# \d: This matches any digit from 0 to 9.

# +: This means "one or more" of the previous character (in this case, digits). So \d+ will match a sequence of one or more digits.
# re.search(r'\d+', string):
