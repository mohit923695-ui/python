#create a class "programer" for sharing information of few programmer working at microsoft 


class programmer :
    company = "microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("harry", 244535, 909)
print(p.name ,p.salary ,p.pin)

r = programmer("rohan", 66767, 909)
print(r.name ,r.salary ,r.pin)        