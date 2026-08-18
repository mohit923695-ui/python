f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word twinkle present in the content")

else:
    print("the word twinkle not present in the content")

f.close()    