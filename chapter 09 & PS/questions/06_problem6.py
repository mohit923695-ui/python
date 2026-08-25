# write a program to mine a log file and find out whether it contains 'python '


with open("python.txt","r") as f :
    content = f.read()

if("pyhton " in content):
    print("python is present in content")
else:
    print("python is not present in content  ")

    