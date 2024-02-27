# Write a Python program to convert a given camel case string to snake case.

import re

def snake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

f = open('lab5/row.txt', encoding='utf-8')
s = str(f.read())
ans = snake(s)

print(ans)