"""
Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.
"""
import random

player_score = 0
computer_score = 0
limit = 5
computer = ["rock", "scissors", "paper"]

for play in range(limit):
    # to check if there is equality
    player_hand = input("input your hand: ")
    computer_hand = random.choice(computer)
    if player_hand == "rock" and computer_hand == "rock":
        print(f"computer choice: {computer_hand}")
        print("equal")
    elif player_hand == "scissors" and computer_hand == "scissors":

        print(f"computer choice: {computer_hand}")
        print("equal")
    elif player_hand == "paper" and computer_hand == "paper":
        print(f"computer choice: {computer_hand}")
        print("equal")
        # checking for the competition
    elif player_hand == "rock" and computer_hand == "scissors":
        print(f"computer choice: {computer_hand}")
        player_score += 1
        print("players win")
    elif player_hand == "scissors" and computer_hand == "paper":
        print(f"computer choice: {computer_hand}")
        computer_score += 1
        print("computer win")
    elif player_hand == "paper" and computer_hand == "rock":
        print(f"computer choice: {computer_hand}")
        player_score += 1
        print("player wins")
    elif computer_hand == "rock" and player_hand == "scissors":
        print(f"computer choice: {computer_hand}")
        computer_score += 1
        print("computer wins")
    elif computer_hand == "scissors" and player_hand == "paper":
        print(f"computer choice: {computer_hand}")
        computer_score += 1
        print("computer wins")
    elif computer_hand == "paper" and "rock":
        print(f"computer choice: {computer_hand}")
        computer_score += 1
        print("computer wins")

# deciding the winning individual
if player_score > computer_score:
    print("player won")
    print()
    print("computer lost")
elif computer_score > player_score:
    print("computer win")
    print()
    print("player lost")
else:
    print("the game ended draw")




