



class vector:
    def __init__(self,x,y,z ):
        self.x = x 
        self.y = y
        self.z = z 

    def __add__(self, other):
        print(f"{self.x}+ {other.x},{self.y}+ {other.y},{self.z}+ {other.z}")

    def __mul__(self, other,add):
        print(f"{self.x} * {other.x},{self.y} * {other.y},{self.z} * {other.z}")           

    def __str__(self):
         return (f"({self.x}i+{self.y}j+{self.z}k")


v1 = vector(1,2,3,)
v2 =vector(4,5,6) 
v3 = vector(7,8,9)

print(v1+v2)
