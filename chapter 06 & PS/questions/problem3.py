#detect the spam 

p1 = "make a lot of money "
p2 = "buy now"
p3 = "suscribe no "
p4 = "click this"

message = input("enter your comment ")

if(p1 in message or p2 in message or p3 in message or p3 in message):
    print("detect the spam ")

else:
    print("not spam ")
        