class employee():
    a = 1


    @classmethod
    def show(cls):
        print(f"the class attributes value is {cls.a}")

o = employee()
o.a = 45
        
o.show()