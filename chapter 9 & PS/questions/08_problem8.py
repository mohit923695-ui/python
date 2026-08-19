#write a program to make a copy of a text.txt. "this.txt"


with open("this.txt", "r") as f :
    content = f.read()

with open("this_copy.txt", "w") as f :
    f.write(content)   