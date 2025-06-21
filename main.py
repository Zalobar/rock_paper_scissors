import random, sys

# tracking variables
wins = 0
losses = 0
ties = 0

# main game loop
while True:
    print(f"{wins}, {losses}, {ties}")

    # player input loop
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        player_move = print(input("> "))
        if player_move == "q":
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
        print("You must type r, p, s, or q.")

    # game loop
    
    # display player choice
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("PAPER versus...")

    # display computer choice
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = "r"
        print("ROCK")
    elif move_number == 2:
        computer_move = "p"
        print("PAPER")
    elif move_number == 3:
        computer_move = "s"
        print("SCISSORS")

    # Calculate and display Wins, Losses, and Ties
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == "r" and computer_move == "s":
        print("You win!")
        wins += 1
    elif player_move == "p" and computer_move == "r":
        print("You win!")
        wins += 1
    elif player_move == "s" and computer_move == "p":
        print("You win!")
        wins += 1
    elif player_move == "r" and computer_move == "p":
        print("Sorry! You lose.")
        losses += 1
    elif player_move == "p" and computer_move == "s":
        print("Sorry! You lose.")
        losses += 1
    elif player_move == "s" and computer_move == "r":
        print("Sorry! You lose.")
        losses += 1
    