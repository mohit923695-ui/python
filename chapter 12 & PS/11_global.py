# global function


a = 89
def fun():
    global a 
    a = 5
    print(a)


fun()
print(a)    