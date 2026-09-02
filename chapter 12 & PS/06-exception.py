# exception handling in python


from sys import exception


try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)    

except ValueError as e:
    print(e)