# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'/.

import re 
f = open('lab5/row.txt', encoding='utf-8')
s= str(f.read())

x = re.search("a.*b$", s)

if x:
    print("it's a match")
else:
    print("not mutch found")