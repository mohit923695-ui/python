
#map example

l = [1, 2, 3, 4, 5]

sqlist = lambda x: x * x

sqlist = map(sqlist, l)
print(list(sqlist))

#filter example

def even(x):
    if(x % 2 == 0):
        return True
    return False

onlyeven = filter(even, l)
print(list(onlyeven))


#reduce example
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, l))    
