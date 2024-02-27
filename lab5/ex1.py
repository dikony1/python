# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
f = open('lab5/row.txt', encoding='utf - 8')
s = str(f.read())

x = re.search('ab * $', s)

if x:
    print("it's a match")
else:
    print("no match found")
