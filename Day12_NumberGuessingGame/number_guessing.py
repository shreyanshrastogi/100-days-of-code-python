import os
import random

from art import logo


#game happens in this
def game():
    #uses ternary operator to clear the screen
    # 'nt' is the os name for Windows; 'cls' is used for clearing the Windows screen, and 'clear' for Linux/Mac.
    os.system("cls" if os.name=="nt" else "clear")
    print(logo)
    #generating random number

    print("I'm thinking of a number between 1 to 100.")
    rand_num=random.randint(1,100)
    difficulty=input("""do you want "easy" or "hard" difficulty:""").strip().lower()
    #check if the user has entered correct string or not
    while difficulty not in ["easy","hard"]:
        difficulty = input("""do you want "easy" or "hard" difficulty:""").strip().lower()

        #allocating chances according to difficulty

    if difficulty=="easy":
        chances=10
    else:
        chances=5
    #asking the number from gamer till chances are 0.

    for i in range(1,chances+1):
        #checks if the user has entered an integer
        while True:
            number=input("guess the number:").strip()
            if number.isdigit():
                number=int(number)
                break
            else:
                print("please enter valid digit")
        #checking the number is greater less or equal to generated number.
        if number==rand_num:
            print(f"Congrats {number} is the correct number.")
            print(f"you won the game with {chances-i} chances left.")
            return

        elif number<rand_num:
            print("too low.")
            print(f"you have {chances-i} chances left.")

        else:
            print("too high.")
            print(f"you have {chances-i} chances left.")
        #to check if user has lost the game.
        if i == chances:
            print("You have lost the game.")
            print("the number was " + str(rand_num))
            return




while True:
    game()
    repeat=input("do you want to play again? 'yes' or 'no':").strip().lower()
    while repeat not in ["yes","no"]:
        repeat=input("please enter valid 'yes' or 'no'.")

    if repeat=="no":
        break