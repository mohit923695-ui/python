#write a program the text form a given file 'poem.txt' and find out whether it contains the word 'twinkle'



f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word twinkle present in the content")

else:
    print("the word twinkle not present in the content")

f.close()    