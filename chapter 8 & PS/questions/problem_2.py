
#using function of find minimum
# of three numbers 



def minimum(a,b,c):
    return min(a, b, c)   # return the minimum of three numbers (handles ties)

a = int(input("enter the number a:"))
b = int(input("enter the number b:"))
c = int(input("enter the number c:"))
print (minimum(a,b,c))
