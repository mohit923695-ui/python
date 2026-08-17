#pattern 

def pattern(n):
    if(n == 0):
        return 
    print("*" * n)
    pattern(n-1)

pattern(3)
pattern(5)
pattern(7)
pattern(8)
pattern(9)
pattern(12)
