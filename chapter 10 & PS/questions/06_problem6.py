'''
can you change the self parameter inside a class to something else (sat"mohit").
 try changing self to "slf" or  "hard" to end seee the effects.
'''


from random import randint

class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(mohit, fro,to ):
        print(f"the ticket is booked trainNo :{mohit.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"train no:{self.trainNo} status running on time ")  

    def getfare(self, fro,to ):
        print(f"the ticket is booked trainNo :{self.trainNo} from {fro} to {to} from {randint(100,5000)}")

t = train(335)
t.book("rampur" ,"lucknow")        
t.getstatus()        
t.getfare("rampur" ,"lucknow")        
