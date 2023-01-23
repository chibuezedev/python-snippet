import random
print("Welcome to Coin toss, Choose a number to make a toss")


random_number = random.randint(0, 1)

if random_number == 1:
    print("Head")
else:
    print("Tail")
