# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re 
f = open('lab5/row.txt', encoding='utf-8')
s = str(f.read())

x = re.search("[A-Z] + [a-z]+", s)

if x:
    print("it's a match")
else:
    print(" not mutch found")