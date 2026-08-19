# write a python program to remove a file to "renamed_by_python.txt"


with open("poem.txt","r") as f:
    content = f.read()


with open("renamed_by_python.txt", "w") as f:
    f.write(content)

