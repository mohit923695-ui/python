class employee:
    a = 1

class programmer(employee):
    b = 2

class langauage(programmer):
    c = 3


o = employee()
print(o.a) 

o = programmer()
print(o.a , o.b)

o = langauage()
print(o.a , o.b, o.c)