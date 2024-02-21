# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def gendiv(n):
    for i in range(n):
        if  i % 3 == 0 and i % 4 == 0:
            yield i 

a = int(input('Enter number:'))

for num in gendiv(a):
    print(num) 