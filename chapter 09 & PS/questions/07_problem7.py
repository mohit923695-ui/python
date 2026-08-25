#write a program to find out  the line number where python is present from question 6



with open("python.txt","r") as f :
    line = f.readlines()

lineno = 1 
for lines in line:
    if("pyhton " in lines):
        print(f"python is present in content , line:{lineno}")
        break
    lineno += 1
else:
    print("python is not present in content  ")

    