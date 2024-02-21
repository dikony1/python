# Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    while n >=0:
        yield n
        n-=1

a = int(input('Enter the countdown number: '))

for i in countdown(a):
    print(i)