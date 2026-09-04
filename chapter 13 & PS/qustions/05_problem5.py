from functools import reduce
l = [1, 2, 3, 4, 5345,53533464,6546,]
def greater(a,b):
    if(a > b):
        return a
    return b

result = reduce(greater, l)
print(result)
