# import random

# options = ("rock","paper","scissors")

# playing = True

# while playing:

#     player = None
#     computer = random.choice(options)

#     while player not in options and player != "exit":
#         player = input("Choose betwwen (rock, paper, scissors) or 'exit' to quit: ").lower()

#         if player == "exit":
#             print("Ending game....")
#             playing == "false"
#             break

#         print(f"Player: {player}")
#         print(f"Computer: {computer}")


#         if player == computer:
#             print("It's a tie")
#         elif player == "paper" and computer == "rock":
#             print("You win")
#         elif player == "rock" and computer == "scissors":
#             print("You win")
#         elif player == "scissors" and computer == "paper":
#             print("You win")
#         else:
#             print("Computer wins")

#         if not input("Play again? (y/n): ").lower() == "y":
#             playing == "false"
        
# print("Thanks for playing!")

import random

options = ("rock", "paper", "scissors")

playing = True

while playing:
    computer = random.choice(options)
    player = input("Choose between (rock, paper, scissors) or 'exit' to quit: ").lower()

    if player == "exit":
        print("Ending game....")
        playing = False
        break

    if player not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif (player == "paper" and computer == "rock") or \
         (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper"):
        print("You win")
    else:
        print("Computer wins")

    if input("Play again? (y/n): ").lower() != "y":
        playing = False

print("Thanks for playing!")
