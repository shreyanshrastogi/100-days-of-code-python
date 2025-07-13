import os
import random

import art
from game_data import data


def game():
    score=0
    acc_1=random.choice(data)
    while True:
        acc_2= random.choice(data)
        while acc_2 == acc_1:
            acc_2 = random.choice(data)
        os.system("cls" if os.name=='nt' else "clear")
        print(art.logo)


        print(f"{acc_1['name']}, a {acc_1['description']}, from {acc_1['country']} ")

        print(art.vs)

        print(f"{acc_2['name']}, a {acc_2['description']}, from {acc_2['country']} ")

        choose=input("Choose 'A' or 'B': ").lower()
        if choose=='a':
            if acc_1['follower_count']>=acc_2['follower_count']:
                score=score+1
                print("you win!")
                print("Your score:", score)



            else:
                print("you lose!")
                print("Your score:", score)
                break


        else:
            if acc_1['follower_count'] <= acc_2['follower_count']:
                score=score+1
                print("you Win!")
                print("Your score:", score)
                acc_1=acc_2
            else:
                print("you lose!")
                print("Your score:",score)
                break


game()