
from sys import exception


try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as e:
    print(e)

else:
    print("i am inside else block")   