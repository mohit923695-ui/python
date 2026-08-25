# repeat problem 4 for a lot of such words to be 

words = ["donkey" ,"bad", "very bad"]

with open ("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word) )


with open ("file.txt", "w") as f:
    f.write(content)
