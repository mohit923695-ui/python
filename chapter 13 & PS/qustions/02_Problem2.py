'''
write a program to input name , marks , phone number of a students and format it using the format functions below 
" the name of the student is {} and his marks are {} and his phone number is {}"
'''

name = input("Enter the name of the student: ")
marks = input("Enter the marks of the student: ")
phone_number = input("Enter the phone number of the student: ")

s = "The name of the student is {} and his marks are {} and his phone number is {}".format(name, marks, phone_number)
print(s)