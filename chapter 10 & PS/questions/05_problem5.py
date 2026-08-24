'''
write a class train where has methods to book a ticket , 
getstatus(no. of seats) and getfare information of train running under indian railways 
'''

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro,to ):
        print(f"the ticket is booked trainNo :{self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no:{self.trainNo} status running on time ")  

    def getfare(self, fro,to ):
        print(f"the ticket is booked trainNo :{self.trainNo} from {fro} to {to} from {randint(100,5000)}")

t = train(335)
t.book("rampur" ,"lucknow")        
t.getstatus()        
t.getfare("rampur" ,"lucknow")        
