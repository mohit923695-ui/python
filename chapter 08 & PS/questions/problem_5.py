#a recursive to calculate the sum of first n number 

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))    
print(sum(23))    
print(sum(56))    
print(sum(78))  
print(sum(90))   
print(sum(100))  