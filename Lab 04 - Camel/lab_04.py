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

        elif user_choice.upper() == "E":
            print()
            print("Miles traveled: ", miles_traveled )
            print("Drinks in canteen: ", drinks )
            print("The natives are", miles_traveled - natives_traveled, "miles behind you." )
            print()

        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print()
            print("Your camel got some rest, it's happy!")
            natives_traveled += random.randrange (7, 15)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you.")
            print()

        elif user_choice.upper() == "C":
            new_miles_traveled = random.randrange(10, 21)
            miles_traveled += new_miles_traveled
            new_natives_traveled = random.randrange(7, 15)
            natives_traveled += new_natives_traveled
            print()
            print("You traveled", new_miles_traveled, "miles.")
            print("The natives are", new_natives_traveled, "miles behind you.")
            print()
            camel_tiredness += random.randrange (1, 4)
            thirst_level += 1
            oasis = random.randrange (20)
            if oasis == 13:
                thirst_level = 0
                camel_tiredness = 0
                drinks = 4
                print("You have found an oasis!")

        elif user_choice.upper() == "B":
            two_new_miles_traveled = random.randrange(5, 13)
            new_miles_traveled += two_new_miles_traveled
            two_new_natives_traveled = random.randrange(7, 15)
            new_natives_traveled += two_new_natives_traveled
            print()
            print("You traveled", two_new_miles_traveled, "miles.")
            print("The natives are", two_new_natives_traveled, "miles behind you")
            print()
            thirst_level += 2

        elif user_choice.upper() == "A":
            print()
            if drinks >= 1:
                print("You took a drink from your canteen.")
                thirst_level = 0
            else:
                print("You have no more ")

        elif thirst_level >= 6:
            print("Oh no! You have died of thirst!")
            done = True

        if not done and thirst_level > 4 and thirst_level < 6:
            print()
            print("You are thirsty.")
            print()

        if not done and camel_tiredness > 5 and camel_tiredness < 8:
            print("Your camel is getting pretty tired.")

        elif not done and camel_tiredness > 8:
            print("Your camel was too tired and died!")
            done = True

        if not done and two_new_natives_traveled >= two_new_miles_traveled:
            print("The natives caught up to you!")

        elif not done and two_new_natives_traveled >= two_new_miles_traveled - 15:
            print("The natives are getting close!")

        if not done and two_new_miles_traveled >= 200:
            print("You made it across the desert, you win!")


main()