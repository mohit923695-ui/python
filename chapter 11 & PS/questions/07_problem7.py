# Override __len__() in a vector to display its dimension.


class Vector:
        def __init__(self, l):
                self.l = l 

        def __len__(self):
                return len(self.l) 

v = Vector([1, 2, 3])
print(len(v))