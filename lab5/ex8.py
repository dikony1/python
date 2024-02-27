# Write a Python program to split a string at uppercase letters.

import re
f = open('lab5/row.txt', encoding='utf-8')
s = str(f.read())
ans = re.findall('[A-Z][a-z]*', s)

print(ans)