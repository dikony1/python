# Write a Python program to replace all occurrences of space, comma, or dot with a colon

import re 
f = open ('lab5/row.txt', encoding='utf-8')
s = str(f.read())

x = re.sub(" ", ',', s)

print(x)