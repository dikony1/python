# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
f = open('lab5/row.txt', encoding='utf-8')
s = str(f.read())

x = re.search("[a-z] +- [a-z]+", s)

if x:
    print("it's a match")
else:
    print("not match found") 