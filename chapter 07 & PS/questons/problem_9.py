#print pattern

n = int(input("enter the number: "))


for i in range(1,1+n):
    if(i == 1 or i == n):
        print("*"* n ,end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*" , end="")
    print("")    