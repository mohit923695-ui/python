# raising exceptions in python


a = int(input("Enter a number: "))
b = int(input("Enter your second number: "))

if (b == 0):
    raise ValueError("The second number cannot be zero.")
else:
    print(f"the division of {a} and {b} is {a/b}")