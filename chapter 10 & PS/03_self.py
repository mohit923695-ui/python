class employee:
    language = "py"    # this is a class attributes 
    salary = "1200000"

    def getinfo(self):
        print(f"salary is not there")
    def greet(self):
        print("good night ")    



mohit = employee()
mohit.language = "javascript"     #this is a instance attributes 
print(mohit.salary,mohit.language)  
mohit.greet()
mohit.getinfo()