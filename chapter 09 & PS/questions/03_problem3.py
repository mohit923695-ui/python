'''Write a program to generate multiplication tables from 2 to 20 and save each table in a different file inside a folder.'''

import os


def genretetable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    genretetable(i)         

