'''
the game() function in a program lets a user play a game and return the score as an integer .
you neeed to read a file 'hi-score.txt' which is either blank or contains the previos hi-score .
you need to write a program to update the hi-score whehter the game() function breaks the hi-score. 
'''

import random


def game():
    print("you are playing the game ...")
    score = random.randint(1,100)
    #fetch hiscore 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your hiscore :{score} ")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f :
            f.write(str(score))

    return score

game()            

            
