print("welcome to treasure island")
print("your mission is to find the treasure")
choice1: str = input('You\'re at the crossover, where do you want to go? type "left" or "right"\n').lower()

if choice1 == 'left':
    choice2 = input('you\'ve come to the lake. There is an island in the middle of the lake. type "wait" '
                    'to wait for a boat or "swim" to go across\n').lower()
    if choice2 == 'wait':
        choice3 = input("you arrived at the island unharmed there is a house with 3 doors, one red, yellow and blue. "
                        "which do you want to choose\n").lower()
        if choice3 == 'red':
            print("its a room of fire, game over!")
        elif choice3 == 'blue':
            print("its a room of beasts, game over!")
        elif choice3 == 'yellow':
            print("You found the treasure, you won.")
        else:
            print("you choose a wrong door, sorry!")
    else:
        print("opps! game over, try again!")
else:
    print("you failed into a rabbit hole, try again!")
