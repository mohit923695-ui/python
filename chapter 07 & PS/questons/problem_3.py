#print multiplication table of a given number using while loops


n = int(input("enter the number :"))

i = n
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1