'''
write  a program to filter a list of a number which is divisble by 5
'''


def divisible_by_5(x):
    if x % 5 == 0:
        return True
    return False

f = filter(divisible_by_5, [1, 2, 4366,4, 5, 6, 55, 45, 9, 10])
print(list(f))