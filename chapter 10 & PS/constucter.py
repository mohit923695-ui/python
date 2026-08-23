class employee:
    language = "py"    # this is a class attributes 
    salary = "1200000"

    def __init__(self,name ,salary ,language): 
        self.name = name
        self.salary = salary
        self.language = language                        #dunder method which is a automatically enclosed
        print("i am creating a website")
        
    def getinfo(self):
        print(f"salary is not there")
    def greet(self):
        print("good night ")    



mohit = employee("mohit" , 1300000, 'java')
print(mohit.name , mohit.salary, mohit.language)