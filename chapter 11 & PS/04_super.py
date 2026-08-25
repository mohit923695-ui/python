class employee:
    def __init__(self):
        print("construct th eemployee")
    a = 1

class programmer(employee):
     def __init__(self):
            print("construct the programmer")
     b = 2

class langauage(programmer):
     def __init__(self):
            super().__init__()
            print("construct th language")
     c = 3




o = langauage()
print(o.a , o.b, o.c)