''' write a program to open file 1.txt,2.txt,3.txt if any these files are not present ,
 a message without exiting the program must be promoting the same .'''


try:
    with open('1.txt', 'r') as file1:
        print("Contents of 1.txt:")
        print(file1.read())
except FileNotFoundError:
    print("File 1.txt not found.")

try:
    with open('2.txt', 'r') as file2:
        print("Contents of 2.txt:")
        print(file2.read())
except FileNotFoundError:
    print("File 2.txt not found.")

try:
    with open('3.txt', 'r') as file3:
        print("Contents of 3.txt:")
        print(file3.read())
except FileNotFoundError:
    print("File 3.txt not found.")



print("thankyou ")