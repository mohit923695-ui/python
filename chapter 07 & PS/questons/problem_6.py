#calculate the factorial of a given number using for lopps

n = int(input("enter the number :"))

product = 1
for i in range(1, n+1):
    product = product * i
print(f"the factorial of {n} is {product}")    