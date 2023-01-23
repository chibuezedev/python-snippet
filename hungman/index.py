import random

word_list = ['avocado', 'apple', 'orange']

chosen_word = random.choice(word_list)

print(f'Passt, the solution is {chosen_word}')

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)

end_game = False
while not end_game:
    guess = input("Guess a number: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print("You win")





