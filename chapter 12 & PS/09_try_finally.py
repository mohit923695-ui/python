# try with finall y




from sys import exception


try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as e:
    print(e)

finally:
    print("i am inside finally block")   