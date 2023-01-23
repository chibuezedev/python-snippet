# function and while loop

current_level = 0
final_level = 5

game_completed = True

while current_level <= final_level:
    if game_completed:
        print("you current level is", current_level)
        current_level += 1
print('Level End')


number = 0
while number <= 3:
    print('in loop')
    number += 1
else:
    print('outside loop')
