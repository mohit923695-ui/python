'''
a file contains a word "donkey"  multiple times .you need to write a program which replace this word 
##### by updating the same line.
'''

word = "donkey"

with open ("file.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word,"#####")


with open ("file.txt", "w") as f:
    f.write(contentnew)
