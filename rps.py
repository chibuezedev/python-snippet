import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

# get users input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

# get computer move
computer_choice = random.randint(0, 2)
print("computer chooses: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You chose a wrong number, you loose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice > user_choice:
    print("you lose")
elif computer_choice == user_choice:
    print("Tie game, play again")
