f = open("file.txt")

line1 = f.readlines()
print(line1,type(line1))

line2 = f.readlines()
print(line2,type(line2))

line3 = f.readlines()
print(line3,type(line3))

line4 = f.readlines()
print(line4 =="")

f.close()