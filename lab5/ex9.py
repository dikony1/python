# Write a Python program to insert spaces between words starting with capital letters.

import re 

def insert_spaces(string):
    return re.sub('(?!^)(?=[A-Z])', ' ', string)

f = open('lab5/row.txt',encoding='utf-8')
s = str(f.read())
ans = insert_spaces(s)

print(ans)
