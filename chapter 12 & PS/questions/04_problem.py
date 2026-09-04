''''
write a progra a/b where a & b are integers . if b = 0  display innfinite by handling thwe 'zero division '
'''

try:
    a = int(input("Enter the numerator (a): "))
    b = int(input("Enter the denominator (b): "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")