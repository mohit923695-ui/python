'''
write a list comperision to print  a list which contains the multiplication table of a user entered number using list comprehension.
'''
number = int(input("Enter a number: "))
multiplication_table = [number * i for i in range(1, 11)]
print(multiplication_table)