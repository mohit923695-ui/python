class employee():
    a = 1


    @classmethod
    def show(cls):
        print(f"the class attributes value is {cls.a}")

    @property
    def name(self):
        return f"{self.name}" "{self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



o = employee()

o.a = 45
        
o.show()

o.name = "mohit kumar"
print(o.fname , o.lname)