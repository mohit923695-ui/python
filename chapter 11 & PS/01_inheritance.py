class employee:                             #base classs
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name of employee {self.name} and the salary {self.salary}")

class programmer(employee):                        #derived or child class
    company = "techMNC"
    def showlanguage(self):
        print("the name of employee{self.name} and the language{slef.language}")


a = employee()
b = programmer()
print(a.company , b.company)               