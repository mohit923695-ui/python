'''#create a class with a class attribute a; 
create an object from it and set 'a' directly using object.a= 0 does this change the class attributes.
'''

class demo:
    a = 4

o = demo()
print(o.a)    #print the class attributes because instant attribute is not present
o.a = 0
print(o.a)      #print the class attributes because instant attribute is present

print(demo.a)    #prit the instant attribute