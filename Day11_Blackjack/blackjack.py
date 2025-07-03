import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal_card( card,n):
    card.extend(random.choices(cards, k=n))
    while sum(card) > 21 and 11 in card:
        card[card.index(11)]=1

    return


def game():
    comp_card = []
    user_card = []
    while True:
        deal_card(comp_card, 2)
        deal_card(user_card, 2)

        if 11 in comp_card and 10 in comp_card :
            print("Black jack computer wins")
            break

        elif 11 in user_card and 10 in user_card :
            print("Black jack user wins")
            break

        while True:

            print("computer first card: " + str(comp_card[0]))
            print("user card:"+str(user_card))
            print("user score: "+str(sum(user_card)))
            if sum(user_card) > 21:
                print("you have gone over 21.")

                break
            another = input("do u want another card: y or n \n")
            if another == "y":
                deal_card(user_card, 1)
            else:
                while sum(comp_card) <= 16:
                    deal_card(comp_card, 1)
                break
        if sum(comp_card) > sum(user_card):
            print("computer win")
        elif sum(comp_card) < sum(user_card):
            print("user win")
        else:
            print("Its a tie")

        print("computer's hand:" + str(comp_card))
        print("computer's score:" + str(sum(comp_card)))
        print("user's hand:" + str(user_card))
        print("user's score:" + str(sum(user_card)))

        break

    return

while True:
    game()

    ask=input("do you want to play again?: y or n")
    if ask=="n":
        break