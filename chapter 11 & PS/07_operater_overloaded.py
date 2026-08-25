class number():
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = number(1)
m = number(2)
print(n+m)    