#write a program to find out whether a file is identical & make a content of another file 


with open("this.txt") as f :
    content1 = f.read()

with open("python.txt", "r") as f :
    content2 = f.read()    

if(content1 == content2):
    print("this file is identical")

else:
    print("this file is not identical ")

    