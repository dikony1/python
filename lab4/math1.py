# Write a Python program to convert degree to radian.

import math

degree = int(input('Input degree:'))
radian = degree * math.pi / 180

print("Output radian:", round(radian,6))