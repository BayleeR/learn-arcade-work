import random

def print_intro():
    print("Welcome to Camel!!")
    print()
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print()


def main():
    print_intro()

    miles_traveled = 0
    camel_tiredness = 0
    thirst_level = 0
    natives_traveled = -20
    drinks = 4


    done = False
    while not done:
        print("A. Drinkg from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        user_choice = user_choice.upper()
        if user_choice == "Q":
            done = True
            print("You have quit the game, thanks for playing!")
        elif user_choice == "E":
            print()
            print("Miles traveled: ", miles_traveled )
            print("Drinks in canteen: ", drinks )
            print("The natives are", miles_traveled - natives_traveled, "miles behind you." )
            print()
        elif user_choice == "D":
            camel_tiredness = 0
            print()
            print("Your camel got some rest, it's happy!")
            print()
            natives_traveled += random.randrange (7, 14)



main()