# Map in Python

p1 = [1,2,3,4,5]

def square(num):
    return num**2

p2 = ['a','b','c','d','e']

s = list(map(square,p1))

print(s)

# Filter in Python

p = list(filter(lambda x: x>3 , p1))

print(p)

# Reduce in Python 

from functools import reduce

q = reduce(lambda x,y:x*y,p1)

print(q)