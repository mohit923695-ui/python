#add the static mathod in proble 2 , to greeet the user with hell0 there


class calculater:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square of a number is {self.n*self.n}")  

    def cube(self):
        print(f"the cube of a number is {self.n*self.n*self.n}") 

    def squareroot(self):
        print(f"the squareroot of a number is {self.n**1/2}") 

    @staticmethod
    def hello():
        print("hello there!")    

a= calculater(4)
a.hello()
a.square()
a.cube()
a.squareroot()           