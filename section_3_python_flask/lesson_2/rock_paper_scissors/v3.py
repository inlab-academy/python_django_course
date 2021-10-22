from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"PLayer Score: {player_wins} Computer Score {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player = input("(Enter your choice): ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0, 2)
    if (rand_num == 0):
        computer = "rock"
    elif (rand_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("PLayer wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("PLayer win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("PLayer win!")
            player_wins += 1
    else:
        print("PLease enter a valid move!")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S a tie!")
else:
    print("OH NO :( THE COMPUTER WON...")


# if player1 == player2:
#     print("It's a tie")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("player1 wins!")
#     elif player2 == "paper":
#         print("player2 wins")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("player1 wins!")
#     elif player2 == "scissors":
#         print("player2 wins")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("player1 wins!")
#     elif player2 == "rock":
#         print("player2 wins!")
# else:
#     print("Something went wrong")
