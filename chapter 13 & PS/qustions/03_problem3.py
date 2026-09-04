'''
a list contins the multiplication table of 7 . write a program to convert it to vertical string of the same number 
'''


table = [str(i * 7) for i in range(1, 11)]
vertical_string = "\n".join(table)
print(vertical_string)