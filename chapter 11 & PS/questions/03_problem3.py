#create a class employee and addd salary and increment properties to it 
'''
write a method 'salaryafterincrement' method with @property decorater with a setter which changes the
value of increment based on the salary  
'''

class emoployee():
    salary = 234
    increment = 20 
    @property
    def salaryafterincrement(self):
        return (self.salary +self.salary)* (self.increment/100)


    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment = ((salary/self.salary)-1) *100

e = emoployee()
print(e.salaryafterincrement)
e.salaryafterincrement = 280.8
print(e.increment)


