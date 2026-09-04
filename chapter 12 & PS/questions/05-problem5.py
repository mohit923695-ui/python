'''
store the multiplication table generated in problem 3 in a file name table.txt

'''

n = int(input("Enter a number: "))
multiplication_table = [n * i for i in range(1, 11)]

with open("table.txt", "w") as f:
    for item in multiplication_table:
        f.write(f"table of {n}: {n} x {multiplication_table.index(item) + 1} = {item}\n")