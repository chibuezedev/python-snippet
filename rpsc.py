

# The main function
if __name__ == '__main__':

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"}

    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    # Win-lose matrix for new version of the game
    rpsls_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

    name = input("Enter your name: ")

    # The GAME LOOP
    while True:

        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Which version of Rock-Paper-Scissors?")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 3 to quit")
        print()

        # Try block to handle the player choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")
            continue

        # Play the traditional version of the game
        if choice == 1:
            rps()

        # Play the new version of the game
        elif choice == 2:
            rpsls()

        # Quit the GAME LOOP
        elif choice == 3:
            break

        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")
