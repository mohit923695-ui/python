class employee:                             #base classs
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the name of employee {self.name} and the salary {self.company}")

class coder():
    language = "python"
    def printLanguage(self):
        print(f"he knows the language {self.language}")        

class programmer(employee, coder):                 #derived or child class
    company = "techMNC"
    def showlanguage(self):
        print(f"the name of employee {self.name} and the language {self.language}")


a = employee()
b = programmer()

b.show()
b.showlanguage()
b.printLanguage()