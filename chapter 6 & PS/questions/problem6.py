marks = int(input("enter yout marks :"))


if(marks<=100 and marks>=90):
    grade = "ex"
elif(marks<90 and marks>=80):
    grade = "a+"
elif(marks<=80 and marks>=70):
    grade = "b"
elif(marks<=70 and marks>=60):
    grade = "c"
elif(marks<=60 and marks>=50):
    grade = "d"
elif(marks<=50 and marks>=40):
    grade = "fail"

print("your grade is ", grade)

