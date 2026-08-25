#using function of find greatest of three numbers 



def greatest(a,b,c):
    return max(a, b, c)   # return the greatest of three numbers (handles ties)

a = int(input("enter the number a:"))
b = int(input("enter the number b:"))
c = int(input("enter the number c:"))
print(greatest(a,b,c))
