f = open("file.txt")
print(f.read())
f.close()

#no need of f.close using with stetement 


with open ("file.txt") or f:
    text = f.read()
    print(text)

    