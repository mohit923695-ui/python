#dictionary methods 
a = {"keys": "values", 
     "name": "mohit", 
     "age": 30,
       "city": "New York"
       }


print(a ,type(a))

print(a.keys())

print(a.values())

a.update({"keys": "new_values","name":"rohan"})
print(a )


print(a.get("name"))