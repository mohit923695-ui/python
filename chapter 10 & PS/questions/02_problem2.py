#write a class "calculater" capable of finding squre , cube and square roots of a number


class calculater:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square of a number is {self.n*self.n}")  

    def cube(self):
        print(f"the cube of a number is {self.n*self.n*self.n}") 

    def squareroot(self):
        print(f"the squareroot of a number is {self.n**1/2}") 

a= calculater(4)
a.square()
a.cube()
a.squareroot()           