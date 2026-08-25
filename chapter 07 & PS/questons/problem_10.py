#print the multiplication of table of n using for loop in reverse oder 


n = int(input("enter the number: "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
